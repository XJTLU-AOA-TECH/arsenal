---
name: xipu-press
description: Turn raw text and images into a designed A4 document (handbook, briefing, report, handover) in the XJTLU house style — navy/orange/magenta palette, numbered sections, stat cells, navy-header tables. Use when the user asks for a 西浦风格 / XJTLU-style document, or supplies text and images and wants a polished branded document designed for them. Not for slides, emails, posters, or official letters.
metadata:
  short-description: Design XJTLU-style documents from raw content
---

# XIPU Press

Produce print-ready A4 documents in the XJTLU house style from user-supplied text and images. The deliverable is a self-contained HTML file, plus a PDF when printing is expected. The style was validated on real XJTLU management documents (bilingual EN/ZH competition handbook).

## Workflow

1. Read the user's material. Decide document type, language (English, Chinese, or paired EN pages followed by ZH pages mirroring the same numbering), and a section outline. Ask only when audience or language is genuinely ambiguous.
2. Read [references/design-system.md](references/design-system.md) for the full palette, typography, and component catalog before composing pages.
3. Copy [assets/xipu-doc-template.html](assets/xipu-doc-template.html) as the starting point and replace the placeholder content with the user's material. Keep every component class it uses; add or drop components as the content requires.
4. User images go in with the `.figure` component. Store image files next to the HTML and reference them with relative paths so the document stays portable.
5. Render and visually verify before delivering: `python3 scripts/render_pdf.py <file.html> <out.pdf>` renders through local headless Chrome. If headless Chrome crashes inside a sandboxed shell (SIGABRT), rerun outside the sandbox. Inspect every page for overflow, orphaned headings, cramped tables, and images that break layout; split or rebalance pages until clean. A browser screenshot at A4 width is a fast alternative for on-screen checks.

## Hard rules

- The palette and font stack are fixed (see the design-system reference). No gradients, no shadows, no rounded corners, no decorative imagery, no icons inside this document type.
- One coherent idea per page; dense but organized. If content overflows a page, split the page — never shrink type below the minimums in the reference.
- Factual content comes only from the user's material. Never invent figures, results, names, dates, or commitments to fill a section; leave a visible placeholder and ask instead.
- External-facing documents must not contain unconfirmed promises or open-ended commitments (e.g. "to be added", indefinite offers of support). Audit for open items before finalizing.
