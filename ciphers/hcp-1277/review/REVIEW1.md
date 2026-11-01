REVISE

# Review 1 of HCP1277 (reviewer: Claude Opus 5.5, 2026-11-01)

The decipherment stands: it is Hungarian, the key is right, and the sense of the card is as claimed. Concrete fixes are needed. There are three ledger errors, and the word division around both "not understood" words is wrong. Those two words can very probably be read without changing a single letter (finding 1), so the card may turn out to have no opaque word at all. This was the first review, and the solver made every call below without having seen it.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1277/work/decode_opus.py` ran; all four SHA-256 checks print OK. Its literal rows and normalized text are identical to the `SOLUTION.md` listing.
- **The command proves little by itself.** The ledger tokens are essentially the plaintext letters, so the real test is ledger against pixels.
- **Independent decode.** `review/work/check.py` uses my own token table and reproduces all 36 literal rows. With my three corrections applied, the changes are limited to rows 10, 24 and 25. The main text has 654 tokens, and every token maps.
- **Scan check.** I read all 29 rows and the 7 stamp rows sign by sign from my own 2x contrast crops of `work/hires/*_adr.jpg` (`review/work/g00`…`g61.png`). Doubtful spots were cropped at 3–8x (`z10, z12, z24, z25, z25b, z28, r2a`) and the stamp also in the blue channel (`stampb.png`). No crops from `work/crops/` were reused. Apart from the findings below, the ledger agrees with the card.
- **Key.** The HCP1216 table covers the whole text, and I found no extra sign class. The `a` and `e` calls (2 versus 3 bars) are clean at 3–8x, including both `a` in row 12.
- **Language and context.** The text is natural early-20th-century Hungarian in the family's register (formal address, letter formulas, the writer's habit of dropping doubled consonants). The addressee and signature fit. The picture side has only the printed caption and verse, no cipher.
- **Sources.** The solver's statement that the portal has no attached solution is consistent with `source/metadata.md`. I found no sign of an outside plaintext.

## Findings

1. **major — The two "not understood" words are a word-division error; `{esara}` and `{esebvel}` very probably contain the word *és*.**
   - **Row 12:** the literal `…estemviszaesara` divides as *estem visza | és | ara* = **estem vissza, és arra** ("I have fallen back, and for that I must wait…"). The e of `es` carries an acute stroke above it (`z12.png`, `g21.png`). *ara* = *arra* is exactly this writer's habit of single consonants (*kel, visza, hoszu, miat, legjob*). *Arra kell várnom, míg a forgalom … nem lesznek* is sound Hungarian, and *arra* is the antecedent of the *míg* clause. This also dissolves the solver's problem of finding a noun in -ra. The signs are the ones the solver read; only the division changes.
   - **Row 25:** `kuldtekesebvelkeresztül` divides as *küldtek | és | eb?el* = **és evvel/ebbel keresztülhúztak** ("and with that they crossed out…"). The blotted sign (`z25b.png`) is visibly two strokes on top of each other: a heavy chevron with the small closed bowl of a b inside it. So it is a b/v overwrite, and the writer changed his mind between spellings of *evvel* (= *ezzel*). `SOLUTION.md` says the natural sense is *evvel* "but the signs do not spell that". A b/v overwrite explains why, and the sense it reaches for is confirmed by *és* before it.
   - **Fix:** re-judge both on the pixels. If accepted, rewrite the normalized text, all three translations and uncertainties 1–2. The sentence break "mederbe estem. Vissza {esara}" must go, because *vissza* belongs to *estem*. Say in the text that *ara* → *arra* and *eb?el* → *evvel* are normalizations, and that the blot call rests on word sense.

2. **major — Row 10 is mis-transcribed: the card has *már*, not *mer*.** The sign has two bars plus a clear acute stroke above (`z10.png`), i.e. á. It is the same two-bar width as the a's beside it. The ledger's `M E F` should be `M A F`. Uncertainty 6's "writer's spelling *mer* → már" is therefore a false claim about the writer. The normalized word was right by luck of sense, while the literal row and the disclosure are wrong.

3. **major — Rows 24–25: the "blotted sign with dots beneath" is misdescribed, and the ü of *küldtek* is missing.** The two dots belong to the X of row 25 directly below them (`z24.png`). It is the normal ü of *küldtek*, so the ledger's `K X L` should be `K X:d L`, and the literal `kuldtek` is wrong. The row 24 sign is a dark but plain cross, read as u, so `T # T A M` should be `T X T A M`. The row reads `tutam`: a dittography at the row break, *megtud|tutam*, which is how the solver already normalizes it. Uncertainty 5 needs rewriting; the sign is not unreadable.

4. **minor — "One token = one written sign" is false for GY.** In all the instances I inspected, g and y are two separate signs, the 5-hook then the y-shaped sign, with a visible gap (`r2a.png`). No instance I saw was a joined sign. All 14 `GY` tokens need checking and should be split or re-described, and the "joined loop + descender = gy" key row reconsidered. The ledger has 14 `GY` against 1 `Y`, which is the same y-shaped sign. The plaintext is unaffected; the key table and token count are.

5. **minor — A count in "Why it is correct" is wrong.** *hogy* occurs 6 times (rows 2, 3, 8, 20, 21, 24), not ×7. *édesem* ×5 is right only with the one under the stamp, and *viszontlát-* ×3 is right.

6. **minor — The normalized text misuses editorial brackets and drops letters.**
   - *enyhébb nem lesz[nek]* puts brackets around letters that are written and clearly visible, and silently drops the written *-ek* of `enyhebbek`. Everywhere else `[...]` means lost text. Print *enyhébbek nem lesznek* and note the writer's plural.
   - *szabad[nap]om* inserts letters that are not on the card; the gloss in uncertainty 6 is adequate, but the text should keep *szabadom*.
   - The line *…most már visszakerültem, a régi…* has a comma between verb and complement: *visszakerültem a régi utazási mederbe* is one clause.

7. **minor — Word-sense calls not listed.** Under the stamp, the k of *csókolo* is the g-like hook. In S7, the last faint orange sign looks more like a right hook than a dotted i, so I cannot confirm the literal `eri` as a clean read (`stamp.png`, `stampb.png`). Add both to uncertainty 3 or 4 and consider `{?}` for the last sign of S7. The disclosure that *szerető kedvese Feri* is not read from the pixels is correct; I agree it should stay out of the plaintext.

8. **minor — Date and address side are underused.**
   - The year on the round postmark does read `916`, against the portal file name 1914-03-01. That belongs as a stated conflict, supported by the stamp (not "not read closely"). The boxed mark reads ÚJPEST.
   - The handwritten word over the postmark is not stray. It is the first line of the address and looks like **Szépreményű** (tentative), the courtesy epithet for *Tóth Jolánka úrleánynak*. It is plain writing, not cipher, and should be recorded as such.

## Could not verify

- That no published solution exists elsewhere; I did not repeat the web search.
- Identity of this Feri with the HCP1216 sender, which the solver also leaves unproven.
- The exact day and month of the postmark, and what the sender's job or the "long journey" was.
- The closing in S6–S7 between the blot and the tear; the signs there are not recoverable.
- Whether *ebbel* is a real period spelling. *evvel* is well attested, but I do not claim which of the two the writer settled on.

## For the solver

The verdict is REVISE, not REJECT, because the key and the reading stand. Findings 1–3 change the ledger, the literal rows and the normalized text, so regenerate them with the decoder and update the listing. Finding 1 is my proposal from the pixels and word sense, so test it rather than adopting it blind.
