"use strict";

// This small explorer uses the same illustrative map as the full sample.
(() => {
  const explorer = document.querySelector(".curriculum-explorer");
  if (!explorer) return;
  const controls = explorer.querySelector(".outcome-controls");
  const code = explorer.querySelector("#outcome-code");
  const title = explorer.querySelector("#outcome-title");
  const evidence = explorer.querySelector("#outcome-evidence");
  const edition = explorer.querySelector(".panel-edition");
  const modules = Array.from(explorer.querySelectorAll("[data-module]"));
  const connections = Array.from(explorer.querySelectorAll("[data-connection]"));
  if (!controls || !code || !title || !evidence || !edition || modules.length !== 3) return;

  const outcomes = {
    implementation: {
      code: "P1", title: "Build & Test", edition: "01 / 03", levels: ["I", "R", "D"],
      evidence: "Working code and repeatable tests demonstrate that the application handles normal, empty, loading, and error states.",
    },
    judgment: {
      code: "P2", title: "Reason & Decide", edition: "02 / 03", levels: ["I", "R", "D"],
      evidence: "A design rationale explains the request flow, weighs technical choices, and documents responsible use of synthetic data.",
    },
    communication: {
      code: "P3", title: "Explain & Reproduce", edition: "03 / 03", levels: ["none", "I", "D"],
      evidence: "Setup instructions, an annotated demonstration, and verification notes let another person reproduce the work. Module 1 does not directly assess this outcome.",
    },
  };
  const levelNames = { I: "Introduced", R: "Reinforced", D: "Demonstrated", none: "Not assessed" };

  controls.addEventListener("change", (event) => {
    const input = event.target;
    if (!(input instanceof HTMLInputElement) || !input.checked) return;
    const outcome = outcomes[input.value];
    if (!outcome) return;
    explorer.dataset.outcome = input.value;
    code.textContent = outcome.code;
    title.textContent = outcome.title;
    edition.textContent = outcome.edition;
    modules.forEach((module, index) => {
      const level = outcome.levels[index];
      module.dataset.level = level;
      const badge = module.querySelector(".level-badge");
      badge.textContent = level === "none" ? "—" : level;
      badge.setAttribute("aria-label", levelNames[level]);
      module.querySelector(".level-name").textContent = levelNames[level];
      if (connections[index]) connections[index].dataset.muted = String(level === "none");
    });
    evidence.textContent = outcome.evidence;
  });
  // Never show controls before their interaction is ready.
  controls.hidden = false;
})();

const copyButton = document.querySelector(".copy-email");
const copyStatus = document.querySelector(".copy-status");
const emailLink = document.querySelector(".email-address");

if (copyButton && copyStatus && emailLink && navigator.clipboard && window.isSecureContext) {
  copyButton.hidden = false;
  copyButton.addEventListener("click", async () => {
    copyStatus.textContent = "";
    try {
      await navigator.clipboard.writeText(emailLink.textContent.trim());
      copyStatus.textContent = "Email address copied.";
    } catch {
      copyStatus.textContent = "Copy unavailable. Select the email address above to copy it.";
    }
  });
}

(() => {
  const navLinks = Array.from(document.querySelectorAll('.site-header nav a[href^="#"]'));
  const linkForSection = new Map();
  navLinks.forEach((link) => {
    const section = document.getElementById(link.getAttribute("href").slice(1));
    if (section) linkForSection.set(section, link);
  });
  const header = document.querySelector(".site-header");
  if (header && "ResizeObserver" in window) {
    new ResizeObserver(() => {
      document.documentElement.style.setProperty("--header-height", `${header.offsetHeight}px`);
    }).observe(header);
  }
  let ticking = false;
  const update = () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    if (header) header.classList.toggle("is-scrolled", scrollTop > 8);
    let activeLink;
    linkForSection.forEach((link, section) => {
      if (section.getBoundingClientRect().top <= window.innerHeight * .4) activeLink = link;
    });
    navLinks.forEach((link) => {
      link.classList.toggle("is-active", link === activeLink);
      if (link === activeLink) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
    ticking = false;
  };
  const onScroll = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(update);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  update();
})();
