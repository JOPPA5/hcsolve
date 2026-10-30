# HCP 1477 (pc_hcp_158): a Swedish friendship verse in cipher, Rommehed 1904

Human solver: Tomáš Pavuk

**Status: deciphered (143 of 143 cipher signs read with one key); independent review 1 verdict ACCEPT. One line of the verse (line 7, "ingen ging sbät") decodes letter by letter but is not understood.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1477 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1477), portal name pc_hcp_158, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1904-05-09, language Unknown, location Europe, sender Unknown, recipient Sara Erickson, with no transcription or solution attached.

It is a Swedish picture postcard, "Rommehed. St. Tuna." (publisher N. Aug. Hedblom, Falun), showing a village street with a small wooden photographer's studio ("Nya Fotografi-Atelier"). Rommehed lies in Stora Tuna parish, Dalarna. Several texts in plain Swedish surround the picture: a short verse in the sky, a dated greeting below the picture ("Rommehed den 9/5 04. Många kära hälsningar …", 9 May 1904), and a line along the left margin. The cipher is the narrow strip in the right margin: four lines written with the card turned 90° clockwise.

The address side is in plain writing, a "Brefkort" addressed "Till Fröken Sara Erickson", with a place in Västerdalarna (the address lines are only partly legible); a 5-öre Swedish stamp is cancelled ST. TUNA with day 9. The address side carries no cipher.

![Picture side as scanned; the cipher is the four-line strip in the right margin (source/picture-large.jpg)](../source/picture-large.jpg)

![The cipher strip turned 90° clockwise, 2× enlarged; read top line first (work/strip-clockwise.png)](../work/strip-clockwise.png)

![Address side: Fröken Sara Erickson; ST. TUNA cancellation (source/address-large.jpg)](../source/address-large.jpg)

## Method

The scans and metadata were downloaded by an earlier OpenAI GPT solver session (2026-10-26), which left the card unread. The transcription and decipherment were done by Claude Opus 5.5 on 2026-10-29.

The strip was cropped, turned and enlarged 4–10×, and read sign by sign by hand (no OCR) into `work/transcription.txt`, one token per written sign. Vowels turned out to be written in clear, so only the consonant signs had to be solved. First models (the two-dot sign ":" as a word separator, X = n) and automatic hill-climbing gave nonsense. The breakthrough was to treat ":" as a letter: the opening then reads "har du ingen vän i vär(l)den", giving ":" = n, X = r and the dotted X = v. The rest of the verse followed, and the digit signs were seen to be the positions of the letters in the consonant row b c d f g h j k l.

In review, a separate Claude Opus 5.5 agent made its own crops, read all four lines sign by sign in its own notation, decoded them with its own script and key, and obtained the same 143 signs and the same text except for the two points listed under the review below.

## Key

Partial substitution with vowels in clear. The vowels a e i o u å ä ö are written normally (å with a dot, ä and ö with a small 2- or ^-shaped mark); y is written as i. Consonants are replaced by signs. The consonants from b to l take their position in the consonant row b c d f g h j k l; the later consonants have ad-hoc signs.

| Sign | Letter | Sign | Letter |
|---|---|---|---|
| 1 | b | – · (dash then dot) | m |
| 3 | d | : (two dots) | n |
| 5 (also a heavy closed б-like 5) | g | ⁝ (three dots) | p |
| 6 | h | X | r |
| 8 | k | ÷ (dash, dot above and below) | s |
| 9 | l | dash with dot below | t |
| | | X with dot above | v |

c, f and j (positions 2, 4 and 7) do not occur in the text. The digit part (b1 d3 g5 h6 k8 l9) is a coherent construction that a private writer would naturally make.

## Plaintext

Literal decryption, as printed by the reproduction command (word division supplied by the transcriber):

```text
har du ingen vän i värden den du trikt kan
lita nå litet ödslig blir då härden men var
glad ändå. vänskap brites bandet brister knits
igen ingen ging sbät man mister som en vän.
```

As the rhymed verse it is (trochaic; rhymes världen/härden, på/ändå, brister/mister, igen/vän), with the writer's spellings and slips normalised in brackets:

