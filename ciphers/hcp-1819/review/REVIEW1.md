ACCEPT

# Review 1 — HCP 1819 / pc_hcp_500 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment GO HOME ON SATURDAY is correct.** I read the 16 signs along the curved line myself, turning each one into its local writing orientation, and got the same tokens as `work/transcription.txt`. Two of the signs are only decidable once a local baseline is fixed (finding 2), but the solver has already disclosed that, and English settles both. All findings are minor.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1819/work/decode.py` reports matching hashes and prints `GO HOME ON SATURDAY`, 16 glyphs, 13 distinct. I also re-hashed both scans with `shasum -a 256`, and they match `work/source-sha256.json`.
2. **Independent reading of the scan.** I made crops of `source/address-large.jpg` in `review/work/`:
   - `feather.png` is an overview.
   - `col-rot8.png` is the vertical part, rotated 270°. It reads left to right: `GO · HOME · ON…`.
   - `arc-rot8.png` is the lower arc, rotated so the line is horizontal. In that view the arc text is upside down and runs right to left, consistent with the writing continuing round the curve.
   - `z-sat.png`, `z-satur.png`, `z-day.png` and `z-on.png` are unrotated 12–14× details.

   For every sign I took "up" to be the reader's left of the local writing direction. My reading, in my own notation (grid cell or wedge, `*` for dotted), is in `review/work/my-reading.txt`.
3. **Independent decoder.** `python3 -I ciphers/hcp-1819/review/work/review_decode.py ciphers/hcp-1819/review/work/my-reading.txt ciphers/hcp-1819/work/transcription.txt`. It builds the key from `ACEGIKMOQSUWY` (undotted) and `BDFHJLNPRTVXZ` (dotted):
   ```
   GO HOME ON SATURDAY
   16 signs; distinct 13
   letters written with >1 sign: none
   solver signs: 16      (no differences reported)
   ```
4. **Sign checks.**
   - GO: top+bottom+right, then top+left+right.
   - HOME: the dotted ⊐ has a clear centre dot. Then ⊓, ⅂ and L.
   - SATURDAY: S and T are the same downward wedge, T with a dot. U is a wedge whose point faces the local right. R is a dotted corner pointing diagonally to the local top-left (`z-satur.png`). D is a dotted ⊔ open towards the local top. Both A's are bottom+right corners. Y is a wedge pointing to the local top.

   The two A's and the three O's are drawn consistently. The dots between words are separators, and a final dot ends the line.
5. **Context.**
   - The address side is postmarked TAMWORTH, 7.45 PM, DE 22 (`review/work/z-postmark.png`). It is addressed to Miss K[ite/ile], Standon Green End, High Cross, near Ware, Hertfordshire (`z-addr.png`), and signed "Love from A.E.S." in plain writing.
   - The picture side is the Christmas greeting "A happy Christmas to you", with no cipher.
   - With the catalogue date 1904-12-22, a Thursday, the following Saturday is 24 December, Christmas Eve. "Go home on Saturday" fits a Christmas card written two days earlier.
6. **Prior solutions.** No solution was attached on the portal (`source/metadata.md`). The register snapshot cited in `SOURCES.md` lives in `ciphers/hcp-1825/work/`. I found no sign of an undisclosed published solution.

## Findings

1. **minor — the reproduction command maps a manual transcription.** The solver discloses this. The local rotations are the solver's judgement and are not computed. My independent reading now confirms all 16 tokens, and the report should say so.
2. **minor — two signs depend on the assumed local orientation.**
   - The N of ON (`z-on.png`) is a dotted corner. It sits where the line starts to bend, and its corner points almost straight along the writing direction. Without a fixed baseline it could be read as a dotted ">" wedge, which would give `OV`.
   - Likewise, the S of SATURDAY is a near-right-angled wedge. It could pass for a bottom+left outline if the baseline were taken more vertical.

   In both cases only the solver's reading gives English, and the same orientation rule reads every other sign without strain. The uncertainty is real but does not threaten the solution. The report should mention it as the residual risk rather than speak generally about "watermark and rotations".
3. **minor — protocol.** `source/` and `work/` both have a directory mtime of 00:22:40 local, about 100 s *after* `DONE1` (00:20:59). An entry was added to or removed from both directories after the marker. The files now present predate the marker, and the source hashes still match, so nothing substantive changed. Still, the README says nothing in the cipher directory is touched after a marker.
4. **minor — the key was transferred from earlier postcards, not rediscovered.** This is disclosed. The report should name the system as the alternating dotted/undotted Pigpen with an X-grid for S–Z. Here 16 signs and 13 distinct ones confirm it only because the result is fluent English.

## What I could not verify

- The year on the Tamworth cancel. It is partly hidden by the stamp, so 1904 rests on the catalogue.
- The surname of the recipient (Kite or Kile) and the identity of A.E.S.
- Whether this card has been deciphered elsewhere. I did not repeat a web search.
