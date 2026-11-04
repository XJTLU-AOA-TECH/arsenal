---
name: xipu-press
description: Turn raw text and images into designed print artifacts in one of two house themes. (1) XJTLU house style — navy/orange/magenta A4 documents such as handbooks, briefings, reports and handovers. (2) FDE Lab theme — off-white, ink and chartreuse-lime posters, one-pagers and share pages for FDE Lab; palette, typography and components extracted by pixel sampling from the 2026-10-27 FDE Lab talk deck. Use when the user asks for a 西浦风格 / XJTLU-style document, an FDE Lab poster / one-pager / share page / 展板, or supplies text and images and wants a polished branded artifact designed for them. Not for slides, emails, or official letters.
metadata:
  short-description: Design XJTLU-style documents and FDE Lab posters from raw content
---

# XIPU Press

Produce print-ready artifacts in one of two house themes from user-supplied text and images. The deliverable is a self-contained HTML file plus a PDF when printing is expected.

Two themes, pick one before composing:

- **XJTLU house style** — management documents: handbook, briefing, report, handover. A4. Reference [references/design-system.md](references/design-system.md), template [assets/xipu-doc-template.html](assets/xipu-doc-template.html).
- **FDE Lab theme** — lab-branded display artifacts: poster (A2 portrait, default), one-pager (A4), share page. Reference [references/fde-lab-theme.md](references/fde-lab-theme.md), template [assets/fde-lab-poster-template.html](assets/fde-lab-poster-template.html), logo [assets/fde-lab-logo.png](assets/fde-lab-logo.png). The theme was extracted by pixel sampling from 《AI 领导力——当 AI 开始工作，你准备好了吗》v1.0（2026-10-27，22 页）；色值与组件以 references/fde-lab-theme.md 为准，不要目测改色。

## Workflow

1. Read the user's material. Decide theme, format (A4 doc / A2 poster / A4 one-pager), language (English, Chinese, or paired), and an outline. Ask only when audience, theme or language is genuinely ambiguous.
2. Read the matching reference for palette, typography and the component catalog before composing.
3. Copy the matching template as the starting point and replace placeholders. Keep every component class the template defines; add or drop components as the content requires. For FDE Lab artifacts, copy `assets/fde-lab-logo.png` next to the HTML and keep the relative path so the artifact stays portable.
4. User images go in with the `.figure` component (XJTLU theme). Store image files next to the HTML.
5. Render and visually verify before delivering: `python3 scripts/render_pdf.py <file.html> <out.pdf>` renders through local headless Chrome; if headless Chrome crashes inside a sandboxed shell (SIGABRT), rerun outside the sandbox. For posters also render a PNG preview (e.g. PyMuPDF at 100 dpi) and inspect it. Check every page for overflow, orphaned headings, cramped tables, images that break layout, type below the theme minimums, and theme violations (FDE Lab: lime used as body text on a light background, gray bars on inner pages, radius above 6px). Split or rebalance until clean.
6. External-facing artifacts: audit for open items first; no unconfirmed promises or open-ended commitments; state version, date and draft status in the footer.

## Hard rules

- Per-theme palette and font stack are fixed by the references. No gradients and no shadows in either theme.
- XJTLU theme: no rounded corners, no icons, flat print.
- FDE Lab theme: rounded corners up to 6px on cards only; simple line icons allowed in ink or olive; the diagonal gray bars and the lime outline triangle appear only on covers, section pages and the poster's top band, never on inner body pages; lime is a fill and line color only — emphasized text on light backgrounds uses olive, emphasized text on the dark keybar uses lime.
- One coherent idea per page (documents) or per card (posters). Dense but organized. If content overflows, split or rebalance — never shrink type below the theme minimums.
- Factual content comes only from the user's material. Never invent figures, results, names, dates or commitments to fill a section; leave a visible placeholder and ask instead.
- FDE Lab logo: use the supplied `fde-lab-logo.png` crop. If an official brand file exists, prefer it; do not redraw the monogram by hand.
