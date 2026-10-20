# HCP409 — reviewed decipherment using a transferred Kryha key

**All 295 observed letters decode with the previously reviewed Madrid key.** Claude Opus 5.5 independently confirmed the decipherment. REVIEW1 was REVISE for four source-transcription corrections; those are adopted below. The reviewer explicitly requires no second round after those corrections. Numerical rings, stops and initial displacement are unchanged.

## Origin and attribution

MZV message 80262/1944, 9 September 1944, Polyak to the Slovak legation in Madrid; Slovak National Archive in Bratislava, MZV, box 42. The cover originally types Bern, struck through and amended Madrid. The rendered General, Description and Attachments tabs were inspected on 19 October 2026: Not solved, category Unknown, World War II / Slovakia / Diplomacy. No attached transcript or plaintext was observed.

This is **key transfer**. The numerical rings and 23-stop mask come from the earlier reviewed HCP374 key, which was recovered using attributed public HCP373 context. No published plaintext for 409 was used in selecting its setting. Two bounded web queries found no relevant previous 409 solution; this is not proof of worldwide novelty. Sources and hashes are in SOURCES.md and work/key.json.

The content is the sender's propaganda message. Its descriptions of the uprising, alleged agents, and reported murder/arrest story are documentary assertions, not accepted historical facts.

## Reproduce

From repository root:

```sh
python3 ciphers/hcp-409/work/decrypt.py
```

Python 3 standard library. It verifies the immutable source hashes and the reviewed manual-transcription hash, then prints all 295 literal letters. It does not perform OCR. `--json` reports full coverage and exact re-encryption. `work/verify.py` independently uses absolute wheel coordinates and wrap counts and reproduces the same 295 letters, plus 598 mechanical control roundtrips. These implementation checks do not certify every historical symbol convention.

`work/transfer.py` ranks 3 fixed reviewed keys × 2 prefix choices × 23 phases × 26 displacements = 3,588 cases using generic Slovak four-grams. The unique coherent full-text setting is the Madrid 374 key, no prefix removal, phase 11 in its saved mask ordering, displacement 12. The omit-five version is merely the same decoded suffix at its advanced setting, not independent evidence. The reviewer's independent search of 598 settings also singles out the same setting.

## Working physical key

P and O map alphabetical A–Z labels to coordinates 0–25. Convention: O(cipher) = P(plain) + D modulo 26.

```text
P = 0 11 14 1 20 4 9 2 13 15 16 3 24 7 17 25 18 21 10 5 12 6 22 19 8 23
O = 0 4 1 21 8 3 19 15 13 18 25 10 22 16 2 12 5 23 7 20 11 14 17 24 9 6
Selected holes, zero-based, from the first observed letter:
4 5 8 11 13 17 20 21 24 26 29 31 34 37 40 42 44 45 47 48 49 51 2
Initial displacement = 12 modulo 26.
```

The 52 adjacent distances in key.json sum to 179. Decode by subtracting D from the cipher's output coordinate and locating the resulting input label. After each character, walk the physical edges to the next selected stop. The same 23-stop mask as 374 is cyclically listed from hole 4 rather than 34. The numerical key is unchanged. This establishes a mechanically consistent working Kryha interpretation, not unique original hardware or a reconstructed historical key schedule.

## Exact reviewed output — 295 letters

```text
NASLOVENSKUNIETVOBECCSLALEBOCESKYCHVOISKJSULENTLUPYZASKODNIKOVAZAVEDENISLOVACIKTORYMCESKIAWENTINAHOVORILIZEIDEOPOVSTANIEAKOPOMSTUZAZAVRAZDENIEPREZIDENTATISUAZATKNUTIESLOVVLADYJVSETKOOBYVATELSTVOSLOVENSKAOKREMSPOMENUTYCHCESKYCHAWETOVIEZASAMOSTATNOSTOCISTENIESLOVENSKASADAKONCUIEJOZNAMSLOVAKOMVUSA
```

This output retains the inherited canonical W at input coordinate 22 and J at 15. W occurs twice in A?ENT- contexts and is read as G; the unused old G coordinate never occurs. J appears at the three sentence boundaries, while word-internal J is represented by I. These interpretations are supported by the text and the review, but full historical labels of unused coordinates remain unrecovered. No numerical ring value is changed to apply them.

