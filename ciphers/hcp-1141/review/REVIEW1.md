ACCEPT

# Review 1 of hcp-1141 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands: 480 signs, one key, continuous rhymed Hungarian, no unread word or clause. I tried to break it on the pixels and did not. All findings are minor. Two of them mean the sign table is stated slightly too conservatively, and neither changes a letter of the plaintext.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1141/work/decode.py` ran: hashes OK (4 files), 480 signs, 96 words, 475 by the table, 5 by sense, 29 distinct signs. Its letters match the SOLUTION.md plaintext; apart from the raw decode line, its plaintext is fixed text tied to the transcription by the word check, as SOLUTION.md discloses.
2. **Independent decode.** `review/work/my_decode.py` has its own table and shows every `~` override: output is the same 24 lines, same 480 signs and 29 signs, and exactly five overrides (nál[h>l]ad, nagyo[j>n], tudó[k>s]ítás, [h>l]átlak, ut[a>á]n). Every sign of the transcription is in the table.
3. **Transcription against the scan.** I read all 24 lines of the hires scan in my own 2x crops (`review/work/crops/L1-6, R1-6`) against the transcription, sign by sign in reading order, and enlarged every disputed point 4-9x (`z_*.png`, `S1-S5.png`). I found no sign where the digit or the mark gives a different letter from the stated reading, other than the points below. Rare words confirm on the pixels: `6.` in tornyosulhat, `9, 0, 3, 3,` in megzörrentve, `2` without dot in harctéri and Galiciába, `2,` in csókomat.
4. **The five `~` points.**
   - nállad: first `5,` is clean; the second 5 has no separate comma and a long foot, as described. Disclosed read.
   - nagyon: final 6 is bare, nothing beneath it. Disclosed read, correct as a word.
   - látlak: the 5 is bare, with no comma. Disclosed read; `hátlak` is no word.
   - tudósítás and után: see findings 1 and 2.
5. **Other flagged points.**
   - kép: confirmed. The comma stands about 25 px clear of the 9 on the hires scan, whereas the real `9,` (the az of lines 7, 8, 21; zörrentve) have the comma tight against the tail. It is punctuation.
   - imádód: high dot followed by the hyphen, no second dot visible. As disclosed.
   - sírig: the comma of `7,` sits just above the open "Mezőkövesd" line, but has the shape and weight of a comma and is apart from the ő accent. `7,` stands.
   - friss: both `7,` have clear commas. The speck between them is tiny and at crossbar height, not a `7.` dot.
6. **Key.** All 29 signs are the family values. I checked the hcp-1174 table, and `1,` = b on hcp-1179, and the `4`, `4.`, `6`, `6.` entries filed on hcp-1145, 1163, 1165. No conflict. The `:1` = u/ü merging is as stated (kunn, nélkül, üdvözletemet).
7. **Language and context.** Period Hungarian with a real poem structure: the five claimed rhymes fall where stated. Salutation, closing `hű imádód` and signature (Árpád) fit the family. `nállad`, `vélled`, `mindég` are plausible writer's forms. Open address and date read on the scan as stated (Őnagysága, Szépreményű Sziber Margitka kisasszonynak, Szomolya, u. p. (Bogács), Mezőkövesd, 1916 II/29). English and Slovak translations are faithful in substance.
8. **Picture side.** Couple at a fence, no writing except the collection stamp. As stated.
9. **Sources.** No published solution used; SOURCES.md records the search and its limits.

## Findings

1. **minor: `után` is probably a clean `1'`, not a `~` read.** SOLUTION.md says the dot "sits at mid-height, nearer `1.` than `1'`". On `z_utan`/`S2` the dot stands about a fifth of the way down the stem, the same relative height as the unquestioned `1'` of látlak directly above it. Real `1.` dots sit at the foot. The transcription should be `1'` with no override. The reading does not change.
2. **minor: `tudósítás` is probably a `7,` as written.** On `z_tudos`/`S1` a stroke of normal comma width starts just under the foot of the 7 and runs into the top of the 1 on the next line. It has the shape of a comma that happens to touch that 1. The `~s` is defensible as caution, but "cannot be separated" understates the evidence. With findings 1 and 2 the count could be 477 by table, 3 by sense.
3. **minor: undisclosed blotted sign in `tavasz`.** The last sign (line 17) has a malformed foot: a blob with a short upright beside the stem, under the crossbar (`S5`, top). There is no free dot as on the sign in `panasz` on line 20. It reads best as `7.` with the dot merged, and the rhyme az / tavasz requires sz, but it is transcribed as a clean sign. It should be listed under Uncertainties.
4. **minor: undisclosed dot above `van` (line 16).** A firm dot stands above the 1 of `3. 1. 6,` (`S3`, middle) in addition to its normal low dot. It lies just right of and below the end of `panaszkodom` on line 15, so it is most likely that line's full stop, or a stray. As part of the sign it would make no word. Another free dot stands near x 1100, y 1202 on the hires scan. Neither is mentioned; a note should say so.
5. **minor: the rule over `a lapokat` is misdescribed.** SOLUTION.md and NOTES.md say the rule rising through these words continues as the section divider. On `z_lapok` there are two strokes. The divider runs separately beneath the words. The rising stroke leaves the divider's left end and stops at the 7 of `lapokat`, with a heavier spot there. It does not continue, so "divider, not a deletion" is less well founded than stated: a partial strike of the phrase is not excluded. The words read in either case and the uncertainty is already flagged, so only the description needs correcting. "Pencil" is also unproved; the stroke has the same grey-blue tone as the faded ink around it.
6. **minor: stale header in `work/transcription.txt`.** It says "see ODD in decode.py", but decode.py has no `ODD`; the value is carried by the `~x` token.
7. **minor: wording.** The open date has a comma-like tail after 1916 (`1916, II/29`), given as `1916.` in SOLUTION.md. The translations render `de` in "nagyon rosszul telnek, de szeretnék" as "and"/"a"; "but" is closer.

None of these blocks FINAL. Findings 1 to 6 should be answered in `## Response to review 1`.

## What I could not verify

- The postmark: a few letters and strokes only (`z_post`), no usable date, so the date rests on the open line, as the solver says.
- Whether the "war report" matches events in February 1916, and any printed source for the verses. The solver did neither, and says so.
- The Schrödel article's figures, which were not examined.
- Whether the rising stroke (finding 5) was meant as a deletion.
