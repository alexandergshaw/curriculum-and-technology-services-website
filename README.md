# Access Curriculum & Technology

A complete, dependency-free static website. No build step, external fonts, analytics, or services are required.

## Preview and hosting

Open `index.html` directly in a browser. For a local HTTP preview, run `python tools/preview.py` and visit `http://127.0.0.1:8765`. The preview binds only to loopback and serves an explicit list of public site assets; it does not expose directory listings, Git data, or tooling. Stop it with Ctrl+C when finished.

Upload `index.html`, `curriculum-sample.html`, `styles.css`, `sample.css`, `script.js`, `favicon.svg`, `downloads/`, and `output/pdf/` together to any ordinary static host. Keep their relative paths intact; the site works at a domain root or a repository subdirectory. No deployment or account connection is configured here. `tools/` and `output/previews/` are local development resources and are not needed on the host.

## Editing

- **`index.html`**: main-page copy, navigation, service descriptions, professional experience, and the example course-review engagement.
- **`curriculum-sample.html` / `sample.css`**: the full illustrative curriculum map, rubric, and faculty handoff notes. This page works without JavaScript and has print styles. Keep outcome codes and module descriptions consistent with `downloads/illustrative-curriculum-map.csv`.
- **Email and brand**: update both HTML files and `tools/build_capabilities.py`, then regenerate the PDF. The current public address is `alexandergshaw@gmail.com`; replace it only with a working address. The copy button reads the visible email and has no separate address setting.
- **`styles.css`**: the forest-green, warm-paper, and lime visual system; system typography with serif accents; the interactive diagram, alignment matrix, responsive layouts, and print rules. No external images, fonts, or animation dependencies are required.
- **Curriculum explorer**: `script.js` maps the three radio choices to P1/P2/P3 and their introduction, reinforcement, and demonstration levels. Keep these mappings aligned with the full sample and CSV. Controls appear only after the listener is ready; without JavaScript, the P1 diagram and the full sample link remain available. Native radios support keyboard arrow navigation, and evidence updates use a polite live region. Motion respects the reduced-motion setting.
- **`script.js`**: optional clipboard enhancement, print disclosure-state preservation, and progressive scroll enhancements (entrance motion, active-section navigation, a sticky-header shadow, and a scroll-progress indicator). Content is visible by default, including when the script is blocked or fails. Entrance motion only starts after an element is observed; it never hides content and is disabled under `prefers-reduced-motion` and in print. Modern browsers also expand disclosure content through print CSS. The header remains in normal document flow on small screens.
- **`favicon.svg`**: local brand icon. The footer copyright year is maintained in HTML.
- **`output/pdf/access-capabilities.pdf`**: a one-page overview for internal sharing. Rebuild with `python tools/build_capabilities.py` in an environment with ReportLab installed. Keep its service descriptions, experience, and contact details in sync with the main page; render and inspect the regenerated PDF before release. Equivalent information is available in the main page's HTML.

To add evidence, obtain permission for the specific artifact, attribution, and public use first. Remove student identities and confidential information. Distinguish Alex's individual experience from business engagements; retain “Course proposal” for unimplemented designs. The expanded activities and full curriculum sample are newly authored illustrations, not institutional assignments, student submissions, or evidence of measured results. The sample's rubric weights and performance levels are illustrative; local faculty set grading thresholds. Add only real, permission-cleared artifacts or testimonials, and verify any new links.

## Review before release

- Confirm the final public/legal brand; the current public name omits a legal suffix.
- Retain or replace the public email address and check all contact links.
- Review factual copy, professional affiliations, and publication permissions.
- The course-review engagement is an example; its schedule, fee, and review windows are established in a written proposal. Do not add assumed timelines, client results, or testimonials.
- Supply the real domain before adding canonical links, `og:url`, social-image URLs, or domain-dependent structured data.

## Manual checks

There is no test framework or website build pipeline. Check both pages at 320px, 375px, 768px, and 1440px: select each explorer outcome → open the full sample → editable map download → example engagement → capabilities PDF → correct email. P3 should show no direct assessment in Module 1, introduction in Module 2, and demonstration in Module 3. Verify keyboard radio navigation, the visible skip link and focusable main target, case-study disclosures and proposal labels, the sample table's horizontal scrolling, narrow-screen/zoom reflow, no-JavaScript navigation, blocked-script visibility, and browser console/network errors. Preview printing with samples expanded and navigation controls hidden; verify disclosure states are restored afterward. Check clipboard messages without sending email.
