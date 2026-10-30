# HCP 1436 (pc_hcp_117): a Morse-code love note from Singapore, 1912

Human solver: Tomáš Pavuk

**Status: deciphered in full (105 letters in ten rows of International Morse; two non-Morse marks left undecoded); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1436 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1436), portal name pc_hcp_117, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection and Morse code, category Substitution, date 1912-05-27, language Unknown, location Europe, sender Unknown, recipient M. C. Hutton, with no transcription or solution attached.

The picture side is a printed view captioned "Botanical Garden, Singapore"; it carries no cipher. The address side, written sideways on the card, reads **M. C. Hutton, 94 Gunterstone Rd, West Kensington, London W., England.** It is cancelled SINGAPORE, 10.30 AM, 27 MY 1912. The lower half of the address side, below the printed dividing line, holds ten rows of pen dots and dashes, followed by two rows of small loops along the card edge.

![Picture side: Botanical Garden, Singapore (source/picture.jpg)](../source/picture.jpg)

![Address side as scanned (source/address.jpg)](../source/address.jpg)

![Address side turned upright (rotated 270°): the address and the Singapore postmark above, the ten Morse rows below, and the loop border along the bottom edge (work/upright.jpg)](../work/upright.jpg)

## Method

An earlier pass by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol, 2026-10-26) established the reading orientation (the scan rotated by 270°), identified the script as ordinary International Morse and froze a 98-letter excerpt, leaving the blotted and smudged places open. On 2026-10-29/30 Claude Opus 5.5 re-read every group on 4× to 10× enlarged crops, completed the transcription and wrote a one-command decoder.

The writing conventions are simple: dots and dashes are written in a row, a short upright stroke separates letters and a double stroke separates words. The transcription was made by hand, sign by sign, from the enlargements; no OCR was used. The decoder checks the SHA-256 hashes of both scans and of the metadata, then decodes the transcription with the standard Morse table. Doubtful marks were measured in pixels against the clean dots (11–17 px) and dashes (27–36 px) of the same row.

The reviewer, a separate Claude Opus 5.5 agent, rotated the scan itself, cut its own crops of all ten rows, transcribed the card without using the solver's file, and decoded its transcription with its own script and its own Morse table. The output was **identical** to the solver's: 105 letters, the same word division and the same two non-Morse marks.

## Key

The key is the standard International (Continental) Morse alphabet; no letter is given a private value, and there is no substitution on top of the Morse.

| Letter | Code | Letter | Code | Letter | Code | Letter | Code |
|---|---|---|---|---|---|---|---|
| A | .- | H | .... | N | -. | T | - |
| C | -.-. | I | .. | O | --- | U | ..- |
| D | -.. | K | -.- | P | .--. | V | ...- |
| E | . | L | .-.. | R | .-. | W | .-- |
| G | --. | M | -- | S | ... | Y | -.-- |

Only the letters in the table occur on the card. Two marks are not Morse letters and have no letter value: a heavy horizontal **long stroke**, about four dash-lengths long, at the start of row 6, and a looped **ink blot** between the two words EVER in row 9. The long stroke is not a dash and is not read as T; it is probably punctuation or a cancellation. The two rows of loops along the bottom edge contain no dots or dashes and are an ornamental border.

## Plaintext

Transcription, row by row (`/` separates letters, `//` separates words), with the literal decoding below each row. Lower-case letters are restorations or judgments, explained under Uncertainties.

```text
R01 -- / -.-- // --- / .-- / -. // -.. / .- / .-. / .-.. / .. / -. / --.
    MY OWN DARLING
R02 --. / .. / .-. / .-.. / .. / .
    GIRLIE
R03 .-- / [---] / ..- / .-.. / -.. // -.-- / --- / ..-
    WoULD YOu
R04 .-.. / .. / -.- / . // .- // -. / .. / -.-. / . // .-.. / --- / -. / --.
    LIKE A NICE LOng
R05 .-- / .- / .-.. / -.- // .-. / --- / ..- / -. / -.. // - / .... / .. / ...
    WALK ROUND THIS
R06 [long stroke] // .--. / .- / .-. / - // .... / --- / .-- // .. //
    ... / .... / --- / ..- / .-.. / -..
    [long stroke] PART HOW I sHOULD
R07 .-.. / --- / ...- / . // - / --- // - / .- / -.- / . // -.-- / --- / ..-
    LOVE TO TAKE YOU
R08 -.. / .- / .-. / .-.. / .. / -. / --.
    DARLING
R09 . / ...- / . / .-. // [blot] // . / ...- / . / .-. // -.-- / --- / ..- / .-.
    EVER [blot] EVER YOUR
R10 --- / .-- / -. // --- / -- / .- / .-.
    OWN OMAR
```

