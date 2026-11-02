REVISE

# Review 1 of hcp-1166 (Claude Opus 5.5, independent reviewer, 2026-11-02)

The solution stands: the card is a MASC digit-and-mark love letter in Hungarian, and the whole text reads as claimed. The key is right. Five sign calls need fixing. One is a wrong word form (Adnatok, really Adjatok). One is an undisclosed sign taken by sense. Three are minor. No claim is refuted at the level of the message.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1166/work/decode.py`: hashes OK, 391 signs, literal lines equal the solver's expected lines. The script's normalised text matches SOLUTION.md except for finding 6.
- Wrote my own decoder, `review/work/decode_review.py`, with the key typed separately. It reproduces all 22 lines from `work/transcription.txt`. All 391 tokens decode, 28 distinct signs, no unmapped sign. It takes each sign as written, so it shows `gonvolok`, `margimkám`, `kühdöm`, the three disclosed `~` signs. It uses `5.` = ly (the hypothesis in finding 5), so it prints `helyet`.
- Read every row of the card against the transcription from my own contrast-stretched crops of the hires scan (`review/work/crop.py`; a*, b*, c* for all rows, d*, e*, f* at 4 to 9x for doubtful signs). All 22 lines were covered. The ordinary rows L01 to L08 and the stanza rows agree sign by sign except as listed below.
- Checked the key against the hcp-1174 table and the sister transcriptions. New signs: `6` = j is confirmed by párja, rája, hagyj (and Adjatok, finding 1). `4.` = gy is clear in eight tokens. `8.` = ty has one token, with a clear dot, and fits kártyát.
- The picture side has no writing. Date on the card reads 1916 IV/11 in clear, address reads as given, postmark date not legible. All as stated.
- Language: period Hungarian, rhymes párja/rája, nekem/engem/édesem, Margitkám/vidám. Names and places fit the Mezőkövesd family. No published solution is attached on the portal per SOURCES.md, and the use of the sister key is declared.

## Findings

1. **major. P11 is Adjatok, not Adnátok.** In `Ad 6, 1. 8, 0 7` the first sign has no comma (`review/work/d_adnatok.png`). The strokes below it are the ascenders of Hadd in the next row: they sit at x ≈ 285 and 343 in the hires scan, where the two d's stand (`c1.png`). Every real comma in this row, such as the one on the 8, attaches lower right of its digit, and the 6 has none. As written `6` = j gives Adjatok, "give (plural imperative)". That is a better word than the conditional Adnátok: it needs no comma dropped, no unmarked long á, and it is what the solver's own English "give me" and Slovak "dajte mi" already say. Fix the transcription to `=Ad 6 1. 8, 0 7`, the literal line, the plaintext, uncertainty 4 (which excuses `Adnatok`) and the note in "Why I believe it is correct" that cites Ad|nátok. `6` then has 4 tokens.

2. **major. A fourth sign is taken by sense without disclosure: the last l of üdvözlettel (B21).** The transcription gives `5,`, but this 5 has no comma (`e_tel.png`). The paper below and right of it is blank. The nearest stroke is about 84 hires pixels to the right, directly under the next sign. It is the comma of `7,` in sok, which needs it. On this writer's other 5s the comma sits about 14 px from the digit (`e_3.png`, a row-P18 crop of `5,`). As written the sign is `5` = h. The word is not in doubt, but the statement "388 of 391 decode as written" is wrong, and the sign should be marked `5~l` and listed in uncertainty 1. It is the same dropped comma as kü-l-döm, so the writer's omission of commas on 5 is now a pattern worth stating.

3. **minor. gon-d-olok is plain 3, so this "against the mark" call can be withdrawn.** The solver reads `3.` taken as d (`3.~d`). The "dot" is below and to the LEFT of the hook of the 3, under its start (`f_3.png`). A dot of `3.` stands at lower right (compare `3.` in kívánom, `f_k.png`). The blob is where the foot of a 3 ends, and the middle of the sign is lost in the rubbed patch. Read it as plain `3`, rubbed. Remove it from uncertainty 1.

4. **minor. The d of maradok (B22) is not simply "abraded": what survives looks more like 8 than 3.** The top is a closed loop with a pointed left corner, like this writer's 8. The stem then runs lower right and a ghost of a lower bowl remains at left (`e_mar.png`). His 3 has an open top. Literal m would give maramok, which is no word. "maradok hű kedvesed" is certain, so the reading stands, but this letter rests on word sense and not on the shape, and SOLUTION.md should say so (mark it `~` or state it in uncertainty 3).

5. **minor. `5.` in helet deserves a note, and the key table should not simply merge it.** The mark in P14 is a clear round dot (`d_helet.png`), the only `5.` on the card. This card has `4,`/`4.` = g/gy and `8,`/`8.` = t/ty, so `5.` = ly would give helyet exactly as the normalised text prints it. Against that, hcp-1179 uses `5.` for plain l (csókollak, legszeb in its transcription), which supports the solver's table. One token cannot settle it. State both options in place of treating `helet` as a settled misspelling.

6. **minor. Script and SOLUTION.md disagree on one word.** The reading printed by `decode.py` has `csokkal`; SOLUTION.md has `csókkal`, and says the normalised text is in the script. Align them.

7. **minor. Slovak error.** "Nenechávaj ma poslednému" is ungrammatical. Use "Nenechávaj ma ako posledného" (and "vezmi ma ako prvého" already matches). Also the Hungarian plural Adjatok is kept by Slovak "dajte", and the English "give me" adds a "me" not in the text, which is acceptable as verse translation.

Numbers after these fixes: findings 2 and 3 cancel, so three signs stay in `~` (Margi-t, kü-l, üdvözlette-l), four if finding 4 is marked, out of 391.

## Claims I tested and found sound

- Margi-t-kám (P18): no comma on the 8, disclosed correctly (`d_mg.png`).
- kü-l-döm: no comma, tick over the 3, as disclosed (`d_kuld.png`).
- be-t-űvel: the long faint stroke starts below and right of the 8 and runs diagonally as a comma does, with one dot left of the 1 (`d_betu.png`). Sound. The word rests on sense, as disclosed.
- izt: a plain 1 with a long flag, no dots (`d_izt.png`); normalising to ezt is an emendation and is disclosed.
- gondolok: the g, thin 0 and smudged 6 with its comma are as described (`d_gond2.png`).
- üdvözlettel: `3.` is a top fragment plus smear, `9,` and `5,` faint but present (`e_uv.png`). Disclosed.
- `S azt`: open and rubbed, with the t in a cursive form with a long bar and foot, under the print (`f_azt.png`). kívánom: k, 1, `3.`, `1'`, `6,`, 0, 8 are all visible (`f_k.png`). Sound, though the 1 is rubbed.
- `?` after nekem as punctuation in the form of 2 with a dot: reasonable by position.

## Not verified

- The HistoCrypt article linked from the portal: not checked by the solver or by me, so whether it discusses this card is unknown.
- The postmark date, unreadable; the date rests on the card's own text and the file name.
- Whether `5.` is ly or l (finding 5).
- Native-level judgement of `izt` as a dialect form. I found no alternative that fits.