```text
Har du ingen vän i värden [världen],
den du trikt [tryggt; or trigt] kan lita nå [på],
litet ödslig blir då härden,
men var glad ändå.
Vänskap brites [brytes], bandet brister,
knits [knytes] igen,
ingen ging sbät [?] man mister
som en vän.
```

English translation: **Have you no friend in the world whom you can safely rely on, the hearth becomes a little desolate then; but be glad all the same. Friendship is broken, the bond bursts, is tied again; [line 7 not understood: "ingen ging sbät"] one loses … as a friend.**

Slovak translation: **Nemáš na svete priateľa, na ktorého sa môžeš pevne spoľahnúť, trochu pusté je potom ohnisko (domov); ale buď aj tak veselá. Priateľstvo sa láme, puto praská, znova sa zaväzuje; [7. riadok nezrozumiteľný: „ingen ging sbät“] človek stráca … ako priateľa.**

Notes on the reading:

- The text is an album or friendship verse of the kind written on cards of the period, in two quatrains with consistent metre and rhyme. It fits the plain greeting on the same card.
- The writer spells phonetically: i for y (trikt, brites, knits), no l in värden (världen; the rhyme with härden confirms the word).
- 33 of the 35 decoded words are ordinary Swedish words or transparent spellings of them; the two exceptions are "ging" and "sbät" in line 7.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1477/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the two scans and the metadata in source/, decodes the manual transcription in work/transcription.txt with the key in work/key.json, and prints the four literal lines above followed by `[143 signs decoded, 4 lines]`. It does not read the image; the transcription is manual and was checked independently in review.

## Uncertainties

- **Line 7, "ingen ging sbät".** Every sign is clear on the scan and decodes as shown (both solver and reviewer read it the same way), but the words make no sense as written. Metre and sense suggest something like *ingenting så lätt man mister* ("nothing does one lose as easily"), but that would need two writer errors (the heavy 5 as t; "sbät" for "så lätt"). This is a conjecture only and is not adopted.
- **"nå" for "på" (line 2).** The sign before å has two dots (n), not the three dots of p seen in *vänskap*. *lita på* is certain from sense and the rhyme på/ändå, so it is read as a writer's slip; the literal output keeps "nå".
- **One glyph, two values.** A tall g-like glyph with a descender appears in *trikt*, *vänskap* and *igen*. It looks the same each time and differs from the plain 8 of *kan* and *knits*. It is read k in *trikt* and *vänskap* and g in *igen* by context only. Read as g in line 1, the word is *trigt*, closer to *tryggt*; *trikt* and *trigt* are equal alternatives.
- The heavy closed б-like sign is taken as a variant of 5 = g (from *glad*); whether it is a deliberate variant or a correction is not known.
- The ö in *ödslig* is a dark round blob with the 2-mark, read as ö.
- The scan gives only about 140 × 674 pixels for the strip. The dots that separate s from t are 1–2 pixels; every one was checked and none contradicts the decoded words, but a better scan would make the reading firmer.
- Word division and the verse layout are editorial. The source of the verse is not known: two web searches (2026-10-29) for decoded lines found no published text; a printed source could settle line 7.
- The sender is not identified; the address lines beyond the recipient's name are only partly legible.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**, with no blocker or major findings. The reviewer ran the reproduction command (output identical to the claimed plaintext), made its own crops and enlargements of every line, transcribed all 143 signs in its own notation, decoded them with its own key, and confirmed that each consonant sign is used consistently and confirmed in several independent words. It judged the text to be genuine rhymed Swedish of the period, not words forced onto noise. Its four minor findings and what changed:

- **"på" is written with two dots.** Accepted. The transcription now records the two dots, so the literal output reads "nå", and the slip is listed among the uncertainties.
- **One g-like glyph read two ways.** Accepted. The uncertainties now say plainly that one glyph is read k or g by context, and *trigt* is given as an equal alternative to *trikt*.
- **Word count.** Corrected to 33 of 35 words.
- **Line 7 in the translations.** The English and Slovak translations now carry an explicit gap marker instead of a phrase that read as a complete sentence.

Apart from the literal "nå", no decoded letter changed as a result of the review.

## Sources

- HC Portal record 1477, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1477 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4491/conversions/pc_hcp_158_pic-large.jpg (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/4492/conversions/pc_hcp_158_adr-large.jpg (source/address-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
