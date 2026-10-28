# Access Curriculum & Technology

A dependency-free static website for Access's computing course-development services, offered by Alex Shaw and Baha Marupov. No build step, external fonts, analytics, or services are required.

## Core message and structure

Alex Shaw and Baha Marupov are each software professionals and college educators who help colleges **modernize existing computing courses or create new ones**. The first screen states that offer and gives both names equal prominence. Keep future changes focused on this message.

The homepage has four destinations: **Services**, **Experience**, **Course example**, and **Contact Alex**. Services opens with the origin story: teaching at colleges showed Alex and Baha how course updates compete with teaching and student support for faculty time as technology changes. Access helps with that work through the two course-development services. Compensation differences appear only as supporting context. Experience introduces both people; named organizations describe Alex's individual work history. The course example demonstrates teaching materials; the interactive curriculum map lives on that separate page. Contact repeats the two services and provides Alex's email and a one-page overview.

Use professional, everyday language and company voice ("we") for services. Keep the story within the Services introduction, without adding another navigation item or large section. Both people have confirmed software and college teaching experience; do not invent additional credentials for either person.

## Preview and hosting

Run `python tools/preview.py` and visit `http://127.0.0.1:8765`. The preview binds only to loopback and serves an explicit list of public site assets; it does not expose directory listings, Git data, or tooling. Stop it with Ctrl+C when finished. The static pages also support opening directly in a browser outside the automated preview workflow.

The live site is [GitHub Pages](https://alexandergshaw.github.io/curriculum-and-technology-services-website/). Completed changes are committed and pushed to `main`; verify the published content after pushing. To use another static host, upload `index.html`, `curriculum-sample.html`, `styles.css`, `sample.css`, `script.js`, `favicon.svg`, `downloads/`, and `output/pdf/` together, keeping relative paths intact. `tools/` and `output/previews/` are local development resources and are not needed on the host.

## Editing

- **`index.html`**: core message, two services, professional experience, course-example introduction, and contact.
- **`styles.css`**: shared forest-green, warm-paper, and lime visual system; homepage layouts; responsive behavior; accessible focus and print styles.
- **`curriculum-sample.html` / `sample.css`**: illustrative curriculum map, interactive outcome explorer, rubric, and faculty handoff notes. The full table remains available without JavaScript and in print. Keep the sample consistent with `downloads/illustrative-curriculum-map.csv`.
- **`script.js`**: optional clipboard support, keyboard-accessible outcome selection, gentle entrance motion, active-section navigation, and sticky-header sizing. Content is visible by default. Reduced-motion preferences disable animation. The header is static on small phones.
- **Curriculum explorer**: three radio choices correspond to P1/P2/P3 and their introduction, reinforcement, and demonstration levels. P3 is not directly assessed in Module 1, introduced in Module 2, and demonstrated in Module 3. Controls appear only after the listener is ready; evidence updates use a polite live region.
- **Email and brand**: update both HTML files and `tools/build_capabilities.py`, then regenerate the PDF. The public address is `alexandergshaw@gmail.com`; replace it only with a working address. The copy button reads the visible address.
- **`output/pdf/access-capabilities.pdf`**: one-page service overview with the same two offers, experience, faculty collaboration, and contact. Rebuild with `python tools/build_capabilities.py` using ReportLab, then render and inspect the PDF. Equivalent information appears in HTML.

Affiliations describe Alex's individual experience, not business clients or institutional endorsements. Keep proposed work labeled as proposed. The public course example is an illustration, not an institutional assignment or evidence of student results. Add only real, permission-cleared artifacts or testimonials. Faculty set grading thresholds and approve course decisions. Schedules, fees, and deliverables are agreed during scoping; do not invent commitments.

Supply the actual public domain before adding canonical links, `og:url`, social-image URLs, or domain-dependent structured data.

## Manual checks

There is no build pipeline or test framework. Inspect both pages at 320px, 375px, 768px, and 1440px. Confirm the offer and both professional backgrounds are clear before following the navigation: services → experience → course example → contact. Check the sample's radio controls with pointer and keyboard, the horizontally scrollable table, CSV and PDF downloads, email destinations, clipboard feedback, skip link, anchor offsets, and browser errors. Verify reduced-motion and no-JavaScript readability. Print the sample with its complete table and rubric; the interactive map is omitted from print because the table provides the full information.
