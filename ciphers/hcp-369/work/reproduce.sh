#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
python3 ciphers/hcp-369/work/inventory.py
c++ -O3 -std=c++17 ciphers/hcp-369/work/substitution.cpp -o ciphers/hcp-369/work/substitution
c++ -O3 -std=c++17 ciphers/hcp-369/work/columnar.cpp -o ciphers/hcp-369/work/columnar
ciphers/hcp-369/work/substitution ciphers/hcp-369/work
ciphers/hcp-369/work/substitution ciphers/hcp-369/work reverse
python3 ciphers/hcp-369/work/columnar_cases.py
