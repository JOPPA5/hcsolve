# HCP 1469 (pc_hcp_150): a London love letter from Reg to Gertrude Forrest, 11 November 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (456 of 456 cipher signs, 120 words); independent review 1 verdict ACCEPT, no change to the decoded text.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1469 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1469), portal name pc_hcp_150, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-11-11, language Unknown, location Europe, sender Unknown, recipient Gertrude Forrest, with no transcription or solution attached.

The picture side is a printed view, "Thatched Cottages, Canford, Wimborne" (Dorset). The cipher is on the address side, a British "POST CARD" of "The Wellington Series" (G&P Ltd), with the printed note that the left half may be used for communication for inland postage only. The address is in plain writing: **Miss Gertrude Forrest, West Bank, Eastfield Road, Westbury-on-Trym, Bristol.** The halfpenny Edward VII stamp is cancelled LONDON; the day and year (11 … 07) are legible and agree with the plain date **11.11.07** written above the message. The circular alphabet and logo across both sides are the HCPortal watermark, not part of the cipher.

The message fills the left panel below the date (13 lines) and runs on into the top margin above and beside "POST CARD" (7 lines). It is signed *Reg*. No sister card in this repository uses the same alphabet, so the key was recovered from this card alone.

![Address side with the cipher text in the left panel and the top margin (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Thatched Cottages, Canford, Wimborne (source/picture-large.jpg)](../source/picture-large.jpg)

![Enlarged top margin: lines T1–T7, written around the printed POST heading and the Wellington Series crest (work/top.png)](../work/top.png)

![Enlarged left panel: body lines B01–B13 below the date 11.11.07 (work/body.png)](../work/body.png)

## Method

The only scan is 1024 × 674 px. The earlier GPT solver (2026-10-26) captured the portal page and the two scans and did a first triage, but found no key. Claude Opus 5.5 took the card over as solver on 2026-10-30.

1. **Sign inventory.** The text uses about twenty stroke signs (circle, three-shape, arch, bowls, box, caret, inverted T, and so on) plus small groups of one or two dots.
2. **Key recovery.** A rough first transcription was attacked with an English quadgram hill-climb. Shapes alone, each dot as its own token, and reversed lines gave nothing; treating each **dot group as one sign, distinguished by count and orientation**, gave English at once ("my own dearest … your letter this morning came in time for me to read it at breakfast …"). That first transcription and the quadgram model were scratch files and were not kept, so this discovery step **cannot be reproduced** from the repository. The reading does not depend on it; it rests on the kept transcription and key below.
3. **Final transcription.** Every line was then read again sign by sign on 4–10× enlargements (work/lines/, work/crops/). The faint dot groups of line B01 were also checked with a connected-component listing of the dots. The result is the manual transcription work/transcription.txt, one line per written line, with ASCII codes for the signs. No OCR was used.
4. **Decoding.** work/decode.py checks the hashes of the files in source/, decodes the transcription with the key and prints the plaintext and a count of lines, words and signs.

The reading order is body (B01–B13) then top margin (T1–T7): the body ends "the fog cleared" at the foot of the panel and the margin begins "a good bit …". All text is upright; an "inverted continuation" mentioned in the first triage does not exist.

## Key

Simple monoalphabetic substitution with invented signs; English. Four letters (e, g, h, i) are dot patterns, all others are strokes. Word spaces are kept.

| Letter | Sign | Letter | Sign |
|---|---|---|---|
| a | circle O | n | caret ∧ |
| b | three-shape 3 | o | circle with bar θ |
| c | rounded arch ∩ | p | bracket ⊐ with top bar |
| d | right bowl ↄ | q | circle with centre dot ⊙ |
| e | one dot | r | seven-shape 7 |
| f | gamma corner Γ | s | two-shape 2 |
| g | two dots falling (high-left, low-right) | t | inverted T ⊥ |
| h | two dots rising (low-left, high-right) | u | T on its side ⊢ |
| i | two dots vertical (colon) | v | angle > |
| j | reversed-J hook | w | caret ∧ (same sign as n) |
| k | angle < or ʞ with a stem | y | caret with a central stem |
| l | box □, sometimes with a divider | m | left bowl ( |

x and z do not occur. The caret is used for both n and w (see Uncertainties).

## Plaintext

Literal English, line by line, as decoded (the two places where the caret stands where r is expected are shown as capital R):

```text
B01 my own dearest girlie it is now almost
B02 half past five and i shall soon
B03 be clearing out and shall
B04 not be sorry either i was
B05 dRedful glad to get your
B06 letter this morning it came
B07 in time for me to read it at
B08 breakfast time it was quite
B09 foggy this morning and
B10 train was a bit late every
B11 time we have fog signals now
B12 makes me think of our journeys
B13 up together the fog cleared
T1  a good bit and it has been a fairly decent day
T2  goodbye for the present only four days now to wait
T3  i hope i have a
T4  letter from home tonight
T5  reg sends you dRedful lots
T6  of love and is always your
T7  own boy reg
```

Punctuated English (punctuation and the bracketed words are editorial):

**My own dearest girlie, it is now almost half past five and I shall soon be clearing out, and shall not be sorry either. I was dreadful glad to get your letter this morning; it came in time for me to read it at breakfast time. It was quite foggy this morning and [the] train was a bit late. Every time we have fog signals now [it] makes me think of our journeys up together. The fog cleared a good bit and it has been a fairly decent day. Goodbye for the present, only four days now to wait. I hope I have a letter from home tonight. Reg sends you dreadful lots of love and is always your own boy, Reg.**

Slovak translation: **Moje najdrahšie dievčatko, je skoro pol šiestej a čoskoro sa odtiaľto poberiem, a ani mi nebude ľúto. Strašne som sa potešil tvojmu listu dnes ráno; prišiel včas, aby som si ho prečítal pri raňajkách. Ráno bola dosť hmla a vlak trochu meškal. Zakaždým, keď teraz počujeme hmlové signály, spomeniem si na naše spoločné cesty hore [do mesta]. Hmla sa poriadne rozplynula a bol to celkom slušný deň. Zatiaľ zbohom, už len štyri dni čakania. Dúfam, že dnes večer budem mať list z domu. Reg ti posiela strašne veľa lásky a je navždy tvoj chlapec, Reg.**

Notes on the reading:

- **dreadful glad, dreadful lots** is colloquial English of the time for "dreadfully"; the writer spells it *dredful* both times (see Uncertainties).
- **clearing out** means leaving work for the day; **fog signals** are the detonators placed on railway lines in fog; **our journeys up together** are most likely trips up to London.
- **only four days now to wait** points to a meeting planned for about 15 November 1907. "A letter from home tonight" suggests that Reg was living away from his family.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1469/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the three files in source/ against work/source-sha256.json, decodes work/transcription.txt with the key, prints the twenty lines and the full text, and ends with `STATS: 20 lines, 120 words, 456 sign tokens, unknown=0, caret read as w=11, caret read as r=2`. The saved output is work/decoded.txt. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

- **n and w share one sign.** The caret stands for n in most words and for w in eleven places (own ×2, now ×3, was ×3, we, wait, always). Solver and reviewer both compared carets for n and w on enlarged crops (e.g. the two carets of *own*, which are identical) and found no stable difference in size or shape at this resolution. Every w is forced by context; no word has two sensible readings.
- **"dredful" twice.** In B05 and T5 the word is written d-caret-e-d-f-u-l, the caret standing where r is expected. Both solver and reviewer confirmed on crops that the sign is the caret, not the 7-shaped r. Because the spelling recurs, it is most likely the writer's habit or slip, not a transcription error; it is read as *dreadful*.
- **Faint dots.** e, g, h and i are written only as dots, which are small and sometimes faint at 1024 px (for example the e's of *together* in B13). The orientation that separates g (falling pair) from h (rising pair) is sometimes only a few pixels. Each word gives the only English reading, but a higher-resolution scan would settle the faint dots better.
- **Glyph variants.** l appears as a plain box and as a box with a divider (both in *shall*); k as < (*makes*) and as ʞ with a stem (*breakfast*, *think*); t sometimes has a hooked foot; the s of *is* (T6) has a lead-in stroke. None changes a reading.
- **The printed crest in T2.** The crown crest of The Wellington Series lies under the word *only* in T2. The w of *now* further to the right is a dark, blotted caret over the grey watermark band; its outline and the context (*four days now to wait*) agree.
- **Omitted words.** "the" before *train* and "it" before *makes* are not on the card; they are added only in the punctuated version, in brackets.
- **Not reproducible:** the statistical step by which the key was first found (see Method). The key and transcription themselves are in the repository and fully checked.
- The writer is known only as Reg; neither he nor Gertrude Forrest was identified outside the card. The London postmark is only partly legible; the date rests on the plain 11.11.07 on the card and agrees with the portal metadata.
- No published solution of this card was found: the portal shows Not solved with no transcription or solution, and the AI Decipherment Register had no record for it on 2026-10-29.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), in a separate session working only from the files in the cipher directory; round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decoded the transcription with its own independent script and key table (same 20 lines, 456 sign tokens, 120 words, every token mapped), made its own 4–10× crops and checked the transcription against the scan (B01–B06, B09–B13 and all of T1–T7 sign by sign, B07–B08 at 4×), confirmed the caret in both *dredful*, the reading order and the absence of inverted text, and checked the context (date, London postmark, Bristol address, portal metadata). It found no sign that a published solution had been used. Its four findings were minor:

- **Sign count.** SOLUTION.md said "about 500 signs"; the decoder now prints the exact count (456 sign tokens, 120 words).
- **Crest description.** The crest lies under *only*, not under the w of *now*; the description was corrected.
- **Reproducibility of key discovery.** The quadgram step is now stated plainly as not reproducible.
- **n/w.** The report now says that the carets for n and w were compared and show no stable difference.

No sign, key entry or plaintext word changed as a result of the review.

## Credit

- Portal capture, scans and first triage (no key, no reading): OpenAI GPT solver (GPT-6 Astra), 2026-10-26.
- Cipher identification, key recovery, transcription, decipherment, response to review and this report: Claude Opus 5.5 (Anthropic).
- Independent review: a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1469, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1469 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4468/conversions/pc_hcp_150_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4467/conversions/pc_hcp_150_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
