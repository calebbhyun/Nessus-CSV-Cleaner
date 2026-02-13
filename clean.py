import csv
import sys
import re
import argparse

# Increase field size limit for large Nessus fields
csv.field_size_limit(10**9)

WS = re.compile(r"\s+")

# Excel limit is 32767 → keep safely below it
MAX_CHARS = 30000

def clean_cell(v: str) -> str:
    if v is None:
        return v

    # collapse whitespace
    v = WS.sub(" ", v).strip()

    # truncate long values
    if len(v) > MAX_CHARS:
        v = v[:MAX_CHARS] + " [TRUNCATED]"

    return v

def main():
    parser = argparse.ArgumentParser(
        description="Clean Nessus CSV by removing embedded newlines and collapsing whitespace."
    )
    parser.add_argument("input_file", help="Input Nessus CSV file")
    parser.add_argument("output_file", help="Output cleaned CSV file")

    args = parser.parse_args()

    with open(args.input_file, "r", newline="", encoding="utf-8-sig") as infile, \
         open(args.output_file, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)

        if reader.fieldnames is None:
            raise RuntimeError("Could not read CSV headers.")

        writer = csv.DictWriter(
            outfile,
            fieldnames=reader.fieldnames,
            quoting=csv.QUOTE_MINIMAL,
            lineterminator="\n",
        )

        writer.writeheader()

        for row in reader:
            for k in row:
                row[k] = clean_cell(row[k])
            writer.writerow(row)

if __name__ == "__main__":
    main()
