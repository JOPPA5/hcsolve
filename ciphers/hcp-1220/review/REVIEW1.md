ACCEPT

# Review 1 of HCP1220 (Claude Opus 5.5, 2026-11-02)

The 12 ciphered rows are correct: my own sign-by-sign reading gives the same letters as the ledger on every row. The only weak part is the end of the plain stamp-box note, and the solver disclosed that. Only minor points remain. They are corrections and labelling, not changes to the reading.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1220/work/decode.py` ran; all four SHA-256 checks passed. Its output matches the rows, normalized text and stamp note in SOLUTION.md.
- **Independent decode.** `review/work/glyphs.txt` is my own row transcription in sign-class names, made from new crops of the hires address side (`review/work/rows.py`, `r01a` to `r12b`, 2x). I made it knowing the claimed reading, so it is not blind. `review/work/indep.py` decodes it and diffs it against `work/ledger.txt`:
  `python3 -I indep.py glyphs.txt ../../work/ledger.txt`. Rows 01 to 12 agree exactly. Row 13 differs in one sign (finding 2). Total 177 tokens, of which 176 carry a letter and 1 is the `?` mark, so the "177 signs decoded" line counts the unassigned mark too.
- **Key coverage.** Every sign on the card maps to the family classes (`hcp-1216/work/graphic-key.json`). No new sign value was needed. The left-tick d / right-tick h-p distinction holds: all 4 d and 7 h/p signs agree with their words.
- **Every restoration checked on pixels:**
  - Row 3 `mely`, row 6 double h (two complete signs, confirmed; the crops' overlap was taken out), row 4 undotted first o: as stated.
  - Closed s (rows 1, 1, 2): closed loops as stated. The o sign elsewhere has a crossing tail, so the call is reasonable.
  - Row 5 first i: blot with its dot visible, as stated.
  - Row 7 raised mark: a small heavy x-shaped mark, as stated (see finding 1).
  - Row 11 blot: F-like arms, as stated. `t` by the word is the only reading, disclosed.
  - Row 12 star in a stain: `f` by the name, disclosed. The sign after it does have three bars.
- **Stamp box.** I built my own ink map that suppresses the blue imprint (`review/work/stamp.py`, `box_ink.png`, `ink_mid.png`, `ink_low.png`), not using `work/unmix.py`. It shows:
  - `hit remény`, `és szere-`, `tet`, `se` and `sziv` clearly.
  - `kös-` legibly: tall loop, o, s, hyphen.
  - `össze` as arches, then a z whose descender loops into the row below, then e. This supports the solver's explanation of the false "d" in `szivün-`.
  - `ün` as heavy, overlapped arches, compatible only.
  - Last row: a short peak, a speck, then a small letter merged with heavy strokes.
  On balance `kösse össze sziv-` is seen on the card, and only the ending `-ünket` relies mainly on the formula. HCP1234 (review ACCEPT) carries the same formula. No competing wording fits. I do not treat this as an unread clause, so the card can count as complete.
- **Language and context.** The text is ordinary period Hungarian in the family's register (`szeretett édes Jolánkám`, `viszontlátásra`, `hű kedvese Feri`). Addressee, place and signature fit the family. English and Slovak translations are faithful.
- **Honesty.** Portal status Not solved, nothing attached; no published solution used or claimed. Credit is truthful.
- **Plain parts.** Address and the pencil line along the top are as stated. Picture side: hussar and girl, printed 2541, plus a small publisher's mark in the corner, no writing.

## Findings

1. **minor. Row 7 acute is not on the card.** The ledger has `e:a` in `délutan` ("acute tick seen"), so the literal row prints `é`. On a 4x crop (`review/work/blot7.png`) this e has three plain bars and no tick. The only mark nearby is the raised x-shaped blot to its upper left. So the header "accents only where a mark was seen" is false for this sign, and `délután` should come out of the "Why it is correct" list of accented vowels. The raised blot may be a spoiled acute. Uncertainty 3 should offer that as an alternative to "false start". Fix: `e` in the ledger, and amend the two statements.
2. **minor. Row 13 second sign has two bars but the ledger gives plain `e`.** SOLUTION.md discloses this, yet the ledger token has no `!` flag, so the printed `feri` looks like a clean read. Literally it is `fari`. `e` is still right: e signs with a nearly lost third bar occur on this card (row 2 `becses`). Fix: mark it `e!`.
3. **minor. Sister-guided stamp wording is printed without marks.** `work/plain-note.txt`, the literal block and the normalized text show `kös-`, `se össze`, `szivün-`, `ket` as plain reading. Only `tet` and earlier are firm. Fix: mark the guided letters in the literal text, for example `sziv[ün]-` and `[ke]t`, and repeat that in the report. SOLUTION.md also says "The t is clear" in the last row. I find it compatible, not clear, because it merges with the heavy strokes above it.
4. **minor. Undisclosed overwrite in row 5.** The ü of `örülök` is a heavy star-shaped overwrite with a thin earlier arc to its left (`review/work/blot5.png`), not mentioned in uncertainty 5. The dots and the hooked arm still give ü, so the reading stands. Add it to the list.
5. **minor. "Why it is correct" slightly overclaims.** `megkaptam` needs the h/p call and `viszontlátásra` needs the restored t, so they are not fully "unforced". `köszönök` has dots on only two of its three vowel positions needing them in the standard spelling. Reword.
6. **minor. Date.** Uncertainty 10 calls the cancels unread. The receiving cancel at the top shows `DEC` and `27` when rotated (`review/work/pm_110.png`), which agrees with the -12-27 in the filename. No year can be read. State December 27, year unread.
7. **minor. Bottom of the stamp box.** The green strip with a `FIL` denomination is the surviving lower part of the stamp, not only a damaged area. It may still cover ink. Say so in uncertainty 1.

## Could not verify

- The year, and the second cancel beyond isolated characters.
- Whether any writing remains under the surviving stamp strip.
- `-ünket` independently of the formula. Whether the last-row peak is really k.
- The nature of the raised mark in row 7.
- The HistoCrypt article linked on the portal. I did not read it; neither SOURCES.md nor the solver says it was consulted.
- My reading was not blind, because the claimed text was known before I looked at the crops.
