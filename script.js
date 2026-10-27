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
