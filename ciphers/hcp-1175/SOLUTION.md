# hcp-1175 solution

Status: complete, review 1 ACCEPT. Every written word reads. The only gap is a dotted line in which the writer withheld the end of a sentence (Uncertainties, point 1). Treating that one line as a single unread item, not as a partial card, is a judgement call about the completeness rule, stated there.

Solver: Claude Opus 5.5, 2026-11-02 (second attempt). The first attempt, also Claude Opus 5.5 on 2026-11-01, was partial and left no SOLUTION.md. The portal lists the card as Not solved with nothing attached, and I found no published solution. The HistoCrypt article the portal links was not checked for this card.

## Cipher type and key

Hungarian open text with one boxed block of digits, five lines, 57 signs. Type: MASC. It is the Mezőkövesd digit-plus-mark key of hcp-1174: each letter is a digit plus an optional mark, and the mark changes the letter. There are no word divisions. Hungarian digraphs have one sign.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o | | `2.` | é | | `6,` | n |
| `0,` | ö, ő | | `3` | d | | `7` | k |
| `1` | i | | `3,` | r | | `7,` | s |
| `1.` | a | | `3.` | v | | `7.` | sz |
| `1:` | e | | `4,` | g | | `8` | m |
| `.1` (dot left of the 1) | u, ú * | | `4.` | gy * | | `8,` | t |
| `1,` | b * | | `4` | f * | | `9,` | z |
| `5` | h | | `5,` | l | | | |

* not in the hcp-1174 table, but ordinary family signs, attested on FINAL sister cards (Uncertainties, point 3).

Ciphertext, line by line (`work/transcription2.txt`):

    5 1. 8 2. 4, 1: 4. 7. 1: 3, 1: 5,
    1 6, 3 .1 5, 0 7 2. 7, 0 3 1. 6, 1: 8
    2. 3, 5 1: 8, 1: 7 1. 7 0 3, 1. 9,
    .1 8, 0 6, 4 0, 1, 5, 0, 3. 0, 8
    8 1. 4, 1. 8

## Plaintext (Hungarian; [ ] = enciphered on the card)

    1915. (X.25.)   [blue-black pen, top corner]
    Kedves Ángyika!

    [Ha még egyszer elindulok és oda nem érhetek akor az uton főblövöm magam]
    (Margitkám!)   [violet, beside the box]

    A szellő is csak azt sugja,
    Amely tőlem hozzád téved,
    A gerle is csak azt bugja:
    Mikor látlak ujra téged?

    Távolban a vágyam-
    nekem;
    Ha te is itt volnál
    velem.   [boxed:] Légy szives irjál
    mert . . . . . . . . m . . . . .
    Sz. A.

Normal spelling of the cipher sentence: Ha még egyszer elindulok és oda nem érhetek, akkor az úton főbelövöm magam.

Address: Tek. Szegedi Jánosné urasszonynak / Szomolya / Borsod m. / u. p. (Bogács). Postmark: OKT 25 is legible, the year is smudged. The pen note at the top gives 1915.

## English translation

Dear Ángyika (a kin word: sister-in-law or aunt by marriage)!

[If I set out once more and cannot get there, then I will shoot myself in the head on the way.] (My Margit!)

Even the breeze whispers only this, / the one that strays from me to you; / the turtle-dove too coos only this: / when will I see you again?

My longing is far away, for me; / if only you too were here with me. Please be so kind as to write, because . . . m . . . (rest left blank by the writer) Sz. A.

## Slovak translation

Milá Ángyika (príbuzenské slovo: švagriná alebo teta cez manželstvo)!

[Ak sa ešte raz vydám na cestu a nedostanem sa tam, tak sa cestou strelím do hlavy.] (Moja Margitka!)

Aj vánok šepká len to, / ktorý odo mňa k tebe zablúdi; / aj hrdlička vrká len to: / kedy ťa zas uvidím?

