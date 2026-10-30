# HCP 1509 (pc_hcp_190): a German love postcard from Heinrich to Elisabeth, Lieblos 1912

Human solver: Tomáš Pavuk

**Status: deciphered in full (359 of 359 cipher signs); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1509 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1509), portal name pc_hcp_190, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1912-04-05, language Unknown, location Europe, sender and recipient Unknown, with no transcription or solution attached.

The picture side carries a printed German drinking and love verse ("Es lebe der Wein und die Liebe …"); it contains no cipher. The cipher text is on the address side. Turned upright (90° counter-clockwise from the scan), the upper half carries the address in Kurrent script and the lower half, below a ruled line, carries the message: a plain heading **Lieblos, 5. 4. 12.**, sixteen lines of digit-like cipher signs, and the plain Kurrent farewell **Auf Wiedersehn** inserted between them.

The address reads, tentatively, *Fräulein Elisabeth Herb[…] in Wächtersbach, im Schloß, Kreis Gelnhausen*. The card bears a German Reich 5-pfennig Germania stamp and a railway post (Bahnpost) cancellation "…SSEN–GEL[NHAUSEN] … ZUG 512", i.e. the Gießen–Gelnhausen line. Lieblos (today part of Gründau, Main-Kinzig-Kreis, Hesse) lies on that line, and Wächtersbach is in the same district. 5 April 1912 was Good Friday (Easter Sunday fell on 7 April 1912), so the "second holiday" mentioned in the text is Easter Monday, 8 April 1912.

![Picture side: printed verse, no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side turned upright: Kurrent address at the top, the plain heading "Lieblos, 5. 4. 12." and the cipher message below; "Auf Wiedersehn" in plain Kurrent between the cipher lines (work/address-rotated.png)](../work/address-rotated.png)

**Credits.** An OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) captured the portal tabs and both scans on 2026-10-26 and noted that the card is a dense numeral-like substitution in a German context; it produced no transcription or key. The transcription, the key and the decipherment were made by Claude Opus 5.5 on 2026-10-30, and a separate Claude Opus 5.5 agent reviewed them. No published decipherment of this card was found or used, and no sister card in this repository uses the same alphabet.

## Method

The transcription is **manual**. The solver rotated the scan and read every line sign by sign at 4–8× enlargement, recording each sign as a short token (work/transcription.txt). No OCR was used, and the portal supplied no transcription.

The key was found from a crib. The first line begins with a five-sign word whose 2nd and 5th signs are equal (an `8`), which fits MEINE; the last word of the line, nine signs long with the same `8` in 1st and 7th place, fits ELISABETH, and the name recurs in the closing formula. These two words gave M, E, I, N, L, S, A, B, T and H; the following words HABE DEINEN LIEBEN HEUTE MORGEN filled in D, R, U, G and O. From then on the key was held fixed and decoded the rest of the card without any change and without an unknown sign.

Signs that needed care at high enlargement: the plain `1` (T) against the `7` with a hooked top (R); the tall `9` with a long descender (G) against the closed-top R in "mir"; single against double underline under `11` (O against V); and the two dots of the umlauts on O and U.

In review, the reviewer made its own crops of the scan (per-line strips at 4–7×), compared every line sign by sign with the transcription, and decoded the text with its own decoder and its own key table typed from the scan, not loaded from the solver's files (review/work/decode_rev.py). It obtained the same word sequence and the same 359 signs, with no unknown token.

## Key

A homemade **monoalphabetic substitution** with digit-like signs (a private "number alphabet"), German, with `x` as the word divider. The tokens below are conventional names for the handwritten shapes.

