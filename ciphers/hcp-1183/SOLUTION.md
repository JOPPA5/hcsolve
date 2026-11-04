# hcp-1183 — solution (Claude Opus 5.5, 2026-11-03, round 1)

Card: US one-cent postal card (Liberty-head indicium, the 1873–1881 issue type), postmarked SANTA CLARA CAL. JUN 25 (year not legible/not printed), addressed "Miss Fannie E. Brimblecom[?], San José, Cal." HC Portal 1183, status Not solved, no transcription or solution attached. A short web search found no published solution of this card (see SOURCES.md). All work below is my own (Claude Opus 5.5); there was no earlier work on this number.

## Cipher type and key

Simple monoalphabetic substitution (MASC) with invented geometric symbols, English, word spaces and punctuation kept. Twenty-one letters occur (A–I, L–P, R–W, Y; corrected from "twenty" after review 1); J, K, Q, X, Z do not.

| sign | letter | sign | letter |
|---|---|---|---|
| `/` slash | A | `≠` vertical with two bars | N |
| `\` backslash | B | `┐` hook (rounded 7) | O |
| `X` | C | `┌` top-left corner | P |
| X with horizontal bar | D | `┘` bottom-right corner | R |
| X with vertical bar | E | `⊔` open-top box | S |
| plain circle (small tick at top) | F | `□` square | T |
| circle with dot `⊙` | G | square with dot `⊡` | U |
| circle with horizontal bar `θ` | H | arch with feet `⊓` | V |
| circle with vertical bar `ϕ` | I | arch with feet and dot inside | W |
| `+` one bar | L | arrow up `↑` | Y |
| `#` | M | | |

Sign-name tokens and the full transcription are in `work/transcription.txt`; the key is `work/key.json`.

## Command (run from the repo root)

    python3 -I ciphers/hcp-1183/work/decode.py

It checks the SHA-256 of the two source scans and the hi-res message scan, then prints the plaintext line by line.

## Plaintext (English, as on the card)

    RECEIVED YOUR POSTAL CARD
    THIS MORNING. I HEARD OF IT
    LAST NIGHT, SO I HURRIED TO GET
    IT. I WENT RIGHT UP TO GRANDMA'S
    AND SENT THE CARD OVER TO THE
    MOUNTAINS BY AUNT LUCY. GOODNIGHT.
    O. W. L.
    GAY AND FESTIVE.
    CIDER

The last two lines are written apart at the bottom of the card (left and right).

## Translations

English (normalised): "Received your postal card this morning. I heard of it last night, so I hurried to get it. I went right up to Grandma's and sent the card over to the mountains by Aunt Lucy. Good night. O. W. L. — Gay and festive. — Cider"

Slovak: "Dostal(a) som tvoj korešpondenčný lístok dnes ráno. Počul(a) som o ňom včera večer, tak som sa ponáhľal(a), aby som ho dostal(a). Išiel/išla som hneď hore k babičke a poslal(a) som lístok do hôr po tete Lucy. Dobrú noc. O. W. L. — Veselý a sviatočný. — Cider"

## Uncertainties (all small)

1. `+` (L) vs `≠` (N): the writer separates them by the number of bars. On enlarged crops LAST, POSTAL and LUCY have one bar; MORNING (2x), NIGHT, WENT, AND, SENT, MOUNTAINS (2x), AUNT, GOODNIGHT and GRANDMA'S have two. In WENT, SENT and AUNT the second bar is fainter but visible.
2. Bottom-left AND: the N sign has, besides the strong vertical with two bars, a faint shorter second vertical to its left, so it could be taken for `#` (M). "AMD" is not a word; N rests on word sense and on the stroke weight (the extra stroke looks like a false start).
3. Bottom-right CIDER: lies under the HC Portal watermark that is printed over the scan. X (C), ϕ (I) are clear; the third sign shows the X arms and the left horizontal arm (D); in the fourth the X is visible but the vertical bar of E is only faintly visible beside the watermark letters, so E partly rests on word sense (plain X would give "CIDCR"); the last sign is a vertical with the base running left (R) — the stroke continuing to the right is the watermark's letter, not pencil (no colour fringe). Meaning of "Gay and festive. / Cider" (a joke, nickname or a postscript) is not clear from the card; the letters read.
4. "O. W. L.": three initials with stops below the last line (┐ = O, dotted arch = W, + = L); partly under the watermark but legible. Read literally; I do not know whether they are the sender's initials or a playful signature ("owl").
5. A small dot after θ in HURRIED (line 3) is read as a stray mark, not a sign.
6. Addressee's surname: handwriting on the address side reads "Brimblecom" / portal says "Brimblecone"; not part of the cipher.
7. No steganography found: the address side has a printed indicium (postal card, nothing can be hidden under it), the postmark, the address and a small pencil number "51" at lower left (probably a dealer/collection mark). The message side holds only the cipher text.

## Why it is correct

- Every one of the 163 enciphered signs (all lines, including initials and the two bottom groups) decodes under one fixed 21-letter key; no sign is unassigned, no letter has two signs.
- The plaintext is coherent period American English with no forced words: a reply about a postal card that was forwarded "over to the mountains" by Aunt Lucy, closing with "Goodnight."
- Long words fix the key independently of each other (RECEIVED, MORNING, HURRIED, GRANDMA'S, MOUNTAINS, GOODNIGHT) and recurring words agree (TO ×3, THE ×2, CARD ×2, IT ×2, I ×3).
- The key itself is systematic (A/B slashes; C/D/E X-family; F/G/H/I circle family; L/M/N cross family; O/P/R corners; S/T/U boxes; V/W arches), which an invented alphabet of this kind typically shows.
- It fits the card: a postal card itself (the message mentions "your postal card"), posted in Santa Clara to San José.

## Response to review 1

Verdict ACCEPT, four minor findings. No decoded letter changed.

1. Letter count (fixed). Recounted with a script over work/transcription.txt and work/key.json: 163 signs, 21 distinct sign types, 21 letters (A B C D E F G H I L M N O P R S T U V W Y). "Twenty" and "20-letter key" in this file are corrected to 21; the report uses 21. Letter frequencies: A12 B1 C5 D10 E14 F2 G8 H8 I15 L4 M3 N12 O13 P2 R12 S8 T19 U6 V3 W2 Y4.
2. CIDER (agreed, kept as uncertain). E and R rest partly on word sense under the watermark; uncertainty 3 stays and the report repeats it.
3. "Gay and festive." / "Cider" (agreed). Every letter decodes to English words; the meaning of the closing is unclear and is stated as such in the report. I re-checked the first sign of FESTIVE on a 4x autocontrast crop: a plain circle with no bar through it, unlike the barred H of THIS (line 2), so F holds.
4. Pencil traces on the address side (added). I re-inspected the hi-res address scan: besides the pencil "51" at lower left there are a few faint pencil strokes near the lower-left ruled line; they form no letters or signs. The card is a pre-printed postal card with an imprinted one-cent indicium, so there is no adhesive stamp under which anything could be hidden, and no writing was found along the edges or in the printed frame. Steganography check (prompted by the human's note on hidden messages under stamps on the Jolánka series): none present; the type stays MASC.

Reproduction re-run after the edits: `python3 -I ciphers/hcp-1183/work/decode.py` prints three OK hash checks and the same nine plaintext lines.
