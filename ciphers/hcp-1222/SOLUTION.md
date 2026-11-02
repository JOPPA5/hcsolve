# HCP1222 — Feri to Jolánka Tóth: arrived at Gyöngyös, his father says he must work

**Status: complete reading, review 1 (REVISE) addressed; see the response at the end.** Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. Portal status Not solved, no attached transcription or solution; no published solution of this card was found or used. The key comes from the finished family cards (HCP1216, 1212, with 1213, 1217, 1218, 1243, 1301), whose solvers are credited in their own directories.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the Jolánka/Feri postcard family). The sign-to-letter key is unchanged; the table describes the forms of this hand on this card. Word spaces are only partly kept; accents are marks over the signs. One plain digit (7) stands in clear in row 5.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / 5-shape | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| short stroke + long stroke (HCP1216: "long stroke + short tick", same sign; here the short stroke is on the left) | d | two short strokes | n | plain heavy cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short tick at right | h / p (near-homograph) | low descender | y |
| open loop with descender | g | dotted crossed curve | i | tall crossed sign with long arm | z |
| inverted T | j | g + descender | gy | opposed bowls | cs |

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1222/work/decode.py
```

It checks the SHA-256 of both source scans and both hi-res originals, decodes the sign ledger `work/ledger.txt` (one token per written sign, 20 main rows plus 6 rows in the stamp corner) and prints the normalized text `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of `work/hires/*adr.jpg`, not OCR.

## Literal decipherment (as printed by the command)

