# Unsolved attempt — HC Portal351
Solver: OpenAI GPT-6 Astra, 2026-10-11.

No key, cipher-type identification or plaintext has been recovered. No translation of the encrypted message is available. No review marker or registration is warranted.

## Source
Portal identifies MZV message3002/1944, 3November1944, sender Cieker, recipient MZV Bratislava, archive MZV box42. Status is Not solved; tag Unsolvable and title "Nerozlúštiteľný telegram" are recorded faithfully, not endorsed as mathematical impossibility. All three tabs were inspected by the parent solver; original image is preserved unchanged. No supplied decipherment or transcription was encountered.

The portal date is disputed by the source image: the round arrival postmark appears to read2.III.44−23. That is an independently checked image reading, not permission to overwrite the portal metadata or a proven dispatch date. Source-collation evidence is in `batches/framing-source-audit-sol61/REPORT.md`. A human-supplied review identifies a strong350[i]→351[i+1] relationship with period23, independently reproduced in `batches/kryha-shift23-sol61/scan.json`. The earlier whole-pair reset/offset0 searches do not test that shifted relationship; recovery of its cycle, source discrepancies and physical settings is now the priority. No plaintext is claimed.

## Attempt
I manually transcribed77 groups (385letters) in work/transcription.txt. Several typed glyphs are faint or obscured; NOTES.md lists uncertainties. Letter IC0.03908 is near the uniform26-letter value; this does not identify a cryptosystem. Basic rectangle readings, period diagnostics and a Slovak-fourgram-scored Vigenere annealing search at periods1–30 did not yield coherent plaintext.

Reproduce these **attempts**, from the repository root:

```sh
sh ciphers/hcp-351/work/reproduce.sh
```

Requires Python3 and a C++17 compiler. The command consumes a manual working transcription, not automatic OCR of source, and does not produce verified plaintext. All scored candidate outputs are retained; isolated language-looking fragments are not treated as recovered text.

## Limits
Transcription needs independent validation. Search covered only simple transposition readings and standard A–Z periodic additive Vigenere under one Slovak language model. Other cipher families, key mismatches or transmission errors are possibilities, not established explanations. There is no defensible full or partial decipherment claim.

## Calibrated two-ring Kryha attempt

Independent385letter held-out Slovak control was exactly recovered using projected-IC→MASC language ranking→joint refinement with both rings unknown; reproduced evidence copied towork. 
Full351 baseline completed34 phase/sign cases,10200 IC candidates, MASC8×30k each and top language seed joint8×100k. Best joint score-413.007 atphase6/sign1; bestMASC-461.099. All are incoherent; exact re-encryption of385 baseline letters is key-fit consistency only. Heuristic failure doesnotexclude early17step Kryha. Candidatekeys/outputs and budgets retained in ring-ic-target-report.json and per-case directories. No DONE.
 The baseline literal transcription is unchanged. Uniform two-press control also recovers385/385, but that is a different conditional model; target scout outputs are not claims of historical adoption.

## Selective plaintext-J stepping control, no target inference

A separate conditional simulator skips an extra consecutive selector step after each literal plaintext J. This interpretation follows the primary wartime memo's J rule but its original17step instantiation and adoption for Slovak traffic are unproved. A German TEST control uses J-separated word tokens and preserves natural J; independently randomized rings and phase11. With the output ring supplied and input J position fixed, frozen German5gram scoring recovers ALL385letters including70J; independent reencryption exact. Quad scoring failed370/385 because a false candidate outranked truth.

Four attempts with unknown output ring failed that same control: sequential IC, partial-ring unigram beam, partial-ring renewal beam, and binary J/nonJ path beam with repeatedsymbol domains and exact matching feasibility. Therefore no selective-J target attack or exclusion is supported. Known-output success validates only the limited model. All controls, failures and budgets are saved inwork andNOTES; reproduce with `sh ciphers/hcp-351/work/reproduce-selective-j-control.sh`.

## Uniform doublepress350 conditional scout completed

All34 phase/sign cases on literal385letter350, read-onlyinput, alloutputs stored351/work. Same validated budgets:3000×10k IC,300 retainedO eachcase, MASC8×30k each, top language seed joint8×100k. Total10200 candidates. Independent doublepress control recovered385/385; best target joint-413.29 phase4 sign-1, bestMASC-464.889. Outputs incoherent, no supported plaintext/key; exact completebaseline reencryptions are only key-fit checks. This uniformtwo-press model is conditional and differs from the primary memo selectiveJ mechanism. Heuristicfailure not exclusion; historicalSlovakadoption unproved. Report work/ring-double-target350-report.json. No351 doublepress scout requested after parent cap350only; no sourceedits/watchers/DONE.
