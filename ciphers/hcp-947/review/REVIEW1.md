REVISE

# Review 1 of hcp-947 (reviewer: Claude Opus 5.5, 2026-11-03)

Summary: the ciphertext reading "Ach, wärst du hier!" is correct and I could not refute it. The key covers every sign. What needs fixing is the unenciphered Kurrent text of writer 1: the word the solver gives as "Grüße" does not look like "Grüße" on the scan, and the "Pfingst…" word is still unread. Both are part of the card. Under this run's rule ("a whole unread clause is partial"), the first writer's opening clause must be either read properly or declared unread before FINAL/register.

## What I verified and how

1. Ran the solver's command from the repo root: `python3 -I ciphers/hcp-947/work/decode.py`. Output: `source hashes OK`, `plaintext: ACH, WARST, DU, HIER!`, matching the claim apart from the umlaut, which is a disclosed word-sense addition.
2. Independent decode: `review/work/verify.py` uses my own sign names, read from my own crops of the hires scan (`review/work/block.png`, `l1.png` at 4x, `l2.png` and `l3.png` at 3x, autocontrast). Output: `ACH WARST DU HIER`. When I keep only the signs that are plain 180° rotations of Latin capitals (∀, ⊥, Π, ᗡ, 3=Ɛ, turned i, 8/S, C, H), I get `ACH?A?STDU?IE?`. So 11 of 14 letter positions follow from shape alone, and only W (Λ with a central stem), R (Σ, twice, consistent) and the I-beam H rest on word sense. The solver's table says the same.
3. Sign-by-sign check against the pixels:
   - Line 1: ∀ with crossbar; a bracket-shaped C; an H-like sign, partly overwritten. ACH fits.
   - Line 2: Λ with a faint stem through it; ∀ with crossbar and a small mark above; Σ; 8; ⊥; then ",-". The mark above the ∀ is a single small tick, not two dots, and it sits above the sign even though the letter is turned. So "Ä" is word sense, as the solver disclosed.
   - Line 3: ᗡ with an extended stem; Π; ",-"; serifed I-beam; a stroke above a dot; a heavily retraced 3; Σ; "!-". The long stroke that crosses Σ is the descender of the Kurrent word above, not part of the sign. I confirmed this in `l3.png`.
   - Word separators ",-" sit after every word. The final "!-" is the upright exclamation. It looks the same as the "turned i" sign, but its position (after the last word, before the dash) separates the two.
4. Coverage: every sign in the three-line block is used. There is no residue, and no other cipher-like writing is on the address side.
5. Picture side (`source/picture-large.jpg`, hires): printed portrait of Gudrun Hildebrandt, with the printed name and the publisher mark "GCo 1936/3". The violet streaks on the top and bottom edges are ink or dye stains. I found no handwriting, no hidden text in the picture and nothing along the edges.
6. Stamp box (`review/work/stamp.png`): 5 Pf Germania, intact, with a postmark across it and the year "09" legible. Nothing is visible at the perforations. Following the user's note that the Jolánka series hides messages under the stamp, I checked this specifically. On this card nothing can be seen, and what is under the stamp cannot be judged from a scan. The solver disclosed this limit, which is correct.
7. Context: German, 1909, greetings from several people to Frl. Erna Garbe, Reddelich. "Ach, wärst du hier!" is an idiomatic period postcard phrase. Sister card hcp-946 (same addressee, same year) uses a different letter-numbering cipher, so this card's system is a separate one. That is plausible for a group of friends.
8. Published solution: the portal has none, and I found no claim of one in SOURCES/NOTES. I did not search further.
9. Register type: MASC is an allowed label and fits, since each letter is replaced by a turned or altered capital in normal order. The user's request suggests "MASC + Steganography" only where a hidden message is actually found. Nothing hidden was found here, so MASC stays.

## Findings

1. **major – writer 1, line 2 is misread as "Grüße".** In my crop `review/work/line2w.png` (hires x 80–1000, y 380–780) the first word of line 2 is long. It begins with a Kurrent g-e, has a dotted vowel, a large ſch loop and a final t, and a tall stroke that looks like "!" follows it. It reads much more like "gewünscht" (possibly "gewünscht!") than "Grüße", which would need a capital G, r, ü and ß and is shorter. Together with "Fröhliche Pfingst…" this gives "Fröhliche Pfingst[…] gewünscht!", a normal formula, and "sendet" on the next line then goes with "H. Weber" ("… sendet … Weber"). The solver should re-read this line and update SOLUTION.md and the translations, or mark the word as unread.
2. **major – the end of the "Pfingst…" word is unread.** `review/work/pfingst.png` shows, after "Pfingſt", roughly "e-n-o-r-k" with a tall-ascender ch/k and a dot below the last letter, maybe "!". "Pfingsten u." is not what is written: I see no "u." with a space. Candidates are "Pfingsten noch" or a compound such as "Pfingstwoche", but none is secure. Note also that Whit Sunday 1909 fell on 30 May and the card is postmarked 3 June. If "Fröhliche Pfingsten" is right, it was written before posting or sent belatedly. The solver should give the literal letter sequence with "[unread]" and not offer "en u." as the best reading. Under the run rule, if this word and the misread "gewünscht" together leave the opening clause unread, the card is partial and gets no register entry. If it narrows to a single uncertain word, the card can stand.
3. **minor – decode.py prints "ACH, WARST, DU, HIER!"**, with a comma after WARST, because every ",-" maps to ", ". The claimed plaintext has no comma there. The script should print the word-separator form (`ACH / WARST / DU / HIER!`) or drop the comma, so that the command output and the claim match exactly.
4. **minor – disclosure of the umlaut mark.** SOLUTION.md calls it "a small mark". It is a single tick above the ∀, so it is not drawn turned like the letter itself. Say this explicitly so it is clear that Ä rests on word sense alone.
5. **minor – signatures.** "Warkow": on my crop the signature reads more like "Warchow". "A. Schmidt(?)" is plausible. The initial before Weber is a large looped capital, H or J. These are correctly marked uncertain, and "Warchow" could be added as an alternative.

## What I could not verify

- Whether anything is written under the stamp. It was not lifted, and scans cannot show it.
- The postmark town and day. Only "09" is clearly legible on the scan; 3 June comes from the collection file name.
- A secure reading of the "Pfingst…" ending, as described in finding 2.
