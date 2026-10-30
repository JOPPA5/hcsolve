# HCP1300 — Feri to Jolánka Tóth: no leave before spring

**Status: complete reading, with the residual points listed below; review 1 verdict REVISE, findings addressed (see Response to review 1).** Solver: Claude Opus 5.5, 2026-10-30. There is no earlier work on this number. The portal shows status *Not solved* and attaches no transcription or solution; I transcribed the card myself (`work/ledger.txt`). The orchestrator's check of 2026-10-30 found no AI-register record. No published solution was seen; no wider literature search was made.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the Jolánka postcard family, same key as the finished cards HCP1216, 1212, 1213, 1217, 1218, 1243, 1301 (sign table in `ciphers/hcp-1216/SOLUTION.md`, reused unchanged, no new letter value invented). Main text is 27 rows, running as long rows under the address; a further 6 rows are in the stamp box, around and under the printed green triangle, ending in the signature.

Sign behaviour specific to this card:
- Tall stroke + tick on the **right** = h/p; tick on the **left** = d. Which of h/p is meant rests on word sense (`hedig` = pedig, `fenykehet` = fényképet, `hete` = hetek).
- The tilted cross is u (`tudatnom`), but is also the writer's f in `férfi` (row 16) and the signature `Feri` (B6); row 24 and row 25 f is the upright cross. In row 27 *az* the z is an upright cross, not the usual crossed diagonal (see point 7).
- e and a are three and two bars; the writer's bars are sometimes ambiguous. He writes a for e in `angem` (*engem*) and e for a at the end of `arre` (*arra*).
- He repeats material: `szeretetett` for *szeretett* (row 1), `lesszek` for *leszek* (row 15), `sza|momomra` for *számomra* (rows 13-14), `dokoksi` (box row 3).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1300/work/decode.py
```

It checks the SHA-256 of all four scans, decodes the 643-token ledger `work/ledger.txt` by the key, prints the literal rows, then the editorial `work/normalized.txt`. The ledger is a manual reading of the pixels, made with `work/crop.py`, `crop3.py` and, for the stamp box, `work/ink.py` (cancels the green ink so the pencil beneath shows; `work/crops/I1.png` to `I6.png`). It was not blind to sense: words were recognised while reading.

## Literal decipherment

```
01 szeretetettedesjolankam          15 enlesszekalegboldogabb
02 fojtatomsoraimsajnalat           16 ferfiavilagonbarmost
03 talkeltudatnomhogyen             17 isanakerzemmagamert
04 atavaszigegyaltalannem           18 bodogiazatudathogy
05 hetehazamertitojanvi             19 magaszeretkedvesem
06 lagvanhogysajattestvere          20 enmagatmindigjobban
07 lakodamerasemmehetha             21 szeretninemmegunni
08 zaazemberhedighigyje             22 tudomenaztcsakazert
09 eledesemnagyonszeret             23 irtamhogymajdegyma
10 nekmarbeszelnimagaval            24 sikferiszebjovovkecsegtettiesangemakkor{+}{s?}eh
11 edesemkedvesemenisarre           25 nelhagyenazegeszvilagelotismegmondomnom
12 keremajoistenhogy{#}maga         26 magavagysenkiafenykehetvaromsikertkivanok
13 szer{e?}{l?}{m?}{|}{e?}{m?}virgaiscsaksza  27 hozzaorulokhogyegessegesenisazvagyok
14 momomranyiljonakor               box: istenve / lemere / dokoksi / righui / madoja / feri
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Folytatom soraimat. Sajnálattal kell tudatnom, hogy én a tavaszig egyáltalán nem [me]hetek haza, mert itt olyan világ van, hogy saját testvére lakodalmára sem mehet haza az ember. Pedig higgye el, édesem, nagyon szeretnék már beszélni magával, édesem, kedvesem. Én is arra kérem a Jóistent, hogy maga, szerelmem virága, is csak számomra nyíljon, akkor én leszek a legboldogabb férfi a világon. Bár most is annak érzem magam, mert boldogít az a tudat, hogy maga szeret, kedvesem. Én magát mindig jobban szeretni, nem megunni tudom. Én azt csak azért írtam, hogy majd egy másik férfi szebb jövővel kecsegteti, és engem akkor szépen elhagy. Én az egész világ előtt is megmondom: nőm maga vagy senki. A fényképet várom, sikert kívánok hozzá. Örülök, hogy egészséges, én is az vagyok.

Isten vele, maradok sírig hű imádója, Feri.

## English

My beloved sweet Jolánka! I continue my lines. I regret to have to tell you that I cannot come home at all before the spring, because things here are such that a man may not go home even for his own sibling's wedding. And yet, believe me, my darling, I would so like to talk with you at last, my darling, my dear. I too pray to the good God that you, the flower of my love, may bloom for me alone; then I shall be the happiest man in the world. Though even now I feel I am, for the knowledge that you love me, my dear, makes me happy. I can only love you more and more, never tire of you. I only wrote that because some other man may one day tempt you with a finer future, and then you would simply leave me. I will say it before the whole world: my wife will be you or no one. I am waiting for the photograph, and wish you success with it. I am glad you are well; I am too.

God be with you, I remain your admirer, faithful unto the grave, Feri.

## Slovak

Moja milovaná, sladká Jolánka! Pokračujem vo svojich riadkoch. S ľútosťou Vám musím oznámiť, že do jari vôbec nemôžem prísť domov, lebo je tu taký svet, že človek nemôže ísť domov ani na svadbu vlastného súrodenca. A pritom mi verte, drahá, veľmi by som sa už chcel s Vami porozprávať, drahá moja, milá moja. Aj ja prosím dobrého Boha, aby ste Vy, kvet mojej lásky, rozkvitli len pre mňa; potom budem najšťastnejším mužom na svete. Hoci aj teraz sa tak cítim, lebo ma robí šťastným vedomie, že ma ľúbite, milá moja. Ja Vás viem len stále viac ľúbiť, nie sa Vás nabažiť. Napísal som to len preto, že Vás raz možno iný muž zláka krajšou budúcnosťou a potom ma pekne opustíte. Pred celým svetom poviem: mojou ženou budete Vy alebo nikto. Čakám na fotografiu a želám Vám k nej veľa úspechov. Teší ma, že ste zdravá, aj ja som. 

S Bohom, zostávam Váš do hrobu verný ctiteľ, Feri.

## Uncertainties

Signs read but changed by normalization are the writer's habits; signs not secure are numbered first.

1. **Row 24, `{+}{s?}`** (before `eh`, normalized *szépen*): two pencil signs among the portal seal's letters: a plain upright cross, then a sign with an upper arm, a lower bar and a curve at the right, probably a wide right bowl (s). Key values would give *f* + *s*, and the upright cross stands for z in row 27, so the order would be z + s, the reverse of *sz*. *szépen* is therefore **inferred from sense** (*szép* + `n` of row 25; the e of *-pen* is not written), and this word is the weakest point of the card. No other word was found. `work/resp_violet.py`, `work/crops2/r24_violet.png`.
2. **Row 12 `{#}`**: an overstruck sign after *hogy*, possibly a corrected j or e; treated as a false start with no value. The next word is `maga`: its vowel has two bars, crossed by the printed rule, with no third bar.
3. **Row 13 `szer…virga`**: the letters after *szer* are heavily overwritten, and *szerelmem* is **recognised, not read sign by sign**. I can see e, l, a three-stroke m, an extra heavy stroke, a boxed e and a thin tail; no distinct second m is seen, so *szerelmem* ("of my love") and *szerelem* ("of love") cannot be separated. The ledger marks these tokens uncertain. `v` is a heavy overwritten sign and the g a blot with a descender. *virága* lacks the second vowel. The combination with *nyíljon* (bloom) supports it.
4. **Rows 13–14 `sza|momomra`**: normalized *számomra*, assuming one repeated *mo* across the row break; the last sign of row 13 has two bars, so it is a, and no vowel exchange is needed. The strokes of the middle m are uneven; the reading *mondom* ("I say") would leave `sza` senseless, so this rests on sense.
5. **Row 25 end `megmondom nom`**: most of it lies under the portal seal; the signs are still traceable (`work/crops/u2.png`, `u3.png`, `u4.png`). `nom` runs down into the corner, its m as three stacked strokes. *nőm* ("my wife") is the sense reading. A short pencil tick stands at the upper left of the o: it may be the ő mark, or the tick of an h-type sign; the two dots of a normal ő are not seen.
6. **Row 5 `hete`**: normalized *[me]hetek*: the writer's me- and -k are absent, an editorial supply and not a reading of hidden signs. `hazamert` row-joins into *haza, mert*.
7. **Row 27 *az***: the a has its lower bar blotted, and the next sign is an upright cross, read z from sense (*én is az vagyok*).
8. **Box row 2 `lemere`**: the third stroke of the m falls on the blot at the triangle's apex; bars after it may be two or three, so *mara-* rests on sense with *dok*.
9. **Box row 3 `dokoksi`**: normalized *maradok sírig*. The extra `ok` (∂ + k-sign) has no place in the sentence and is dropped as dittography, like the repeat in point 4. The first sign's tick is on the left, hence d. The final `s` is preceded by the k-sign with a small loop at its foot, which I also take as part of `ok`.
10. **Box row 5 `madoja`**: the o is only a hook above the triangle's base line.
11. **Row 24 `sikferi`**: *másik férfi* with one f omitted, not the name Feri, by sense. `jovov` = *jövővel* with *-el* omitted, `kecsegtetti` = *kecsegteti*.
12. **Row 26 *sikert* and *kívánok***: the t and the i of *kívánok* are overlapped by the seal letters HIST/OF but visible in `work/crops/t3.png`.
13. Other writer spellings normalized: `fojtatom`, `ojan`, `it`, `kel`, `mondom` unchanged; `soraim` → *soraimat* (added suffix, the only change affecting grammar), `higyje` → *higgye* (g added, j dropped), `magamert` → *magam mert* (one m written for two), `szeretetett` → *szeretett*, `lesszek` → *leszek* (repeats, see the sign behaviour above); `lakodamera` → *lakodalmára* (l omitted), `bodogi` → *boldogít* (l, t omitted), `isanak` → *is annak*, `arre` → *arra*, `Jóisten` → *Jóistent* (t omitted), `szeb`, `angem` → *engem*, `elot` → *előtt*, `egesseges` → *egészséges*, `akor`, `nelhagyen` → *elhagy, én* (e of *-pen* and word breaks are editorial; in `hagyen` the row reads *hagy én*). Row 9 opens with a joined e + l sign (`el`), also used in row 25. Accents are mostly faint and are supplied.
14. The phrase *sikert kívánok hozzá* after the photograph is a plain reading, but what it refers to (a photo Jolánka is to have taken, or to send) is not stated.
15. Date: the card shows only a partial postmark (a day 26 is visible, and a figure 11 on the stamp cancel, month or hour not established); no year is claimed. Feri is taken from the signature; no identification with Feri of other cards is claimed, though the signature formula matches HCP1216 (*Sírig hű kedvese, Feri*) and more closely HCP1292 (*sírig hű imádója, Feri*).
16. **Address, not enciphered**: pencil, *Szépreményű / Tóth Jolánka / úrleánynak / Jász Árokszállás*. The first word runs into the cancel, and its last letters rest on the parallel in HCP1287. The picture side has only a printed title and verse (*Szeretni édes…*; *Nincs boldogság másban…*), no handwriting.

## Why it is correct

Every letter value comes from the existing family key; none was fitted here. Under that key the whole card gives connected Hungarian in the family's register: address, regret at no leave, wartime-like restriction, love declaration, sign-off, signature. The stamp box was unknown before `ink.py` revealed the pencil inside the triangle, and it then read at once as the formula *Isten vele … sírig hű imádója Feri*, known from HCP1216 and HCP1301. Long unforced stretches such as *legboldogabb férfi a világon*, *boldogít az a tudat, hogy maga szeret*, *fényképet várom* leave little room for chance.

## Response to review 1

Verdict REVISE. I rechecked each finding on the reviewer's crops and on my own colour crops of the hi-res scan. The normalized text and the translations did not change. `python3 -I ciphers/hcp-1300/work/decode.py` still runs: all four hashes OK, 643 ledger tokens.

1. **Row 1, fixed.** Signs in order: s, z, e, r, e, t, e, t, e, t, t, e, d, e, s (`work/crops2/r1.png`). The ledger now has `szeretetett`. This word had been read from expectation, and the repeat is now recorded. The normalization stays *Szeretett*.
2. **Row 15, fixed.** Two bowls stand before the z. Ledger: `lesszek`. Normalized *leszek* stands.
3. **Row 13 last sign, fixed.** Two bars, so a: `sza|momomra`. The *szemomra* note is withdrawn and point 4 and the sign-behaviour notes are corrected.
4. **Row 12, fixed.** Two bars: `maga`. Point 2 corrected.
5. **Row 24, partly disagreed; ledger fixed.** The reviewer is right that the hook on top is the s of *Tobias*, and that the seal's R is there. But more pencil exists than one cross. `work/resp_violet.py` maps blue excess over red and green, which separates violet pencil from olive seal ink. In `work/crops2/r24_violet.png` and `r24_colour.png`, a pencil stroke runs from upper left into the R, a pencil bar runs below it, and a pencil curve comes down at the right, with the seal's R showing faintly by comparison. So a second sign is present, and "one visible upright cross" understates the card. Its shape fits a wide right bowl (s), though the seal covers its middle. The ledger now has `{+} {s?}`. `zeh|n` is not adopted. *szépen* remains inferred from sense, with the order problem stated in point 1.
6. **Row 13 `szerelmem`, fixed.** Tokens are marked uncertain and both forms are given in point 3. The translation keeps "my love", the likelier sense.
7. **Normalizations, fixed.** All three added to point 13.
8. **Address, fixed.** Recorded in point 16, including the dependence on HCP1287 for the end of the first word. I also add the printed picture-side text.
9. **Row 25 tick, fixed.** Mentioned in point 5, with both explanations.

Also taken from the review: the parallel with HCP1292 and the figure 11 on the cancel (point 15). The token count rose from 638 to 643: row 1 two, row 15 one, row 13 one (the extra stroke), row 24 one.
