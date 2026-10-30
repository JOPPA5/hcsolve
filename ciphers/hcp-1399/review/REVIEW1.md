ACCEPT

# Review 1 — HCP 1399 (pc_hcp_80), Caesar −1, round 1

Reviewer: Claude Opus 5.5, 2026-10-30. Reviewed: SOLUTION.md / NOTES.md / work/ as handed over with DONE1.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1399/work/solve.py` (from repo root): source hashes OK; output
   `MY OWN [E.h.] / MANY THANKS / FOR "SWEETS" / THIS MORNING. / [N & Lt] FROM / YOUR OWN [E.h.]`, 46 enciphered letters.
   Identical to the plaintext table in SOLUTION.md.
2. **Independent decryption.** `review/work/decode_review.py` uses my own transcription taken from my own crops
   (not the solver's JSON) and tries all 26 shifts. Only shift −1 gives English:
   `MY OWN / MANY THANKS / FOR SWEETS / THIS MORNING / FROM / YOUR OWN` (46 letters). The key covers every
   enciphered word on the card; no letter is inserted, dropped or left over.
3. **Transcription against the scan.** I rotated `source/address.jpg` 90° CCW (`review/work/rot.png`) and made
   my own 3–7x enlargements: `r_head.png` (heading + salutation), `r_body.png` (three body lines),
   `r_close.png`, `r_nlt.png`, `r_gspn.png`, `r_eh.png`, `r_post.png`. Sign by sign:
   - `S. 7. Sunday.` plain heading — clear.
   - `Nz Pxo` — N with high lead-in stroke (the writer's N), z clear; P looped with long stem, x, o. Clear.
   - `Nboz uibolt` — clear; the final t has its cross written as a trailing dash.
   - `gps "Txffut"` — looped g, p, s; T written like a 7; double f; quotation marks visible before and after. Clear.
   - `uijt npsojoh.` — clear, full stop visible.
   - `gspn` — a long looped g whose descender runs into the line below, then s, a heavy p overwritten by the stroke from the line above, n. The individual s/p are only partly separable, as the solver says (uncertainty 3); the word length and the shapes fit, and FROM is the fixed formula of the sister cards (`gspn` on hcp-1386, 1395, 1402, 1407). Accepted.
   - `Zpvs Pxo` — clear.
   - `E.h.` (twice) — a loop sitting on a c-shaped bowl (cursive E), dot, h, dot. Both occurrences have the same form. Literal reading is fair; not expanded. Disclosed.
   - `N & Lt` — capital with two arches (N; M not excluded), reversed-c ampersand, L with looped foot, then a small looped letter and a detached dash. Disclosed and kept literal.
   - Postmark (`r_post.png`): `7.30 PM / E 2 / 08` with lower arc `…N ABBOT` — matches the solver. Only `E` of the month is legible.
4. **Date check.** `datetime.date(1908,2,2)` is a Sunday, agreeing with the heading "Sunday". Since the month is only `?E`, the solver correctly calls this consistent, not proved.
5. **Context.** The sister series hcp-1386…1407 is letters from a girl to Mr W. Abbott, Chudleigh (near Newton Abbot); hcp-1407 was posted at Wimborne, Miss Dean's town. This card goes the other way (Newton Abbot → Miss Dean, Wimborne), consistent with the solver's statement. Halfpenny Edward VII stamp fits 1902–1910. The plaintext ("many thanks for 'sweets' this morning") is ordinary Edwardian English.
6. **Honesty.** Portal status Not solved, no attachment solution (SOURCES.md, metadata.md). Earlier GPT work and Claude's completion are credited separately. All interpretive material (E.h., N & Lt, gspn, postmark month, heading) is disclosed. No restoration of letters is claimed.

## Findings

1. **minor — `N & Lt`: the "t" deserves a weaker label.** On my crop `r_nlt.png` the sign after L is a small loop followed by a separate dash; the same writer ends `uibolt` with a dash-cross t, so "t" is possible, but the dash could equally be the L's flourish/full stop and the group could be the family's usual `N. & L.` (hcp-1386, 1402, 1403). SOLUTION.md should state that `N. & L.` (as on the sister cards) is an equally possible reading and that the Caesar −1 value is then `M. & K.`.
2. **minor — family-level inconsistency not mentioned.** hcp-1395 reads the same closing slot as enciphered (`M. & L.` → L. & K., "love & kisses"), while hcp-1386/1402/1403 and this card keep it literal. That is acceptable, but SOLUTION.md should mention the hcp-1395 treatment so readers see both options. Similarly, hcp-1400 (also to Miss Dean) has `E.h.` in its salutation; citing it would support the `E.h.` reading better than the `El.` of hcp-1386.
3. **minor — `gspn` letters partly overwritten.** Disclosed (uncertainty 3); the report should keep this note and not present the word as fully clear.

No blocker or major findings.

## What I could not verify

- The month letter(s) of the postmark before `E` and the full upper arc of the office name (only `…N ABBOT` lower arc readable).
- What `E.h.`, `N & Lt` and `S. 7.` stand for, and whether the initials are themselves shifted.
- The house name in the address ("Queen's House" vs. hcp-1400's "Court House") — not part of the message.
- Whether a published solution exists elsewhere than the portal (none found by the solver; I did no web search).
