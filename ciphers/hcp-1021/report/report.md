# HCP 1021 (cpc_1901-03-13_DE_Roggenburg_DE_Weyarn_): "Radfahren soll leben!" — a Pigpen line on a 1901 Bavarian postcard

Human solver: Tomáš Pavuk

**Status: deciphered (28 of 28 uncancelled signs; one sign struck out by the writer is not read); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1021 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1021), portal name cpc_1901-03-13_DE_Roggenburg_DE_Weyarn_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection and Pigpen, category Substitution / Monoalphabetic, date 1901-03-13, language **Unknown**, location Europe, sender Unknown, recipient Fräulein Schmid. No transcription or solution was attached; the only reference was Schrödel's overview paper *Cryptographic postcards* (HistoCrypt 2021), which does not give a reading of this card.

It is a "Gruss aus …" picture postcard (the picture shows a child bathing), sent from Roggenburg to Fräulein Schmid in Weyarn (Bavaria) and postmarked 13 March 1901. The cipher is a single line of 29 angular signs along the **top edge of the picture side**. The language of the plaintext is **German**.

![Picture side as scanned (source/picture.jpg)](../source/picture.jpg)

![Address side (source/address.jpg)](../source/address.jpg)

The margins of the picture side also carry ordinary cursive pencil writing (left, right and bottom). It is plain German handwriting, not cipher, and was not transcribed; the only part checked is a date "R. 11.III.01" in the right margin, which fits the postmark of 13 March 1901 and a sender in Roggenburg.

## Method

**Earlier work.** An earlier solver (OpenAI GPT, GPT-6 Astra / GPT-6.1 Sol) downloaded the scans and metadata, recorded the 29 sign positions with their bounding boxes (`work/transcript.json`), and tried the standard Pigpen key with all 24 orders of its four letter groups and a dictionary-constrained arbitrary monoalphabetic search. It reached no reading. The main obstacle was two signs (positions 11 and 24) that look like a "T" lying on its side, a shape that does not exist in the Pigpen alphabet.

**The decisive observation** (Claude Opus 5.5, 2026-10-29/30). On enlarged crops it is clear that the line was **written with the card turned upside down**: the signs stand on the printed frame line, and the five comma-like word dividers hang *below* that line, as commas do. Turned 180°, the line reads left to right as six groups of signs:

![The cipher line turned 180° (2x, autocontrast; work/report-line-rotated.png)](../work/report-line-rotated.png)

Read this way, with the **textbook Pigpen key** and no change at all, every uncancelled sign gives a letter and the groups give German words. The only free choice was the orientation, and the scan in its stored orientation gives no words with the same key. The two sideways-T signs then fall at places where only A gives words (ALL, FAREN); they are a ⌟ (A) drawn with the horizontal stroke meeting the vertical a little above its foot.

The transcription is **manual** (no OCR), made sign by sign from 4–14x enlargements. The reviewer made its own crops, transcribed all 29 positions independently from wall sets and dot/no-dot decisions, decoded them with its own script, and got the same text.

## Key

Standard Pigpen (Freemason) cipher: letters A–I in a plain tic-tac-toe grid, J–R in the same grid with a dot, S–V in a plain X, W–Z in a dotted X. A letter is written as the shape of its cell.

```
 A | B | C        J.| K.| L.        \ S /         \ W. /
---+---+---      ---+---+---      T  X  U      X.  X  Y.
 D | E | F        M.| N.| O.        / V \         / Z. \
---+---+---      ---+---+---
 G | H | I        P.| Q.| R.
```

Signs that occur on this card (described with the card turned 180°): A ⌟, B ⊔, D ⊐, E □, F ⊏, G ⌝, H ⊓, I ⌜, L ⌞ with dot, N □ with dot, O ⊏ with dot, R ⌜ with dot, S V, U <.

Repeated signs are consistent throughout: ⌞· = L six times, □ = E four times, ⌜· = R three times, □· = N twice, V = S twice, ⌟ = A three times (once plain, twice T-like).

## Plaintext

Literal reading (card turned 180°, dividers as spaces; `[x]` = one sign struck through by the writer):

```text
RAD[x]FAREN SOLL LEBEN ALL HEIL GRUS
```

Sign by sign (portal position ids, which run right to left on the stored scan):

