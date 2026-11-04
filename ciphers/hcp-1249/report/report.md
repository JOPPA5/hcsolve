# HCP 1249: Feri invites Jolánka Tóth to a July ball

Human solver: Tomáš Pavuk

**Status: all 602 signs read with the transferred family key; two isolated words (rows 1 and 23) keep an unresolved form, and one row under the stamp is tentative. Independent review 1 verdict REVISE; all findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1249 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1249), portal name cpc_1914-03-25_HU__HU_Jasz Arokszalas_jolanka-51, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The date 1914-03-25 is taken from the portal's file name.

The picture side carries only printed verse. The cipher text is on the address side: 28 rows, plus 7 more rows written under the stamp, which has since been lifted. The plain address reads Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás. The postmark shows BU… and 914 MÁR, which fits the portal's date. The card is signed Feri twice.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the family of cipher postcards addressed to Jolánka Tóth, several of which are deciphered in this repository (for example HCP 1216, 1212, 1213, 1217, 1218, 1243 and 1301). Whether this Feri is the Feri of those cards is not proved, though key, hand style, addressee and the closing formula agree. No published solution of this card was found or used.

## Method

The key was **transferred unchanged** from the finished family cards, so this is a reading with a known key, not a new key recovery. Earlier work on those family cards was done by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) and completed by Claude Opus 5.5; no earlier work exists on this number.

The transcription is manual. Claude Opus 5.5 read every row sign by sign from enlarged crops of the un-converted high-resolution scan and recorded it in a ledger (work/ledger.txt). The rows under the stamp were read in the blue channel, which suppresses the blue printed triangle. A short script checks the source hashes and decodes the ledger:

```sh
python3 -I ciphers/hcp-1249/work/decode.py
```

The text is Hungarian, without reliable word spacing; digits are plain.

## Key

Simple monoalphabetic substitution with invented graphic signs. The labels are conventional names for handwritten shapes.

Cipher type (updated 2026-11-03): **MASC + Steganography**. Besides the 28 main rows, the writer hid a seven-row message in the same cipher signs in the stamp box, under the stamp, which has since been lifted. That message is read in full below (rows S1 to S7, "Under the stamp"); a fresh check of the stamp box on 2026-11-03 confirmed the reading and found no plain-language writing there.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | S shape, short | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three strokes | m | gamma (Γ) | t |
| long + short stroke, crossed or joined | d | two equal strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + tick | h / p | low descender | y |
| hooked S with long descender | g | dotted loop | i | cross with long tail | z |
| inverted T | j | opposed bowls | cs | | |

A tick over the bars gives é; ticks or dots on o and u give ö, ő, ü, ű. Most other accents are not written. h and p share one sign, split by word sense: p occurs only in percz. The writer's short S and hooked S overlap, so k and g are also partly taken from the word.

## Plaintext

Literal decipherment, row by row; S1 to S7 are the rows under the stamp. `[x]` means read through damage.

```text
01 meretségmertnemugyvan          S1 csokjai[t]
02 minarokszalasbahogyha          S2 alig[v][a]
03 nincsegylanynakismerős         S3 [r][o][m][h][i][d][d]
04 selelülhe[t]reggeligés         S4 edeseb
05 amiatestvéreitillet            S5 anal[a]
06 azoknaksemkifogasokel          S6 percz
07 lén[e]merttelégtekin           S7 n[é]lferi
08 téjesmulatsagbahivom
09 aholnemmindenkifor
10 d[u]lnatmeskülömbenis
11 mégleszidőmegondolas
12 rametcsakjulius24és25
13 énleszkedvesemene[r]anem
14 isakarokgondolnihogy
15 nemjönelmerthamarmeg
16 hozomazanyagialdozatot
17 mulatisszetnékkedvem
18 remutné[{s|k}]azmarne[m]iskel
19 irnomhogy[o]terzemjol
20 magamaholmaga[i][s]otvan
21 kedvesemremélemhogy
22 mégarokszálasbavi
23 szontfukegybiztosat
24 nemirhatokmertnekem
25 mindenmegforditva
26 téljesülmiténisalig
27 varokezelbezaromsoraim
28 maradoksirighűkedveseferi
```

### Hungarian (normalized)

Square brackets mark supplied or unresolved text.

[Meretség], mert nem úgy van, mint Árokszállásba, hogy ha nincs egy lánynak ismerőse, [l]elülhet reggelig, és ami a testvéreit illeti, azoknak sem kifogások ellene, mert elég tekintélyes mulatságba hívom, ahol nem mindenki fordul[h]at me[g]. Különben is még lesz idő meg[g]ondolásra, me[r]t csak július 24 és 25-én lesz. Kedvesem, én er[r]e nem is akarok gondolni, hogy nem jön el, mert hamar meghozom az anyagi áldozatot. Mulat[n]i is sze[re]tnék kedvemre, mu[la]tnék (or mut[at]nék), az már nem is kel[l] írnom, hogy ott érzem jól magam, ahol maga is ot[t] van. Kedvesem, remélem, hogy még Árokszállásba viszont[...]uk. Egy biztosat nem írhatok, mert nekem minden megfordítva teljesül, mit én is alig várok. Ezzel bezárom soraim. Maradok sírig hű kedvese Feri.

