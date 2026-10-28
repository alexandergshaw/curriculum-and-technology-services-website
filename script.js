"use strict";

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

let printDisclosureStates;

window.addEventListener("beforeprint", () => {
  if (printDisclosureStates) return;
  printDisclosureStates = Array.from(document.querySelectorAll("details"), (detail) => ({
    detail,
    open: detail.open,
  }));
  printDisclosureStates.forEach(({ detail }) => { detail.open = true; });
});

window.addEventListener("afterprint", () => {
  if (!printDisclosureStates) return;
  printDisclosureStates.forEach(({ detail, open }) => { detail.open = open; });
  printDisclosureStates = undefined;
});

(() => {
  const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const revealItems = Array.from(document.querySelectorAll("[data-reveal]"));

  if (!("IntersectionObserver" in window)) {
    revealItems.forEach((el) => el.classList.add("is-visible"));
  } else {
    document.querySelectorAll("[data-reveal-stagger]").forEach((group) => {
      Array.from(group.querySelectorAll("[data-reveal]")).forEach((el, index) => {
        el.style.transitionDelay = `${index * 90}ms`;
      });
    });
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        revealObserver.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -12% 0px", threshold: 0.12 });
    revealItems.forEach((el) => revealObserver.observe(el));
  }

  const navLinks = Array.from(document.querySelectorAll('.site-header nav a[href^="#"]'));
  const linkForSection = new Map();
  navLinks.forEach((link) => {
    const section = document.getElementById(link.getAttribute("href").slice(1));
    if (section) linkForSection.set(section, link);
  });
  if ("IntersectionObserver" in window && linkForSection.size) {
    const navObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        const link = linkForSection.get(entry.target);
        if (!link || !entry.isIntersecting) return;
        navLinks.forEach((other) => other.classList.remove("is-active"));
        link.classList.add("is-active");
      });
    }, { rootMargin: "-45% 0px -50% 0px", threshold: 0 });
    linkForSection.forEach((link, section) => navObserver.observe(section));
  }

  const header = document.querySelector(".site-header");
  const progressBar = document.querySelector(".scroll-progress-bar");
  let ticking = false;
  const update = () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    if (header) header.classList.toggle("is-scrolled", scrollTop > 8);
    if (progressBar && !prefersReduced) {
      const scrollable = document.documentElement.scrollHeight - window.innerHeight;
      const ratio = scrollable > 0 ? Math.min(1, scrollTop / scrollable) : 0;
      progressBar.style.transform = `scaleX(${ratio})`;
    }
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
