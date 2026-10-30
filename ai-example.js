"use strict";

// A local teaching exercise using the same authored fixtures as the Python unit.
// No model calls, tracking, or visitor submissions.
(() => {
  const lab = document.querySelector("#answer-lab");
  if (!lab) return;
  const selector = lab.querySelector("#case-select");
  const controls = lab.querySelector("#decision-controls");
  const feedback = lab.querySelector("#case-feedback");
  const status = lab.querySelector("#lab-status");
  const choices = { accept: "Accept", revise: "Revise", refer: "Refer to a person" };
  // Format interface headings only; quoted source titles and teaching text stay verbatim.
  const titleCaseLabel = (label) => {
    const words = label.split(" ");
    return words.map((word, index) => index > 0 && index < words.length - 1
      && /^(a|an|and|as|at|but|by|for|in|nor|of|on|or|per|the|to|via|with)$/i.test(word)
      ? word.toLowerCase() : word.charAt(0).toUpperCase() + word.slice(1)).join(" ");
  };
  let data;
  let current;
  const findSource = (id, version) => data.documents.find((item) => item.id === id && item.version === version);
  const setText = (id, value) => { lab.querySelector(`#${id}`).textContent = value; };

  const showCase = (id, announce = true) => {
    current = data.cases.find((item) => item.id === id);
    if (!current) return;
    setText("case-title", titleCaseLabel(current.label));
    setText("case-question", current.question);
    setText("case-count", `${String(data.cases.indexOf(current) + 1).padStart(2, "0")} / ${String(data.cases.length).padStart(2, "0")}`);
    const baseline = findSource(current.baseline_source.id, current.baseline_source.version);
    setText("baseline-answer", baseline.text);
    setText("model-answer", current.response.text);
    setText("answer-citations", current.response.citations.length
      ? `Cites: ${current.response.citations.map((citation) => `${citation.source_id} · v${citation.version}`).join(", ")}`
      : "No sources cited; response declines to answer.");
    setText("fallback-decision", `Instructor Judgment: ${titleCaseLabel(choices[current.expected_decision])}`);
    setText("fallback-explanation", `${current.explanation} ${current.alternative_judgment}`);
    const sources = lab.querySelector("#case-sources");
    sources.replaceChildren();
    const visibleSources = [findSource(current.source_id, current.source_version)];
    current.response.citations.forEach((citation) => {
      const source = findSource(citation.source_id, citation.version);
      if (!visibleSources.includes(source)) visibleSources.push(source);
    });
    visibleSources.forEach((source) => {
      const article = document.createElement("article");
      const heading = document.createElement("h4");
      const meta = document.createElement("p");
      const excerpt = document.createElement("p");
      heading.textContent = source.title;
      meta.className = "source-meta";
      meta.textContent = `${source.id} · v${source.version} · ${source.status}`;
      excerpt.textContent = source.text;
      article.append(heading, meta, excerpt);
      sources.append(article);
    });
    controls.querySelectorAll("input").forEach((input) => { input.checked = false; });
    feedback.hidden = true;
    status.textContent = announce ? `Loaded ${current.label}. Review the sources and choose a decision.` : "";
  };

  lab.querySelector("#review-decision").addEventListener("click", () => {
    if (!current) return;
    const selected = controls.querySelector("input:checked")?.value;
    if (!Object.hasOwn(choices, selected)) {
      status.textContent = "Choose accept, revise, or refer before comparing your reasoning.";
      controls.querySelector("input").focus();
      return;
    }
    setText("feedback-title", `Instructor Judgment: ${titleCaseLabel(choices[current.expected_decision])}`);
    setText("feedback-choice", selected === current.expected_decision
      ? "Your decision matches the suggested judgment. The evidence and reasoning still matter."
      : `You chose ${choices[selected].toLowerCase()}. Compare your reasoning with the suggested judgment and alternatives.`);
    setText("feedback-explanation", current.explanation);
    setText("feedback-alternative", current.alternative_judgment);
    setText("feedback-rubric", current.criterion);
    setText("feedback-change", current.implementation_change);
    feedback.hidden = false;
    status.textContent = `Comparison ready. Suggested judgment: ${choices[current.expected_decision]}. ${current.explanation}`;
  });
  selector.addEventListener("change", () => showCase(selector.value));

  fetch("./teaching-sample/data/cases.json")
    .then((response) => {
      if (!response.ok) throw new Error("Teaching cases unavailable");
      return response.json();
    })
    .then((payload) => {
      if (payload.schema_version !== 1 || !Array.isArray(payload.cases) || !payload.cases.length || !Array.isArray(payload.documents)) {
        throw new Error("Invalid teaching data");
      }
      const sourceKeys = new Set();
      payload.documents.forEach((source) => {
        const key = `${source.id}@${source.version}`;
        if (!Number.isInteger(source.version) || sourceKeys.has(key)
          || [source.id, source.title, source.text, source.status].some((value) => typeof value !== "string")) {
          throw new Error("Invalid source");
        }
        sourceKeys.add(key);
      });
      const caseIds = new Set();
      payload.cases.forEach((item) => {
        if (!/^[a-z-]+$/.test(item.id) || caseIds.has(item.id) || !Object.hasOwn(choices, item.expected_decision)
          || [item.label, item.question, item.explanation, item.criterion, item.implementation_change, item.alternative_judgment].some((value) => typeof value !== "string")
          || !sourceKeys.has(`${item.source_id}@${item.source_version}`)
          || !sourceKeys.has(`${item.baseline_source?.id}@${item.baseline_source?.version}`)
          || typeof item.response?.text !== "string" || !Array.isArray(item.response.citations)
          || item.response.citations.some((citation) => !sourceKeys.has(`${citation.source_id}@${citation.version}`))) {
          throw new Error("Invalid teaching case");
        }
        caseIds.add(item.id);
      });
      data = payload;
      selector.replaceChildren();
      data.cases.forEach((item) => {
        const option = document.createElement("option");
        option.value = item.id;
        option.textContent = titleCaseLabel(item.label);
        selector.append(option);
      });
      showCase(data.cases[0].id, false);
      lab.querySelector(".lab-controls").hidden = false;
      controls.hidden = false;
      lab.querySelector("#lab-fallback").hidden = true;
    })
    .catch(() => {
      // The first complete case remains readable if JavaScript or fetching fails.
      status.textContent = "Interactive cases are unavailable. Read the example and instructor explanation, or download the complete sample.";
    });
})();
