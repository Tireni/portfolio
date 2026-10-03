# Enoch Benson — professional portfolio

A static, accessible portfolio for development, application support, testing, implementation and systems roles. Includes five case studies and a supplied resume. Company work is distinguished from the BANT product, which is in development.

## Edit and preview

Edit `content.json` for contact details, project content, the canonical origin and the resume filename. Edit `scripts/build.mjs` for page sections and `assets/style.css` for presentation.

Run `npm run build`, then `npm start`. Open http://127.0.0.1:4173. No JavaScript packages are needed to build or serve the site. Node.js and Python are required locally. The published pages work without JavaScript; only the mobile menu uses JavaScript.

Place a replacement resume in `assets/Enoch-Benson-Resume.pdf` and rebuild. The resume download uses the provided PDF rather than a generated document.

## Publish

Push to `main`; the GitHub Actions workflow builds the static pages and deploys `dist` to GitHub Pages. The public URL is https://tireni.github.io/portfolio/.

## Content and image notes

The employment and contribution descriptions come from Enoch's brief. Public websites provide project context, not proof of individual ownership. No project-specific languages, architecture, usage figures, revenue, performance improvements or awards are inferred.

- N-Alerts: supplied public mobile complaint screen and public website context.
- NFEC: supplied public website screenshot. Automated access to fire.ng returned HTTP 406 during research; description relies on the brief and supplied public screenshot.
- BOOSTAR: supplied public website screenshot and public website context.
- NFDRC: supplied images were labelled NFEC, so they are omitted. nfdrc.ng had a certificate error during verification. Its description relies on the brief, and its original public link is retained.
- BANT: typography presents the product concept; it is not a fabricated application screenshot. The demo is linked and the MVP is clearly marked in development.

Authenticated dashboard screenshots, operational data and company source code are not included in this repository. Branding and project assets belong to their respective owners. Only the selected public visuals and the explicitly supplied resume are published.

## Verification

`npm test` checks every page at mobile and desktop widths, navigation targets, asset loading, the mobile menu, metadata, resume delivery and accessibility using Playwright. Install the Python Playwright package and Chromium if they are not already available: `python -m pip install playwright` and `python -m playwright install chromium`. Tests start and stop their own local server. Test screenshots and results remain untracked.
