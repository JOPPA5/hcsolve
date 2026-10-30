ACCEPT

# Review 1 — HCP 1393 (pc_hcp_74), Caesar −1

Reviewer: Claude Opus 5.5, 2026-10-30. Round 1 (solver's DONE1: 2026-10-29T22:41Z, Claude Opus 5.5).

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1393/work/decode2.py` (repo root): "source hashes OK",
   seven lines, 73 enciphered letters. The output is identical to the plaintext table in SOLUTION.md.
2. **Independent decryption.** `review/work/indep.py` is my own Caesar −1 decoder, run on my own
   letter-only transcription. It gives MY OWN DEAREST I AM / GLAD THERE IS ONE / MORE LETTER FOR /
   ME THIS WEEK / FROM YOUR OWN / GIRL / HURRAH, with 73 letters. One shift covers every enciphered
   letter, and no group is left undecoded.
3. **Transcription against the scan.** I rotated `source/address.jpg` myself (`review/work/crops.py`) and
   made 3–6x autocontrast crops (`review/work/rows2.py`, `one.py` → `v_*.png`, `m_*.png`). Sign by sign:
   - Heading `G. H. Monday` (`m_h.png`): plain, correct.
   - L1 `Nz. Pxo. Efbsftu. J. bn` (`m_r1.png`, `m_r1b.png`): all clear. The b of Efbsftu is a filled loop.
   - L2 `hmbe. uifsf. jt. pof.` (`v_r2_*.png`, `m_r2mid.png`): hmbe, f-s-f, t and pof are clear. See
     findings 2 and 3 for the u-i of uifsf and the j of jt.
   - L3 `npsf. mfuufs. gps.` (`v_r3_*.png`, `m_r3mid.png`): I confirm `mfuufs` with no extra t. The
     solver's correction of the earlier `mfuufst` is right.
   - L4 `nf. uijt xffl!` (`m_r4.png`, `m_r4mid.png`, `m_r4r.png`): the t of uijt is a c-shaped stroke
     with a detached cross-bar. After "!." there is a cross below the line, then the shorthand group
     `M ? L` with an underlined raised mark.
   - L5 `gspn. zpvs. pxo.` (`m_r56.png`): the z is the "2"-shaped cursive z. Correct.
   - L6 `M + raised sign`, `"Hjsm` (`m_r6b.png`): Hjsm is clear (H drawn like an A with a cross-bar,
     j with a long descender). See finding 1 for the raised sign.
   - L7, in the cloud, `"Ivssbi` (`m_oval.png`): I, v, s, s and b are clear. The last stroke is an undotted
     i (single hump). HURRAH.
4. **Context.** The postmark reads WIMBORNE 10 PM AP 29 07. 1907-04-29 was a Monday (checked with
   Python), which agrees with the heading "Monday" and the portal date. The address is Mr W. Abbott,
   Chudleigh, which agrees with the sister cards hcp-1386…1407 in the same shift. The phrasing ("My own
   dearest", "from your own … Girl") is natural Edwardian English and matches hcp-1390.
5. **Honesty about sources.** The portal shows Not solved, with no attached solution (source/metadata.md).
   The earlier GPT work is credited. There is no register-exclusions entry for 1393, and 1393 is not in
   skip.txt.

## Findings

1. **minor — The signature abbreviation `Mᵘ` is not supported as a "u", and the sister citation is
   stale.** On `review/work/m_r6b.png`, the raised sign after the M has a tall ascender. It looks like an
   h or b, not a u, and has dots/dash below it. SOLUTION.md says it "matches the 'Mu. Hjsm' closing of
   sister hcp-1390". However, hcp-1390's own Response to review 1 (item 2) withdrew "Mu." for exactly
   this reason; it now reads "M + raised h/k/b-like letter, unread". Fix: describe the field as
   "M + raised h-like letter (unread)" in SOLUTION.md, transcription2.json and the report. Drop or
   correct the hcp-1390 cross-reference and the "Lᵗ (little)" aside. The plaintext body does not change.
2. **minor — The first letter of `jt` looks more like g than j.** On `m_r2mid.png` it has a closed upper
   loop and a descender, i.e. a "9"/g shape, and no dot. The reading IS comes from the context
   ("glad there is one more letter"), since `gt` gives FS. The solver discloses this (uncertainty 4). It is
   acceptable as a writer's j/g confusion, but the report should say plainly that this letter was chosen by
   context.
3. **minor — The u and i of `uifsf` are very faint.** On `m_r2mid.png` these two letters are a pale,
   partly overlaid scribble; f-s-f is firm. THERE is the only sensible reading, and the length fits.
   Uncertainty 4 mentions only that `hmbe` is faint. Add `uifsf` (first two letters) to the list of letters
   read with effort.
4. **minor — The "&" in `M & L` is not a clear ampersand.** On `m_r4r.png` the middle sign looks like a
   small r or a +. The group is kept literal and the uncertainty is disclosed, so this is a wording point
   only: write "M ? L (middle sign &/r/+-like)" rather than asserting "&".

None of these changes the decipherment.

## What I could not verify

- The meaning of the two shorthand groups (`M ? L`, and M + raised letter) and the identity of the
  sender.
- The farm name in the address. It is outside the cipher.
- I did not re-open the portal page. I relied on source/metadata.md and SOURCES.md (status Not solved,
  no attached solution) and on the orchestrator's register check.
