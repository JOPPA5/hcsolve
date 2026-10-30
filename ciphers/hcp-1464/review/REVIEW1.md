ACCEPT

# Review 1 — hcp-1464 (pc_hcp_145), reviewer Claude Opus 5.5, 2026-10-29

## What was verified and how

1. **Solver command.** `sips -f horizontal source/address-large.jpg --out review/work/flip.jpg`
   ran cleanly; `cmp review/work/flip.jpg work/decoded.jpg` reports the files
   are identical. The command is a pure pixel reflection and adds no text of its own.
2. **Independent decoding.** `review/work/verify.py` (PIL, `FLIP_LEFT_RIGHT`) reflects
   the scan independently and makes enlarged crops: `msg_flip_3x.png` (message, 3x),
   `edge_orig_5x.png` (edge word, 5x, original orientation) and `addr_orig_2x.png`
   (address). I read the reflected message letter by letter:
   `I hope you / will like thi[s] / from Joe. / Amen`. It matches the claim exactly.
   Each word reads clearly once reflected: the looped capital I, "hope", "you",
   "will", "like", "from", the capital J of "Joe" followed by a full stop, and "Amen".
3. **Edge restoration "this".** In the 5x crop of the original, the first stroke
   at the card's left edge is a heavy, blotted ink mass that runs into the
   card edge, directly after a clear "t-h-i" with the i-dot. The mass fills the
   position of a final letter, and the ink ends at the physical edge of the card,
   where white scan background begins. The *s* cannot be read as a letter form, but
   the end of a word is plainly there, and "will like thi-" admits essentially
   only "this". The solver discloses this as a restoration. Accepted.
4. **Coverage.** The whole message area is accounted for: four lines and nothing else.
   The dashes under "Amen" and under "York's" are decorative flourishes or
   underlining of the kind common on postcards, not an alphabet. The picture side
   (`source/picture-large.jpg`) has only the printed caption "FELISKIRK. NEAR
   THIRSK C.T." and no handwriting. The large lettered wheel and the padlock house
   drawn over both scans are the HCPortal watermark, not part of the card. The
   only "key" is the reflection, and it covers all of the hidden text.
5. **Language and context.** The text is natural Edwardian English, a short affectionate
   note, and mirror writing is a common postcard game of the period. The address
   reads Miss L. Wood, **Kepwick**, Northallerton, York's. Kepwick is a village
   a few miles north of Felixkirk/Thirsk, which fits the picture side. The postmark
   reads DE 12 05, and the portal date is 1905-12-12. Everything is consistent.
6. **Published solution.** The portal attaches no transcript or solution, and I
   found nothing to suggest one was used.

## Findings

1. **minor — address misread.** SOLUTION.md gives the second address line as
   "Hayrick(?)". In `review/work/addr_orig_2x.png` it is clearly **Kepwick**
   (capital K, e, p, w, i, c, k), a real village near Northallerton that fits the
   Feliskirk picture. The solver should correct it and may drop the "(?)".
2. **minor — postmark wording.** SOLUTION.md says the postmark reads "DE 12 05"
   "on the reflected image". It reads that way on the *original* scan; on the
   reflected image it is mirrored. The date itself is correct.
3. **minor — stale text.** The first section still says "No DONE1/FINAL or
   accepted review claimed" and calls the reading "not claimed fully observed",
   which the completion section now supersedes. The two Slovak renderings also
   differ slightly in punctuation. Tidy these for the report.
4. **minor — disclosure wording.** The completion section says the final hooked
   stroke is "the usual cursive terminal s". At 5x it is an ink blot at the edge
   rather than a recognisable *s*. The reading "this" stands, but the report should
   say that the last letter is restored from context and from an edge blot, not
   seen as a letter form.

No blocker or major findings.

## What I could not verify

- The physical card. Whether the last letter is lost to trimming or to blotting
  can only be judged from the 1024 px scan.
- The identities of "Joe" and Miss L. Wood. These are not needed for the reading.
