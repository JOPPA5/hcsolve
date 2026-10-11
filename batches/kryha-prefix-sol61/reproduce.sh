#!/bin/sh
set -eu
cd /Users/tomaspavuk/Desktop/hcsolve
python3 batches/kryha-prefix-sol61/scout.py
python3 batches/kryha-prefix-sol61/controls.py
python3 batches/kryha-prefix-sol61/verify-body.py
