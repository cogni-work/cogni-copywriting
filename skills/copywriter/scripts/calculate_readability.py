#!/usr/bin/env python3
"""
Calculate readability metrics for markdown documents.

Usage:
    python3 calculate_readability.py <file_path>

Returns JSON with:
- flesch_score: Flesch Reading Ease score (0-100, target 50-60)
- avg_paragraph_length: Average sentences per paragraph (target 3-5)
- total_paragraphs: Number of paragraphs in document
- visual_elements: Count of tables, callouts, lists, bold sections
- header_levels: Max header depth (target ≤3)
"""

import sys
import re
import json


def count_syllables(word):
    """Estimate syllable count for a word."""
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    previous_was_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            count += 1
        previous_was_vowel = is_vowel

    # Adjust for silent 'e'
    if word.endswith('e'):
        count -= 1

    # Ensure at least 1 syllable
    if count == 0:
        count = 1

    return count


def calculate_flesch_score(text):
    """Calculate Flesch Reading Ease score."""
    # Remove markdown formatting but keep text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)  # Links
    text = re.sub(r'[*_`#>-]', '', text)  # Markdown symbols

    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return 0

    # Count words
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0

    # Count syllables
    total_syllables = sum(count_syllables(word) for word in words)

    # Flesch Reading Ease formula
    # 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words)
    total_words = len(words)
    total_sentences = len(sentences)

    avg_words_per_sentence = total_words / total_sentences
    avg_syllables_per_word = total_syllables / total_words

    score = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)

    return round(score, 1)


def analyze_document(file_path):
    """Analyze markdown document for readability metrics."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]

    # Calculate Flesch score
    flesch_score = calculate_flesch_score(content)

    # Analyze paragraphs
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip() and not p.strip().startswith('#')]
    total_paragraphs = len(paragraphs)

    if total_paragraphs > 0:
        total_sentences = sum(len(re.split(r'[.!?]+', p)) - 1 for p in paragraphs)
        avg_paragraph_length = round(total_sentences / total_paragraphs, 1)
    else:
        avg_paragraph_length = 0

    # Count visual elements
    visual_elements = 0

    # Tables
    visual_elements += len(re.findall(r'\|.*\|', content))

    # Callouts (blockquotes with bold text)
    visual_elements += len(re.findall(r'>\s*\*\*', content))

    # Bullet/numbered lists (count list blocks, not individual items)
    list_blocks = re.findall(r'(\n[-*+\d]+\.?\s+.+(\n[-*+\d]+\.?\s+.+)*)', content)
    visual_elements += len(list_blocks)

    # Bold emphasis sections
    visual_elements += len(re.findall(r'\*\*[^*]+\*\*', content))

    # Section dividers
    visual_elements += content.count('---')

    # Analyze header hierarchy
    headers = re.findall(r'^(#+)\s', content, re.MULTILINE)
    max_header_level = max(len(h) for h in headers) if headers else 0

    return {
        "flesch_score": flesch_score,
        "avg_paragraph_length": avg_paragraph_length,
        "total_paragraphs": total_paragraphs,
        "visual_elements": visual_elements,
        "header_levels": max_header_level
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python3 calculate_readability.py <file_path>"}))
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        result = analyze_document(file_path)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
