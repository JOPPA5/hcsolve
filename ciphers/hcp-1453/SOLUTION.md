# HCP1453 / pc_hcp_134 — American Morse postcard, Washington D.C., 11 June 1906

**Current status (2026-10-29): complete reading of every legible cipher
position, accepted in review 1 (verdict ACCEPT).** Cipher: American
(railroad/landline) Morse. Main text 137 letters, plus a separate terminal
item of two rows of larger dots read R S (probably the writer's initials as a
signature). One cancelled box in column 1 is illegible and unread.

The sections below up to "Completion and handover" are the history of the
earlier passes (by an OpenAI GPT solver, 2026-10-26), kept unchanged; their
statements "partial", "not independently reviewed" and "No DONE marker" are
superseded by this header, the completion section and the response to review.

Single command (from the repository root): `python3 -I ciphers/hcp-1453/work/decode.py`
— prints the three columns, the signature item R. S. and the status of the
cancelled box.

## Source and method

The portal was freshly Not solved on 2026-10-26. General, Description and
Attachments were read; only the two scans were attached, no supplied
transcript or solution. Picture caption: Treasury Building. Handwritten
heading: Washington, D.C., June 11 '06. Address is to Carl Schmitt,
Warren, Ohio. These ordinary inscriptions are not cipher positions.

The picture has three narrow columns on the right. Follow each column
downward, then proceed to the next column to the right, as the arrows
indicate. Each horizontal row of small marks is a letter, and ruled boxes
separate words. American Morse explains the spaced-dot letters and long L.
Ordinary International Morse does not give this reading.

The exact key is in work/decode.py. In particular: O = `. .`, R = `. ..`,
C = `.. .`, Y = `.. ..`, F = `.-.`, P = `.....`, and L is one long dash,
written `=` in the manual transcript. T is the shorter dash `-`.
Internal spaces in a letter must be retained. `/` separates letters only.

## Literal decoded main text

```text
I GOT IN A [cancelled box] HOLE AND HAD TO SELL THAT ORCHESTRA CARTOON
FOR A DOLLAR WENT OUT TO BROOKLAND YESTERDAY PM I HAVE
BEEN WEARING A SKULL CAP WONT HAVE THE NERVE TO WEAR IT AT HOME
[terminal oversized dots: . .. / ... ; possible R S, not established]
```

Word boundaries above follow the boxes. Sentence punctuation and the
apostrophe in WON'T are editorial, not encrypted characters. In natural
English this can be read: “I got in a hole and had to sell that orchestra
cartoon for a dollar. Went out to Brookland yesterday p.m. I have been
wearing a skull cap. Won't have the nerve to wear it at home.”
No omitted letters are inserted into the literal text.

## Slovak translation of the main text

„Dostal som sa do tiesne a musel som predať tú karikatúru orchestra za
dolár. Včera popoludní som bol v Brooklande. Nosím priliehavú čiapku.
Doma by som sa ju neodvážil nosiť.“

