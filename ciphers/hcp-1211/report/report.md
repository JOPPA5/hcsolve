# HCP 1211 (cpc_1912-02-10_HU__HU_Jasz Arokszalas_jolanka-04): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (322 written signs in 17 rows), with one uncertain word at an ink blot; independent review 1 verdict REVISE, findings addressed, sense of the card unchanged except for one false word removed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1211 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1211), portal name cpc_1912-02-10_HU__HU_Jasz Arokszalas_jolanka-04, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side shows a printed scene of a courting couple with roses, framed on a dark ground with swallows. It has no writing. The whole message is on the address side, in pink ink: 17 rows of invented signs to the left of the printed divider, the last row running on across it. The word "is" stands in plain Latin letters in the middle of the cipher. A short plain note is hidden under the place of the stamp, which is now gone, and the address is in plain hand.

The address reads **Szépreményű Tóth Jolánka kisaszonynak sz. r. t. Jász-Árokszállás, Alszög**: to the hopeful Miss Jolánka Tóth (the writer spells kisasszonynak with one s). The abbreviation sz. r. t. is reported as seen and not expanded. Alszög is taken as a part of Jászárokszállás, which was not verified.

The first postmark shows ...ÁROKSZÁ..., the year remains 912, a month beginning with F and the day 10, which agrees with the date 1912-02-10 in the portal file name. A second mark begins GYÖN..., possibly Gyöngyös, which remains a guess.

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth in Jászárokszállás, several of which are deciphered in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key. This card was therefore read with a **known, transferred key**, with one sign form that differs (see Key). No reading of this card was supplied or consulted, and no published solution was found.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the 17 cipher rows, the postmarks and the plain note under the stamp (source/address-large.jpg)](../source/address-large.jpg)

## Method

All work on this number was done by Claude Opus 5.5 on 2026-11-02. The transcription is **manual**: every row was read sign by sign from enlarged crops of the un-converted scan and recorded in a sign ledger, one token per written sign. No OCR was used. It was not blind, because the family key was known and the reading used word sense where signs were doubtful; those places are listed under Uncertainties.

A script then checks the hashes of the images, decodes the 322 tokens with the key and prints the literal rows. The first readings of some places were corrected on the enlargements. For example, row 6 first looked like "abból hogy" and is "a boldogságtól", and "neher vadjon" is "ne her-vadjon", divided across the row break.

The writer divides words across rows with a hyphen stroke. In the literal text the h/p sign is always shown as h.

## Key

Cipher type (register): **MASC + Steganography** (updated 2026-11-03): a Hungarian simple monoalphabetic substitution with invented graphic signs, plus a plain-Hungarian message hidden in the stamp box under the stamp. The names below are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark with dot below | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma | t |
| short + long stroke joined | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short tick | h / p | crossed diagonal | z |
| C-shape | g (this card) | dotted crossed curve | i | inverted T | j |

Joined forms: C + y = gy, two strokes + y = ny, wave + y = ly. Accents are marks over the base sign and are not used consistently.

**The g sign is the one difference from the family tables**, which list a left bowl as c and an open loop with a descender as g. Here a large C-shape serves as g in meg (three times), alig, boldogság, leg-, virága and joined gy. Reading it as c would give no words. The reviewer confirmed this independently.

## Plaintext

Literal decipherment by written row, as printed by the reproduction command. {blot} is an ink blot and {O} an over-inked ring left out of the reading. [is] is the word in plain Latin letters.

```text
01 édesegyetlenremé
02 nyemsoraitköszönet
03 telmegkahtammelyavar
04 vavartidöabelolmeg
05 érkezetédesjolánkam
06 aboldogsagtolalig
07 tudokválaszolai
08 széhszemébennyilik
09 énreszemrealeg{O}szebb
10 rozsaésszivébenane
11 felejcs[is]csaknekemvirul
12 {blot}onszivevirágaésneher
13 vadjonelsohalegyen
14 asorbarmilymosto
15 haazenedesjolánkámat
16 elfeledninembirnám
17 sohaistenveleédesemaviszolatasraferi
```

Normalized Hungarian (accents, capitals, punctuation and word division are editorial; square brackets mark letters the writer omitted):

**Édes egyetlen reményem! Sorait köszönettel megkaptam, mely a várva várt időn belől megérkezet[t]. Édes Jolánkám, a boldogságtól alig tudok válaszolni. Szép szemében nyílik én részemre a legszebb rózsa, és szívében a nefelejcs is csak nekem virul. Ön szíve virága, és ne hervadjon el soha, legyen a sor[s] bár mily mostoha, az én édes Jolánkámat elfeledni nem bírnám soha. Isten vele, édesem, a visz[ont]látásra! Feri**

Under the stamp, plain hand, rotated: **Csókolom a csókra való kis száját. Feri**

Stamp-box audit 2026-11-03: the stamp is lifted; the box holds four lines in plain Hungarian cursive (literal: csokolom a / csokro va- / ló kis sza / ját Feri), no cipher signs. Everything is read; the o-for-a in csókra and the j at the start of the last line rest on shape plus word sense.

English translation: **My sweet only hope! I received your lines with thanks; they arrived within the long-awaited time. My sweet Jolánka, I can hardly answer for happiness. In your beautiful eyes the loveliest rose blooms for me, and in your heart even the forget-me-not blooms only for me. The flower of your heart, may it never wither, however cruel fate may be, I could never forget my sweet Jolánka. Farewell, my darling, until we meet again! Feri**

