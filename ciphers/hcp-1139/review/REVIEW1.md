ACCEPT

# Review 1 of hcp-1139 (reviewer: Claude Opus 5.5, 2026-11-02)

Verdict: the reading is correct. All 366 signs were compared with the high-resolution scan, and I found no wrong letter and no forced word. Only minor points remain. The main one is that one more sign rests on sense than the solver declares (finding 1).

## What I verified and how

1. Solver's command. `python3 -I ciphers/hcp-1139/work/decode.py` ran clean: `source hashes OK (4 files)`, `cipher signs: 366, distinct: 31; 363 decode by the table, 3 rest on sense (ODD)`. All asserts passed.
2. Claimed plaintext. `review/work/cmp.py` compares the plaintext block in SOLUTION.md (with the `[= ...]` glosses removed) with the block the script prints. Result: `True`. The script's reading block is typed, as SOLUTION.md says, so this only shows the two copies agree. The real check is items 3 and 4.
3. Independent decode. `review/work/verify.py` has its own letter-to-sign table and tokeniser and imports nothing from the solver. On `work/transcription.txt` it gives the same 22 lines. The only unresolved tokens are `9~ö` (twice) and `8~t` (once), so no token falls outside the 29-sign table. Counts: 366 signs, 31 distinct, as claimed.
4. Pixels. `review/work/crop.py` cut the whole message from `work/hires/*adr.jpg` into overlapping bands at about 2x (`review/work/crops/b00L` to `b08R`). `crop2.py` and `crop3.py` made 4x to 7x close-ups of every disputed place. I read all 22 rows, including the boxed signature, against the transcription sign by sign, and they agree except for the points in the findings.
5. Disputed signs on the close-ups:
   - `téged`, line 15 (`l15t.png`): plain 8, no comma anywhere near it. The solver's description is right, and the correction is disclosed.
   - `tubicám`, line 18 (`l18tub.png`): the sign has the entry stroke and single stem of the 1 beside it, with a comma below. The long stroke crossing it comes from the line above. It lacks the top bar plus crossbar of this writer's 7, so `1,` = b stands on shape, not only on sense. `tusicám` is rightly rejected.
   - `hozzád`, line 19 (`l19hoz.png`): a large dot at mid to upper height, as the solver says. Disclosed.
   - `ha`, line 11: stem and dot are visible in the blue blot. Confirmed.
   - Left dot of the first `hogy`, line 2: present, as disclosed.
   - Signature (`box.png`, read upside down): `1' 3, 9 1' 3` = Árpád. Confirmed.
   - Date in the margin (`date.png`): `Mezőkövesd 1916 I/6`. Confirmed.
6. Key behaviour on this card. `.1` (9 times) and `:1` (4 times) never cross for u/ü, and `hű` is the only ű, disclosed. `1'` occurs 11 times, always where á is needed. Sister keys in hcp-1174, 1148 and 1160 agree with the table for the signs they share. No value is invented.
7. Language. It is continuous natural Hungarian with no gap. All four long verse lines scan 6+6 (I counted the syllables), and the rhymes `lehetsz/szeretsz`, `tenéked/téged`, `gazdagságot/boldogságot` come out of the decode. The writer's spellings (`mer`, `máskép`, `beütöt`) are consistent with a casual hand and do not suggest forcing. `beütött a krach` is an idiom known to me, from memory only.
8. Context. Addressee, Szomolya, u. p. Bogács, signature and closing formula fit the family. A New Year letter fits 6 January. The picture side has no writing. Address transcription confirmed from the scan.
9. Sources. NOTES.md, SOURCES.md and the metadata show no attached solution, and I saw no sign that a published one was used. The unchecked HistoCrypt article is disclosed.

## Findings

1. **Minor. Undisclosed sense call in the first `rosszul` (line 3).** The sign after `7,` is a 7, and what stands under it is not a clean dot but a heavy ink blot with a thin tail to the lower left (`review/work/crops/l3blot.png`). That is the position and outline of a comma, like the `7,` directly before it. The pixels do not separate `7.` (sz) from `7,` (s). The transcription gives a plain `7.`, so the sign is counted among the table-clean 363, and SOLUTION.md does not mention it. `rosszul` is safe: the same word stands with a clear `7, 7.` in line 4, and `rossul` would only be a spelling variant. The ledger should list this place and read 4 of 366 by sense, or at least mention it under Uncertainties.
2. **Minor. The two "9-shaped ö" are over-described.** On `l5end.png` and `l20o.png` I see a round 0 with a comma touching it, not a 9. There is no diagonal stem like the true `9,` beside it in line 20. In line 5 the stroke entering from above is the comma tail of line 4's `5,`. The value ö is the same, so nothing changes in the reading. These two signs could count as clean `0,` written tight. The solver may keep the cautious count, but "9-shaped" is an interpretation, not plain sight. This is a judgment on my part and does not block.
3. **Minor. Translation nuance.** `egy kicsit beütöt a krak` is rendered in English as "the crash has rather struck"; `egy kicsit` is "a little, a bit". Slovak "trochu" is right. Suggested English: "in other ways too the crash has struck a bit".
4. **Minor. Key provenance of `2`.** Sign `2` = c occurs once here (`tubicám`). It comes only from hcp-1148, which is not FINAL (its review was REVISE; hcp-1160 has no `2`). SOLUTION.md does say these signs come from cards awaiting review. The report should still state that this one value rests on that card and on this word. The saying "all five are confirmed by words here" is fair, but for `2` and `6.` it is one word each.
5. **Minor. Address normalised.** The card has `ur-leánynak` (no accent, with hyphen), and SOLUTION.md prints `úrleánynak`. The plaintext is declared "spelling as on the card", but the address line is not. Give the literal form or say it is normalised.

No blocker or major finding.

## What I could not verify

- The HistoCrypt article linked on the portal, not opened by me either.
- Whether the verses are a known popular rhyme.
- The postmarks: letters are visible on the stamps but no date (`review/work/crops/pm.png`). The date rests on the writer's own note.
- What the "krach" referred to.
- The meaning of the `>` stroke before `maradok` and of the left dot in `hogy`. Neither affects a word.
