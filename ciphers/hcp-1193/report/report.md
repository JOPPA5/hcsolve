# HCP 1193 (cpc_1907-12-08_USA_Kingston, NY_USA_New York_): a numbered-Pigpen love postcard to Helen, December 1906

Human solver: Tomáš Pavuk

**Status: deciphered (223 cipher signs; 214 read directly, 4 restored from a water stain, 4 ambiguous between two letters in the signature, 1 sign outside the key); independent review 1 verdict ACCEPT, no change to the decoded text.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1193 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1193), portal name `cpc_1907-12-08_USA_Kingston, NY_USA_New York_`, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-10-25 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection and Pigpen, category Substitution / Monoalphabetic, date 1907-12-08, language Unknown, location North America, recipient "M. R. Rod.", with no transcription or solution attached. The collection is described in T. Schrödel, "Cryptographic postcards", HistoCrypt 2021 (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166).

The message side carries thirteen lines of small box-shaped signs, each with a tiny numeral 1, 2 or 3, under a clear-text header *Friday. 9 P.M.* followed by a short mark that probably reads "’06". A water stain covers the left margin, and the HC Portal collection stamp covers the lower right corner, including the end of the signature.

The address side is in plain writing to Mrs. M. R. Rod[?]mond (the surname is not securely read), Oyster Bay, New York. The postmark reads KINGSTON N.Y. / DEC 8 / 7 A / 190[6], with a Rondout Station cancel, and a receiving stamp is also dated DEC 8. 7 December 1906 was a Friday, so the card was most likely written on Friday evening 7 December 1906 and posted the next morning. The catalogue date 1907-12-08 fell on a Sunday and is probably one year off. This is an observation only. The portal record has not been changed.

![Message side (source/picture-large.jpg). The water stain is on the left, the collection stamp at the lower right](../source/picture-large.jpg)

![Address side, with the Kingston N.Y. postmark and the address in Oyster Bay, New York (source/address-large.jpg)](../source/address-large.jpg)

## Method

The tag "Pigpen" and the shapes themselves suggested a Pigpen-like cipher. Each sign is the outline of one cell of a 3×3 # grid, which has nine shapes, and the small numeral raises the number of letters to 27. The OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol, 2026-10-25) took the outlines in the natural order of the grid, so numeral 1 gives A–I, numeral 2 gives J–R and numeral 3 gives S–Z. The words HELEN, NOT GET THE LETTER and EXPECTED TONIGHT then appeared at once. That solver transcribed lines 1–11 by hand and decoded them with a short script.

On 2026-10-30 Claude Opus 5.5 checked every sign again against the full-resolution scan (`source/picture-original.jpg`, 3468×2298 pixels), using enlarged, slightly rotated crops with enhanced contrast. This collation confirmed lines 1–10. It found the word SO in line 11, which the first transcription had missed, and it transcribed lines 12–13 for the first time. The transcription was done by hand. A script then applies the key mechanically and also checks the SHA-256 hash of each source file.

A separate Claude Opus 5.5 reviewer rebuilt the key from the geometry of the grid alone, without the solver's list of shapes, and decoded the transcription with its own script. Its output matched letter for letter. It also cut its own crops of the scan and checked a sample of ordinary lines and every difficult sign.

## Key

Monoalphabetic substitution of the Pigpen family. A letter is a cell outline plus a numeral that selects its block.

| Outline (strokes present) | 1 | 2 | 3 |
|---|---|---|---|
| bottom + right | A | J | S |
| bottom + left + right | B | K | T |
| bottom + left | C | L | U |
| top + bottom + right | D | M | V |
| all four sides | E | N | W |
| top + bottom + left | F | O | X |
| top + right | G | P | Y |
| top + left + right | H | Q | Z |
| top + left | I | R | (27th cell, no letter) |

Word gaps, punctuation (`,` `.` `?` `-`) and a cursive `&` are written in the clear. The same alphabet decodes the sister cards HCP 1131, 1189 and 1190 in this repository. Those cards mark the block with dots instead of numerals.

