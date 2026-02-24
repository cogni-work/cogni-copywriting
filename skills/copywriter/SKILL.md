---
name: copywriter
description: Create high-impact business documents using messaging frameworks (BLUF, Pyramid, SCQA, STAR, PSB, FAB) and sophisticated persuasion techniques (number plays, power words, rhetorical devices). Supports memos, emails, briefs, reports, proposals, one-pagers, executive summaries, and business letters with measurable quality standards.
allowed-tools: Read, Write, Edit, Bash, TodoWrite
---

# Copywriter Skill

## Critical Constraints

### German Character Preservation

**MANDATORY:** ALL German-specific characters MUST be preserved exactly as written. NEVER convert to ASCII equivalents.

| Original | WRONG Conversion | Rule |
|----------|------------------|------|
| ä | ae | PRESERVE as ä |
| ö | oe | PRESERVE as ö |
| ü | ue | PRESERVE as ü |
| Ä | Ae | PRESERVE as Ä |
| Ö | Oe | PRESERVE as Ö |
| Ü | Ue | PRESERVE as Ü |
| ß | ss | PRESERVE as ß |

This applies to ALL text: body, headers, citations, technical terms.

### Citation Preservation

**MANDATORY:** ALL citation markers and their URLs MUST be preserved exactly as written. **Removing or omitting citations is a CRITICAL FAILURE** that invalidates the entire document output. Citations are evidence markers for audit trail integrity, NOT style elements eligible for compression.

| Format | Example | Rule |
|--------|---------|------|
| Inline with URL | `[P1-1](https://...)` | PRESERVE complete link |
| Shortform | `[P1-1]` | PRESERVE marker |
| Superscript | `<sup>[1]</sup>` | PRESERVE HTML tags |
| Provenance markers | `[portfolio-validated]` | PRESERVE after citation |
| Portfolio-derived | `[portfolio-derived]` | PRESERVE inline marker |

**DO NOT:**
- Remove URLs from inline citations
- Change citation marker format (e.g., [P1-1] to [1])
- Relocate citations to different positions in text
- Merge or split citation markers
- **Treat citations as clutter, noise, or candidates for word-count reduction**
- Summarize citations into a footer reference (e.g., "See research.md for sources")

**TIEBREAKER RULE:** When conciseness principles conflict with citation preservation, **citation preservation ALWAYS wins.** Reduce word count from prose, not from evidence markers. The output MUST contain at least as many citation markers as the source document.

**CONSEQUENCE:** If the polished output has fewer citations than the source, the output will be rejected and the source document used as-is.

Create professional business documents using structured messaging frameworks, measurable quality standards, and sophisticated impact techniques.

## When to Use

- Creating business documents (memos, emails, briefs, reports, proposals, one-pagers, executive summaries, business letters)
- Creating blog posts from research insights
- Applying messaging frameworks (BLUF, Pyramid, SCQA, STAR, PSB, FAB, Inverted Pyramid)
- Enhancing document impact with persuasion techniques
- Improving document readability and executive appeal

## Protected Content (DO NOT Modify)

Documents may contain tagged diagram descriptions for later processing by diagram-expert. These MUST be preserved exactly as-is.

**Protected patterns:**

1. **Diagram placeholder blocks** - Complete XML structure:

   ```xml
   <diagram-placeholder id="..." type="...">
     <title>...</title>
     <content-data>...</content-data>
     <instructions>...</instructions>
   </diagram-placeholder>
   ```

2. **Figure reference text** - Introductory sentences referencing figures:
   - "As shown in Figure N below..."
   - "Wie in Abbildung N unten dargestellt..."
   - Any text pattern: `Figure/Abbildung/Figura/Figuur {N}`

3. **Figure captions** - Lines following placeholders or embeds:
   - `**Figure N:** Title`
   - `**Abbildung N:** Titel`

4. **Obsidian embeds** - Already-resolved diagrams:
   - `![[assets/*.svg]]`

