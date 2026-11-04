# HCP1230 — Feri to Jolánka Tóth: late home, fear of a mark on his record

**Status: complete reading, reviewed (REVIEWED1, verdict REVISE) and corrected.** Written 2026-11-02 by Claude Opus 5.5. No earlier work exists on this number. The portal shows status Not solved and attaches no transcription or solution, and no published solution of this card turned up. The sign classes were transferred from the finished Jolánka family cards (hcp-1216 and sisters; that key was reconstructed earlier by the OpenAI GPT solver and completed by Claude Opus 5.5).

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the "Jolánka" postcard family, register type MASC). Same key as hcp-1216:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | S-shaped section sign | k | F-like | r |
| six | b | wave | l | right bowl | s |
| long stroke + tick to its left | d | three short strokes | m | gamma/corner | t |
| three bars | e | two short strokes | n | plain cross | u |
| upright cross + | f | cursive loop | o | chevron | v |
| open loop with descender | g | crossed curve, normally dotted | i | y-loop | y |
| inverted T | j | opposed bowls | cs | crossed x with tail | z |
| long stroke + tick to its right | h | same stroke pair (near-homograph of d and h) | p | | |

The letter c is not used on this card. On this card gy is written as two signs, g + y. Marks over a sign give á/é/ö/ő/ü; most are faint and are supplied in normalization. The address side is in clear (pencil): Széprém[enyű] (under the postmark, wording as on hcp-1216) Tóth Jolánka úrleánynak, Jász Árokszállás. The picture side is printed: "Te vagy a csillagom." and a four-line verse; it holds no handwriting.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1230/work/decode.py
```

It checks the SHA-256 of all four image files, decodes the manual sign ledger `work/ledger.txt` (477 signs in 26 rows) with the key, and prints the literal rows and the normalized text `work/normalized.txt`. The ledger was read from the un-converted scan in `work/hires/`. Row 26 runs along the bottom edge to about two thirds of the card's width. `work/crop.py` makes grey enlargements. `work/violet.py` makes a blue-minus-green channel, which keeps the violet pencil and removes most of the black postmark; this was needed for rows 1 to 6 at the right.

## Literal decipherment (as printed by the command)

```
01 szereretedesjolán[k]ám        14 stiklimelsimuljtöb
02 bivanomhogyaljobegezeg        15 betnemcsinalokijes
03 bentalaljasoraimensze         16 mitmertnemabüntetés
04 rencsésenmegérkeztem          17 sanálomhanemaztaz
05 igazhogynemavalavo            18 ijesmitbejegyzies
06 nattalamelikkelszá            19 haelolepteteskorazt
07 mitotottammertazcsak          20 nézikvoltemarbüntet
08 egyorávalmintszamitot         21 veeshanyszorezront
09 tamesigycsakregelhet          22 jaazelőrhaladast
10 orakkorértemhaza              23 demostmastnemirok
11 személyvonattalde             24 mivelnagyonalmos
12 talannemleszbelő              25 dakistenveleedesem
13 lesemmibajcsakeza             26 maradoksirighukedvesefer
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb egészségben találja soraim. Én szerencsésen megérkeztem. Igaz, hogy nem avval a vonattal, amelyikkel számítottam, mert az csak egy órával [előbb/később], mint számítottam, és így csak reggel hét órakor értem haza személyvonattal. De talán nem lesz belőle semmi baj. Csak ez a stiklim elsimuljon, többet nem csinálok ilyesmit, mert nem a büntetést sajnálom, hanem azt, az ilyesmit bejegyzi, és ha előléptetéskor azt nézik, volt-e már büntetve, és hányszor, ez rontja az előrehaladást. De most mást nem írok, mivel nagyon álmos [va]gyok. Isten vele, édesem. Maradok sírig hű kedvese, Fer[i].

## English

My beloved sweet Jolánka! I wish that my lines find you in the best of health. I arrived safely. True, not by the train I had counted on, because that one was just an hour [earlier or later; the word is not written] than I had reckoned, and so I got home only at seven in the morning, by passenger train. But perhaps nothing bad will come of it. If only this prank of mine gets smoothed over, I will not do anything like it again, because it is not the punishment I regret but this: he enters such a thing in the record, and if at promotion time they look at whether one has already been punished, and how many times, that spoils one's advancement. But I write nothing else now, as I am very sleepy. God be with you, my sweet. I remain, faithful unto the grave, your sweetheart, Feri.

