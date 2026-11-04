# HCP 1252: Feri to Jolánka Tóth, "we should say te" and a pay sum

Human solver: Tomáš Pavuk

**Status: cipher block deciphered in full (8 rows, 180 tokens, of which 174 are key signs); the plain handwriting on the card is also read, except for one short itinerary phrase. Independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-01. All reading by Claude Opus 5.5; there was no earlier work on this number.

## Origin and context

The cryptogram is record 1252 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1252), portal name cpc_1913-06-13_HU__HU_Jasz Arokszalas_jolanka-37, from Tobias Schrödel's collection of cryptographic postcards (private collection). At capture on 2026-11-01 the portal listed it as **Not solved**, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution was found or used.

The date 1913-06-13 comes only from the filename; the postmarks are too faint to confirm it.

The picture side shows a couple with printed song text ("Cigányprímás / Lári-Fári", Amag 60681/5) and has no handwriting.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address side reads Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás ("To the promising young lady Jolánka Tóth, Jászárokszállás"). The message has two parts in one green ink: a **cipher block** of 8 rows at the top left, then **plain Hungarian handwriting** that runs on below it and along the bottom edge of the card. A plain greeting is written inside the stamp box and was hidden under the stamp, which is now lifted (steganography; checked 2026-11-03). So only part of the message is enciphered.

