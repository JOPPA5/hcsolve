ACCEPT

# Review 1, HCP 1349 / pc_hcp_30 (reviewer: Claude Opus 5.5, 2026-10-30)

The solver's reading stands: Caesar -1, English, "My own [..] boy, this church is opposite Park Place. The last one of this stock. [..] Your own [..] girl." I tried to refute it and could not. The findings below are all minor. Note that solver and reviewer here are the same model, in separate sessions.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1349/work/solve.py` runs; hashes OK; 69 letters; output equals the SOLUTION table.
- **Independent decoder.** `review/work/dec.py` uses rows I typed from my own crops, with its own shift code. Same plaintext, 69 letters. Shifts 0, 2 and 25 give no language.
- **Key coverage.** All 69 letters take the one shift. Nothing is restored and no letter needs an exception. The only undeciphered material is the abbreviation groups, which are disclosed.
- **Transcription.** I rotated the original `work/hires/pc_hcp_30_adr.JPG` 90 degrees CCW and read every row on 3-6x crops (`review/work/r_*.jpg`, `z_*.jpg`; scripts `rot.py`, `c.py`, `c2.py`). Every enciphered word agrees: Nz Pxo Cpz / uijt Divsdi Jt / pqqptjuf / Qbsl Qmbdf / uif mbtu pof / pg uijt tupdl / Zpvs Pxo / Hjsm.
- **Hard spots, sign by sign.**
  - `Qbsl` capital (`r_park.jpg`): top-left hook, arc, long diagonal, closed bottom-left loop, tail right. This is the same build as the capital of `Qmbdf` (`r_place.jpg`), so one letter is the sound reading. It differs from `Z` of `Zpvs`, which has a small flat foot and no closed loop (`r_l7.jpg`).
  - I tested **York Place**, a real Stray-side street in Harrogate, as the best rival (`Zpsl`). It fails on the pixels: sign 2 has its bowl at the foot of the stem and stops at the baseline (b), while this writer's p has its bowl high and the stem running far below the line (`r_opp.jpg`, `r_l6.jpg`). The capital would not be Z either. PARK stands.
  - `pqq` (`r_opp.jpg`): pale but readable as two bowls with descenders; g gives no word. The disclosure is accurate.
  - `tupdl` final l (`z_stock.jpg`): loop and foot are visible behind the f descender of line 5. Accurate.
  - `Qmbdf`: the top of the capital does overlap the f descender. Accurate.
- **Language and sense.** Ordinary English. "This church" matches the printed Christ Church view. The formula matches sister cards such as hcp-1369.
- **Date.** 31 Aug 1907 was a Saturday (computed), matching the heading.
- **Published solutions.** Portal shows none; SOLUTION discloses this. I did not search for one beyond the street lookups below.

## Findings

1. **minor: the literal group capital is probably M, not N.** In lines 1, 7 and 8 the capital has three downstrokes (`r_l1.jpg`, `r_l7.jpg`, `r_l8.jpg`), against two in `Nz` on the same line. hcp-1369 uses this same criterion to report `M-h`. SOLUTION writes `N-h` / `N- L.'` and glosses them as "shifted M. G." / "M. K.", which assumes N. Fix: report M (or N/M) and correct the shifted gloss. No effect on the plaintext.
2. **minor: the "short dark foot" of the `Qbsl` capital is said to have no parallel, which overstates it.** Darker touches on pale strokes recur nearby: inside the first p's bowl and on the first q in line 3 (`r_opp.jpg`), and at the s foot in `Qbsl` itself (`r_park.jpg`). It looks like re-inking, not a separate stroke. Also, `Nbsl` / `Mbsl` are less open than SOLUTION suggests, because the capital matches the Q of `Qmbdf`. The current wording is cautious and honest, so this is optional.
3. **minor: "Park Place" remains unverified, as SOLUTION says, and a nearby real name should be mentioned.** Two web searches found no Park Place in Harrogate. They did find a Park Parade in the Christ Church area (listed Park House, Park Parade) and York Place on the Stray. The ciphertext clearly spells PLACE, not PARADE, so the transcription should stay. The report should say that the street name is the writer's and unconfirmed, and may be a loose name for Park Parade (a possibility only).

## What I could not verify

- The postmark. I see fragments on the stamp only (`z_stamp.jpg`) and could not confirm the town, or "10 / AU 31? / 07" beyond fragments consistent with it. The portal date and weekday agree.
- The meaning of the abbreviation groups and of "G. H.".
- Whether a Park Place existed in Harrogate in 1907.
- "The last one of this stock" as meaning the last postcard: this is the solver's gloss, labelled as such, and I find it reasonable.