## Plaintext

Decoded text, line by line. `{x}` marks a sign restored from the stain, `[x/y]` an ambiguous sign with the preferred reading first, `<TL3>` the sign outside the key, and `~` marks under the stamp that cannot be read.

```text
{W}ELL HELEN MY <TL3>, I DID
NOT GET THE LETTER I
EXPECTED TONIGHT - WAS
IST LOSDENN MIT DIR? - WELL
SWEETHEART AS I WILL BE
THERE ALMOST AS SOON AS
{T}HIS CARD, I WILL ONLY
{T}ELL YOU HOW MUCH I MISS
YOU & HOW MUCH I WILL
LOVE YOU, TO MAKE UP FOR
IT WHEN I SEE YOU. SO GOOD
{N}IGHT, LOVE & KISSES YOUR
[F/C]ETT[S/J][O/L]C[K/L] ~
```

The text is in English with one German question. It is written WAS IST LOSDENN MIT DIR, with no gap inside LOSDENN. Idiomatic German would be *Was ist denn los mit dir?*

Normalized: **Friday, 9 P.M. ’06. Well Helen my ⟨?⟩, I did not get the letter I expected tonight — *was ist los denn mit dir?* — Well sweetheart, as I will be there almost as soon as this card, I will only tell you how much I miss you & how much I will love you, to make up for it when I see you. So good night, love & kisses, your FETTSOCK …**

English translation (the German part translated): **Well Helen my [?], I did not get the letter I expected tonight — what is the matter with you? Well sweetheart, as I will be there almost as soon as this card, I will only tell you how much I miss you and how much I will love you to make up for it when I see you. So good night, love and kisses, your [signature: FETTSOCK, possibly the German nickname *Fettsack*, "fatso" (an interpretation)].**

Slovak translation: **Nuž, Helen, moja [?], dnes večer som nedostal list, ktorý som čakal — čo sa to s tebou deje? Nuž, miláčik, keďže tam budem takmer súčasne s touto pohľadnicou, napíšem ti len, ako veľmi mi chýbaš a ako veľmi ťa budem ľúbiť, aby som ti to vynahradil, keď ťa uvidím. Tak dobrú noc, láska a bozky, tvoj [podpis: FETTSOCK, možno nemecká prezývka *Fettsack*, „tlstoch“ (interpretácia)].**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1193/work/decode_full.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the five files in `source/`, decodes the hand-made symbolic transcription in `work/transcription-full.txt` with the key above, and prints the thirteen lines shown, followed by the count `223 cipher signs: 4 restored {}, 4 ambiguous [], 1 outside the key <>`. It does not read the image. The transcription step is manual, and the review checked it independently.

## Uncertainties

- **The sign after MY (line 1)** has a clear top-and-left outline with numeral 3. This is the 27th cell, which has no letter in the key. It is probably a private sign for an endearment, but it is reported as written and not read as a word.

  ![The sign outside the key after MY (work/opus/glyph_q.jpg)](../work/opus/glyph_q.jpg)

- **Four restorations in the water stain.** The first sign of four lines has lost its left and/or bottom strokes:
  - `{W}ELL` (line 1): numeral 3, outline faint. SELL, TELL, WELL and YELL are all possible. WELL is chosen because line 4 has "WELL SWEETHEART", so this is a choice from context.
  - `{T}HIS` (line 7): numeral 3 and a right stroke are visible. THIS is the only reading that makes a word.
  - `{T}ELL` (line 8): numeral 3 and a right stroke are visible. TELL is chosen from context ("I will only tell you how much I miss you").
  - `{N}IGHT` (line 12): the top stroke, the right stroke and numeral 2 are clear. N (all four sides) is read from the word, because the only alternative with these strokes, P (top + right), would give PIGHT.
