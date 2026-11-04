# HCP 993 (cpc_1903-02-04_DE_Munchen_DE_Eschersheim_kellermann-01): a German love letter from Erich to Margarethe Kellermann

Human solver: Tomáš Pavuk

**Status: deciphered in full; every cipher sign on the card decodes with one 23-sign key. Independent review 1 verdict ACCEPT; four minor corrections, no change to the meaning.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 993 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/993), portal name cpc_1903-02-04_DE_Munchen_DE_Eschersheim_kellermann-01, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Margarethe Kellermann. No transcription or solution was attached; the only reference is T. Schrödel, "Cryptographic postcards", HistoCrypt 2021, whose abstract page gives no decipherment of this card.

The card is a coloured picture postcard "München – Wittelsbachbrunnen" (Verlag Wagner & Weil, Kunstverlag, München, No. 503). The address side is in plain German Kurrent script: **Fräulein Margarethe Kellermann / p. Adr. Herrn A. Weyhe / Hochwohlgeboren / Eschersheim b/Frankfurt a/Main / Frankfurterstr. 49.** A green 5-Pfennig Bavarian stamp is cancelled MUENCHEN; the arrival postmark reads **ESCHERSHEIM -4.2.03 6-7 V.** (4 February 1903, 6–7 a.m.).

The whole message is on the picture side, written with the card turned 90° below the printed picture. The writer dated it "München d. 4. Febr. 03". Most of it is in a digit-and-symbol cipher; one sentence in the second and third lines is in plain Kurrent; the last two cipher lines ("und Küssen / Dein Erich") and two rows of dots are written upside down in the right half of the card.

A second card of the same correspondence, HCP 992 (München, 4 December 1903, same address, same cipher), is deciphered separately in this repository.

![Picture side as scanned (source/picture-large.jpg)](../source/picture-large.jpg)

![Picture side turned so that the cipher lines run left to right; the smeared band runs through the left part of the text (work/crops/rot_left.png)](../work/crops/rot_left.png)