Under the stamp: **I kiss your little mouth, made for kissing. Feri**

Slovak translation: **Moja sladká jediná nádej! Vaše riadky som s vďakou dostal, prišli v očakávanom čase. Sladká moja Jolánka, od šťastia sotva dokážem odpovedať. Vo Vašich krásnych očiach pre mňa kvitne najkrajšia ruža a vo Vašom srdci aj nezábudka kvitne len pre mňa. Kvet Vášho srdca, nech nikdy nezvädne, nech je osud akokoľvek krutý, svoju sladkú Jolánku by som nikdy nedokázal zabudnúť. S Bohom, drahá, dovidenia! Feri**

Pod známkou: **Bozkávam Vaše malé ústa stvorené na bozkávanie. Feri**

Notes on the reading:

- **The close is verse-like:** soha, mostoha and soha rhyme.
- **belől** is the writer's form of belül ("within").
- **sor** may stand for sors ("fate"), but sor can itself mean "lot", so the bracketed s is optional.
- **Isten vele** ("God be with you") and **a viszontlátásra** ("until we meet again") are the usual close; the writer left out the nt of viszont.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1211/work/decode.py
```

The script checks the SHA-256 of the four image files, decodes the 322 tokens of work/ledger.txt with the key, prints the 17 literal rows, and prints the editorial text from work/normalized.txt. It does not read the images: the ledger itself is a manual reading of the pixels. In review a second, independent decoder with its own key table gave the same values for all tokens.

## Uncertainties

- **Row 12, first word (the weakest point).** An ink blot stands in the first-sign position, followed by a plain cursive o and an n. The o is on the card; its two dots are supplied, and they are absent, not hidden. The word is read Ön. Neither solver nor reviewer could tell from the pixels whether the blot covers a letter in front of on. The phrase Ön szíve virága is also loose; "[You are] the flower of the heart" is possible.
- **Two emendations, rows 4 and 7.** The card literally has idő a belől and válaszolai with two clear horizontal bars (a) where the sense needs n. Both are normalized with n, as the same slip of horizontal for vertical strokes. They rest on word sense.
- **Word-sense calls.** h against p is decided by word sense (p in megkaptam and szép; h in hervadjon, soha and mostoha). d against n differ by the joined short + long form, and d in hervadjon and elfeledni also rests on word sense. u and z are hard to tell apart by shape on this card, and the two u tokens (tudok, virul) rest on word sense.
- **The g value** rests on the words listed under Key; no sign-by-sign comparison with the sister cards was made.
- **Over-inked signs.** Row 9 has a filled ring between leg and szebb, left out as a false start or correction. Row 6 has two filled g, row 11 a blot on the n of nekem, row 12 a blot on the á of virága, and the f of elfeledni in row 16 is a star-shaped blot under the printed "Série 2285". The u of tudok and the z of viszo- are over-inked. All are read by shape plus word sense.
- **Small marks.** A separate short bar above the m of meg in row 3 is not read as a letter. The last sign of Feri is thick, with its dot at the upper right.
- **Writer's spellings.** érkezet with one t, sor, viszolátásra, and accents mostly absent. Accents in the literal text are as seen, but were not audited one by one in review.
- **Plain text.** The second line under the stamp is cramped, and the a of csókra looks like o. The address abbreviation is unexplained.
- **Date and sender.** The postmarks are only partly legible. The sender signs Feri, as on the family cards; no further identification is claimed.
- **Prior publication.** The portal attaches no solution, and the AI Decipherment Register had no record for this card on 2026-11-02. The linked HistoCrypt article was not read for this card.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, wrote its own decoder and alignment, read all 17 rows on its own crops, and studied the critical places at stronger zoom. It confirmed the language, the key, the C-shaped g, the two emendations and the plain writing. Its seven findings were all accepted and fixed:

- **False word removed (major).** The earlier normalized text had "mostoha, ha az én", using the same two signs twice. There is only one ha, the end of mosto-ha. Removing it cleared an apparent grammar problem and improved the translation: "since" and "lebo" were dropped.
- **Row 15, Jolánkámat.** One sign was corrected from three bars to two bars, so the card gives a, not e. The solver also marked the acute over that sign.
- **Row 7.** The last sign does have its dot, so the i is better supported than first stated.
- **Row 12.** The wording now says exactly what is supplied (the dots) and what is open (a letter under the blot).
- **Address.** Corrected to kisaszonynak [sic] sz. r. t.
- **u against z.** Added to the word-sense calls.
- **Date.** The postmark note was extended.

No key value changed. The ledger keeps 322 signs, and the reproduction command still works.

## Sources

- HC Portal record 1211, General, Description and Attachments tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1211 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3693/conversions/cpc_1912-02-10_HU__HU_Jasz-Arokszalas_jolanka-04_pic-large.jpg (source/picture-large.jpg), and the original https://api.hcportal.eu/media/3693/cpc_1912-02-10_HU__HU_Jasz-Arokszalas_jolanka-04_pic.jpg.
- Address side: https://api.hcportal.eu/media/3694/conversions/cpc_1912-02-10_HU__HU_Jasz-Arokszalas_jolanka-04_adr-large.jpg (source/address-large.jpg), and the original https://api.hcportal.eu/media/3694/cpc_1912-02-10_HU__HU_Jasz-Arokszalas_jolanka-04_adr.jpg, used for reading.
- Family key: earlier Jolánka family cards in this repository, chiefly ciphers/hcp-1216 and ciphers/hcp-1212.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-02.
