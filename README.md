# cogni-copywriting

A copywriting plugin for Claude Code. Polish documents for executive readability, get multi-stakeholder feedback, and strengthen story arc narratives — in English or German. Claude applies messaging frameworks, readability standards, and impact techniques so your writing lands.

## Installation

```
claude plugins add cogni-copywriting
```

## What It Does

- **Document polishing** — Takes any markdown document and transforms it for executive readers. Applies messaging frameworks (BLUF, Pyramid, SCQA, STAR, PSB, FAB, Inverted Pyramid), optimizes readability, and adds visual hierarchy. Works with memos, emails, briefs, reports, proposals, one-pagers, executive summaries, business letters, and blogs. Supports English (Flesch Reading Ease) and German (Amstad readability + Wolf Schneider style rules) with full preservation of German characters and citations.
- **Stakeholder review** — Runs your document through five simulated reader personas (executive, technical, legal, marketing, end-user) in parallel. Synthesizes cross-persona feedback, flags blind spots, and auto-applies improvements — with a backup of the original.
- **Arc-aware polishing** — When paired with cogni-narrative, detects story arcs and applies element-specific techniques (Number Plays, Power Words, forcing functions) tuned to each arc element's purpose. Structure is preserved; impact is strengthened.

## Commands

| Command | What it does |
|---------|--------------|
| `/copywrite <file>` | Polish a document for executive readability |
| `/copywrite <file> --scope=structure` | Restructure only (McKinsey Pyramid) — skip tone and formatting |
| `/copywrite <file> --scope=tone` | Transform academic tone to executive — skip structure and formatting |
| `/copywrite <file> --scope=formatting` | Optimize visual hierarchy only |
| `/review-doc <file>` | Run all five stakeholder personas and auto-apply improvements |
| `/review-doc <file> --personas=executive,legal` | Run specific personas only |
| `/review-doc <file> --no-improve` | Feedback only — don't change the document |

## Example Workflows

The recommended sequence: **polish first, then review**. Copywriting gets the document into shape; stakeholder review validates the result and catches blind spots.

### Polish a Document

```
You: /copywrite quarterly-report.md

Claude: [Reads the document, detects it's a report]
        [Applies Pyramid Principle structure]
        [Transforms academic language to executive tone]
        [Adds visual hierarchy — callout boxes, bold key metrics]
        [Validates: Flesch 57, active voice 84%, 12 visual elements]
        [Writes polished document back to quarterly-report.md]
```

### Then Review Before Sending

```
You: /review-doc quarterly-report.md

Claude: [Creates backup at .quarterly-report.pre-reader-review]
        [Runs 5 personas in parallel: executive, technical, legal, marketing, end-user]
        [Executive: "Lead with the $2.3M impact figure, not the timeline"]
        [Legal: "Remove absolute guarantee language in section 3"]
        [Synthesizes: 3 critical improvements, 5 high-priority suggestions]
        [Auto-applies critical and high-priority improvements]
        [Reports: overall score 82/100, 8 improvements applied]
```

### Polish a Story Arc

When cogni-narrative has created a story arc, copywriting strengthens it without breaking the structure:

```
cogni-narrative → cogni-copywriting → cogni-workplace
(creates arc)     (polishes arc-aware)  (story-to-slides)
```

```
You: /copywrite why-change-narrative.md

Claude: [Detects arc_id in frontmatter — activates arc-aware mode]
        [Loads arc-technique-map instead of messaging frameworks]
        [Why Change section: adds ratio framing ("3x faster than current process")]
        [Why Now section: strengthens forcing functions ("regulatory deadline: Q3")]
        [Why Pay section: applies compound impact techniques]
        [Validates: arc structure preserved, element techniques strengthened]
```

### Polish a German Document

```
You: /copywrite vorstandsbericht.md

Claude: [Detects German language]
        [Loads Wolf Schneider style rules instead of English defaults]
        [Breaks Satzklammer: "stellt ... dar" → "beschreibt"]
        [Shortens Mittelfeld: max 12 words per clause]
        [Eliminates Floskeln: "im Rahmen von" → "bei"]
        [Keeps Subjekt and Verb close together]
        [Chains Hauptsätze for rhythm: short — long — short]
        [Preserves ä, ö, ü, ß and all citations exactly]
        [Validates: Amstad 55, avg clause 9.2 words, 0 Floskeln, rhythm ✓]
```

### Quick Scope: Tone Only

```
You: /copywrite research-paper.md --scope=tone

Claude: [Reads the document, skips restructuring]
        [Transforms passive academic voice to direct executive language]
        [Replaces jargon with plain language equivalents]
        [Writes updated document — structure and formatting untouched]
```

### Feedback Only (No Changes)

```
You: /review-doc proposal.md --no-improve

Claude: [Runs all 5 personas — does NOT modify the document]
        [Returns structured feedback per persona with scores]
        [You decide which suggestions to apply manually]
```

## Skills

| Skill | Description |
|-------|-------------|
| `copywriter` | Document polishing with 7 messaging frameworks, 9 deliverable types, readability scoring, Wolf Schneider German style rules, arc-aware mode, and sales enhancement |
| `reader` | Multi-stakeholder review through 5 parallel personas with synthesized feedback and auto-improvement |

## German Language Support

When a German document is detected, the plugin applies **Wolf Schneider style rules** instead of the English defaults:

| Rule | What it does | Target |
|------|-------------|--------|
| 3-Sekunden-Regel | Limits clause length for fast comprehension | Max 12 words per clause |
| Satzklammer | Replaces split verbs with single verbs | "stellt dar" becomes "beschreibt" |
| Mittelfeld | Shortens the middle field between verb parts | Max 6 words between subject and verb |
| Floskeln | Detects and replaces bureaucratic phrases | 0 matches against 40+ known phrases |
| Hauptsatz-Reihung | Chains main clauses instead of nesting | Hauptsatz before Nebensatz |
| Attribut-Tilgung | Replaces stacked adjectives with relative clauses | Max 2 attributes before a noun |
| Rhythmus | Varies sentence length for natural flow | Std dev > 3.0 words |

The readability script (`readability.sh`) reports these metrics automatically when German is detected.

## Prerequisites

- Python 3 (for readability calculations)
- Claude Code with plugin support

## License

CC-BY-NC-SA-4.0
