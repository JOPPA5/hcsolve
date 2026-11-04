# HCP 1246 (cpc_1913-09-_HU__HU_Jasz Arokszalas_jolanka-115): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (28 rows, one row up the right edge, 7 rows in the stamp box, 778 signs); independent review 1 verdict REVISE, all findings addressed. The key and the reading stood; one group left unread at handover was solved in review.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1246 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1246), portal name cpc_1913-09-_HU__HU_Jasz Arokszalas_jolanka-115, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution was found.

The picture side is a tinted photograph of a courting couple, printed no. 3244, with a printed Hungarian verse headed Oh csak még egyszer összejönnénk ("Oh, if only we could meet once more"). It carries no cipher text. The message is on the address side in green ink: 28 rows of invented signs running around the address, one row up the right edge and seven short rows in the stamp box. The address itself is in clear: Nagysága Tóth Jolánka úrleánynak, Jász Árokszállás. The postmark reads 913 SEP, that is September 1913.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the clear address and the postmarks (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth in Jászárokszállás and signed Feri, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery.

## Method

The key was taken unchanged from HCP 1216. The work was the transcription: all rows were read sign by sign on enlarged crops of the full-resolution address scan, and each written sign was recorded as a token in a ledger (778 signs). The ledger is manual, with no OCR, and it is not blind: it was read knowing the family's hand and vocabulary. All sign classes on the card are in the family key, and no new sign was needed. A short script checks the hashes of the scans, decodes the ledger and prints the text.

The writer spells loosely: he drops letters, repeats syllables and marks acute accents only faintly. The literal decipherment below keeps what is written; the normalized Hungarian is editorial.

## Key

**Cipher type: MASC + Steganography** (updated 2026-11-03): Hungarian simple monoalphabetic substitution with invented signs, and part of the message (7 rows) is hidden in the stamp box under the stamp, which is now lifted. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma / corner | t |
| long stroke + tick | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + tick | h / p | low descender | y |
| open hooked loop | g | crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

One sign serves for both h and p, so that call always rests on word sense (kaptam, szépen, Pestre, lapját = p; hogy, haragszom = h). Digraphs are written as letter pairs on this card (gy = g+y, sz = s+z, cs = c+s). Dots over o and u give ö and ü. The sound ly is written j (mijen, ijesmit, gujas).

## Plaintext

Literal decipherment, row by row (h stands for the h/p sign; `[o]` is a sign hidden by a blot and restored):

```text
01 imadotedesegyetlenreme
02 nyembecsesleveveletmeg
03 kahtammitköszönökszehen
04 edesemazertnemharagszom
05 agujasrahogyaztbeszelte
06 mocsarnenekmerttudomhogy
07 mijenamoczarnehogykonnyen
08 lehetugratniamoczarnet
09 esörülhaijesmithaldereme
10 lemjolankamedesazijenbesze
11 deknemzavarjakboldogsagunkat
12 esnemhiszelijesmittanacso
13 lomhogycsakegeszhidegenvisel
14 kedjenelötteeshalatjhogynem
15 megysemireakormajdfelhagy
16 veleenmarnemtartomerdemes
17 nekf[o]glalkoznivele.edesem
18 örömemfejezemkihogy
19 felfogjönnihestreaztnem
20 iskeligernemhogyfelkere
21 semazelsöalkalommal
22 megfogomlatogatniir
23 jamegmikorjömenagaelötnincs
24 semimititkomakorraakarok
25 jobbalasurhatvennimerttu
26 domhogyarokonsagjobbanmegneziazembertedesemazt
27 nekelmondanommaganakhogymegegylahjatsemolvas
28 taavatatlakezcsakenistenveleedesemaboldogvi
29 szontlatasra (up the right edge)
stamp box: hükedves / seferi / csokol / jaszam / talan / szor / feri
```

**Hungarian (normalized; [..] = letters not on the card; {..} = literal form kept, sense uncertain):**

Imádott édes egyetlen reményem! Becses levelét megkaptam, mit köszönök szépen. Édesem, azért nem haragszom a Gulyásra, hogy azt beszélte Mocsárnénak, mert tudom, hogy milyen a Mocsárné, hogy könnyen lehet ugratni a Mocsárnét, és örül, ha ilyesmit hall. De remélem, Jolánkám édes, az ilyen beszédek nem zavarják boldogságunkat, és nem hisz el ilyesmit. Tanácsolom, hogy csak egész hidegen viselkedjen előtte, és ha látja, hogy nem megy semmire, akkor majd felhagy vele. Én már nem tartom érdemesnek foglalkozni vele. Édesem, örömem fejezem ki, hogy fel fog jönni Pestre. Azt nem is kell ígérnem, hogy felkeresem az első alkalommal, meg fogom látogatni. Írja meg, mikor {jöm}. Én [m]aga előtt nincs semmi titkom. Akkorra akarok jobb állású r[u]hát venni, mert tudom, hogy a rokonság jobban megnézi az embert. Édesem, azt ne[m] kell mondanom magának, hogy még egy lapját sem olvasta avatatla[n] kéz, csak én. Isten vele, édesem, a boldog viszontlátásra.

Stamp box: Hű kedvese Feri. Csókolja számtalanszor Feri.

**English:**

My adored, sweet, only hope! I received your esteemed letter, for which I thank you kindly. Darling, I am not angry with Gulyás for having told that to Mrs Mocsár, because I know what Mrs Mocsár is like, that she is easily teased, and she is glad when she hears such things. But I hope, my sweet Jolánka, such talk does not disturb our happiness, and that you do not believe such things. I advise you to behave quite coolly in front of her, and when she sees she gets nowhere, she will give it up. I no longer think it worth bothering with her. Darling, I express my joy that you will come up to Pest. I need not even promise that I will look you up at the first opportunity, I will visit you. Write when {you are coming / I should come}. I have no secrets from you. By then I want to buy a better suit (reading uncertain, perhaps "better-fitting"), because I know the relatives look a person over more closely. Darling, I need not tell you that not one of your cards has been read by an uninitiated hand, only by me. God be with you, darling, until a happy meeting again.

Stamp box: Your faithful sweetheart Feri. Feri kisses you countless times.

**Slovak:**

Moja zbožňovaná, sladká, jediná nádej! Váš vzácny list som dostal, za čo pekne ďakujem. Drahá, nehnevám sa na Gulyása, že to povedal Mocsárovej, lebo viem, aká je Mocsárová, že sa dá ľahko doberať a teší sa, keď počuje niečo také. Ale dúfam, moja sladká Jolánka, že také reči nenarušia naše šťastie a že niečomu takému neveríte. Radím Vám, aby ste sa pred ňou správali celkom chladne, a keď uvidí, že ničoho nedosiahne, tak s tým prestane. Ja už nepovažujem za hodné zaoberať sa ňou. Drahá, vyjadrujem radosť, že prídete hore do Pešti. Ani Vám nemusím sľubovať, že Vás pri prvej príležitosti vyhľadám, navštívim Vás. Napíšte, kedy {prídete / mám prísť}. Pred Vami nemám nijaké tajomstvá. Dovtedy si chcem kúpiť lepší oblek (čítanie neisté, azda „lepšie padnúci“), lebo viem, že príbuzní si človeka lepšie obzrú. Drahá, nemusím Vám hovoriť, že ani jeden Váš lístok nečítala nepovolaná ruka, iba ja. S Bohom, drahá, do šťastného zvidenia.

Pole na známku: Váš verný milý Feri. Bozkáva Vás nespočetnekrát Feri.

## What remains uncertain

- **Row 28, avatatla[n] kéz.** The fifth sign of the row is cut by the lower edge of the card. Two strokes are visible, so a is possible, and only the set phrase settles it. The n of avatatlan is not on the card. Lap is taken as "card"; it could mean "page".
- **Row 23, `jöm`.** The strokes after jö are heavily over-inked, so the count of three is less firm than elsewhere. The word could be jön ("you are coming") or a slip for jöjjek ("I should come"). The literal form is kept and both senses are given. Én [m]aga előtt is a broken construction; the m is not on the card.
- **Row 25, jobb állású r[u]hát.** The signs a l a s u r h a t are clear, but the u of ruhát is taken as omitted, and the sense "better-fitting" is an interpretation that no sister card or period dictionary confirms.
- **Row 17, f[o]glalkozni.** The o lies under an ink blot and is a restoration; it is the only letter that makes a word.
- **Row 20, first sign.** A blotted crossed curve, read i from its shape and from is. Its accent in ígérnem rests on word sense.
- **Row 5, Gulyás.** Taken as a surname; the common noun "herdsman" is possible. Mocsárné is spelled two ways on the card (`mocsar-`, `mocz ar-`).
- **Right edge (row 29).** Read after rotating; `sz` is faint and crossed by a flourish of the address.
- **Stamp box.** The reading order is taken top to bottom.
- **Accents and h/p.** Acute accents are mostly supplied in normalization, and every h/p call rests on word sense.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the reproduction command, checked that every sign class belongs to the family key, diffed the ledger against the normalized text, and read the rows on its own enhanced crops of the scan. Some rows were zoomed only at 2.2×. Its verdict was REVISE. It confirmed the cipher type, the key and the reading and made eight findings, all accepted:

- The one group left unread at handover, `a vetatlakez` (row 28), is the set phrase avatatla[n] kéz. The card is complete because of this finding.
- The word előtte (row 14) had been dropped from the normalized text and translations and was restored.
- Two signs were misread in the ledger and first listed as writer's errors: `mondanim` is `mondanom` (row 27), and `tenacsolom` is `tanacsolom` (row 12). The other doubtful spellings were then re-read and stand as written.
- `jöm` (row 23) had been silently normalized to jöjjek; it is now kept literal, with both senses.
- Smaller changes: felkeresem with one s, two more spellings disclosed, two Slovak corrections, and a firmer caveat on állású r[u]hát.
