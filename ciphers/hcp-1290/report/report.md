# HCP 1290 (cpc_-02-_HU__HU_Jasz Arokszalas_jolanka-92): a travelling man writes to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered, apart from one ink bar in row 6 and the torn end of the text where the stamp was; independent review 1 verdict REVISE, all findings addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1290 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1290), portal name cpc_-02-_HU__HU_Jasz Arokszalas_jolanka-92, part of Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language unknown, sender unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution was met.

The picture side shows a rider with the printed verse "Kis házikóm ablakánál…" and carries no cipher. The whole message is on the address side: 27 rows in invented signs, then further short rows on the part of the card where the stamp was. The stamp has been torn off, exposing writing done under it. The plain address names Jolánka Tóth at Jászárokszállás. The first word of the address is uncertain and nothing here relies on it.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the torn stamp and the postmarks (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards to Jolánka Tóth, several of which are deciphered in this repository (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery. The family key was unchanged, and no new letter value was needed.

No earlier work exists on this number. The transcription and decipherment are by Claude Opus 5.5.

## Method

The transcription is **manual**, not OCR. Every sign was read from enlarged crops of the un-converted high-resolution scan and recorded in a sign ledger (work/ledger.txt): one token per written sign. A short script (work/decode.py) checks the SHA-256 of all four image files, maps the ledger through the key and prints the text:

```text
python3 -I ciphers/hcp-1290/work/decode.py
```

The cipher is a simple monoalphabetic substitution. Hungarian accents are written only sometimes, and word division is not marked. The writer spells loosely: "ly" always appears as "j", double consonants are often single, and letters are sometimes dropped. Word division, accents and restored letters in square brackets are therefore editorial.

The sign for h and p is a near-homograph (tall stroke plus tick), so h and p were separated by word sense. d and n differ in stroke length; the one doubtful case is listed below.

The first draft misread three signs. The independent reviewer found them (see "Review and what changed").

## Key

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark, also 5- and 8-shaped | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c (seen only in cs) | three short strokes | m | gamma/corner | t |
| short tick + long stroke | d | two strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + tick | h / p | low descender | y (in gy) |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

## Plaintext

Literal decipherment, row by row (the two columns are rows 1–14 and 15–27; `{j}` and `{i}` are signs read from sense):

```text
01 szeretetédesjolankámbecsesso      15 csapatbanutazokéselőre
02 raitmegkaptammitnagyon            16 tudomhomejiknapmikor
03 szenköszönökkedvesemhigy          17 kelelutaznomszerdan
04 jeelédenojanjokedveluta           18 egesznapszabadleszek
05 zokmostismintmikor                19 esmajdelmegyekapaszto
06 elkezdtemcsakajoisten[blot]       20 rinehozishogyhagytudjam
07 egyetlenkérésemminelelőb          21 meghogyvanazendragacsila
08 teljesitseaztmagaistudja          22 gomameliktőlo{j}tavolva
09 edesemhogymiazkedvesem            23 gyokdenemsokakozelehoz
10 nempanaszkodniakartamcsak         24 zaasorskezedemostbezaro
11 azértirtamhogynevegyrosz          25 msoraimmertmenem
12 nevenhogyijenritkanirok           26 kelholnapfojtatom
13 majdebbenahonapbangyak            27 {i}stenveledesem
14 rabbanirokmertrendes              stamp: csok | lom | szam | talan | szor | [unread]
```

Row 24 from the final e of "keze" onward, rows 25 to 27 and the stamp rows are in darker ink: the writer changed pen or ink at that point.

### Hungarian (normalized)

Szeretet[t] édes Jolánkám! Becses sorait megkaptam, mit nagyon szé[pe]n köszönök, kedvesem. Higgye el, éde[s], [é]n olyan jókedvvel utazok most is, mint mikor elkezdtem. Csak a jó Isten [tintafolt] egyetlen kérésem minél előbb teljesítse, azt maga is tudja, édesem, hogy mi az, kedvesem. Nem panaszkodni akartam, csak azért írtam, hogy ne vegy[e] rossz néven, hogy ilyen ritkán írok. Majd ebben a hónapban gyakrabban írok, mert rendes csapatban utazok, és előre tudom, ho[gy] melyik nap, mikor kell elutaznom. Szerdán egész nap szabad leszek, és majd elmegyek a Pásztorinéhoz is, hogy hadd tudjam meg, hogy van az én drága csillagom, amelyiktől oly távol vagyok, de nemsoká közelé[be] hozza a sors keze. De most bezárom soraim, mert mennem kell, holnap folytatom. Isten vele, [é]desem.
Csók[o]lom számtalanszor. [rest unreadable]

### English

My beloved sweet Jolánka! I have received your valued lines, for which I thank you very much, my dear. Believe me, my sweet, I am travelling in as good a mood now as when I started. May the good God only [blot] fulfil my one request as soon as possible; you yourself know, my sweet, what it is, my dear. I did not mean to complain; I wrote only so that you would not take it amiss that I write so rarely. This month I will write more often, because I am travelling in a regular crew and I know in advance which day, when, I have to leave. On Wednesday I shall be free all day, and I will also go over to Mrs Pásztori's, so that I may find out how my dear star is, from whom I am so far away, but before long the hand of fate will bring me near her. But now I close my lines because I have to go; I will continue tomorrow. God be with you, my sweet.
I kiss you countless times. [rest unreadable]

### Slovak

Moja milovaná sladká Jolánka! Dostal som Vaše vzácne riadky, za ktoré Vám veľmi pekne ďakujem, drahá. Verte mi, sladká, cestujem teraz v takej dobrej nálade, ako keď som začínal. Len nech dobrý Boh [atramentová škvrna] čo najskôr splní moju jedinú prosbu; Vy sama viete, sladká, čo to je, drahá. Nechcel som sa sťažovať, napísal som len preto, aby ste mi nezazlievali, že píšem tak zriedka. V tomto mesiaci budem písať častejšie, lebo cestujem v riadnej partii a vopred viem, ktorý deň a kedy musím odcestovať. V stredu budem mať celý deň voľno a pôjdem aj k Pásztoriovej, aby som sa dozvedel, ako sa má moja drahá hviezdička, od ktorej som tak ďaleko, ale čoskoro ma ruka osudu privedie do jej blízkosti. Ale teraz končím svoje riadky, lebo musím ísť; zajtra budem pokračovať. S Bohom, sladká.
Bozkávam Vás nespočetnekrát. [zvyšok nečitateľný]

## What remains uncertain

1. **Rows 3–4 `higy|jeeléden`.** Read "Higgye el, …" ("believe me"), the writer's own formula (HCP1308 `higyjeedesem`, HCP1300 `higyje`, HCP1216 `higgyjeel edesem`). The word division is firm. The tail `éden` is a restoration: most likely "éde[s], [é]n olyan…" (one s and one é dropped), which agrees with first-person "utazok". "édesem" with a slip is possible but further from the signs. The sense of the sentence does not depend on this choice.
2. **Row 6, ink bar.** After "jóisten" a heavy horizontal ink bar about three signs wide ends the row. It may be a deletion. Nothing under it can be read, and a small tick above it stays uninterpreted. The sentence runs on without it.
3. **Row 19/20 Pásztorinéhoz.** The name runs over the row break. It is read as a surname from sense (Mrs Pásztori); "pásztor" words were considered and give no sentence. It occurs on no other Jolánka card in this repository.
4. **Stamp area.** The stamp was torn off the card, exposing writing done under it. Five rows read: "csok | lom | szam | talan | szor". A sixth row (`[UNREAD]` in the ledger) shows only a stroke with a foot, a short bar and a low curve, then the torn stamp remnant covers the card. Any closing or signature there is lost, so the sender is unnamed. The dark slanted strokes over the printed FILLÉR are on top of the remnant and taken for postmark, not cipher.
5. **Row 22 blotted sign** between "o" and "t": a retouched sign with an upright, a heavy foot and a top flag. Read `j` ("oj" = oly, as in "ojan", "ijen", "mejik") from sense; a k-shape is not excluded by the pixels. Marked `{j}`.
6. **Row 20 `hagy`** (= hadd). The sign after `ha` is a doubled, retouched g with a dot-like mark to its right, before the y tail. "hagy" is the best reading and fits "hadd tudjam meg", but this sign is not clean.
7. **Row 27 `veledesem`.** Both "vele, [é]desem" and "veled, [é]desem" drop one é and cost the same. Only the formal address on this card ("sorait, maga") favours "vele", which is printed here. The first sign of the row shows no dot and looks like an open loop; `{i}` for "Isten" is from sense.
8. **Row 24 first sign** is heavy, but its body matches the z at the end of row 23 and differs from the clean + of "fojtatom", so z is secure. Rows 23–24 literal "kozelehoz|za"; "közelé[be]" is a normalization.
9. **h/p calls rest on word sense**: p in "megkaptam, panaszkodni, hónapban, nap" (×3 with "holnap"), "csapatban, Pásztori-"; h elsewhere. **d/n**: "drága" (row 21) has two strokes then tick + stroke; the division n + d is from sense. Row 3 "szen": two long strokes with no p tick, so n; normalized "szé[pe]n" as a dropped syllable.
10. **Writer's spelling, normalized**: "szeretet, szen, higy, vegy, rosz, ho mejik" (ho[gy] melyik; ly always as j), "előb, kel, kelelutaznom, menem, soká" ("sokakozele"), "mit" (= amit), "csók lom". Accents are given in the ledger only where seen; the rest are supplied.
11. "rendes csapatban utazok" suggests a work crew or troupe; the writer's trade is not established. The date is unknown: a figure 16 was seen, and the circular postmark at the stamp shows letters including S and E on its left arc, but I could not resolve a place name (the reviewer's …PEST is a hypothesis only). None of this touches the plaintext.

## Review and what changed

A separate Claude Opus 5.5 agent reviewed the first draft. It ran the reproduction command, decoded the ledger with its own script, and checked all 27 rows and the stamp rows sign by sign on its own contrast crops, with doubtful signs enlarged 3 to 7 times. It confirmed the key and the bulk of the reading. Its verdict was **REVISE**, with three major and five minor findings. All were checked against the enlargements and accepted:

- **Row 3:** the last word is `higy`, not `hogy`; the sign has a dot and the body of i. The "unresolved word" `jeeléden` disappeared: the text reads "Higgye el…" ("believe me"), the writer's own formula on sister cards.
- **Row 20:** the supposed `ó` is an i. The text reads "Pásztorinéhoz is, hogy…" ("also to Mrs Pásztori's, so that…") with no gap.
- **Row 24:** the ledger had two m signs but the card has three strokes, one m. The text reads "keze, de most" with nothing supplied. The earlier "[É]de[s]em" was withdrawn from the text and translations.
- **Minor:** the correctness argument was reworded and the count of "hogy" corrected to five; the two row 27 divisions are given evenly; the retouched sign in row 20 `hagy` is disclosed; the unread sixth stamp row is marked in the ledger; the postmark is recorded as unresolved.

The key did not change. The corrections touched three signs and removed two open problems and one forced restoration.
