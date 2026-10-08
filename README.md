# STELLAR Lab self-hosted website

This folder is a complete static replacement for the former Google Sites website. It uses plain HTML, CSS and a very small amount of JavaScript. There is no framework, database, cookie banner, external font, image CDN or build step.

## Preview locally

From this folder, run:

    python3 -m http.server 8000

Then open `http://localhost:8000/`. You can also open `index.html` directly in a browser.

## Deploy

Upload the *contents of this folder* to any static host (GitHub Pages, GitLab Pages, Netlify, Cloudflare Pages, university web space, Apache or Nginx). `index.html` is the site entry point.

For GitHub Pages, push this folder to a repository and publish the repository root. For Netlify/Cloudflare Pages, use this folder as the publish directory and leave the build command empty.

## Edit the site

- Global styles: `assets/css/site.css`
- Mobile menu and publication filter: `assets/js/site.js`
- Local artwork/logo: `assets/img/`
- Main pages: root `.html` files
- Project and resource pages: `projects/`

The HTML already uses relative URLs, so it can be hosted under a subdirectory as well as at a domain root.

## Before launch

1. Replace `YOUR-DOMAIN.example` in `sitemap.xml` with the real domain.
2. Review `positions.html`: the migrated postdoc advert includes a priority date that has already passed.
3. The approved homepage concept artwork and the lab branding are stored locally in `assets/img/`; no image depends on Google Sites.
4. Add analytics only if you actually want it; none is included now.

## Content provenance

The structure and research content were migrated from the STELLAR Lab's public Google Site in October 2026 and rewritten for a cleaner self-hosted presentation.
