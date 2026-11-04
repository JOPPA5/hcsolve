# HCP 947 (cpc_1909-06-03_DE_Doberan_DE_Reddelich_ernagarbe-03): "Ach, wärst du hier!" in turned capitals

Human solver: Tomáš Pavuk

**Status: the cipher block is deciphered in full (14 of 14 letter signs); the plain Kurrent greetings are read with one partly uncertain word. Independent review 1 gave the verdict REVISE; the cipher reading did not change, and the plain-text reading and the reproduction script were corrected.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 947 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/947), portal name cpc_1909-06-03_DE_Doberan_DE_Reddelich_ernagarbe-03. It belongs to Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03, the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Erna Garbe. No transcription or solution was attached. The collection file name gives the posting date as 3 June 1909 and the route as Doberan to Reddelich (Mecklenburg, Germany). On the scan only the year "09" of the postmark can be read with certainty.

The picture side is a printed studio portrait of the actress Gudrun Hildebrandt, with her printed name and the publisher mark "GCo 1936/3". It has no handwriting. The violet streaks along its top and bottom edges are ink or dye stains.

The address side is written in pencil and addressed to **Frl. Erna Garbe, Reddelich**. It carries a 5-pfennig Germania stamp and greetings from three people in German Kurrent script. There is also a small drawn airship and, in the left margin, a three-line block of strange signs. That block is the only ciphertext on the card. Two other cards to Erna Garbe from the same year are in the collection (HCP 946 and 948). They use different systems.

