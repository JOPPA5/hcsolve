# HCP 910 (cpc_1917-08-03_DE_Ulm_DE_Erbenschwang_zwick-02): a soldier asks his parents for sugar

Human solver: Tomáš Pavuk

**Status: deciphered in full (92 of 92 digit signs); independent review 1 verdict ACCEPT, four minor findings, no change to the deciphered text.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 910 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/910), portal name cpc_1917-08-03_DE_Ulm_DE_Erbenschwang_zwick-02, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, recipient Georg Zwick, with no transcription or solution attached.

It is a German First World War picture postcard. The picture side shows the Ulm Minster with a printed red caption and carries no handwriting. The address side is written in German Kurrent script in blue ink:

- address (plain): **An Herrn Georg Zwick, Erbenschwang, Post Ingenried b. Schongau (Bay.)** - a hamlet in Upper Bavaria;
- sender (plain, top right): **Abs. M. Zwick, [rank, probably Musketier] [unit, probably J.R.] 247, Ulm a. Donau**;
- postmark **ULM Nr. 1 (DONAU) 3.8.17**, i.e. 3 August 1917; the letter itself is dated "2.";
- the message, mostly enciphered, and one plain line written vertically along the divider.

The writer is the same M. Zwick who wrote the sister cards HCP 1057 (from Aulendorf, July 1917, also to his parents; finished in this repository, FINAL 2026-11-03) and HCP 1056 (from Ulm). Sugar was strictly rationed in Germany in 1917, which fits the fact that the request is the part he chose to hide.