| Sign on the card | Token | Plain | Sign on the card | Token | Plain |
|---|---|---|---|---|---|
| fraction 16 over 1 | `16/1` | A | `11` underlined | `11_` | O |
| 6 | `6` | B | `11` underlined, two dots | `11_"` | Ö |
| small c/v hook | `c` | C | 7 (1 with hooked top) | `7` | R |
| h-shape | `h` | D | 4 | `4` | S / ß |
| 8 | `8` | E | S / long-s curve | `S` | F |
| 9 with descender | `9` | G | plain 1 | `1` | T |
| = with dot below | `=` | H | colon | `:` | U |
| single dot | `*` | I | colon with two dots | `:"` | Ü |
| 3 | `3` | K | `11` double underlined | `11=` | V |
| 1 with bar on top | `T` | L | 111 | `111` | W |
| Kurrent-M-like N | `N` | M | h with hook on top | `hz` | Z |
| 11 | `11` | N | x | `x` | word divider |

J, P, Q, X and Y do not occur. The key is one fixed table of 23 letter signs used for the whole text, with no homophones. Note that M is written with a sign resembling a Kurrent N, while N is written as `11`, and that O, Ö and V are all built on `11` with different marks underneath. Two numerals ("2." and "100,000") are written in clear.

Letter frequencies of the decoded text (E 74, I 39, N 27, R 24, H 20, D 20, T 18, A 18, S 16, M 15, B 15, …) are a normal German profile.

## Plaintext

Literal output of the decoder, line by line, spellings exactly as on the card (plain-script lines marked `[plain]`):

```text
[plain] Lieblos, 5.4.12.
MEINE HEIS GELIETE ELISABETH
HABE DEINEN LIEBEN HEUTE MORGEN
ERHALTEN ABER MEINE FREUDE WAR GRÖSER
ALS ICH MIR DACHTE DENNEWIE GERNE
WARE ICH WIEDER EINMAL BEI DIR
DENN ICH BIN ZU VERLIEBTEIN DICH
ABER ICH HOFFE DOCH GANZ BESTIMMT
DASS DU DENN 2. FEIERTAG KOMMEN
WIRST SCHREIBE MIR MITEWELCHEM
ZUGEDU KOMMST
[plain] Auf Wiedersehn
VIELE GRÜSE UND 100,000 KUSSE SENDET AN
DICH MEINE HEIS GELIEBTE ELISABETH
DEIN DIR AUF EWIG TREU BLEIBENDER
BALD ANTWORTE
HEINRICH
```

German, in normalised spelling and punctuation (editorial restorations in square brackets):

**Lieblos, 5.4.12. Meine heiß gelie[b]te Elisabeth! Habe deinen lieben [Brief / deine liebe Karte] heute Morgen erhalten, aber meine Freude war größer, als ich mir dachte, denn wie gerne wäre ich wieder einmal bei dir, denn ich bin zu verliebt in dich. Aber ich hoffe doch ganz bestimmt, dass du den 2. Feiertag kommen wirst. Schreibe mir, mit welchem Zuge du kommst. Auf Wiedersehn. Viele Grüße und 100.000 Küsse sendet an dich, meine heiß geliebte Elisabeth, dein dir auf ewig treu bleibender Heinrich. Bald antworte[n]!**

English translation: **Lieblos, 5 April 1912. My dearly beloved Elisabeth! I received your dear [letter] this morning, but my joy was greater than I had imagined, for how gladly I would be with you again, for I am too much in love with you. But I do hope very much that you will come on the second holiday [Easter Monday]. Write and tell me which train you are coming on. Goodbye till we meet again. Many greetings and 100,000 kisses to you, my dearly beloved Elisabeth, from your Heinrich, who remains faithful to you forever. Answer soon!**

Slovak translation: **Lieblos, 5. 4. 1912. Moja vrúcne milovaná Alžbeta! Dnes ráno som dostal tvoj milý [list], ale moja radosť bola väčšia, než som si myslel, lebo ako rád by som bol zase raz pri tebe – som do teba príliš zaľúbený. Ale celkom určite dúfam, že prídeš na druhý sviatok [Veľkonočný pondelok]. Napíš mi, ktorým vlakom prídeš. Do videnia. Veľa pozdravov a 100 000 bozkov ti posiela, moja vrúcne milovaná Alžbeta, tvoj navždy verný Heinrich. Odpíš čoskoro!**

Notes on the reading:

