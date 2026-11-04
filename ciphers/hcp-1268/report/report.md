# HCP 1268 (cpc_1912-01-17_HU__HU_Jasz Arokszalas_jolanka-03): Holes Ferenc to Jolánka Tóth, an invitation for a Sunday

Human solver: Tomáš Pavuk

**Status: deciphered in full (236 written signs, all read, 15 rows and the stamp box). One word rests on word sense (távolban, written ravoban), and one choice stays open (szabók or szabónk). Independent review 1 verdict REVISE; all findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1268 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1268), part of Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The portal links a HistoCrypt article as the collection reference (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166); it was not consulted for this card.

The picture side is a tinted photographic postcard of a young couple among ivy, with the printed Hungarian verse "Hulló falevél…". The address side has the whole message in red ink: fifteen rows of invented signs at the left and four short rows in the printed stamp box at the top right. No stamp is on the box now; the postmark is struck at the box's left edge, so a stamp was most probably stuck over these four rows and later lifted. The stamp-box rows, in the cipher signs, read **Csókolom a kis szájat** ("I kiss the little mouth"); this was re-checked on 2026-11-03. The address is in plain red longhand: **Szépreményű Tóth Jolánka kisasszony saját kezeiben, Jász-Árokszállás, Alszög** ("To the promising Miss Jolánka Tóth, into her own hands"). The town line is partly overwritten. Jászárokszállás is in Hungary. The bottom line, al szög, is read as Alszög, a part of the village.

The postmark reads 912 JAN 17, and the portal file name gives the same date: Wednesday 17 January 1912. A second cancel is partly legible. Which of the two is origin or arrival was not determined.

The card belongs to a large family of cipher postcards to Jolánka Tóth, many of them deciphered in this repository (for example HCP 1216, 1213, 1217, 1218, 1243, 1285, 1301). The sender signs here as Holes Ferenc, a name supported by HCP 1278, 1303 and 1309. HCP 1285, posted three days earlier, is another card of the same weeks.