## Readable Slovak reconstruction — editorial

> Na Slovensku niet vôbec čsl. alebo českých vojsk. Sú len tlupy záškodníkov a zavedení Slováci, ktorým českí agenti nahovorili, že ide o povstanie ako pomstu za zavraždenie prezidenta Tisu a zatknutie slov. vlády. Všetko obyvateľstvo Slovenska okrem spomenutých českých agentov je za samostatnosť. Očistenie Slovenska sa dokončuje. Oznám Slovákom v USA.

Spaces, accents and punctuation are supplied. J is read as a sentence break; word-internal I may represent J, and coordinate 22 is read as G. The only remaining substantive repairs are **AWETOV → AGENTOV**, restoring the absent N as well as applying W/G, and **DAKONCUIE → DOKONČUJE**, correcting the literal A/O discrepancy. The readable paragraph is not the exact decoder output or a surviving archival draft.

## English translation of the reconstruction

> There are no Czechoslovak or Czech troops at all in Slovakia. There are only bands of saboteurs and misled Slovaks, whom Czech agents have told that this is an uprising in revenge for the murder of President Tiso and the arrest of the Slovak government. The entire population of Slovakia, except the aforementioned Czech agents, supports independence. The clearing of Slovakia is being completed. Inform the Slovaks in the USA.

## Source collation and remaining uncertainty

All positions in solver documentation and manifests are **one-based**. The review's finding-1 table is zero-based; add one to convert.

The first-pass transcript and complete DONE1 documentary state are preserved under work/round1-before-review/ and work/transcription-first-pass.txt. The reviewed transcript adopts these four further source readings:

| Position, one-based | Before review | Reviewed reading | Result |
|---|---|---|---|
| 121 | L in LHGUL | H in HHGUL | RKO becomes AKO |
| 161 | E in EXZVO | A in AXZYO | ZATM… becomes ZATK… |
| 164 | V in EXZVO | Y in AXZYO | …NUSIE becomes …NUTIE |
| 224 | E in IIAEY | A in IIAAY | CESKKCH becomes CESKYCH |

The review's crops and original pixels support these corrections; this reinspection was plaintext- and reviewer-assisted, not blind. Source bytes are unchanged. The earlier Y→V change at 164 was wrong and is expressly reversed. QMQHH remains unchanged: it reads KTORYM. The earlier H/L alternative is not retained as an equal default after review.

The scan's **handwritten** count appears 300, while its 59 visible five-letter groups contain 295 letters. A clerk's check or charging count is plausible; it is not evidence of a missing group. The decoded text has a complete beginning and ending. No unseen group or indicator is invented, and no source letter is omitted from decoding.

AWETOV and DAKONCUIE remain literal. They are supported source readings under the frozen key, unlike the four corrected transcription errors. The absent N is consistent with omission during preparation/encryption, but its precise historical cause is not independently established. Unused input labels, historical preparation conventions and unique hardware settings remain open.

## Response to review 1

**REVISE addressed; no second review round required by the reviewer.**

1. Adopted all four source corrections, regenerated the working transcription, its SHA-256, literal plaintext, search output and report. RKO, ZATMNUSIE and CESKKCH are withdrawn as alleged original garbles: they were our transcription errors. The key is unchanged.
2. Retained only AWETOV and DAKONCUIE as substantive literal irregularities. Restoring their intended words is editorial. Historical error attribution remains qualified.
3. Preserved W/G and J-boundary interpretations with the stronger contextual support described by the reviewer. Unused labels remain canonical.
4. Corrected the count description to handwritten and removed any implication that an absent initial group is evidenced.
5. Made numbering explicit. The original solver JSON already listed its first-pass changes one-based (including 164); the review used zero-based 163 in its table. The new manifest labels the convention directly.
6. Retained the limited prior-solution search wording and the attribution of the transferred key to the published 373 context.

The original review and REVIEWED1 marker are unchanged. The final PDF records the corrected text, working key, source scans, limitations and review response. The register entry names Tomáš Pavuk as the solver; it is submitted to the AI Decipherment Register by him.
