# HCP1208: Feri to Jolánka Tóth, the cancelled train (Budapest, 15 October 1914)

**Status: complete reading of all cipher text on the card, with small disclosed residual points; review 1 (verdict REVISE) addressed.** Written 2026-11-02 by Claude Opus 5.5. There is no earlier work on this number. Portal status when captured: Not solved, no transcription or solution attached. No published solution of this card was found (orchestrator AI-register check 2026-11-02: no record). The key comes from the finished cards of the family, credited below.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs, the Jolánka postcard family (key established on HCP1301, 1243, 1213, 1216 and others; the fullest legend is in `ciphers/hcp-1216/SOLUTION.md`). The key was transferred unchanged; no new sign value was needed.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark or 5-shape | k | F-like, two bars | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| long stroke + short tick on the left | d | two equal strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall + short stroke | h / p (near-homograph) | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | | | | |

Digraphs are written with two signs (c+s, s+z, g+y). Dots or strokes over a sign give ö, ü, ű, é.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1208/work/decode.py
```

It checks the SHA-256 of both scans in `source/` and both originals in `work/hires/`, decodes `work/ledger.txt` through the key table in the script (420 written signs in 22 main rows and 5 rows round the stamp), prints the literal text, the weekday of the postmark, and the normalized text `work/normalized.txt`. Since review 1 the ledger holds sign classes, not letters, so the key is really applied; the only word-sense choices are explicit (`TS=p`, `FIVE=g`). The ledger is a manual transcription from the pixels, not OCR. The cancellation lines and the postmark are black over violet pencil; `work/crop6.py` and `work/crop7.py` (run from `work/`, they write to `work/crops/`) separate the pencil by blue minus green, which was needed for rows 4 to 10.

## Literal decipherment (as printed by the command)

```
01 szeretetedesjolankam        12 holnapazazpentakan
02 kivanomhogyalegjobbked      13 delutanszabadleszeke
03 vebentaleljasoraim          14 eshogyelmehtekemagá
04 sajnalomhogyeztalapot       15 hozédesemmivelmég
05 kelkuldenemmertmagais       16 nemtudomhogyhova
06 gondoljahogyvalami          17 megyünkesmikorjö
07 különösdologadtaelo         18 vűnkviszszadehale
08 magatsajnalattalkeltu       19 hetelmegyekezel
09 datnomedesemhogyavona       20 bezaromsoraim
10 tunkatlemondjakesigy        21 maradoksirighű
11 mostmarnemtudomhogy         22 kedveseferi
round the stamp: csokol / szam / talan / szor / ferid
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Sajnálom, hogy ezt a lapot kell küldenem, mert maga is gondolja, hogy valami különös dolog adta elő magát. Sajnálattal kell tudatnom, édesem, hogy a vonatunkat lemondják, és így most már nem tudom, hogy holnap, azaz pénteken délután szabad leszek-e, és hogy elmehetek-e magához, édesem, mivel még nem tudom, hogy hová megyünk és mikor jövünk vissza, de ha lehet, elmegyek. Ezzel bezárom soraim, maradok sírig hű kedvese, Feri.

Round the stamp: Csókol számtalanszor Ferid.

## English

My beloved sweet Jolánka! I wish that my lines may find you in the best of moods. I am sorry to have to send this card, since you too will think that something unusual has come up. I must tell you with regret, my darling, that they are cancelling our train, and so I now do not know whether I shall be free tomorrow, that is Friday afternoon, and whether I can go to you, my darling, because I do not yet know where we are going and when we are coming back; but if it is possible, I will go. With this I close my lines; I remain, faithful unto the grave, your sweetheart, Feri.

Round the stamp: Your Feri kisses you countless times.

## Slovak

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Mrzí ma, že musím poslať tento lístok, lebo aj Vy si pomyslíte, že sa stalo niečo zvláštne. S ľútosťou Vám musím oznámiť, drahá, že náš vlak rušia, a tak teraz neviem, či budem zajtra, teda v piatok popoludní voľný a či budem môcť prísť k Vám, drahá, lebo ešte neviem, kam pôjdeme a kedy sa vrátime; ale ak to bude možné, prídem. Týmto končím svoje riadky a zostávam až do hrobu verný Váš milý, Feri.

Okolo známky: Bozkáva Vás nespočetnekrát Váš Feri.

## Unenciphered text on the card (not part of the cipher)

- Address, in plain pencil: Önagysága / Tóth Jolánka / úrleánynak (the hand is loose; the ending reads roughly -nyak or -nak) / Budapest / István út, then a number group under the collector's stamp, read as 5 sz. II. e. 5 a (house number, floor, door). The name and town are certain; this number group is tentative and does not bear on the message.
- Postmark: BUDAPEST 914 OKT 15, with 62 and a time mark. Printed on the picture side: A szerelem hőmérője. Aztán, hogy megöleltelek lett „16" fok a meleg.; publisher number 34213/4. The picture side has no handwriting.

## Uncertainties

Spelling is as written; the normalization is editorial and no letter was restored from a hidden place unless stated.

