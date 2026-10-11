#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 prepare.py
python3 alternatives.py
python3 exact_periodic.py
python3 playfair_invariant.py
