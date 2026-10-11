#!/bin/sh
set -eu
cd /Users/tomaspavuk/Desktop/hcsolve
B=batches/kryha-procedure-sol61
pdftotext -layout batches/kryha-wheel-sol61/source/nr2417.pdf "$B/nr2417.txt"
pdftotext -f 187 -l 192 -layout batches/kryha-wheel-sol61/source/NSAmilitaryCryptalyticsPt3_1977.pdf "$B/nsa-kryha-excerpt.txt"
pdftotext -f 190 -l 190 -layout batches/kryha-wheel-sol61/source/NSAmilitaryCryptalyticsPt3_1977.pdf "$B/nsa-page185.txt"
pdftotext -f 193 -l 209 -layout batches/kryha-wheel-sol61/source/NSAmilitaryCryptalyticsPt3_1977.pdf "$B/nsa-kryha-analysis-excerpt.txt"
pdftoppm -f 1 -l 1 -scale-to 1600 -png -singlefile batches/kryha-wheel-sol61/source/nr2417.pdf "$B/nr2417-page1"
pdftoppm -f 14 -l 15 -scale-to 1600 -png batches/kryha-wheel-sol61/source/nr2417.pdf "$B/nr2417-end"
pdftoppm -f 190 -l 190 -scale-to 1600 -png -singlefile batches/kryha-wheel-sol61/source/NSAmilitaryCryptalyticsPt3_1977.pdf "$B/nsa-page185"