![Address side with the message (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Ulm Minster, no handwriting (source/picture-large.jpg)](../source/picture-large.jpg)

**Stamp box and steganography.** The stamp box holds only the printed dotted frame, a green printed number "Z 4285" and the Ulm postmark; no adhesive stamp was ever affixed (no glue residue or tear), so nothing can be hidden under a stamp. Both solver and reviewer searched both sides for hidden writing and found none beyond the vertical plain line, which is included below. The card is therefore plain MASC, not MASC + Steganography.

![Stamp box: printed frame, green Z 4285, ULM Nr. 1 postmark, no stamp (review/work/stampbox.png)](../review/work/stampbox.png)

## Prior publication

The digit key of this family was published on 21 February 2019 by a reader ("Thomas", comment #1) under Klaus Schmeh's blog post "two encrypted postcards from 1918" (Zwick cards to Erbenschwang): https://scienceblogs.de/klausis-krypto-kolumne/2019/02/21/two-encrypted-postcards-from-1918/ . Comment #9 there mentions a 1917 card of M. Zwick to his parents and cites T. Schrödel, "Ich glaube, es hackt!" (Springer), p. 233; that page could not be viewed, so it is unknown whether it shows this card or a decipherment. The portal links Schrödel's HistoCrypt article "Cryptographic postcards" (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166); only its abstract was consulted and it does not mention Zwick. No plaintext of this card was found anywhere. The key was taken from the sister card HCP 1057 in this repository; the transcription and decipherment of this card are new.

## Method

The transcription is manual, made by Claude Opus 5.5 from the high-resolution original scan (work/hires/), using enlarged crops of each line (work/crops/). Where the Ulm postmark crosses the writing, the blue ink was isolated from the black postmark (blue channel minus red) to separate the strokes. A short script (work/decode.py) checks the hashes of the source images, replaces the digits by letters and prints the result line by line. Reproduction, from the repository root:

```text
python3 -I ciphers/hcp-910/work/decode.py
```

The reviewer transcribed the ten enciphered lines independently from its own crops, wrote its own key table and decoder (review/work/my_decode.py) and obtained the same text and the same count of 92 digit signs.

## Key

Partial monoalphabetic substitution: ten letters (the five vowels and l, n, m, r, s) are written as digits; every other letter, and the ligatures ch, ck, tt, stay in plain Kurrent.

| digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| plain | a | e | i | o | u | l | n | m | r | s |

Umlauts are written as the digit with two dots: 1" = ä, 4" = ö, 5" = ü. Sign counts on this card: 0:3, 1:7, 2:22, 3:14, 4:3, 5:7, 6:4, 7:19, 8:6, 9:7. All ten digits occur and each is used consistently in several words (for example 7 = n in 74ch "noch", 237 "ein", d277 "denn", 73cht "nicht"), so the key is confirmed by this card itself, not only borrowed.

## Ciphertext and plaintext

```text
568 d27  2.  Liebe Eltern!         ulm den 2. Liebe Eltern!
2372 k61372 b3tt2                  eine klaine bitte
h1"tt2 3ch 74ch 177 25ch           hätte ich noch ann euch
72863ch 20 w5"9d2                  nemlich es würde
83ch 029 f92527                    mich ser freuen
w177 J29 8329                      wann Jer mier
237 P1k2t Z5ck29                   ein Paket Zucker
sch3ck27 k4"7t, d277               schicken könt, denn
3ch w230 73cht w177 3ch            ich weis nicht wann ich
37 59615b k4882.                   in urlaub komme.
Gruß Euer Sohn Zwick               (plain)
```

Vertical line along the divider (plain): **Den Brief habe ich erhalten, besten Dank dafür.**

The date numeral "2.", the salutation "Liebe Eltern!", the greeting and signature and the vertical line are plain; everything else of the message is enciphered.

**German, writer's spelling:** Ulm, den 2. Liebe Eltern! Eine klaine Bitte hätte ich noch ann euch, nemlich es würde mich ser freuen, wann Jer mier ein Paket Zucker schicken könt, denn ich weis nicht, wann ich in Urlaub komme. Gruß Euer Sohn Zwick. - Den Brief habe ich erhalten, besten Dank dafür.

**Normalised German:** Eine kleine Bitte hätte ich noch an euch, nämlich es würde mich sehr freuen, wenn ihr mir ein Paket Zucker schicken könntet, denn ich weiß nicht, wann ich in Urlaub komme.

**English:** Ulm, the 2nd [of August 1917]. Dear parents! I have one more small request to you, namely it would make me very happy if you could send me a parcel of sugar, because I do not know when I will come home on leave. Greetings, your son Zwick. (Along the edge:) I have received the letter, many thanks for it.

**Slovak:** Ulm, 2. [augusta 1917]. Milí rodičia! Ešte mám na vás jednu malú prosbu, totiž veľmi by ma potešilo, keby ste mi mohli poslať balík cukru, lebo neviem, kedy prídem na dovolenku. Pozdrav, váš syn Zwick. (Na okraji:) List som dostal, veľká vďaka zaň.

## Uncertainties

- **würde**: w5"9d2 lies under the postmark. w, 5, 9, d and 2 are visible on the blue-isolated enlargement; the umlaut dots on the 5 cannot be separated from the postmark and rest on word sense ("wurde" is possible, with the same meaning).
- **ann** (177) is the writer's doubled spelling of "an"; **Jer** (J29) is his spelling of "Ihr". The signs are clear; the interpretation is by sense. The writer spells phonetically throughout (klaine, nemlich, ser, mier, weis).
- **könt** (k4"7t): an ink blot follows the 4; it is too small to hide a second 7, and the sense is the same either way.
- Kurrent capitals read by word sense: Z in Zucker, P in Paket, B in Brief.
- Only the day "2." is written; month and year come from the postmark 3.8.17.
- **Sender line**: the rank word and the unit abbreviation before 247 are not read with confidence. "Musketier" (as on HCP 1057) and "J.R." (Infanterie-Regiment) fit the shapes but rest on sense. These two words belong to the sender's military address, not to the message.

## Review and what changed

An independent Claude Opus 5.5 reviewer re-ran the reproduction command, transcribed all enciphered lines itself, decoded them with its own script and key table, checked the difficult places under the postmark on its own enlargements, inspected the stamp box and the picture side, and looked for prior publications. Verdict **ACCEPT**, with four minor findings:

1. The sender's rank and unit should be shown as gaps, not as readings - done (bracketed, with the probable readings marked as such).
2. The umlaut of "würde" should be marked as inferred in the transcription file - done.
3. The notes cited HCP 1057 as finished while it was still in review - reworded; HCP 1057 has since been finished.
4. The HistoCrypt article linked by the portal should be listed as consulted at abstract level - done.

The deciphered text did not change. After the review the stamp box was checked once more for a hidden message under a stamp (as found on other postcard series); there is no stamp and no hidden writing, so the cipher type stays MASC.