![Address side: Fräulein Margarethe Kellermann in Eschersheim near Frankfurt; MUENCHEN cancellation on the stamp, ESCHERSHEIM -4.2.03 arrival mark at the bottom left (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is manual. The solver (Claude Opus 5.5) read the high-resolution original scan of the picture side (work/hires/), rotated and cut into enlarged line crops (work/crops/), sign by sign, and wrote one token per sign into work/transcription.txt. Restorations (signs hidden by an ink smear or the card edge), a sign the writer left out and one sign read against its shape are marked separately there.

The cipher was broken from the text itself. The plain Kurrent sentence in the middle and the end of the letter fix the context (a love letter signed by a man). Long words with repeated letters then fix the key: "herzinniggeliebtes" (8 4 hook Ibar arc 2 2 arc 9 9 4 1 arc 4 6 7 4 5), "Herzens", "Rechnung", "ungeduldiger", "innigsten". Each sign stands for one letter; the digits 0–9 are letters, not numbers. The one real number, 18, is written in plain digits inside a drawn box so that it is not read as cipher.

In review a second Claude Opus 5.5 agent wrote its own key table and parser, decoded the transcription independently with the same result, and checked every cipher line against enlarged crops of the scan.

## Key

Simple monoalphabetic substitution (MASC). The sign names are conventional descriptions of the handwritten shapes.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| 0 | O | 1 | L | 2 | N |
| 3 | M | 4 | E | 5 | S |
| 6 | B | 7 | T | 8 | H |
| 9 | G | arch with a dot under it | I | C-shaped hook with blob foot | R |
| reversed c | C | capital I with serifs | Z | u-shaped cup | U |
| pointed v | D | oval crossed by a long vertical (φ) | A | + | F |
| + with two bars (≠) | K | z-stroke joined to 0 (one sign) | W | 0 with a bar above | V |
| cup with two dots | Ü | 0 with two dots | Ö | | |

Not attested on the card: J, P, Q, X, Y. ß is written as s or ss.

## Plaintext

Decoder output, line by line as on the card (lower case = deciphered, capitalised words in L2–L3 = plain Kurrent):

```text
L1   mein herzinniggeliebtes herzens....!
L2   Deinen lieben Brief habe ich erhalten. Bin kern=
L3   gesund. werde von tag zu tag ungeduld-
L4   iger dich bald wieder, in die arme schlie
L5   sen zu können. nun sind es noch 18 tage bis
L6   dahin. bin nur froh dass mir diesmal kein
L7   feldwebel einen strich durch die rechnung ma-
L8   chen kann. lieb! dein e wird dich ganz und
L9   gar aufessen wenn er kommt. doch nun lebe
L10  recht wohl. und grüsse alle lieben recht herz=
L11  lich. dich aber umarmt mit innigsten, grüssen.
L12  und küssen          (upside down)
L13  dein erich          (upside down)
L14  (.... ....)         (upside down, two rows of dots)
```

Normalised German (spelling, capitals and punctuation editorial; the plain-script sentence in brackets):

**München d. 4. Febr. 03. Mein herzinniggeliebtes Herzens....! [Deinen lieben Brief habe ich erhalten. Bin kerngesund.] Werde von Tag zu Tag ungeduldiger, Dich bald wieder in die Arme schließen zu können. Nun sind es noch 18 Tage bis dahin. Bin nur froh, dass mir diesmal kein Feldwebel einen Strich durch die Rechnung machen kann. Lieb! Dein E. wird Dich ganz und gar aufessen, wenn er kommt. Doch nun lebe recht wohl und grüße alle Lieben recht herzlich. Dich aber umarmt mit innigsten Grüßen und Küssen Dein Erich ........**

English translation: **Munich, 4 Feb. 1903. My most dearly beloved darling (literally "heart's ....")! [I have received your dear letter. I am in the pink of health.] I grow more impatient from day to day to hold you in my arms again soon. Now there are still 18 days until then. I am just glad that this time no sergeant can spoil my plans (literally "draw a line through the reckoning"). Dear! Your E. will eat you up completely when he comes. But now farewell, and give my warmest regards to all your loved ones. And you are embraced, with most heartfelt greetings and kisses, by your Erich ........**

Slovak translation: **Mníchov 4. febr. 1903. Moje najvrúcnejšie milované srdiečko....! [Tvoj milý list som dostal. Som zdravý ako repa.] Zo dňa na deň som netrpezlivejší, kedy ťa znova zovriem v náručí. Teraz to ešte potrvá 18 dní. Som len rád, že mi tentoraz žiadny šikovateľ nepreškrtne plány. Milá! Tvoj E. ťa celú zje, keď príde. Ale teraz sa maj veľmi pekne a srdečne pozdravuj všetkých svojich drahých. Teba však objíma s najvrúcnejšími pozdravmi a bozkami Tvoj Erich ........**

Notes on the reading:

- "Herzens....!" ends in dots on the card: the endearment is deliberately left unfinished.
- "Dein E." is a single cipher sign 4 (E), the writer's initial.
- The writer was evidently a soldier: he fears that a Feldwebel (sergeant) could again cancel his leave, and he expects to visit in 18 days, around 22 February 1903.

## Uncertainties

- **Ink smear.** A wiped vertical band crosses the left part of lines L5–L11. Signs restored there on spacing and word sense: the b of "Feldwebel", the h of "wohl", two signs "es" in "aufessen" (the gap measures about two signs; "auffressen" would need four and fits worse, with the same meaning), the last s of "bis" at the card edge. "kann" and the first signs of "bin" and "recht" are faint but visible. In all, 337 signs are read directly, 6 are restored.
- **Writer's slips.** "ungedul-iger": the second d is not written on the card and is supplied. "dahin": the third sign is 6-like (closed lower loop, heavy blotted top); it may be a 6 (b, "dabin") or an 8 with a filled upper loop; it is read as h on word sense either way. "schliesen" has a single s for ß.
- **Close sign pairs.** The R-hook and the 6 (B) are similar; in "bin", "nur" and "mir" the call partly rests on word sense. The W-sign is a ligature of a z-like stroke and 0 and is treated as one sign; reading it as two gives no words.
- **Plain Kurrent sentence.** "kern" in "kern=gesund" is a dense scrawl: the k is clear, the following humps are read as e-r-n on word sense ("kerngesund" is idiomatic). "Febr." in the date line may be "Fbr.".
- **Postmarks and date.** The Eschersheim arrival mark clearly reads 4.2.03, 6–7 a.m. The München cancellation, struck over the stamp, is only partly legible ("MUENCHEN", "03", a day "3" and unclear month letters) and does not confirm the date. A morning arrival on 4 February implies posting on 3 February, although the card is dated "d. 4.".
- **Steganography.** Postcards of other series often carry hidden messages under the stamp. On this card the stamp is still affixed, so the area under it cannot be checked from the scans; no writing is visible at its edges, in the picture or in the margins. The two rows of dots at the end are read as plain sign-off dots (kisses), not as a code.
- The writer's full identity (Erich, a soldier stationed in or near Munich) and the relation of the A. Weyhe household to the recipient are not established.
- Only the abstract page of the HistoCrypt 2021 paper was checked for a published decipherment; none was found there or on the portal.

## Review summary

Reviewer: Claude Opus 5.5 (a separate agent), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decoded the transcription with its own independent script (same text; every sign within the 23-sign key, no sign with two values), and checked every cipher line against 2–6× crops of the scan. It confirmed the omitted d of "ungeduldiger", the boxed 18, the upside-down closing lines and that each restoration in the smear is disclosed and consistent with the spacing. Its four minor findings were all accepted:

- **Umlaut on the last "Grüßen".** Two dots are visible above the U; the transcription now has Ü there, and an earlier remark that the dots were missing is withdrawn.
- **Postmarks.** The München cancellation is now described as partly legible and no longer claimed to confirm the date; the full address ("p. Adr.", "Hochwohlgeboren") is given.
- **"dahin".** The third sign is described as 6-like, possibly an 8 with a blotted top; the reading is unchanged.
- **Punctuation.** A full stop after "wohl" was added to the transcription.

The meaning of the letter did not change. All work on this card (transcription, key reconstruction, decipherment, report) was done by Claude Opus 5.5 on 2026-11-03; there was no earlier work on this number.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-993/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the four scans (source/ and work/hires/), decodes the manual transcription in work/transcription.txt with the key above and prints the fourteen lines shown in the Plaintext section. It does not read the images; the transcription step is manual and was checked independently in review.

## Sources

- HC Portal record 993, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/993 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3039/conversions/cpc_1903-02-04_DE_Munchen_DE_Eschersheim_kellermann-01_pic-large.jpg (source/picture-large.jpg) and the original https://api.hcportal.eu/media/3039/cpc_1903-02-04_DE_Munchen_DE_Eschersheim_kellermann-01_pic.jpg (work/hires/).
- Address side: https://api.hcportal.eu/media/3040/conversions/cpc_1903-02-04_DE_Munchen_DE_Eschersheim_kellermann-01_adr-large.jpg (source/address-large.jpg) and the original in work/hires/.
- T. Schrödel, "Cryptographic postcards", HistoCrypt 2021: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 (abstract page checked).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03 by the orchestrator: no entry for this card.
