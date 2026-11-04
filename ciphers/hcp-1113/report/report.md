# HCP 1113 (cpc_1909-07-30_DE_Freiburg-(Schlesien)_DE_Hier_fritzlehmann-06): a number-cipher love note to Fritz Lehmann

Human solver: Tomáš Pavuk

**Status: deciphered in full (44 of 44 cipher numbers); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1113 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1113), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Fritz Lehmann, with no transcription or solution attached. The portal links the HistoCrypt article https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 as a general reference for the collection.

The picture side is a printed photographic card titled "Gretchen", with the Faust caption "Was ist das? Gott im Himmel! Schau, Ein Schmuck!"; it carries no handwriting. The address side has a Germania 5-pfennig stamp of the Deutsches Reich, cancelled **FREIBURG (SCHLESIEN) 30.7.09** (30 July 1909; today Świebodzice, Poland). The address is in plain Kurrent pencil: **Herrn Fritz Lehmann, Hier, Alte L...straße** ("Mr Fritz Lehmann, here [local delivery], Alte L... street"). The message is written in pencil, sideways, on the left half of the address side, as dotted groups of numbers.

The card is one of a group of cards to Fritz Lehmann in the same collection. The sister card HCP 1134, also posted in Freiburg (Schlesien) and also signed "Susi", uses the same number cipher; this card was checked against it.

![Address side (source/address-large.jpg)](../source/address-large.jpg)

![Message area turned upright, from the high-resolution scan (work/message-upright.png)](../work/message-upright.png)

![Picture side, printed only (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, made from the un-converted high-resolution scan of the address side (3468 x 2298 px) by Claude Opus 5.5. The message area was turned upright and every number was read on 3-4x enlargements; the doubtful signs (the first numeral, the two struck-through 19s, the barred 13 and the retraced 14) were compared with other occurrences of the same digits on the card. Dots separate letters and dashes separate words.

The number set (2 to 26, no 1, no number above 26) and the sister card HCP 1134 pointed to a plain number alphabet. The key A=2 ... Z=26 with J omitted decodes all 44 numbers into German; no number is left over and no letter is adjusted. A bar over a number doubles the letter (13 with bar = MM in BESTIMMTEN).

The reviewer read the scan independently, wrote its own decoder and obtained the same 44 numbers and the same German text.

## Key

Number substitution (simple monoalphabetic), German, 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |

| O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

Numbers occurring on this card: 2 3 4 5 6 8 9 10 12 13 14 18 19 20 21 26.

## Plaintext

Transcription, row by row (x marks the extra diagonal stroke on a 19, = the bar over 13):

```text
8.6.12.10.6.3.20.6.18.
19x.4.9.2.20.26! -
3.10.14. - 26.21.18. -
3.6.19.20.10.13=.20.6.14.
19x.20.21.14.5.6. -
3.6.10. - 5.10.18.
5.6.10.14.6. -
19.21.19.10.
```

Decoded:

```text
GELIEBTER
SCHATZ! -
BIN - ZUR -
BESTIMMTEN
STUNDE -
BEI - DIR
DEINE -
SUSI
```

German, normalized: **Geliebter Schatz! Bin zur bestimmten Stunde bei dir. Deine Susi.**

English: **Beloved darling! I will be with you at the appointed hour. Your Susi.**

Slovak: **Milovaný poklad! V dohodnutú hodinu budem u teba. Tvoja Susi.**

The note confirms a rendezvous; "Hier" in the address shows the card was posted for local delivery in Freiburg itself.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1113/work/decode.py
```

The script checks the SHA-256 hashes of the two source scans and the high-resolution address scan, then decodes the manual transcription work/transcription.txt with the key above and prints the eight decoded rows. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **First numeral (G of GELIEBTER).** An open, S-shaped numeral with a separate top stroke. It differs from this writer's 5s (three on the card), so it is read as an open-written 8; there is no other 8 on the card to compare, and 5 would give the non-word DELIEBTER. The call rests partly on word sense.
- **Diagonal strokes on two 19s.** The 19s that begin the nouns Schatz and Stunde carry an extra heavy diagonal stroke; the underlying 1 and 9 are visible. Its purpose is unknown: it may mark a capital or be a correction stroke. It does not affect the decoding, because without the S the words would be CHATZ and TUNDE.
- **Last number of BESTIMMTEN** is 14 with a heavily retraced 1.
- **Street name.** The street in the plain address, "Alte L...straße", is one unread word: the middle letters are crossed by the portal watermark and are not legible with confidence. It is not part of the message.
- **Persons.** "Susi" is a name or nickname; neither she nor Fritz Lehmann is identified beyond the card.
- **Hidden writing.** The stamp is still affixed, so anything written under it cannot be checked on these scans; no ink shows at its edges. The picture side carries only printed text. No steganographic message was found on this card.
- **Prior publication.** One web search on 2026-11-03 found no published solution of this card; the portal had none attached.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (all hash checks OK, output identical to the claimed plaintext), cut and rotated the message from the high-resolution scan itself, read all 44 numbers and decoded them with its own script; its reading agreed with the solver's number for number. It confirmed the key against the sister card HCP 1134, the doubling bar on 13, the retraced 14, the postmark date and place, and that neither side shows other writing. Its four minor findings and what changed:

- **First numeral 8 vs 5.** Disclosure kept as written (above).
- **Diagonal strokes on the 19s.** The earlier wording "capital marker" is replaced by "purpose unknown (capital marker or correction stroke)".
- **Street name.** Now stated as one unread address word instead of "read loosely".
- **Register type.** MASC; no steganography was found on this card, so the label MASC + Steganography does not apply.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1113, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1113 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3399/conversions/cpc_1909-07-30_DE_Freiburg-(Schlesien)_DE_Hier_fritzlehmann-06_pic-large.jpg (source/picture-large.jpg) and the original https://api.hcportal.eu/media/3399/cpc_1909-07-30_DE_Freiburg-(Schlesien)_DE_Hier_fritzlehmann-06_pic.jpg.
- Address side: https://api.hcportal.eu/media/3400/conversions/cpc_1909-07-30_DE_Freiburg-(Schlesien)_DE_Hier_fritzlehmann-06_adr-large.jpg (source/address-large.jpg) and the original https://api.hcportal.eu/media/3400/cpc_1909-07-30_DE_Freiburg-(Schlesien)_DE_Hier_fritzlehmann-06_adr.jpg.
- Sister card: HCP 1134 in this repository (same recipient and signature, same key).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.
