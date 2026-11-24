#!/bin/sh
# Smoke test: run the entry program twice and verify /output/entry.txt is valid.
set -e
python3 main.py
python3 - <<'EOF'
from pathlib import Path
t = Path("/output/entry.txt").read_text(encoding="utf-8")
assert t.strip(), "entry is blank"
assert 1 <= len(t) <= 200, len(t)
assert "\n" not in t.strip()
print("OK", len(t), "chars:", t)
EOF
