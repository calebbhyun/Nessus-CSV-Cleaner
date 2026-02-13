# Nessus CSV Cleaner

A small Python script to clean **Tenable Nessus** CSV exports by removing embedded newlines and collapsing whitespace inside fields.

Nessus often exports long multi-line values (Plugin Output, Description, Solution, etc.), which can break CSV parsing or make files appear corrupted in spreadsheets. This script normalizes the data so each record is written as a single line.

---

## Features

- Handles very large Nessus fields (raises CSV size limit)
- Removes embedded newlines, tabs, and repeated spaces
- Preserves valid CSV structure
- Works with large scan files
- Simple command-line usage

---

## Requirements

- Python 3.x  
- No external dependencies (uses only the standard library)

---

## Usage

```bash
python3 clean.py input.csv output.csv
```

---

## Example (Large Output)

Update split -l value accordingly.

```bash
python3 clean.py export.csv clean.csv
cat clean.csv | wc -l
h=$(head -n1 clean.csv); tail -n +2 clean.csv | split -l 20000 - chunk_ && for f in chunk_*; do { printf "%s\n" "$h"; cat "$f"; } > "$f.csv" && rm "$f"; done
```
