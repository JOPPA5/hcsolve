# HCP 916: a Hungarian Morse love note to Ilona Márthé, Temesvár 1904

Human solver: Tomáš Pavuk

**Status: deciphered in full (7 Morse lines, 66 letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 916 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/916), portal name cpc_1904-04-01_HU_Temesvar_RO_Temesvar-Jozsefvaros_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient "Ilona Marfke", with no transcription or solution attached. The only reference attached is the general HistoCrypt article on the collection.

The address side is plain Hungarian: **Levelező lap. Ő nagysága Márthé Ilona úrhölgynek, Temesvár-Józsefváros, Eötvös utcza 7 sz.** ("Postcard. To her Ladyship Miss Ilona Márthé, Temesvár-Józsefváros, Eötvös Street No. 7"). The scan reads Márthé, not the portal's "Marfke". A green 5-filler Turul stamp is still on the card; its TEMESVÁR postmark reads ... 90(4) APR 1.

The picture side is a printed Easter card (three children with a nest, publisher mark NPG 277-6). Turned 90° counter-clockwise, it carries a dateline **Tv. 904 III/1.** in the top corner, a block of three Morse lines written diagonally across the oval, a monogram signature below them, and a block of four horizontal Morse lines under the picture. Apart from the dateline and the monogram there is no plain writing on this side.

The same recipient and the same address appear on HCP 1133 (Temesvár, December 1902), a card in this repository that also mixes Morse into its text and is signed Richter Antal. The writer's non-standard Morse sign for Á (`.-.--`) appears on both cards, so the two belong to one correspondence. The key used here was carried over from that card and checked on every sign of this one.

![Picture side turned upright (90° counter-clockwise): dateline at the top, diagonal Morse block and monogram in the oval, four Morse lines below the picture (work/crops/rot.jpg)](picture-upright.jpg)

![Bottom block: four horizontal Morse lines, the opening of the message (work/crops/bottom.png)](bottom-block.jpg)

![Diagonal block rotated a further 53°, with the dateline above and the monogram below. The large grey circular stamp "HCPORTAL.EU, Portal of historical ciphers, Collection: Tobias Schrödel" is a modern collection mark, not part of the 1904 card (work/crops/toprot.png)](diagonal-block.jpg)

