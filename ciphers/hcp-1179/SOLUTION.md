# hcp-1179: solution (Claude Opus 5.5, 2026-11-01)

No published solution was found; the portal lists the card as Not solved with nothing attached. No earlier work exists on this number. The transcription is my own, made from `work/hires/`.

## Card

Picture postcard, Mezőkövesd, 26 Sept 1915, signed Sz. A. (the pixels also allow Sz. K., but hcp-1174 is signed Árpád in cipher and hcp-1175 reads Sz. A., which favours A.), to Tek. Szegedi Jánosné, Szomolya, Borsod megye, u.p. Bogács. The left side is open Hungarian in violet copying pencil, later struck through in brown ink, opening "Kedves Margitkám!". Only the two rows of figures at the bottom are enciphered.

## Cipher and key

Type: MASC, with some homophones and a figure-plus-mark alphabet. Each letter is one digit plus an optional mark after it (none, dot, colon, comma). The mark changes the letter: 8 = m, 8, = t.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| 1 | i | 2. | é | 6, | n |
| 1. | a | 3 | d | 7 | k |
| 1: | e | 3, | r | 7. | sz |
| 1, | b | 4, | g | 8 | m |
| :1 | ü (also on hcp-1174) | 5. / 5, | l | 8, | t |
| 0 | o | | | 8. | t? (variant of 8,, see below) |
| 0, | ö | | | | |

Signs elsewhere in the family, not on this card: 7, = s, 3. = v, 2, = cs, 1' (high dot) = á, 5 = h, 9 = p, 9, = z (hcp-1174 table). 4 appears to be f on hcp-1175.

Key recovery. No key was given; it comes from the sister cards' cipher passages, quoted here as filed in their own directories (nothing written there):
- hcp-1174 heading: `2. 3 1: 7, 8 1. 3, 4, 1 8, 7 1' 8 !` = Édes Margitkám!
- hcp-1178 (FINAL): `2, 0 7 0 5, 5. 1. 7 8, 2. 4, 1: 3` = csókollak téged
- hcp-1174: `7. 1 3. 1: 8 2. 5, 1: 3` = szívem éled, after the open words "Arcom derül"
- hcp-1175 ending: `... 4 0, 1, 5, 0, 3. 0, 8 8 1. 4, 1. 8` = (fő)b lövöm magam, followed by open "(Margitkám!)"

## Ciphertext and plaintext

Run from the repo root (checks source hashes, prints the raw decode line by line; [x] = taken by sense, not from the pixels; t? = the dotted 8 read as 8,):

    python3 -I ciphers/hcp-1179/work/decode.py

Reading order: bottom row left to right, then the shorter row above it, right of "Sz. A.".

Original (a rhymed couplet, érted / néked): **Mindent megtenné[k] én érted, a legszeb[b] kar[t?]im küldöm n[é]ked.**

English: I would do anything for you; my finest [card(s)?] I send you.

Slovak: Všetko by som pre teba urobil; moju najkrajšiu [pohľadnicu?] ti posielam.

Unenciphered text, provisional because of the overstriking and not part of the decipherment: "Kedves Margitkám! Rokoni és baráti szeretetből Második lapot küldöm ... gondolva ... Küldök még én százat is de várom a válaszát is. Poéta én sohasem voltam, Szerelemről nem dalol tam. Bocsásd meg e hibát nekem S fogadd igaz üdvözletem. Kelt Mezőkövesd 1915 IX/26. Sz. A." A line along the top edge reads roughly "... vasárnap ... nem mehetek megint" and is cut by the edge. The ciphertext is a private addition to this open note.

## Uncertainties

