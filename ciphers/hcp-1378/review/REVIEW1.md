ACCEPT

# Review 1: hcp-1378 / pc_hcp_59 (reviewer: Claude Opus 5.5, 2026-10-30)

Reading confirmed: "G. H. Thursday. My own E. L. boy, have I sent card of The Martyrs Memorial, Oxford? Your girl. Nov. 14th 07." Caesar, plaintext +1. Only minor points remain.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1378/work/decode.py` ran clean: 4 hashes OK, output equals the SOLUTION.md table, 31 enciphered letters and 2 literal.
- **Independent decode.** `review/work/indep.py` uses an explicit table, shares no code with the solver and takes the tokens as I keyed them from my own crops: MY OWN BOY / HAVE I SENT / CARD OF / YOUR GIRL, 31 letters, 20 distinct cipher letters. The key covers every enciphered token with no exception.
- **Transcription.** `review/work/crops.py` makes my own crops from the un-converted `work/hires/pc_hcp_59_adr.JPG`, rotated 90 degrees CCW (2.4x whole lines, 4-5x words). I read all eight written lines, not a sample, and looked separately at Pxo, Tfou, dbse, Ibwf, J, Zpvs and Hjsm. There are no restorations or completion sections; this is a first-round handover.
- **Clear lines.** "G. H. Thursday.", "The Martyrs Memorial", "Oxford." and "Nov. 14th 07." are visible as claimed. Shifting them either way gives nonsense (`sgd lzqsxqr ldlnqhzk nwenqc`).
- **Date.** 14 Nov 1907 was a Thursday (`calendar`). The postmarks are legible: WIMBORNE NO 14 07 and (NEWT)ON ABBOT 11.30 AM NO 15 07.
- **Address and picture.** Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon. Picture side is "Sea Front, Herne Bay", 13590, no handwriting (`review/work/pic.png`). Wrench Series Nr. 13590 is on the address side.
- **Sister formulae.** hcp-1386 has the identical `Nz. Pxo. E. L. Cpz.`; hcp-1398 has `Nz. pxo. efbstu Cpz.`; hcp-1397 has `Zpvs. Pxo Hjsm.` These back the key and the literal E. L.
- **Solver's Oxford claim.** Grepping SOLUTION.md and NOTES.md of hcp-13* and hcp-14* finds Oxford/Martyr only in hcp-1378 itself, so the claim holds.
- **Language.** Natural English of the period and of this correspondence. The Martyrs' Memorial is a real Oxford monument. Nothing is forced onto noise.
- **Sources.** No published solution is used, and the sister-card origin of the key is disclosed.

## Findings

1. **minor: v/w uncertainty is disclosed for only one of three tokens.** Uncertainty 3 flags the blotted `x` of `Pxo`, but the same weakness applies to `Ibwf` and `Zpvs`. The third sign of `Ibwf` is a small two-humped form joined to b and f (`w_ibwf.png`) and is hardly different from the `v` of `Zpvs` (`w_zpvs.png`). The u/v/w choice there rests on the word (HATE, HAVE; YOUR), not the pen shape. Add one line; the reading does not change.
2. **minor: the `d` comparison in Uncertainty 2 is overstated.** The first sign of `dbse` has a long lead-in and a tall slanted ascender; the d of "Thursday" is short and a-like (`l1.png`, `w_dbse.png`). What excludes A is the word (Z-ARD), not a shape match; a capital D would decode the same. Also, the last sign is not "filled": in the 4x crop it is open with a notched right end, e/c-like (`w_dbse.png`). CARD is still the only sense.
3. **minor: `Pxo` middle sign.** At 4x it is a blot with a stem and a rising stroke (`w_pxo.png`). x is plausible but not positively seen; OWN relies on the sister formula. This is disclosed correctly and is listed only to confirm that it stands as "context-supported".
4. **minor: layout not recorded.** `Zpvs Hjsm` and "Nov. 14th 07." are on one physical line, with the date on the LEFT and the signature on the right. The table and `transcription.json` split them and put the signature first. A long underline below `Hjsm` (`l7.png`), which is not part of the text, is not mentioned. The j of `Hjsm` has a hooked descender down to that underline, and the `J` of the third line is a plain slanted hook. Note the layout in the report.

## What I could not verify

- The meaning of E. L. and of G. H. (the solver leaves both open; G is clear from the tail, as against C on some sister cards).
- Whether the Oxford card survives or which it was.
- Whether a published solution exists on the open web: I ran no web search, and the portal shows none attached.
- The hires original is 1785x1175, so stroke order in the T-f ligature of `Tfou` cannot be proved. The two-sign reading is the only one giving a word (`w_tfou.png`).
