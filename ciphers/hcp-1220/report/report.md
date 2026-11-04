# HCP 1220: Feri to Jolánka Tóth, thanks for her letter and going home

Human solver: Tomáš Pavuk

**Status: deciphered in full (176 of 176 letter signs, plus one blotted mark with no value); independent review 1 verdict ACCEPT, no letter value changed. One short plain-script note under the stamp is partly read from a parallel, and this is marked below.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1220 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1220), portal name cpc_-12-27_HU__HU_Jasz Arokszalas_jolanka-97, from Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side shows a hussar and a girl and carries only the printed number 2541 and a small publisher's mark. All writing is on the address side. In plain script it is addressed to **Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás** ("To the promising young lady Jolánka Tóth, Jászárokszállás", Hungary). Twelve rows of invented signs fill the left half of the card. The stamp was removed from the upper right corner and uncovers a hidden short note in plain script, followed by the name Feri in cipher signs. A pencil line along the top edge, "Jász Árokszállás Hungary", is a later note in another hand and is not part of the message.

The receiving cancel at the top shows `DEC` and `27` when turned round, which agrees with the -12-27 in the portal's file name. The year could not be read, so the card is dated 27 December, year unknown.

The card belongs to the family of cipher postcards to Jolánka Tóth, written in Hungarian by her sweetheart Feri. The key was transferred unchanged from cards already finished in this repository (HCP 1216, which has the fullest legend, and 1212, 1213, 1217, 1218, 1243, 1301). Those cards were solved by an OpenAI GPT solver and completed by Claude Opus 5.5. This card was therefore read with a **known, transferred key**. It is not a new key recovery. No reading of this particular card was supplied or consulted, and no published solution is known.

