# HCP 1190 — full candidate reading, awaiting independent review

## Cipher and key

Pigpen with three dot counts. For any outline, one dot selects the first
alphabet block, two dots add nine, and three dots add eighteen. There is
no J omission. The outlines and alphabet are:

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

This alphabet was transferred from the preceding HCP1193 analysis,
replacing its numerals with dot counts. The Pigpen family was already
identified in the catalogue. Neither family identification nor a new
general cipher method is claimed here.

## Plaintext

With line breaks and separators represented:

```text
I - SHALL - BE -
THINKING - OF -
YOU - TONIGHT -
RUTH,
BE - GOOD
```

Normalized: **I shall be thinking of you tonight, Ruth. Be good.**

Slovak: **Dnes večer budem na teba myslieť, Ruth. Buď dobrá.**

This covers all 38 encrypted letters on the address side. The separate
unencrypted initials appear to be W.D.M.; no name is inferred from them.
The picture side contains no observed cipher text.

## Reproduction

From repository root:

```sh
python3 ciphers/hcp-1190/work/decode.py
```

The script verifies hashes of the preserved sources, decodes the manual
outline/dot transcription in work/transcription.txt and checks an exact
symbol roundtrip. It does not perform OCR. A source image alone plus this
key still requires the disclosed manual transcription step; a successful
run does not independently validate the glyph readings.

## Evidence and uncertainties

The same alphabet accounts for the entire message, repeated glyphs retain
their values, and the decoded addressee RUTH agrees with the visible address.
No missing cipher letters were filled with guessed words. A few dot counts
and the last L outline in SHALL are weak and need independent visual
collation. The surname, full sender name and year from the postmark are
not established by this decipherment. The date 1907-09-14 is catalogue
metadata, not an independently verified year reading.

No published plaintext was used. The cited collection article was checked
after obtaining the reading; no matching target plaintext was found there.
This does not establish historical priority. Independent review is pending;
no accepted-solution register entry or FINAL marker is warranted yet.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-26). The reviewer read all 38 signs from source/address-large.jpg independently, in its own notation, and decoded them with its own script; the reading agrees with work/transcription.txt sign for sign and dot count for dot count. The plaintext is unchanged.

1. Reproduction decodes a manual transcription (minor). Accepted. The command still maps the manual outline/dot transcription and does not read the image. The earlier statement that weak signs "need independent visual collation" is superseded: review 1 collated all 38 signs, including the flagged ones (both L's of SHALL with two dots and no top stroke; the final T of TONIGHT with three dots; R, U, T, H of RUTH; Y of YOU with its dots to the left of the outline; G of THINKING with one dot). The report says the transcription was checked sign by sign in review.
2. Key transferred, not derived (minor). Accepted. The report names the system a dotted three-block Pigpen variant: the nine cells of a plain 3×3 grid (no X-grid) are read in the order A–I, and one, two or three dots select the blocks A–I, J–R and S–Z; J is not omitted and the ninth three-dot cell is unused. It states that the alphabet was carried over from the solver's HCP 1193 work as a hypothesis and confirmed here by the decoded text, not derived from this card alone.
3. Editorial punctuation (minor). Accepted. On the card the words are separated by hyphens and there is one comma after RUTH. The capital letters and full stops of the normalized reading "I shall be thinking of you tonight, Ruth. Be good." are editorial.

Remaining uncertainties carried into the report: the year 1907 rests on the catalogue (the Carthage cancel shows SEP 14 4.30 PM without a legible year, the Denmark backstamp is faint); the recipient's surname and the identity behind the plain initials W.D.M. are not established; faint pencil marks under OF are illegible and not part of the cipher; the bounded check against Schrödel (2021) found no prior publication of the plaintext, which does not prove that none exists.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
