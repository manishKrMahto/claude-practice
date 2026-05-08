---
name: csv-cleaner
description: >
  Cleans, validates, and reformats CSV/TSV files. Use this skill whenever
  the user mentions messy data, fixing spreadsheets, removing duplicates,
  standardizing column headers, handling missing values, or cleaning any
  .csv or .tsv file.
---

# CSV Cleaner Skill

## What this skill does
Reads a CSV file, fixes common issues, and outputs a clean version.

## Steps to follow
1. Read the uploaded file using pandas
2. Standardize column headers (lowercase, underscores)
3. Remove duplicate rows
4. Fill or flag missing values
5. Output a cleaned .csv to /mnt/user-data/outputs/