ACCEPT

# Review 1 – hcp-1046 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Solver command. `python3 -I ciphers/hcp-1046/work/decode.py` (from repo root) prints `source hashes OK` and
   `DU KLEINER BÖSEWICHT`, identical to the claimed plaintext.
2. Independent decryption. `review/work/my_decode.py` holds my own number sequence, typed fresh from my reading of the hi-res
   scan (not copied from work/transcription.txt), and its own A=2..Z=26 (no J) table. Output: `DU KLEINER BÖSEWICHT`.
   All 18 numbers fall in 2..26 and decode; no leftover signs.
3. Transcription against the pixels. From work/hires/...adr.jpg (3469x2298) I cropped and rotated the message lines myself
   (review/work/msg_full.png) and enlarged the uncertain spots 3x (z_l1start.png, z_l2start.png, z_l2end.png). My reading:
   `5x.21. - 11.12.6.10.14.6.18. -` / `3x.15(umlaut).19.6.23.10.4.9.20.` – the same as the solver's sign for sign.
   - Line 1 start: a flagged 5 with a lower bowl, crossed by a diagonal; then a clear 21 (2 plus heavy 1).
   - Line 2 start: a 3 crossed by a diagonal. The crossed-numeral capital marker matches the convention on the FINAL-reviewed
     sister hcp-1113 (crossed 19 at noun-initial S). Either way (crossed numeral or stylised Latin D/B) the letters are D and B.
   - Double mark: clearly present, directly above the 15 (slightly left). Ö is a fair reading.
   - Last number: second digit is a thin stroke with an upward hook, the same form as the 0 in both "10"s on this card, unlike
     the heavy 1 of "21" in line 1. 20 = T is a pixel reading, not only word sense.
4. Key. Same table as hcp-1113 / hcp-1134 (same recipient Fritz Lehmann, 1909), both already reviewed. The key is simple and
   the plaintext is fully determined by it; the solver discloses that the key came from the sister cards.
5. Language and context. "Du kleiner Bösewicht!" is idiomatic German of the period, a teasing endearment fitting a love-motif
   card ("Der Herzensschmied"). English and Slovak translations are given and are correct.
6. Other surfaces. Picture side (review/work/pic_small.png): printed caption and publisher marks only, no handwriting. Stamp
   box (review/work/stamp.png): Germania 5 Pf, postmark "13 . 09", no writing on the margins; what is under the stamp cannot be
   seen, and the solver says so.
7. Published solution. The solver reports one search with no find; portal status Not solved, no attachment. I did not find a
   reason to doubt this.

## Findings

1. (minor) A faint short tilde-like stroke sits right of the 15, before its dot (z_l2start.png). It is much lighter than the
   writing and is probably a pen trace, but it is not mentioned in SOLUTION.md. It does not affect the reading; mention it in the
   uncertainties.
2. (minor) The house number in the address looks to me like "No 29" (a 2 and a 9 written over or next to a 1), whereas the
   solver gives "2?". The street name in Kurrent is not securely readable for me either ("Alte ...hofstraße"). These are
   address details, already disclosed as loose, and they are not a message clause; no effect on completeness.
3. (minor) SOLUTION.md describes the umlaut as "a little above and left of the 15 (between '3.' and '15')"; on my crop it
   stands over the 15 itself. Wording only.

## What I could not verify

- Anything under the stamp.
- The postmark place name (not legible on the scan).
- Whether an independent published solution exists beyond the one web search reported by the solver.

Register: type `MASC` is an allowed label and fits. The card has no unread clause; a register entry is appropriate.
