ACCEPT

# Review 1 — HCP 1407 (pc_hcp_88)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Review round 1 on DONE1.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1407/work/solve.py` (run from the repo root) prints `source hashes OK` and the seven lines quoted in SOLUTION.md. Its output matches the claimed plaintext exactly.
2. **Independent decryption.** `review/work/indep.py` holds my own transcription of the five cipher rows, taken from my crops and not copied from the solver's JSON. It applies Caesar −1 on its own:
   `Nz Pxo Efbsftu / Nboz uibolt gps / dbse up-Ebz / gspn zpvs / Pxo Hjsm` → MY OWN DEAREST / MANY THANKS FOR / CARD TO-DAY / FROM YOUR / OWN GIRL. That is 49 letters, all decoded by the one key with no exceptions, and it matches the solver's count and reading.
3. **Transcription against the scan.** I cropped `work/reading.jpg`, the rotated derivative of `source/address.jpg`, and checked it against the source orientation:
   - 3× crops of every row are in `review/work/r1.png` … `r5.png`.
   - 5× crops of the doubtful groups are `z_dbse.png`, `z_ebz.png`, `z_uibolt.png`, `z_l4grp.png`, `z_l5grp.png` and `z_hjsm.png`.
   - Sign by sign I confirm Nz, Pxo, Efbsftu (the crossed cursive E, then b and s written like "6" and "5"), Nboz, gps, dbse, up-, gspn, zpvs, Pxo and Hjsm (H followed by the writer's long slanted j).
   - Doubtful signs, all of them disclosed:
     - `uibolt`: the final t is only a short hook after the l (SOLUTION uncertainty 3).
     - `Ebz`: it looks like "E62" (uncertainty 4). It is supported by the same group `up-Ebz` on HCP1386, 1397 and 1406, and by the matching E, b and z forms elsewhere on this card.
     - `dbse`: the final e has a trailing flourish that could be mistaken for "el". Only CARD makes sense, and it does not affect the key.
   - None of these readings is forced. Each word is a regular Caesar −1 image of a common English word.
4. **Key coverage.** Every alphabetic sign of the message falls into one of three groups: decoded by the key, clear text (the heading "G. H. Tuesday." and the date "May. 14th 1907."), or one of the two disclosed initial groups. No sign was left out or silently dropped.
5. **Context.**
   - `datetime.date(1907,5,14)` is a Tuesday, which agrees with the clear heading, the dated foot and the portal date 1907-05-14.
   - The postmark crop (`review/work/z_postmark.png`) shows WIMBO[RNE], 6.30 PM, MY and 07.
   - The formulas ("Nz Pxo", "up-Ebz", "& … gspn zpvs Pxo … Hjsm") match the sister cards of the same couple: HCP1386, 1399, 1403 and 1406.
6. **Honesty.**
   - The portal status is Not solved and no transcription or solution is attached.
   - The help from comparing with HCP1406 is recorded in SOURCES.md and NOTES.md.
   - The earlier GPT work and the later Claude completion are both credited.
   - The card is not listed in `register-exclusions.json`.

## Findings

1. **minor — the closing initial groups are not decoded.** They are `M. & L.'` before FROM and `N.-1` before GIRL.
   - On the 5× crop (`z_l5grp.png`), the line-5 capital shows a top hook, a descending stroke and a following arch. It could be N or M, and the solver lists both.
   - The raised stroke after it closely resembles the raised tick after L in line 4. It may be the same reduced mark (t/apostrophe) and not a digit "1", so the gloss "No. 1" is weak.
   - The solver claims no expansion and keeps both groups literal, consistent with HCP1386/1399/1403/1406.
   - This is acceptable. In the report I suggest describing the second group neutrally (e.g. "N/M with a raised tick") and not emphasizing "No. 1".
2. **minor — the farm name in the address is under-read.** The solver calls it "Whiteway/Upcott-like, uncertain". On my 3× crop (`review/work/z_addr.png`) the word reads most naturally as **Stokelake** Farm. That is the farm name the sister card HCP1403 reads for the same recipient, Mr W. Abbott of Chudleigh. Context only; it does not affect the decipherment.
3. **minor — the postmark day is only partly visible.** On the crop the "14" lies mostly under or beside the stamp edge; MY and 07 are clear. The date 14 May still stands on the written foot date and the Tuesday heading. The report should not present the postmark day as independently read.

There are no blocker or major findings.

## What I could not verify

- The meaning of the initial groups (`M. & L.'`, `N.-1`) and of the heading initials "G. H.".
- Whether these groups are themselves shifted.
- The original card beyond the single 1024-px scan, such as ink, pencil or later additions.