1. **Rows 4 to 10, under the postmark and wavy cancellation.** All signs there were read on the blue-minus-green separation and on saturated colour crops. The least clean are row 4 *ezt a lapot*, row 5 end *maga is*, row 9 end *a vona-*, row 10 *lemondjak* (the d and j overlap the postmark circle and the 62, and the k runs under the left stroke of the 6). The words are the ones that fit every visible stroke, but these rest partly on word sense.
2. **Row 10 *lemondjak*** is the literal form; the 3rd person plural *lemondják* (they cancel) is my reading because *jak* has no accent visible. A 1st person *lemondjak* (that I should give up our train) is grammatically possible and would change only that clause. In either case the card does not explain "our train" or who "we" are. HCP1228 has Feri in railway clothes (*vasúti ruhában*), which may be the background; that is a hint, not evidence for this card.
3. **Row 7, d of *dolog***: a long stroke crossed by a cancellation line, with a small round mark to its right. The left tick of this card's d is not visible, so the d rests on word sense alone (*különös dolog*).
4. **Row 14 end, *magá***: the g is drawn in the 5-shape, the same as the g of row 15 *még* and of row 21; g rather than k rests on word sense. The two-bar a, the two-bar a and the acute over it are clear.
5. **Row 14 *elmehtek*** is literal: the sign before t is tall + short, not two equal strokes, so h and not n. Normalized *elmehetek-e* (the e of -het- omitted). *elmentek* would need n and gives no sense.
6. **Row 20 sign 5, r of *bezarom***: a stem, a top bar and a faint low arm. The low arm is weak; gamma t is the alternative and gives no word.
7. **Row 21 *sirig***: the fourth letter is a heavy overwritten blot, a loop at lower left with a crossing bar and an upward stem, read i partly on sense. Its dot is not separately visible. The last sign is the 5-shape, read g on sense (see 4). The formula *sírig hű* is the family's own (HCP1216, 1228).
8. **Writer's a/e slips and spelling** (literal, then normal): *talelja* → találja, *pentakan* → pénteken, *szeretet edes* → szeretett édes, *kel* → kell, *ezel* → ezzel, *viszsza* → vissza (sz+sz for ssz). *ezel* opens the sentence with *bezárom*. Acutes are marked only where seen (é in rows 15, twice, and á in row 14); the others are supplied. Row 16 *hova* → hová. *soraim* for *soraimat* is the writer's habit (row 3, and the family formula).
9. **g and k**: the open descender loop and the 5-shape are close in this hand. Word-sense choices are explicit in the ledger as `FIVE=g`.
10. **h / p**: *holnap* (p at the end, h at the start), *lapot*, *pentakan* and *hogy* rest on word sense, as on the sister cards; explicit in the ledger as `TS=p`.
11. **Stamp row S3**: the first sign is drawn as a steep corner close to the chevron; read t (*talan*), since v gives no word. Row S4 is partly on the printed stamp.

## Why it is correct

- The key was not fitted to this card: it was taken unchanged from finished cards and yields continuous Hungarian across all 420 signs, with only the isolated points above.
- An independent external check: the text says *holnap, azaz pénteken* (tomorrow, that is Friday), and the postmark of 15 October 1914 is a Thursday (the command computes this).
- The close was read from the signs and turns out to be the family's standard formula: *bezárom soraim* occurs on 19 cards of hcp-12xx and hcp-13xx, and *bezárom soraim, maradok sírig hű kedvese* on HCP1228, 1237, 1249 (reviewer's search). The address, the name Jolánka, the signature Feri and the formal *maga* address (now also *magához*) agree with the family; the placing of text round the stamp matches HCP1216.
- Repeated words decode the same: *hogy* ×7, *édesem* ×2, *nem tudom* ×2, *soraim* ×2.

## Response to review 1

Verdict REVISE, all findings addressed. I re-read the reviewer's crops of every disputed place (`review/work/crops/panel.jpg`, `r19a`, `r20a`, `r20b`, `r21b`, `r7a`) and agree with them. The command was re-run after the changes: all hashes OK, 420 signs, output as printed above.

1. **Row 20 *bezarom*: fixed.** The three bars, the crossed z and the two bars are plain on `r20a.jpg`; I forced *banatom* to sense. Row 20 sign 5 is r with a faint arm, disclosed in uncertainty 6.
2. **Row 21 *sirig*: fixed.** The looped dotted sign is i, as the panel shows; the [s] and the omitted e are gone. The blot and the final g are disclosed in uncertainty 7.
3. **Row 19 *hetel*: fixed.** Three bars on `r19a.jpg`; *al → el* removed.
4. **Normalized text and translations: fixed.** *soraim* is kept unbracketed, as HCP1228 normalizes it, so no *-at* is restored. "Why it is correct" is rewritten. My earlier statement about the family's closing formula was false and is gone.
5. **Row 7 d: fixed.** Uncertainty 3 now says word sense alone.
6. **Row 15 *hozzá[d]*: fixed, by a reading the review did not make.** Both of us missed a sign. The end of row 14 runs across the printed divider, and past the *g* stand two more bars with a thick mark above them (`work/row14-15-end.jpg`, made by `work/crop_row14.py`). The bars before the g are also only two, not three. So row 14 ends *m a g á*, not *m e g*, and it joins row 15 *hoz*: **magához**, "to you". No letter is missing, *hozzá[d]* goes, and the formal register holds. The sense of the clause is unchanged, but *még* "still" leaves the English and Slovak of this clause. The reviewer's finding 8 mark on row 14 is this acute, on á and not on an e. This added sign has not been seen by the reviewer: 420 signs against the reviewer's expected 419.
7. **Decoder: fixed.** `work/ledger.txt` is now in sign classes (built by `work/build_ledger2.py` from the reviewer's class list with the corrections above, asserting each letter); `decode.py` applies the key. The round 1 ledger is kept as `work/ledger-round1.txt`. `review/work/redecode.py` reads the old letter format, so to rerun it, point it at that file.
8. **Accents: fixed.** Row 14 á and row 15 é are marked in the ledger; uncertainty 8 no longer says "mostly not visible".

One error of mine beyond the review: "Why it is correct" said *hogy* ×8; the literal text has it 7 times. Corrected.