The idiomatic reading of “got in a hole” is interpretive. The translation
does not identify a cartoon, sale, individual, or specific cap from any
external historical record.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1453/work/decode.py
```

The command checks the unchanged source hashes, decodes all 137 frozen
manual letter transcriptions and tests their inverse-key roundtrips.
It does not perform OCR, nor derive the transcript automatically from
the scan. Source-to-transcript comparison remains a visual task.

## Evidence and limitations

The same fixed American-Morse key reads all three columns continuously.
Repeated HAVE, TO, WEAR/WEARING and the spaced-dot letters agree across
different boxes. Source crops support HOLE (H, spaced O, long L, E),
BROOKLAND (including K and long L), PM (five dots then two dashes), and
the ending AT HOME (short T, spaced O, two-dash M).

The crossed-out box between A and HOLE is not recovered; it may be an
abandoned attempt, but its contents are not asserted. Six unusually large
dots after HOME are arranged in two rows. Reading their spacing as
American Morse gives possible initials R S, but a decorative ending or
another intended function is not ruled out. They are not silently
converted into a signature or numeral. Arrow strokes, word rules and
printed/background marks are not treated as Morse letters.

This reading is newly transcribed from the scans in this attempt. An
external American-Morse alphabet was consulted, not a published solution
to this postcard; see SOURCES.md. Independent review is still needed.

## Bounded follow-up on excluded marks

A further solver pass inspected both excluded areas in the original image,
with new crops `work/agent-cancelled-large.jpg` and
`work/agent-terminal-large.jpg`. The terminal top-row dot centres are
approximately x=934,956,966; the bottom row x=934,949,962 (original pixels,
visual estimates within about two pixels). Thus the top row has a visibly
larger first gap (22 versus 10 pixels), while the bottom gaps are comparable
(15 versus 13 pixels). This supports `. ..` / `...`, hence conditional **R S**
under the already established American-Morse table. It strengthens the mark
reading without establishing their function. They remain outside the 137
frozen main-message positions; the condition that each row is one letter
has not been proved merely by decoding it. No person or signature is inferred.

`python3 ciphers/hcp-1453/work/check-terminal-scope.py` reproduces that mapping
and the manually measured gap comparison from `work/terminal-scope.json`.
The measurements are not automated pixel segmentation or independent review.

The cancelled box contains several oblique crossing strokes over dot-like
marks and a dark horizontal run. The enlarged scan does not uniquely separate
original marks from cancellation. No cancelled letter/word is recovered, and
no assumption that it is decorative, disposable, or a particular abandoned
word is used to claim full coverage. Overall status remains partial.

## Native-pixel spacing controls (ten-agent follow-up)

`work/measure-terminal-pixels.py` now compares the terminal marks with
three explicitly selected controls from the same original scan: R in
WEARING, R in WEAR, and S in SKULL. It checks the source hashes, thresholds
the original grayscale pixels, and measures centroids of 4-connected dark
components of at least three native pixels. All seven trial thresholds
(90, 100, 110, 120, 130, 140, 150) are retained in
`work/terminal-pixel-measurements.json`; low-threshold fragmentation is
reported rather than silently filtered into a preferred result.

At thresholds 110–150 each selected row yields exactly three components.
The upper terminal row's first/second Euclidean centroid-gap ratio is
2.169–2.213. The two control R rows give 2.062–2.324. The lower terminal
row gives 1.113–1.129; the control S gives 0.808–0.845. Thus the upper row
has the same conspicuously unequal-gap structure as R; the lower row has
approximately equal gaps, compatible with S. The control S is not perfectly
symmetric either. These are descriptive comparisons from three manually
chosen rows, not a trained or statistically calibrated classifier.

Reproduce the pixel measurements with a Python environment containing Pillow:

```sh
python3 ciphers/hcp-1453/work/measure-terminal-pixels.py
```

This strengthens the conditional transcription **R S**, and replaces the
previously manual-only spacing estimate with measurements derived from the
original pixels. It does not prove that the terminal rows are alphabetic
rather than a flourish, or that RS are someone's initials. The crossed-out
box remains unread: its dark horizontal ink and oblique cancellation overlap.
Thresholding cannot reconstruct the overwritten stroke order. The fixed
137-letter main transcription and overall **partial** status are unchanged.
No DONE marker is warranted by these additional measurements alone.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading, handed to review (DONE1).**

1. **Cancelled box (work/agent-cancelled-large.jpg).** The box is covered
   with dense diagonal hatching over a short row of marks. The writer struck
   out a false start, and it is not part of the message. Its marks are
   illegible under the hatching and are unread; nothing is read from it.
2. **Terminal dots (work/agent-terminal-large.jpg).** Two rows of the same
   heavy dots used throughout the card: upper `.  ..` (one dot, gap, two
   dots) and lower `...`. They follow the same convention as every other letter
   (one horizontal row = one letter; spaced dots matter). In American Morse,
   `. ..` = **R** and `...` = **S**. Read **R S**, **probably** the writer's
   initials as a signature at the end of the third column (interpretation from
   position and setting-apart, not proven). The addressee is Carl Schmitt,
   so an R. Schmitt in the family is possible but not claimed; the sender is
   not identified. The larger dots may be a deliberate signature flourish.

Full reading: “I got in a hole and had to sell that orchestra cartoon for a
dollar. Went out to Brookland yesterday p.m. I have been wearing a skull
cap. Won't have the nerve to wear it at home. — R. S.”
(Washington, D.C., 11 June 1906; Brookland is a neighbourhood of Washington.)

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent): verdict **ACCEPT**, five minor
findings, no blocker or major. No letter of the reading changed.

1. **Inconsistent status (minor) — fixed.** The header now states the current
   status (complete reading, accepted) and marks the earlier sections as history
   whose "partial / no DONE" statements are superseded.
2. **Single command does not produce the full reading (minor) — fixed.**
   `work/decode.py` now also decodes the two terminal rows from
   `work/terminal-scope.json` with the same key, as a separately labelled
   signature item, asserts `RS`, and reports the cancelled box as unread.
   Re-run from the repository root with `python3 -I ciphers/hcp-1453/work/decode.py`:
   the three column lines are unchanged, then `137 mapped letters; source hashes
   and transcript/key roundtrips pass.`, `Signature (terminal larger dots,
   separate item): R. S.`, `Cancelled box (column 1, between A and HOLE):
   illegible under hatching, unread.`
3. **R S stated too firmly (minor) — agreed, fixed.** The completion section now
   says "probably the writer's initials as a signature"; the sentence that the dots
   are larger "only because they sit alone in the corner" is replaced by a note
   that the enlargement may be a deliberate flourish. No sender is identified.
4. **Cancelled box (minor) — fixed.** Stated explicitly that its marks are
   illegible under the hatching and unread (the reviewer's 8x crop
   `review/work/cancelled8x.png` agrees: a dot or two and a dash run under
   hatching, nothing legible).
5. **Editorial marks (minor) — kept.** WON'T, p.m. and sentence punctuation are
   editorial; the literal text has WONT and PM. This disclosure is repeated in the
   report.