5. **Kanban table and placeholder** - Trend Landscape tables with planning horizons:
   - Table header pattern: `| Dimension | Act | Plan | Observe |` (or German: `| Dimension | Act | Plan | Observe |`)
   - Wikilinks in table cells: `[[06-megatrends/data/megatrend-*|*]]`, `[[11-trends/data/trend-*|*]]`
   - Legend line: `Legend: **M** = Megatrend, **T** = Trend` (or German equivalent)
   - HTML placeholder: `<!-- kanban-board -->`

**Preservation rules:**

- DO NOT rephrase or "improve" diagram instructions text
- DO NOT modify figure numbering or caption format
- DO NOT add, remove, or reorder content-data JSON
- DO NOT change diagram type or id attributes
- PRESERVE all whitespace within placeholder blocks

## Workflow

**Initialize TodoWrite** with these 8 steps, then execute sequentially:

1. Parse parameters and load references
2. Gather content requirements
3. Apply structure and framework
4. Apply writing principles
5. Apply impact techniques (optional)
6. Stakeholder review (optional)
7. Synthesis and refinement (optional)
8. Validate and write document

### Step 1: Parse Parameters & Load References

**Extract from user request:**

- `deliverable_type`: memo | email | brief | report | proposal | one-pager | executive-summary | business-letter | blog
- `framework` (optional): bluf | pyramid | scqa | star | psb | fab | inverted-pyramid
- `impact_level` (optional): standard | high (for executive audiences)
- `MODE` (optional): standard | sales (default: standard)

**Load references:**

```text
READ: references/04-deliverable-types/{deliverable_type}.md
READ: references/02-messaging-frameworks/{framework}-framework.md
READ: references/01-core-principles/clarity-principles.md
```

If framework not specified, use deliverable's recommended framework.
If `impact_level: high` or audience is executive/C-suite, also load impact techniques.

**If MODE: sales:**

```text
READ: references/08-sales-techniques/power-positions.md
READ: references/07-impact-techniques/number-plays.md
READ: references/07-impact-techniques/power-words.md
```

Sales mode enables intelligent enhancement of Power Positions (IS-DOES-MEANS structure) while preserving structure markers.

### Step 2: Gather Content Requirements

Ask user for:

- **Main message**: What's the bottom line?
- **Audience**: Who reads this? (role, seniority)
- **Action**: What should readers do?
- **Key points**: 2-3 supporting facts
- **Output path**: Where to write the document

**For high-impact documents, also ask:**

- **Quantifiable data**: What numbers support the message? (for number plays)
- **Urgency/exclusivity**: What's the timeline or scarcity factor? (for power words)

### Step 3: Apply Structure & Framework

Use deliverable structure from loaded reference, then integrate framework pattern:

| Framework | Pattern |
|-----------|---------|
| BLUF | Bottom line first → supporting facts → action |
| Pyramid | Main argument → MECE groups → evidence |
| SCQA | Situation → Complication → Question → Answer |
| STAR | Situation → Task → Action → Result |
| PSB | Problem → Solution → Benefit |
| FAB | Feature → Advantage → Benefit |
| Inverted Pyramid | Critical info → details → background |

### Step 4: Apply Writing Principles

**Clarity**: 15-20 word sentences, concrete language, simple words
**Conciseness**: 3-5 sentence paragraphs, no filler phrases, strong verbs
**Active voice**: 80%+ active voice usage
**Formatting**: Max 3 heading levels, visual elements every 2 paragraphs

### Step 5: Apply Impact Techniques

For enhanced persuasion, apply techniques from `references/07-impact-techniques/`:

#### Number Plays

Transform vague claims into concrete, memorable data.

| Technique | Pattern | Example |
|-----------|---------|---------|
| Ratio framing | % → "X in Y" | "12%" → "1 in 8" |
| Specific quantification | Vague → precise | "many" → "127 customers" |
| Comparative anchoring | Raw → relative | "$36K/year" → "$100/day" |
| Before/after contrast | Old → New (gain) | "5 days → 4 hours (97% faster)" |

