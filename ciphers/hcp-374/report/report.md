# HC374: Madrid telegram

The message body and a working Kryha key have been recovered. The deciphered body contains 80 letters. KIDAH is the shared indicator associated with the same starting state as telegram 373; how its letters encode that setting remains open. Historical uncertainties are stated explicitly.

## Origin and content

MZV message 80174/1944, 20 May 1944, Šulík to the Slovak legation in Madrid. Slovak National Archive, MZV, box 42. Portal status at acquisition: Not solved. The scan prints a count of 85 and seventeen five-letter groups. The title describes a request to repeat the last 15 groups of 80172; the new 80-letter block is not claimed to be exactly the same 75-letter slice.

Public Solved telegram 373 (80172/1944, 17 May 1944) supplied an archival clear-text draft and ciphertext. Its final sentence provided the known plaintext for recovering the machine key. The commercial content was already published in that source; the new work is key recovery and its transfer to 374.

## Literal output from the independent transcription

```text
AUPOZORNUIESPANLELSKEPROTIBODAVKYUZPEVNEKUPENENAZAKLADEPOVODNYCHCIENCELULOZYXXXX
```

Separate indicator: KIDAH, shared with 373 and its machine starting state. The reviewed default at source position 35 is N; alternative M gives PROTIBODVVKY. SPANLELSKE and PROTIBODAVKY preserve two garbled letters in this copy. Source letters are not edited to obtain correct words. XXXX is X padding, supported by sentence-ending X and terminal XX in 373.

## Readable Slovak reconstruction from the published draft

A upozorňuje španielské protidodávky už pevne kúpené na základe pôvodných cien celulózy.

English translation: And points out that the Spanish counter-deliveries have already been firmly purchased on the basis of the original cellulose prices. This is a content reconstruction supported by the published draft, not an error-free literal machine output.

## How the key was recovered

The final 186-letter sentence of 373 contains no numerals. Sliding it through the complete ciphertext and testing periods 2-52 produces one witness in 94,656 cases: J normalized to I, no Q wrapper, offset 462, period 23. All 183 non-erased equations agree. Three independent physical control messages are recovered in full. Two distinct audits confirm one compatible 23-stop mask on the 52-hole wheel.

Of all 598 phase/displacement pairs for 374, phase 3 and shift 8 are uniquely strongest: the reviewed reading matches 74 of 76 content letters; the next candidate matches 21, median 3. Independent source readings predate key recovery. The same key reads the entire 645-letter body of 373, including 459 letters outside the fitted 186-letter span. Running Slovak with spelled-out numbers and sentence-ending X strongly validates the key; literal source errors remain.

## Working physical key

P and O map letters to coordinates 0-25; O(c)=P(p)+d modulo 26. P(A)=O(A)=0 is a coordinate convention. The table canonically completes unused F/G/J/Q/W labels; their historical positions were not recovered. M at 24 is supplied by held-out MADRID in 373; sentence boundaries and terminal XX support X at 19. Unused completions do not affect the body of 374.

| Letter | A | B | C | D | E | F | G | H | I | J | K | L | M |
| P | 0 | 11 | 14 | 1 | 20 | 4 | 9 | 2 | 13 | 15 | 16 | 3 | 24 |
| O | 0 | 4 | 1 | 21 | 8 | 3 | 19 | 15 | 13 | 18 | 25 | 10 | 22 |

| Letter | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| P | 7 | 17 | 25 | 18 | 21 | 10 | 5 | 12 | 6 | 22 | 19 | 8 | 23 |
| O | 16 | 2 | 12 | 5 | 23 | 7 | 20 | 11 | 14 | 17 | 24 | 9 | 6 |

Selected holes in walking order from the first body letter, ZERO-BASED indices 0-51 (add 1 for human hole labels 1-52):

```text
34 37 40 42 44 45 47 48 49 51 2 4 5 8 11 13 17 20 21 24 26 29 31
```

Initial displacement 1 modulo 26, equivalent to 27. After each letter, walk adjacent edges to the next selected hole. The 52 adjacent distances are:

```text
4 3 4 3 3 3 4 3 4 4 3 3 3 3 4 4 3 3 4 3 3 4 3 3 4 3 3 4 4 4 3 3 4 3 3 3 4 3 4 3 3 4 5 3 3 3 3 4 3 3 4 5
```

One revolution sums to 179. Decode by subtracting the current displacement from O and locating the resulting coordinate in P. The historical dial setting, indicator coding and unused alphabet labels are not established. Mask uniqueness applies only to this geometry and the frozen recovered schedule.

## Reproduction and independent verification

```text
python3 ciphers/hcp-374/work/decrypt.py
```

Run from the repository root. Python checks the original JPEG and manual-transcription hashes; it does not perform OCR. It returns all 80 body letters and the indicator separately. --alternate-35-m selects the other reading. A separate verify.py uses absolute coordinates and wrap counts. An internal GPT-6.1 Sol audit used its own continuous physical algorithm without importing these functions: both complete 80-letter readings re-encode exactly to their source transcriptions.

## Independent review and remaining limits

Claude Opus 5.5: ACCEPT, no second round required. His independent decoder verified the complete body, all 598 settings and the body of 373. Changes after review: default N at 35 with M retained, the 459-letter held-out test, observed X preparation and two garbles in this copy. Extending the requested 15 groups to a word boundary and repadding yields 16; this is an explanatory inference. Full responses are in SOLUTION.md.

Readers prefer G/Q/V at source positions 9/25/60. At 35, the reviewed default is the older independent N; the newer M reading remains an alternative. Source 21 S and 32 L are not changed to W/A: they are garbles in this copy, with their cause unresolved. The updated review confirms shared KIDAH and the same starting state (first selected stop, displacement 1). The sentence begins after 567 body emissions in 373, but from the start in 374: zero of 76 ciphertext letters agree, versus 74 plaintext letters. It was re-enciphered, not copied; indicator coding remains open. No register entry is written without separate human authorization because the content was already public.

Sources: crypto.hcportal.eu/dashboard/cryptograms/374 and /373; all three rendered tabs and attachments recorded in SOURCES.md. Antal/Zajac/Grošek, Diplomatic Ciphers Used by Slovak Attaché During the WW 2, HistoCrypt 2020; wheel geometry from Callimahos, Military Cryptanalytics Part III, §52. Main solver: OpenAI GPT; mathematical recovery and internal audits: GPT-6.1 Sol; external reviewer identified in REVIEW 1.md.

## Original document 374

Unmodified archival image from the recorded portal attachment. The manual transcription and its alternatives are kept separate from the image.

![Original scan](/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-374/source/cryptogram.jpg)
