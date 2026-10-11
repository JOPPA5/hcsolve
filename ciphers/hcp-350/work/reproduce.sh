#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
python3 ciphers/hcp-350/work/classical.py
c++ -O3 -std=c++17 ciphers/hcp-350/work/substitution.cpp -o ciphers/hcp-350/work/substitution
ciphers/hcp-350/work/substitution ciphers/hcp-350/work
ciphers/hcp-350/work/substitution ciphers/hcp-350/work reverse