**Read `references/07-impact-techniques/number-plays.md` for detailed patterns.**

#### Power Words

Use emotional triggers strategically in headlines, CTAs, and key statements.

| Category | Words | Use When |
|----------|-------|----------|
| Urgency | now, deadline, limited | Time-sensitive requests |
| Exclusivity | exclusive, insider, select | Premium offerings |
| Trust | proven, guaranteed, validated | Risk reduction |
| Achievement | breakthrough, transform, unlock | Aspirational goals |

**Target density:** 3-5 power words per page, concentrated in headlines/CTAs.
**Read `references/07-impact-techniques/power-words.md` for complete list.**

#### Rhetorical Devices

Apply structural persuasion for key messages.

| Device | Pattern | Example |
|--------|---------|---------|
| Rule of Three | A, B, C | "Faster, cheaper, better" |
| Anaphora | Same start | "We deliver results. We deliver on time." |
| Antithesis | X, not Y | "More output, less effort" |
| Cadence | Long → Short | "After months of analysis—we're ready." |

**Place 2-3 devices per document, concentrated at opening and closing.**
**Read `references/07-impact-techniques/rhetorical-devices.md` for detailed guidance.**

#### Executive Impact

For C-suite and board communications:

1. **Lead with the ask** — Recommendation in first 2 sentences
2. **Quantify everything** — All benefits as numbers
3. **Respect time** — One page maximum, 30-second scannable
4. **Provide decision clarity** — Specific action, timeline, consequence
5. **Signal credibility** — Data sources, risk acknowledgment

**Read `references/07-impact-techniques/executive-impact.md` for templates.**

#### Power Positions Enhancement (MODE: sales)

When MODE is set to `sales`, apply intelligent enhancement to Power Positions content while preserving the IS-DOES-MEANS structure.

**Structure markers to preserve exactly:**

```markdown
**IS**:
**DOES**:
**MEANS**:
**Proof**:
**Addresses**:
**Competitor Gap**:
```

**Enhancement by layer:**

| Layer | Enhancement Focus | Techniques |
|-------|-------------------|------------|
| **IS** | Make specific and concrete | Add details: numbers, specs, timeframes |
| **DOES** | Quantify outcomes | Number Plays: %, time, before/after |
| **MEANS** | Strengthen resonance | Power Words: protect, transform, exclusive |

**Example enhancement:**

Before:

```markdown
**DOES**: Helps improve operations
```

After:

```markdown
**DOES**: Reduce decision cycle from 2 weeks to 48 hours, enabling 10x faster response to market shifts
```

**Critical rules:**

- NEVER merge IS into DOES or DOES into MEANS
- PRESERVE all structure markers unchanged
- PRESERVE Power Position numbering (`### Power Position #N:`)
- PRESERVE proof points, need references, and citation markers
- Apply Number Plays primarily to DOES layer
- Apply Power Words primarily to MEANS layer

**Read `references/08-sales-techniques/power-positions.md` for detailed enhancement rules.**

### Step 6: Stakeholder Review (Optional)

**Skip if:**
- `skip_review: true` parameter set
- Deliverable type is informal (email, casual memo)

**Two review modes available:**

#### Option A: Interactive Review via Reader Skill (Recommended)

Delegate to the `cogni-copywriting:reader` skill for parallel multi-persona Q&A with automatic document improvement.

```text
Skill: cogni-copywriting:reader
Args: FILE_PATH={{output_path}} PERSONAS={{stakeholders}} AUTO_IMPROVE=true
```

The reader skill runs all selected personas in parallel, synthesizes feedback, and applies one auto-improvement loop directly to the document. See the reader skill for full details.

**When to use:** Formal deliverables (reports, proposals, executive summaries, briefs) where stakeholder alignment matters.

#### Option B: Automated Checklist Review (Lightweight)

