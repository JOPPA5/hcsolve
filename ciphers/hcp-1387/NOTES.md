# HCP 1387 working notes

2026-10-26, solver subagent, exactly this cipher.

- Read README in full. Root supplies fresh rendered three-tab observations and original downloads. User override means no watcher or reviewer is started.
- Personally inspected address.jpg and picture.jpg, then rotated the address 270 degrees in work/ and enlarged crops. Originals untouched.
- Tested Caesar −1 against actual ink rather than importing the adjacent-card text. Independently clear Nz Pxo / Cpz / wfsz / Nvdi gps / Gspn / Pxo give My Own / Boy / very / Much for / From / Own.
- Cursive capitals, compressed middle words and initial-like groups prevent a full transcript. Initial guesses such as a Mother/Never-like word were not retained: the first middle word may instead be Mfuufs (Letter), but the pixels do not yet justify freezing it. No corpus search or contextual fill was used to repair these spans.
- Frozen transcript contains 26 selected alphabetic positions, not a full-message count. Decoder checks source hashes and inverse Caesar mapping; it is not a pixel-to-text recognizer.
- Candidate remains partial. No marker, reviewer launch, PDF or registration.

## 2026-10-29 — Claude Opus 5.5 (solver)

- Re-read all seven rows on enlarged crops of work/message-large.jpg and the source rotated 90° CCW. Full body: `Nz. Pxo. E.h Cpz. / Mfuufs uijt / npsjoh, / Uibolt wfsz. / Nvdi gps bmm. / Nz. h.v y. Gspn / Zpvs Pxo. E.h Hjsm` → "My own D.g boy. Letter this mor(n)ing. Thanks very much for all. My g.u x. From your own D.g girl."
- Row 2 first word is Mfuufs (Letter), not Mother: two f-descenders, no i-dot. Second word uijt (this): 3 minims + j + uncrossed t.
- Row 3 is npsjoh: n, p, s, then a long upward j stroke, o, h. No second o is visible → "moring" literally.
- Row 4 Uibolt (Thanks); this writer's s in wfsz is c-shaped.
- Row 6 middle: dotted group h.v y. (h as in E.h; looped v; cursive y with descender). Tried: Mpwf (no p/w/f forms), C.M (best love), H.O (good night: second glyph not a clear o), f for the third glyph (f's lower loop goes back left, this one is ʒ-shaped). Left unexpanded.
- Row 7 last word: H is the heading H. The following glyphs look like "pn" of Gspn but the stem ends in a j-hook; read Hjsm (Girl), literal alternative Hpn (Gom) disclosed.
- Context: 1 Dec 1907 was a Sunday (heading "Sunday"). Aside "going to D." is plain.
- Wrote work/transcript_full.json, work/solve.py (hash check + decrypt), rewrote SOLUTION.md. DONE1 created.
- Note: shared scratchpad paths collided with another agent (r1.png showed another card); crops were redone in a unique subfolder.
