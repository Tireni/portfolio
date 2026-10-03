"""End-to-end checks for the actual generated portfolio, with no server left behind."""
from pathlib import Path
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
from threading import Thread
from urllib.parse import urlparse, unquote
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
RESULTS = ROOT / 'test-results'
RESULTS.mkdir(exist_ok=True)
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass

server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(DIST)))
Thread(target=server.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{server.server_port}'
pages = ['index.html'] + [f'case-studies/{slug}.html' for slug in ['boostar', 'nfec', 'nalerts', 'nfdrc', 'bant']]
errors = []
checks = []
try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for size in [(1440, 1000), (390, 844), (320, 740)]:
            context = browser.new_context(viewport={'width': size[0], 'height': size[1]}, device_scale_factor=1)
            page = context.new_page()
            page.on('pageerror', lambda error: errors.append(str(error)))
            for route in pages:
                response = page.goto(f'{base}/{route}', wait_until='networkidle')
                assert response.status == 200, route
                assert page.locator('h1').count() == 1, route
                assert page.title() and page.locator('meta[name="description"]').get_attribute('content'), route
                assert page.locator('meta[property="og:title"]').get_attribute('content') == page.title(), route
                assert page.locator('main').count() == 1
                assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'), f'Horizontal overflow: {route} {size}'
                for img in page.locator('img').all():
                    img.scroll_into_view_if_needed()
                    img.evaluate('(el) => el.decode()')
                page.evaluate('window.scrollTo(0, 0)')
                page.wait_for_timeout(100)
                assert page.evaluate('Array.from(document.images).every(img => img.complete && img.naturalWidth > 0)'), f'Broken image: {route}'
                ids = page.locator('[id]').evaluate_all('(els) => els.map(el => el.id)')
                assert len(ids) == len(set(ids)), f'Duplicate IDs: {route}'
                for link in page.locator('a[href]').evaluate_all('(els) => els.map(el => ({href:el.getAttribute("href"),target:el.getAttribute("target"),rel:el.getAttribute("rel")}))'):
                    href = link['href']
                    parsed = urlparse(href)
                    if parsed.scheme in ['http', 'https']:
                        assert link['target'] == '_blank' and 'noopener' in link['rel'], href
                    elif not parsed.scheme:
                        if not parsed.path:
                            if parsed.fragment:
                                assert parsed.fragment in ids, f'Broken anchor: {route} {href}'
                        else:
                            target = (DIST / route).parent / unquote(parsed.path)
                            assert target.exists(), f'Missing link destination: {route} {href}'
                            if parsed.fragment:
                                assert f'id="{parsed.fragment}"' in target.read_text(encoding='utf-8'), href
                for asset in page.locator('[src],link[rel="stylesheet"],link[rel="icon"]').evaluate_all('(els) => els.map(el=>el.getAttribute("src")||el.getAttribute("href"))'):
                    assert ((DIST / route).parent / asset).exists(), f'Missing asset: {asset}'
                if size[0] < 700:
                    toggle = page.get_by_role('button', name='Menu')
                    assert toggle.is_visible()
                    toggle.click()
                    assert toggle.get_attribute('aria-expanded') == 'true'
                    assert page.get_by_role('navigation').is_visible()
                    page.keyboard.press('Escape')
                    assert toggle.get_attribute('aria-expanded') == 'false'
                    toggle.click()
                    page.get_by_role('navigation').get_by_role('link', name='Work', exact=True).click()
                    assert toggle.get_attribute('aria-expanded') == 'false'
                    page.goto(f'{base}/{route}', wait_until='networkidle')
                if route == 'index.html':
                    assert page.get_by_role('link', name='enochbenson61@gmail.com').count() == 1
                    assert page.locator('.availability').first.inner_text() == 'Open to Remote Opportunities'
                    assert page.locator('.development').inner_text() == 'In Development'
                    with page.expect_download() as download_info:
                        page.get_by_role('link', name='Download Resume').first.click()
                    assert download_info.value.suggested_filename.endswith('.pdf')
                if route == 'case-studies/bant.html':
                    assert 'MVP — In Development' in page.inner_text('main')
                elif route != 'index.html':
                    assert 'professional work' in page.inner_text('main').lower()
                if size[0] in [1440, 390]:
                    page.screenshot(path=str(RESULTS / f'{Path(route).stem}-{size[0]}.png'), full_page=True)
                checks.append({'page': route, 'width': size[0], 'result': 'passed'})
            context.close()
        browser.close()
    assert not errors, errors
    assert (DIST / 'assets/Enoch-Benson-Resume.pdf').read_bytes().startswith(b'%PDF')
    report = {'checks': checks, 'browser_errors': errors, 'result': 'passed'}
    (RESULTS / 'report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(f'Passed: {len(checks)} page/viewport checks, all local links/assets, mobile navigation, resume download and browser runtime.')
finally:
    server.shutdown()
    server.server_close()
