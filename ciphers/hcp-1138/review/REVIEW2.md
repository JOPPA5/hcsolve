REVISE

# Review 2 of hcp-1138 (reviewer: Claude Opus 5.5, 2026-11-02)

The key, the transcription and the reading all stand. All ten findings of review 1 are fixed. One real error is left, and neither the solver nor I caught it in round 1: `akkor ra` is one word, `akkorra`, "by then". That removes the solver's main open clause and changes both translations. One visible mark at the same place is undisclosed. No sign value changes, and no further full review is needed once these fixes are in.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1138/work/decode.py`: 4 hashes OK, 409 signs, 85 words, 3 plain 9 as z, 1 `8.`, no mismatch. Output agrees with the SOLUTION.md plaintext. The enciphered text is now printed from the asserted words, and the address is hard-coded and labelled as such.
- Made a new rotation at 46 degrees from `work/hires/..._adr.jpg` (`review/work/r2/t.py`, `r46.png`), so the rows run level, not the 51 degrees used before. Cut 16 overlapping tiles at 2x (`r2/c.py`: A1 to F2) and 3x to 4x enlargements of disputed spots (`r2/z.py`: Z1 to Z4). I went through all 20 rows sign by sign, so this was more than a sample. It was not blind: I had read the transcription first.
- Wrote `review/work/r2/own.py`: own table, own row list, no reading column, and my own word divisions. Output:

      édes margitkám
      értesitlek hogy májusba fognak sorozni
      de csak azokat akik még nem voltak sor alatt tehát
      most már nyugott lehec édes de most már ne szedjétek le a hernyot hagyjatok ugy mindent
      aztán ugy volna jo kevesem ha már mostanába lejönne ángyika házat nézni hogy akkorra lenne
      de most többet nem irok mert rosszul vagyok ugy veszem észre ott a kapuba alaposan megfáztam
      kártyámon e kis virág tolmácsolja érzelmem
      minden orád a távolban jol teljen
      most üdvözöl és számtalanszor csokol szeretö kedvesed árpád
      signs 409
      solver 409 identical

  The sign list matches `work/transcription.txt` exactly. The only text difference is the word division in finding 1.
- Round 1 fixes, checked on the pixels:
  - `0 8, 8, 1. 7 1. 9 .1` plus dash, then `1, 1.` (kapu-ba): D3, D1.
  - `8, 0, 1, 1, 1: 8, 6, 1: 8` plus dash (többet nem): D3.
  - `1. 8,` at the end of házat: C3.
  - The full comma on `5,` of lejönne: C2.
  - `6 1.` in tolmácsolja, with the stroke at the top right coming from the `6,` above: E1, E2.
  - `8.` in kártyámon, with a clear low dot: E1.
  - The gap in `üdvözöl és`: F1, F2.
- Plain 9s: no comma at azokat (B2), aztán (C2) or házat (C3). The writer's real `9,` is a separate short stroke beside the tail (`sorozni`, `nézni`, `érzelmem`, `üdvözöl`, `megfáztam`), so the three really do lack it. The stroke above the házat 9 reaches down from the `7,` of the row above. The disclosure is correct.
- `lehec`: Z3 at 4x shows a bare 2, with no comma and no dot. Correct as stated.
- `még`: the curved stroke after the 4 is the comma of `4,` (B3). This is the same curved form as at `8,` ends of rows. It is not a `)`.
- Row-2 blot and stray marks (`már` dot, `)` signs, `:` after megfáztam, violet pencil): all as disclosed.
- Key: `Édes Margitkám` is the same 13 signs as `hcp-1174/work/decode.py`. FINAL hcp-1142 (`kártyán`) and hcp-1164 (`kártyát`) do read `8.` = ty. hcp-1146 I only confirmed as FINAL; I did not find `8.` there in my grep. It does not matter, because two cards are enough.
- Coverage: every sign decodes with the table. Plaintext is real Hungarian of the period with a dialect or careless spelling. `szedjétek le a hernyót` fits caterpillar nest removal in early spring; `sor alatt` is the idiom for military service. Names and date fit the Margitka and Árpád series. hcp-1144 also has `ángyika` and `lejösz`.
- Sources: no published solution seen on the portal capture. The HistoCrypt article is disclosed as unread.

## Findings

1. **major. `akkor ra` is one word, `akkorra`, and the clause is not obscure.** The signs `1. 7 7 0 3, 3, 1.` run without a gap (`r2/Z1.png`, D2); the two 3s nearly touch, and the spacing is no wider than inside a word. `akkorra` is ordinary Hungarian, "by then, by that time". The clause is `ángyika házat nézni, hogy akkorra lenne`: "to look at a house, so that by then there would be one". The word break was the solver's own, as the Command section says, and I carried it over in round 1 without testing it. So, in the solver's files:
   - transcription and plaintext: one word, `akkorra`; word count 84, signs still 409
   - English and Slovak: replace "so that then it would be up to her(?)" and "aby potom bolo na nej(?)". The subject is left unstated on the card, most likely the house; keep a light marker on that alone. By then probably means May, but that is my inference
   - delete Uncertainty 2, and `ra = rá` from the odd forms
   - review 1's "could not verify" item on this clause is closed by this finding

2. **minor. Undisclosed dot at the first 7 of `akkorra`.** `r2/Z1.png` shows a grey dot below right of that 7, with a thin grey trail running down to the 7 of row 11. It sits where the `7.` dot sits. Read strictly, the sign is `7.` (sz), giving `aszkorra`, which is no word. It is paler than the writer's dots, and the trail suggests a smear or pen drag, so plain 7 is the right reading, by word sense. It should go into the Uncertainties with the other stray marks. The transcription need not change, but this is a reading by sense and has to be said.

3. **minor. Slovak: `vzdialene` is awkward.** `nech ti každá hodina vzdialene plynie dobre` should be something like `nech ti každá hodina v diaľke plynie dobre`, matching "in the distance".

4. **minor. Counts to update after finding 1.** Card section and "Why I believe it is correct" say 85 words. The sentence "with one fixed table and no unread word" can stay. The list of open questions in the report must not carry `akkor ra` forward.

## Findings not made

All other signs and readings stand. `ke(d)vesem`, `lehec`, `nyugott`, `kapuba`, `mostanába` are as disclosed. `Kívánom:` and the date and place are in clear. I found no forced restoration: nothing on this card is restored beyond the disclosed `(d)` and the three plain 9s.

## Note for the solver

Finding 1 changes one word division and one clause of translation; no sign or key value changes. In my view that is not a substantial change under README step 5, so it can go to the report, register entry and `FINAL` without another round. Whether to do so is the solver's decision. With `akkorra` no whole clause stays unread, so the card counts as complete.

## What I could not verify

- The grammatical subject of `akkorra lenne`. It is unstated on the card; the house is the likely reading.
- What `ott a kapuba` refers to, and who `ángyika` is.
- The exact postmark date, which is partly hidden. I did not recheck it this round.
- Whether the row-10 dot is ink from the writer or a later smear. It cannot be settled from the scan.
- The HistoCrypt article, which I did not open. I also did not review the sister cards' pixels.
- My sign-by-sign pass was not blind, so an error shared with the solver's reading is unlikely but possible. The 4x enlargements cover only the disputed spots.
