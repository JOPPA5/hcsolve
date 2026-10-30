# HCP 1391 / pc_hcp_72 — partial reading

**Not a complete solution (PARTIAL).** Message lines 1-2 plus isolated groups of lines 3-7 are frozen (44 letters, updated 2026-10-29). Several groups of lines 3-7 and the terminal ornament remain unresolved.

## Source and context

Public HC Portal postcard, status Not solved when root read General, Description and Attachments on 2026-10-26. Portal date 1907-05-11, private collection, recipient recorded as W. Abboú. Both original scans and rendered metadata are preserved in `source/`; exact links are in SOURCES.md. No attached solution was observed. Picture caption: “River Stour & Bridge, Blandford.”

I personally inspected both scans. The address-side message is read after rotating the supplied image 270° clockwise. Transcription is manual, not supplied or OCR-derived. The initial Caesar hypothesis came from root's collection-family observation, then was checked on this card's visible letters.

## Method and key

Caesar substitution, decrypt each ciphertext letter one position backward, wrapping A→Z. Upper/lower case is preserved by the decoder; capitalisation in the handwritten transcript is not used to infer content.

```
Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain:  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

This whole alphabet is the tested shift rule; the card's frozen excerpt does not attest every alphabet letter.

## Frozen manual transcription and plaintext

```
Nz Pxo Efbsftu
Nboz uibolt gps
```

```
My Own Dearest
Many thanks for
[five lower message lines not reliably transcribed]
```

Slovak translation of the excerpt: „Moja najdrahšia / veľmi ďakujem za …“ It does not supply the object of the thanks or any missing closing.

## Reproduction

From repository root:

```
python3 ciphers/hcp-1391/work/decode.py
```

The command checks SHA-256 hashes of all three unchanged source files, reads `work/transcription.json`, and reproduces exactly these 25 manually transcribed letters. It cannot transcribe the scan automatically or produce full plaintext from pixels. Its output explicitly labels partial scope.

## Evidence and limits

The same shift maps all 25 frozen letters to coherent English salutation and thanks; the words agree with the visible ink. That establishes a reliable excerpt and plausible cipher mechanism. It does not establish lower unseen letters. Faded writing and watermark overlap leave five message lines unresolved, and their length is not frozen. Possible SWEET, HAVE and OWN readings in those lines remain hypotheses and are excluded from coverage. Date/address and the terminal hatch/monogram are not decoded here. No DONE, FINAL, register entry or report is warranted.

## Update 2026-10-29 — Claude Opus 5.5 (continuing the GPT-6 Astra partial work above)

Still **partial**; no DONE marker. Newly frozen from enlarged crops (`work/crops/`), all under the same Caesar -1 key:

```
L1  Nz Pxo Efbsftu          My Own Dearest
L2  Nboz uibolt gps         Many thanks for
L3  [dvs?:] [?p.] [J?] pomz [unread] only
L4  Ibwf [uij?] [p?f?] ...  Have [unread] ...
L5  [?oe.] [Ibs?] ...       [unread]
L6  [M x/y Z/c] gspn Zpvs   [initial group, cf. hcp-1390 "M xx"] from Your
L7  Pxo [Mh.] [faint word] [ornament]   Own [abbrev.] [unread; perhaps "Girl" as on hcp-1390]
```

`python3 ciphers/hcp-1391/work/decode.py` (from repo root) now checks source hashes and reproduces these 44 letters. Sketched reading: "My own dearest, many thanks for [...] only have [...] from your own [..] [girl?]". Slovak: „Môj najdrahší, veľká vďaka za [...] len mám [...] od tvojej vlastnej [...]“. Context hypotheses (CARD, I ONLY HAVE THIS ONE, AND, HARD, GIRL) are recorded in NOTES.md but not adopted, because the pixels (≈10 px per letter, watermark and faded ink) do not support them letter by letter.