![Address side: Ilona Márthé, Temesvár-Józsefváros, Eötvös utcza 7; 5-filler stamp still attached (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is manual. The solver rotated the high-resolution scan, cut enlarged crops of each Morse line (3x to 8x), and wrote down every dot, dash and separator into work/morse_transcription.txt. The writer puts a slanted stroke "/" after every letter and leaves no gaps between words, so letter boundaries are given by the card itself; word division is editorial. Two first readings were corrected on enlargement before handover: the third letter of bottom line 3 is `.-.` (R, giving KÉREM), not `.-..`, and the letter before EK in diagonal line 3 is `-.` (N), not `-..`.

The script work/decode.py checks the SHA-256 hashes of the four scans and decodes the transcription with the key below. In review, a separate agent rotated the scan itself, cut its own crops of every line, read every group again, and decoded its own transcription with its own table-driven decoder that uses only standard Morse plus É and flags anything else. Its reading agrees group for group with the solver's, apart from the two non-standard points listed under Uncertainties, which both sides read the same way.

## Key

International Morse code, with these additions and departures:

| Morse | Letter | Note |
|---|---|---|
| `..-..` | É | standard Hungarian sign |
| `.-.--` | Á | the writer's own sign (standard is `.--.-`); 3 times here, also on HCP 1133 |
| `.-.-` | C | once, in CSÓK; standard C is `-.-.` (word sense) |
| hooked stroke with a dot | Í | once, in ÍRJON; not a Morse group (word sense) |

Other long vowels (Ó, Ö, Í) are written as plain O and I. The register type label is **MASC/Morse**.

## Plaintext

Morse transcription, line by line ("/" = separator stroke on the card):

```text
B1 ../.-../..-/.../-.-/.-.--/--/-../.-./.-.--/--./.-/
B2 --/../-.-/---/.-./.-../.-.--/-/..../.-/-/---/--/?
B3 -.-/..-../.-./ ./--/.-/.-./.-/-./-.--/---/--/
B4 [hook]/.-./.---/---/-./
T1 --/../.-../.-../../---/..-./---/.-./
T2 .-./---/.-.-/.../---/-.-
T3 ..-../-../ ./.../ ./--/-./ ./-.-/
```

Decoded, as the card spells it:

```text
B1 ILUSKÁMDRÁGA
B2 MIKORLÁTHATOM?
B3 KÉREMARANYOM
B4 ÍRJON
T1 MILLIOFOR
T2 ROCSOK
T3 ÉDESEMNEK
```

The bottom block opens the message and the diagonal block closes it, followed by the monogram. Normalized Hungarian (word division, punctuation and the accents on MILLIÓ, FORRÓ, CSÓK are editorial):

**Tv. [Temesvár] 904 III/1. Iluskám drága, mikor láthatom? Kérem, aranyom, írjon. Millió forró csók édesemnek. [monogram]**

English translation: **[Temesvár] 1 March 1904. My dear little Ilus, when can I see you? Please, my golden one, write. A million hot kisses to my sweetheart. [monogram]**

Slovak translation: **[Temešvár] 1. marca 1904. Moja drahá Iluška, kedy Vás môžem vidieť? Prosím, zlatko, napíšte. Milión horúcich bozkov mojej milej. [monogram]**

Notes on the reading:

- **Iluska, Ilus** is the usual Hungarian pet form of Ilona, the addressee's name on the address side.
- **írjon** is the polite imperative ("write"), so the writer uses the formal address while calling her "my golden one" and "my sweetheart"; the Slovak translation keeps the polite Vás / napíšte.
- **édesemnek** is "to my sweet one" (dative of édesem).

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-916/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the four scans (source/ and work/hires/) and prints:

```text
B joined: ILUSKÁMDRÁGAMIKORLÁTHATOM?KÉREMARANYOMÍRJON
T joined: MILLIOFORROCSOKÉDESEMNEK
```

It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **Í of ÍRJON.** The first mark of bottom line 4 is not a Morse group: a long horizontal stroke turning down into a short slant with a tick, with a separate dot above it. Both solver and reviewer read it as a cursive í. The word ÍRJON ("write") is certain from the sentence, but this letter rests on word sense alone.
- **C of CSÓK.** Written `.-.-`, four clear elements, where standard Morse has `-.-.`. A slip or a private sign; the word is certain ("millió forró csók").
- **Stray marks.** Three small isolated dots above bottom line 2 (above the separator after M of MIKOR, above the separator between Á and T of LÁTHATOM, above the last dash of O in LÁTHATOM), and in bottom line 3 a dot below the separator before R of ARANYOM and an ink blob on the separator after it. None lies on the writing line as a Morse element, and none changes the reading; if the third dot in line 2 were an accent, it would make LÁTHATOM wrong.
- **S of ÉDESEMNEK.** The middle dot of `...` is an ink blot, larger than the others, but still one dot.
- **Separators.** Diagonal line 2 ends with K and no closing "/" stroke; the transcription follows the card.
- **Modern overprint.** The HCPORTAL.EU collection stamp covers the start of the diagonal lines and the monogram. The signs under it were read on enlargement by both solver and reviewer.
- **Monogram.** A looped initial crossed by a stroke, possibly two joined letters. The reviewer suggests a cursive A with a looped R, which would fit "Richter Antal" of HCP 1133, but this is a hypothesis and the monogram is reported as unread.
- **Date.** The dateline reads III/1 (1 March), the postmark seems to read APR 1, and the portal file name gives 1904-04-01. "Tv." as an abbreviation of Temesvár is an interpretation, supported by the Temesvár postmark and address.
- **Under the stamp.** The stamp is still attached, so nothing under it can be inspected from the scans; no writing shows at its edges or elsewhere on either side. Hidden messages under stamps are frequent on some Hungarian card series of this time, but none can be shown on this card, so no steganography is claimed.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (hashes OK, output identical to the claim), rotated the scan itself, read all seven lines on its own 2x to 5x crops, and decoded them with its own decoder; the result agreed group for group with the solver's. It confirmed in particular the three five-element Á groups, the L of LÁTHATOM, the Y of ARANYOM, the N before EK, the R at the start of diagonal line 2, the É under the overprint, and the hooked Í mark. It confirmed the name Márthé Ilona on the address side, that the language is natural Hungarian of the period, that the translations are correct, and that no published solution had been used. Its four findings were minor and are reflected here:

- **Stray marks in bottom line 3.** Now listed under Uncertainties and noted in the transcription file.
- **No closing "/" after diagonal line 2.** The transcription now omits it, with a comment; the decoded text is unchanged.
- **Modern HCPORTAL overprint.** Now stated in the context and the uncertainties.
- **Monogram.** The reviewer's A + R hypothesis is recorded; the monogram stays unread.

No decoded letter changed as a result of the review.

## Credits

Transcription, key transfer from HCP 1133 and decipherment: Claude Opus 5.5 (Anthropic), 2026-11-03. Independent review: a separate Claude Opus 5.5 agent. There was no earlier solver work on this card.

## Sources

- HC Portal record 916, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/916 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/2808/conversions/cpc_1904-04-01_HU_Temesvar_RO_Temesvar-Jozsefvaros__pic-large.jpg (source/picture-large.jpg); the original is in work/hires/.
- Address side: https://api.hcportal.eu/media/2809/conversions/cpc_1904-04-01_HU_Temesvar_RO_Temesvar-Jozsefvaros__adr-large.jpg (source/address-large.jpg); the original is in work/hires/.
- Sister card HCP 1133 in this repository (same recipient and address, same Á sign).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.
