ACCEPT

# Review 1 of hcp-1091 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Ran the solver's command from the repo root: `python3 -I ciphers/hcp-1091/work/decode.py`. All four SHA-256 checks print OK. The literal decode matches the claimed plaintext word for word (52 words), and the script's pattern check passes. The output plaintext is identical to the one in SOLUTION.md (apart from the punctuation the solver says he added).
2. Made my own crops from `work/hires/cpc_1886-03-12_AT_Wien_AT_Krems__pic.jpg`. I rotated it 90 degrees for blocks A and B and 180 degrees for block C, and enlarged by 1.4 to 4x (`review/work/crop.py`, `rot_full.png`, `A1_5.png`, `A4_5end.png`, `A6_10.png`, `A9z.png`, `B1_5.png`, `B2B4z.png`, `B5z.png`, `B6_10.png`, `B11_14.png`, `C_all.png`, `C_stamp.png`, `C2end.png`). I read all 27 lines sign by sign, not just a sample. My reading agrees with `work/transcription.txt` on every sign, apart from the notational point in finding 2.
3. Wrote an independent decoder, `review/work/my_decode.py`, which uses my own sign list and a single-value key (1 = t, 5 = k, 9 = v, + = c). Result: 189 signs and no unknown sign. Each word is the solver's word up to the declared d/t, g/k, f/v and c/z classes ("jakas bua", "tu bist also wirklich ernstlich böse", ..., "sente tir aber toch noch ten süsen kus"). The key therefore covers the whole ciphertext.
4. Checked each disclosed point on the pixels:
   - A5 final [h]: only a dark stroke with a blob is visible on the green picture edge. The restoration is plausible and disclosed.
   - C1 "abe[r]": the start of a stroke is visible at the stamp perforation. Disclosed.
   - C2 "de[n]": "1 .." is fully visible. The faint long stem of the 1 runs up into the sky colour, and the next sign is under the stamp. Disclosed.
   - B5 "re[c]ht": the sign is a 1-like stroke with a left flag and no crossbar. Disclosed as word-sense.
   - B8 "w[o]l": the sign has its bar on the left and its stem from the right end, so it is a 7 rather than the centred-bar T. Disclosed as word-sense.
   - B2 "m[i]r": the mark is a short raised tick. Disclosed.
   - A9 and C3 closed 4-shape = s: this is clearly a heavier, closed form, distinct from the r-sign in A1, B9 and B11. Disclosed.
5. Language and context. The text is fluent, idiomatic Austrian German of around 1900 with the writer's single-consonant spelling (wen, kanst, Kus, das, wol), and Kurrent vowel marking is kept consistently (u-bar, ü, ö, ä). The 1-Heller picture-side stamp shows CAROLVS VI, which is the 1908 Austrian jubilee issue. That supports the solver's point that the portal date 1886 is wrong. The address side is consistent with the solver's account: a forester's address ("Förstla", in Gföhl struck through, b. Krems) for a recipient addressed as "Jaga". The Wien postmark matches.
6. A web search was claimed and recorded. I found nothing on the portal (status Not solved, no attached solution) that would contradict it.

## Findings

1. (minor) Register type and steganography. On the Jolánka series a hidden message under the stamp was found on most cards. This card also has a stamp on the picture side, and ciphertext lines C1/C2 demonstrably run under it. No scan shows what lies under the stamp, so a further hidden line cannot be excluded. Writing in the picture margins and upside down in the sky is the normal postcard layout, not steganography in itself. I recommend keeping type `MASC`, and stating explicitly in SOLUTION.md and the report that the area under the picture-side stamp could not be inspected and may hold more text. Use `MASC + Steganography` only if evidence appears.
2. (minor) "verzein" versus the literal. In B3 and B13 the three dots are the same sign that gives "ie" in lieber, nie and tief, so the literal reading is "verzien". The writer's spelling is therefore "verzien" (for "verzeih'n"). The solver adds a special token `...ei` so that the text reads "verzein". This is a one-off exception that the key does not need. Better to keep `...` = ie, give the writer's spelling as "verzien", and give the standard German as "verzeihen". The meaning is unchanged.
3. (minor) Transcription inconsistency. The r-sign in B3 ("9 .. 4") has the same S-like shape as the sign the solver codes `S{r}` in B4 (see `review/work/B2B4z.png`). B4 is therefore just this writer's variant of r, not a reading forced by word sense, and the uncertainty list somewhat overstates it. Either code both as the same sign or note that the shape recurs in B3.
4. (minor) Unenciphered matter on the address side is not fully described. It carries a violet handwritten forwarding note above "Förstla" (it begins with a capital that looks like S, roughly "Schilling…"; I could not read it with confidence) and a violet rubber stamp at the top edge ending "…INGERAMT". Neither is the sender's message, but SOLUTION.md and the report should at least mention them as postal/redirect annotations that are left unread. The reading "Förstla" itself is also uncertain and should be labelled so.

## What I could not verify

- What lies under the picture-side stamp, apart from the two disclosed end signs.
- The postmark year, which is not legible to me either.
- The identity of the writer and of August Hradegh.
- Whether "Jaga(s)" is a nickname or the recipient's occupation. The forester-style address makes "hunter" plausible.
