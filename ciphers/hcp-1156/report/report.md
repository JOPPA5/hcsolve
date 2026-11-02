# HCP 1156 (cpc_1915-12-28_HU_Mezokovesd_HU_Szomolya_szomolya-13): "if not with letters, then write with numbers"

Human solver: Tomáš Pavuk

**Status: deciphered in full (151 of 151 cipher signs, one of them restored under an ink blot); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1156 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1156), from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), which was not consulted, so it is not known whether it discusses this card. No published solution was used.

The card belongs to a series sent from Mezőkövesd to Szomolya in north-east Hungary during the First World War. It is a tinted picture postcard of a young couple on a rustic bench, with no handwriting on the picture side. The whole message is on the address side, dated in clear Mezőkövesd, 1915. XII/28. The postmark reads Mezőkövesd, DEC 28; its year is hidden by the stamp, but the written date and the scan's file name agree on 1915. The address reads: Tek. / Rózsareményű / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács. Printed on the card are Serie Nr. 2963 and a trefoil trademark.

The writer signs Árpád in cipher, the same sign string as on the sister card hcp-1174. Most of the letter is ordinary Hungarian in clear; the salutation, the confidential closing passage and the signature are in digits.

![Address side, carrying the whole message (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no handwriting (source/picture-large.jpg)](../source/picture-large.jpg)

![The digit block from the original scan: the clear verb "lássa" stands in its second line, the blot at the start of its fourth line (work/cipher-block.png)](../work/cipher-block.png)

## Method

The transcription was made by hand from the un-converted original scans at 2x to 4x enlargement; no OCR was used. The family key was taken from the finished sister cards hcp-1174, 1178 and 1179 and applied directly. It gave Kedves igazszívű Margitkám at once, then irhatsz akármit, senki, betüvel, számokkal, bizhatsz bennem and Árpád. A first attempt read `6 1. 5,` as irnál, but the `6` there has no comma, and on enlargement this gave `6` = j, hence irjál, félj and jó. The pair `:1 4.` in úgyse and úgy gave `4.` = gy. Every sign was then run through a script that decodes the card and checks it against the reading.

## Key

Monoalphabetic substitution. Each letter is one sign: a digit, or a digit with a mark, and the comma, dot or colon belongs to the sign. Words are separated only by small gaps. The register label is MASC.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| `0` | o, ó | `3` | d | `6` | j (new) |
| `1` | i, í | `3,` | r | `6,` | n |
| `1.` | a, also unmarked á | `3.` | v | `7` | k |
| `1:` | e | `4` | f | `7,` | s |
| `1'` (high dot) | á | `4,` | g | `7.` | sz |
| `:1` (dots to the left) | ü, ú, ű | `4.` | gy (new) | `8` | m |
| `1,` | b | `5` | h | `8,` | t |
| `2.` | é | `5,` | l | `9` | p |
| | | | | `9,` | z |

The card has 151 cipher signs of 25 kinds. All come from the family table except three values fixed on this card: `6` = j (three words), `4.` = gy (two words), and `4` = f (one word, confirming a value tentative on hcp-1179). None clashes with an earlier value.

## Ciphertext

As on the card; the words in brackets are in clear.

```text
7 1: 3 3. 1: 7,  1 4, 1. 9, 7. 1 3. :1  8 1. 3, 4, 1 8, 7 1' 8 !
1 3, 5 1. 8, 7.  1. 7 1. 3, 8 1 8,  6, 1: 4 2. 5, 6
:1 4. 7, 1: (lássa) 8 1: 4, 7, 1: 6, 7 1 5 1.
1, 1: 8, :1 3. 1: 5, 6, 1: 8  1. 7 7 0 3, 1 3, 6 1. 5,
7. 1. 8 0 7 7 1. 5,  1, 1 9, 5 1. 8, 7.  1, 1: 6, 6, 1: 8
8, 1: 7, 8, 3. 2. 3,  2. 6,  :1 4. 1, 1 9, 0 7
1, 1: 6, 6, 1: 3  8 1 6, 8,  1. 6 0  1 7, 8, 1: 6, 7 2.
1, 1: 6,  (Sokszor csókollak maradok)  5 :1  7 1: 3 3. 1: 7, 1: 3  (1' 3, 9 1' 3)
```

## Plaintext

Hungarian; square brackets mark the enciphered parts. The cipher has no punctuation, so stops inside it are editorial.

[Kedves igazszívű Margitkám]!

Szerencsésen haza érkeztem, nagyon meleg volt és nagy sár. Gyalog jöttem a telepen lejjebb egy darabig, ott ért utól Nagy Lojzi, egy lovas kocsival jött és felvett. Úgy értem aztán haza nyolc órakor. Már a lapokat is megvettem, de nem volt akitől elküldjem. Már az arcképet is berámáztattam, ami othol maradt neked arckép, annak majd magam fogok faragott rámát csinálni. Más különös ujság nincs. Róza nem jött el. Majd ha irsz, sokat irjál mindenről. Most már [irhatsz akármit, ne félj, úgyse] lássa [meg senki. Ha betüvel nem, akkor irjál számokkal. Bizhatsz bennem testvér, én úgy bizok benned, mint a jó istenkében.]

Sokszor csókollak, maradok [hű kedvesed] ([Árpád])

Mezőkövesd, 1915. XII/28.

## English translation

The brackets in both translations are approximate around "lássa meg": the clear verb and its enciphered prefix form one idea.

[Dear true-hearted Margitka]! I got home safely; it was very warm and there was a lot of mud. I came on foot along the settlement and further down for a while, and there Nagy Lojzi caught up with me; he was coming with a horse carriage and picked me up. So I reached home at eight o'clock. I have already bought the postcards too, but there was nobody to send them with. I have also had the portrait framed; as for the portrait for you that stayed at home, I will make a carved frame for it myself. There is no other special news. Róza did not come. When you write, write a lot about everything. Now [you can write anything, do not be afraid, nobody will] see it [anyway. If not with letters, then write with numbers. You can trust me, sister; I trust you as I trust the good Lord.] Many kisses, I remain [your faithful sweetheart] ([Árpád]). Mezőkövesd, 28 December 1915.

"Sister" renders testvér, literally "sibling". It is a plain turn of address here, on what is otherwise a love letter, and is not taken as evidence of family ties.

## Slovak translation

[Milá Margitka úprimného srdca]! Šťastne som došiel domov, bolo veľmi teplo a veľké blato. Išiel som pešo popri osade a kúsok ďalej dolu, tam ma dohonil Nagy Lojzi, išiel konským povozom a vzal ma. Tak som došiel domov o ôsmej. Pohľadnice som už tiež kúpil, ale nebolo po kom ich poslať. Aj portrét som už dal zarámovať; a k portrétu pre teba, ktorý zostal doma, urobím sám vyrezávaný rám. Iné zvláštne novinky nie sú. Róza neprišla. Keď budeš písať, píš veľa o všetkom. Teraz už [môžeš písať čokoľvek, neboj sa, aj tak to nikto] neuvidí. [Ak nie písmenami, tak píš číslami. Môžeš mi veriť, sestra; ja ti verím ako dobrému Pánu Bohu.] Veľakrát ťa bozkávam, zostávam [tvoj verný milý] ([Árpád]). Mezőkövesd, 28. decembra 1915.

## What remains uncertain

Cipher signs:

- The first sign of számokkal is inside an ink blot. A crossbar, a stem and a dot at lower right survive, which fits `7.`. The letter sz is a restoration by word sense, the only one in the cipher part.
- `:1` in úgyse and úgy is read with help from word sense. Elsewhere it has two separate dots; in these two words the mark is one slanted bar or a stroke joined to the stem, read as a dragged colon. It is certainly not a plain `1`.
- The first sign of senki has a hook closed against the crossbar and resembles a 4. The bar runs through the stem as on the other 7s, and "g-enki" is no word.
- `4.` = gy rests on two words and `4` = f on one; neither is attested independently beyond the tentative f on hcp-1179. The words leave no alternative.
- In Margitkám the mark of `1'` is joined to the stem as a short bar; read as á by the name. The writer otherwise spells á with `1.` (akármit, irjál, számokkal), which is his spelling and not a key change.
- Small marks: a tick left of the `5` in irhatsz is taken as a pen mark; the `1,` of benned and the `6,` of -ben are heavily inked, the latter over the printed "Serie"; the comma of `7,` in istenkében is faint.

Open text:

- In Nagy Lojzi the capital N could look like T; the reading is the one that makes a name, and the person is not otherwise known.
- ért seems to be written with a doubled t. utól and othol are as written (colloquial), and berámáz-tattam is broken across a line.
- telepen touches the printed divider, and the sense of "a telepen lejjebb" in the translation is approximate.
- Sentence division is editorial; the writer uses few stops.

## Why the reading is believed correct

The table came from finished sister cards and was not fitted to this text, apart from the three values above. The signs give continuous, grammatical Hungarian that runs through the clear word lássa: the cipher on either side of it has to yield úgyse before and its verbal prefix meg after, and it does. The passage names its own method, "if not with letters, then write with numbers", from inside a block of digits. The name, the recipient, the town and the signature all fit the Mezőkövesd series.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) tried to break the reading. It retyped all the signs from its own crops, decoded them with its own script and the sister tables, and got the same 151 signs and the same text line by line. It checked every sign on enlargements, including all commas and the absence of a comma on the three `6` signs that separates j from n, and read the open text line by line without disagreement. Verdict ACCEPT.

It raised five minor points. None changed a word:

- The counts for the new values were wrong: `4.` occurs twice, not three times, and the claim that each value was fixed by several words was overstated. Corrected.
- The dragged form of `:1` in the two gy words was not disclosed. Added.
- The closed-looking 7 of senki was in the notes but not in the solution. Added.
- Bracket placement in the translations is only approximate. A note was added.
- "Sister" for testvér was kept, with the note above.

Neither solver nor reviewer could verify who Nagy Lojzi, Róza and Árpád were, or the year on the postmark. The Hungarian judgement is an AI reading; no native speaker checked it.

## Reproduction

From the repository root: `python3 -I ciphers/hcp-1156/work/decode.py`. It checks the SHA-256 of the four scans, decodes every sign and prints the full text and address. The open text is hard-coded in the script, so it proves only the cipher part.