## Slovak

Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky našli v najlepšom zdraví. Šťastne som dorazil. Pravda, nie tým vlakom, s ktorým som počítal, lebo ten išiel len o hodinu [skôr alebo neskôr; slovo nie je napísané], než som počítal, a tak som domov prišiel až o siedmej ráno, osobným vlakom. Ale azda z toho nebude nijaká nepríjemnosť. Len nech sa mi tento kúsok urovná, viac už nič také neurobím, lebo neľutujem trest, ale to, že sa také niečo zapíše, a ak sa pri povyšovaní pozerajú na to, či už bol človek trestaný a koľkokrát, to kazí postup. Ale teraz už nič iné nepíšem, lebo som veľmi ospalý. S Bohom, drahá. Zostávam do hrobu Váš verný milý, Feri.

## Uncertainties

Every sign is transcribed as written, and the normalization is editorial. The record of marks in the ledger is selective: faint accents are not all transcribed.

Calls that rest on word sense, restorations and supplied text:

1. **Row 25 `dak` (the one word not fully explained).** The first sign is in a stain at the edge: a long rising stroke with a faint tick to its left, so d class; no second leg of a chevron v is visible. The next two signs are a and k. The sentence needs "I am" after *álmos*. I normalize *[va]gyok*, but that is an inference and the literal is *dak*. *álmosodok* ("I am getting sleepy") with a dropped o and a for o is an alternative with the same sense. Colloquial *vok* does not fit, because the second sign is a.
2. **Row 1 k of *Jolánkám* is a restoration.** The sign is under a heavy postmark blot; only traces of violet remain. Exactly one letter fits, and the name is in clear in the address.
3. **Row 26 final i of *Feri* is an editorial supply, not a restoration.** After F-e-r the paper is blank in both the grey and the violet crops, while the neighbouring faint signs stay legible. The card reads *Fer*, and he may simply have stopped there. The name Feri is the signature on hcp-1216.
4. **Row 2 first sign** is clearly the six b, so literal *bivanom*. It is normalized *kívánom*, the standard greeting formula, as a writer's slip. No Hungarian word fits *bívánom*.
5. **Row 19 p of *előléptetés*** has its tick to the left, the d shape on this card; the value p rests on the word only. The o of that word (blotted, overwritten) shows no visible double mark, and ő is supplied.
6. **Row 23 d of *de*** has its tick clearly to the right, the h shape on this card; the value d rests on word sense only (as on hcp-1216, row 5).
7. **Row 21 first sign** is a heavy chevron with extra strokes across it; v rests on word sense (*büntet|ve*).
8. **Row 2 g of *egezeg*** lies under the postmark, with a closed bowl nearer the six than this card's open g; g rests on word sense.
9. **Row 14** `elsimulj` is taken as *elsimuljon*, with -on not written. The dot on the i is tiny. The first reading without it, *elsom*, gives no word.
10. **Rows 15 and 18** `ijes mit` = *ilyesmit*: the writer's j for ly. The i sign has no visible dot in either row, but it has the straight crossing bar of i, as in *mit*, not the curled top of o.
11. **Row 8** `egy órával mint` has no comparative. I checked the junction of the crops and nothing is missing on the card: the writer left out a word. Which word is not established. *[később]* ("later") and *[előbb]* or *[korábban]* ("earlier", so he missed that train) both fit, and the second explains the missed train at least as well, so the text keeps both options. The verb (*ment*) is also unwritten.
12. **Row 17 á of *sajnálom*** is the least clean of the signs corrected in review: two heavy bars joined by a short connecting stroke, with the accent dot above. At low zoom the connector looks a little like e, but at 5x there is no third bar.
13. **Row 26** the sign read as s of *sirig* has a shape nearer to the k sign (two S forms in a row: *maradok | sirig*); s is by word sense. The two i in the word are loops crossed by a long bar.
14. **Row 4 first sign** sits at the card's edge and is read as r (*sze|rencsésen*).

Writer's spellings normalized, none in doubt. He mostly drops letters: `szereret` → szeretett (a second r sign where t belongs, and one t omitted; the sign has the middle bar of r and is transcribed as r); `aljob egezeg | ben` → a legjobb egészségben (leg-, b, s and sz dropped); `avalavo|nattal` → avval a vonattal; `amelikkel` → amelyikkel; `szá | mitotottam` (rows 6-7) → számítottam, with a repeated -to-; `regel` → reggel; `orakkor` → órakor; `büntetes` → büntetést (-t omitted); `sanálom` → sajnálom (j dropped); `bejegyzi` is kept, though *bejegyzik* ("they enter") is possible; `előrhaladast` → előrehaladást.

Word division is editorial. Where *személyvonattal* belongs (with *értem haza*, or as a fragment) does not change the sense.

Date and postmarks: the Budapest postmark visibly reads `913 DE`, which agrees with the December 1913 in the portal's file name. Its day digits could not be read, and neither could the second postmark at top left (`...16`).

## Why it is correct

