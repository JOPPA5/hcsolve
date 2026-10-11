#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
python3 ciphers/hcp-351/work/analyze.py
python3 ciphers/hcp-351/work/diagnostics.py
c++ -O3 -std=c++17 ciphers/hcp-351/work/vigenere.cpp -o ciphers/hcp-351/work/vigenere
ciphers/hcp-351/work/vigenere ciphers/hcp-351/work