![Address side: the twelve cipher rows at the left, the plain address at the right, the note in the bare stamp box at the upper right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: a hussar and a girl, with no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is **manual**, not OCR, and the reader knew the key. Each sign was read from enlarged crops of the un-converted portal original and recorded in a hand-made ledger, one token per written sign (work/ledger.txt). A short script, work/decode.py, checks the hashes of the scans, decodes the ledger and prints the result:

```text
python3 -I ciphers/hcp-1220/work/decode.py
```

The ledger holds 177 written signs in 13 rows: 176 letter signs and one blotted raised mark with no value. Every sign fell into a sign class of the family. No new letter value was needed.

The note in the stamp box runs over the blue printed imprint, so the purple ink was separated from the blue by script (work/unmix.py; the reviewer made its own ink map independently). The first attempt at this note, made without a parallel, gave "alkos-se ... szivdén", which is no Hungarian. The "A" turned out to be the blue imprint, and the "d" the descender of the z in the row above. The note was then read with the wording of sister card HCP 1234, "kösse össze szívünket", in view.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs. The names are conventional descriptions of the handwritten shapes.

Register type (2026-11-03): **MASC + Steganography**. Besides the cipher rows, a message is hidden in the stamp box under the removed stamp: a plain Hungarian note signed with the name feri in cipher signs. A stamp-box audit on 2026-11-03 re-read it from the original scan and changed no letter (see Plaintext and Uncertainties).

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma or corner | t |
| long stroke, short tick on the left | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright or tilted cross | f | tall stroke, tick on the right | h / p | low descender | y |
| hook with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

The digraphs gy and sz are written as two signs each. Dots over o and u give ö and ü, though not always. No cipher sign on this card carries an acute tick, so long vowels are supplied in the normalized text. The h/p sign is one shape on this card and is decided by the word. Three times the s sign is written as a closed narrow loop, always at a word edge.

## Plaintext

Literal decipherment by written row. Spaces are editorial, h stands for the h/p sign, and {?} is the blotted mark in row 07. Square brackets in the stamp note mark letters supplied from the HCP 1234 formula, where the traces are only compatible.

```text
01 szeretet edes jolan
02 kam becses sorait
03 megkahtam mely
04 nagyon koszönök
05 igen örülök hogy uj
06 ra olvashhatom
07 sorait d{?}elutan
08 megyek haza most
09 mast nem irhatok
10 mert keves idom
11 van viszontlatas
12 ra hü kedvesse feri

Stamp box, plain script:  hit remény / és szere- / tet kös- / se [öss]ze / sziv[ün]- / [ket]
Stamp box, cipher signs:  feri
```

### Hungarian (normalized)

Szeretett édes Jolánkám! Becses sorait megkaptam, mely[et] nagyon köszönök. Igen örülök, hogy újra olvashatom sorait. Délután megyek haza. Most mást nem írhatok, mert kevés időm van. Viszontlátásra! Hű kedvese, Feri.

Under the stamp: Hit, remény és szeretet kösse [öss]ze szív[ünket]. Feri.

### English

My beloved sweet Jolánka! I have received your dear lines, for which I thank you very much. I am very glad that I can read your lines again. This afternoon I am going home. I cannot write anything else now, because I have little time. Until we meet again! Your faithful sweetheart, Feri.

Under the stamp: May faith, hope and love bind our hearts together. Feri.

Address: To the promising young lady Jolánka Tóth, Jászárokszállás.

### Slovak

Moja milovaná, sladká Jolánka! Vaše milé riadky som dostal, za ktoré veľmi ďakujem. Veľmi sa teším, že môžem znova čítať Vaše riadky. Popoludní idem domov. Teraz nemôžem napísať nič iné, lebo mám málo času. Dovidenia! Váš verný milý, Feri.

Pod známkou: Nech viera, nádej a láska spoja naše srdcia. Feri.

Adresa: Sľubnej slečne Jolánke Tóthovej, Jászárokszállás.

## Uncertainties

- **Stamp-box note, the weakest part of the card.** `hit remény`, `és szere-`, `tet` and `kös-` can be read on the ink-separated image. In `össze` the z and e are seen, while `öss` is a run of arches over the printed wreath. In `sziv-ünket` the letters s, z, i and v can be followed, but `ün` is heavily overlapped. The last row has a peak, a speck and a letter merged with heavy strokes, compatible with `ket` but not firm. The ending therefore rests mainly on the formula of HCP 1234. No competing wording fits. The tall stroke that looks like a d in this row is the descender of the z above, and the thick mark at the row's end is a hyphen. The surviving strip of the stamp, with the denomination `FIL`, may still cover ink.
- **Row 13 `feri`.** The first sign is a thick diagonal cross, which has the shape of u, and it is read f by the name. The second shows only two bars, so taken literally the signs give `fari`. e signs with a nearly lost third bar occur elsewhere on the card (`becses`, row 2).
- **Row 7 raised mark.** A small heavy x-shaped blot stands between the d and e of `delutan`. It has no value in the word. It is probably a false start or a spoiled acute, and it is left out. Reading it u or f gives no word.
- **Blotted or overwritten signs.** The t of `viszontlátás` (row 11) is a black blot with F-like arms, and t is the only value that makes the word. The first f of `kedvese feri` (row 12) is a blotted star in a stain, read by the name. The first i of row 5 is a blot with its dot visible. The ü of `örülök` is a star-shaped overwrite with a thin earlier arc beside it, but its dots and hooked arm still give ü.
- **Word-sense calls.** The h/p sign in `megkaptam` is p by the word, and the others on the card are h. Three closed s signs could be taken for o, but o gives no word in any of those places (`ozeretet`, `edeo`, `becseo`). The d signs have their tick on the left and are distinct from n here.
- **Writer's spellings, normalized.** `szeretet` to szeretett, `mely` to mely[et] (a grammar repair, bracketed), `koszönök` to köszönök, `olvashhatom` to olvashatom (two complete h/p signs written), `kedvesse` to kedvese (two s signs written), `idom` to időm, `hü` to hű.
- **Date.** The year is unread, and the second cancel is not read beyond isolated characters.

## Review

An independent review by a separate Claude Opus 5.5 agent ran the reproduction command, made its own crops, transcribed all rows in its own sign-class names and decoded them with its own script. Rows 1 to 12 agree exactly with the ledger. Row 13 differed in one sign, the two-bar e. The reviewer knew the claimed reading, so this was not a blind check. It also built its own ink map of the stamp box. It judged `kösse össze sziv-` to be seen on the card and only `-ünket` to rest mainly on the formula, so it did not treat the note as an unread clause. Verdict: **ACCEPT**, with seven minor findings.

What changed because of the review (no letter value changed):

- The acute on the e of `delutan` (row 7) was removed, because the sign has three plain bars and no tick. On rechecking, the solver found the same error on `keves` (row 10), which the review had not listed, and removed that too.
- The two-bar e of row 13 is now flagged in the ledger.
- The guided letters of the stamp note are now in brackets. The claim that the t of the last row is clear was withdrawn.
- The overwrite on the ü of `örülök` was added to the disclosed points.
- The argument for correctness was reworded so that it no longer overclaims on `megkaptam`, `viszontlátásra` and `köszönök`.
- The date is now given as 27 December, year unread, and the green `FIL` strip is identified as the surviving part of the stamp.
- The sign count was corrected to 176 letters plus one unassigned mark.

The reviewer could not verify the year, whether writing remains under the stamp strip, or `-ünket` independently of the formula.

![Stamp box with the blue imprint suppressed, from the reviewer's ink map (review/work/box_ink.png)](../review/work/box_ink.png)

![Foot of the stamp box: the end of sziv-, the last plain row, feri in cipher signs, and the surviving green strip with FIL (work/crops/stamp_strip.png)](../work/crops/stamp_strip.png)