```
01 szerétetédesjolan             11 esmérkiadtaédeapam
02 kámtudatomhogyszeren          12 ajelszothogyhol
03 csesenmegerkeztembár          13 goz{a|e}kmernemadeni
04 lekéstemavonatrol             14 {d?}emostnemíroktöb
05 escsak7oraraértemgyön         15 betmajdestéraböve
06 gyösre.edesemmegnem           16 benistenveleédesem
07 tudommijansorsvá              17 vigyazonegésségére
08 rámmégcsakhelutan             18 adjaatiszteletemkedves
09 nezekmunka.utanota            19 mamajanakestestvé{t>r}einek
10 honisvanmunka                 20 tiszteltetemamanczikatis
stamp corner: csoko / lom / szam / talan / szo{t>r} / feri
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Tudatom, hogy szerencsésen megérkeztem, bár lekéstem a vonatról, és csak 7 órára értem Gyöngyösre. Édesem, még nem tudom, milyen sors vár rám. Még csak hely után nézek, munka után; otthon is van munka. És mér? Kiadta éde[s]apám a jelszót, hogy dolgozzak, mer[t] nem ad enni. De most nem írok többet, majd estére bővebben. Isten vele, édesem, vigyázzon egészségére. Adja át tiszteletem kedves mamájának és testvéreinek. Tiszteltetem a Manczikát is.

Stamp corner: Csókolom számtalanszor. Feri

## English

My beloved sweet Jolánka! I let you know that I arrived safely, although I missed the train and only reached Gyöngyös at 7 o'clock. My darling, I do not yet know what fate awaits me. For now I am only looking for a place, for work; there is work at home too. And why? My dear father has given out the word that I should work, for he will not feed me. But I will not write more now; by this evening [I will write] at more length. Farewell, my darling, take care of your health. Give my respects to your dear mother and your brothers and sisters. My regards to Manczika too.
In the stamp corner: I kiss you countless times. Feri

## Slovak

Moja milovaná, sladká Jolánka! Oznamujem Vám, že som šťastne dorazil, hoci som zmeškal vlak a do Gyöngyösa som sa dostal až o 7. hodine. Drahá moja, ešte neviem, aký osud ma čaká. Zatiaľ len hľadám miesto, hľadám prácu; aj doma je práca. A prečo? Môj drahý otec vydal heslo, aby som pracoval, lebo mi nedá jesť. Ale teraz už viac nepíšem, do večera napíšem podrobnejšie. S Bohom, drahá, dávajte si pozor na zdravie. Odovzdajte moju úctu Vašej milej mamičke a súrodencom. Pozdravujem aj Manciku.
V rohu pod známkou: Bozkávam Vás nespočetnekrát. Feri

## Uncertainties

The first ledger dropped four written signs (rows 5, 6, 11, 18; see the response to review 1). All 20 row ends and the corner were then rechecked on new enlargements (`work/crops/ends1.png`, `ends2.png`, `ends3.png`, `corner.png`) and no further drops were found. Letters are read from the pixels; the calls listed below rest on word sense. The writer drops doubled and other letters; signs are transcribed as written, and the normalization is editorial.

Calls that rest on word sense:

1. **Row 13, the sign in `goz?k`**: it is blotted. An arc above the blot and traces below show a bar sign, not a loop, so it is a or e and o is unlikely; the count of bars cannot be fixed. Normalized *dolgozzak* (a, writer's single z). *Dolgozok* or *dolgozék* would keep the sense.
2. **Rows 12/13 `hol|gozak`**: the first sign of the word is the tall-stroke + right-tick sign (h/p), not this hand's usual d (short left, long right). Read as d from context, *hogy dolgozzak* (same d/h slip as HCP1216 row 5). The three signs count once: there is no separate *hol*. Literal "hol gozak" is not Hungarian.
3. **Row 14, first sign**: two heavy slanted strokes joined by a bar, with a lead-in at left; no clean match with d. Read d from context: *De most nem írok*.
4. **Row 11 `édeapam`** = *éde[s]apám*: the first e carries a tick at upper right, placed like the acutes of rows 15 and 17, so é; it could also be a stray mark, which would not change the word. The s is not written. The p is the h/p near-homograph, read p by sense; *édesapám* has the same p on HCP1255 row 12. A heavy cross of row 10 falls over the top of this passage, but the signs are distinct. The clause rests on the idiom *kiadta a jelszót* (gave out the word). *Mér* = *miért* (colloquial); punctuating *És mér kiadta édesapám a jelszót...* or reading *mér* as *mert* would change only the link with the previous sentence.
5. **Row 8 `hel`** = *hely*: tall stroke + tick, then bars, then wave; the final y (or j) is missing. *hal*, *pél* give no sense with *után nézek*.
6. **Row 7 `sors`**: the last s is a small hooked form with the k shape of rows 5 and 8; *sors* by sense, the only sensible word.
7. **Rows 19 and c5 `{t>r}`**: *testvéreinek* and *számtalanszor* are written with a corner sign without a visible mid bar (literal t) where r is needed. Read r from sense; the mid bar may coincide with the top bar of the following e in row 19, but not in c5.
8. **Row 3 t of `megérkeztem`**: a heavy sign like E (stem, top bar and extra strokes), apparently an overwritten t. t by sense.
9. **Row 15 `estéra`** = *estére*: three bars with a tick above, then r, then two clear bars (the tick below them is the acute of the é in row 16). *Este rá* is excluded by the é and would leave *rá* with no meaning. The normalization changes one written sign, a for e, a slip by the writer. It is the one word of the card that is emended against a clear sign.
10. **Stamp corner `feri`**: the f is a blotted star shape, not a clean cross. The name is safe from the family.
11. **Rows 5 and 6, signs at the postmark**: row 5 n is two strokes of the script's ink, partly over the postmark rim, both visible. Row 6 m: the first stroke is clear, the next stands in the postmark block, a third can only be guessed. Both words are regular.

Writer's spellings normalized: *szerétet* → szeretett; *megnem* → még nem; *mijan* → milyen (as *ojan* for olyan on HCP1216); *ota|hon* → otthon; *többet* written *töb|bet*; *bőve|ben* → bővebben; *eni* → enni; *vigyazon* → vigyázzon; *egésségére* → egészségére; *mer* → mer[t]; `adjaatiszteletem` has one t where *át tiszteletem* needs two. Row 1 ends *Jolán*, row 2 begins *kám*. The dot marks over o are read as ö/ő per sense. Acute accents are often not visible and are supplied. The first sign of row 4 has a separate low tick, taken as part of l or as a stray mark; a similar tick stands to the lower right of the last i of row 13. The final m of rows 16 and 19's *mam-* may have an extra stroke; neither word is affected.

**Unenciphered parts.** The address reads, in plain hand, *Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás* (first word read from the cursive). Printed card text: "Printed in Germany". The left postmark shows a date block with 13 and JAN, and rim letters that look like the middle of Jászárokszállás (an inference from a few letters). The right postmark shows G on the rim and 13; this suits Gyöngyös but it is only an initial. The portal filename gives 1913-01. The day cannot be read. Nothing else on the address side or on the picture side carries writing. *Manczika* is not identified; no identification of Feri is claimed beyond the family.

## Why it is correct

- The key, transferred with no change of value, gives Hungarian for every sign of all 20 rows and the corner. No new sign value was needed; the 7 is a plain digit in a time expression that reads naturally.
- The text is coherent, idiomatic and ordinary: arrival report, a missed train, job hunting, a closing formula (*Isten vele*, *Csókolom számtalanszor*) matching the family. The word *Gyöngyös* came out of the signs without being sought. It fits the family context: HCP1303/1310 notes record Feri's Gyöngyös connection, and later cards speak of his Gyöngyös pay and a Gyöngyös postmark.
- Repeated words decode identically: *hogy* ×2, *munka* ×2, *után* ×2, *édesem* ×2, *tiszteletem/tiszteltetem*, *szer-*, *-tem*.

## Response to review 1

Verdict REVISE. All findings were rechecked on the enlargements and addressed. The ledger now has 381 written signs; the reviewer's independent decoder (`review/work/decode_review.py`) gives 390 letters on both sides and all 26 rows identical with accents ignored. `python3 -I ciphers/hcp-1222/work/decode.py` was re-run and passes its hash checks.

1. **Rows 12/13, `hol` counted twice: fixed.** Normalized *hogy dolgozzak*; English, Slovak and title corrected; uncertainty 2 now says the signs count once.
2. **Row 11, missing sign: fixed, and the clause is resolved.** I confirm the sign on the crop: three bars, lowest heavy, tick at upper right. Literal `kiadta` + `é` + `deapam` gives *kiadta éde[s]apám*, "my dear father gave out"; the s is dropped, as this writer drops letters. The "emphatic particle" gloss is withdrawn. The sense is as before, and there is no unresolved sign. The word occurs on HCP1255 row 12 (`edesapam`). The tick is not needed for the reading.
3. **Row 18 end: fixed.** Three bars after k and a right-bowl s beyond the divider are both visible; literal *kedves*. The old uncertainty 9 is deleted.
4. **Rows 5 and 6 ends: fixed.** n and m added to the ledger, as written *gyön|gyösre* and *megnem*; the claims of omission are withdrawn. Which strokes are obscured is stated in uncertainty 11.
5. **Claim "every letter read from the pixels": fixed.** Statement reworded, the drops recorded in NOTES.md, all row ends rechecked (`work/crops/ends1-3.png`); no further drops.
6. **Row 15 `rá`: fixed, differently from the old reading.** On a new 3.6× crop (`work/crops/r15e.png`) I agree the sign after r is two bars. But the e before r has an acute the ledger had missed, so the row is `estéra`, which rules out *este rá*. Normalized *estére* with a for e, listed as uncertainty 9 and translated consistently as "by this evening".
7. **Row 7 `sors`: agreed**, already disclosed; wording of item 6 aligned.
8. **Stamp-corner f: added** as uncertainty 10.
9. **Key description: fixed.** The table now states this hand's form of d and that the values are unchanged.
10. **Slovak: fixed**, *Pozdravujem aj Manciku*.
11. **Postmarks: added.** 13 and JAN confirmed on the left mark, G and 13 on the right one; stated as weak evidence, in "Unenciphered parts".

The reading is not substantially changed: the same message, four written signs restored, one acute added in each of rows 11 and 15, *hol* removed, *de apám* becoming *éde[s]apám*, and *este rá* becoming *estére*. Rows 11 and 15 go beyond what the reviewer proposed, so they are flagged here; they were not seen by a reviewer.
