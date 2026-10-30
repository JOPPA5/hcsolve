ACCEPT

# Review 1: hcp-1373 / pc_hcp_54 (reviewer: Claude Opus 5.5, 2026-10-30)

I tried to refute the reading and could not. Key, transcription and plaintext stand. Only minor points remain. Solver and reviewer are both Claude Opus 5.5 on this card, so this is not an inter-vendor check.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1373/work/decode.py` runs. Source hashes pass, and the output matches the SOLUTION.md table. It reports 63 enciphered and 6 abbreviation letters.
- **Hashes.** `shasum -a 256` on the two `source/` files and two `work/hires/` files matches SOURCES.md.
- **Independent decode.** `review/work/mine.py` has tokens typed from my own crops and its own shift loop. Output: MY OWN / BOY / I AM GOING ON / NCIELY ABOUT / MY ROOM TRY USUAL / FOR MY / FROM YOUR OWN / GIRL. 63 letters, identical.
- **Coverage.** One shift covers every enciphered token. Unenciphered items are the heading, "No 1", "Friday", "&", `E. L.` (twice) and `N. & L.`
- **Transcription.** From `work/hires/pc_hcp_54_adr.JPG`, rotated by me, I made 3-4x crops of every row (`review/work/h, r1, r2, r3, r4a, r4b, r5a, r5b, r6, r7`) and 7x crops of the hard places (`z_nicely, z_usual, z_going, z_L`). I read every sign. All tokens are as transcribed. "Friday" is plainly written, with F, r, i, d, a, y all visible.
- **`odjfmz`.** The solver's sign order holds (`z_nicely`). The bowl-and-stem sign comes first. The j stroke starts to the right of that stem, directly under the detached dot, and its hooked foot runs back under the bowl. Then come the looped f, m and z. The slip is real and disclosed, and the table marks NICELY as an emendation.
- **`Vtvbm`.** This was the place most open to forcing, and I tried to break it (`z_usual`). The second sign is a tall stem with a long bar running right from its top. That matches the crossed t of `Nztufsz` on hcp-1376 (`hcp-1376/work/crops/l6.png`) closely. It is not an h: the flag on the h of `hpjoh` on this card leads in from the left (`z_going`). Then come down-up (v), a tall stem with a bowl (b), and m with a tail reaching the card edge. The tail runs off along the baseline, and I see no extra letter. THANK, VITAL and TRIAL fail because a t stands in second place. Words of the form ?-T-?-A-L give USUAL only. The reading comes from the signs, not from context.
- **Date and context.** 4 Nov 1907 was a Monday (computed), which matches the heading. The postmark reads WIMBORNE, 10 PM, NO 4, 07. The address reads Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. "No 1" (Mon 4 Nov) fits "No. 3" on hcp-1376 (Sat 9 Nov).
- **Language.** Natural Edwardian English. "Going on nicely" and "about my room" are good period convalescent phrasing. The formula `Nz Pxo E. L. Cpz ... Nz N. & L. Gspn Zpvs Pxo E. L. Hjsm` recurs on sister cards (hcp-1376; hcp-1403 has it without "from").
- **Sources.** No published solution appears. Portal status is Not solved with no attachment. The number is in neither skip.txt nor register-exclusions.json.

## Findings

1. **Minor: the heading initial is better read G than C.** The first capital has a small rising foot stroke at its lower right (`h.png`), which is a G tail. Sisters hcp-1374, 1375 and 1376 give "G. H.". The solver disclosed C/G but prints "C. H." in the title line, table and translation. Prefer "G. H." and note the doubt. The solver's wording "sister cards differ" should be checked; the three I read all have G.

2. **Minor: uncertainty 5 overstates the match for `Nz` in row 1.** The solver calls the z a tail "joined after the N" and "the same form" as hcp-1376. On hcp-1376 the z is a clearly detached 7-shaped sign (`work/crops/z_nz2.png`). Here the third stroke is shorter and sits closer to the N (`r1.png`), so it could be taken for a third stem of an M. MY still stands on the formula and on the fuller `Nz` in rows 4 and 5. Say it is a compressed form, weaker than on hcp-1376, and that the z here rests partly on the formula.

3. **Minor: two sign shapes are not described.**
   - In rows 1 and 6 the P of `Pxo` has a very long flat bowl and looks like a T at first sight. The T-reading gives `Txo`, which is no word. The form is the big-bowled P of hcp-1376 and hcp-1386.
   - The L opening row 6 has a top flag (`z_L.png`), unlike the plain L of `E. L.` in row 1.
   Neither changes the reading, but the PDF reader should be told.

4. **Minor: "Why it is correct" lists USUAL among long words decoding "with no per-word adjustment".** That is true of the signs, but it is also the card's hardest word. Qualify it by pointing to uncertainty 2.

## What I could not verify

- The sense of "try usual for Friday" and of the abbreviations E. L., N. & L. and G. H. The solver leaves these open, and rightly so.
- Whether a mark was lost past the card edge after `Vtvbm`. The scan ends at the card edge, and nothing suggests one.
- The picture side beyond the conversion and original scan: I hashed it but did not re-inspect it sign by sign. The solver reports no handwriting.
