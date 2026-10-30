# HCP 1349 / pc_hcp_30 — Caesar shift (+1 written, −1 to decrypt)

**Status: whole message read; review 1 verdict ACCEPT, plaintext unchanged.** Abbreviation groups are kept literal; the capital of `Qbsl` is a disclosed sense-supported reading. All work by Claude Opus 5.5, 2026-10-30; there is no earlier work on this number. No published solution was found or used (portal status Not solved, no attachment).

## Origin

Portal record 1349, status Not solved, date 1907-08-31, recipient "W. Abboú" (catalogue spelling; language Unknown). Picture side: printed view "Christ Church, Harrogate", no handwriting. Address side: Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon; halfpenny Edward VII stamp. The postmark shows "10", fragments of a date that fit AU 31, and "07"; the town is not legible (only a few letters on the stamp's top edge). 31 Aug 1907 was a Saturday, which agrees with the heading. The message is on the left half of the address side, read rotated 90° counter-clockwise (`work/reading.jpg`). Language: English. It belongs to the W. Abbott correspondence (hcp-1386…1407 and neighbours) by hand, key and formula.

## Cipher and key

Simple Caesar substitution: each plaintext letter is written as the next letter of the alphabet. Heading is in clear.

```
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext

| Line | Ciphertext | Plaintext |
|---|---|---|
| heading (clear) | G. H. Saturday | G. H. Saturday |
| 1 | Nz. Pxo. **M-h.** Cpz. | MY OWN [M-h.] BOY |
| 2 | uijt Divsdi Jt. | THIS CHURCH IS |
| 3 | pqqptjuf | OPPOSITE |
| 4 | Qbsl. Qmbdf. | PARK PLACE |
| 5 | uif. mbtu pof | THE LAST ONE |
| 6 | pg. uijt tupdl. | OF THIS STOCK |
| 7 | **M- L.'** Zpvs. Pxo. | [M- L.'] YOUR OWN |
| 8 | **M-h.** Hjsm. | [M-h.] GIRL |

69 enciphered letters; all decoded by the one key.

Reading: *G. H. Saturday. My own [M-h.] boy, this church is opposite Park Place. The last one of this stock. [M-L.] Your own [M-h.] girl.*

"The last one of this stock" most naturally means the last picture postcard of a stock she had; that gloss is mine, not on the card.

English: the plaintext is English (above).

Slovak: *G. H. sobota. Môj vlastný [M-h.] chlapec, tento kostol je oproti Park Place. Posledná z tejto zásoby. [M-L.] Tvoje vlastné [M-h.] dievča.*

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1349/work/solve.py
```

It checks the SHA-256 of `source/` and `work/hires/`, decodes `work/transcription.json`, checks the round trip and prints the lines above.

## Uncertainties

1. **First sign of `Qbsl` (main point; `work/crops/z_Q.jpg`, `w_park.jpg`).** It is pale, and crosses the descenders of line 3. It is a large 2-shaped capital: top arc with a hook start, long diagonal to a small bottom-left loop, tail to the right. The tail then bends down into a short dark foot; darker touches like it recur on pale strokes nearby (first p and first q of line 3, s foot of this word), so it is probably re-inking, not a separate stroke. This is not the 9-shaped Q read on hcp-1369 (`z_park.png`), and it differs from this card's `Z` (`Zpvs`), which has a small flat foot and no closed loop. I read Q because the first sign of the next word has the same build (`Qmbdf`, where only Q gives a word: KLACE, YLACE, FLACE are not words), and PARK makes sense. `Nbsl` = MARK and `Mbsl` = LARK are unlikely, as they would break that match of the two capitals; `Zbsl` = YARK is no word. York Place (`Zpsl`) fails on sign 2, which is b, not this writer's p. The literal letters b, s, l are clear. **The street is unverified:** the reviewer's two web searches found no Park Place in Harrogate, but did find a Park Parade in the Christ Church area and York Place on the Stray. The card clearly spells PLACE, so the transcription stands; the name is the writer's, and it may be a loose name for Park Parade (a possibility only).
2. **First sign of `Qmbdf`.** Its top overlaps the descender loop of the f of `pqqptjuf`, so the upper part of the capital cannot be seen separately. The base oval and tail are clear; Q rests on the word.
3. **`pqq` in `pqqptjuf` (`z_qq.jpg`).** Both middle signs are pale and tangled with the watermark and with line 4. They are bowls with descenders; the second tail closes in a loop (the writer's q), the first tail is less clear and is crossed by another stroke. g would give OFFOSITE, not a word. The t has a curled foot and long top bar; the j's dot and hooked descender are clear.
4. **`tupdl`.** The final l is pale and crossed by the dark descender of the f of `pof`; its looped top and foot are visible (`w_stock.jpg`). STOCK is the only word found.
5. **Abbreviation groups, kept literal (`z_NL1.jpg`, `z_NL3.jpg`, `w_NL.jpg`).** `M-h.` (lines 1, 8; shifted L. G.) and `M- L.'` (line 7; shifted L. K.) match forms read on sister cards ("M-h", "N. h.", "N. L."). The capital has three downstrokes, against two in `Nz` on the same line, the criterion used on hcp-1369; sister cards vary between M and N for what is probably the same group. Their meaning and cipher status are not established. In line 7 the second sign is a long diagonal with top curl and foot, read L; it is similar to `Z`. A short stroke and a dot follow it, reported as an apostrophe-like mark (compare `M. & L.'` on hcp-1407). It carries no reading.
6. **Heading G** could be C on form (sister cards vary); it is clear text and does not affect the message. Word dots are irregular and carry no meaning.

## Why it is correct

One fixed shift, not tuned to this card, gives English for all 69 letters, including the 8-letter `pqqptjuf` and `Divsdi`, whose repeated pattern matches CHURCH. The content is not a stock formula: "this church" refers directly to the printed Christ Church picture. Opening and closing are the couple's formula, the heading's Saturday matches the portal date, and the key matches the sister cards.

## Credits

Capture, transcription, decipherment: Claude Opus 5.5, 2026-10-30. Key and formulae were compared with accepted sister cards in this repo, treated as hypotheses and tested on this card's pixels.

## Response to review 1

Verdict ACCEPT; all three findings are minor, none changes the plaintext of the 69 enciphered letters.

1. **Literal group capital M, not N: fixed.** I re-read lines 1, 7 and 8 on `review/work/r_l1.jpg`, `r_l7.jpg`, `r_l8.jpg` and work/reading.jpg: the capital has three downstrokes, against two in `Nz` on line 1. `work/transcription.json`, the table, the reading, the Slovak and uncertainty 5 now give `M-h.` and `M- L.'`, and the shifted glosses are corrected to L. G. and L. K. These groups were never decoded, so the plaintext is otherwise identical. Re-ran the command: hashes OK, 69 letters, round trip OK, output now shows `[M-h.]` and `[M- L.']`.
2. **"Short dark foot" overstated: fixed.** Uncertainty 1 no longer says it has no parallel and treats it as probable re-inking. It also no longer calls the capital close to `Z`, and marks `Nbsl` / `Mbsl` as unlikely because the capital matches that of `Qmbdf`.
3. **Park Place unverified, Park Parade nearby: fixed.** Uncertainty 1 now records the reviewer's search result and the possibility of a loose name for Park Parade, labelled as a possibility. The transcription stays PLACE. I ran no further street search; the search result is the reviewer's.

Items the review could not verify stay open and are carried into the report: the postmark town, the meaning of the abbreviation groups and of "G. H.", the existence of a Park Place in 1907, and the "last postcard" gloss.
