# Enoch Benson — Flutter mobile developer portfolio

Live site: https://tireni.github.io/portfolio/

A static, accessible portfolio positioning Enoch primarily as a **Flutter mobile app developer**, with complementary website, web-app, API and backend experience.

## Featured mobile work

- **BANT:** Personal student voice/social app (MVP in development).
- **BOOSTAR:** Public safety / emergency reporting mobile workflows (professional contribution).
- **N-Alerts:** Mobile safety reports and location-aware alert features (professional contribution).
- **NFDRC:** Mobile-accessible fire-data reporting, incident map and administration (professional contribution).
- **NFEC:** Complementary system, web and data-management experience.

Professional project contributions are distinguished from full product ownership. Screenshots of BANT, BOOSTAR, NFDRC and N-Alerts were provided for review in November 2026; newly provided screenshots have **not yet been uploaded into this repository**. Existing public project images remain in use until the supplied mobile screenshots are approved for public publication and added as image assets.

## Edit and preview

- Edit `content.json` for project copy, contact details and project order.
- Edit `scripts/build.mjs` for the static page templates and sections.
- Edit `assets/style.css` for styles.
- Run `npm run build`, then `npm start`. Open http://127.0.0.1:4173.

The static pages work without JavaScript; only the mobile menu and contact dialog require JavaScript. Node.js and Python are required for local tooling.

## Deployment

Push to `main` to trigger the GitHub Actions build and GitHub Pages deployment of `dist`. Public URL: https://tireni.github.io/portfolio/.

## Privacy and verification

Only publish mobile screen assets cleared for public use. Avoid private dashboards, operational coordinates, incident details, personal identifiers, source code or confidential organisational information. Project branding belongs to its respective owners.

`npm test` runs browser checks through Playwright after dependencies are installed.
