#!/usr/bin/env python3
"""Safety-first EBPro CSV bridge: inspect export and request real column mapping.
Does NOT invent vendor CSV headings or field encodings. Returns actionable failure.
"""
from argparse import ArgumentParser
from csv import DictReader
from pathlib import Path

p=ArgumentParser()
p.add_argument("--template",required=True)
p.add_argument("--source",default="tags/resource-manager-dictionary.csv")
p.add_argument("--output",required=True)
args=p.parse_args()
with Path(args.template).open(encoding="utf-8-sig",newline="") as f:
    sample=DictReader(f); columns=sample.fieldnames or []; first=next(sample,None)
with Path(args.source).open(encoding="utf-8-sig",newline="") as f:
    source=DictReader(f); fields=source.fieldnames or []
print("EBPro exported columns:", columns)
print("Engineering dictionary columns:", fields)
print("First exported row:",first)
raise SystemExit("Import conversion deliberately blocked: exact EBPro exported type/address columns and sample rows must be verified before writing --output; no fabricated import file.")
