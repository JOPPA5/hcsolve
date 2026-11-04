ACCEPT

# Review 1 – hcp-954 (Claude Opus 5.5, reviewer, 2026-11-03)

## What I verified and how

1. Ran the command from SOLUTION.md (`python3 -I ciphers/hcp-954/work/decode.py`, repo root).
   All four SHA-256 checks print OK; the letter stream is
   `BESTENDANKFÜRDEINELIEBENKARTENWIESEHNEICHMICHZUDIRMEINEGUTEMICHLIEBEDICHDOCHSOSEHRMEINENBRIEFHASTDUDOCHERHALTENFREUNDLICHEGRÜSZEEWIGDEINCARL`
   and the built-in segmentation assert passes. It matches the plaintext in SOLUTION.md.
2. Independent transcription and decoder: `review/work/indep_decode.py` holds my own reading
   of the 12 pencil lines, made from my own crops of `work/hires/..._pic.jpg`
   (`review/work/c_top.png`, `c_l3_6.png`, `c_mid.png`, `c_bottom.png`, `c_gruesze.png`,
   made with `review/work/crop.py`). Decoding with A=1…Z=25 (no J) gives the same stream; my
   number sequence is identical to the solver's (140 numbers, check printed "identical: True").
3. Key: one fixed J-less alphabet; values used 1–14, 17–20, 22, 25; no conflicts, no unused or
   unexplained number. The key is self-evident (9 3 8 = ICH occurs four times, 4 9 3 8 = DICH,
   12 9 3 8 = MICH).
4. Pixels, sign by sign at the disclosed hard spots:
   - Line 1 "6 : 2ü 17": the two dots over the 20 are clearly visible (FÜR). Line 10 "20" in
     GRÜSZE also has the dots.
   - Line 7 HAST: the first sign is a tall, angular 8 with an open top (similar to the 8 in
     "18 19" next to it); 8 = H is the natural reading, not forced.
   - Line 8 DOCH: "4 1x 3 8" – the second sign is small, r/x-shaped, consistent with the
     x-shaped 4 in FREUNDLICHE ("13 x 11"), and the 3 is written over another figure. Disclosed.
   - Line 10 GRÜSZE: "7 17 2ü 18 2" clear; after the 2 only a faint hook at the leaf edge, then a
     darker 5 whose flag runs into a long stroke that ends as a slash. Reading 25 5 (ZE) needs the
     faint hook to be a 5; the alternative is "2 5" with one 5 (GRÜSBE / GRÜS2E) – the
     solver's call is the only one giving a word and is disclosed.
   - Ordinary rows 2–6 and 9, 11, 12 checked in full: every figure and slash matches the
     transcription.
5. Language and context: fluent German of the period (Kurrent-era love card), "Grüsze" for
   Grüße is a normal Latin-script spelling of ß, signature Carl, "meine gute M." fits the
   addressee Martha Ihnken. Address side (plain Kurrent: Fräulein Martha Ihnken, bei Frau Wwe.
   Ihnken, Jever, Oldenburg; Heide 6.7.02, arrival 7.7.02) checked on the hi-res scan; it is
   not enciphered.
6. Published solution: none recorded; I have no evidence of one. Portal status "Not solved".
7. Translations (English, Slovak) are faithful.

## Findings

1. (minor) Number count. SOLUTION.md says "12 lines, 147 numbers"; the transcription has
   140 number tokens (both my count and the solver's file). Correct the figure.
2. (minor) Position of the "?". The question mark is written at the right end of line 8,
   after "…19 5 13" (ERHALTEN?), near the rose; the transcription puts it at the end of line 7
   after "4 20 /". No effect on the plaintext, but the transcription should place it where it
   is.
3. (minor) Steganography / stamp. In this collection hidden messages under the stamp are
   common (cf. the Jolánka series). The stamp on this card is still attached, so nothing under
   it can be inspected from the scan; SOLUTION.md says this (point 6). Keep that statement in
   the report and do not add "Steganography" to the type: nothing hidden is visible, so the
   register type stays MASC.
4. (minor) GRÜSZE ending: say plainly in the report that the faint second figure of 25 is the
   one call that rests on word sense (already in uncertainty 2; keep it).

## What I could not verify

- The area under the stamp (stamp present; scan only).
- The street line of the address (under the HCPortal watermark), which is not part of the message.
- Whether the card has a published solution in print literature beyond the short web search the
  solver recorded.
