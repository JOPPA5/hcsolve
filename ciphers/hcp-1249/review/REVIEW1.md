REVISE

# Review of HCP1249, round 1

Reviewer: Claude Opus 5.5, 2026-11-01. Solver: Claude Opus 5.5 (DONE1).

Summary: the key, the cipher type and most of the reading stand. The solver's ledger is sound on the whole card except for four signs that change the text. Those signs and one word division resolve passages that the solver left open or forced (rows 2-4, rows 9-10, stamp row S6). No finding touches the key. The fixes are concrete, so the verdict is REVISE, not REJECT.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1249/work/decode.py` runs; all four SHA-256 checks print OK; 603 signs; output equals the literal block in SOLUTION.md.
- **Independent decoder.** `review/work/indep.py`, key typed from the HCP1216 table, not imported from the solver. Output in `review/work/indep.out`. All 35 rows equal the solver's literal text (0 differ). 28 sign classes, all with a value, so the key covers the whole ledger.
- **Transcription against pixels.** With `review/work/crop.py` on the hi-res address side I read all 28 main rows and all 7 stamp rows (`g1`-`g6`, `g1b`-`g6b`, about 2x to 2.3x) and enlarged the disputed places 3.5x to 6x (`z_r2`, `z_r3`, `z_r4`, `z_r7`, `z_r10`, `z_r18`, `z_r20`, `z_r26`, `z_r28`, `z_s6`, and `stampA`, `stampB` in the blue channel). Apart from the findings below, the ledger agrees with what I see.
- **Language and context.** The Hungarian is period love-letter prose in Feri's manner. *Árokszállás* matches the address (*Jász-Árokszállás*). The postmark reads 914 MÁR, as the solver says (`work/crops/pm.png`), and agrees with the portal date. *sírig hű kedvese Feri* is in HCP1216.
- **Sources.** The portal metadata shows no attached solution. I found no use of a published one.

## Findings

1. **major, row 2 end: `na` is `ha`.** The pair before the final two bars is the h/p sign, not n. In `z_r2.png` the first stroke is about twice the length of the second, as in the h of *hogy* just before it. A true n, as in `z_r3.png` (row 3 *nag*), has two equal strokes. Ledger `N A` must become `H A`. The text is *hogy ha nincs*. The solver's interjection or false start (Uncertainty 10) goes.
   Together with item 2, this changes the sense of the clause.

2. **major, rows 3-4: forced sense.** "there is no girl who [can] sit up with a close acquaintance until morning" needs a supplied verb and makes poor sense. With *ha*, and with the row 3 sign after *na* taken as k (the solver himself says short S and hooked S overlap on this card, and this one is not distinct), the literal `lanynakismerős|selelülhet` gives *ha nincs egy lánynak ismerőse, elülhet reggelig*: "if a girl has no acquaintance, she can sit there until morning". That is, unasked at a dance, which fits the invitation exactly: it is not like that at the ball he proposes. `s` is doubled across the row break, as in *kedvesse* on HCP1248. The written `sel` still leaves one `l` to account for: `ismerősse lelülhet` or `ismerőssel elülhet`. The solver must say which, and disclose that k here rests on word sense.

3. **major, rows 9-10: the "unresolved" `kifordulnat mes` is a wrong word division.** Read *mindenki fordul[h]at me[g]*: "where not everybody can turn up" (*megfordul valahol*). The solver split `minden | kifordulnat mes`. The signs themselves are as the solver gives them: in `z_r10.png` the pair in `dulnat` is near equal (n, not the 2:1 h pair) and the sign in `mes` is the s bowl. So this needs two writer's slips (n for h, s for g), and that must be disclosed. With his habit of slips (*met*, *szetnék*, *kel*) and his t/r swaps on HCP1248, I accept it as the reading of the clause. The English and Slovak bracket and Uncertainty 2 must be replaced. It is otherwise a whole unread clause end.

4. **major, stamp S6-S7: `nercz` is `percz`.** The first sign of S6 is the h/p sign, not n: in `z_s6.png` the first stroke is much longer than the second. The n of S7 directly below has two equal strokes, so the contrast is on the same crop. Read *annál a percznél*: "than that moment". *percz* is the period spelling, and the same writer has *az a percz* on HCP1279. Then the first sign of S7 is more likely é than the solver's á, because *percz* takes a front-vowel suffix. The blob with its tick does not settle it; *-nál* would be a slip. Keep it marked as read through damage. Uncertainty 4 goes, and so does the solver's claim that "no word on the card needs p". S4-S7 then reads: *édesebb annál a percznél*.

5. **major, row 26: `mot` is `mit`.** The sign before Γ has a dot, clearly separate and in the normal place (`z_r26.png`), so it is i, not o. Ledger `M O T` must become `M I T`. The text is *mit én is alig várok*, "which I too can hardly wait for", with no emendation. The solver's *mo[s]t* and the listed spelling *mot → most* are wrong.

6. **minor, row 20: one T too many.** `z_r20.png` shows one Γ after the blotted o, then v, a, n. The ledger has `O T T`. The literal is *ot van*, as on row 19, and the sign count becomes 602. Normalized *ott* stands.

7. **minor, row 18 `mutnék`.** *mut[at]nék* "I would show [it]" has no object and is an unsupported fit. *mu[la]tnék* "I would make merry" follows directly from *Mulatni is szeretnék kedvemre*, and needs the same size of omission. Give both, prefer neither without a reason. The blotted sign (`z_r18.png`) remains s or k, as disclosed.

8. **minor, small ledger and text errors.**
   - Row 22: *szá* has a tick above the a that the ledger leaves out, though its header says seen marks are transcribed.
   - Row 24: the vowel shows two bars, so a; drop the `{a|e}`.
   - Row 2: `min` → *mint* is normalized but missing from the spelling list (Uncertainty 12).
   - "Why it is correct" says *hogy* ×6. The ledger has 4. Fix the count.

9. **minor, context check not made.** 24 and 25 July 1914 were a Friday and a Saturday. That is not an objection, but it is the only date check available and SOLUTION.md does not make it. Anna-day balls around 26 July are a possible context, unproved; do not assert it.

## Claims I tested and accept

- Row 1 `meretség`: the eight signs are as given. No better word found. Isolated.
- Row 23 `viszontfuk`: the signs are as given (Γ, upright cross, u, short S). No better reading found. Isolated.
- Row 7 blot and row 13 blot are honestly described. The double tick on row 7 stays unexplained, which SOLUTION.md says in substance.
- Stamp S1, S2, S4, S5 and S7's *Feri* are readable in the blue channel. S2 *alig va* is better than the solver's "faint" suggests.
- S3 is correctly marked weakest. I see r, o, m through the blot and then an h/p sign and a dotted i, but only one clear d-like sign after that, so *hidd* stays tentative.

## Verdict conditions

After items 1-8 the card has only rows 1 and 23 as isolated unread words plus the disclosed S3 weakness, so it meets the batch's rule for a complete card. Re-run the command after the ledger edits. A new round is not needed for these fixes unless the solver disputes items 2-4 with a substantially different reading.

## Could not verify

- Rows 1 and 23: no reading found, so I cannot say whether they are errors or unknown words.
- S3 (`rom`, `hidd`) and the vowel of S7: the stamp gum removed too much ink.
- Whether the row 3 sign is k or g: pixels do not decide, only sense.
- Items 2 and 3 are word-sense readings resting on disclosed slips, not on pixels alone.
- That this Feri is the Feri of HCP1216; the same limit the solver states.
- I read ordinary rows at about 2x and enlarged further only where needed, not every sign at 5x.
