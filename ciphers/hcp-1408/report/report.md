# HCP 1408 (pc_hcp_89): "My Valentine", a sighing-cipher rebus

Human solver: Tomáš Pavuk

**Status: read in full (44 of 44 signs); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1408 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1408), portal name pc_hcp_89, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, with category, period and language Unknown, location Europe, sender "F. E. Cotby" and recipient Aimee S. Farrar, and no transcription or solution attached.

The card is a **US 1-cent McKinley postal card** (a design in use from about 1902 into the 1910s), addressed in plain handwriting to **Aimee S. Farrar, Hillsboro, N.H.** It carries no visible postmark or date, so the date rests only on the stamp design. The portal's location "Europe" is therefore a **portal metadata error** (probably a collection default), not a fact about the card.

The message side has a plain handwritten heading *My Valentine*, a five-sign line underlined by a long stroke, four lines of capital letters and ovals, and a plain signature. The signature is read here as **F. E. Colby** (the third letter is an uncrossed looped ascender, i.e. "l"); the portal's "Cotby" is kept as metadata. Neither the sender nor the recipient has been identified further.

![Picture (message) side (source/picture.jpg)](../source/picture.jpg)

![Enlarged verse: the heading line and four verse lines (work/verse-large.jpg)](../work/verse-large.jpg)

![Address side: Aimee S. Farrar, Hillsboro, N.H., on a 1-cent McKinley postal card (source/address.jpg)](../source/address.jpg)

The large circular alphabet and the padlock-and-building logo on both sides are the HCPortal watermark, not part of the card.

## Method

The transcription is **manual**, from enlarged crops of the scan; the portal supplied none. It has 44 signs:

```text
OONOO
UOAOOIOU
ONOOOOMETOO
UOAOIDOSO
IONOOIOBUTU,
```

All ovals have the same shape: the writer does not distinguish the digit 0 from the letter O. The mark after the last U is punctuation, not a sign.

The card is **not a substitution cipher** but an English **letter rebus** (a gramogram). It is built on an old pun: a *cipher* is a zero, a nought, and "cipher" sounds like **"sigh for"**. So the oval 0 can be read as the noun "cipher" (zero, a nobody) or as the verb "sigh for". This is the well-known 19th-century "sighing riddle", whose classic form runs approximately "U 0 a 0, but I 0 U; O 0 no 0, but O 0 me …". That quotation is given from memory and is approximate only: a newspaper column on famous puzzles that reproduces the riddle (Trove article 32700190) was found by search, but neither solver nor reviewer could open the page. The card is a home-made variant of that riddle.

The letters U, I and A stand for their names ("you", "I", "a"), and the remaining capitals spell plain words: NO, ME, TOO, DO, SO and BUT. Which role an oval plays (verb, noun, or the interjection "O") is decided by grammar, since every oval looks the same. The solver recorded the segmentation of each line in work/rebus-key.json, and the decoder checks that it uses every one of the 44 signs exactly once.

An earlier attempt (OpenAI GPT, 2026-10-26) made the first transcription and tried "U = you / I = I" letter-name readings, but treated the ovals as free wildcards. That gave several unrelated, equally fitting fragments (e.g. URAQTILU, YNOTCOMETOO). This showed that a common rule was needed, and those readings were dropped.

## Key

| Sign / token | Reads |
|---|---|
| oval in verb position | "sigh for" |
| oval in noun position | "cipher" (a zero, a nobody) |
| oval standing alone before a clause | interjection "O" |
| U, I, A | you, I, a (letter names) |
| NO, ME, TOO, DO, SO, BUT | the plain words |

Segmentation, line by line:

```text
OONOO        -> O | O | NO | O
UOAOOIOU     -> U | O | A | O | O | I | O | U
ONOOOOMETOO  -> O | NO | O | O | O | ME | TOO
UOAOIDOSO    -> U | O | A | O | I | DO | SO
IONOOIOBUTU  -> I | O | NO | O | I | O | BUT | U
```

## Plaintext

English (original; punctuation editorial):

> **O, sigh for no cipher!**
>
> **You sigh for a cipher, O I sigh for you;**
> **Sigh for no cipher, O sigh for me too;**
> **You sigh for a cipher, I do so;**
> **I sigh for no cipher, I sigh for but you.**