- The key was transferred unchanged from the finished family, not fitted to this card, and it turns all 477 signs of 26 rows into Hungarian with 1 restoration; the only unexplained group is one three-letter word (item 1).
- The text is coherent and unforced over its whole length, and has a specific, unexpected story: a man, evidently a soldier or someone in a service with a disciplinary record, got back late, hopes the *stikli* blows over, and fears the entry more than the punishment because it counts at promotion. Words like *személyvonattal*, *előléptetéskor* and *előrehaladást* cannot arise by chance from a substitution.
- After the corrections of review 1 the writer's errors are almost all dropped letters, a simpler and more credible pattern than the swapped vowels of the first transcription.
- Repeated words decode the same at separate places: *hogy*, *nem*, *csak* (three times), *számítot-* (twice), *ijes mit* (twice), *büntet-* (twice).
- The formulas fit the family: greeting, formal Ön address (*találja*, *Isten vele*), and the close *sírig hű kedvese, Feri*, as on hcp-1216. No identification of this Feri is claimed beyond that shared close.

## Response to review 1

Verdict REVISE. I re-examined the reviewer's crops in `review/work/crops/` and agree with all 14 findings; none is disputed. The ledger, literal block, normalized text, translations, spelling list and uncertainties above are corrected, and the command was re-run: 4 of 4 hashes OK, 477 signs, literal rows identical to the block above.

1. Row 7 *mert az*: **fixed.** Crop `t02` shows two bars after `mert`. Normalized text and both translations now say "that one".
2. Row 3 *talalja*: **fixed.** Crop `r3tal` shows two bars. The "writer's spelling" entry is deleted.
3. Row 7 *mitotottam*: **fixed.** Crop `r7end`: the upper bar belongs to row 6 (its gap is about 220 px against 130 px between the real bars). "e for a" is deleted from the spelling list.
4. Row 8 *orával*: **fixed.** Crop `oravel` shows two bars. The spelling entry is deleted.
5. Row 15 opening six: **fixed.** Crop `r15L` shows the faded 6 in the same rubbed pencil as the e and t after it. The card has *töb|bet*, spelled correctly, and "b dropped" is deleted.
6. Row 21 *ront*: **fixed.** Crop `ront`: two strokes, then the t stem. The spelling entry is deleted.
7. Row 26 *sirig*: **fixed.** Crop `s26z`: the sign is a loop crossed by a bar, the same form as the second i. The bars above belong to row 25. The old uncertainty item is rewritten (now item 13).
8. Row 17 *sanálom*: **fixed.** Crop `r17`: two bars with a connector. Disclosed as the least clean of these (item 12). The pattern claim "drops, repeats and swaps letters" is withdrawn, and the spelling paragraph now says what remains.
9. d/h family: **fixed.** h and p added to the key table; row 23 *de* (item 6) and row 19 p (item 5) now say plainly what shape they have.
10. Row 21 v and row 2 g: **fixed.** Disclosed as items 7 and 8.
11. Row 8 supplied word: **fixed.** The text now carries *[előbb/később]*, and the translations do not commit to either (item 11).
12. Row 26 final [i]: **fixed, with one departure from the reviewer's count.** Crop `end26v` shows blank paper, so the supplied i is not a sign and I removed it from the ledger. The literal is now *fer*; *Fer[i]* appears only in the normalized text. That is why the count is 477 and not the reviewer's 478: +1 six in row 15, −1 supplied i.
13. Marks: **fixed in part.** Added to the ledger: row 16 last e acute and row 14 o diaeresis (two ticks; crop `t13`). The row 13 mark is not distinct enough in that crop to record, so the ledger header and the Uncertainties section now say the record of marks is selective.
14. Dating: **fixed.** The postmark `913 DE` is now used; its day digits remain unread.

The reading is not substantially changed: same key, same story, one word of the normalized text corrected (ez → az) and one supplied word left open. Per the reviewer's closing note, no DONE2 round is needed.

## Stamp-box check (2026-11-03)

Checked by Claude Opus 5.5 on the un-converted address scan in `work/hires/` (crops in `work/stamp-2026-11-03/`: `stamp_x2.png`, `tear_x4.png`, `tear_violet_x4.png`). The green 5-filler Turul stamp is **still in place**, top right, cancelled by the Budapest postmark. Its lower-left part is torn or abraded away, and the paper surface exposed there shows only postmark ink (the arc, `9`, `3`, part of a frame line) and a blue-green stain; no violet pencil and no cipher sign is visible in it, in the colour crop or the blue-minus-green channel. Whatever the sender may have written under the rest of the stamp cannot be seen on this scan. No hidden message is read or claimed. The cipher type therefore stays **MASC** (not "MASC + Steganography"); register-entry.txt and the report are unchanged.
