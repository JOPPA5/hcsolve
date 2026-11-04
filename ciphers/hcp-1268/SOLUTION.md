# HCP1268 — Holes Ferenc to Jolánka Tóth: an invitation for a Sunday, posted 17 January 1912

**Status: complete. Every written sign is read and the message reads. The last word before the signature, written *ravoban*, is read as *[a] távolban* by word sense, with one substituted and one missing letter; rows 6–7 keep one open choice, *szabók* or *szabónk*.** Written 2026-11-01 by Claude Opus 5.5, corrected after review 1. There was no earlier work on this number.

Portal status: Not solved, no attached transcription or solution. No published solution was used. The article linked on the portal (HistoCrypt) is the collection reference; it was not consulted for this card. The key comes from the finished family cards of this repo (HCP1216, 1213, 1217, 1218, 1243, 1285, 1301), whose earlier work was partly done by the OpenAI GPT solver and completed by Claude Opus 5.5. The surname rests on HCP1278, 1303 and 1309.

## Cipher type and key

Hungarian (the portal says Unknown), simple monoalphabetic substitution with invented graphic signs, the Jolánka family key without change:

2026-11-03: type for the register is **MASC + Steganography**: the four cipher rows in the stamp box (*Csókolom a kis szájat*) were written where the stamp was to be stuck, so they were hidden once it was on. The stamp is no longer on the card. See "Stamp-box message (2026-11-03)".

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl (with hook) | c / g on this card, see below | three short strokes | m | gamma | t |
| long + short stroke, short at left | d | two short strokes; tail with arches after a loop | n | plain or crossed x | u / z |
| three bars | e | cursive loop | o | chevron (both ways up) | v |
| upright cross + | f | tall + tick, high | h | low descender | y |
| crossed curve, dotted or not | i | tall + tick, low | p | inverted T | j |

The open bowl with an inner hook gives g in *legjob*, *meg* and, joined to y, *gy* (*hogy*, *egylet*). The barred left bowl (€) followed by the right bowl gives cs (*hacsak*, *becses*, *csókolom*). Dots over a loop or cross give ö/ü; two ticks give ő.

