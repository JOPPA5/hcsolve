#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 prepare.py
c++ -O3 -std=c++17 vigenere.cpp -o vigenere
./vigenere . control-cipher.txt > control-results.txt
python3 analyze.py > analysis-summary.txt
python3 structure.py > structure-summary.txt
