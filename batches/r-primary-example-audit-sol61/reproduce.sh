#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
b=batches/r-primary-example-audit-sol61
python3 "$b/audit.py"
python3 "$b/audit-collated.py"
python3 "$b/alignment-audit.py"
clang++ -O2 -std=c++17 "$b/existing-cpp-audit.cpp" -o "$b/existing-cpp-audit"
clang++ -O2 -std=c++17 "$b/existing-shared-inverse-audit.cpp" -o "$b/existing-shared-inverse-audit"
"$b/existing-cpp-audit" > "$b/existing-cpp-audit.txt"
"$b/existing-shared-inverse-audit" > "$b/existing-shared-inverse-audit.txt"
