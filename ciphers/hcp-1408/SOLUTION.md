# HCP 1408 / pc_hcp_89 — "My Valentine" sighing-cipher rebus

**Status: complete reading (Claude Opus 5.5, 2026-10-29), handed to review as DONE1.**
Portal status when captured (2026-10-26): Not solved; no transcription or solution attached.
No published solution of this card was found.

## Card

US 1-cent McKinley postal card (issue in use c. 1902–1910s), addressed to
**Aimee S. Farrar, Hillsboro, N.H.** No date or postmark visible. Message side:
handwritten heading *My Valentine*, a 5-sign heading line (underlined by a long
stroke), four verse lines in capitals, signature read as **F. E. Colby** (portal
metadata says "F. E. Cotby"; the cursive "l"/"t" is not decisive; kept literal).

## Cipher type and key

Not a substitution cipher but an English **letter rebus** (gramogram) built on the
old pun **cipher = zero = "sigh-for"**, the 19th-century "sighing riddle" type
(classic version: "U 0 a 0, but I 0 thee; O 0 no 0, but 0 me…"). Key:

| sign / token | reads |
|---|---|
| oval O in verb position | "sigh for" |
| oval O in noun position | "cipher" (a zero) |
| oval O standing alone before a clause | interjection "O" |
| U / I / A | you / I / a (letter names) |
| NO, ME, TOO, DO, SO, BUT | the plain words |

The key and the sign-by-sign segmentation are in `work/rebus-key.json`.

## Transcription (read on enlarged crops, 44 signs)

```
OONOO
UOAOOIOU
ONOOOOMETOO
UOAOIDOSO
IONOOIOBUTU,
```
(the final mark after the last U is a comma/full-stop-like dot; not a cipher sign)

## Plaintext (English, original)

> O, sigh for no cipher!
>
> You sigh for a cipher, O I sigh for you;
> Sigh for no cipher, O sigh for me too;
> You sigh for a cipher, I do so;
> I sigh for no cipher, I sigh for but you.

Meaning: "you" long for a nobody (a "cipher", a zero), the writer longs only for you;
do not sigh over a nobody, sigh for me.

**Slovak translation:** „Ó, nevzdychaj za nulou! / Ty vzdycháš za nulou, ó, ja vzdychám za tebou; /
nevzdychaj za nulou, ó, vzdychaj aj za mnou; / ty vzdycháš za nulou, ja tiež; /
ja nevzdychám za nulou, ja vzdychám len za tebou.“ (pun: *cipher* = nula / „vzdych-za“).

## Command (from repo root)

```sh
python3 -I ciphers/hcp-1408/work/decode.py
```

Checks SHA-256 of all `source/` files, checks that the segmentation consumes each of
the 44 transcribed signs exactly once, prints the segmentation and the plaintext.

## Uncertainties

1. **Ambiguity is inherent to the rebus:** every oval looks the same on the card (no
   distinct 0 vs O shapes on the enlargements), so which oval is "sigh for", "cipher"
   or interjection "O" is resolved by grammar. Alternatives exist only in punctuation /
   interjection placement (e.g. line 2 as "O, sigh for no cipher, sigh for me too"
   — same sense). Line 1 "O I sigh" could also be meant as "oh, I sigh"; same sense.
2. Line 3 "I do so" (= I do sigh so / I do the same) is read literally from D-O-S-O;
   there is no extra oval there.
3. The heading OONOO is read as "O, sigh for no cipher!" (= the classic riddle's
   line "O 0 no 0"); it is the same construction as the start of verse line 2.
4. Signature: Colby vs portal "Cotby" not decided; recipient's middle initial "S."
   from portal and scan.
5. The pun convention is supported by memory of the classic riddle and a search hit
   (Trove newspaper article 32700190, "the sighing riddle", about O standing for
   sigh and cipher); that page could not be opened (access denied), so the exact
   historical text was not verified.

## Why it is correct

- Covers all 44 signs with one rule set; no sign is skipped or invented.
- Unciphered context ("My Valentine") matches a love verse; the literal plain words
  on the card (NO, ME TOO, DO SO, BUT U) only make sense with O = sigh-for/cipher.
- Each line is grammatical English and the four lines are parallel (you/I contrast),
  the rhyme you / too / so / you fits a short verse.
- Matches the well-known 19th-c. "sighing riddle" form.

## Credit

Setup, scan capture, metadata and the first transcription (44 signs, verified here
on the pixels and found correct) were done by an OpenAI GPT solver on 2026-10-26;
it considered U=you / I=I letter-name readings but did not find the O rule.
The O = cipher = "sigh for" reading, key, decoder and this write-up: Claude Opus 5.5,
2026-10-29.

## Response to review 1

Review 1 (Claude Opus 5.5, 2026-10-30): verdict **ACCEPT**, four minor findings. The
transcription, key and plaintext are unchanged; the reproduction command
`python3 -I ciphers/hcp-1408/work/decode.py` was re-run on 2026-10-30 and still prints
"source hashes OK", "all 44 signs covered by the segmentation" and the same five lines.

1. **Sense of line 4 (agree, clarified).** The signs U-O-A-O-I-DO-SO are certain on the
   scan (the D is a clear D; there is no oval between I and D), so the words "You sigh
   for a cipher, I do so" stand. Read literally, "I do so" (= I sigh for a cipher too)
   sits awkwardly beside line 5 ("I sigh for no cipher"). Possible intended senses:
   (a) "You sigh for a cipher – I do so [sigh, i.e. for you]"; (b) a question, "Do you
   sigh for a cipher? I do so"; (c) "so" in the sense "too". The card does not decide
   between them; the intended sense of line 4 is therefore marked **unclear**. This
   affects only the interpretation, not the reading of any sign.
2. **Classic riddle quoted from memory (agree).** The quotation in the key section above
   ("U 0 a 0, but I 0 thee; O 0 no 0, but 0 me…") is from memory and is only the classic
   form, approximately; the Trove article 32700190 could not be opened by either solver
   or reviewer. The report quotes it only as an approximate form and does not present it
   as a verified source text.
3. **Portal location "Europe" (agree).** The card is a US 1-cent McKinley postal card
   addressed to Hillsboro, N.H.; the portal field Location: Europe is a portal metadata
   error (probably a collection default) and is reported as such, not as a fact about
   the card.
4. **Punctuation and interjection placement are editorial (agree).** Kept as stated in
   uncertainty 1; the report repeats that the commas, the exclamation mark and the
   choice of which oval is the interjection "O" (heading, line 2, line 3) are editorial.

No file in work/ needed to change. Next step: report and FINAL.