For faster review without interactive depth:

**Load stakeholder profiles:**

```text
READ: references/10-stakeholder-review/{perspective}-review.md
```

**Default stakeholder selection:**

| Audience Parameter | Default Stakeholders |
|-------------------|---------------------|
| `executive` | executive, technical, end-user |
| `technical` | technical, executive |
| `general` | end-user, marketing, executive |
| `legal` | legal, executive, technical |
| `sales/marketing` | marketing, executive, end-user |

**Custom selection:** Override with `stakeholders: [executive, legal, technical]` parameter.

**Review process:**

1. Initialize Phase 6 TodoWrite with sub-tasks for each stakeholder
2. For each stakeholder:
   - Load review criteria from `references/10-stakeholder-review/{perspective}-review.md`
   - Evaluate document against checklist (5 weighted criteria per perspective)
   - Assign scores: PASS (100), CONCERN (60), FAIL (0)
   - Calculate weighted overall score (0-100 scale)
   - Generate structured feedback:
     - Strengths (what works well)
     - Concerns (areas needing improvement)
     - Recommendations (specific, actionable improvements with priority labels)
3. Mark stakeholder todo completed
4. Collect all feedback for synthesis

**Review mode parameter:**
- `review_mode: reader` - Use interactive reader skill (Option A)
- `review_mode: automated` (default) - Run checklists automatically (Option B)
- `review_mode: skip` - Bypass review phases entirely

**Scoring thresholds (Option B only):**
- 85-100: Excellent, meets stakeholder expectations
- 70-84: Good, minor improvements recommended
- 50-69: Concerns, significant improvements needed
- 0-49: Failing, major issues detected

**Graceful degradation:**
- Single stakeholder review failure → Log warning, continue with remaining stakeholders
- All stakeholder reviews fail → Skip to Step 8 with `fallback_reason: "review_failure"`
- Document continues to Phase 8 regardless—review enhances quality but never blocks delivery

### Step 7: Synthesis & Refinement (Optional)

**Skip if:** Step 6 used reader skill (Option A, which handles its own synthesis) or was skipped entirely.

**Load synthesis guidelines:**

```text
READ: references/10-stakeholder-review/synthesis-guidelines.md
```

**Synthesis process:**

1. **Aggregate feedback** - Collect all stakeholder reviews into structured format
2. **Identify common themes** - Pattern match recommendations across stakeholders:
   - 3+ stakeholders mention same issue → CRITICAL priority
   - 2 stakeholders mention same issue → HIGH priority
   - 1 stakeholder mentions issue → OPTIONAL priority
   - Executive + 1+ other on same issue → CRITICAL priority
3. **Prioritize recommendations:**
   - **CRITICAL** - Multiple stakeholders OR blocks validation OR executive + other
   - **HIGH** - Multiple stakeholders OR high-weight criterion (>=20%)
   - **OPTIONAL** - Single stakeholder OR low-weight criterion (<15%)
4. **Create refinement TodoWrite** with sub-tasks for each CRITICAL and HIGH improvement
5. **Apply improvements to document:**
   - For each CRITICAL: Apply change, validate improvement, mark complete
   - For each HIGH: Assess feasibility, apply if feasible, log if skipped
   - For each OPTIONAL: Log for manual review, do NOT apply automatically
6. **Re-evaluate changed sections** - Verify improvements raised criterion scores
7. **Calculate synthesis metrics** - Overall score, application rate, recommendations applied
8. Mark synthesis complete

**Synthesis output format:**

```json
{
  "stakeholder_reviews": [
    {
      "perspective": "executive",
      "score": 85,
      "strengths": ["Clear BLUF", "Strong ROI"],
      "concerns": ["Missing timeline"],
      "recommendations": ["CRITICAL: Add decision deadline"]
    }
  ],
  "synthesis": {
    "overall_score": 82,
    "audience_weighted_score": 84,
    "critical_improvements": ["Add decision timeline"],
    "high_improvements": ["Add risk section"],
    "optional_improvements": ["Add comparison table"],
    "recommendations_applied": true,
    "application_rate": 1.0
  }
}
```

