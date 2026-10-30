ACCEPT

# Review 1 of hcp-1357 / pc_hcp_38 (Claude Opus 5.5, reviewer, 2026-10-30)

The reading stands: Caesar +1, "My own dearest boy, this will make the pair for album. From your girl." Date in clear: March 22nd 07. I tried to break it on the pixels and could not. Only minor disclosure and transcription points remain (below). Fixing them changes no plaintext letter.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1357/work/decode.py` from the repo root: "source hashes OK", 54 enciphered letters, output identical to the table in SOLUTION.md.
2. **Independent decryption.** `review/work/decrypt_independent.py` decodes my own transcription, made from my crops. My letters are the same as the solver's; I differ only in punctuation (finding 2). All 26 shifts were scored against a word list built from the claimed reading plus common words: shift 1 hits 14 of 14 words, every other shift 0. That list contains the claimed words, so this shows that one shift fits and no other does; it is not an independent language test.
3. **Transcription against the scan.** I rotated `work/hires/pc_hcp_38_adr.JPG` 90 degrees counter-clockwise (`review/work/adr_ccw.png`) and enlarged it 3 to 9 times, some crops with contrast stretch (`review/work/r_*.png`, `z_*.png`). Every word was read; the crops include each point in SOLUTION.md (`Uijt`, `Xjmm`, `qbjs`, `gps`, `Zpvs`, `gspn`, `Hjsm`, `bmcvn`, `Efbsftu`).
   - **qbjs/gps:** confirmed. The first sign of line 3 has a long descender closing in a loop (`z_q.png`); the g of `gps` has a short hook. The loop matches `qptu` on hcp-1395 in the solver's comparison crop. PAIR holds.
   - **Uijt:** the first sign does look like h. Sister cards hcp-1358 and hcp-1362 record the same tall-stroked word-initial u of this writer, in `uijt`, so the reading is supported. Dots for i and j are both visible.
   - **Zpvs:** Z and p are clear. The disclosed restoration is honest: the last sign is an unreadable brown mass with no letter structure (`z_blot.png`), and the v is only a low stroke plus a rising stroke. Neither is forced beyond what is disclosed.
   - **Xjmm minims:** about six strokes after the j, which fits mm; they cannot be separated one by one (`z_mm.png`).
   - **Line start:** nothing is missing at the left of line 3; the card continues past it.
4. **Key coverage.** One shift, no per-word change, all 54 letters.
5. **Context.** Address side: stamp, WIMBORNE postmark with PM, MR and 07 legible, and Mr W. Abbott's address are as described (the day in the postmark is only partly legible). The clear date is "March 22nd 07". Picture side is print only, hymn verse credited to Neale. "My album" also appears on sister card hcp-1398, and the formula and groups fit the Abbott series. Period English.
6. **Sources.** No published solution is used; the absence of a separate web search is stated. Credit is truthful.

## Findings

1. **minor: undisclosed anomalous j in `Xjmm`.** The second sign has no dot, unlike the j's of `Uijt` and `qbjs`, and it has a large head loop with a hooked tail, so it is nearly the same shape as the g of `gps` (`z_j.png`). Literally it would give WFLL, so WILL rests on sense and on the word on hcp-1351, not on the sign alone. SOLUTION.md does not mention this, and "Only the disclosed blot depends on a restoration" is therefore too strong. Add it as an uncertainty and soften that sentence.
2. **minor: two dots omitted.** Uncertainty 8 says dots are kept as read, but there are small dots after `gspn` and after `Zpvs` (`r_all.png`, `z_blot.png`) that are not in the table or in `transcription.json`. Add them, or say that they are left out. No letter depends on them.
3. **minor: other undisclosed letter forms.** The second f of `Efbsftu` has a closed round head and a straight descender, with no ascender or lower loop, unlike the other f's on the card (`z_efb.png`). The c of `bmcvn` has a closed e-like top, and the v of that word is cursive and run into the n stroke (`z_album.png`). The j of `Hjsm` also has no visible dot. All are settled by sense (DEARPST, ALDUM and GORL are not words), but the claim that the shift was checked word by word from the sign alone should mention them. Together with finding 1 they also show that head shape alone does not separate g, j, q and f in this hand. The q reading therefore rests on the descender loop and on sense, as uncertainty 3 mostly says already.
4. **minor: `Uijt` capital U.** The sign is the writer's tall word-initial u, as recorded on hcp-1358 and hcp-1362. There is no evidence for a capital; `uijt` would be the better transcription, or cite those cards instead of "capital or enlarged u". The capital T in the reading is not a plaintext issue.

## What I could not verify

- The last letter of `Zpvs` as an actual s: no pixel evidence either way. YOUR rests on the sense and on this writer's usual `Zpvs` (for example hcp-1376).
- Which card "the pair" refers to.
- The q on hcp-1368 and hcp-1376: I looked only at the hcp-1395 comparison.
- Whether a published solution exists outside the portal and the repo: I made no web search either.