| Word | Signs (id → letter) |
|---|---|
| RAD[x]FAREN | 29 R, 28 A, 27 D, 26 cancelled, 25 F, 24 A, 23 R, 22 E, 21 N |
| SOLL | 20 S, 19 O, 18 L, 17 L |
| LEBEN | 16 L, 15 E, 14 B, 13 E, 12 N |
| ALL | 11 A, 10 L, 9 L |
| HEIL | 8 H, 7 E, 6 I, 5 L |
| GRUS | 4 G, 3 R, 2 U, 1 S (then a long vertical end stroke) |

German, normalised: **Radfahren soll leben! All Heil! Gruß**

English: **Long live cycling! "All Heil!" Greetings.**

Slovak: **Nech žije cyklistika! „All Heil!" Pozdrav.**

*All Heil!* was the customary greeting of German cyclists' clubs around 1900 (general historical knowledge, not taken from a cited source), which fits "Radfahren soll leben". The spellings *Radfaren* (unless the missing h is under the cancelled sign) and *Grus* for *Gruß* are ordinary informal spellings.

## Uncertainties

![Enlarged signs, card turned 180° (6x; work/report-glyphs.png): glyph 28 is a plain ⌟ = A; glyphs 24 and 11 are the T-like A; glyph 27 (D) with a dot outside its open side; glyph 4 (G) with an ink blot above the top bar; glyph 26 struck through](../work/report-glyphs.png)

- **Cancelled sign 26.** The writer crossed it out with a heavy X; neither solver nor reviewer could identify the sign underneath, even at 10x. It is omitted. It may have been a mis-written letter (perhaps the h of *Radfahren*), but that is only a guess.
- **The T-like A (signs 11 and 24).** Their shape alone is not a clean ⌟; the reading A rests on the words ALL and FAREN and on the plain ⌟ = A at sign 28 in the same first word. No other letter gives words in either place.
- **Stray marks.** A dot just outside the open side of sign 27 (D) and an ink blot above the top bar of sign 4 (G) lie outside the cells. They are not read as cell dots (which would give M and P and no words). Solver and reviewer agree on this.
- **GRUS.** Read literally with four signs; no second S is restored.
- **Margins.** The cursive pencil text in the margins is not cipher and was not transcribed; it may contain a personal message, but it is outside this solution.
- **Image quality.** Only the portal scan (1024×678) was available; the original card could not be examined.
- **Prior publication.** No reading of this card was found in Schrödel's 2021 paper, on the portal (no attached solution) or in the AI Decipherment Register (checked 2026-10-29). The reading is our own.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1021/work/solve_1021.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of `source/picture.jpg`, `source/address.jpg` and `source/metadata.md`, holds the full sign-by-sign transcription (29 positions, shapes described with the card turned 180°) and the standard Pigpen key, and prints the decoded line, asserting that it equals `RAD[x]FAREN SOLL LEBEN ALL HEIL GRUS`. It does not read the image; the transcription step is manual and was confirmed independently in review. The figures in this report are made by `work/report_figs.py` (needs PIL).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claim), checked the key against the standard Pigpen layout, made its own rotated crops and per-sign 6x tiles, transcribed all 29 positions itself and decoded them with its own script: the result was identical. It confirmed the 180° orientation (signs on the frame line, dividers hanging below), every dot/no-dot decision, the coverage of all 28 uncancelled signs by one key, the plausibility of the German, the margin date, and that no published solution had been used. Its six findings were minor:

- **T-like A** — the report now shows signs 28, 24 and 11 side by side (figure above); reading unchanged.
- **Cancelled sign 26** — wording kept: not read, any letter is a guess.
- **Stray marks at 27 and 4** — kept as a disclosed reading choice, shown in the figure.
- **Count of L** — corrected from "five" to six occurrences in SOLUTION.md.
- **"All Heil" unsourced** — kept, labelled as general knowledge; the decipherment does not depend on it.
- **Language and type** — this report states German (the portal says Unknown); the register type is "Pigpen", as for the other standard-Pigpen cards in this repository.

No decoded letter changed as a result of the review.

## Credit

Scans, metadata, the 29-position geometry and the earlier unsuccessful key experiments: OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol). Orientation, identification of the T-like A, transcription check and decipherment, response to review and this report: Claude Opus 5.5 (Anthropic), 2026-10-29/30. Independent review: a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1021, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1021 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3123/conversions/cpc_1901-03-13_DE_Roggenburg_DE_Weyarn__pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/3124/conversions/cpc_1901-03-13_DE_Roggenburg_DE_Weyarn__adr-large.jpg (source/address.jpg).
- Tobias Schrödel, *Cryptographic postcards*, HistoCrypt 2021: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
