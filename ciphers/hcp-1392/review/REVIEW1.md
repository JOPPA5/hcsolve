REVISE

# Review 1 — hcp-1392 (pc_hcp_73), Caesar −1 English postcard, 9 May 1907

Reviewer: Claude Opus 5.5, 2026-10-30. Round 1 (marker DONE1).

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1392/work/decode_full.py` runs: source
   hashes OK, 6 lines decoded, 61 letters, round trip asserts pass. Output matches the
   plaintext table in SOLUTION.md exactly.
2. **Independent decode.** `review/work/indep_decode.py` (own code, own transcription,
   shift sweep). With my transcription of the enciphered body
   (`Nz Pxo. Efbsftu / Tfoejoh. b. dbse / up. Z— jotufbe / pg. mfuufs. / Gspn. zpvs pxo / Hjsm`,
   57 letters) only shift −1 gives English: MY OWN DEAREST / SENDING A CARD / TO Y— INSTEAD /
   OF LETTER / FROM YOUR OWN / GIRL. Key = the Abbott-family key (hcp-1390, 1393, 1395,
   1397, 1407), confirmed.
3. **Transcription vs. scan.** Rotated `source/address.jpg` 90° CCW (`review/work/rot.png`)
   and checked every line in enlarged contrast crops (3–7x): `R2.png`, `R3.png`, `R4.png`,
   `R5.png`, `R6.png`, `L2start.png`, `L2end.png`, `L5start.png`, `K1b.png` (Efbsftu),
   `R4t.png` (line-4 tail), `R5t.png` (closing abbreviation), and a side-by-side
   `compare_N.png`.
   - Line 1 `Nz Pxo. Efbsftu`: N, z, P, x, o dark and clear; E (6-form with top loop), f,
     b clear; the final `ftu` is pale and crossed by the watermark ring but an f-stem with
     a cross stroke and a u-like trace are visible. Reading acceptable, uncertainty
     correctly disclosed.
   - Line 2 `Tfoejoh. b. dbse`: large T with top bar joined to the f descender, then o e j o h;
     `b` and `dbse` clear. Accepted.
   - Line 3 `up. Z— jotufbe`: clear; the long dash after Z is a real ink stroke.
   - Line 4 `pg. mfuufs.`: clear. **The tail is misread – see Finding 1.**
   - Line 5 `Gspn. zpvs pxo`: G has the writer's Y-like G form; s p n, z(2-like) p v s,
     p x o clear. Accepted.
   - Bottom `Hjsm`, written to the right of "May 9th 07", same "H/sm" form as on hcp-1407
     (`ciphers/hcp-1407/work/row4.png`). Accepted.
   - Plain fields (heading "G. H. Thursday.", "May 9th 07", address W. Abbott, Stokelake
     Farm, Chudleigh, Devon, postmark ...MBORNE 10 PM MY 9 07) agree with the scan.
4. **Sources/honesty.** Portal status "Not solved", no attached solution; no published
   solution is claimed; earlier GPT work is credited. Fine.

## Findings

### 1. (major) The line-4 tail "Ib-Ib!" = "Ha-Ha!" is a misreading; it is the family's "N & L" closing group

Evidence:
- In `review/work/compare_N.png` the first sign of the tail (top row) is put next to the
  capital N of the closing abbreviation (middle row) and the N of `Nz` (bottom row). All
  three have the same construction: a long rising lead-in stroke, a down-stroke, and an
  arched second hump. The tail's first group is this writer's capital **N**, not a
  copperplate "I" plus a joined "b"; there is no further letter between it and the short
  dash.
- The next signs are a small reversed "9"/c-like sign (the writer's ampersand) and a tall,
  pale single loop with a dark foot (capital **L**), then "!". 
- This is the same group, in the same slot (end of the message, just before
  "From your own"), as on the sister cards of the same writer: hcp-1393 line 4
  (`ciphers/hcp-1393/work/crops/l4c.png`: N/M, small ampersand, tall L – nearly identical
  pixels), hcp-1395 "M. & L. gspn", hcp-1407 "M. & L.' gspn", hcp-1403 "N. & L.".
- "Ib-Ib" requires two different shapes (a long stroke and a "9") both to be capital I,
  while the long-stroke form is used twice elsewhere on the same card as N.
Consequence: "Ha-Ha!" and the interpretation "teasing sense" must be withdrawn. The tail
should be transcribed literally as an initial group, e.g. `N & L!` (N/M not fully
excluded; under the shift it would give "M & K", but like the sisters it should be kept
literal and not expanded). The letter count drops from 61 to 57 enciphered body letters
plus literal groups; SOLUTION.md, transcript_full.json, the decoder's printed reading, the
English and Slovak translations, and Uncertainty 2 need updating.

### 2. (minor) Closing abbreviation before "Girl": add the "No." possibility and the sister parallels

The sign after the capital N (`R5t.png`) is a small raised letter with an ascender and a
doubled dot/dash beneath. Kept literal – correct. But the description should mention that
a raised letter with a mark under it is the usual way of writing a superscript
abbreviation such as "Nᵒ", and that hcp-1407 has "N.-1" ("No. 1"?) in exactly this slot
and hcp-1393 "Mᵘ.". None of this is proven; it should be listed as an alternative, not
expanded.

### 3. (minor) "Why it is correct" overstates

"Every word decodes with one fixed shift" includes the Ha-Ha group (Finding 1). After the
fix the statement should say that the enciphered body decodes completely and that two
initial groups (N & L; N + raised letter) are kept literal, as on the sister cards.

## What I could not verify

- The exact letters of the pale `ftu` in "Efbsftu" under the watermark ring; DEAREST is
  supported by the visible E f b s and the identical salutation on hcp-1390/1407.
- Whether the "N & L" and "N^x" groups are enciphered or plain initials, and their
  expansion.
- The identity of "G. H." and of "Y—"; the full postmark office name.
