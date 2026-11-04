REVISE

# Review 1 - hcp-1182 (cpc_1909-10-16_DE_Berlin_DE_Lichtenrade_)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. Role: reviewer, round 1.

Summary: the 17-line Morse message on the left half of the address side is read correctly; I
re-read every line on the hi-res scan and my own decoder gives the same text. But the card holds
**a second, fainter line of Morse running vertically along the printed divider line**, from the top
edge of the card down to the bottom. SOLUTION.md does not mention it, so the claim "complete
reading of the whole message" does not hold. The main reading stands; the card must be completed
or declared partial.

## What I verified and how

1. Ran the solver's command from the repo root:
   `python3 -I ciphers/hcp-1182/work/decode.py` - hashes OK for all three files; line-by-line and
   running output are identical to the plaintext in SOLUTION.md.
2. Independent decoder `review/work/decode_review.py` (my own ITU table built letter -> code,
   no reuse of work/decode.py), run as
   `python3 -I ciphers/hcp-1182/review/work/decode_review.py ciphers/hcp-1182/work/transcription.txt`.
   With the standard table the text reads "... BLEIBE Y U HAUSE DIE YEIT PIRD MIR EP IG ...";
   with only P -> W and Y -> Z it gives exactly the solver's text. No unknown codes; standard
   W `.--` and Z `--..` never occur, so the two substitutions are not in conflict with any other
   use (P 3x, Y 4x, all in words where W/Z is the only German fit). Key covers all 17 lines.
3. Transcription vs. pixels: my own crops of
   `work/hires/cpc_1909-10-16_DE_Berlin_DE_Lichtenrade__adr.jpg` (review/work/b*_L.png,
   b*_R.png, f*.png, l7*.png, l9-l11.png, l14.png, l16.png, l17.png; 1.0-4x). I read every one
   of the 17 lines group by group and agree with work/transcription.txt, including:
   - the doubling bars over `--` (BESTIMMT, line 3) and `...` (SCHLIESSEN, line 15);
   - the Kurrent glosses: "3"-shaped z under the first Z (line 4), the "w" squiggle at the
     left margin under WIRD (line 6), the squiggle under Ü `..--` in GRÜST (line 16);
   - WILL `.--.` (l14.png: dot, two dashes, dot - not three dashes);
   - LIEBR `.-.. .. . -... .-.` with no E before R (l10.png);
   - GRÜST with a single `...` and no bar (l16.png);
   - lone `-..` between heavy word strokes before HUGO (l17.png);
   - underlining from B= (line 7) to MIT (line 9).
4. Plaintext: idiomatic German of the period ("die Zeit wird mir ewig lang", "ich hoffe stark
   auf dein Erscheinen", "Nun will ich schließen"); Lichtenberg (sender header) and Lichtenrade
   (address) are both Berlin-area places, postmark Berlin, 5 Pf. Germania - consistent with 1909.
   English and Slovak translations are faithful.
5. Published solution: portal status "Not solved", no attachment; I found nothing to suggest a
   published solution was used.

## Findings

1. **Blocker (for "complete" status / register entry) - an untranscribed second Morse text along
   the divider line.** Faint grey dots, dashes and letter strokes run vertically down the card
   at x ~ 1500-1620 px of the hi-res address scan, starting above the top of the printed divider
   (card y ~ 130) and continuing to the bottom edge (y ~ 1840). It is written with the card turned
   90 degrees (it reads top to bottom; rotated 90 degrees counter-clockwise it reads left to right,
   and its letter strokes then lean "/" like those of the main text). It uses the same system:
   dots, dashes, thin slanted letter strokes and at least one darker word stroke. Evidence:
   review/work/divider.png (unrotated overview), review/work/div_a.png, div_b.png, div_c.png
   (rotated, 2x) and v0000.png ... v1750.png (rotated, blurred, contrast-stretched, 3x, card y
   0-2050 in 250 px steps). It is clearly Morse, not stains or offset: groups are separated by
   regular strokes. My tentative, unverified group sequence from the top is roughly
   `... / ..-- or .-- / ... / .... / . / .-. // ... / ---- / .-.. / . or .. / -. / --. / . / .-- ...`
   (contains readable S, CH, L, N, G, E groups), about 15-25 letters in all, partly crossed by the
   main text's heavy word strokes. I could not get a confident word reading from it; I leave the
   reading to the solver. SOLUTION.md point 7 says only "the stamp could not be lifted" and NOTES.md
   never mentions this strip. Under this run's rule (a whole unread clause anywhere on the card
   makes it partial), the card cannot be FINAL as complete, and cannot get a register entry, until
   this line is read or shown not to be text. Fix: crop the strip (e.g. x 1480-1640, rotate 90
   degrees, 3-5x, contrast stretch), transcribe it into work/transcription.txt as its own block,
   decode with the same key (watch for the writer's W `.--.` and Z `-.--`), and add it to the
   plaintext, translations and SOLUTION.md. If it cannot be read, change the status to partial.
2. **Minor - line 7: there is no word stroke after LANG.** At 4x (review/work/l7c.png) the G
   `--.` is closed by one thin letter stroke only; the lone dash that follows is then closed by a
   thin + heavy pair, as words are elsewhere. The transcription's `|` between LANG and the dash
   is therefore not on the card, and SOLUTION.md point 3 ("a single dash between two
   word-strokes") is inaccurate. Read strictly, the group is attached to the word (LANGT). The
   dash-as-Gedankenstrich reading is still the most plausible one, but say that it rests on
   sense and correct the description and the transcription token.
3. **Minor - cipher type / register label.** "MASC/Morse" from the allowed list fits the main
   text (no secret key; the writer's W/Z variants are personal quirks). If the faint vertical line
   (finding 1) proves to be a deliberately hidden second message, say so and reconsider the label
   (the allowed list has "MASC + Steganography"); if it is simply a postscript squeezed into the
   margin, keep MASC/Morse. Decide on the evidence after reading it.
4. **Minor - address suggestion.** SOLUTION.md suggests "probably Holzmarktstr." for the street.
   Holzmarktstraße is in central Berlin, not in Lichtenrade; the Kurrent (review/work/street.png)
   shows "Holz" + an unclear m/w + "...t str. No 34". Keep it as "Holz...str." without the
   suggestion, or state that the suggestion conflicts with the Lichtenrade address. "bei
   Schreiber" is plausible from the pixels but uncertain, as disclosed.

## What I could not verify

- The faint vertical Morse line (finding 1): I did not reach a reliable reading.
- Writing under the stamp: the stamp is still on the card and the scan cannot show beneath it.
- The picture side shows no writing at the resolution available; I did not confirm the printed
  series number "9/18".
- The pencil "A A 4"-like mark over the printed "Correspondenz-Karte" lines (review/work/pencil.png)
  looks like a collector's/dealer's mark, as the solver says; not verifiable further.
