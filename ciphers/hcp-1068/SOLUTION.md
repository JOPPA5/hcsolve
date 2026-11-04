# hcp-1068 – SOLUTION (PARTIAL)

Status: **partial**. The enciphered letter (9 lines plus the signature strip) is read in full. A separate, unenciphered note written upside down in the stamp box, partly under the 1965 slogan postmark and running up to the stamps, cannot be read in full, so the card as a whole is not complete. No DONE marker and no register entry.

Work by Claude Opus 5.5, 2026-11-03. There is no earlier work on this number, and no published solution was found.

## Card
Picture postcard of the Wittelsbacher Brunnen in München (Lengauer Nr. 687), postmarked München 6.4.65, with the IVA slogan postmark ("Erste Weltausstellung des Verkehrs 25. Juni – 3. Oktober 1965"). It is addressed to Frl. Bärbel Hoffmann, (28) Bremen, Elsasserstr. 97. The heading "München 6.4.65 / Liebe Bärbel!" is plain writing. The picture side has no writing.

## Cipher type
Simple monoalphabetic substitution with invented signs (MASC), with a few variant signs for s, a, e and h. Word spaces and punctuation are kept, including parentheses, "?" and a line-end hyphen. The signature "Eva" is plain.

Key (cipher sign → plaintext). The codes are those used in work/transcription.txt:
- a: v with a dot above (W); v with a grave stroke above (Y, once); the two-stroke v "(/" (q, once)
- b: lying eight ∞
- c: brace }
- d: a cluster of four short ticks
- e: x (X); k-like sign (K, three times)
- f: slash with a tick "/'"
- g: double dash "--"
- h: v with a heavy blob at the point (V); wide U with a blob (U, once)
- i: vertical stroke
- j: j
- k: "||"
- l: 2-shape
- m: two-hump m
- n: low tick pair followed by a high tick pair („ ")
- o: o
- ö: o with a mark above
- p: B
- r: 6-shape
- s: $-like sign; variants: a hooked stroke (once), a reversed-L hook (once), S (once)
- t: F-like sign
- u: one-hump u
- ü: u with a mark above
- v: plain light v with no blob
- w: double tilde ≈
- z: long-tailed brace (yogh-like)

Not attested: q, x, y, ä, ß.

## Command
From the repo root:

    python3 -I ciphers/hcp-1068/work/decode.py

It checks the SHA-256 of both source scans and the hi-res address scan, then decodes work/transcription.txt with work/key.json.

## Plaintext (German, normalised)
München 6.4.65 / Liebe Bärbel! [plain]
Ich bin gut in München angekommen. Die Fahrt war ganz prima. Ich bin von Frau Hölzer richtig verwöhnt worden (jedenfalls was das Essen betrifft). Ist Stefan schon bei euch? Wir haben [h]ier bannig gutes Wetter. Ich hoffe, ihr auch. Herzlichst Deine Eva.

English: Munich 6.4.65 / Dear Bärbel! I arrived in Munich safely. The journey was really great. I have been properly spoiled by Mrs Hölzer (at least as far as the food is concerned). Is Stefan with you yet? We are having really good weather here. I hope you are too. Most cordially, your Eva.

Slovak: Mníchov 6.4.65 / Milá Bärbel! Do Mníchova som dorazila v poriadku. Cesta bola úplne skvelá. Pani Hölzerová ma poriadne rozmaznáva (aspoň čo sa jedla týka). Je už Stefan u vás? Máme tu veľmi pekné počasie. Dúfam, že vy tiež. Srdečne tvoja Eva.

("bannig" is northern/Low German for "very", which fits a writer from Bremen.)

## Uncertainties
1. "[h]ier": the cipher has i-e-r (line 8, read clearly at 2x). The h is missing, and "hier" is restored from word sense as the writer's slip.
2. "von" (line 3): the main line has a plain v. Above it, with a caret, the writer inserted v, o (with a small mark above it) and the n sign. The reading "von" rests on word sense.
3. Variant signs read from word sense, each attested only once or a few times:
   - three forms of s (in schon, das, gutes)
   - three forms of a (in haben, das)
   - U for h (in haben)
   - K for e (in betrifft, verwöhnt, herzlichst)
4. "jeden falls" and "Ste fan" are written with a gap inside the word, which may be the writer's own spacing.
5. Small marks next to the start of the signature strip (a dot, a crossed stroke, and a column like "h / i / crossed stroke" at the divider line) are not read. They may belong to the upside-down note.
6. **Upside-down plain note in the stamp box (steganographic placement), not fully read.** It is written in Latin cursive upside down relative to the address, across and partly under the black slogan postmark, up to the stamps. What is visible, line by line:
   - "Hen?el(l)" (perhaps the brand Henkell)
   - an illegible word ending "…eul9"
   - "…ebrau(i)ch!"
   - "bei Wein"
   - possibly "hic" in the side column

   The overprinted letters cannot be separated from the postmark by colour, and part of the note may run under the stamps. This unread clause is why the card is partial.

## Why the main reading is believed correct
Every sign of the 9 lines and the signature strip decodes under one consistent key into fluent 1965 German. The reading fits the card itself: it was posted in München, the slogan postmark is from 1965, and the recipient lives in Bremen, which fits the Low German "bannig". Repeated words decode the same way every time: ich ×3, bin ×2, ihr/hier, auch/euch, essen/was/ist. Doubled letters fall where German has them: gekommen (mm), betrifft (ff), Wetter (tt), hoffe (ff), falls (ll), bannig (nn), Essen (ss).

How the key was found: a quadgram hill-climb gave the crib "ich bin" for the thrice-repeated "I}V ∞I„"". The rest was extended by hand: auch, München, gekommen, Fahrt, ganz prima.
