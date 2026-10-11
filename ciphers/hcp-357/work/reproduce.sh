#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
python3 ciphers/hcp-357/work/baseline.py
c++ -O3 -std=c++17 ciphers/hcp-357/work/attack.cpp -o ciphers/hcp-357/work/attack
c++ -O3 -std=c++17 ciphers/hcp-357/work/multistage.cpp -o ciphers/hcp-357/work/multistage
ciphers/hcp-357/work/attack ciphers/hcp-357/work > ciphers/hcp-357/work/results.txt
ciphers/hcp-357/work/attack ciphers/hcp-357/work reverse > ciphers/hcp-357/work/results-reverse.txt
ciphers/hcp-357/work/attack ciphers/hcp-357/work normal cipher-full.txt > ciphers/hcp-357/work/results-full.txt
ciphers/hcp-357/work/multistage ciphers/hcp-357/work cipher.txt > ciphers/hcp-357/work/multistage-results.txt
ciphers/hcp-357/work/multistage ciphers/hcp-357/work cipher-full.txt > ciphers/hcp-357/work/multistage-full-results.txt

# Review1: test header-prefix-as-indicator-position hypothesis.
ciphers/hcp-357/work/attack ciphers/hcp-357/work normal cipher-group6.txt > ciphers/hcp-357/work/results-group6.txt
ciphers/hcp-357/work/attack ciphers/hcp-357/work reverse cipher-group6.txt > ciphers/hcp-357/work/results-group6-reverse.txt
