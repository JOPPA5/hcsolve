# HCP 1378 / pc_hcp_59: Caesar (+1) postcard, 14 Nov 1907

Status: **whole message read; review 1 verdict ACCEPT (four minor findings, addressed below); no decoded letter changed.**

## Origin

HC Portal cryptogram 1378 (`pc_hcp_59`), portal status *Not solved*, language Unknown, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). Picture side: printed view "Sea Front, Herne Bay", No. 13590, The Wrench Series, no handwriting. Address side: halfpenny Edward VII stamp, postmark WIMBORNE / NO 14 / 07, receiving mark NEWTON ABBOT NO 15 07; addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (portal spells the recipient "W. Abboú"). No published solution of this card was found or used. No separate web search for one was made; the orchestrator's register check found no record.

The circular alphabet disc on both scans is a collection overlay, not part of the card.

## Cipher and key

Monoalphabetic Caesar: each plaintext letter is written as the **next** letter of the alphabet; decrypt by subtracting one.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The key was taken as a hypothesis from the Abbott sister cards (hcp-1386, 1397, 1398 and others) and verified on this card alone. Only part of the card is enciphered: heading, date and the name of the monument are in clear.

## Transcription and plaintext (all writing on the card)

Rotate the address side 90 degrees counter-clockwise (`work/crops/rot.png`).

| Card | Reading | Mode |
|---|---|---|
| G. H. Thursday. | G. H. Thursday. | clear |
| Nz. Pxo. E. L. Cpz. | MY OWN [E. L.] BOY | cipher, E. L. literal |
| Ibwf. J. Tfou | HAVE I SENT | cipher |
| dbse. pg. | CARD OF | cipher |
| The Martyrs Memorial | The Martyrs Memorial | clear |
| Oxford. | Oxford. | clear |
| Nov. 14th 07. (left) | Nov. 14th 07. | clear |
| Zpvs Hjsm (right, same physical line) | YOUR GIRL | cipher |

31 enciphered letters, all decoded by the one key; 2 abbreviation letters kept literal. The date and the signature share the last physical line, date at the left and signature at the right; the long underline below `Hjsm` is a flourish, not text. There are seven physical lines of writing.

English (plaintext language): *"G. H., Thursday. My own E. L. boy, have I sent card of The Martyrs Memorial, Oxford? Your girl. Nov. 14th 07."*

Slovak: *„G. H., štvrtok. Môj vlastný E. L. chlapec, poslala som pohľadnicu Pamätníka mučeníkov v Oxforde? Tvoje dievča. 14. nov. 1907."*

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1378/work/decode.py
```

It checks the SHA-256 of the two source images and the two hires originals, decodes every token of `work/transcription.json`, checks the inverse round trip, and prints the plaintext, the letter counts and the weekday check.

## Uncertainties

1. **`Tfou` (SENT).** The T and the f are run together and share the top bar (`work/crops/w3.png`): the T stem ends in its usual left hook as in "Thursday", the f is this writer's looped descender as in `Ibwf`. Read as two signs by shape; a single-sign reading gives no word (`?ou` = ?NT gives no English word).
2. **`dbse` (CARD).** The first sign has a long lead-in and a tall slanted ascender (`work/crops/w4.png`, `review/work/w_dbse.png`). It is not the same shape as the short, a-like d of "Thursday"; what excludes A is the word (`Abse` would give Z-ARD), and a capital D would decode the same. The last sign is open with a notched right end, so it could be e or c by shape alone; `e` rests on the word, since `dbsc` would give CARB.
3. **u/v/w signs in `Pxo`, `Ibwf`, `Zpvs`.** The middle sign of `Pxo` (OWN) is a blot with a stem and a rising stroke (`review/work/w_pxo.png`): `x` is plausible but not positively seen, `w` would give OVN, and the reading rests on the couple's recurring formula on the sister cards. The third sign of `Ibwf` (`review/work/w_ibwf.png`) is a small two-humped form joined to its neighbours and hardly differs from the `v` of `Zpvs`. In these tokens the choice among u, v and w rests on the word (HATE/HAVE, YOUR), not on the pen shape.
4. **`E. L.`** is kept literal, as on the sister cards; a shifted value (D. K.) or an expansion such as "ever loving" is not proved. Heading initials G. H. are not expanded (sister cards have C or G).
5. **The clear words.** "Martyrs": the t-bar is taken to be the long stroke above "yr" (it could instead be an underline of `pg`); there is a gap before the final s and no visible apostrophe. "Memorial": the final l sits high at the card edge. Shifting these lines would give nonsense (SGD LZQSXQR ...), so they are clear text.
6. **Question.** No question mark is written; the inverted word order makes it a question in the reading. Punctuation is editorial.
7. The sender's meaning (which card, whether it survives) is unknown. No sister card in hcp-13xx/140x mentions Oxford or the Martyrs' Memorial in its solution or notes.

## Why it is correct

One fixed shift turns all 31 enciphered letters into English without exception, and there are no unused signs. MY OWN, BOY, YOUR, GIRL are the couple's recurring formulae (hcp-1386, 1397, 1398), and the sentence reads naturally with the clear monument name. Heading "Thursday" and "Nov. 14th 07" agree with the postmark, the portal date and the calendar (14 Nov 1907 was a Thursday). The Martyrs' Memorial is a real monument in Oxford, and the sentence fits a card about a sent picture postcard.

## Response to review 1

Verdict ACCEPT. All four findings are minor; no decoded letter changed. `python3 -I ciphers/hcp-1378/work/decode.py` re-run after the changes: hashes OK, 31 enciphered and 2 literal letters, weekday OK.

1. **v/w uncertainty disclosed for only one of three tokens.** Fixed: Uncertainty 3 now covers `Pxo`, `Ibwf` and `Zpvs`. Rechecked on `w_ibwf.png`: the sign is two humps joined to b and f, so the choice rests on the word.
2. **`d` comparison overstated; last sign of `dbse` not filled.** Agreed and fixed in Uncertainty 2. On `w_dbse.png` the first sign is long and slanted, unlike the d of "Thursday", and the last sign is open with a notch. CARD stays on the word alone.
3. **`Pxo` middle sign.** Agreed; rechecked on `w_pxo.png`. It stands as context-supported, and Uncertainty 3 now says so outright.
4. **Layout not recorded.** Fixed: `work/transcription.json` and the table now put the date first and the signature second on the same physical line, with layout notes. The underline is recorded as a flourish. The running English keeps signature before date as the natural reading order.

The points the reviewer could not verify remain open and are not claimed: E. L. and G. H. are not expanded, the Oxford card is not identified, and no web search for a published solution was run.

## Credits

All transcription and decipherment by Claude Opus 5.5 acting as solver, 2026-10-30. Key hypothesis from the accepted sister cards in this repo. No earlier work on this number.
