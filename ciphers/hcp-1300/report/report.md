# HCP 1300 (cpc_--26_HU__HU_Jasz Arokszalas_jolanka-91): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (27 main rows and 6 rows in the stamp box), with named weak points; independent review 1 verdict REVISE, findings addressed, sense of the text unchanged.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1300 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1300), portal name cpc_--26_HU__HU_Jasz Arokszalas_jolanka-91, part of Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. A check of the AI Decipherment Register on the same day found no record for this card.

The picture side is a hand-coloured photograph of a couple, with the printed title *Szeretni édes…* and a printed four-line verse beginning *Nincs boldogság másban*. It has no handwriting. The message is on the address side, in pencil, in invented signs: 27 rows, of which rows 1 to 23 fill the left half and rows 24 to 27 run the full width under the address, and 6 short rows in the stamp box, around and under a printed green triangle.

The address is plain pencil: *Szépreményű / Tóth Jolánka / úrleánynak / Jász Árokszállás* ("To the promising young lady Jolánka Tóth, Jászárokszállás"). The end of the first word runs into the cancel, and its reading rests on the same form on HCP 1287. The postmark shows a day 26. A figure 11 on the stamp cancel may be a month or an hour. No year is claimed.

![Address side with the cipher rows, the plain address, the stamp box and the HC Portal seal (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: printed title and verse, no handwriting (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The card belongs to the Jolánka postcard family, and the key was **transferred unchanged** from the finished cards in this repository (the fullest table is in HCP 1216; also HCP 1212, 1213, 1217, 1218, 1243, 1301). No letter value was fitted on this card, so this is a known-key reading, not a new key recovery.

The transcription is manual: Claude Opus 5.5 read every sign from enlarged crops of the un-converted scan and recorded one token per written sign in work/ledger.txt. The reading was not blind to sense. Inside the stamp box a tool (work/ink.py) cancels the green printed ink so that the pencil beneath shows. No published solution of this card was seen, and no wider literature search was made.

The result can be reproduced from the repository root with `python3 -I ciphers/hcp-1300/work/decode.py`, which checks the hashes of the four scans, decodes the 643-token ledger and prints the literal rows and the normalized text.

## Key

Monoalphabetic substitution of Hungarian, with signs named by shape:

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| long stroke + short tick | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

On this card the tall stroke with a tick on the right is h or p, chosen by word sense (`hedig` = *pedig*, `fenykehet` = *fényképet*); a tick on the left gives d. The tilted cross is u, but the writer also uses it for f in *férfi* (row 16) and in the signature. In row 27 *az* is written with an upright cross for z. A joined e + l sign occurs in rows 9 and 25.

## Plaintext

Literal letters as decoded. Braces mark signs not secure: `{#}` is a struck-out false start, `{|}` an extra stroke, `{+}` an upright cross of uncertain use.

```text
01 szeretetettedesjolankam
02 fojtatomsoraimsajnalat
03 talkeltudatnomhogyen
04 atavaszigegyaltalannem
05 hetehazamertitojanvi
06 lagvanhogysajattestvere
07 lakodamerasemmehetha
08 zaazemberhedighigyje
09 eledesemnagyonszeret
10 nekmarbeszelnimagaval
11 edesemkedvesemenisarre
12 keremajoistenhogy{#}maga
13 szer{e?}{l?}{m?}{|}{e?}{m?}virgaiscsaksza
14 momomranyiljonakor
15 enlesszekalegboldogabb
16 ferfiavilagonbarmost
17 isanakerzemmagamert
18 bodogiazatudathogy
19 magaszeretkedvesem
20 enmagatmindigjobban
21 szeretninemmegunni
22 tudomenaztcsakazert
23 irtamhogymajdegyma
24 sikferiszebjovovkecsegtettiesangemakkor{+}{s?}eh
25 nelhagyenazegeszvilagelotismegmondomnom
26 magavagysenkiafenykehetvaromsikertkivanok
27 hozzaorulokhogyegessegesenisazvagyok
B1 istenve
B2 lemere
B3 dokoksi
B4 righui
B5 madoja
B6 feri
```

### Hungarian (normalized)

Szeretett édes Jolánkám! Folytatom soraimat. Sajnálattal kell tudatnom, hogy én a tavaszig egyáltalán nem [me]hetek haza, mert itt olyan világ van, hogy saját testvére lakodalmára sem mehet haza az ember. Pedig higgye el, édesem, nagyon szeretnék már beszélni magával, édesem, kedvesem. Én is arra kérem a Jóistent, hogy maga, szerelmem virága, is csak számomra nyíljon, akkor én leszek a legboldogabb férfi a világon. Bár most is annak érzem magam, mert boldogít az a tudat, hogy maga szeret, kedvesem. Én magát mindig jobban szeretni, nem megunni tudom. Én azt csak azért írtam, hogy majd egy másik férfi szebb jövővel kecsegteti, és engem akkor szépen elhagy. Én az egész világ előtt is megmondom: nőm maga vagy senki. A fényképet várom, sikert kívánok hozzá. Örülök, hogy egészséges, én is az vagyok.

Isten vele, maradok sírig hű imádója, Feri.

### English

My beloved sweet Jolánka! I continue my lines. I regret to have to tell you that I cannot come home at all before the spring, because things here are such that a man may not go home even for his own sibling's wedding. And yet, believe me, my darling, I would so like to talk with you at last, my darling, my dear. I too pray to the good God that you, the flower of my love, may bloom for me alone; then I shall be the happiest man in the world. Though even now I feel I am, for the knowledge that you love me, my dear, makes me happy. I can only love you more and more, never tire of you. I only wrote that because some other man may one day tempt you with a finer future, and then you would simply leave me. I will say it before the whole world: my wife will be you or no one. I am waiting for the photograph, and wish you success with it. I am glad you are well; I am too.

God be with you, I remain your admirer, faithful unto the grave, Feri.

### Slovak

Moja milovaná, sladká Jolánka! Pokračujem vo svojich riadkoch. S ľútosťou Vám musím oznámiť, že do jari vôbec nemôžem prísť domov, lebo je tu taký svet, že človek nemôže ísť domov ani na svadbu vlastného súrodenca. A pritom mi verte, drahá, veľmi by som sa už chcel s Vami porozprávať, drahá moja, milá moja. Aj ja prosím dobrého Boha, aby ste Vy, kvet mojej lásky, rozkvitli len pre mňa; potom budem najšťastnejším mužom na svete. Hoci aj teraz sa tak cítim, lebo ma robí šťastným vedomie, že ma ľúbite, milá moja. Ja Vás viem len stále viac ľúbiť, nie sa Vás nabažiť. Napísal som to len preto, že Vás raz možno iný muž zláka krajšou budúcnosťou a potom ma pekne opustíte. Pred celým svetom poviem: mojou ženou budete Vy alebo nikto. Čakám na fotografiu a želám Vám k nej veľa úspechov. Teší ma, že ste zdravá, aj ja som.

S Bohom, zostávam Váš do hrobu verný ctiteľ, Feri.

## Uncertainties

- **Row 24, *szépen* ("nicely, simply") is the weakest word.** Before `eh` stand two pencil signs among the seal's letters: an upright cross and a sign that is probably a wide right bowl. By the key that would be f + s, or z + s if the cross is used as in row 27, which is the reverse of *sz*. The word is inferred from sense, and the e of *-pen* is not written.
- **Row 13, *szerelmem virága*.** The signs after *szer* are heavily overwritten and were recognised, not read one by one. *szerelem* ("of love") is equally possible; no distinct second m is visible. *virága* lacks its second vowel.
- **Row 12.** One overstruck sign after *hogy* has no value.
- **Row 13–14 *számomra*.** The text has `sza|momomra`; one *mo* is taken as repeated.
- **Row 25, *megmondom nőm*.** This lies mostly under the seal. *nőm* ("my wife") is a sense reading; a small tick by the o may or may not be its accent.
- **Row 5, *[me]hetek*.** The bracketed me- and the final k are supplied by the editor, not read.
- **Box rows.** In `lemere` (*maradok*) the bars after the m are not secure. In `dokoksi` the second `ok` has no place in the sentence and is taken as a repeat. In `madoja` the o is only a hook.
- **Row 24 *másik férfi*.** `sikferi` is split by sense, with one f omitted, and is not the name Feri.
- **Writer's spelling.** Many normalizations follow from it: `fojtatom`, `ojan`, `lakodamera`, `bodogi`, `angem`, `arre`, `soraim` (suffix *-at* added), `higyje`, `jovov` (for *jövővel*). The full list is in SOLUTION.md.
- **Identity and date.** Feri is known only from the signature; the closing matches HCP 1292 (*sírig hű imádója, Feri*) and HCP 1216, but identity is not claimed. The year and place of writing are unknown. The ban on leave suggests military or similar service, but the card does not say so.

## Review and what changed

An independent Claude Opus 5.5 reviewer read every row on its own panels, decoded them with its own script, and returned **REVISE**. It found no wrong word in the normalized sense, but several errors in the literal transcription. All findings were rechecked on the scan, and the changes were:

- Row 1 is `szeretetett`, not `szeretett`; the first reading had followed the wording expected from HCP 1216. Row 15 is `lesszek`, with a doubled s.
- Row 13's last sign and row 12's vowel have two bars: `sza|momomra` and `maga`. An earlier claim that the writer put e for á in *számomra* was withdrawn.
- Row 13's uncertain signs are now marked uncertain in the ledger, with both *szerelmem* and *szerelem* given.
- Three undisclosed normalizations, the plain address and a tick in row 25 were added to the record.
- Row 24: the reviewer showed that part of what had been read as a hook was seal ink, and proposed a single cross. A colour map separating violet pencil from olive seal ink shows a second pencil sign after the cross, so the solver kept two signs and redescribed them. This point was not re-reviewed.

The normalized Hungarian and the translations did not change, so no second review round was needed.

![Row 24 crux at 7x: pencil cross, then pencil strokes around the olive seal R (work/crops2/r24_colour.png)](../work/crops2/r24_colour.png)
