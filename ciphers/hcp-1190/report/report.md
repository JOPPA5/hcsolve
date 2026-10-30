# HCP 1190 (cpc_1907-09-14_USA_Carthage, NY_USA_Denmark, New York_): a dotted Pigpen postcard to Ruth

Human solver: Tomáš Pavuk

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-26.

## Origin and context

The cryptogram is record 1190 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1190), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was acquired on 2026-10-25 the portal listed it as **Not solved**, tagged Postcard and Pigpen, language Unknown, with no transcription or solution attached.

It is an American picture postcard published by G. W. Schmid, Carthage, N.Y. The picture side shows Kings Falls near Carthage and carries no cipher. On the address side the cancel reads CARTHAGE N.Y., SEP 14, 4.30 PM, and a faint receiving backstamp reads DENMARK, SEP 14. The card is addressed to "Miss Ruth [surname not securely read], Denmark, New York"; the portal shows the recipient as "Miss Ruth tis". The portal date is 1907-09-14 (a Saturday); the cancel itself shows no legible year. Below the five lines of cipher the sender signed in plain writing with the initials W.D.M. Carthage and Denmark, N.Y., are about ten miles apart, so same-day delivery is plausible.

![Address side with the five cipher lines on the left (source/address-large.jpg)](../source/address-large.jpg)

## Method

The cipher consists of 38 Pigpen-type outlines in five lines, each outline carrying one, two or three dots, with hyphens between words and a comma after the fourth line. The transcription is **manual**: each sign was recorded as an outline (which sides of the cell are drawn) plus a dot count in work/transcription.txt. The portal supplied no transcription.

The alphabet was not derived from this card alone. The solver carried over the grid alphabet it had just established for the related card HCP 1193, replacing that card's small numerals by dot counts. Applied to this card it gave English at once, covering all 38 signs: the decoded text, not the transfer, is what confirms the key. 17 distinct signs occur; repeated letters (I ×4, O ×5, N ×3, T ×3, H ×3 and others) are drawn the same way each time, and no sign has two values.

In review the transcription was checked independently, sign by sign, against enlarged crops of the scan, including the faint dot groups the solver had flagged. The reviewer's own reading, decoded with its own script, agrees with the solver's for all 38 signs.

## Key

A dotted three-block Pigpen variant. The cells of a plain 3×3 grid are taken in the order A–I; one dot selects A–I, two dots J–R, three dots S–Z. J is not omitted, so the ninth three-dot cell is unused.

| Outline (sides drawn) | 1 dot | 2 dots | 3 dots |
|---|---|---|---|
| bottom + right | A | J | S |
| bottom + left + right | B | K | T |
| bottom + left | C | L | U |
| top + bottom + right | D | M | V |
| all four sides | E | N | W |
| top + bottom + left | F | O | X |
| top + right | G | P | Y |
| top + left + right | H | Q | Z |
| top + left | I | R | (unused) |

## Plaintext

As written on the card (hyphens and the comma are on the card):

```text
I - SHALL - BE -
THINKING - OF -
YOU - TONIGHT -
RUTH,
BE - GOOD
```

Normalized English (capitals and full stops editorial): **I shall be thinking of you tonight, Ruth. Be good.**

Slovak translation: **Dnes večer budem na teba myslieť, Ruth. Buď dobrá.**

The plain initials W.D.M. below the cipher are not part of the encrypted text.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1190/work/decode.py
```

The script checks the SHA-256 hashes of the source files, decodes the manual transcription in work/transcription.txt with the key above and checks an exact sign-to-letter round trip. It does not read the image; the transcription step is manual (and was confirmed independently in review).

## Uncertainties

- The year 1907 rests on the portal catalogue; the cancel shows only SEP 14, 4.30 PM, and the Denmark backstamp is faint.
- The recipient's surname and the person behind the initials W.D.M. are not established.
- Several dot groups are faint (final T of TONIGHT, the letters of RUTH, the Y of YOU, the G of THINKING); solver and reviewer read all of them the same way. Reading the G with two dots would give the non-word THINKINP.
- Faint pencil marks under OF in line 2 are illegible and are not part of the cipher.
- The alphabet was transferred from HCP 1193 rather than derived independently; it is confirmed here only by the coherent result over all 38 signs.
- A bounded check of Schrödel (2021) found no published plaintext for this card; this does not prove that no earlier decipherment exists.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, read all 38 signs from the scan in its own notation before comparing, decoded them with an independently written decoder, and found no sign-level differences. It checked key consistency, the context (postmarks, addressee Ruth, the Saturday date) and the provenance check. Its three findings were minor and are reflected here:

- The reproduction decodes a manual transcription: this report now states that the transcription was verified sign by sign in review.
- The key was transferred, not derived: the system is named a dotted three-block Pigpen variant and its origin in the HCP 1193 work is stated.
- Punctuation: the full stops and capitals of the normalized reading are marked as editorial; the card has hyphens and one comma.

No change to the plaintext resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1190, General, Description and Attachments tabs, captured 2026-10-25: https://crypto.hcportal.eu/dashboard/cryptograms/1190 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/3631/conversions/cpc_1907-09-14_USA_Carthage,-NY_USA_Denmark,-New-York__adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/3630/conversions/cpc_1907-09-14_USA_Carthage,-NY_USA_Denmark,-New-York__pic-large.jpg (source/picture-large.jpg).
- Tobias Schrödel, "Cryptographic postcards", HistoCrypt 2021: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 (source/schroedel-2021.pdf), consulted after the reading was obtained.
- Internal: the grid alphabet of ciphers/hcp-1193/, applied here as a hypothesis.
