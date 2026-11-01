# HCP 1267 (cpc_1913-07-13_HU__HU_Jasz Arokszalas_jolanka-39): Feri to Jolánka Tóth, a new job as a railway brakeman

Human solver: Tomáš Pavuk

**Status: deciphered in full, apart from one un-understood lone word (row 15) and one word cut by a tear (row S2). Independent review 1 verdict REVISE; all seven findings addressed, one hour in the text changed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1267 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1267), portal name cpc_1913-07-13_HU__HU_Jasz Arokszalas_jolanka-39, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language unknown, sender unknown, recipient Tóth Jolánka, with no transcription or solution attached. The date 1913-07-13 comes from the portal's file name; on the postmarks only "21" can be read.

The picture side carries a printed caption, *Szerelem törvénye 2. §: Soha soha, el ne hagyj!* ("Law of love, § 2: never, never leave me!"), and no cipher text. The message is on the address side, in green ink: 24 rows on the left half, three long rows along the bottom edge, and eight short rows under the stamp, where only an offset of the writing remains and the paper is torn. The address is in clear: *Tóth Jolánka úrhölgynek, Jász Árokszállás*. A clear sender's line, roughly *Vörösmarti u. 9?* and *Szépremény(?)*, stands under the postmarks and is not part of the message. The last row gives the writer's address in Latin script: *Holecz Ferencz M.A.V. fekezo Rakos Palota*, a brakeman of the Hungarian State Railways at Rákospalota near Budapest.

The card belongs to the family of cipher postcards from Feri to Jolánka Tóth. Their shared key was established on the finished cards HCP 1216, 1212, 1213, 1217, 1218, 1243 and 1301. This card was read with that **known, transferred key**; it is not a new key recovery. No published solution of this card was found or used, and the HistoCrypt paper was not read for it.

![Address side, with all the cipher text (source/address-large.jpg)](../source/address-large.jpg)