![Address side: the cipher block at the top left, the plain text below it (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the family of cipher postcards addressed to Jolánka Tóth, several of which are finished in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). The same hand, ink, address and signature recur.

## Method

This card was read with a **known, transferred key**, not a new key recovery. The key and sign classes come unchanged from HCP 1216 and its sister cards, on which earlier work was done by an OpenAI GPT solver and by Claude Opus 5.5.

The transcription is manual, not OCR. Each cipher row was cropped from the un-converted original scan at 2.5×, with hard signs at 5×, and read sign by sign into a ledger (work/ledger-opus.txt). A script (work/decode_opus.py) decodes that ledger with the key. The plain text was read separately as ordinary cursive.

To reproduce, from the repository root:

```sh
python3 -I ciphers/hcp-1252/work/decode_opus.py
```

It checks the SHA-256 of the four image files, prints the literal rows, then the normalized text.

## Key

Type: **MASC + Steganography** (updated 2026-11-03). Hungarian simple monoalphabetic substitution (MASC) with invented graphic signs; in addition a plain greeting was hidden under the postage stamp. The names below are conventional labels for handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left + right bowl pair | cs | three short strokes | m | gamma/corner | t |
| stroke + tick to its left | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| open hook with descender | g | stroke + tick to its right | h/p | low descender | y |
| dotted crossed curve | i | inverted T | j | crossed diagonal | z |

The signs for h and p are one homograph, so the choice between them rests on word sense. On this card that means h in hogy (twice) and haragudjon, and p in megkaptam. Dots over o or u mark ö or ü. This writer spells gy as g + y. The digits **10** stand unenciphered inside the block (row 7), with a flagged 1 and a closed ring, unlike the tailed cipher o on the same row.

Accents on a, e, i, o and u are not marked by the cipher and are supplied in the normalized text.

## Plaintext

Literal decipherment of the cipher block (h stands for the h/p sign):

```text
1 szeretetetedesjolankam
2 becsessoraitmegkahtammelyet
3 igenkoszönök.igazanorü-
4 lökhogyigyszolimarne
5 künktegeznikeleneegymast
6 edesem,kedvesemneharagudjon
7 hogyrövidenirokde10re
8 rendezonkellenni.
```

The plain handwriting, as written:

```text
 9 án indultam 4·30 p kor Érsek
ujvára érk. 10 én éjel 1ó
30 p vigas in. 18 ól. u 1ó 11 p
rendezőre érk. 11 éjel 1ó 30 p
Kedvesem számítsa
ki mit kerestem csináltam
23[7?] km fizetne 6 tized fil
kilométerenkint és 33 órát
a 8 fil és 2 korona napi
díj most mást nem irok
men/mer menem kel 10 órára rendezö(i)nkbe lenem
majd legközelebb bővebben isten vele édesem
más külömben jó dolgom van
```

In the stamp box, under the lifted stamp: [C]sókolom számtalanszor Feri (the C mostly under a stamp fragment).

### Hungarian (normalized)

**Cipher:** Szeretett édes Jolánkám! Becses sorait megkaptam, melyet igen köszönök. Igazán örülök, hogy így szólí[t]. Már nekünk tegezni kellene egymást, édesem, kedvesem! Ne haragudjon, hogy röviden írok, de 10-re rendezőn kell lenni.

**Plain:** 9-én indultam 4.30 p-kor Érsekújvárra, érk. 10-én éjjel 1 ó 30 p. {vigas} in. {18 ól. u} 1 ó 11 p. rendezőre érk. 11[-én] éjjel 1 ó 30 p. Kedvesem, számítsa ki, mit kerestem! Csináltam 23[7?] km-t, fizetne 6 tized fillért kilométerenkint, és 33 órát a 8 fillér, és 2 korona napidíj. Most mást nem írok, mer[t] mennem kell, 10 órára rendezőnkbe lennem. Majd legközelebb bővebben. Isten vele, édesem. Máskülönben jó dolgom van.

**In the stamp box (under the stamp):** Csókolom számtalanszor. Feri

### English

**Cipher:** Beloved sweet Jolánka of mine! I have received your precious lines, for which I thank you very much. I am truly glad that you address me like this. We ought to be saying te to each other by now, my sweet, my darling! Do not be angry that I write briefly, but by 10 I have to be at the marshalling yard.

**Plain:** I left on the 9th at 4.30 for Érsekújvár, arrived on the 10th at 1.30 at night; {vigas} dep.(?) {18 ól. u} 1.11, arrived at the yard on the 11th at 1.30 at night. Darling, work out what I earned! I did 23[7?] km; it would pay six tenths of a fillér per kilometre, and 33 hours at 8 fillér, and a 2-crown daily allowance. I write nothing else now, because I have to go, I must be at our yard by 10 o'clock. More next time. Farewell, my sweet. Otherwise I am doing well.

**In the stamp box (under the stamp):** I kiss you countless times. Feri

### Slovak

**Šifra:** Milovaná sladká moja Jolánka! Vaše vzácne riadky som dostal, za čo veľmi ďakujem. Naozaj sa teším, že ma takto oslovujete. My by sme si už mali tykať, drahá moja, milá moja! Nehnevajte sa, že píšem stručne, ale do desiatej treba byť na zoraďovacej stanici.

**Nezašifrované:** Deviateho som odišiel o 4.30 do Nových Zámkov, prišiel som desiateho v noci o 1.30; {vigas} odch.(?) {18 ól. u} 1.11, na zoraďovaciu stanicu som prišiel jedenásteho v noci o 1.30. Drahá, vypočítajte, čo som zarobil! Urobil som 23[7?] km, platili by šesť desatín fillára za kilometer, a 33 hodín po 8 fillárov, a 2 koruny denné. Teraz viac nepíšem, lebo musím ísť, o desiatej musím byť na našej stanici. Nabudúce viac. S Bohom, drahá. Inak sa mám dobre.

**V políčku na známku (pod známkou):** Bozkávam Vás nespočetnekrát. Feri

## Uncertainties

Cipher block:

- **Row 1 szeretetet édes.** The signs give one -et- too many for szeretett. Normalized as on HCP 1216; the card literally has szeretetet. No effect on the sense.
- **Row 4 szoli már.** The sign after i is three strokes (m), so no t is on the card. szólí[t] is a sense-based normalization. Support for a dropped final t comes from mer[t] on HCP 1216. Whether már closes this clause or opens the next is editorial.
- **Row 8 kel lenni.** The letters are k-e-l-l-e-n-n-i. Kell enni ("one must eat") is the other division; the plain text's rendezőnkbe lenem decides for lenni. The o of rendezon shows no dots, and ő is supplied.
- **Row 3 köszönök.** The final sign is k, though grammar would want köszönöm with melyet. Transcribed as written.
- **Row 2.** The sign after sorai is a blot that keeps a top bar and a stem; t is the only fit. The p sign of megkaptam is also heavily inked.
- **Spellings.** kelene is normalized to kellene.

Plain handwriting, an ordinary cursive reading and no part of the cipher:

- **{vigas} in. {18 ól. u} is not understood.** The letters are v, i, a descending z/g-like letter, a/o and s. in. as indultam is a guess. vissza in[dultam] ("started back") would suit the itinerary but cannot be confirmed on the pixels, so it stays an open hypothesis. **This phrase is the one limit on the claim of a complete reading of the card.** It lies outside the cipher.

![Third plain row, enlarged: "30 p vigas in. 18 ol. u 1ó 11 p" (work/crops/report-row3.png)](../work/crops/report-row3.png)

- **23[7?] km.** The third digit is a crossed sign under a faded streak; a crossed 7 is likely. As a check, 237 km × 0.6 f + 33 h × 8 f + 2 K comes to about 6.06 K, a plausible sum, but this does not settle the digit.
- **men/mer.** The word looks like men. It is read mer[t] only because that is the writer's form on HCP 1216 and his r and n are close.
- **rendezö(i)nkbe.** Partly under the HCPortal stamp; normalized rendezőnkbe.
- **Smaller points.** indultam ends in a flourish; csináltam could be csináltan; the last row is faint and van is the best fit for a smudged word.

Inferences:

- **Railway work.** The writer's job is not stated. "Marshalling yard" for rendező is an inference from the pay per kilometre, the hours, the daily allowance and the arrival times.
- **Sender.** "Feri" is the signature, matching the name on HCP 1216. The portal lists the sender as Unknown, and nothing further is claimed.

## Why the reading is correct

- The key, transferred unchanged, gives Hungarian for all 174 key signs among the 180 tokens. The other six are 2 digits, 2 dots, 1 comma and 1 hyphen. No sign lacks a value and none was invented.
- The text is natural private Hungarian of the period. The proposal to move to tegezés suits a courtship card.
- The plain text confirms the cipher: cipher 10re rendezon kel lenni matches plain 10 órára rendezö(i)nkbe lenem.
- Repeats decode identically, including hogy twice, and a written hyphen divides örü-lök across rows 3 and 4.

## Review

An independent Claude Opus 5.5 reviewer ran the reproduction command and decoded the card with its own script and key table, with all 8 rows and 180 tokens the same. It had seen the solver's text before naming the signs, so this proves agreement sign by sign, not a blind reading. It then checked every sign of all 8 rows on its own enlargements, and re-read the plain handwriting, the key against HCP 1216 and the sources.

Verdict: **ACCEPT**, with four minor findings on wording. What changed because of them:

1. The unread itinerary phrase is now stated as a limit on completeness, and vissza in[dultam] is recorded as an open hypothesis.
2. The support for the dropped t now rests on HCP 1216 alone, not on the uncertain mer of this card.
3. The railway job is now marked as an inference, including in the title.
4. "Every one of the 180 tokens" became 174 key signs plus six digits and marks.

The ledger, the key and the reading did not change. The reviewer could not verify the third digit of 23[7?], the 1913-06-13 date, or the supplied accents.
