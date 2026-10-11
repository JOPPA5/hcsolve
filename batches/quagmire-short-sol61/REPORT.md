# HCP332 short restricted keyword QI/QII/QIII scouts

No supported solution. Twelve fresh source-length controls, five exact recoveries and seven failures. Ten gated targets remain incoherent; word fragments are not a decipherment. No source/marker changed.

Source has43characters (TRC3+40body), not46. Source43whole and hypothetical40prefix omission each independently calibrated atT3/T9 for QI/QII/QIII. No erasures and no added letters. All absolute shifts free. Same frozen18,098TRAIN keyword alphabet dictionary and language pipeline as prior batch; no truth initialization. Full model definitions and ACA orientation checks inherited from batches/quagmire-keywords-12-sol61; QIII keys both sides.

| N | Model | T | Exact letters | Full26 maps |
|---:|---|---:|---:|---|
| 43 | Q1 | 3 | 43/43 | True |
| 43 | Q1 | 9 | 2/43 | False |
| 43 | Q2 | 3 | 0/43 | False |
| 43 | Q2 | 9 | 43/43 | True |
| 43 | Q3 | 3 | 43/43 | True |
| 43 | Q3 | 9 | 3/43 | False |
| 40 | Q1 | 3 | 40/40 | True |
| 40 | Q1 | 9 | 3/40 | False |
| 40 | Q2 | 3 | 0/40 | False |
| 40 | Q2 | 9 | 5/40 | False |
| 40 | Q3 | 3 | 40/40 | True |
| 40 | Q3 | 9 | 7/40 | False |

Gate: highest5gram winner must recover every control plaintext letter. Five passes also recovered full26-letter phase maps. Failures have0–7matches, so restricted-family short-text recovery is demonstrably unreliable for other conditions. No target branch for those failed pairs. Independent ciphertext inverse/reencryption and scores checked on all320candidate rows perrun;22runs=7040rows.

Ten targets: whole43 QI3/QII9/QIII3 and conditional40 QI3/QIII3, each O/D source-supported alternative atbody position28 (0-based27). Only this glyph alternative and prefix framing varied; allsource letters remain literal. Source/work hashes match at completion.

| N | Model | T | Glyph | Score | Winner plaintext |
|---:|---|---:|---|---:|---|
| 43 | Q1 | 3 | o | -122.414 | jqftaakonarizibxveodidepjhcovjepomkfnnjwpbt |
| 43 | Q1 | 3 | d | -122.304 | rqaniyfzrhsdcklavteedsfurjmevedovolajtetoln |
| 43 | Q2 | 9 | o | -40.8176 | kidskzurotqnestrobitnuponasisovapostupodaty |
| 43 | Q2 | 9 | d | -33.0365 | oukyqlizavlnsypbridenavislednotistalabolipl |
| 43 | Q3 | 3 | o | -115.598 | tdakxsfpyhficeralneninaktoteleomlutaisezmrk |
| 43 | Q3 | 3 | d | -113.99 | zkkfqsanechmiratajszmjvyztisaneddnokymnqdaf |
| 40 | Q1 | 3 | o | -107.414 | taakonarizibxveodidepjhcovjepomkfnnjwpbt |
| 40 | Q1 | 3 | d | -107.304 | niyfzrhsdcklavteedsfurjmevedovolajtetoln |
| 40 | Q3 | 3 | o | -100.598 | kxsfpyhficeralneninaktoteleomlutaisezmrk |
| 40 | Q3 | 3 | d | -86.2524 | pckkvymishsnfteohsujhymtotojeprazarovenp |

AtT9 a43-character message provides fewer than five letters per phase. Language overfitting can produce fragments such as postup/podaty without whole coherence; these are not credible solutions. No historical attribution, family exclusion, missing plaintext, or source correction is claimed.

Fixtures, seeds, TRAIN/TESTsplit, candidate keys and fullsubstitution-map comparison are saved. Reproduce: python3 batches/quagmire-short-sol61/setup.py; clang++ -O3 -std=c++17 batches/quagmire-short-sol61/search.cpp -o batches/quagmire-short-sol61/search; python3 batches/quagmire-short-sol61/run.py. This writes only the batch.