![Address side with the cipher rows at the left and the stamp box at the top right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, scanned sideways (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

This is a **known, transferred key**, not a new key recovery. The Jolánka family key was taken from the finished cards of this repository. Their earlier work was partly done by an OpenAI GPT solver (GPT-6 Astra, GPT-6.1 Sol) and completed by Claude Opus 5.5. There was no earlier work on this number, and no published solution was used.

The transcription is manual. Claude Opus 5.5 read every sign from 3× to 8× crops of the un-converted original scan and recorded it in a ledger by shape, one token for one written sign. The reading was not blind: the key was known and word sense helped, and each such call is listed below. The family key gives Hungarian across all rows and no sign value had to be invented. Row 7 begins with two plain longhand words or parts of words, meg hi, and then returns to cipher in mid-word.

One command reproduces the text. It checks the hashes of the scans, applies the key to the ledger and prints the literal rows and the normalized text:

```text
python3 -I ciphers/hcp-1268/work/decode.py
```

## Key

Simple monoalphabetic substitution with invented graphic signs, Hungarian, with a hidden part: register type **MASC + Steganography** (set 2026-11-03). Four short cipher rows were written in the stamp box, where the stamp would cover them. The labels below describe handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| open left bowl with hook | g | three short strokes | m | gamma | t |
| long + short stroke | d | two short strokes | n | crossed x | z |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + high tick | h | inverted T | j |
| crossed curve | i | tall stroke + low tick | p | barred bowl + right bowl | cs |

Joined loop and descender give gy. Dots over the crossed x give ü, and two ticks over the loop give ő. The family also has signs for c, u and y, which do not occur as separate clear signs here; the last sign of Ferenc is c or k. Accents are mostly not written.

## Plaintext

Literal decipherment by row. S1–S4 are the stamp box; meg hi is plain writing; braces and (n?) mark uncertain signs.

```text
01 kedvesedesjolankam
02 kivanomtisztaszi
03 vebőlhogylegjob
04 kedvebentalalja
05 soraim.olvastan
06 azegyletbenaszabo(n?)k
07 meg hivojesvasar
08 naplesz{e|a}zishacsak
09 leheebbemenjünk
10 asirjameghogy
11 mibenalapodor
12 megbecsessorait
13 varvamaradokepe
14 dőszivel{a}ravo
15 banholesferen{c|k}
S1 csoko
S2 lom
S3 akis
S4 szajat
```

Hungarian, normalized. Square brackets restore omitted letters; {r=t} marks a written r taken as t; {a} is a struck sign.

**Kedves édes Jolánkám! Kívánom tiszta szív[em]ből, hogy legjob[b] kedvében találja soraim olvastán. Az egyletben a szabók (or: szabónk) meghívój[a], és vasárnap lesz ez is. Hacsak lehe[t], ebbe menjünk. [É]s írja meg, hogy miben ál[l]apodo{r=t}[t] meg. Becses sorait várva maradok epedő szív[v]el {a} {r=t}ávo[l]ban. Holes Ferenc.**

**Stamp box: Csókolom a kis szájat.**

English: **Dear sweet Jolánka! I wish with all my pure heart that on reading my lines you may find yourself in the best of spirits. In the association there is the tailors' invitation (or: our tailor's invitation), and this too will be on Sunday. If it is at all possible, let us go to this one. And write and tell me what you have agreed on. Awaiting your esteemed lines, I remain with a yearning heart in the distance. Ferenc Holes. Stamp box: I kiss the little mouth.**

Slovak: **Milá sladká Jolánka! Z čistého srdca si želám, aby Vás moje riadky zastihli v najlepšej nálade. V spolku je pozvanie krajčírov (alebo: nášho krajčíra), a aj toto bude v nedeľu. Ak to len bude možné, poďme na toto. A napíšte mi, na čom ste sa dohodli. Očakávajúc Vaše vzácne riadky, zostávam s túžiacim srdcom v diaľke. Ferenc Holes. V rámčeku na známku: Bozkávam tie malé ústa.**

The Sunday is not dated. Since the card was posted on a Wednesday, it is 21 January 1912 at the earliest. The event itself is not identified.

## Uncertainties

- **távolban (rows 14–15), word sense only.** The signs are r a v o, b a n. The reading needs r for t, as in row 11 of this card, and an omitted l. The first sign is F-shaped with a smudged stem, so the pixels give r, not t. A small low arc after the o is far too small for this card's l and stays unexplained. A tick over the following a supports long á, but says nothing about r against t. The support is the phrase a távolból, common on this correspondence (HCP 1243, 1244, 1261, 1271, 1276), and the absence of any other Hungarian word. The struck two-bar sign before it is taken as the article a.
- **szabók or szabónk (row 6).** The sign after b is a loop overlaid with heavy strokes, with an arched tail running into a pink blot. No n can be separated from them, though a joined n is possible. Both words parse, and the sense of the clause holds under both.
- **meghívój[a] (row 7).** The j is explained by a dropped final vowel. This is word sense.
- **Row 8 struck sign.** It has three tiers, so it is e-shaped and gives ez is. If the arched top is not part of the sign, it is an overwritten a and gives az is.
- **lehe[t] (row 9).** The t is taken as omitted; it could lie under the blot next to it. Only hacsak lehet makes sense.
- **as for és (row 10).** Two bars, with no third visible. This is word sense.
- **álapodor (row 11).** The last sign is a clear F, so r is written for t. állapodott meg takes its meg from row 12 and is word sense.
- **Holes (row 15).** The tick of the first sign is rather low, which leans to p. H comes from the sister cards. The last sign of Ferenc is heavily overwritten, c or k.
- **Undotted i and spelling.** The i often has no dot. The writer's forms szíveből, legjob and szivel are normalized as shown. In the stamp box the last sign of csoko is a heavily inked loop.
- **Address.** Szépreményű and the bottom line are longhand and were not part of the decipherment.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. It ran the command, made its own crops, wrote its own shape ledger before comparing, and decoded it with its own key table. It disagreed in 4 of 19 rows. It upheld the cipher, key, language and sender. Its eight findings led to these changes:

- **ravoban:** the reviewer proposed távolban, which the first version had left not understood. It was adopted, with word sense disclosed. Two supports were not accepted: the tick does not separate r from t, and the small arc is not counted as an l.
- **Rows 4 and 11:** the sign after b has three bars, not two. The text is kedvében and miben, and the writer made no error in either.
- **Row 8:** the struck sign has three tiers, so the reading is ez is, with az is as the alternative.
- **Rows 6–7:** normalized to meghívój[a] so that the clause parses, with szabók and szabónk as equals.
- **Title and date:** 17 January 1912 was a Wednesday, so it is the posting date, not the Sunday of the card.
- **Row 11:** álapodor is now shown as r for t, not as a simple omission.
- **ő:** two ticks now print as ő in the literal text.
- **Command:** the ledger now names sign shapes and the script applies a key table.

The reviewer could not verify távolban and szabók or szabónk from pixels alone, the hand match with HCP 1278, 1303 and 1309 on scans, the identity of the event, or which cancel is origin or arrival.

## Sources

- HC Portal record 1268, General, Description and Attachments tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1268 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3864/conversions/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/3864/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_pic.jpg.
- Address side: https://api.hcportal.eu/media/3865/conversions/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/3865/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_adr.jpg.
- Family key: ciphers/hcp-1216 and its sister cards in this repository.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-01: no record for this card.