- **KISSES, sign 6 (line 12).** The outline is clearly bottom + right, but the numeral is a single open hook rather than the two-bowled "3" of the neighbouring signs, and it could be taken for a "2". Numeral 2 would give J (KISSEJ), so S is read from the word.
- **The signature (line 13)** is given literally as FETTSOCK, with four ambiguous signs:
  - Sign 1 is F or C, because its top stroke touches the tail of the `&` above.
  - Sign 5 is S or J, because its numeral is loose.
  - Sign 6 is O or L, because its "top" may be the end of a long underline from line 12.
  - Sign 8 is K or L, because its right side runs into the stamp.

  The likeness to German *Fettsack* ("fatso", a jocular name for oneself) is only an interpretation: the scan shows O, not A. Further marks under the collection stamp may be one or two more signs or a flourish. Neither the solver nor the reviewer could read them.

  ![Start of the signature, F E T (work/opus/G12.jpg)](../work/opus/G12.jpg)

- **People.** The writer's identity is not known. The addressee's surname is not securely read, and her initials may be M. R. or M. P. The message calls her Helen.
- **Date.** The year 1906 rests on the postmark and the "’06" of the header, whose last digits are partly covered, and on the weekday agreement.
- **Provenance of the full-resolution scan.** `source/picture-original.jpg` was saved by an earlier session that did not record its download URL. It is presumably the portal's original image of media 3639. Its SHA-256 is recorded, and its content matches `source/picture-large.jpg`, whose URL is recorded.
- **Prior publication.** The portal status was Not solved, no solution was attached, and the AI Decipherment Register had no entry for this card. The HistoCrypt 2021 article that describes the collection was checked only at the level of its landing page and abstract. Its PDF was not examined, so it is not established that no decipherment of this card was published before.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent. Round 1, verdict **ACCEPT**.

The reviewer ran the reproduction command, and its output matched the claimed plaintext. It wrote an independent decoder that derives the key from the geometry of the grid, and that decoder agreed letter for letter. It counted the 223 signs and found an English-like frequency profile. On its own crops of the full-resolution scan it confirmed the sign outside the key, the added SO, lines 12–13, the four stain restorations and the 1906 dating.

There were five findings, all minor:

1. The loose numeral in KISSES was not flagged. It is now disclosed in SOLUTION.md, as a comment in the transcription file and in this report. The reading S is unchanged.
2. NIGHT depends on context. This was already disclosed and is repeated above.
3. The download URL of `source/picture-original.jpg` is not recorded. The "not recorded" note is kept, together with the hash and the match with `picture-large.jpg`.
4. The translations made the *Fettsack* reading sound settled. They now say "possibly … (an interpretation)".
5. The HistoCrypt PDF was not examined. This is now stated in this report.

No decoded letter changed as a result of the review. The reproduction command was run again after the edits and gave the same output.

**Credit.** The key and the first reading of lines 1–11 are the work of the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol, 2026-10-25). On 2026-10-30 Claude Opus 5.5 made the full collation, added SO and lines 12–13, and wrote the response to the review and this report. The independent review was by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1193, General, Description and Attachments tabs, captured 2026-10-25: https://crypto.hcportal.eu/dashboard/cryptograms/1193 (`source/metadata.md`).
- Message side: https://api.hcportal.eu/media/3639/conversions/cpc_1907-12-08_USA_Kingston,-NY_USA_New-York__pic-large.jpg (`source/picture-large.jpg`). The full-resolution `source/picture-original.jpg` has no recorded URL (see Uncertainties).
- Address side: https://api.hcportal.eu/media/3640/conversions/cpc_1907-12-08_USA_Kingston,-NY_USA_New-York__adr-large.jpg (`source/address-large.jpg`).
- T. Schrödel, "Cryptographic postcards", HistoCrypt 2021: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 (landing page only).
- AI Decipherment Register, https://ai.hcportal.eu/register/, checked 2026-10-25 and 2026-10-29: no entry for this card.