Moja túžba je ďaleko, pre mňa; / keby si aj ty bola tu so mnou. Buď taká dobrá a napíš, lebo . . . m . . . (zvyšok pisateľ nechal prázdny) Sz. A.

## Command

From the repo root:

    python3 -I ciphers/hcp-1175/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription2.txt`, asserts the result letter by letter, and prints the sign counts and the full card. The open text is hard-coded, so the command reproduces only the decoding of the digits.

## Uncertainties

1. **`mert . . . m . . .`, a withheld clause.** After `mert` the card has only ink dots and short ticks and one written `m`: 8 marks, the m, 5 marks. Three marks are raised: the 3rd before the m (the tallest), and the 2nd and 4th after it. With the dark ink isolated (`work/rev/dots_r.png`) no other letters appear, and the brown overstrike hides none. This looks deliberate, not damaged, so there is nothing further to read, but what the writer meant is unknown: the end of the sentence is withheld. **Judgement call on the completeness rule:** the rule makes a card partial for a whole unread clause, and I count this line as one unread item that stands alone, for three reasons: nothing written is unread, since the marks are not letters; the string is one even run with no visible word space; everything else on the card reads. This is a call about the rule, not a fact about the card. On a stricter reading the card is partial and its register entry should be dropped. **Conjecture, not a reading:** 8 + m + 5 is exactly the letter count of `főbelövöm magam`, the end of the cipher sentence, with the m in the place of the m of `-lövöm`. That would give "Please write, because I will shoot myself". A letter count this short proves little, and the marks do not imitate letter heights consistently: the tallest mark falls on the b of `főbelövöm`, which fits, but the l (position 5) is low, and the raised marks after the m do not fit `agam`. The cipher also spells the word `főb-` without the e. It is not in the plaintext.
2. **`Margitkám` and the addressee.** The card is addressed to Szegedi Jánosné and opens `Kedves Ángyika!`, and `(Margitkám!)` in violet stands beside the box. `ángyika` is a kin word (sister-in-law or aunt by marriage), as glossed on FINAL sisters hcp-1138, 1144, 1165 and 1167, not a name, though hcp-1165 does not exclude a personal name. The likely picture is that the card goes openly to the kinswoman and the digits are for Margit. That Ángyika is Szegedi Jánosné herself, and that the digits are meant for Margit, are inferences from placement and from the sister cards.
3. **Four signs outside the hcp-1174 table.** `.1` = u (twice), `4.` = gy, `4` = f and `1,` = b (once each) are not in that table, but they are ordinary family signs. The key tables of FINAL cards hcp-1138, 1165 and 1167 give all four the same values; hcp-1138 has `4.` in hogy, úgy, ángyika and `.1` in úgy, május, kapuba, and hcp-1165 confirms `4` by `fiú`. On this card each stands in a word fixed by its neighbours.
4. **`.1`, reading of the dot.** On line 2 the dot touches the foot of the 1 and stands clear of the 3 before it. On line 4 it is the first thing in the line, left of the 1, and a brown stroke runs just under it; the dark blob is the writer's ink (`work/rev/z_u2.png`, `z_u4.png`).
5. **`9,` = z.** The comma stands higher than usual, next to the long stem of the 9 (`work/rev/z_z3.png`). Ignoring it would give bare `9` = p and `ap uton`, which is no word.
6. **Spelling as written.** `akor` for akkor has one k, and `főb` lacks the e of `főbe`. `akor` matches this writer's habit of single letters (`legszeb` on hcp-1179, `Angyukádal` on hcp-1178). I do not restore either in the transcript of the signs. `érhetek` is literally "I may reach".
7. **`Távolban a vágyam- / nekem`.** Letters are clear, including the hyphen at the line end and the semicolon. The sense is slightly odd, and I translate it plainly. No printed source of the verse was found.
8. **Date note `1915. (X.25.)`.** It is pen, not pencil: blue-black ink pooled at stroke ends, the colour of the address and `u. p.`, and the 5 has the same detached top stroke as in the digit block. It is probably the writer's own hand. It agrees with the postmark day. The third digit of the year has a blot and a crossing stroke, so 1915 rests partly on the date of the card family (and on the portal file name), not on a clean digit.

## Why I believe it is correct

- 52 of the 57 signs decode by the hcp-1174 table with no change, into a grammatical, single Hungarian sentence. The other 5 use 4 signs outside that table, which FINAL sister cards attest with the same values, and each stands in a word already fixed by its neighbours.
- The new reading fixes what stopped the first attempt. That attempt had inverted many values (for example 1 = é, 3 = m, 8 = d) by forcing `hadifelszerelés` onto line 1, which the hcp-1174 table does not give, and it transcribed `.1` as `1.` and `9,` as `9`.
- It fits the circle of cards: on hcp-1174 the writer apologises that he could not come up to Szomolya, and hcp-1179 is an impatient love note. The sentence is a lover's exaggeration, not a real threat that needs outside evidence.

## Revision 2026-11-02

Earlier status: partial; the first attempt read `hadifelszerelés mal/vél okis omas edir hetekakor a[9]étos[4]ö[1,]lövöddafad`, and the whole block stayed unread except for a guess at the end.

Tried: new 2x and 5x crops of every digit line from `work/hires/` (`work/rev/`, colour and red channel), and I read every sign without the old ledger. I dropped the old key and started from the hcp-1174 table.

Changed: the block now reads in full (see Plaintext). Two transcription corrections: L2 sign 4 and L4 sign 1 are `.1`, with the dot left of the 1, not `1.` or bare `1`; L3 last sign is `9,`. The open verse needed no change except the spelling as written (`sugja`, `bugja`, `ujra`, `szives irjál`). The `vágyam` word, called unsure in the notes, is clear on the 2x crop. The dotted line was examined with the ink isolated and holds no further letters.

`work/decode_partial.py` and `work/transcription.txt` are kept as the record of the first attempt; both are superseded.

## Response to review 1

Verdict ACCEPT, five minor findings. I checked each against the images and the sister cards. No sign, key value or word of the plaintext changed. `python3 -I ciphers/hcp-1175/work/decode.py` was re-run after the edits and still passes: hashes OK, 57 signs, same raw output.

1. **Dotted line against the completeness rule: accepted, status kept.** Uncertainty 1 now states this in the reviewer's terms: nothing written is unread, the string is one even run, the rest of the card reads, the clause is withheld and unknown, and this is a call about the rule. "Every written word reads" stays. On `review/work/dots.png` I count the same 8 + m + 5 marks. The report says the same, and the card gets a register entry on that basis; if the human reads the rule more strictly, the entry should be dropped.
2. **Four "new" signs: fixed.** "New" and "only here" are removed from the key table, Uncertainty 3, "Why I believe" and `work/decode.py`. I confirmed the values in the tables of hcp-1138, 1165 and 1167 (FINAL). I did not recount the reviewer's per-sign card totals and cite only those named cards. One note: hcp-1144 records that `.1` = u was removed from the reviewed key on hcp-1178, so that one card does not support it, but hcp-1138, 1165 and 1167 do.
3. **Date note is pen: fixed.** On `review/work/date.png` the strokes are blue-black pen with ink pooled at their ends. Plaintext, address line, Uncertainty 8 and `work/decode.py` are corrected, and the note on the third digit of the year is added. The note also has a full stop after 1915, now transcribed.
4. **`Ángyika` gloss: fixed.** Added to both translations and to Uncertainty 2, which also keeps hcp-1165's caveat that a personal name is not excluded.
5. **Description of the dots: fixed.** Three raised marks, with the `b` and `l` positions and the misfit after the m stated in Uncertainty 1. The conjecture stays a conjecture and stays out of the plaintext.

Open, as the reviewer lists: the HistoCrypt article was not read, the verse source is not found, the sense of `Távolban a vágyam- / nekem` is only a plain reading, the meaning of the dotted line is unknown, the postmark year is smudged, and who made the brown overstriking is unknown.