![Picture side with the printed caption (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is **manual**: every sign was read from enlarged crops of the un-converted scan, and recorded one token per written sign in a ledger, with 27 main rows and 8 stamp rows. Red-channel crops made the portal's watermark stamp pale, so that the bottom rows could be read through it. A script checks the hashes of the scans and decodes the ledger (`python3 -I ciphers/hcp-1267/work/decode.py`). Figures and the signature line are in clear inside the enciphered text, and the clear figures sit in sentences that need them.

Word division, accents and bracketed letters in the normalized text are editorial. The writer's spelling is semi-phonetic: doubled consonants are mostly written single, and d is dropped in *monta*.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs (register type MASC). The sign names are conventional labels for handwritten shapes.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S | k | F-like | r |
| six | b | wave | l | right bowl or flagged hook | s |
| left bowl (only in `cs`, `cz`) | c | three short strokes | m | gamma/corner | t |
| short stroke + long stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | long stroke + short tick; p also short + long | h / p | crossed curve, usually dotted | i |
| open hook with descender | g | inverted T | j | crossed diagonal with tail | z |
| low looped descender | y | opposed bowls | cs | | |

The writer spells gy and ny with two signs (g+y, n+y). Accent and dot marks stand over the base sign. The figures `½3`, `10`, `2 kor`, `10 K.m. utan 6 f. es`, `8 fil`, the numeral 2 before *levelel* and the signature line are in clear.

## Plaintext

```
01 szeretetédesjolánkámmostmar        15 ticsakaztsajnalomhogyk?e?l
02 nyugodtabbairhatommertvarom        16 elnemkezdtemelöbbfizetés
03 hogyhovaküldönekésénelhoz          17 2 kor . nahontaakarkelutazni
04 tammagammalatentatéstolathogy      18 akarnemésazonkivülminden
05 irhasakegyrendeslahotmert          19 10 K.m. utan 6 f. es mikorszol
06 maskéhnemnagyonérekramint          20 galatbava[g]yokmiorara 8 fil
07 irtam ½ 3 korfeküdtemleés 10       21 mostfélbekeletszakitaniaz
08 rerendezönkeletlenemazér           22 irastmertelkeletmennem
09 irtamojanoszevisza . köva          23 hestreakeletih[a]jaudvara 2 levelel
10 nomhogyjoidölegyenhogy             24 viszafelébementemsandorhozaz?t
11 jolmulathasonakmegénisleg          25 montahogyjonézekkihogyvettesemlemagam . kah?tamtothilon
12 jobbszeretnémhamindigjoidö         26 k?atolégylahot?haidejibemegkahjaadjatiszteletemetilon
13 volnamertn?emkelemesroz            27 k?anak , czim Holecz Ferencz M.A.V. fekezo Rakos Palota
14 idöbeutazniamiamunkatile
Stamp: i?stenvele | édese{tear} | bold[o]g | viszont | latasra | csoko[l]ja | imadoja | feri
```

### Hungarian (normalized)

Szeretet[t] édes Jolánkám! Most már nyugodtabba[n] írhatom, mert várom, hogy hova küldenek, és én elhoztam magammal a tintát és tol[l]at, hogy írhassak egy rendes lapot, mert másképp nem nagyon érek rá. Mint írtam, ½3-kor feküdtem le és 10-re Rendezőn kel[l]et[t] len[n]em, azér[t] írtam olyan összevissza. Kívánom, hogy jó idő legyen, hogy jól mulathassanak; még én is legjobb[an] szeretném, ha mindig jó idő volna, mert nem kel[l]emes rossz időbe[n] utazni. Ami a munkát il[l]eti, csak azt sajnálom, hogy [kel] el nem kezdtem előbb. Fizetés 2 kor. naponta, akár kel[l] utazni, akár nem, és azonkívül minden 10 Km. után 6 f., és mikor szolgálatba[n] vagyok, mi[nden] órára 8 fil. Most félbe kel[l]et[t] szakítani az írást, mert el kel[l]et[t] mennem Pestre, a Keleti pályaudvarra, 2 levél[l]el. Visszafelé bementem Sándorhoz, azt mon[d]ta, hogy jó[l] nézek ki, hogy vettessem le magam. Kaptam Tóth Ilonkától egy lapot; ha idejébe[n] megkapja, adja át tiszteletemet Ilonkának. Czím: Holecz Ferencz M.Á.V. fékező, Rákos Palota.

Under the stamp: Isten vele, édese[...]! Boldog viszontlátásra. Csókolja imádója, Feri.

### English

My beloved sweet Jolánka! Now I can write more calmly, because I am waiting to hear where they will send me, and I have brought ink and pen with me so that I can write a proper card, since otherwise I do not have much time. As I wrote, I went to bed at half past two and had to be at Rendező by 10, that is why I wrote so haphazardly. I wish you good weather, so that you all enjoy yourselves; I too would like it best if the weather were always good, because it is not pleasant to travel in bad weather. As for the work, I am only sorry that I did not start it earlier. The pay is 2 korona a day, whether I have to travel or not, and on top of that 6 fillér for every 10 km, and when I am on duty 8 fillér for every hour. I just had to break off writing, because I had to go to Pest, to the Keleti station, with 2 letters. On the way back I went in to see Sándor; he said that I look well and should have my photograph taken. I received a card from Ilonka Tóth; if you get this in time, please give my respects to Ilonka. Address: Ferencz Holecz, M.Á.V. [Hungarian State Railways] brakeman, Rákospalota.

Under the stamp: God be with you, my darling(?). Until a happy reunion. Your admirer Feri kisses you.

### Slovak

Moja milovaná, sladká Jolánka! Teraz už môžem písať pokojnejšie, lebo čakám, kam ma pošlú, a priniesol som si so sebou atrament a pero, aby som mohol napísať poriadny lístok, lebo inak nemám veľa času. Ako som písal, ľahol som si o pol tretej a do 10 som musel byť na Rendezi, preto som písal tak zmätene. Želám, aby bolo pekné počasie, aby ste sa dobre zabávali; aj ja by som bol najradšej, keby bolo stále pekne, lebo v zlom počasí nie je príjemné cestovať. Čo sa týka práce, ľutujem len, že som ju nezačal skôr. Plat je 2 koruny denne, či už treba cestovať, alebo nie, a okrem toho po každých 10 km 6 fillérov, a keď som v službe, 8 fillérov za každú hodinu. Práve som musel prerušiť písanie, lebo som musel ísť do Pešti, na stanicu Keleti, s 2 listami. Cestou späť som sa zastavil u Šándora, povedal, že vyzerám dobre, nech sa dám odfotiť. Dostal som lístok od Ilonky Tóthovej; ak to dostanete včas, odovzdajte, prosím, moju úctu Ilonke. Adresa: Ferencz Holecz, brzdár M.Á.V. [Maďarské štátne železnice], Rákospalota.

Pod známkou: S Bohom, drahá(?). Šťastné videnie. Bozkáva Vás Váš ctiteľ Feri.

## Uncertainties

Every `?` and `[ ]` in the ledger is listed here. Everything else is a clear sign.

1. **Row 15, `k?e?l` at the end of the row:** S, then a faint sign that looks more like a Latin e than three bars, then a wave. Row 16 goes straight on with *el nem kezdtem*. I do not understand this word in the sentence and treat it as a false start (*kel* written, then dropped), bracketed in the normalization. It is the only un-understood word on the card, and the clause reads without it.
2. **Row 20, `mi órára`:** the signs are clearly m i o r a r a (a dot beside the r is a pen mark). Normalized *mi[nden] órára* ("every hour") by parallel with *minden 10 Km. után* in row 18; the writer's contraction, not a hidden sign.
3. **Row 13, `n?em`:** the first sign has the tall + short form of h/p, not two even strokes. *nem* from word sense.
4. **Row 25, `kah?tam`:** the sign is two near-even strokes, like n, read as the h/p sign from word sense (*kaptam*; *kantam* is no word; with item 8 it is the short + long p form at its least distinct). The following three strokes (m) lie under the portal's stamp ring but are visible in the red-channel crop.
5. **Row 24, `az?t`:** the sign before t is a tilted cross between z and f; *azt* from word sense.
6. **Row 26, `lahot?`:** the last sign looks like r/t with a dot beneath it; *lapot* from word sense.
7. **Rows 26 and 27, first sign `k?`:** the row-initial sign has a closed loop (δ-like; g-like in row 27). k from word sense (*Ilon-kától*, *Ilon-kának*). In rows 25/26 and 26/27 the name is split over the row end.
8. **h/p sign:** as in the family it is near-homographic. Its usual shape is long stroke + short tick (*Pestre, lapot*), but in *naponta* (row 17), *pályaudvar* (row 23), *megkapja* (row 26) and probably *kaptam* (row 25) p is short stroke + long stroke, the same shape as d here, so p calls can collide with d as well. p is chosen by word sense in *lapot, másképp, Pestre, pályaudvar, naponta, megkapja, kaptam*; h in *hogy, hova, írhatom, írhassak, mulathassanak, hoz*.
9. **d vs n, and d vs p:** d (short stroke + long stroke) is close to n, and has the same shape as the second p form (item 8), at this pen size. d chosen by word sense in *nyugodtabba, idő, kezdtem, feküdtem, küldenek, rendes, Rendezőn, mindig, minden, Sándor, adja, idejébe*. *monta* (row 25) shows two even strokes, so it is transcribed n and normalized *mon[d]ta*.
10. **Row 20 `[g]`** in *vagyok*: covered by a solid ink blot, restored; only g fits (it is the first half of gy). **Row 23 `[a]`** in *pályaudvara*: the top bar shows above a blot, a restored from the word. Row 6, the n of *nem* is partly blotted but its strokes are visible.
11. **Stamp rows.** The signs here are an offset of the text under a stamp now removed, and the paper is torn. Row S1 `i?`: the first sign looks like the following s, without a dot; *Isten vele* from word sense. Row S2: *édese* is clear, and then the tear hides the end; a bar sign is visible to the right of the tear. *édesem* is the natural reading, but it is **not** restored and the last word stays incomplete. Row S3: the o of *boldog* lies in the tear, restored. Row S6: the l of *csókolja* lies in a faded area, restored (*csókolja* is confirmed by the visible j a; its l is only a faint tail).
12. **Row 23 "2":** written like the clear 2 of row 17 and read as the numeral (*2 levéllel*, "with 2 letters"). The same sign might in principle be something else, but no other family letter has this form.
13. **Writer's spellings kept in the literal text:** *szeretet, nyugodtabba, küldönek, tentát, tolat, irhasak, lahot* (= *lapot*, as in row 26), *máskép, kelet, lenem, azér, ojan, oszevisza, kövanom, roz, ile/ti, jo nézek, szolgalatba, idejibe, levelel, viszafelé, monta, vettesem*. *tenta* for *tinta* and *kövanom* for *kívánom* are the writer's forms; *vettessem le* = *vétessem le*. Accent marks are recorded only where seen and are otherwise supplied in the normalization.
14. **Not enciphered and not fully read:** the clear sender's address above Jolánka's name, reading roughly *Vörösmarti u. 9?* / *Szépremény(?)*, is under the postmarks; it is not part of the message. Address: *Tóth Jolánka úrhölgynek, Jász Árokszállás*. Picture side: printed *Szerelem törvénye 2. §: Soha soha, el ne hagyj!* The portal's file name carries the date 1913-07-13; I could not read a date on the postmarks (only "21" is clear), so the date is the portal's.
15. Rendező is taken as the Rákosrendező railway yard in Budapest, from context; the card itself says only *Rendezőn*.
16. **Row 7, `és 10`:** after é there is one hook, then clear `1 0`, and nothing else. The hook has the flagged form of the s sign in rows 1, 9 and 12, so I read *és 10-re* ("and by 10"), which uses every mark and drops no letter. The alternative is *é[s] 7.10-re*: the hook is a figure 7 and the writer dropped s. There is no other 7 on the card to compare, so shape alone cannot exclude it. Either way the sentence reads; only the hour differs.
17. **Row 25, small m:** the m of *vettesem* is written small below the line between e and l, an insertion by the writer. It is in reading order in the ledger.

## Why the reading is correct

The unchanged family key gives running Hungarian of the period over all 27 rows, with one un-understood word. The content is specific and fits the clear text: a M.Á.V. brakeman writes of the Rendező yard, the Keleti station, travel, duty and pay by day, by distance and by hour. The enciphered *Feri* matches the clear *Ferencz*, and Sándor also appears on HCP 1216 and 1217. Repeated words decode the same way each time. Reviewer's note: the neighbouring card HCP 1266 (brakeman exam, move to Rákospalota, address to follow) fits this one independently.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-ran the command, decoded the ledger with a key typed separately from the HCP 1216 table (736 enciphered signs, none unmapped, same letters), and read all the rows sign by sign from its own crops. Its verdict was REVISE, with seven findings:

- **Row 7 (major):** the solver had read "7.10", using one hook both as the s of *és* and as the figure 7. The scan has one hook only. The text now reads *és 10-re* ("and by 10"), and the alternative *é[s] 7.10-re* is disclosed. This is the only change to the meaning.
- **Rows 5, 9 and 14 (minor):** three sign errors in the ledger corrected, giving literal `lahot`, `visza` and `idöbe`. A false remark about the writer's spelling was removed. The normalized words did not change.
- **p shape (minor):** p has a second form, short + long stroke, the same shape as d. The key table and uncertainties now say so. No word changed.
- **Row 25 (minor):** the small m written below the line is now noted.
- **Claim wording (minor):** the count for *kelet* and the statement about the ledger were corrected.

The reviewer could not verify whether the row 7 hook is s or 7 beyond its shape, nor the postmark date. Rendező as Rákosrendező rests on context only.