- **The opening formula recurs.** "Meine heiß geliebte Elisabeth" opens the letter and returns in the closing formula, and both decipher identically (apart from the missing B in the first, see below). The name Elisabeth also matches the first name in the address, an independent check.
- **"2. Feiertag"** is the second day of a church holiday; with the card dated Good Friday, it is Easter Monday. The writer asks Elisabeth to say "mit welchem Zuge" (on which train) she will come, which fits the railway post on the card.
- **"Viele Grüße und 100.000 Küsse … dein dir auf ewig treu bleibender"** is a typical formula of love postcards of the 1910s.
- **"deinen lieben"** stands without a noun; the writer means his beloved's letter or card. "Bald antworte" is read as a request, "answer soon".

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1509/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the three files in source/, decodes every token of the manual transcription in work/transcription.txt with the key in work/key.json, prints the plaintext line by line as given above, and ends with `cipher signs decoded: 359; unknown tokens: none`. It does not read the image; the transcription step is manual and was checked independently against the scan in review.

## Uncertainties

None of these affects the meaning.

- **GELIETE (line 1).** In the first "geliebte" there is no B sign (`6`): the signs are `9 8 T * 8 1 8`. The same word in the closing formula has it (`… 8 6 1 8`). The writer most likely left out the B. The literal output keeps GELIETE; the normalised text restores gelie[b]te.
- **Extra E in DENNE·WIE, VERLIEBTE·IN, MITE·WELCHEM.** In these three places a clear `8` (E) stands between two words with no divider. It is read literally and dropped in the normalised German. In ZUGE·DU the E belongs to "Zuge" and only the divider is missing.
- **R in "mir" (line 4).** This R has its hooked top closed into a small loop, so it looks like a small 9, but it lacks the long descender of G; "mig" would make no sense. Everywhere else R is the open 7.
- **Final T of BESTIMMT (line 7).** The last `1` is written onto the second M at the trimmed edge of the card. It is read as T, which the word requires.
- **1 against 7.** The plain 1 (T) and the hooked 7 (R) are close at the resolution of the scan (1024 px wide). Every occurrence was checked at high enlargement by the solver and the reviewer, and in every case the shape agrees with the word.
- **Stray mark in ALS (line 4):** two small ticks (,,) under the L; ignored, possibly an umlaut set on the wrong line or a pen slip.
- **Writer's spellings kept in the literal text:** HEIS (heiß), GRÖSER and GRÜSE (single s for ß), WARE (wäre, no umlaut), DENN for "den" (2. Feiertag), and KUSSE (Küsse). For KUSSE, an umlaut over the U is not visible, but the Kurrent "Wiedersehn" runs directly above it, so its absence cannot be established.
- **Placement.** The cipher signature HEINRICH stands below and right of "Bald antworte"; the reading order given here is the natural one.
- **The address** (surname, exact place lines) is only partly legible at this resolution and is not part of the claim. Neither the writer Heinrich nor the addressee has been identified historically.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (three hashes OK, output identical to the literal plaintext, 359 signs, no unknown token) and decoded the text with its own decoder and its own key table typed from the scan, with the same result. It compared every line with the scan sign by sign at 4–7× and confirmed the doubtful places: no B in GELIETE, the closed-top R in MIR, the extra E in DENNE·WIE, the double underline of V, the umlaut dots on GRÖSER and GRÜSE, the stray mark in ALS, and the plain-script parts. It checked the context (Good Friday 1912, the Gießen–Gelnhausen Bahnpost, Elisabeth in the address) and found no sign that a published solution was used. Its four findings were all minor and are reflected in this report:

- **KUSSE umlaut.** The claim that this U has no umlaut is now worded as "not visible, cannot be established", because the Kurrent "Wiedersehn" occupies the space above.
- **Final T of BESTIMMT.** Now listed under the uncertainties.
- **"zu verliebt".** The English is now literal: "too much in love", matching the Slovak "príliš zaľúbený".
- **Restorations.** The normalised German now marks gelie[b]te and the missing noun after "deinen lieben" in brackets.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1509, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1509 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4588/conversions/pc_hcp_190_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4587/conversions/pc_hcp_190_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
