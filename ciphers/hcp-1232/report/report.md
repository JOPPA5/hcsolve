# HCP 1232 (cpc_--24_HU__HU_Jasz Arokszalas_jolanka-89): Feri to Jolánka Tóth at Corpus Christi

Human solver: Tomáš Pavuk

**Status: deciphered in full, no unread word; a few damaged signs rest on word sense and are listed below. Independent review 1 verdict REVISE; findings addressed.** Report dated 2026-11-02. Solved by Claude Opus 5.5; there was no earlier work on this number.

## Origin and context

The cryptogram is record 1232 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1232), part of Tobias Schrödel's cryptographic postcard collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The portal links a Histocrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166); it was not opened, and no published solution of this card was found or used.

The picture side carries only the publisher's printed poem and the caption Aranyeső (Golden rain), with no handwriting. The address side is plain script in red ink: **Szépreményű Tóth Jolánka úrhölgynek, Jász Árokszállás** ("To the promising young lady Jolánka Tóth, Jászárokszállás", a town in Hungary). The whole left half of that side is filled with 23 rows of cipher, and five more short rows stand in the stamp field at top right.

Two postmarks can be seen: a fragment ending PEST, and an Árokszállás postmark in which the number 24 is clear. It is not claimed as the day, and month and year are not readable, so the year is unknown. The mention of Úrnap (Corpus Christi) points to late May or June.

The card belongs to the family of Hungarian cipher postcards to Jolánka Tóth, many of them signed Feri. It is not proved that this Feri is the Feri of HCP 1216, though the signature and the key agree.

