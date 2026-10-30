REVISE

# Review 1 of HCP1291 (Feri to Jolánka Tóth, 31 Aug 1913)

Reviewer: Claude Opus 5.5, 2026-10-30. Scripts, crops and the stroke survey are in `review/work/`.

**Summary.** The cipher type, the key, the sender's message and the English and Slovak translations stand. I could not refute the reading. But the ledger, and so the "literal decipherment", differs from the pixels at five places in the main text, one in each of rows 4, 11, 13, 18 and 21, and at one disclosure-level place in row 12, with a probable omitted sign in row 3. The statement "This is the only restoration on the card" is false (row 11). The d/h/p statement in the key section is false for this hand. The solution's largest editorial step (`négy(en)sze[r]`, item 12) disappears once the sign is read correctly: the card has *negyedsze[r]*.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1291/work/decode.py` runs; all 4 SHA-256 checks pass. A script comparison of its 28 output rows with the literal block in SOLUTION.md found no differences.
- **Independent decoding.** `review/work/my_decode.py` holds my own row-by-row transcription by sign shape, made from `review/work/` crops of the hires scan before comparing with the ledger, and a key of its own. It diffs against the solver's ledger. Result: 21 of 28 rows are identical (the three signs uncertain in both, rows 5, 14 and S6, aside); rows 3, 4, 11, 12, 13, 18 and 21 differ, see findings. Row 16 `irantam mert` and row 9 `va es` were confirmed sign by sign as the solver gives them. (The equal sign totals of 445 are a coincidence of offsetting differences.)
- **Pixels.** Every row was read on 1.7–1.8x crops (`bl*.png`), with 2.3–5x crops (`z_*.png`) of the rows and signs in question and of the stamp rows. Sign-class gallery: `gallery.png`. Stroke lengths: `strokes.py`, `strokes.txt` (noisy connected-component measurement, used only as support for what the crops show).
- **Key coverage.** Every sign falls in a class of the HCP1216 key. Nothing on this card needs a new sign.
- **Language and context.** The Hungarian is real period colloquial with formal address. Addressee and place on the address side match (*Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás*; the first word partly under the postmark, as disclosed). Postmark `…SZAPÁTI 913 AUG 31` confirmed. The picture side is a printed verse (*Két szív ha földobog*), no cipher.
- **Published solutions.** Portal capture shows none; nothing in SOLUTION.md or NOTES.md suggests outside use. Repeat counts claimed (*hogy* ×6 and so on) are correct.

## Findings

1. **major – row 11: an m in the ledger that is not on the card; undisclosed restoration.** The ledger has `... V A R O M H~ O G Y L E`. `z_r11.png` (4x, x 720–1040, y 950–1040) shows cursive o, directly the tall+short h, then cursive o: there is no three-stroke sign between them. The literal text is `aligvarohogyle`. *Várom* must be normalized `váro[m]`, and the literal block, item 6 ("the only restoration on the card") and the normalized text must be corrected. This is the kind of forced-from-context reading the literal text is meant to exclude.

2. **major – row 13: the sign read n in `negyen` is d; the reading is *negyedsze[r]*.** The sign before `sz` is a short high stroke followed by a long stroke running below it (`z_r13.png`, `gallery.png` cell "r13 n/d#2", x ≈ 724–754). This is the geometry of every d on the card (cells r4, r6, r22, S2, S3; `z_dset.png` for r1, r15). The n's are level pairs (r5, r9). The measured ratio (about 0.75–0.83) is less extreme than the cleanest d's (0.25–0.5), so the shape alone is strong but not absolute, and the word decides it: *már negyedszer fogok hozzá* is exact Hungarian for "I am setting about it for the fourth time already", needing only the omitted final r. The solver's `négy(en)sze[r]` means "four times", not the "fourth time" of its own translation, and needs a superfluous syllable as well. Item 12 ("the largest editorial step") goes away; the sentence "n is always two equal short strokes" must go too, or be restated.

3. **major – d is not a homograph of h/p here; the key section and item 8 are wrong, and row 12 `de` is unsupported by shape.** The section says d, h and p are all "a tall stroke with a short tick" and "every d/h/p choice rests on word sense". On this card d is *short then tall* (rows 1, 4, 6, 15, 22, S2, S3, S5: all eight clean d's) and h/p are *tall then short* (all h and p tokens I inspected). So d vs h needs no word sense in those rows; only h vs p does. Two tokens break the pattern, and both are recorded in the ledger as `D~` without saying so:
   - row 12, the sign after `fek` (`z_r12a.png`, x ≈ 332–359): plain tall-then-short, the same shape as *ehez* and *laphoz*. By shape the literal is `fekheehez`. The solver's `lefek | de ehez` therefore reads an h-shape as d. The alternative `lefekhe[ssek] | ehez a laphoz is` ("that I may lie down. Even to this card…") is at least as good a Hungarian sense and needs no off-shape sign. Both are truncated verbs, and the translation hardly changes, but the division must not be presented as "the only division found that gives sense". NOTES.md shows the solver did try `lefekhe e hez` and left it. Give both, with the shape facts.
   - row 18, the sign after `min` (`z_dset.png` right panel): also tall-then-short. *Mindennap* is not in doubt, but this sits next to the overwritten sign and is likely part of the same correction. Mark it `{d}`, by sense, and include it in the item 3 uncertainty.

4. **major – row 4: a sign omitted from the ledger, and a spelling error attributed to the writer.** `z_r04.png` shows gamma, two bars, wave, two bars, wave, inverted T: `talalja`, with both l's. The ledger's `T A L A J A` drops one, and item 13 reports *talaja* as the writer's spelling. It is not. Correct the ledger, the literal block and item 13.

5. **minor – row 3: a probable faint sign not in the ledger.** Between *hogy* and *legjobb* there is a gap wide enough for one sign containing two faint grey marks one above the other (`z_r03.png`, near x ≈ 350–380, y ≈ 285–300), in the position of a pale two-bar a. *Hogy a legjobb egészségben* is also the better idiom. It is not certain, since the area is pale and blotted, but SOLUTION.md says nothing about it. Enter it as `{a?}` and add an uncertainty item; the claim that every sign has a value should mention it.

6. **minor – row 21: the "isolated slash" is the stem of the t.** In `z_r21.png` the horizontal bar of the following gamma starts exactly at the top of the slash, and no other stem lies under that bar (the bar crosses the printed divider line). Slash plus bar are one t. The ledger's `| T` should be `T`, and `{|}` and item 5 should be dropped. With that, no sign on the card is left without a value (subject to finding 5).

7. **minor – second postmark not mentioned.** The context paragraph gives only Jászapáti. A second, larger postmark sits over the stamp position, with `BU…` and `913` legible and the rest partly gone (`z_pm.png`, `stamp.png`). I can read no more than that, but it should be listed, since it bears on where the card was mailed and on whether 31 Aug is the sending or the arrival date. The solution should not imply that the Jászapáti strike is the only one.

8. **minor – knock-on edits.** The rows in findings 1, 2, 3, 4 and 6 need changing in `work/ledger.txt`, the literal block and `work/normalized.txt`; ledger comments that define `H~/D~/P~` and `|` need the same. The "Why it is correct" line "no sign left without a value except the slash of item 5" and the row 12 description in NOTES.md should follow. The two translations stand, but the Slovak and English should be rechecked against the final Hungarian (for example a period after *lefek-*). The solver may add the row-18 and row-12 points to the d/h/p note.

## Checked and upheld

- Row 5 `haragu{j}on`: bar with stem above and a shorter stem below, touching the x (`z_r05.png`). The solver's description is accurate, and j by sense is the right call.
- Row 14 `{m}agát`: a cross followed by two strokes, as disclosed; m by sense is fine.
- Row 18 overwritten sign: two heavy stems with two crossbars, as disclosed; `e+n` by sense is reasonable.
- Row 18 `mi{n}t`: two strokes on my crops, n; the solver's caution is acceptable.
- Row 10 `fglava`, row 9 `va és`, rows 5–6 `rit|an`, row 22 ending `Fer` with clean paper after r: all as described.
- Row S6: `s`, then a gap under the stamp remnant, then `fer` and a hook sign. Restoration `[e]` is disclosed and modest; faint marks at the upper edge of the gap are not readable (`z_s6.png`). Final hook i by sense is fine.
- *Hű* in S5: the sign is on the stamp-darkened strip; no double mark visible, as disclosed.

## What I could not verify

- Whether the row 3 marks are ink or staining, and which signs (if any) lie under the stamp remnant in S6.
- The text of the second postmark.
- That Feri here is the Feri of HCP1216: the name, closing formula, key and addressee match, but I did not compare the handwriting of the two cards. The d-shape rule found here was not tested on the sister cards; the HCP1216 table lists d and h/p as separate shapes, which agrees with it.
- The historical background of the troop trains, for which the solution rightly claims nothing.
