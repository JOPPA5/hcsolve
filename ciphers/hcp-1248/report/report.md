# HCP 1248: Feri invites Jolánka Tóth to the railwaymen's vintage ball

Human solver: Tomáš Pavuk

**Status: complete reading of the card (616 written tokens; the only unread mark is one sign blotted out by the writer); independent review 1 verdict REVISE, all findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1248 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1248), portal name cpc_1913-09-13_HU__HU_Jasz Arokszalas_jolanka-43, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The date 13 September 1913 comes from the portal's file name; it could not be confirmed from the postmark, which is only partly struck.

The picture side is a tinted photograph of an embracing couple with a printed Hungarian verse headed "Oh csak még egyszer összejönnénk" ("Oh, if only we could meet once more"). It is not enciphered.

The address side has the plain address **Őnagysága Tóth Jolánka úrleánynak, Jász-Árokszállás**. The cipher text fills the left half of this side in 25 rows; the last rows run on across the bottom edge. Seven more cipher rows stand in the box printed for the stamp, at the top right. The writer enciphered everything except "Okt" and two numbers.

The card belongs to the Jolánka family: cipher postcards to Tóth Jolánka of Jászárokszállás, signed Feri, in the same hand and cipher. Several are finished in this repository (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). The key was therefore **transferred, not recovered blind**. It came from those cards, whose earlier passes were by an OpenAI GPT solver and Claude Opus 5.5. The reading of this card is new and is by Claude Opus 5.5. There was no earlier work on this number, and no published solution was found or used.