![Address side: cipher rows at left, stamp-field rows at top right, plain address, postmarks (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: printed text only (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The opening was recognised as the Jolánka family. The first word, "Szer", is written in plain script and runs straight into the cipher ("Szeretet..."), a useful confirmation. The key was **transferred unchanged** from the finished card HCP 1216 and tested again on every sign of this card; this is not a new key recovery.

The transcription is **manual**: every row was read sign by sign from enlarged crops of the un-converted high-resolution scan. The signs are invented shapes that cannot be typed, so the transcription (work/ledger.txt) labels each one, mostly by the letter it stands for. The one command `python3 -I ciphers/hcp-1232/work/decode.py` checks the hashes of the images and prints the literal rows and the normalized text from that ledger; it reproduces the transcription and is not a separate application of a key to raw ciphertext.

The writer's spelling is close to speech, and he drops letters. Accents are mostly not written and were supplied in the normalized text.

## Key

Simple monoalphabetic substitution with invented graphic signs. The labels describe the handwritten shapes.

| Shape | Plain | Shape | Plain |
|---|---|---|---|
| two bars | a | three short strokes | m |
| six | b | two short strokes | n |
| left bowl | c | cursive loop | o (dots over it: ö) |
| tick + long stroke | d | F-sign | r |
| three bars | e | right bowl | s |
| upright cross | f | gamma | t |
| open loop with descender | g | plain cross | u |
| tall stroke + short | h / p | chevron | v |
| dotted crossed curve | i | low descender | y |
| inverted T | j | crossed diagonal | z |
| section mark (S or 8 form) | k | wave | l |

h and p are a near-homograph and are separated by word sense only. Joined sz and cs are not used as ligatures here: c and s are two separate bowls.

## Plaintext

Literal decipherment, row by row; {x} is a sign restored, smeared or overinked.

```text
01 Szeretetedesjolankam          13 hiany{n}emtudomhogymelik
02 kivanomhogyalegjobb           14 szomb{a}tonkapomkiaköny
03 kedvebenta{l}jasoraim         15 vetde[blot]arokszalasracsagak
04 hogymulaturna{p}jan           16 kormegyekhamagaedesem
05 remele{m}jolendol             17 hivhazaarokszalasba
06 goztammittudjakcsinal         18 tiszeletetetmegkap
07 nilegalabbtelikaval           19 tammelyetköszönök
08 isazidömegmos{t}aztis         20 örülökhogyszesenfo
09 el{v}esztemamiedigszora       21 gadtaaszobaaszonyom
10 kozasomvoltajagerjo           22 ezel{b}ez{a}romsoraim
11 z{s}ihazamegymoczarhoz        23 maradokimadjaferi
12 dolgoznimernagyamuka
stamp: {c}sokolom szamta lanszor imdoja feri
```

**Hungarian (normalized):** Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Hogy mulat Úrnapján? Remélem, jól. Én dolgoztam, mit tudjak csinálni, legalább telik avval is az időm. Meg most azt is elvesztem, ami eddig szórakozásom volt: a Jáger Józsi hazamegy Móczárhoz dolgozni, mer nagy a munkahiány. Nem tudom, melyik szombaton kapom ki a könyvet, de Árokszállásra csak akkor megyek, ha maga, édesem, hív haza Árokszállásba. Tiszteletét megkaptam, melyet köszönök. Örülök, hogy szívesen fogadta a szobaasszonyom. Ezzel bezárom soraim. Maradok imádója Feri.

In the stamp field: Csókolom számtalanszor. Imádója Feri.

**English:** My beloved sweet Jolánka! I wish that my lines find you in the best of spirits. How are you enjoying yourself on Corpus Christi Day? Well, I hope. I worked, for what else could I do; at least that too passes my time. And now I lose even what has been my amusement until now: Józsi Jáger is going home to work for Móczár, because work is very scarce. I do not know on which Saturday I will get my [work] book out, but I will go to Árokszállás only if you, my sweet, call me home to Árokszállás. I have received your respects, for which I thank you. I am glad that my landlady received [it/you] gladly. With this I close my lines. I remain your admirer, Feri.

In the stamp field: I kiss you countless times. Your admirer, Feri.

**Slovak:** Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Ako sa zabávate na Božie telo? Dúfam, že dobre. Ja som pracoval, čo iné mám robiť, aspoň aj tým mi ubieha čas. A teraz strácam aj to, čo bolo doteraz mojou zábavou: Józsi Jáger ide domov pracovať k Móczárovi, lebo je veľký nedostatok práce. Neviem, ktorú sobotu dostanem knižku, ale do Árokszállásu pôjdem len vtedy, ak ma Vy, moja drahá, zavoláte domov do Árokszállásu. Vaše pozdravy som dostal, za čo ďakujem. Teším sa, že [to/Vás] moja bytná prijala ochotne. Týmto končím svoje riadky. Zostávam Váš ctiteľ Feri.

V poli známky: Bozkávam Vás nespočetnekrát. Váš ctiteľ Feri.

## Uncertainties

No word is unread. These points remain.

**Signs resting on word sense:**

- Row 3 {l}: partly under the postmark; a wave shows under the ring. `talja` stands for találja (writer omitted lá).
- Row 4 {p}: two smeared strokes; compatible with p, which alone gives Úrnapján.
- Row 5 {m}: third stroke stands where the postmark ring crosses the row.
- Row 8 {t}: gamma with an ink pool (most).
- Row 9 {v}: chevron with an extra crossing stroke, possibly a correction.
- Row 11 {s}: overinked, looks overwritten; the name form Józsi is therefore an interpretation.
- Row 13 {n}: blot plus one stroke (nem).
- Row 14 {a}: looks closer to three bars; szombaton requires a.
- Row 15: a blot with no readable sign, then the a of Árokszállásra, possibly a false start or a corrected letter. `csagak` has the form of g where csak needs k.
- Row 22 {b}: heavily overinked, with a hollow foot; {a} after z is in a pink smear. The formula fixes both.
- Stamp {c}: the bowl has an inner curl like a six. The t of számta is imperfect, and a short final bar in S3 and small marks are treated as punctuation.

**Interpretations:**

- `szesen` (row 20) is clear in the signs, normalized as szívesen; szépen is the alternative. The object of fogadta is not stated.
- `muka` omits the n of munka (it is also a colloquial word for toil).
- h/p, and d/n, were separated by word sense and on enlarged crops respectively.
- `meg most` could be még most. `mer` is the spoken form of mert and is kept.
- The book of "a könyvet" is taken as a work or service book; the card does not say. Józsi Jáger and Móczár are not identified.

## Review and what changed

An independent Claude Opus 5.5 reviewer reran the command, compared it with its own script, read all 28 rows on its own crops and checked each restoration. It confirmed the type, key, row count and nearly all of the reading, and gave the verdict REVISE with ten findings.

- **Major, row 22.** The handover read a chevron v and left the sentence as "az elbe ... várom soraim", unresolved. The reviewer showed that the sign is the crossed diagonal z, so the word is bezárom and the sentence is the family's closing formula, Ezzel bezárom soraim, known from cards such as HCP 1235 and 1249. This reading is the reviewer's.
- **Major, translation.** Munkahiány means a lack of work, not of workers; English and Slovak were corrected.
- **Minor readings.** Row 5 is remélem with a third stroke under the ring, not `remelen`; row 14 has dots over the o of könyvet.
- **Minor disclosure.** Three more damaged signs were listed (rows 9 and 14, stamp S1), the postmark 24 was reported, the fogadta gloss made consistent, a spelling note extended, and it was stated plainly what the reproduction command does.

One detail of the review was not followed. It read the first sign of row 22 as two bars, giving `azel`. On a closer crop the sign has three strokes, with the two-bar a of row 21 directly above for comparison, so it is e and the literal is `ezel`, the same form as on the sister cards. The solver's handover ledger had the same error.

![Row 22: e z e l, overinked b, e, z, smeared a, r o m, s o r a i m (work/crops/row22.png)](../work/crops/row22.png)

![Comparison from the review: the disputed sign, z of rows 21 and 10, and for contrast (right) the v of rows 7 and 9 (review/work/crops/cmp.png)](../review/work/crops/cmp.png)
