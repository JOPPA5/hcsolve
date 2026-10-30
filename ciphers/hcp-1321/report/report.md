# HCP 1321 (pc_hcp_2): a birth announced in cipher on a Chislehurst postcard

Human solver: Tomáš Pavuk

**Status: cipher block deciphered in full (23 of 23 cipher signs); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1321 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1321), portal name pc_hcp_2, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date and language Unknown, location Europe, sender Unknown, recipient J. E. Fortescue, with no transcription or solution attached.

It is a British picture postcard, a coloured view numbered and titled "6073 The Lake. Chislehurst.", with cattle at a pond. The picture side has no handwriting.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address side carries an Edward VII halfpenny stamp, which dates the card to about 1902 to 1911. It is addressed to **Miss S. E. Fortescue, South St. House, Meopham, Kent**. The portal gives the initials as J. E., but the first initial has the same form as the S of "St." on the next line, so the evidence leans to S. The postmark could not be read for place or date. The message is written sideways on the left half.

![Address side (source/address-large.jpg)](../source/address-large.jpg)

Most of the message is in clear English. Three lines in the middle are in cipher. The writer enciphered only the private news.

![Message turned upright, with the three cipher lines between the clear text (work/crops/msg2x.png)](../work/crops/msg2x.png)

The clear text, with the place of the cipher marked:

```text
Dear P. If fine will come
[struck-out word] 6.40 (it's not altered.)
(Tomorrow Friday evening)
[three cipher lines]
All news later
With love to you all
Y[?] etc.  [monogram, perhaps J. B., A. B. or S. B.]
```

## Method

The solver, Claude Opus 5.5, made the transcription by hand from enlarged crops of the original scan. No OCR was used and there was no earlier work on this number. No sister card in the repository uses these signs, and no other Fortescue card was found there, so the key was recovered from this card alone.

Each sign was recorded as a shape and the position of a dot. The block has 23 signs and 13 distinct sign types. A pattern search on the seven-sign group with the double sign in places 2 and 3 offered ARRIVED and ALLOWED. ARRIVED made the square signs A and D, at opposite corners, which suggested that each shape covers a block of the alphabet. That pattern gave HEIR, LAST, NIGHT and SON. Earlier guesses such as MEETING and STAND gave no sensible rest.

Two features support the reading. Every sign decodes to a common English word, with nothing left over and no restoration. All 13 letters also fall in unbroken alphabet blocks by shape, which a random assignment of these signs would do about 3.3e-05 of the time. This second figure is a check on the key given the reading, not a language-free test: the letter values come from the English, it was computed afterwards, and it relies on three merges of sign variants described below.

## Key

A monoalphabetic substitution with geometric signs. The shape gives a block of the alphabet and a dot in the shape picks the letter. Only these 13 values are attested. B, C, F, J, K, M, P, Q, U, W, X, Y and Z do not occur, and no signs are assigned to them.

| Shape | Dot | Letter |
|---|---|---|
| Square | top left | A |
| Square | bottom right | D |
| Triangle | top | E |
| Triangle | lower right | G |
| Circle | top | H |
| Circle | left | I |
| Angle `<` | vertex | L |
| Angle `<` | lower arm | N |
| Angle `<` | upper arm | O |
| Diamond | top | R |
| Diamond | centre | S |
| Diamond | bottom | T |
| Caret `V` | no dot | V |

## Plaintext

Transcription as shape:dot codes, with the decoded words:

```text
DI:C AN:U AN:D  &  CI:T TR:T CI:L DI:T    SON & HEIR
SQ:TL DI:T DI:T CI:L VE:0 TR:T SQ:BR      ARRIVED
AN:V SQ:TL DI:C DI:B                      LAST
AN:D CI:L TR:LR CI:T DI:B                 NIGHT
```

**Original (English): Son & heir arrived last night**

Meaning: a son and heir was born last night.

Slovak: Syn a dedič prišiel na svet včera večer. (Doslova: "Syn a dedič dorazil včera v noci.")

The whole card in Slovak: Drahá P. Ak bude pekne, prídem [prečiarknuté slovo] o 6.40 (nie je to zmenené.) (Zajtra, v piatok večer.) Syn a dedič prišiel na svet včera večer. Všetky novinky neskôr. S láskou vám všetkým, Y[?] atď. [monogram]

To reproduce the decoding from the repository root, run `python3 -I ciphers/hcp-1321/work/decode.py`. It checks the hashes of the four image files and decodes `work/transcription.txt` with `work/key.json`.

## Uncertainties

- **The "&" is a reading, not a decipherment.** Line 1 has a thin looped scribble between the groups. It is not one of the shape signs. Its form and the set phrase "son and heir" make "&" natural, but it could be a cancelled sign. Without it the text is SON HEIR, and no enciphered letter depends on it.
- **Three merges of sign variants.** Circle with dot at upper right (line 1) and at top (line 3); triangle with dot at upper right and at top; and the tilted diamond closing line 1 with the two top-dotted diamonds of line 2. The writer's slant moves "top" to the upper right. The reviewer judged these sound on the pixels. In search, splitting them gave only word salad.
- **A variant square.** The second sign of LAST is drawn as a parallelogram. Its dot is top left, as in the A of ARRIVED, so it is read as the same sign.
- **Single-use signs.** The values of L, V, D, G and O each rest on one occurrence. *Arrived past night* fits every constraint, including the alphabet blocks, and only idiom selects LAST. SOL fails for SON because the same sign is N in NIGHT, and the *sol ... light* strings are nonsense.
- **Clear text not firmly read.** The struck-out word before 6.40, the letter after Y (perhaps a contraction before "etc."), and the monogram.
- **Date and people.** The postmark, and so the exact date and which Friday is meant, are not read. P., the sender and the child are not identified.
- **Prior publication.** Neither the solver nor the reviewer searched the web for a published solution. The portal showed Not solved, and the AI Decipherment Register had no record for this card on 2026-10-30.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The solver and reviewer are the same model, so this was not a cross-vendor review. The reviewer ran the reproduction command, made its own contrast-stretched 6x to 12x crops, and read all 23 signs before comparing: every sign agreed. It then searched with its own sign classes and word lists against the repeat pattern alone, without the solver's key. The only sentence-like results were the *son heir arrived last/past night* family. With the merges split, no rival sentence appeared. It confirmed the clear text, the picture side and the address.

Its six findings were all minor. None changed a decoded letter:

- **Brackets.** The card has two separate bracketed asides, "(it's not altered.)" and "(Tomorrow Friday evening)". The text and Slovak were corrected.
- **Single-use L.** The *past night* alternative and the other single-use signs are now disclosed.
- **Block check wording.** It was overstated as language-independent and has been corrected.
- **Reproducibility.** The solver's first search used a session word list that is not in the repository, so that run cannot be repeated. The reviewer's own search covers the same ground.
- **Slovak closing.** Now `Y[?]`, matching the English.
- **Addressee initial.** The solution now says the evidence leans to S rather than J.

The reviewer could not verify the postmark, the struck-out word, the monogram, or the scribble as "&"; these remain open as listed above.

## Sources

- HC Portal record 1321, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1321 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4023/conversions/pc_hcp_2_pic-large.jpg (source/picture-large.jpg); original at https://api.hcportal.eu/media/4023/pc_hcp_2_pic.JPG (work/hires/).
- Address side: https://api.hcportal.eu/media/4024/conversions/pc_hcp_2_adr-large.jpg (source/address-large.jpg); original at https://api.hcportal.eu/media/4024/pc_hcp_2_adr.JPG (work/hires/).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