![Address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![The cipher block in the left margin, enlarged (work/crop_cipher.png)](../work/crop_cipher.png)

## Method

All reading was done by hand from enlarged crops (3 to 5 times) of the high-resolution scan. No OCR was used. The solver tried two ways of reading the whole block: turning it by 180 degrees, and flipping it top to bottom. With 180 degrees it reads backwards with no words. With the flip, the D and E come out mirrored. Both were rejected.

What does work is to read each sign in normal writing order as a Latin capital that has been turned upside down. Six signs are plainly such letters: ∀ = A, ⊥ = T, Π = U, the turned D = D, a stroke over a dot (a turned i) = I, and 3 (a turned Ɛ) = E. These fix line 3 as "DU ?IE?" and line 2 as "?A??T". The sentence "Ach, wärst du hier!" fills every gap with a consistent assignment, and the sign for R occurs twice in the same form. Each word is closed by ",-" and the last by "!-". These marks are normal punctuation and are not enciphered.

The reviewer cropped the scan independently, named the signs in its own way and decoded them with its own script. It got the same result. Of the 14 letter positions, 11 follow from shape alone. Only W, R (twice) and the second H rest on word sense.

## Key

Simple monoalphabetic substitution (register type MASC). Each letter is written as an altered, mostly upside-down Latin capital.

| Sign as drawn | Letter | Basis |
|---|---|---|
| ∀ (turned A with crossbar) | A | shape |
| bracket open to the right | C | shape and word sense |
| H-like sign with extra strokes | H | shape and word sense |
| Λ with a faint central stem (turned W) | W | shape and word sense |
| zigzag Σ-like sign (twice) | R | word sense, consistent |
| 8 (closed S) | S | word sense |
| ⊥ | T | shape |
| turned D | D | shape |
| Π | U | shape |
| I-beam (H turned by 90 degrees) | H | word sense |
| stroke over a dot (turned i) | I | shape |
| 3 (turned Ɛ) | E | shape |

## Ciphertext and plaintext

```text
line 1:  ∀ [C] [H] ,-
line 2:  Λ| ∀' Σ 8 ⊥ ,-
line 3:  [turned D] Π ,- [I-beam] 'ı. 3 Σ !-
```

Decoded: ACH / WARST / DU / HIER!

German: **Ach, wärst du hier!**

- English: "Oh, if only you were here!"
- Slovak: "Ach, keby si tu bola!"

To reproduce, run `python3 -I ciphers/hcp-947/work/decode.py` from the repository root. The script checks the SHA-256 hashes of the source images and decodes the hand-made sign transcription through the key. It prints "ACH / WARST / DU / HIER!".

## Plain (unenciphered) text on the card

| Writer | German (Kurrent, transcribed) | English | Slovak |
|---|---|---|---|
| 1 | Fröhliche Pfingsten und Grüße sendet. – Eine neue Karte folgt bald. H.(?) Weber | H. Weber sends a happy Whitsun and greetings. A new card follows soon. | H. Weber posiela veselé Turíce a pozdravy. Čoskoro príde nová pohľadnica. |
| 2 | Auch ich sende schönen Gruß. Kollegin Warchow | I too send kind regards. Colleague Warchow | Aj ja posielam pekný pozdrav. Kolegyňa Warchow |
| 3 | Meinen Gruß sendet unbekannterweise A. Schmidt(?) | My greetings, though we have not met, A. Schmidt(?) | Môj pozdrav, hoci sa nepoznáme, posiela A. Schmidt(?) |

Address: Frl. Erna Garbe, Reddelich.

## Uncertainties

- **Umlaut.** The Ä in "wärst" rests on word sense alone. Above the second sign of line 2 there is only a single small upright tick. It is not two dots, and it is not turned like the letter. Read literally, the line gives "warst".
- **Signs that rest on word sense.** R, S, C and both forms of H are read from word sense. R is at least the same in both places where it occurs.
- **Writer 1, "und".** "und" at the end of the first line rests partly on word sense. After "Pfingst" the strokes are e-n, then u-n, and then a tall looped letter that is taken as Kurrent d. Other literal readings are possible, for example the letters e-n-o-r-k, or "Pfingstwoche" (Whit week). "Pfingstwoche" would also suit the posting date, Thursday 3 June 1909, four days after Whit Sunday (30 May). The clause reads either way.
- **Writer 1, "Grüße".** "Grüße" is read from the letter shapes: G with a descender, r, ü, ß and e. "Wünsche" ("wishes") would give the same sense.
- **Names.** The initial before Weber may be H or J, and "A. Schmidt" is probable but not certain.
- **Under the stamp.** The stamp was not lifted, so what is under it is unknown. Nothing written is visible at its perforations or anywhere in the picture. The type "MASC + Steganography" is therefore not claimed.
- **Published solution.** None was found. The portal gives only the general collection paper.

## Review and what changed

Review 1 was done by an independent Claude Opus 5.5 agent and returned the verdict **REVISE**. The reviewer confirmed the cipher reading and the key with its own crops and its own decoding script, and found no hidden writing on the picture side or around the stamp. Its findings concerned the plain text and some details:

1. **"Grüße" or "gewünscht" (line 2 of writer 1).** The reviewer proposed "gewünscht!". New crops show that the "!"-like stroke and a tall stroke inside the word are the long descenders of P and f in "Pfingst" on the line above. Without them the word has only five letter groups and no t, which fits "Grüße" and is too short for "gewünscht". "Grüße" also gives the verb "sendet" on the next line the object it needs. The reading was kept, and "Wünsche" was added as an alternative.
2. **The ending after "Pfingst".** This was re-read as "Pfingsten und" and openly marked as partly resting on word sense, with the literal alternatives listed.
3. **Script output.** The script used to print a comma after every word. It now treats ",-" as a word separator and prints ACH / WARST / DU / HIER!.
4. **The umlaut mark.** It is now described as a single upright tick, so Ä rests on word sense alone.
5. **Signature.** "Warkow" was corrected to "Warchow". The letters W-a-r-c-h-o-w are clear on the enlarged scan.

The decoded message, the key and the cipher type did not change.

## Credits

Transcription, key reconstruction and decipherment were done by Claude Opus 5.5 (Anthropic) on 2026-11-03. There was no earlier AI work on this number. Independent review was done by a separate Claude Opus 5.5 agent. Human solver: Tomáš Pavuk.
