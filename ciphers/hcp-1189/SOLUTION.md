# HCP 1189 — full candidate reading, awaiting independent review

## Plaintext

```text
DEAR VELMA
I LOVE YOU.
```

Normalized punctuation: **Dear Velma, I love you.**

Slovak: **Milá Velma, ľúbim ťa.**

All 17 encrypted letters on the address side are included. No encrypted
letters were observed on the picture side. Punctuation after VELMA in the
normalized reading is editorial, not an extra cipher symbol.

## Cipher and key

Pigpen outlines with one, two or three dots. Key transferred from the
preceding HCP1193/HCP1190 analyses, not independently rediscovered here.
The catalogue already supplies the Pigpen classification.

| Outline strokes | Token | 1 dot | 2 dots | 3 dots |
|---|---|---|---|---|
| bottom/right | BR | A | J | S |
| bottom/left/right | B | B | K | T |
| bottom/left | BL | C | L | U |
| top/bottom/right | R | D | M | V |
| four sides | C | E | N | W |
| top/bottom/left | L | F | O | X |
| top/right | TR | G | P | Y |
| top/left/right | T | H | Q | Z |
| top/left | TL | I | R | unused |

## Reproduce

From repository root:

```sh
python3 ciphers/hcp-1189/work/decode.py
```

The command verifies source hashes and decodes work/transcription.txt,
a manual solver-authored transcription of the image. The portal supplied
no transcription. This command does not OCR the scan: the pixel-to-token
step is disclosed manual work and still needs independent checking.

## Why this reading and what remains uncertain

One unchanged alphabet covers all glyphs, including repeated E, A, L, O
and V. The decoded VELMA matches the unencrypted forename in the address.
The first V has closely clustered dots and the following E has a dark
single-dot blob; the reviewer should independently collate these against
the scan. No ciphertext gap has been replaced with a contextual guess.
The very short message limits independent statistical evidence.

The catalogue date is unknown; no year is claimed from the postmark.
The sender's identity and any relationship beyond the literal words are
not established. No published plaintext was used and no claim to first
historical decipherment is made. This is a complete solver candidate,
not a review-accepted final solution.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-26). The reviewer ran the documented command, decoded with its own independently written script (review/work/review_decode.py), and read all 17 signs from enlarged crops of source/address-large.jpg; its reading (review/work/reviewer-reading.txt) is identical to work/transcription.txt and decodes to the same text. The plaintext is unchanged: DEAR VELMA / I LOVE YOU.

1. V and E of VELMA decided by the address, not by dot count (minor). Accepted, and stated plainly here and in the report. On the scan the first sign of VELMA (top/bottom/right outline) shows **two** separable dots, the same visible count as the M two signs later; the right-hand dot is elongated and may be two merged dots. Read strictly by visible dots it would be M, giving MELMA. The following E carries one wide blob about twice the width of a single dot, which by itself could also be read as two merged dots (N, giving e.g. VNLMA). The reading V (three dots) and E (one dot) is chosen because VELMA is the forename of the addressee written in plain on the same card ("Miss Velma Cornel"), and it is consistent with the key: the V of LOVE uses the same outline with three clearly separate dots, and E occurs twice more with one dot (DEAR, LOVE). For these two signs the address is therefore the deciding evidence, not merely corroboration as the earlier text put it. All other 15 signs read unambiguously.
2. Reproduction only round-trips a manual token list (minor). Accepted. work/decode.py decodes the manual outline/dot transcription and does not read the image; its round-trip assertion checks only internal consistency of the key and is not evidence for the reading. The evidence for the transcription is the sign-by-sign collation in review 1, which agrees for all 17 signs (with the two VELMA signs resolved as in finding 1). The script's closing line "Independent visual review is still pending" is superseded by review 1; work/ is left unchanged.

Remaining uncertainties carried into the report: no date is claimed (the stamp is a 1-cent Washington of the 1908–1914 design type and the machine cancel shows a day "30" without a legible year, so c. 1909–1915 is plausible but not established); the postmark town is not securely read; the recipient's surname "Cornel" is less secure than the forename; the sender is unknown; the key was transferred from HCP 1193/1190 rather than derived from this card alone, and the 17-sign text is too short for independent statistical support; no published plaintext was found, which does not prove none exists.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
