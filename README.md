# Access Curriculum & Technology

A complete, dependency-free static website. No build step, external fonts, analytics, or services are required.

## Preview and hosting

Open `index.html` directly in a browser. For local HTTP preview, run `python3 -m http.server 8000` from this directory and visit `http://localhost:8000`.

Upload `index.html`, `styles.css`, `script.js`, and `favicon.svg` together to any ordinary static host. Keep their relative paths intact; the site works at a domain root or a repository subdirectory. No deployment or account connection is configured here.

## Editing

- **`index.html`**: all public copy, navigation, examples, and contact links. Search for `Access` to update the brand, including the page title, social metadata, wordmark, biography, footer, and accessible home-link label.
- **Email**: search `index.html` for `alexandergshaw@gmail.com` and replace every occurrence, including both plain and subject-bearing `mailto:` links. The copy button reads the visible email; it has no separate address setting.
- **`styles.css`**: colors and fonts in `:root`, responsive layouts, focus styles, and print rules.
- **`script.js`**: optional clipboard enhancement, print disclosure-state preservation, and progressive scroll enhancements (reveal-on-scroll transitions, active-section navigation, a sticky-header shadow, and a scroll-progress indicator). Content, navigation, native disclosures, and email links work without JavaScript; the `js` class gates all reveal styling, and reveals are disabled under `prefers-reduced-motion` and in print. Modern browsers also expand disclosure content through print CSS.
- **`favicon.svg`**: local brand icon. The footer copyright year is maintained in HTML.

To add evidence, obtain permission for the specific artifact, attribution, and public use first. Remove student identities and confidential information. Distinguish Alex's individual experience from business engagements; retain “Course proposal” for unimplemented designs. The expanded activities are newly authored illustrative samples, not institutional assignments or student submissions. Add only real, permission-cleared artifacts or testimonials, and verify any new links.

## Review before release

- Confirm the final public/legal brand; the current public name omits a legal suffix.
- Retain or replace the public email address and check all contact links.
- Review factual copy, professional affiliations, and publication permissions.
- Supply the real domain before adding canonical links, `og:url`, social-image URLs, or domain-dependent structured data.

## Manual checks

There is no test framework or build pipeline. Check the visitor journey at 375px, 768px, and 1440px: services → expanded sample → approach → correct email. Verify keyboard focus and disclosures, narrow-screen/zoom reflow, no-JavaScript navigation and email, and browser console/network errors. Preview printing with samples expanded and navigation controls hidden; verify disclosure states are restored afterward. Check the clipboard success and failure messages without sending email.