Sense: you are pining for a nobody (a "cipher", a zero), while I pine only for you; do not sigh over a nobody, sigh for me. The rhymes you / too / so / you and the parallel you/I lines fit a short valentine verse.

Slovak translation (the pun cannot be kept; *cipher* = nula, "a nobody"):

> **Ó, nevzdychaj za nulou!**
>
> **Ty vzdycháš za nulou, ó, ja vzdychám za tebou;**
> **nevzdychaj za nulou, ó, vzdychaj aj za mnou;**
> **ty vzdycháš za nulou, ja tiež;**
> **ja nevzdychám za nulou, ja vzdychám len za tebou.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1408/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in source/, checks that the segmentation in work/rebus-key.json uses each of the 44 transcribed signs in work/transcription.txt exactly once, and prints the segmentation and the five-line plaintext. It does not read the image: the transcription is manual and was confirmed independently in review.

## Uncertainties

- **Role of each oval.** Every oval looks the same, so whether one is read as "sigh for", "cipher" or the interjection "O" is decided by grammar. The commas, the exclamation mark and the placement of the interjection "O" (heading, lines 2 and 3) are editorial. Other placements give the same sense (e.g. line 2 "O, sigh for no cipher, sigh for me too"; "O I sigh" as "oh, I sigh").
- **Sense of line 4 (unclear).** The signs U-O-A-O-I-DO-SO are certain: the D is a clear D and there is no oval between I and D. Read literally, "You sigh for a cipher, I do so" says that the writer also sighs for a cipher, which sits awkwardly beside line 5, "I sigh for no cipher". Possible intended senses:
  - "You sigh for a cipher – I do so [sigh, for you]";
  - a question: "Do you sigh for a cipher? I do so";
  - "so" in the sense of "too".

  The card does not decide between them.
- **Heading.** OONOO is read as "O, sigh for no cipher!", the same construction as the start of verse line 2 (third line of signs) and the classic riddle's "O 0 no 0".
- **Signature.** Colby (here) or Cotby (portal); the scan favours an "l".
- **Date and persons.** No postmark: the date (about 1902–1910s) rests only on the stamp design. F. E. Colby and Aimee S. Farrar are not identified.
- **The classic riddle.** It is quoted only approximately, from memory. The background source (Trove 32700190) was seen only as a search result.
- **Prior publication.** No published reading of this card was found by web search (2026-10-29 and 2026-10-30); the portal attached none; the AI Decipherment Register had no entry for it (2026-10-29).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer:

- ran the reproduction command, whose output was identical to the claimed plaintext;
- made its own 4× crops of the heading, the four lines and the signature, and read all 44 signs itself, agreeing with the transcription;
- confirmed that the D is a D, the I's are not 1's, and there is no separate 0 versus O shape;
- wrote an independent decoder (review/work/indep_decode.py) with its own tokenizer and a different, rule-based assignment of the oval's roles; it reproduced the same segmentation and plaintext for all five lines;
- found no published solution.

Its four findings were minor and are reflected here:

1. **Sense of line 4.** The tension with line 5 and the possible intended senses are now stated, and the sense is marked unclear.
2. **Riddle quoted from memory.** The classic riddle is now given only as an approximate form, with the unopened source named.
3. **Portal location "Europe".** This is now reported as a portal metadata error.
4. **Editorial punctuation.** The note that punctuation and interjection placement are editorial is kept.

No sign, token or word of the reading changed as a result of the review.

Credit: setup, scan capture, metadata and the first transcription (44 signs, later verified as correct) were done by an OpenAI GPT solver (GPT-6 Astra) on 2026-10-26; it did not find the oval rule. The "cipher = sigh for" reading, the key, the decoder and the write-up are by Claude Opus 5.5 (2026-10-29). The response to the review and this report were also written by Claude Opus 5.5 (2026-10-30).

## Sources

- HC Portal record 1408, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1408 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4284/conversions/pc_hcp_89_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4285/conversions/pc_hcp_89_adr-large.jpg (source/address.jpg).
- Background on the sighing riddle (not opened): https://trove.nla.gov.au/newspaper/article/32700190
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