![Address side: the cipher text at the left and along the bottom, the stamp box at the top right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, with printed verse and no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual. Every row was read sign by sign from enlargements (2.2x to 5x) of the un-converted original scan in work/hires/, and recorded as one token per written sign in work/ledger.txt. No OCR was used. Each sign was given its family value, including the cases where the word would have preferred something else; the writer's own slips are kept in the literal text and corrected only in the normalized text.

The reviewer read all 32 rows separately from its own crops, in a private alphabet, and decoded them with the family table. That comparison found the errors listed under Review summary.

From the repository root, this command checks the SHA-256 hashes of both scans and both originals, decodes the ledger, and prints the literal rows and the normalized text:

```sh
python3 -I ciphers/hcp-1248/work/decode.py
```

## Key

Hungarian text in a simple monoalphabetic substitution with invented graphic signs. The names below are conventional descriptions of handwritten shapes.

Cipher type (updated 2026-11-03): **MASC + Steganography**. Part of the message, seven cipher rows, was hidden in the stamp box under the stamp, which has since been lifted.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S-shape | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma / corner | t |
| long stroke + tick upper left | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + tick right | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

One sign serves for both h and p, so each case is decided by the word. Dots over o and u give ö and ü, and accents are written only sometimes. On this card gy is written as two signs, g + y, although HCP 1216 has one joined sign. "Okt" is in Latin letters and 15 is in plain digits. The 5 of "5-én" has the same shape as the writer's k sign and is read as a digit, because "on the 5th" is the only sense and it matches the 5 of 15.

## Plaintext

Literal decipherment, row by row (h stands for the h/p sign; S1 to S7 are the stamp box):

```text
01 edesegyetlenreményemnetün
02 jonfelhogyegyszetrekét
03 lahotisirokdehirtelenjöt
04 egyjóötletemnagyonorül
05 nekhamaganakismegtetszene
06 <Okt><5>énleszavasutasoknaka
07 szüretimulatságéshamaga
08 nakkedvevolnaeljönniak
09 korbeléhnékrendezönekazt
10 elöreigégremhogyojjan
11 mulatsagbamégnemvolt
12 ésfogalmasincsrorahogy
13 mijenlehetegyhestimu
14 latságlesznekvagyezren
15 isnagyo[blot].onszeretnemha
16 eljonnemertugysemmulat
17 hatunkmáskéhegyütmert
18 itnagyonnehézszabadidőt
19 kahnimostiscsakugykahnék
20 rendezölennéktehatke
21 remhogygyorsangondol
22 jamegadolgotmert<15>
23 igbekeljelentenihogy
24 rendezöakaroklenniezelbezatomsoraim
25 maradokb.soraitvarokedvesseferi
S1 istenve
S2 leédesem
S3 aboldog
S4 viszont
S5 latasr
S6 hűkedves
S7 seferi
```

Normalized Hungarian (word division, accents, punctuation and spelling corrections are editorial):

**Édes egyetlen reményem! Ne tűnjön fel, hogy egyszerre két lapot is írok, de hirtelen jött egy jó ötletem. Nagyon örülnék, ha magának is megtetszene. Okt. 5-én lesz a vasutasoknak a szüreti mulatság, és ha magának kedve volna eljönni, akkor belépnék rendezőnek. Azt előre ígérem, hogy olyan mulatságban még nem volt, és fogalma sincs róla, hogy milyen lehet egy pesti mulatság; lesznek vagy ezren is. Nagyon szeretném, ha eljönne, mert úgy sem mulathatunk másképp együtt, mert itt nagyon nehéz szabadidőt kapni. Most is csak úgy kapnék, ha rendező lennék. Tehát kérem, hogy gyorsan gondolja meg a dolgot, mert 15-ig be kell jelenteni, hogy rendező akarok lenni. Ezzel bezárom soraim, maradok b[ecses] sorait váró kedvese, Feri.**

**Stamp box: Isten vele, édesem, a boldog viszontlátásr[a]! Hű kedvese, Feri.**

English translation: **My sweet only hope! Don't be surprised that I am writing two cards at once, but a good idea has suddenly come to me. I would be very glad if you liked it too. On 5 October the railwaymen are holding their vintage ball, and if you felt like coming, I would sign up as a steward. This I promise you in advance: you have never been to such a ball, and you have no idea what a Pest ball can be like; there will be as many as a thousand people. I would very much like you to come, because we cannot have fun together any other way, since it is very hard to get free time here. Even now I would only get it if I were a steward. So I ask you to think it over quickly, because by the 15th I have to report that I want to be a steward. With this I close my lines, and remain, awaiting your [dear] lines, your sweetheart, Feri.**

**Stamp box: God be with you, my sweet, until our happy meeting! Your faithful sweetheart, Feri.**

Slovak translation: **Moja sladká jediná nádej! Nečudujte sa, že píšem naraz dva lístky, ale náhle mi prišiel dobrý nápad. Veľmi by som sa potešil, keby sa páčil aj Vám. 5. októbra bude vinobranecká zábava železničiarov a ak by ste mali chuť prísť, prihlásil by som sa za usporiadateľa. Vopred Vám sľubujem, že na takej zábave ste ešte neboli a nemáte potuchy, aká môže byť peštianska zábava; bude tam aj okolo tisíc ľudí. Veľmi by som chcel, aby ste prišli, lebo inak sa spolu aj tak nemôžeme zabaviť, keďže tu je veľmi ťažké dostať voľný čas. Aj teraz by som ho dostal, len keby som bol usporiadateľom. Prosím Vás teda, aby ste si to rýchlo rozmysleli, lebo do 15. treba ohlásiť, že chcem byť usporiadateľom. Tým končím svoje riadky a zostávam, čakajúc na Vaše [milé] riadky, Váš milý, Feri.**

**V rámčeku na známku: S Bohom, moja sladká, do šťastného zhľadania! Váš verný milý, Feri.**

Notes on the reading:

- The writer addresses Jolánka formally (maga, "you"), which is usual for this family of cards.
- Spellings corrected in the normalized text: egyszetre to egyszerre and bezatom to bezárom (t for r); rora to róla (r for l); igégrem to ígérem (an extra g); ojjan to olyan (j for ly, as in mijen, milyen, on this card and ojan on HCP 1216); it to itt; jöt to jött; kel to kell; ezel to ezzel; másképegyüt to másképp együtt; mulatsagba to mulatságban; kedvesse to kedvese, twice. Row 25 shares one k between váró and kedvese. The word látásr[a] lacks its final a.

## Uncertainties

- **h / p.** One sign serves for both. The choice is made by the word in hogy, hirtelen, ha, lehet, nehéz, hatunk, tehát, hű (h) and lapot, belépnék, pesti, másképp, kapni, kapnék (p).
- **Row 18, szabadidőt.** The sign after "szabad-" is faint and looks overwritten. Its flat right arm and the dot high above it fit i, not the writer's curled o, so i is **probable, not certain**. The next sign, read d, lies under a printed blue line. If the faint sign were a corrected o, the row would read szabadodot, a repeated szabadot kapni. Both mean "get time off". The z of "sza-" is a tilted cross read by the word.
- **Row 9, azt.** The sign after the two bars is heavy and looks overwritten, partly like an a. It is read z from context.
- **Row 19, first kapni.** The tick of the p sign sits low on the stroke; read p by the word.
- **Row 24, k of akarok.** The lower half lies on an abraded spot. This is a partial restoration; only one letter gives the word.
- **Missing i dots.** In row 13 and in the stamp box (isten) the i sign has no visible dot.
- **Row 25, "b.".** The card has only a six (with a dark blot in it) and a dot. The expansion b[ecses], "dear", is a **conjecture** from letter formulas; the rest of the closing does not depend on it.
- **Row 15, blot.** After nagyo the writer blotted out a sign, with a dot beside it, then wrote on. This is taken as a corrected slip, and nothing is read from it.
- **Stamp box, hű.** The h is faint and the marks over the cross are one tick and a trace; ű is chosen by the formula hű kedvese, which also occurs on HCP 1216.
- **Date and the 15th.** 13 September 1913 rests on the portal's file name. The card does not name the month of "the 15th"; if the date is right, 15 September would explain "gyorsan" (quickly), but that is an assumption. 5 October 1913 was a Sunday, a natural day for a ball.
- **Accents.** They were not audited sign by sign in review. They do not affect the reading.
- **Identity.** Feri is known only by that name. The ball itself was not looked up in any outside source.
- **The second card.** The writer mentions two cards at once. No other card dated 13 September was found among the portal records captured in this repository. HCP 1247 (19 September, in the portal's file name), which is still in review, mentions a ball and giving up the steward's post, so it appears to continue the story.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the command, read all 32 rows independently from its own crops and decoded them with the family table. It agreed with the ledger in 28 of 32 rows, accents ignored. It also confirmed the key's coverage, the address, the stamp box, the absence of a published solution, and that the language is natural for the period. It could not confirm the date from the postmark.

![Row 10, 5x enlargement: the two inverted T signs (j) after hogy o, followed by a and n, which give ojjan, olyan (review/work/z_r10_ttan.png)](../review/work/z_r10_ttan.png)

The findings, each checked on the enlargements and accepted:

- **Row 10 (major).** The first version read ottan and treated rows 10–11 as a broken clause. The two signs are inverted T (j), not gamma (t), so the word is ojjan, olyan. "Olyan mulatságban még nem volt" ("you have never been to such a ball") is one complete sentence, and the supposed weak point of the first version came from this misreading.
- **Row 12 (minor).** The first word is és, three bars with a dot above, not ás.
- **Row 18 (minor).** The first word is it, with one t; the supposed second t was a grey smudge.
- **Row 20 (minor).** The word is lennék, three bars, not lannék.
- **Row 18 end (minor).** The first version read a dittography, szabadodot. It now reads szabadidőt, with the i marked as probable.
- **Wording (minor).** The claim that every word was read clearly was withdrawn and the token count was corrected from 617 to 616.

The key did not change. These fixes improve one clause and one word, and the sense of the letter is otherwise as handed in. The reviewer stated that no second round is needed if these fixes are made, so the card was closed after review 1.

## Sources

- HC Portal record 1248, General, Description and Attachments tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1248 (source/metadata.md). The portal cites https://ecp.ep.liu.se/index.php/histocrypt/article/view/166.
- Picture side: https://api.hcportal.eu/media/3804/conversions/cpc_1913-09-13_HU__HU_Jasz-Arokszalas_jolanka-43_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/3804/cpc_1913-09-13_HU__HU_Jasz-Arokszalas_jolanka-43_pic.jpg (work/hires/).
- Address side: https://api.hcportal.eu/media/3805/conversions/cpc_1913-09-13_HU__HU_Jasz-Arokszalas_jolanka-43_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/3805/cpc_1913-09-13_HU__HU_Jasz-Arokszalas_jolanka-43_adr.jpg (work/hires/).
- Family key: finished cards in this repository, chiefly ciphers/hcp-1216.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-01: no record for this card.