**Conflict resolution patterns:**

| Conflict | Resolution |
|----------|------------|
| Executive wants brevity, Technical wants detail | Executive summary + technical appendix |
| Marketing wants emotion, Executive wants data | Lead with data, use power words for emphasis |
| End-user wants simple, Technical wants precision | Plain language with technical glossary |
| Legal wants hedging, Marketing wants bold claims | Strong but hedged: "designed to deliver" |

**Tiebreaker hierarchy:**
1. Primary audience perspective (if specified)
2. Deliverable requirements (framework, regulatory)
3. Impact techniques effectiveness
4. User-specified preference

**Graceful degradation:**
- Individual improvement fails → Revert change, log failure, continue with remaining
- Synthesis calculation fails → Continue to Step 8 with original document, log `fallback_reason: "synthesis_failure"`
- Document continues to Phase 8 regardless—synthesis enhances quality but never blocks delivery

### Step 8: Validate & Write Document

**Validate against:**

- **German characters preserved** (ä, ö, ü, ß MUST remain as-is, NEVER converted to ae, oe, ue, ss)
- **Citations preserved** (all `[P1-1](URL)` markers MUST retain their URLs, format unchanged)
- Framework pattern applied correctly
- Deliverable requirements met (length, structure, tone)
- Readability: Flesch 50-60 target
- Active voice: 80%+ usage
- Impact techniques applied (if specified)
- **Critical stakeholder improvements applied** (if review conducted)
- **Protected content preserved** (diagram placeholders, figure references, captions unchanged)
- **Citation formatting applied** (see below)

**Backup original document** before writing:

1. Extract directory and filename from output path
2. Check if file exists at output path using Bash: `[[ -f "{output_path}" ]]`
3. If file exists, create backup with hidden filename:
   ```bash
   # Extract directory and filename
   dir=$(dirname "{output_path}")
   filename=$(basename "{output_path}")
   backup_path="${dir}/.${filename}"

   # Copy original to backup (hidden file)
   cp "{output_path}" "${backup_path}"
   ```
4. Report backup creation: `Backup created: {backup_path}`

**Apply citation formatting** (if document contains citations):

Read `references/03-formatting-standards/citation-formatting.md` for complete rules.

1. **Move citations to specific claims** (Rule 1):
   - Identify sections with "Begruendung:" paragraphs followed by "Umsetzung:" lists
   - Move citations from "Begruendung:" text to individual "Umsetzung:" list items
   - Place citations at the end of the specific claim they support

2. **Add superscript commas between consecutive citations** (Rule 3):
   - Find all instances of `</sup><sup>`
   - Replace with `</sup><sup>,</sup> <sup>` using perl:
   ```bash
   perl -pi -e 's/<\/sup><sup>/<\/sup><sup>,<\/sup> <sup>/g' "{output_path}"
   ```

**Write document** using Write tool, then present summary:

```text
Document: {deliverable_type} using {framework}
File: {path}
Backup: {backup_path if created, or "None (new file)"}
Quality: Framework ✓ | Structure ✓ | Readability ✓
Impact Techniques: {techniques applied, if any}
Citation Formatting: {citations formatted, if applicable}
```

## Bundled Resources

### References (Progressive Disclosure)

**Core Principles** (01-core-principles/):

- clarity-principles.md - 15-20 word sentences, concrete language
- conciseness-principles.md - 3-5 sentence paragraphs, strong verbs
- active-voice-principles.md - 80%+ active voice usage

**Formatting Standards** (03-formatting-standards/):

- citation-formatting.md - Citation placement and superscript comma formatting
- markdown-basics.md - Standard markdown syntax
- heading-hierarchy.md - Header structure standards
- visual-elements.md - Visual hierarchy principles

