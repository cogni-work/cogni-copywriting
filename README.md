# cogni-copywriting

Professional copywriting toolkit for Claude Code. Provides document polishing with messaging frameworks, multi-stakeholder review via parallel persona Q&A, readability optimization, and sales copy enhancement.

## Skills

### copywriter

Create and polish business documents using 7 messaging frameworks (BLUF, Pyramid, SCQA, STAR, PSB, FAB, Inverted Pyramid) with measurable quality standards.

**Features:**
- Document types: memos, emails, briefs, reports, proposals, one-pagers, executive summaries, business letters, blogs
- Readability optimization (Flesch 50-60 target)
- Sales mode with Power Positions (IS-DOES-MEANS) enhancement
- Multi-stakeholder review (automated or via reader skill)
- German character and citation preservation

### reader

Review documents through parallel stakeholder persona simulation with synthesized feedback and automatic improvement.

**Features:**
- 5 stakeholder personas: executive, technical, legal, marketing, end-user
- Parallel persona analysis for fast results
- Cross-persona theme synthesis
- Automatic document improvement with backup
- Structured Q&A feedback per persona

## Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/copywrite` | `/copywrite <file> [--scope=full\|structure\|tone\|formatting]` | Polish documents for executive readability |
| `/review-doc` | `/review-doc <file> [--personas=executive,technical]` | Stakeholder persona review |

## Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| copywriter | opus | Orchestrate document polishing, return JSON metrics |
| reader | sonnet | Orchestrate stakeholder review, return JSON results |

## Prerequisites

- Python 3 (for readability calculations)
- Claude Code with plugin support

## Installation

```bash
claude --plugin-dir /path/to/cogni-copywriting
```

## License

CC-BY-NC-SA-4.0
