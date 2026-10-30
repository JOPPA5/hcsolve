# HCP 1388 — solver notes

2026-10-26: Read README in full. Root supplied fresh rendered three-tab provenance: Not solved, no attached solution. Personally inspected both original scans. Picture is Nottingham Castle, with no observed handwriting. Address-side message is vertical; made a working 270-degree rotation and enlarged crops. Original bytes unchanged.

Alphabet shift minus one is supported directly by Nz→My, Efbsftu→Dearest, uibolt→thanks, gps→for, Zpvs→Your, pxo→own, hjsm→girl. No corpus or published solution used.

Initial transcript: Nz Efbsftu uibolt / gps mfuufs ju Xbt / [unresolved] [cancelled] Nz [unresolved] gspn / Zpvs pxo hjsm. Six-letter mfuufs gives letter singular. Xbt gives Was. These words do not settle the difficult row below.

Line 3 first word resembles gjof (fine), but I have not frozen that reading. The next dense mark is cancelled. A later group between Nz and gspn comprises large loops; length and letters remain uncertain. Do not replace it with love just to make a fluent closing. Both unclear groups need further visual work. Farm name and C. H. heading are also not secure.

Ran work/decode.py: source hashes match; frozen transcription yields 46 letters. This is reproducibility of a manual partial transcript, not pixel recognition. No DONE or register entry; no watcher/reviewer launched under the persistent human override.

2026-10-29 (Claude Opus 5.5, solver): Completed the reading. Re-cropped source/address.jpg (rotated 90° CCW, 3–10x) — note: a shared scratchpad briefly served another card's crop; all readings below were redone from this card's own source in a private subfolder.
- Line 3 word 1 `gjof` → fine confirmed (j dot visible above line) — `work/c-l3-gjof.png`.
- The old "{L3-B}" group: the long diagonal and left oval loop are the descender and descender loop of the tall j of line-2 `ju`. Remaining signs: capital N (as in line-1 `Nz`), y (big top curl, stem merged with j descender), y (small hook, diagonal, foot) → `N yy` → "M xx". Parallels hcp-1390 "to day. M yy From your own Girl" — `work/c-l3-nyy-and-j-descender.png`, `work/c-l3-yy-10x.png`.
- The old "{CANCELLED}": two small dense star-shaped marks in darker ink, no letter form; kept as [**], not read (crosses / blots / cancelled letters all possible).
- Line 4 `Hjsm` H is a crossed slanted stroke + second stroke, as on hcp-1390 — `work/c-l4-hjsm.png`.
- Postmark …MBORNE 10 PM AP 15 (year faint) agrees with written date April 15th 1907.
- New transcript work/transcript_full.json and command `python3 -I ciphers/hcp-1388/work/decode_full.py` (hash check + asserted plaintext, 51 letters). Plaintext: "My dearest, thanks for letter, it was fine. [**] M xx from your own girl." SOLUTION.md rewritten; DONE1 created.
