# HCP 1496 (pc_hcp_177): a number-cipher postcard to Highland Park, Kentucky

**Status: solved, accepted in independent review 1 (2026-10-26).** The whole message is written as numbers under the direct alphabet 1=A … 26=Z. All 93 numbers decode to coherent English under this single key.

## Origin and context

The card is item 1496 of the HCPortal cryptographic postcard collection (`pc_hcp_177`, private collection), https://crypto.hcportal.eu/dashboard/cryptograms/1496. The portal classes it as Substitution / Monoalphabetic, region North America, date and language Unknown, sender Unknown, recipient "Frederica Celark". At acquisition (2026-10-26) the portal status was **Not solved**, with no attached transcription or solution.

The address on the card reads **Miss Friderica Clark, Highland Park, Ky.** (Highland Park is a neighbourhood of Louisville, Kentucky). The first name is written with an i after the r, and the surname is Clark with a looped capital C; the portal's "Celark" appears to be a misreading of that C. The card is a Bamforth & Co. (Holmfirth and New York) postcard, no. 6025, marked "Copyright 1910", with a U.S. 1-cent Franklin stamp of the Washington–Franklin series, so it was sent in 1910 or later. The postmark shows only fragments (…AND, A…, 18) and gives no reliable date. The picture side carries only the printed caption "Good Bye."

![Address side of the card (source/address-large.jpg). The nine rows of numbers on the left are the message.](../source/address-large.jpg)

## Method

The message consists of nine rows of numbers between 1 and 26, separated by hooked commas. The first five numbers, 8 5 12 12 15, give HELLO under 1=A, 2=B, …, 26=Z, and the same direct alphabet then gives the whole message. The numbers were transcribed by hand from the scan and enlarged crops (no OCR; the portal has no transcription), then decoded by a script. The card has **no word dividers**: the long underline strokes under some numbers do not coincide with word boundaries (in row 1 they underline LO inside HELLO), and row ends split words (R/ICA, AR/E, WOUL/D, S/EE, SI/MON). Word division in the plaintext below is editorial.

## Key

A1Z26: the number n stands for the n-th letter of the English alphabet.

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | B | C | D | E | F | G | H | I | J | K | L | M |
| **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** | **24** | **25** | **26** |
| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |

Letters actually used: A B C D E F H I K L M N O P R S T U W Y.

## Plaintext

Transcription and literal decoding, row by row as on the card:

| Row | Numbers | Letters |
|---|---|---|
| 1 | 8 5 12 12 15 18 | HELLOR |
| 2 | 9 3 1 8 15 23 1 18 | ICAHOWAR |
| 3 | 5 25 15 21 9 23 15 21 12 | EYOUIWOUL |
| 4 | 4 12 9 11 5 20 15 19 | DLIKETOS |
| 5 | 5 5 25 15 21 9 19 1 23 19 9 | EEYOUISAWSI |
| 6 | 13 15 14 1 14 4 8 5 1 19 11 | MONANDHEASK |
| 7 | 13 5 9 6 9 8 1 4 2 5 5 14 | MEIFIHADBEEN |
| 8 | 21 16 8 15 13 5 20 8 1 20 12 15 15 11 19 | UPHOMETHATLOOKS |
| 9 | 2 1 4 1 14 19 19 15 15 14 6 13 19 | BADANSSOONFMS |

With editorial word division:

```
HELLO RICA HOW ARE YOU I WOULD LIKE TO SEE YOU
I SAW SIMON AND HE ASK ME IF I HAD BEEN UP HOME
THAT LOOKS BAD ANS SOON FMS
```

Normalized English: "Hello Rica, how are you? I would like to see you. I saw Simon and he ask[ed] me if I had been up home. That looks bad. Ans[wer] soon. FMS." The literal ASK (dropped -ed) and ANS (a common postcard abbreviation of "answer") are kept on the card's terms. "Up home" is regional for "back home"; no destination is established. Rica is plausibly a short form of the addressee's name Friderica.

Slovak translation: „Ahoj Rica, ako sa máš? Rád/rada by som ťa videl/videla. Videl/videla som Simona a pýtal sa ma, či som bol/bola doma. To vyzerá zle. Čoskoro odpíš. FMS.“ The writer's gender is unknown.

## Reproduction

From the repository root:

```
python3 -I ciphers/hcp-1496/work/decode.py
```

The script checks the SHA-256 hashes of the files in `source/`, decodes every number in `work/transcription.txt` (the manual transcription) with the A1Z26 key, checks the inverse mapping, and prints the text with the spacing from `work/words.txt`, after asserting that the spacing file contains exactly the decoded letters in order. Output ends with "Encrypted numeric positions: 93". The script checks the mapping, not the pixels; the transcription itself was checked against the scan by the reviewer.

## Uncertainties

- Handwritten 15 resembles 10, 14 resembles 19, and 2 resembles 3. The first 15 of LOOKS (row 8) is a closed blob and could graphically be 10; the last number of row 8 is a looped 19, not 15. The 2 of BEEN is read as 2.
- Row 6: the 4 of AND is written over another digit; 4 is the final form. The last number of row 6 (K of ASK) looks like 13 at normal size but is two plain strokes (11) when enlarged.
- Row 5: the 1 of SAW is a bare stroke squeezed between "19," and "23" and could be mistaken for a comma.
- In every one of these cases the alternative reading produces a non-word.
- Word division is editorial; the card has no word dividers.
- SIMON, FMS (the signature initials) and the place meant by "up home" are not identified. Rica = Friderica is a plausible inference only.
- No date beyond 1910 or later; the postmark is illegible.
- Absence from the AI Decipherment Register snapshot of 2026-10-26 does not prove that no decipherment was published elsewhere.

## Review summary

Reviewer: Claude Opus 5.5, round 1, verdict **ACCEPT**. The reviewer reran the command, transcribed all nine rows independently from their own enlarged crops (identical to the solver's 93 numbers), and decoded them with their own script. Findings, all minor:

- Additional doubtful glyphs (row 6 "4" and "11", row 5 "1", row 8 "15" and "19"): added to the uncertainties above.
- Underline strokes are not word dividers: stated in the Method section.
- Addressee spelling: the card's "Friderica Clark" is given without normalisation; the portal's "Frederica Celark" is noted as differing.
- Dating: the terminus post quem 1910 (copyright line and stamp) is added.

The plaintext did not change. The closing steps (response to the review, this report and the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request.

## Sources

- Portal page: https://crypto.hcportal.eu/dashboard/cryptograms/1496 (General, Description and Attachments tabs, read 2026-10-26).
- Address side: https://api.hcportal.eu/media/4549/conversions/pc_hcp_177_adr-large.jpg (`source/address-large.jpg`).
- Picture side: https://api.hcportal.eu/media/4548/conversions/pc_hcp_177_pic-large.jpg (`source/picture-large.jpg`).
- AI Decipherment Register snapshot: https://ai.hcportal.eu/register/?format=json (`work/register-snapshot.json`); no entry for this card.
- No published solution was used.
