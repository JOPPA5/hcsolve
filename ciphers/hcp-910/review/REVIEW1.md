ACCEPT

# Review 1 - hcp-910 (M. Zwick to his parents, Ulm, 2 Aug 1917)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. Reviewed solver work by Claude Opus 5.5 (same date).

## What I verified and how

1. Ran the command from SOLUTION.md: `python3 -I ciphers/hcp-910/work/decode.py`. All four source hashes OK; the output
   matches the claimed text line by line ("eine klaine bitte hätte ich noch ann euch nemlich es würde mich ser freuen
   wann Jer mier ein Paket Zucker schicken könt, denn ich weis nicht wann ich in urlaub komme").
2. Independent decode: review/work/my_decode.py holds my own transcription of the ten enciphered lines, read from the
   hires scan, and my own key table (1-0 = a e i o u l n m r s). It gives the same plaintext. 92 digit signs in both
   transcriptions (0:3, 1:7, 2:22, 3:14, 4:3, 5:7, 6:4, 7:19, 8:6, 9:7); every one decodes into an ordinary German word,
   no residue. All ten digits are used and each is used consistently across many words (e.g. 7 = n in 74ch, 237, d277,
   73cht; 3 = i in 3ch x4, b3tt2, sch3ck27), so the key is forced by this card alone, not only borrowed from hcp-1057.
   The key also matches hcp-1057/SOLUTION.md (same writer).
3. Pixels: own crops in review/work/ made with review/work/crop.py (plain and blue-minus-red isolation):
   - r1.png (568 d27 / 2. / Liebe Eltern / 2372 k61372 b3tt2): clear.
   - l3b.png, ann.png, ann_c.png (h1"tt2 3ch 74ch 177 25ch, under the postmark): blue isolation shows the umlaut on
     the 1, then 1-7-7 as three separate strokes and 2-5-ch; reading confirmed.
   - r2b.png, wurde.png, freuen.png: 72863ch 20 w5?9d2 / 83ch 029 f92527. w, a 5-shaped bowl, 9, tall d loop and 2
     are visible; the umlaut on the 5 is not distinguishable from postmark noise (disclosed by the solver). f92527:
     f, 9, 2, 5, the oversized-loop 2, 7 - confirmed.
   - r3.png, r4.png (w177 J29 8329 / 237 P1k2t Z5ck29 / sch3ck27 k4"7t d277 / 3ch w230 73cht w177 3ch /
     37 59615b k4882.): all signs clear; the blot after 4" in k4"7t is as described.
   - r5.png: plain "Gruß Euer Sohn" and the flourished signature "Zwick".
   - vert_a.png, vert_b.png (vertical line along the divider, rotated): "Den Brief habe ich erhalten, besten Dank
     dafür." - confirmed, plain Kurrent.
   - sender.png: "Abs. M. Zwick [rank] [unit] 247 / Ulm a. Donau" - as transcribed, rank and unit unread.
4. Steganography check (stamp box, picture side): stampbox.png shows the printed stamp frame holding only the green
   "Z 4285" number and the ULM Nr. 1 postmark 3.8.17; no stamp was ever affixed (no glue residue or tear), so nothing
   can be hidden under one. The picture side (Ulm Münster, printed red caption) carries no handwriting. Register type
   MASC is therefore right; "MASC + Steganography" does not apply to this card.
5. Context: Ulm garrison 1917, request for sugar (rationed), leave uncertainty, recipient Georg Zwick at Erbenschwang
   (Post Ingenried, Schongau) - consistent with the address side and with sister cards hcp-1056/1057.
6. Prior publication: the solver disclosed the 2019 Schmeh-blog key and the Schrödel book citation. I fetched the
   portal's linked HistoCrypt article page (Schrödel, "Cryptographic postcards"); the abstract does not mention Zwick
   or this key. No plaintext of this card found.

## Findings

1. (minor) Sender block not fully read. "Abs. M. Zwick [rank] [unit] 247" - the rank word and unit abbreviation are
   left unread. This is disclosed (Uncertainty 7) and it is not part of the message, so it does not make the card
   partial; the report should show it as a bracketed gap, not as a reading.
2. (minor) Umlaut of w5"9d2 rests on word sense (würde vs wurde; the dots are not separable from the postmark under
   the stroke). Disclosed; the transcription file should mark it as inferred (e.g. a comment) rather than writing 5"
   as if seen.
3. (minor) NOTES.md calls hcp-1057 "FINAL path"; that directory currently has DONE1 + REVIEWED1 and no FINAL. Reword
   so the report does not cite it as finished.
4. (minor) The HistoCrypt article linked by the portal (and its PDF) was not checked by the solver; I only saw the
   abstract page. Mention it in SOURCES.md as consulted at abstract level.

## What I could not verify

- Whether Schrödel's book p. 233 or the HistoCrypt PDF reproduces this card with a decipherment (not viewable).
- The exact umlaut on "würde" and the rank/unit words in the sender line.
