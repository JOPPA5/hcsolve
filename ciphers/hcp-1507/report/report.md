# HCP 1507 (pc_hcp_188): a number-cipher love note to Leah Doane, 1913

Human solver: Tomáš Pavuk

**Status: accepted in independent review 1 (ACCEPT); final edition, 2026-10-26.**

## Origin and context

The card is record 1507 of the HCPortal cryptographic postcards collection (https://crypto.hcportal.eu/dashboard/cryptograms/1507), portal name pc_hcp_188, held in a private collection. The portal lists the main category as Substitution / Monoalphabetic, the date as 1913-05-10, the location as North America, the sender as Unknown and the recipient as "Leeah Doane". When the solver acquired it on 2026-10-26 the record was marked **Not solved**, with no attached transcription or solution.

The address side reads "Miss Leah Doane, Little Marsh, Pa." and carries a one-cent Washington stamp with the postmark KNOXVILLE, MAY 10, 10 AM, 1913, PA. The catalogue spelling "Leeah" is a variant; the address and the decoded greeting both give LEAH. The numeric message is written sideways in the left half and dated `5-10-13` (one digit of the day overwritten), in agreement with the postmark. A plain-language note across the top reads "Please come to the store first thing". The picture side is a printed Dutch-themed comic card ("Vhen vill ve meet to shveet nodings shpeak") with no cipher. The large lettered disk over the scan is the portal's watermark, not part of the card.

![Address side; the numeric message is written sideways at the left (portal scan)](../source/address-large.jpg)

## Method

There is no attached transcription. The solver transcribed the numbers by hand from rotated, enlarged crops (`work/transcription.txt`). Dots separate letters, dashes separate words, and three cursive words (Sat. Eve., Good.) are written in plain English. The solver took the key from the neighbouring card HCP 1508 as a hypothesis and checked it on this card: DEAR LEAH, EXPECT, TOWN, RIDE, GOOD, HONEY, LOOK and SWEETHEART all confirm it, and LOOK fixes 14=K. All 93 numeric positions are decoded by a single key, with no per-word exceptions. The numbers are not a simple A1Z26 alphabet: the assignment looks arbitrary.

## Key

| Number | Letter | Number | Letter | Number | Letter |
|---|---|---|---|---|---|
| 1 | M | 3 | E | 4 | R |
| 6 | L | 7 | O | 8 | T |
| 9 | P | 10 | S | 11 | F |
| 12 | A | 13 | G | 14 | K |
| 16 | U | 17 | I | 18 | D |
| 20 | C | 21 | W | 22 | H |
| 24 | X | 25 | N | 26 | Y |

21 distinct numbers occur; each gives one letter and no letter has two numbers.

## Plaintext

Literal decoded text, line by line as on the card (plain cursive words in mixed case):

```
MY DEAR LEAH
I EXPECT TO
SEE YOU IN
TOWN Sat. Eve. DEAR
DOR ME
A RIDE W ILL DO
YOU GOOD HONEY
I WILL LOOK FOR
YOU SWEETHEART
Good. N IGHT
```

W ILL and N IGHT are split on the card by the writer's own dashes and join to WILL and NIGHT. DOR is exactly what is written (see Uncertainties).

Normalized reading: "My dear Leah, I expect to see you in town Sat. eve. Dear, [for?] me a ride will do you good, honey. I will look for you, sweetheart. Good night."

Slovak translation: „Moja drahá Leah, očakávam, že sa uvidíme v meste v sobotu večer. Drahá, [pre mňa?] jazda ti prospeje, miláčik. Budem ťa vyzerať, drahá. Dobrú noc."

## Reproduction

From the repository root:

```
python3 ciphers/hcp-1507/work/decode.py
```

It checks the SHA-256 hashes of the scans and metadata, decodes `work/transcription.txt` with the key above, checks the inverse-key round trip, and reports 93 encrypted positions. It does not read the image; the transcription is manual.

## Uncertainties

- DOR (`18.7.4`, line 5): written as such; the sign is clearly the writer's 18, not 11. Two guesses, neither adopted: FOR ("Dear, for me a ride…"), which would need 11 instead of 18; or DO with a stray `4` ("Dear, do me…").
- SEE (`10.3.3`, line 3): the second digit of the first number is between this writer's `0` and `8`. Read as 18 the word would be DEE; context fixes SEE.
- The cursive signature below the last line (possibly an "E" monogram with "t." or "r.") is not read. The sender is unidentified.
- The "xx×" marks at lower right and the cross marks after ME and NIGHT are not cipher numbers (probably kisses).
- The wording "Dear, [for] me a ride will do you good" is awkward even with a correction; no smoother rewriting is offered as recovered text.

## Review summary

The reviewer was Claude Opus 5.5 (Anthropic) and the verdict was **ACCEPT**. The reviewer read all 93 numeric signs from enlarged crops without looking at the solver's file, and the two transcriptions agree token for token. The reviewer's own decoder, which uses no code from the solver, gives the same text with no unmapped numbers, and the documented command reproduces the claimed output byte for byte. Four minor findings, all incorporated as disclosures:

- SEE is uncertain at sign level: now listed in Uncertainties.
- DOR: the literal reading is kept; FOR and "do me" are both given as guesses.
- Header date: read as `5-10-13`, matching the postmark; now given above as the date of the card.
- Cross-card evidence: HCP 1506 (pc_hcp_187) has the same recipient and the same key, and its header group `24.24.24` decodes to XXX with 24=X. This supports the key, but HCP 1506 is still in its own review and is cited only as corroboration.

The key and plaintext did not change as a result of the review. The closing steps (response to review, this report, register entry) were prepared by Claude Opus 5.5 on behalf of the solver (OpenAI GPT-6 Astra) at the human's request.

## Sources

- Portal record: https://crypto.hcportal.eu/dashboard/cryptograms/1507 (General, Description and Attachments tabs, read 2026-10-26).
- Address side: https://api.hcportal.eu/media/4582/conversions/pc_hcp_188_adr-large.jpg
- Picture side: https://api.hcportal.eu/media/4581/conversions/pc_hcp_188_pic-large.jpg
- Related cards in this repository: HCP 1508 (source of the key hypothesis, partial) and HCP 1506 (same recipient and key, in review).
- AI Decipherment Register snapshot (https://ai.hcportal.eu/register/?format=json, 110 records): no entry for this card. This is not proof that no solution was ever published.
- No published solution was used.
