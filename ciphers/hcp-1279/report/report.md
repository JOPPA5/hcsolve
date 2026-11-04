# HCP 1279 (cpc_1914-04-12_HU__HU_Jasz Arokszalas_jolanka-53): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: the whole visible card is read (647 written signs), with disclosed residual points; independent reviews 1 and 2 both gave the verdict REVISE, and all findings are addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1279 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1279), part of Tobias Schrödel's cryptographic postcard collection (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The portal cites the HistoCrypt article https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 as its source.

The picture side carries the printed title Miért is vagyok szegény ("Why am I poor, after all") with a verse about a poor suitor. The address is in clear: Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás. The card was cancelled at Budapest on 12 April 1914. The letter is in green ink in small invented signs. It fills the message area, runs across the bottom under the address in rows 27 to 29, and has five further rows beside and below the stamp.

The card belongs to the large family of cipher postcards to Jolánka Tóth, signed Feri, several of which are deciphered in this repository (for example HCP 1216, 1251, 1263, 1297 and 1308). Identity of the sender with other cards is not claimed beyond the same name and key. Its theme answers the picture: Feri lacks the money for a home and is impatient to see her.

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, Miért is vagyok szegény (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The key was **transferred unchanged** from finished cards of the family; this is not a new key recovery. The transcription is manual: every row was read sign by sign from enlargements of the original high-resolution scan and recorded as one token per sign. No OCR was used, and the portal supplies no transcription. The script `ciphers/hcp-1279/work/decode.py` checks the hashes of the scans, applies the key to the sign ledger and prints the literal rows.

Where the sign alone did not decide, word sense did, and each such call is listed under Uncertainties. An attempt to separate the green ink from the black postmark by colour failed because the JPEG colour blocks are too coarse, so rows 5 and 6 under the postmark could not be recovered that way.

To reproduce, from the repository root:

```text
python3 -I ciphers/hcp-1279/work/decode.py
```

## Key

Monoalphabetic substitution with invented graphic signs, with steganography: the closing rows are hidden in the stamp box, under the stamp. Register type: MASC + Steganography (changed from MASC on 2026-11-03). The labels are conventional names for handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| long stroke + short tick | d | two strokes | n | plain cross x | u |
| three bars | e | upright cross + | f | chevron | v |
| open loop with descender | g | tall stroke + short tick | h / p | low descender | y |
| loop or curve with dot above | i | cursive loop | o | crossed diagonal with tail | z |
| inverted T | j | left + right bowl | cs | | |

The dot is the working difference between i and o: a loop with no dot is o. The h/p sign has one shape for two letters and was split by word sense in every case: h in hogy, láthassam, ruhát, ha; p in pénz, percz, pedig. Dots or ticks over o and u give ö/ő and ü/ű. Acute marks are mostly not visible and are supplied. The writer writes gy as g+y and usually writes double consonants once.

## Plaintext

Literal decipherment, one line per written row (h stands for the h/p sign; `{a|e}` means undecidable; `{x}` a scribbled-out sign; square brackets a hidden sign restored from sense):

```text
01 nezhogyacsalditüzhely{a|e}t
02 megszerezemadigkelsokat
03 küzdenem[s]okszorelvesz
04 tetüremhogymiertnem
05 [r]endelkezemmárlegalab
06 [{a|e}][n]yihénzelamierre
07 debizomazistenbe
08 hogymegezismegelem
09 egyszerugyörulokéde
10 semhogymarcsak[h]erom
11 {n|h}evalasztelattolhogy
12 viszontlathessemhogy
13 leszakivezereljen
14 eskitöjotanacsokatker
15 jekmertencsakugyakarok
16 elniahogymagakivanja
17 vagyjobbanmondvacsak
18 maganakesszolgalatom
19 nakfogomelnibarmar
20 itvol{x}aazaherczhogy
21 lathassamamiaszüle
22 imetilletiegygyen
23 lörenemküldommegmert
24 masrakelahenzmertmost
25 akaruhat{o|i}scsinaltat
26 nieshedigkeszhenzer
27 dehamagakivanjaakorelkuldömdomelsejenezcsakma
28 gatolfügdeenszeretnekelöbatöltözniezel
29 bezaromsoraimmaradokszeretökedveseferi
stamp: og | csokjai | év{a|e}gyo | kedvesse | feri
```

**Hungarian, normalized (square brackets are editorial):**

Néz[d], hogy a családi tűzhelyet megszerez[z]em, ad[d]ig kel[l] sokat küzdenem. Sokszor elveszte[m] türe[lme]m[et], hogy miért nem rendelkezem már legalább [a/e]n[n]yi pénzel, ami erre [kell], de bízom az Istenbe[n], hogy még ez[t] is megélem egyszer. Úgy örülök, édesem, hogy már csak [h]árom hé[t] (?) választ el attól, hogy viszontláthassam, hogy lesz, aki vezéreljen, és kitő[l] jó tanácsokat kérjek, mert én csak úgy akarok élni, ahogy maga kívánja, vagy jobban mondva csak magának és szolgálatomnak fogom élni. Bár már it[t] volna az a percz, hogy láthassam! Ami a szüleimet illeti, egygyenlőre nem küldöm meg, mert másra kel[l] a pénz, mert most akar[ok] ruhát is csináltatni, és pedig készpénzér[t], de ha maga kívánja, ak[k]or elküldöm elsején. Ez csak magától függ, de én szeretnék előb[b] átöltözni. Ezel bezárom soraim[at], maradok szerető kedvese Feri.

By the stamp: [row lost under the stamp ...]og. Csókjaié[rt] vagyo[k] (?) kedvese Feri.

**English:**

See, until I obtain the family hearth I have to struggle a great deal (free: the card has hogy ... addig, "that I may obtain ..., until then"). I often lose my patience over why I do not yet have at least [so] much money as this needs, but I trust in God that I shall live to see this too one day. I am so glad, my darling, that only three weeks (?) now separate me from seeing you again, so that there will be someone to guide me and someone from whom to ask good advice; for I want to live only as you wish, or better said, I shall live only for you and for my work. If only the moment were already here when I can see you! As for my parents, for the time being I am not sending it, because the money is needed for something else: now I want to have clothes made as well, and for cash at that. But if you wish it, I will send it on the first. That depends only on you, but I would like to get newly dressed first. With this I close my lines and remain your loving sweetheart, Feri.

By the stamp: [row lost] ... For your kisses I am (?) your sweetheart, Feri.

**Slovak:**

Pozrite, kým nezískam rodinný krb, musím veľa bojovať (voľne: na lístku hogy ... addig). Často strácam trpezlivosť, prečo ešte nemám aspoň [toľko] peňazí, koľko je na to treba, ale dôverujem v Boha, že sa aj toho raz dožijem. Tak sa teším, moja drahá, že ma už len tri týždne (?) delia od toho, aby som Vás znova videl, aby bol niekto, kto ma povedie, a od koho si môžem pýtať dobré rady; lebo ja chcem žiť len tak, ako si Vy želáte, alebo lepšie povedané, budem žiť len pre Vás a pre svoju prácu. Kiežby už tu bola tá chvíľa, keď Vás uvidím! Čo sa týka mojich rodičov, zatiaľ to neposielam, lebo peniaze treba na iné: teraz si chcem dať ušiť aj šaty, a to za hotové. Ale ak si to želáte, pošlem to prvého. To závisí len od Vás, ale ja by som sa chcel najprv nanovo obliecť. Týmto končím svoje riadky a zostávam Váš milujúci milý, Feri.

Pri známke: [riadok stratený] ... Za Vaše bozky som (?) Váš milý, Feri.

## Stamp-box message

A check on 2026-11-03 confirmed that the stamp has been lifted. Only a torn strip of its top frame and two small fragments remain. The paper where the stamp sat carries five short rows in the cipher signs, in the same green ink as the letter. They are the rows marked "stamp" above, so the message was already part of the decipherment: **[...]og. Csókjaié[rt] vagyo[k] (?) kedvese Feri.** ("[...] For your kisses I am (?) your sweetheart, Feri.") The first row is still under the remaining strip of the stamp, except for its last two signs. Because the message was hidden under the stamp, the card is typed MASC + Steganography.

## Uncertainties

Conjectural words, marked (?) in the text:

- **Rows 10-11, [h]árom hé[t], "three weeks".** The frame "only X now separates me from seeing you again" is secure and needs a span of time; the words are not. For it: a long rising stroke with a short mark under the postmark fits the h/p sign, and the same family has the phrase on HCP 1297 (1912) and HCP 1263 (1913), which are earlier cards and support the phrase only. Against it: erom is written with e for á (three clear bars) and the final t is dropped. The first sign of row 11 is undecided between n and h, though the reviewer found its shape leans to h. The number three is the weakest point.
- **Stamp, csókjaié[rt] vagyo[k], "for your kisses I am".** This follows the family formula on HCP 1308, Csókjaiért vagyo[k] sírig hű imádója, Feri, which has the same `vagyo` without k at a row end. Here the third sign is a top bar over a two-lobed black blot, so a or e is undecidable. The alternative is vágyó, "longing for your kisses": a separate tick by the last sign would favour it if it is an accent and not stray. The letters are the same in both readings.

Signs physically hidden:

- **Row 3:** an ink blot covers one sign; only s gives sokszor.
- **Row 5:** the first sign lies under the postmark; only r gives rendelkezem.
- **Row 6:** two signs lie under the postmark. annyi and ennyi are both possible, so this restoration is not unique.
- **Stamp row 0:** two signs, o and g or y, stand at the edge of the stamp. The rest of that row, at most one short row, is lost under the stamp.

Sign calls and the writer's forms:

- **Row 1:** Néz[d] is a guess; the last vowel of tűzhelyet has lost its top bar.
- **Row 4:** `tetürem` split as elveszte[m] türe[lme]m[et] is interpretive; a whole syllable is omitted.
- **Rows 6-7:** the [kell] in ami erre [kell] is not on the card, which runs directly `amierre | de`. It is supplied for sense.
- **Row 14:** kitő[l] has the l dropped.
- **Row 18:** in szolgálatomnak the sign after o is an unusual loop read as l from the word, and the o of -tom is merged and weak.
- **Row 20:** one sign is scribbled out where the n of volna belongs. Every other letter of volna az a is on the card; whether the scribble hides an n is not read.
- **Row 22:** the first i is smeared, and the g of the second gy is dark and narrow.
- **Row 25:** the r of akar and of ruhát is written once; the loop before s has no visible dot, normalized is; akar[ok] as first person rests on the end of the sentence.
- **Row 27:** a repeated -dom is dropped as dittography, which is unproven; the writer repeats elsewhere (HCP 1216).
- **Row 28:** függ, de én is divided from a run with the d directly after g.
- **Stamp row 3:** `kedvesse` has a doubled s, for kedvese; its first sign crosses the blue cancel.
- Word division, punctuation and accents are editorial. No native Hungarian reader checked this text.

## Review summary

The reviewer was Claude Opus 5.5 (Anthropic), a separate agent. It ran the command and wrote its own decoders, which agree with the ledger. It checked the ledger against its own enlargements, in bands across the card and at higher zoom at disputed points.

**Round 1, verdict REVISE.** It corrected five signs and two passages, none of which changed the key:

- Row 14 is és kitő[l] jó tanácsokat kérjek, which replaced a forced reading with "kiss".
- Rows 9-10 are édesem, which replaced ennek, semhogy.
- Rows 10-11 lost a forced erőm ne választana. It was replaced first by the frame, then by the conjecture három hét after a stroke under the postmark was found.
- Three further signs changed, in családi, élni and kedvesse.
- Translations and counts were corrected.

**Round 2, verdict REVISE.** It found the fixes correct and accepted három hé[t] as a disclosed conjecture. It raised five more points, all addressed:

- The stamp first reading became vagyo[k], replacing vágyó, after the parallel on HCP 1308 that the solver had missed; vágyó stays as the alternative.
- Row 20 sign 7 is two bars, not three, which removed an unexplained sign.
- Two stamp signs had been described too firmly; one is now undecidable and the other carries a recorded tick.
- "Same writer" became "same family".
- The supplied kell is now disclosed.

The reviewer could not verify the number in row 10, the hidden signs of row 6 and stamp row 0, the scribble in row 20, the dom of row 27 or the split in row 4. In round 2 it checked sample bands (rows 1-4, 14-17, 28-29) and the disputed rows; the other rows were checked at band level in round 1. Neither round found any use of a published solution.

## Credits

- **Earlier cards of the family:** key established with work by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol) and Claude Opus 5.5 (see HCP 1216). No earlier work exists on this number.
- **Claude Opus 5.5, 2026-11-01:** transcription, decipherment, responses to review and this report.
- **Claude Opus 5.5, separate reviewer agent:** independent review, rounds 1 and 2.

## Sources

- HC Portal record 1279, General, Description and Attachments tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1279 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3897/conversions/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-53_pic-large.jpg (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/3898/conversions/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-53_adr-large.jpg (source/address-large.jpg); original at https://api.hcportal.eu/media/3898/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-53_adr.jpg (work/hires/).
- Family cards: ciphers/hcp-1216, 1251, 1263, 1297, 1308.
