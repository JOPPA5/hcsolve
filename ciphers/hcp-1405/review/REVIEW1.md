ACCEPT

# Review 1 — hcp-1405 (pc_hcp_86), Caesar −1 English postcard to W. Abbott

Reviewer: Claude Opus 5.5, 2026-10-30. Note: the round-1 solver was also Claude Opus 5.5 (completing earlier GPT work), so this review is not cross-provider.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1405/work/v2/decode.py` from the repo root: source hashes OK, output
   `MY. OWN. [El] BOY. / I. HAVE. BEEN. / VERY. BUSY. / TO-DAY. / MY. [N. & L.] YOUR / OWN. [Mu] GIRL`,
   "43 enciphered letters decoded + 6 abbreviation letters kept literal". Matches the table in SOLUTION.md exactly.
2. **Independent decryption.** `review/work/mydecode.py` (own shift −1 implementation, typed from my own reading of the scan) gives the same six lines and the same count of 43 enciphered letters (8+9+8+5+6+7).
3. **Transcription vs scan.** I rotated `source/address.jpg` 90° (`review/work/rot.png`) and made my own 3–4x crops (`a.png`, `b.png`, `l2.png`, `l4.png`, `l5.png`, `l6.png`, `l6full.png`). Line by line:
   - L1 `Nz. Pxo. El Cpz.` — N with small z ("Nr"-like), P with x-like and o, a capital E followed by a single looped l (no dot between), C-p-small 1-like z with final dot. Consistent. The earlier GPT reading "Efbs" is correctly rejected: there are only two letters between `Pxo.` and `Cpz.`.
   - L2 `J. ibwf. Cffo.` — clear.
   - L3 `wfsz. cvtz.` — w, f with long descender, s, small 2-like z (partly under the grey watermark ring), dot; c, v, t with long crossbar, z. Visible.
   - L4 `up-Ebz` — faint but u-p, hyphen, E, 6-like b, z are visible.
   - L5 `Nz. N. & L. Zpvs` — clear: N z, N., ampersand, L., Zpvs.
   - L6 `Pxo. Mu Hjsm` — Pxo. with long P-flourish, then an M with a small following stroke, then H, a small sign, s, m, all crossed by the upside-down printed publisher line. The H-?-s-m shape fits Hjsm (GIRL) but the second letter (j) is not individually secure on the pixels; it is read as in the sister cards.
4. **Key coverage.** Every enciphered token decodes with the single shift; no token-specific substitutions; heading "G. H. Friday" is plain writing, as on the sister cards ("C. H. Friday" on hcp-1403, same date 1908-02-07).
5. **Context.** Postmark WIMBORNE FE 7 08 visible on my rotation; 7 Feb 1908 was a Friday, agreeing with the heading. Formulas ("My own E. L. boy", "My N. & L. … your own … girl", "Mu. girl") match hcp-1386, 1390, 1393, 1406. Plaintext is natural Edwardian English.
6. **Honesty.** No published solution exists or was claimed; earlier GPT work is credited and its errors listed; abbreviations kept literal and not expanded. Card is not in skip.txt or register-exclusions.json.

## Findings

1. **minor — `Hjsm` second letter not visible as a distinct j.** In the final word the letter between H and s is cramped under the printed line; GIRL is secure from shape and the series formula, but SOLUTION.md lists the uncertainty only for `Mu`. Add one line saying the j of Hjsm is read from context/shape.
2. **minor — `El` vs `E. L.`.** On this card the group is written `El` without an inner dot (verified), while sister cards write `E. L.`; the solution treats them as the same group, which is reasonable and disclosed. No change needed beyond what is stated.
3. **minor — same-provider review.** Solver round 1 and reviewer are both Claude Opus 5.5; the register `role` field should name the reviewer truthfully and not imply cross-provider review.
4. **minor — heading initial G/C.** Disclosed; sister cards read "C. H.". Not part of the cipher.

## What I could not verify

- The meaning of the abbreviations `El`, `N. & L.`, `Mu` (not claimed by the solver either).
- The exact identity of the small second sign in `Mu` (u or h) and of the j in `Hjsm`, beyond shape and series parallels.