Under the stamp: Csókjait alig várom, hidd, édesebb annál a percznél. Feri.

### English

[Meretség: unresolved, perhaps "a daring thing"], because it is not as in Árokszállás, where if a girl has no acquaintance she can sit there until morning; and as for your brothers and sisters, they too [can have] no objections to it, because I am inviting you to quite a respectable ball, where not everybody can turn up. Besides, there will still be time to think it over, because it will only be on July 24 and 25. My dear, I do not even want to think that you will not come, because I will soon make the financial sacrifice. I would like to enjoy myself to my heart's content too, I would make merry (or: I would show [it]); there is no need for me to write that I feel well where you are too. My dear, I hope that we will still [see each other?] again in Árokszállás. I cannot write anything certain, because for me everything comes true the other way round, which I too can hardly wait for. With this I close my lines. I remain, faithful unto the grave, your sweetheart Feri.

Under the stamp: I can hardly wait for your kisses; believe me, [they are] sweeter than that moment. Feri.

### Slovak

[Meretség: nevyriešené, azda „odvážna vec"], lebo to nie je ako v Árokszállási, kde ak dievča nemá známeho, môže tam presedieť do rána; a čo sa týka vašich súrodencov, ani tí proti tomu [nemôžu mať] námietky, lebo vás pozývam na dosť úctyhodnú zábavu, kam sa nedostane hocikto. Okrem toho bude ešte čas na rozmyslenie, lebo to bude až 24. a 25. júla. Drahá moja, ani nechcem myslieť na to, že neprídete, lebo tú finančnú obeť čoskoro prinesiem. Aj ja by som sa rád zabavil do sýtosti, zabával by som sa (alebo: ukázal by som [to]); to už ani nemusím písať, že sa dobre cítim tam, kde ste aj vy. Drahá moja, dúfam, že sa ešte v Árokszállási [uvidíme?]. Nič isté nemôžem napísať, lebo mne sa všetko plní naopak, čoho sa aj ja sotva dočkám. Týmto končím svoje riadky. Ostávam váš do hrobu verný milý Feri.

Pod známkou: Sotva sa dočkám vašich bozkov; ver mi, [sú] sladšie než tá chvíľa. Feri.

## What remains uncertain

- **Row 1 `meretség`.** All signs are clear, but no word of this form is known. merészség ("daring") is a guess.
- **Row 23 `viszontfuk`.** The signs are clear. viszontlátjuk ("we see again") is the obvious sense, but it needs dropped letters.
- **Stamp row S3.** The weakest place: the stamp gum removed ink, and hidd is chosen for sense. The vowel of S7 is also read through damage.
- **Rows 3–4.** The reading rests on word sense: k rather than g in lánynak, s doubled across the row break, and one surplus l in `lelülhet`, which stands for elülhet or leülhet.
- **Rows 9–10.** `fordulnat mes` is read fordul[h]at me[g] with two writer's slips (n for h, s for g). fordulna[t] me[g] is an alternative with the same sense.
- **Row 18.** The blotted sign is s or k; mu[la]tnék and mut[at]nék are both possible.
- **Row 26.** mit has no stated antecedent, so the link of that clause is loose.
- **Blots.** Rows 7, 13, 19 and 20 have blotted signs, read from context. A double tick on row 7 is unexplained.
- **Date.** 24 and 25 July 1914 were a Friday and a Saturday; this neither supports nor contradicts the text.

## Why the reading is believed

The unchanged family key turns all 602 signs into Hungarian with no new value. The text brings its own checks: Árokszállás twice, matching the address; the digits 24 és 25; anyagi áldozat, tekintélyes mulatság; and the formula sírig hű kedvese Feri, also found on HCP 1216. Repeated words decode identically (hogy ×4, nem ×6, kedvesem ×2, alig ×2). The content is coherent: he invites her to a respectable ball in July, answers the family's likely objections and offers to bear the cost.

## Review and what changed

A separate Claude Opus 5.5 agent re-ran the command, decoded the ledger with its own script typed from the HCP 1216 key (all 35 rows matched), and checked all rows against the scan. It accepted the key and the cipher type, and returned REVISE for four changed signs and one word division:

- Row 2 end is ha, not na: the sign's first stroke is much longer than the second.
- Rows 3–4 now read ha nincs egy lánynak ismerőse, elülhet reggelig, replacing a forced sense.
- Rows 9–10 were wrongly divided: mindenki fordulhat meg replaces an unresolved passage, with the slips disclosed.
- Stamp row S6 is percz ("moment"), not an unresolved nercz, and S7's vowel is now read é.
- Row 26 is mit, not mot: the dot is present.
- Minor: one t removed in row 20 (603 signs became 602), a tick added in row 22, the vowel of row 24 settled as a, both options given in row 18, word counts corrected, and the date check made.

The solver checked each place on the enlargements and accepted all findings, adding the alternative fordulna[t] for rows 9–10. The key did not change. The reviewer could not read rows 1 and 23 either, and could not settle S3 or the vowel of S7.