**Messaging Frameworks** (02-messaging-frameworks/):

- bluf-framework.md - Bottom Line Up Front
- pyramid-framework.md - McKinsey Pyramid Principle
- scqa-framework.md - Situation-Complication-Question-Answer
- star-framework.md - Situation-Task-Action-Result
- psb-framework.md - Problem-Solution-Benefit
- fab-framework.md - Feature-Advantage-Benefit
- inverted-pyramid-framework.md - Journalism style

**Deliverable Types** (04-deliverable-types/):

- memos.md, emails.md, briefs.md, reports.md
- proposals.md, one-pagers.md, executive-summaries.md, business-letters.md

**Impact Techniques** (07-impact-techniques/):

- number-plays.md - Quantification, ratios, before/after contrasts
- power-words.md - Emotional triggers by category
- rhetorical-devices.md - Rule of Three, anaphora, antithesis, cadence
- executive-impact.md - C-suite optimization, decision clarity

**Sales Techniques** (08-sales-techniques/):

- power-positions.md - IS-DOES-MEANS enhancement for sales proposals

**Stakeholder Review** (10-stakeholder-review/):

- 00-index.md - Overview of stakeholder review system
- executive-review.md - Executive perspective: decision-readiness, clarity, ROI
- technical-review.md - Technical perspective: accuracy, precision, logical consistency
- legal-review.md - Legal/compliance perspective: risk language, regulatory alignment
- marketing-review.md - Marketing perspective: persuasiveness, audience resonance
- end-user-review.md - End-user perspective: accessibility, plain language, actionability
- synthesis-guidelines.md - Multi-stakeholder feedback aggregation and conflict resolution

**Workflow** (workflow/):

- step-by-step-guide.md - Detailed sub-steps and validation checklists

### Scripts

**calculate_readability.py** - Measure Flesch score, paragraph length, visual elements

```bash
python3 scripts/calculate_readability.py <file_path>
```

## Quick Reference

| Deliverable | Length | Recommended Frameworks | Impact Techniques | Default Stakeholders |
|-------------|--------|----------------------|-------------------|----------------------|
| memo | 1 page | BLUF, Pyramid, SCQA | Number plays, anaphora | executive, end-user |
| email | 200-300 words | BLUF, SCQA | Power words in subject | end-user, marketing |
| brief | 1-3 pages | BLUF, Pyramid, SCQA | Rule of Three | executive, technical |
| report | variable | Pyramid, SCQA | Before/after contrasts | executive, technical, end-user |
| proposal | variable | FAB, PSB, Pyramid | All techniques | executive, legal, marketing |
| one-pager | 1 page | PSB, FAB | Rule of Three, power words | marketing, executive |
| executive-summary | 1-2 pages | BLUF, Pyramid | Executive impact | executive, technical |
| business-letter | 1 page | Direct/Indirect | Trust words |
| blog | 800-1500 words | Inverted Pyramid, SCQA | Number plays, power words in CTA |

## Impact Techniques Quick Reference

### Number Plays Cheat Sheet

```text
Vague → Specific: "many customers" → "2,847 customers"
Percent → Ratio: "25% fail" → "1 in 4 fail"
Compound Impact: "10 hrs/week × 52 weeks × 5 people = $130K recovered"
Before/After: "Error rate: 12% → 0.3% (40x improvement)"
```

### Power Words by Category

| Urgency | Exclusivity | Trust | Achievement |
|---------|-------------|-------|-------------|
| now | exclusive | proven | breakthrough |
| deadline | insider | guaranteed | transform |
| limited | select | validated | accelerate |
| immediate | elite | certified | unlock |

### Rhetorical Patterns

```text
Rule of Three: "Reduce cost. Improve speed. Maintain quality."
Anaphora: "We deliver results. We deliver on time. We deliver beyond expectations."
Antithesis: "This isn't a cost—it's an investment."
Cadence: "After eighteen months of development—we're ready."
```
