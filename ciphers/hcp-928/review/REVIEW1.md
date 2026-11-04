ACCEPT

# Review 1 — hcp-928 (Vance, Ala. to Miss Delia Fischer, Birmingham, 8 Sep 1908)

Reviewer: Claude Opus 5.5, 2026-11-03. Solver work under review: Claude Opus 5.5 (same date), round 1.

## What I verified and how

1. Ran the solver's command from the repo root:
   `python3 -I ciphers/hcp-928/work/decode.py` prints "source hashes OK" and a plaintext that is identical, line for line, to the "Plaintext (literal decoder output)" in SOLUTION.md.
2. Independent decryption: `review/work/indep.py` holds my own word-by-word reading of both sides (sign names of my own, entered from my crops, not copied from work/transcription.txt) and my own key. Output:
   - picture side: "take me back back back to bir?ingham delia is thet trip you intend taking a honeymoon if not please dont go soon that letter was a god send to me will yos be so kind as to write another please yours truly we?"
   - address side: "this is a fine moon light night and id give the world just to be walking with you we?"
   25 distinct signs, 233 sign tokens; the same key as the solver's, with no conflict. Every word on the card is covered; the only signs outside the key are the blot in Birmingham and the signature sign K.
3. Transcription against the scans: enlarged crops (2–3x of the work/hires originals) in `review/work/` — r1–r7, w1, w2, s1, sig2 (picture side, every row), b_top, b_end (address side, every row), adr_small/pic_small overviews. Checked sign by sign:
   - Row 1 "^CX98 78 qX69 qX69 qX69": q-shaped b (straight stem) against round 9 (k) is visibly distinct; take/back read cleanly. The dot over the first dash is a stray mark.
   - "bir#ingham": the 4th sign is a solid ink blot with a short tail; its outline is compatible with an inked-over 7 (m) but not readable. m restored from sense and the address "Birmingham" on the card; disclosed.
   - "Delia" (caret under pi-sign), "thet" (cent-3-8-cent: the third sign is the same 8-shape as e elsewhere, not X), "honeymoon" (3 5 / 8 -o- 7 5" / ?: the barred circle is y, doubling strokes over the second 5), "god send", "Will" (caret under the division sign, doubling strokes over d), "yos" (the third sign is ")" not "(" — confirmed), "kind as to write", "another? Please, Yours truly".
   - Address side: "This is a fine / moon light night / and i'd give the / world just to / be walking with / you." — "j" is y with a dot beside it, "i'd" has a visible apostrophe; u is written both as "(" and as a larger C-shape (in "you." and "truly"), the same sign.
   - Signatures: address side "÷8K." and picture side "÷8K, ÷" with a short vertical stroke above the second ÷ — transcribed correctly.
4. Language and context: natural American English of 1908; "Take me back ... to Birmingham" sits beside the "Rapid Transit" pig-ride cartoon and the addressee lives in Birmingham, Ala. Nothing forced.
5. Stamp box and picture side: no writing visible around the Franklin one-cent stamp or in the picture area; the stamp is affixed, so its underside cannot be seen. Unlike the Jolánka series, this card shows no sign of a hidden message, so MASC (not "MASC + Steganography") is the right label on the evidence available.
6. Sources: portal lists no solution or transcription; nothing in SOURCES.md or SOLUTION.md suggests a published solution was used.

## Findings

1. (minor) The signature sign K is left unread ("We[K]", plus a trailing "w" on the picture side). This is a single item and the rest of the card reads, so it does not make the card partial; keep it disclosed in the report as the sender's unresolved signature (possibly an initial in plain letters).
2. (minor) The mark above o in "don't" (picture side, row 6) looks like the two doubling strokes plus a dot rather than a clean three-dot mark. Either way "don't" rests on sense; the description in Uncertainty 4 could say "two strokes and a dot".
3. (minor) SOLUTION.md says no web search was made. The run allows a short search for a published solution of this card; either do one and record the result, or keep the statement as is in the report so the limitation is clear.
4. (minor) The swapped file names (address-large.jpg shows the picture side and vice versa) are disclosed in SOLUTION.md and NOTES.md; repeat this in the report for a reader who opens source/.

## What I could not verify

- The letter under the ink blot in "Birmingham" (restoration from sense and address only).
- The identity of the signature sign K and the sender's name.
- Whatever may lie beneath the affixed stamp.
