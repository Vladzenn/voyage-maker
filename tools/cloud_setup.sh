#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 --version
node --version
python3 tools/project.py validate
python3 tools/project.py sync --check
node tools/test_item_mechanics.cjs
node tools/test_adventurers.cjs
node tools/test_creation.cjs
python3 tools/test_validation.py