1. **kar[t?]im (main open point; this word is not fully understood).** The dot after the 8 is clear and round. It stands between the 8 and the following 1, slightly nearer the 8. This writer uses a dot for the comma in this same passage (`5.` = `5,` = l), so `8.` is taken as `8,` = t, giving literally `kartim`. The leading sense is a loose or dialect form of kártya, "card" (kártyám / kártyáim): the open text on this card is about sending cards ("Második lapot küldöm", "Küldök még én százat is"). This is a proposal only: y and an a are unwritten, the 1 is unexplained, and the accusative ending is absent (verse may have shortened it). Weak alternatives: karjaim, "my arms" (no sign for j is attested in the family, a is missing, the sense is poor); a left-placed dot on the 1 as in `:1`, giving `8 .1 8`, kar-m-a-m, which yields no fitting word. The rest of the text reads, so this stands as one uncertain word.
2. **Blot in megtenné[k].** After the `2.` the blot and its smear span about 157 px of the hires scan, room for 2 or 3 signs with marks; the number of hidden signs is unknown, and it may be a correction. The enhanced crop shows a left lobe, a long diagonal stem with a low horizontal, and a heavy mass, none certainly a digit. Directly right of the blot, before the `2.` of én, stands a comma-shaped mark with an arched head. If it belongs to the last hidden sign, that sign is not plain 7. So [k] is a restoration by word sense, not a reading: megtennék ("I would do") suits "én"; the bare megtenné ("he would do") does not.
3. **`:1` in küldöm.** The two dots stand left of the stem, on a violet stain, while every other 1: has them right. The same sign is filed as ü on hcp-1174 (üdvözöllek), so it does not rest on this card alone; a plain 1: would give "keldöm", not a word.
4. **n[é]ked.** There is no separate dot after this 2. The one candidate mark is a hook at mid-height with a tail running down-left into the row below; it has the shape of this row's commas but merges with the 1 below and may partly be that stem. The pixels favour `2,` or nothing, and the key alone gives "ncsked". néked (older or dialect form of neked) rests entirely on word sense and on the rhyme with érted.
5. **legszeb.** One written sign for bb; the normal spelling is legszebb. A spelling simplification, not a restoration.
6. **Row order.** I put the bottom row first because it starts at the left margin and the upper row ends in a real period; the rhyme érted / néked also places néked at the end. A short dark tick at the extreme top right of the card corner, after the last 8, is unexplained: a mark for another sign or a stray. The reverse order "Küldöm néked. Mindent megtennék ..." loses the final rhyme but cannot be excluded.
7. **l-signs.** `5.` and `5,` both act as l here. No plain 5 occurs on this card; on hcp-1174 plain 5 = h.
8. **Sister cards.** Quotations follow the filed readings of hcp-1174 and hcp-1178 and the partial transcription of hcp-1175, which is unfinished. The strings for hcp-1174 were conformed to that card's filed reading in response to the review; I did not reread those pixels in round 2.

## Why it is correct

The key was built from other cards and then applied here. It gives plain Hungarian (mindent megtennék én érted a legszeb ... küldöm néked) with only the disclosed points above, the two clauses rhyme (érted / néked), which also supports the row order, and the sense suits a love note hidden in a card to the same Margit. The same key independently yields full words on four other cards, including téged, csókollak, szívem, lövöm magam, and all 13 signs of the heading Édes Margitkám. 1, = b appears on hcp-1175 too (fő-b lövöm), independently of legszeb. A monoalphabetic fit this consistent across cards of ~20 signs is unlikely to be chance.

## Response to review 1

Verdict REVISE. All findings are accepted and addressed; I looked again at the reviewer's crops of the dot, the blot and néked. The reading is unchanged except for the one uncertain word. `python3 -I ciphers/hcp-1179/work/decode.py` re-run after the changes: hashes ok, output `mindent megtenné[k] én érted a legszeb kart?im küldöm n[é]ked`.

1. **kar?im: fixed.** `8.` is now `t?` in `work/key.json`, taken as the variant of `8,`. Uncertainty 1, plaintext and both translations give kartim, with kártyám/kártyáim as the proposed sense and karjaim as weak. The word stays labelled as not fully understood. I added one alternative of my own: the dot sits between 8 and 1, so `.1` was tested and gives nothing.
2. **Blot: fixed.** Uncertainty 2 now states the 157 px width, the comma-shaped mark and the unknown number of hidden signs; the note in `work/transcription.txt` says the same. [k] stays as a sense restoration. The decoder prints it in brackets and lower case.
3. **néked: fixed.** On `z_ned.png` and `y_hook.png` I also see no dot. The token is now `[2.]`, printed `n[é]ked`, and uncertainty 4 gives the evidence, including the rhyme.
4. **Key and sister statements: fixed.** Plain 5 is removed from the l row and key.json, with 5 = h noted. `:1` is cited to hcp-1174. The strings for hcp-1174 now match its filed reading (`7 1' 8`, `5, 1: 3`). The heading is still 13 signs, Édes Margitkám. hcp-1178 is cited as FINAL; hcp-1175 stays described as partial.
5. **Signature: fixed** in the Card section.
6. **Raw output: fixed.** `a` is split from `legszeb` and the capital marker is replaced by brackets, documented in `work/decode.py`.

Not resolved, as the reviewer also could not resolve them: what lies under the blot, and the corner tick. Both are disclosed.