Text runs left to right in 15 rows, with four rows in the stamp box. Row 7 begins with two plain words or parts of words, *meg hi*, then returns to cipher in mid-word.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1268/work/decode.py
```

It checks the SHA-256 of both source scans and both hires originals, applies the key in `decode.py` to the manual sign ledger `work/ledger.txt` (236 tokens, each named by the shape of the written sign) and prints the literal rows and `work/normalized.txt`. The ledger is a manual reading from enlarged crops (`work/crops/`), not OCR, and not blind: the key was known and word sense helped. The normalized text is editorial and is not generated from the ledger.

## Literal decipherment

```
01 kedvesedesjolankam      09 leheebbemenjünk
02 kivanomtisztaszi        10 asirjameghogy
03 vebőlhogylegjob         11 mibenalapodor
04 kedvebentalalja         12 megbecsessorait
05 soraim.olvastan         13 varvamaradokepe
06 azegyletbenaszabo(n?)k  14 dőszivel{a}ravo
07 meg hivojesvasar        15 banholesferen{c|k}
08 naplesz{e|a}zishacsak   stamp: csoko / lom / akis / szajat
```

## Hungarian (normalized)

Square brackets restore omitted letters. `{r=t}` marks a written r taken as t. `{a}` is a struck sign.

Kedves édes Jolánkám! Kívánom tiszta szív[em]ből, hogy legjob[b] kedvében találja soraim olvastán. Az egyletben a szabók (or: szabónk) meghívój[a], és vasárnap lesz ez is. Hacsak lehe[t], ebbe menjünk. [É]s írja meg, hogy miben ál[l]apodo{r=t}[t] meg. Becses sorait várva maradok epedő szív[v]el {a} {r=t}ávo[l]ban. Holes Ferenc.

Stamp box: Csókolom a kis szájat.

Plain writing, not cipher: Szépreményű Tóth Jolánka kisasszony saját kezeiben, Jász-Árokszállás, Alszög.

## English

Dear sweet Jolánka! I wish with all my pure heart that on reading my lines you may find yourself in the best of spirits. In the association there is the tailors' invitation (or: our tailor's invitation), and this too will be on Sunday. If it is at all possible, let us go to this one. And write and tell me what you have agreed on. Awaiting your esteemed lines, I remain with a yearning heart in the distance. Ferenc Holes.

Stamp box: I kiss the little mouth.

Plain writing: To the promising Miss Jolánka Tóth, into her own hands, Jász-Árokszállás, Alszög.

The postmark date, Wednesday 17 January 1912, is the posting date. The Sunday of the card is a later day, 21 January at the earliest; the card does not give it.

## Slovak

Milá sladká Jolánka! Z čistého srdca si želám, aby Vás moje riadky zastihli v najlepšej nálade. V spolku je pozvanie krajčírov (alebo: nášho krajčíra), a aj toto bude v nedeľu. Ak to len bude možné, poďme na toto. A napíšte mi, na čom ste sa dohodli. Očakávajúc Vaše vzácne riadky, zostávam s túžiacim srdcom v diaľke. Ferenc Holes.

V rámčeku na známku: Bozkávam tie malé ústa.

Otvorené písmo: Sľubnej slečne Jolánke Tóthovej, do vlastných rúk, Jász-Árokszállás, Alszög.

## Stamp-box message (2026-11-03)

Audit on 2026-11-03 (Claude Opus 5.5), after the register team asked that Jolánka cards with writing under the stamp be typed MASC + Steganography. Crops: `work/stamp-2026-11-03/box_2x.png` and `box_green.png` (hires address scan, stamp box only).

State of the box: no stamp is on the card now. The box shows the printed dashed frame and a printed blue circular emblem; the posting cancel (912 JAN 17) is struck at the left edge of the box, where it would have tied a stamp, so the stamp was most probably stuck here and later lifted. The writing sits inside the box and over the printed emblem, in the same red ink and in the cipher signs; there is no plain writing in the box.

The message was already read in full on 2026-11-01 and is in the ledger and in `work/decode.py` output (stamp rows S1–S4). I re-read it by eye on the new crops and it agrees sign for sign:

- literal: `csoko / lom / akis / szajat`
- Hungarian (normalized): Csókolom a kis szájat.
- English: I kiss the little mouth.
- Slovak: Bozkávam tie malé ústa.

Unread: nothing. The only soft point is the one already listed in Uncertainties item 10: the last sign of *csoko* is a heavily inked loop, read as o. The script was not changed.

## Uncertainties

1. **Rows 14–15 *ravoban* = *[a] távolban*: word sense, not pixels.** The signs are written r a v o, b a n. The first sign has the F shape, with a short middle arm and a smudged lower stem; I do not read it as a gamma, so the written letter stays r. *távolban* needs r for t, which this writer also does in row 11 *állapodor*, and which the family shows elsewhere (HCP1243 `alí{t|r}ja`). It also needs an l. A small low arc stands right of the o at the row end. It is about a sixth of the width of this card's l, so I do not count it as a written l. It may be a cramped l, a row-end mark or a stray stroke, and no other row end on this card has such a mark. The l is therefore taken as omitted, like other letters on this card. A tick above and right of the F sits over the following a, as the tick over the first a of row 11: it supports long á, but it would fit *rá-* as well, so it says nothing about r against t. For the reading: *a távolból* is the stock phrase of this correspondence (HCP1243, 1244, 1261, 1271, 1276), and *a távolban* gives a natural close. No other Hungarian word was found; I had rejected rabja, imádója, reményben and Rákospalota. The struck sign before it (two bars crossed by diagonals, a by shape) is taken as the article *a*.
2. **Row 7 *meghívój[a]*.** *meg hi* is plain, then v o j. The j gives the possessive *meghívója* with a dropped final vowel, like the other omissions on this card. The older alternative *meghívott* ("invited") would need a j for t and is weaker.
3. **Row 6 *szabók* or *szabónk*.** The sign after b is a loop overlaid with heavy strokes, ending in an arched tail that runs into a pink blot (`review/work/crops/x_row6end.png`). The heavy strokes might be the two strokes of a joined n, as in the HCP1285 key table, or a long o tail reworked; no n can be separated from them. *a szabók meghívója* ("the tailors' invitation") and *a szabónk meghívója* ("our tailor's invitation") both parse. I print *szabók* first because a tailors' event in an association fits the winter season, and *szabónk* stands as the equal alternative. The ledger keeps one token, literal `o(n?)`. The sense of the clause, an invitation and a Sunday event, holds under both, and the word itself is word sense.
4. **Row 8 struck sign.** It has three tiers: a separate arched top bar over two bars crossed by diagonals (`review/work/crops/x_struck8.png`). That is e-shaped, giving *ez is* ("this too"), which goes well with *ebbe menjünk*. If the arch is not part of the sign, it is an overwritten a, giving *az is* ("that too"). The meaning hardly differs. The row 14 struck sign really has two bars, so the two struck signs are not the same.
5. **Row 9 *lehe ebbe*.** The word is written *lehe*, then e, b, b, e. The top bar of the e is under a blot. The t of *lehet* is taken as omitted by the writer. It could lie under the blot, though the visible stroke is a bar. Either way *hacsak lehet* is the only sense.
6. **Row 10 *as* for *és*.** Two bars, unusually far apart, with no middle bar visible. *És* is word sense alone: the family has no other reading for *asirjameg*.
7. **Row 11 *alapodor*.** The last sign is a clear F, so it is r written for t. *állapodott meg* (with *meg* from row 12) rests on word sense; it also needs the second l and second t restored. The third person is the polite "you" of this card's formal register.
8. **Row 11 p and row 8/9 h.** The tick position separates h (high: *hogy*, *hacsak*, *lehe*) from p (low: *nap*, *állapodott*, *epedő*). In row 11 the p also has a red dot above the tick, taken as a stray accent.
9. **Row 15 *Holes*.** The tick of the first sign is rather low on this card, so the shape alone leans to p. H comes from sister cards: HCP1303 has *Holes* in plain writing (capital uncertain), HCP1309 *holesferi*, HCP1278 Holes F. *Ferenc* ends in a heavily overwritten sign, c or k.
10. **Undotted i.** The crossed curve appears without a dot in *tiszta, soraim, írja, miben, sorait, szívvel*; word sense supports i every time. In the stamp box the last sign of *csoko* is a heavily inked loop, read as o for *csókolom*.
11. **Spelling.** *sziveből* is taken as *szívemből*: the m is missing. *legjob* for *legjobb*, *szivel* for *szívvel*, and *olvastán* are written as shown. Accents are mostly not visible and are supplied.
12. **Plain text.** *Szépreményű* above the address and the bottom line *al szög* (read as Alszög, a part of the village) are longhand. The town line is overwritten or struck through in part. These are not part of the decipherment. The date comes from the postmark 912 JAN 17 and the portal file name.

## Why I believe it is correct

- The family key, unchanged, gives Hungarian across all 15 rows and the stamp box. No value had to be invented.
- The opening is the formula of sister cards (*legjobb kedvében találja soraim*), as is the close (*Becses sorait várva maradok*, *epedő szívvel*, HCP1301, HCP1285).
- The plain words *meg hi* join the cipher in mid-word, and the plain *Szépreményű* matches HCP1212's address.
- Details fit the correspondence: *egylet* and *vasárnap* recur on the sister cards, and Holes Ferenc is the known sender.
- The writer's own errors are few and of known kinds; two of the a-for-e errors claimed in round 1 were my misreadings and are gone.
- Repeats agree: *hogy* ×2, *meg* ×2, *kedv-* ×2, *sorai-* ×2, *v-a-r* in *vasárnap* and *várva*.

## Response to review 1

The review verdict was REVISE. I checked each finding on the reviewer's crops and on `work/hires/`. The reading is not substantially changed: one word is resolved and small details are corrected. `python3 -I ciphers/hcp-1268/work/decode.py` was re-run after the changes; all four hashes pass and the output matches the literal block above (236 tokens: one fewer than round 1, since o + n in row 6 is now one uncertain token).

1. **távolban: adopted, with two corrections to the argument.** Adopted as `{r=t}ávo[l]ban`, labelled as word sense, and "not understood" is dropped throughout. The tick does not help r against t: it marks long á and would fit *rá-* too. The small arc is not a good l. In `r14b.png` it is about 50 px wide and the row 14 l about 300 px, so I treat the l as omitted, and leave the arc unexplained. Uncertainty 1 states this.
2. **Rows 4 and 11, three bars: fixed.** `z_r4e.png` and `z_r11a.png` show three bars. These were my misreadings. The literal text is now *kedvében*, *miben*; no restoration in *miben*. Row 10 *as* stays, and uncertainty 6 now covers only that.
3. **Row 8 struck sign: fixed.** `x_struck8.png` shows the arched top tier. Ledger token `strk3`, literal `{e|a}`, normalized *ez is*, with *az is* reported. The row 14 sign is a separate token, `strk2`.
4. **Rows 6–7: fixed.** Normalized to *meghívój[a]*, so the clause parses, and the translations render it. *szabók* and *szabónk* are given as equals. I keep *szabónk* in play more firmly than the reviewer: the heavy strokes in `x_row6end.png` may be the strokes of a joined n, so the pixels do not exclude it.
5. **Title: fixed.** 17 January 1912 is a Wednesday, confirmed with Python; the title and text now say it is the posting date, and that the Sunday is 21 January at the earliest.
6. **`álapodor`: fixed.** Now `ál[l]apodo{r=t}[t] meg`, with the source spelling and *meg* from row 12 stated in uncertainty 7. "Or an error of mine" is removed.
7. **ő: fixed.** Rows 3 and 14 have two ticks (`r03a.png`, `r14a.png`). Token `loop2` decodes to ő, so the literal has *vebőlhogy*, *dőszivel*.
8. **Command: fixed.** The ledger now names signs by shape and `decode.py` applies the key table, so a key change alters the output. The reviewer's `my_decode.py` compared with the round 1 ledger format and will no longer diff cleanly against this one.
