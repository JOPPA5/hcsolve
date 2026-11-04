ACCEPT

# Review 1 of hcp-1180 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1180/work/decode.py` (from the repo root): all four
   SHA-256 checks print OK, and the output matches the plaintext claimed in SOLUTION.md word for word.
2. **Independent decoder.** `review/work/indep_decode.py` uses its own regex tokenizer (fractions
   first, then single digits, letters and nulls). Running it on `work/transcription.txt` gives
   output identical to the solver's (diffed, `IDENTICAL`). Sign statistics: 173 consonant letters,
   digits 1:13, 2:48, 3:36, 4:10, 5:8, fractions 1/1:2, 5/5:3, and 5 root signs. No digit outside
   1-5 occurs, and no plain vowel letter (a e i o u ä ü) appears anywhere in the transcription
   (`grep` returned empty). So the vowels-only-as-digits key covers the whole message, and every
   consonant is written plain.
3. **Transcription against the pixels.** I made my own crops from the un-converted
   `work/hires/cpc_--___CH_Neuchatel__pic.jpg` (3468x2298) with `review/work/crop.py`, and
   rotated the margin. I checked all 13 main lines and both margin lines group by group:
   - The line 1 groups `(w-2r+t)(h-2r)`, `k-1m+p-f . Vg-2n+4s-s+2 !` are as transcribed.
   - Line 2 `m-2c+h` (mech.png): the digit is a looped 2, the same shape as the 2 in `s-2+3t`,
     and clearly different from this hand's open 3. So "mech" really is a writer's slip, and the
     solver decodes it literally and discloses it.
   - Line 9 `(z-3.2t)` (zeit.png): the 3 comes visibly before the 2, which gives "ziet", a slip.
     The struck-out group before it is crossed through in the writer's ink.
   - Line 9 `m-5s+t` (must.png): two 5-like shapes appear before t, under the grey collection
     stamp. This hand writes s almost like 5 (compare `5r-s+1-c-h+2` Ursache and `4s-s+2` genosse),
     so reading 5 s is sound. It is disclosed.
   - Lines 4, 5, 6, 7, 8, 10, 11, 12 and 13 are as transcribed: Altbüron
     `1-l(t+b-5/5r-4n`, residiere `(r+2s)(3d-3-2r+2`, einen `(2+3)(n-2n)`, brief `b-r+V3.2f`,
     schreiben `s+c / h+r-2+3b-V2n`, hiemit, vorläufig `(v+4r)(l-1/1+5f)-3g`, mittheilen
     (bold, re-inked 2), unterdessen, die `d-3.2`, saumäsigsten, grüsse `g+r-5/5s-s+2`,
     von, Plüs, Soli. The 3.2 = "ie" in "brief" and "die" supports reading the same group as a
     slip in "Zietung".
   - Margin (mA.png, mB.png): `2t-t+3s+w-3l = d-2n = 35 = s+t-4s+m- / 4n-1-t = 1n+4 = t+5b-1+k .`
     This matches the transcription. The "35" has a small tick after it.
4. **Address side and stego check** (pm.png and the full scan). The card is a Swiss 5 c
   Carte-correspondance with an imprinted stamp, so there is no stamp box to hide anything under.
   It carries a cancellation reading "-VI 75" and a plain address to Oskar Egli, Crédit Mutuel,
   Neuchâtel. There is no picture side. I found no hidden, reversed or edge writing on either side.
   The only extra mark is a faint pencil numeral above line 1, which the solver notes.
5. **Language and context.** The text is coherent 1870s Swiss German, with "Werther", the old
   spelling "mittheilen", "hiemit", "saumässig" and "anno Tubak". Ettiswil and Altbüron are
   neighbouring villages in canton Lucerne. A June 1875 postmark fits the 1870s Swiss postal card
   type. Nothing is forced: every group decodes into a dictionary word or one of the disclosed slips.
6. **Published solution.** The portal shows Not solved and attaches no solution. The solver's
   search found nothing, and I have no evidence of a published solution.

## Findings

1. (minor) **Margin direction is misdescribed.** SOLUTION.md and the transcription say the
   margin "reads upwards". In my crops the letters stand upright after a 90-degree
   counter-clockwise turn, so on the card the text runs from top to bottom. The reading and the
   line order are not affected; only the description needs fixing.
2. (minor) **Translation nuance.** "du mir keine Zeitung abonieren must" means "you need not
   subscribe to a newspaper for me". The English "must not" and the Slovak "nemáš" read as a
   prohibition. Suggested fixes: "you need not take out a newspaper subscription for me", and in
   Slovak "nemusíš mi predplácať noviny".
3. (minor) **"Stosmonat" is unexplained.** The solver reads it sign by sign and says so honestly.
   It is the only un-understood word, and the rest of the card reads, so under the run rules the
   card still counts as complete. The report should keep it flagged as a joke month of unknown
   meaning (perhaps a play on the Swiss month names Brachmonat and Heumonat) and not imply that
   it is a known word.
4. (minor) **Type label.** Only the vowels are replaced, by digits, and consonants stay plain
   inside a mock-algebra disguise. MASC is the closest allowed register label and is acceptable,
   but the report should say clearly that it is a partial (vowel-only) substitution. There is no
   steganographic part, so "MASC + Steganography" does not apply to this card.

## What I could not verify

- The postmark year digits are faint ("75", possibly "76"). The decade is secure, but the exact
  year is not.
- The identities of "Plüs = Soli" and of Oskar Egli. I did not check whether the h/k calls
  (Kampf, keine, Tubak) rest on anything other than word sense; they are word-sense calls in a
  hand with one looped letter for both, as the solver discloses.
