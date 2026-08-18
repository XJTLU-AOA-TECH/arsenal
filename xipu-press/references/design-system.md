# XIPU Press Design System

Extracted from the AoA Student Competition Handbook (August 2026), which confirmed the XJTLU management-document rules. Compose pages with the components below; the CSS implementing all of them lives in `assets/xipu-doc-template.html` — do not restyle, reuse the classes.

## Palette

| Token | Value | Use |
|-------|-------|-----|
| `--navy` | `#010544` | Title bands, table headers, section-rule lines, big stat numbers |
| `--orange` | `#FB7831` | Kickers, stat top-rules, square bullets, accent tags |
| `--magenta` | `#CE57C1` | Section numbers, note-panel left bar, secondary tags |
| `--grey` | `#E7E6E6` | Table hairlines only |
| `--ink` | `#1c1c1e` | Body text |

Zebra rows use `#fafafa`; note panels use `#f5f5f7`. Screen background behind pages is `#555` (never printed).

## Typography

- Display/Latin: `'DIN Alternate', 'Arial', sans-serif`. Chinese: `'PingFang SC'`.
- Body 8.5pt / 1.36; lead paragraph 8.8pt; tables 7.4–7.9pt; tags 6.6pt. Nothing below 6.6pt.
- `h2` is 10pt navy and always carries a magenta section number: `<h2><span class="no">01</span> Overview</h2>`; on Chinese pages the title goes in `<span class="zh-t">`.
- Letter-spacing only on small-caps labels (kickers, stat labels, tags, header doc label). Body text letter-spacing stays 0.

## Page model

- One `<div class="page">` per A4 page (210×297mm, padding 9mm/11mm, `page-break-after: always`).
- Every page opens with the header: `<div class="hdr"><span class="doc">DOC LABEL · UNIT</span><span class="mark">XJTLU</span></div>` — uppercase doc label left, XJTLU wordmark right, 2px navy rule below.
- Chinese pages add `class="page zh"` and use `.cn-title-band` instead of `.titleblock`.
- Bilingual documents: all English pages first, then the Chinese pages with the same section numbering.

## Components

**Title band (EN page 1)** — `.titleblock` with `.kicker` (orange, uppercase), `h1`, `.zh-sub`, `.meta` (date · university · team).

**Title band (ZH page 1)** — `.cn-title-band` with `h1`, subtitle line, `.meta`.

**Stat cells** — `.stat` row of 2–5 `.cell`s: orange top rule, big navy `.num`, small-caps `.lab`. Use for the 2–4 figures a reader must remember; not every number deserves a cell.

**Tables** — navy `th`, hairline row borders, zebra rows, explicit column widths inline on `th`. Keep to 7 columns max; long text goes in the widest column.

**Numbered stages** — `<ol class="stages">` renders navy square counters. Use for sequential processes (3–6 steps), bold lead phrase + one sentence per step.

**Plain bullets** — `<ul class="plain">` with orange square markers. Use for short non-sequential items (cost rules, scope notes).

**Note panel** — `.note`: grey panel, magenta left bar, bold lead word. For supplier notes, cautions, context a reader must not miss.

**Tags** — `<span class="tag">` (magenta outline) or `.tag.o` (orange outline). Inline status labels inside tables or lists, e.g. "Supporting unit".

**Two-column block** — `.two-col` (optionally `.tight`) for dense late-page content; headings set `break-after: avoid`.

**Closing band** — `.closing`: 2px navy top rule, one short paragraph. For the wrap-up/continuity statement.

**Figure** — `.figure` wraps a user-supplied image: `<div class="figure"><img src="..."><div class="cap">Caption</div></div>`. Images span the text column, thin grey caption below. Keep total image height under 40% of the page so text stays primary.

## Composition rules

- No gradients, shadows, rounded corners, decorative imagery, or icons — the style is flat print.
- Section numbers (`01`, `02`…) are per-language and continuous across pages of that language.
- A page holds 3–5 components comfortably. If a table or stage list would split across pages, rebalance the outline instead of letting it break awkwardly.
- Reserve orange for structure (rules, bullets, kickers) and magenta for markers (numbers, note bars); never use them as large fills.
