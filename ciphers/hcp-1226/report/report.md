# HCP 1226 (cpc_--17_HU__HU_Jasz Arokszalas_jolanka-85): Feri to Jolánka Tóth, "I take your request as a command"

Human solver: Tomáš Pavuk

**Status: complete reading of the message (all 28 rows, the turn up the right edge and the 7 rows on the stamp, 724 signs). Every sign of row 27 is clear, but one clause there rests on two supplied endings, which are marked. Independent review 2 verdict REVISE; the one change it asked for is made.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1226 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1226), portal name cpc_--17_HU__HU_Jasz Arokszalas_jolanka-85, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no date, transcription or solution attached.

The picture side is a tinted photograph of a man and a woman at telephones, with the printed Hungarian captions "Szerelmi üzenet." ("Love message."), "Nem sokára nálad leszek drága kincsem!" ("Before long I shall be with you, my precious treasure!") and "Jöjj édesem vágyom utánad." ("Come, my sweet, I long for you."). It carries no cipher text.

The message is on the address side, in invented signs without word division: 28 rows over the left half and along the bottom of the card, written in green and then in violet, a last pair of signs up the right edge, and 7 short rows on the stamp. The plain address reads "Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás" ("To the promising young lady Jolánka Tóth, Jászárokszállás"). The left postmark begins ÉRSEK; Érsekújvár is likely but not proved, and the date (a "17" is visible) gives no year.

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). The key was transferred unchanged from those cards. This is a **known, transferred key**, not a new key recovery. No published reading of this card was used; the portal attaches none, and the AI Decipherment Register had no record of it on 2026-11-02.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the plain address and the rows on the stamp (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is **manual**. The solver read all rows sign by sign from enlarged crops of the un-converted scan of the address side and recorded one token for each written sign in work/ledger.txt. On rows 26 to 28 and on the stamp, where printing, the postmark and the portal's mark cross the writing, the ink was separated by colour channel (work/crop2.py, work/crops2/stamp_ink.png). No OCR was used. Word expectations did guide some calls between near-identical signs; each such call is listed under Uncertainties.

No key parameter was fitted on this card. The family key decodes every sign into continuous Hungarian, and long words that nobody could have planned for come out letter by letter: "kimondhatatlan", "sajnálatomat", "összevissza", "teljesíthetném", "parancsnak". Repeated words decode identically ("édesem" five times). The closing "Isten vele, édesem, a boldog viszontlátásra" and the name Feri stand word for word on HCP 1248 and HCP 1251. Only one sign, the scribble in row 18, is taken without a sign value.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs. The labels below are conventional names for the handwritten shapes.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S-shape | k | F-like | r |
| six | b | wave | l | right bowl (also a heavy 9-shape, rows 7, 21) | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| short tick + long stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short (h/p near-homograph) | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | opposed bowls | cs | | |

Dots over o and u give ö, ü and ő. On this card gy is written as the two signs g + y, and old-style "cz" as left bowl + z ("piczi"). Accents stand above the signs as marks and are mostly visible.

## Plaintext

`{x}` is a value taken from word sense, `[#]` a scribbled sign. Plain h in the output stands for the h/p sign, so "szépen" prints as "szehen".

```
01 szeretetedesegyetlenre          15 viszacsokolni{d}esa{j}nosezt
02 menyembecsessoraitmeg           16 megsokatehetemijameg
03 ka{p}tammitköszonoksze           17 edesemmikorjönhalehetki
04 hensajnalatomatkelki            18 megyekelejeb[#]azalloma
05 fejeznemhogynemjönmulat         19 sonkedvesemekeresetmin
06 sagba{d}eigyisjocsakazafö       20 digharancsnakveszemmertcsak
07 hogyviszontlathatom             21 maganakelekesörülaszivem
08 higyjeeledesemmikorso           22 hamagaszavaitteljesithe
09 raitolvasomkimondhatat          23 temlegjobszeretnemmar
10 lanerzesfogtaelszive            24 haszavaithalhatomes
11 metmiterzekenmagairant          25 teljesithetnemdemaj{d}
12 aztleirninemlehetlegjob         26 eljöazazidömitaligaligvarokamitarokonaitil
13 benszetnemmarkeblemreölel       27 letimodorommeglesznekelegetalanamugyismegaztirja
14 niedesemahiczinyszajatosze      28 megedesemhogymicsodafoglakozastmondmajdrokonin
E1 ak (up the right edge, continues row 28)
on the stamp: istenve | leedes | semabol | d{o}gvi | szont | latasra | {f}eri
```

### Hungarian (normalized)

Szeretett édes egyetlen reményem! Becses sorait megkaptam, mit köszönök szépen. Sajnálatomat kell kifejeznem, hogy nem jön mulatságba, de így is jó, csak az a fő, hogy viszontláthatom. Higgye el, édesem, mikor sorait olvasom, kimondhatatlan érzés fogta el szívemet. Mit érzek én maga iránt, azt leírni nem lehet. Legjobban szeretném már keblemre ölelni, édesem, a piczíny száját összevissza csókolni, de sajnos ezt még soká tehetem. Írja meg, édesem, mikor jön, ha lehet, kimegyek eléjébe az állomáson. Kedvesem e kérését mindig parancsnak veszem, mert csak magának élek, és örül a szívem, ha maga szavait teljesíthetem. Legjobban szeretném már, ha szavait hallhatom és teljesíthetném, de majd eljő az az idő, mit alig-alig várok. Ami a rokonait illeti, modorom[mal] meg lesznek elége[dve] talán. Amúgy is még azt írja meg, édesem, hogy micsoda foglalkozást mond majd rokon[a]inak.

On the stamp: Isten vele, édesem, a boldog viszontlátásra. Feri

Plain handwriting, address: Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás. Printed on the picture side: Szerelmi üzenet. / Nem sokára nálad leszek drága kincsem! / Jöjj édesem vágyom utánad.

### English

My beloved sweet only hope! I have received your dear lines, for which I thank you very much. I must express my regret that you are not coming to the dance party, but it is fine this way too; the main thing is that I can see you again. Believe me, my darling, when I read your lines an inexpressible feeling took hold of my heart. What I feel for you cannot be written down. Most of all I would like to clasp you to my breast now, my darling, and kiss your tiny mouth all over, but sadly it will be a long time before I can do that. Write to me, darling, when you are coming; if possible I will come out to meet you at the station. Dear one, I always take your request as a command, for I live only for you, and my heart rejoices when I can carry out your words. Most of all I would like to hear your words now and carry them out, but the time will come that I can hardly, hardly wait for. As for your relatives, they will perhaps be satisfied with my manners [two endings supplied, item 1]. Anyway, do also write to me, darling, what occupation you will tell your relatives.

On the stamp: God be with you, my darling, until the happy reunion. Feri

Address: To the promising young lady Jolánka Tóth, Jászárokszállás. Printed: Love message. / Before long I shall be with you, my precious treasure! / Come, my sweet, I long for you.

### Slovak

Moja milovaná sladká jediná nádej! Vaše milé riadky som dostal, za čo veľmi pekne ďakujem. Musím vyjadriť ľútosť, že neprídete na zábavu, ale aj tak je to dobré, hlavné je, že Vás znova uvidím. Verte mi, drahá, keď čítam Vaše riadky, zmocnil sa môjho srdca nevysloviteľný pocit. Čo k Vám cítim, to sa nedá opísať. Najradšej by som Vás už privinul na hruď, drahá, a celé Vaše maličké ústa pobozkával, ale žiaľ, to ešte dlho nebudem môcť. Napíšte mi, drahá, kedy prídete, ak sa dá, vyjdem Vám v ústrety na stanicu. Moja milá, Vašu prosbu vždy beriem ako rozkaz, lebo žijem len pre Vás a moje srdce sa raduje, keď môžem splniť Vaše slová. Najradšej by som už počúval Vaše slová a plnil ich, ale príde ten čas, na ktorý sotva, sotva čakám. Čo sa týka Vašich príbuzných, s mojimi spôsobmi budú azda spokojní [dve koncovky sú doplnené, bod 1]. Aj tak mi ešte napíšte, drahá, aké zamestnanie poviete svojim príbuzným.

Na známke: S Bohom, drahá, do šťastného zhľadania. Feri

Adresa: Sľubnej slečne Jolánke Tóthovej, Jászárokszállás. Tlačený text: Ľúbostný odkaz. / Onedlho budem u teba, môj drahý poklad! / Príď, moja milá, túžim po tebe.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1226/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the four image files, decodes work/ledger.txt with the key, and prints the literal rows and then work/normalized.txt.

## Uncertainties

1. **Row 27, the one clause with supplied endings.** Every sign is clear; the literal run is `modorommeglesznekelegetalan`, and it ends in the plain word "talán", "perhaps". I read (a) "modorom[mal] meg lesznek elége[dve] talán", "they will perhaps be satisfied with my manners". "-mal" and "-dve" are not on the card; they are supplied, and this division is an editorial reading of the sense, not something the card shows. In its favour: "lesznek" stands complete and its plural fits the relatives as subject, "meg" stands where the resultative needs it ("meg lesznek elégedve"), the instrumental is the regular government with this verb, the same construction occurs on HCP1275 row 25 ("meg lesz örökítve"), and this writer often drops letters and syllables ("szetném", "ija", "foglakozást", "rokon[a]in", "legjob"). Alternatives: (b) the idiom "elege lesz", "they will perhaps have had enough of them", the opposite drift, which the card alone cannot exclude, but it needs "lesznek" broken as "lesz nek[ik]"; (c) "modorom meg lesz nek[ik] elege talán", taken as "will be enough for them", which I held at review 2 and now withdraw: "enough for them" would be "elég lesz nekik", and "elege" does not mean that. No parallel for the words "modor" or "elégedve" turned up in the SOLUTION.md files of other cards.
2. **S4 "boldog**": the first o is partial under the printed stamp, its lower loop is lost; d, g, v, i are legible. The word sense and the closing on HCP1248 and HCP1251 ("a boldog viszontlátásra", same writer) support it.
3. **S7 "Feri**": the first sign is a tilted cross, between f and u; f from word sense, as on HCP1216, whose signature is the same name. No identification of the two writers is claimed beyond the name and the shared key.
4. **Row 18 scribble**: after "b" one sign is inked over solid. It has the size and bar structure of a three-bar sign; e is by sense and gives "eléjébe" ("go to meet"). The ledger keeps it as `[#]`. "az állomáson" "at the station" is what is written ("az állomásra" would also be expected). The row ends in "alloma" and row 19 starts "son"; the double wave of "áll-" is merged but legible.
5. **Word-sense calls among near-homographs** (all h/p and d/n as the task asked to state). "szépen", "parancsnak", "piczíny": p decided by sense, the sign is h/p. Row 3 "kaptam": the sign is a separate tick above-left of a long stroke, the d form, so ledger token `D/p`; p is by sense only. Rows 6 and 15 "de" are written with the h/p sign, not the tick + long d. Row 25 "majd": last sign is two long strokes, read d, not n. Row 15 "sajnos": the sign is an upright cross (the f sign), not the inverted T; only j gives a word. Row 12 "leírni": the first i has its dot, the second i (before "nem") shows none, so that one could be taken as o. Row 19 "kérését": the t is heavily overwritten and may have started as F. Row 28 "foglalkozást": the s has a hook and looks like a reversed bowl. Row 17 "jön": the strokes after ö are thick and run together (n by sense).
6. **Row 16** reads `megsokatehetem`; I take the single t with "tehetem" ("még soká tehetem"). The negative "nem" one might expect is not written. An ö/ő distinction is not made by the hand. Dots over o are marked `:d` only where seen; in row 3 only the first o of "köszönök" has them. Review 1 did not note others, but I did not re-audit every o.
7. **Writer's spellings normalized**: "szeretetedes" (t dropped), "higyje" → higgye, "kel" → kell (row 4, single l), "legjob-ben" → legjobban (row 12–13) and "legjob" → legjobban (row 23), "szetném" → szeretném (row 13, re dropped), "ija" → írja (row 16, r not written), "szájat" → száját, "oszevisza" → összevissza, "viszontlathatom" with the heavy s, "foglakozást" → foglalkozást, "rokonin+ak" → rokonainak (a not written), "amit" → ami (row 26), "hallhatom" written "halhatom", "maj{d}", "eljö" → eljő, "modorom[mal]" and "elége[dve]" (row 27, supplied, item 1), "édes|sem" → édesem (S2–S3, the s is doubled across the row break). Acute accents are mostly visible but not transcribed; they are supplied.
8. **Row 28 → right edge**: "ak" stands rotated up the right edge about 250 px (of 2210) above row 28; on my reading it completes "rokon(a)inak". The wave at the corner is the upright end of row 26 ("il", continued as "leti" on row 27), not part of the edge run.
9. **Address and postmark**: "Szépreményű" runs into the postmark, so its ending is by sense; "úrleánynak" is partly under the portal's mark. The left postmark begins ÉRSEK…; Érsekújvár is likely but unproved, and the date (a "17" is visible) gives no year.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, two rounds. In each round it ran the reproduction command, made its own crops, decoded with its own script and compared the result with the card (in round 2, 724 tokens over 17 rows without a difference, and all 28 main rows of the command output against the stated text).

Round 1, changes made:

- **Stamp rows S3 and S4.** The first reading was wrong. Green-suppressed crops show "semabol" and "dogvi", so the closing is "a boldog viszontlátásra".
- **Row 27.** A sign misread as e is a, so the run ends in plain "talán", "perhaps". The first interpretation of the clause was dropped.
- **Row 18.** The normalized text became "eléjébe az állomáson", and the scribbled sign stays marked.
- **Dots and "kaptam".** Two dots not on the card were removed from row 3, and the p of "kaptam" is marked as taken from sense.
- **Doubled s.** "édes|sem" across rows S2 and S3 is now stated.

Round 2, verdict **REVISE**, changes made:

- **Row 27, major.** The division "lesz nek[ik] elege" broke the complete word "lesznek" and treated "elege" as "elég". The clause now reads "modorom[mal] meg lesznek elége[dve] talán", with the two supplied endings marked. No sign changed.
- **Claim of no parallel.** Narrowed to the words themselves; the construction has a parallel on HCP 1275.
- **Spelling list.** "kel" for "kell" added.

The reviewer could not verify the tone of row 27 from the card alone, the partial o of S4, the postmark date, or which person's occupation row 28 means; the English keeps that open.

## Sources

- HC Portal record 1226, General, Description and Attachments tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1226 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3738/conversions/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-85_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/3738/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-85_pic.jpg (work/hires/).
- Address side: https://api.hcportal.eu/media/3739/conversions/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-85_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/3739/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-85_adr.jpg (work/hires/).
- Family key: finished Jolánka cards in this repository, chiefly ciphers/hcp-1216.
- HistoCrypt paper on the collection: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-02.
