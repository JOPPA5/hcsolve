ACCEPT

# Review 1 – hcp-1484 (pc_hcp_165), reviewer Claude Opus 5.5, 2026-10-30

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1484/work/decode.py` (from repo root):
   "source hashes OK", the ten-line plaintext exactly as in SOLUTION.md, "177 signs, all mapped".
2. **Independent decoder.** `review/work/indep_decode.py` does not read `work/key.json`; it
   derives every consonant from the structural rule only (order Lt, Lb, Rt, Rb, Bt, Bb, three
   bar counts each, consecutive consonants B C D F G H J K L M N P Q R S T V W) plus the six
   vowel shapes. `python3 -I review/work/indep_decode.py work/transcription.txt` gives the same
   letter string (177 signs). So the key is the regular 6x3 grid it claims to be, not a
   sign-by-sign fit.
3. **Transcription against the scan, sign by sign.** I rotated `source/address-large.jpg` by 180
   degrees (`review/work/rot.png`; the "?", commas and quotation marks then read normally,
   confirming the upside-down claim) and cut every one of the ten message lines into two
   4x enlargements (`review/work/L1a.png` … `L10b.png`). I read every sign myself and compared it
   with `work/transcription.txt`. Every word agrees: MY OWN LITTLE DARLING, / THANK YOU EVER SO MUCH /
   FOR THE POSTCARD. I HOPE / TO HEAR EVEN BETTER NEWS / IN THE MORNING. WHY A / CARD OF
   LLANGOLLEN? SHALL / WE GO THERE TOGETHER, SOME / HAPPY DAY, [faint] DARLING? I LOVE /
   YOU, "DEAREST-OF-ALL-THE-WORLD," / YOUR BOY. The line breaks agree with the card too.
   I checked bar counts in particular where 2 and 3 bars must be told apart (N vs P, C vs D,
   R vs S, V vs W). The C and H at the end of MUCH are two separate stems (2 left-top, then
   3 left-bottom; `z_much.png`). The seven superscript "2" marks are visible where claimed.
4. **Signs touched by printed text** (the solver's uncertainty 2):
   - M of SOME (`z_some.png`): a clear stem with one right-bottom bar. A hidden left bar would
     give T ("SOTE"), which is not a word.
   - E of LOVE (`z_love.png`): a triangle under the printed "&".
   - V of LOVE: two bars on both sides at the bottom.
   - D of WORLD: three left-top bars, still visible.
   None of these is a restoration from context.
5. **Faint sign before the second DARLING** (`z_faint.png`, contrast-stretched `z_faint2.png`).
   It is a lighter-ink stem with bars mostly on the left in the upper part and a curl below. It is
   compatible with a D (an abandoned start of DARLING), and it is disclosed as `[d]` and left out
   of the sense. I cannot exclude bars on both sides, but no reading of this one sign changes the
   text.
6. **Picture side.** It carries only the printed caption "The turning of the Tide" and the
   portal watermark, with no cipher writing.
7. **Context.** The address reads plausibly "Baron Hill", York Road, Colwyn Bay, N. Wales
   (`review/work/addr.png`). Llangollen is near Colwyn Bay, and the text is fluent Edwardian
   English. Sister card hcp-1485 (same addressee; its DONE1 solution was reached separately and
   is not used here) has an identical stroke alphabet and is addressed "Gwennie darling", which
   fits "Miss G. Williams". This supports the key here.
8. **Honesty.** The portal status is Not solved and no solution is attached. Credits to the
   earlier GPT setup are stated. The inferred J/Q and the missing X/Z are disclosed.

## Findings

1. **minor – Y glyph description.** SOLUTION.md describes Y as a "square with a V from the two
   top corners". On the card (MY, YOU ×2, YOUR, WHY, HAPPY, DAY, BOY; `y_*.png`) Y is a square
   with a "/" diagonal, sometimes with an extra short stroke from the top-left corner. U is a
   square with a "\" diagonal. hcp-1485 describes Y as the "/" diagonal. The reading is not
   affected, but the report should describe the glyph as it appears (U = "\", Y = "/", often
   with an extra stroke) and match hcp-1485.
2. **minor – Faint sign.** The `[d]` reading is reasonable and disclosed. The report could add
   that the sign is too faint to rule out bars on both sides, and that it is not counted as part
   of the text.
3. **minor – Sister-card corroboration.** SOLUTION.md says hcp-1483/1485 are "untested". hcp-1485
   uses the same key and greets "Gwennie", which matches the addressee here. This can be cited
   in the report as independent support, provided its review status is stated.

## What I could not verify

- Who the sender was ("your boy"). The exact house name ("Baron Hill" vs a similar reading) is
  irrelevant to the decipherment.
- The exact identity of the one faint sign (see finding 2).
- J and Q are not attested on the card. The pattern fixes them, but they are unconfirmed.