English original (punctuation is editorial; "—" stands for the long stroke, which has no letter value):

**My own darling girlie, would you like a nice long walk round this — part? How I should love to take you, darling. Ever [blot] ever your own, Omar.**

The language is plain Edwardian English, so no translation is strictly needed. In modern English: **My own darling girl, would you like a nice long walk round this part [of the world]? How I would love to take you, darling. Ever [and] ever your own, Omar.**

Slovak translation: **Moje vlastné drahé dievčatko, chcela by si sa pekne dlho prejsť po tomto kúte? Ako rád by som ťa vzal, drahá. Navždy [a] navždy tvoj vlastný, Omar.**

The invitation to "a nice long walk round this part" fits the picture side, the Botanical Garden in Singapore, from where the card was posted to a young woman in London.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1436/work/decode_full.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of source/address.jpg, source/picture.jpg and source/metadata.md against work/source-sha256.json, decodes the manual transcription in work/full-transcript.json with the standard Morse table, and prints (long lines wrapped here):

```text
MY OWN DARLING GIRLIE WoULD YOu LIKE A NICE LOng WALK ROUND THIS
[LONGSTROKE] PART HOW I sHOULD LOVE TO TAKE YOU DARLING EVER [BLOT]
EVER YOUR OWN OMAR
105 letters decoded (5 disclosed restorations/judgments shown in lower
case); source hashes OK.
```

It does not read the image; the transcription step is manual and was repeated independently in review.

## Uncertainties

The scan is 1024 px wide, about 2.5 px per dot, and no higher-resolution original is available. 100 of the 105 letters are read from clean marks; the other five are:

- **wOuld (restoration).** An ink blot covers the first two marks of the second group of row 3; its last dash is visible and the blot is about two dash-lengths wide. Only O (`---`) gives a word.
- **yoU.** The first mark of the last group of row 3 is a 24 px lump with a notch, read as two touching dots (`..-`). The other two U's on the card are clean.
- **loNG.** In row 4, after `---`, there is a clean dash, then a grey smudge about 1.5 dashes wide crossed by a letter divider, then a clean dash and a dot. The reading `-. | --.` places two marks inside the smudge: the dot of N and the first dash of G. LONG is the only word that fits.
- **sHOULD or RHOULD.** The first group of the last word of row 6 is dot, a 24 px mark, dot. The mark lies between the dot and dash sizes of that word. Read as a dot it gives S (SHOULD); read as a short dash it gives R, the literal RHOULD recorded by the earlier GPT pass. The reviewer also judged it visibly shorter than the dashes beside it. The meaning does not change.

Other points:

- **The long stroke** before PART and **the looped blot** between the EVERs are not Morse and are not decoded. The blot may be a hand-drawn "&" or a cancelled AND; "ever [and] ever" in the translation is an interpretation only.
- **PART, not PARK.** The final group of that word is a single clean dash (T). PARK (`-.-`) would suit the garden picture, but it is not on the card.
- **OWN.** A divider-like stroke crosses the junction of the two dashes of W in row 10. Taken literally it would split the word into nonsense; it is treated as a stray stroke.
- **Omar.** The signature `--- / -- / .- / .-.` is read from clear groups, but it is tightly spaced: the dot of A touches the divider to its right. "Omar" may be a pet name rather than the writer's given name. Neither the sender nor the recipient M. C. Hutton has been identified in outside records.
- No prior publication of this card's reading is known: the portal status was Not solved with no attached solution, and the AI Decipherment Register had no record for it when checked on 2026-10-29.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command and confirmed the source hashes, made its own upright frame and enlarged crops of every row, transcribed the card independently and decoded it with its own script; the result was identical to the solver's. It checked every disclosed point on the pixels, sampled and confirmed the ordinary rows, confirmed that the picture side carries no Morse and that the loop rows are a border, and judged the text fluent period English that fits the Singapore 1912 context. Its three findings were minor:

- **Two marks in the LONG smudge.** The smudge holds both the dot of N and the first dash of G, so G is now also marked as a judgment (five lower-case letters instead of four; 100 instead of 101 letters from clean marks).
- **Signature spacing.** The note on OMAR now says that the dot of A touches the divider and that the name may be a pet name.
- **The long stroke.** This report states plainly that it has no letter value and is not a T.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1436, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1436 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4369/conversions/pc_hcp_117_adr-large.jpg (source/address.jpg).
- Picture side: https://api.hcportal.eu/media/4368/conversions/pc_hcp_117_pic-large.jpg (source/picture.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
