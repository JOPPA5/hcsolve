REVISE

# Review 1 of HCP1298 (Claude Opus 5.5, reviewer, 2026-10-30)

The key and the reading as a whole stand: Feri's New Year letter to Tóth Jolánka is real, coherent Hungarian. But the pixels contradict the ledger at three signs, and each error produced a false "writer's slip" or a false alternative reading in SOLUTION.md. All three corrections make the text *better* (the writer's spelling is more regular than claimed). The normalization needs small fixes, and the three unread spots stay unread.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1298/work/decode.py` ran: all four hashes OK, output equals the rows in SOLUTION.md, 624 tokens.
- **Independent decoder.** `review/work/decode_independent.py` uses my own table, typed from the HCP1216 legend, and does not read `work/key.json`. `diff` against the solver's rows printed nothing (saved as `review/work/indep.txt`, `sol.txt`). This shows the arithmetic, not the transcription.
- **Key coverage.** Every token decodes; four tokens are marks with no value (`[flourish]`, `[bar]`, `[overwritten]`, `[tick]`). No key change is needed, and the key matches the family.
- **Transcription.** I read my own enlargements from the hi-res address scan (`review/work/crop.py`, `z.py`; 2.4x for all 26 rows, 4–7x for the contested signs, rotated strips for the top and right edges, stamp place 2.2x). I compared every row, B1, R1, T1 and S1–S6 sign by sign with the ledger. Apart from findings 1–3 and the unresolved row 11 stretch, the ledger agrees with what I see, including the corner run *magok|nál* and the upside-down top margin (T1 reads *nál mindig csak én nem mulatha-*).
- **Picture side.** Printed Hungarian verse (*Szeretni édes…*) and a couple; no cipher, as stated.
- **Language and context.** Period Hungarian with a semi-literate spelling; addressee, signature and closing fit the family. No published solution appears to be used; the key's origin is disclosed.

## Findings

1. **major — Row 26: the ledger has a sign that is not on the card.** The ledger gives `… 2BAR GAMMA RBOWL LOOP GAMMA CHEVRON …`. `review/work/m26.png` (5x) shows `= Γ ∂ Γ Λ`: nothing stands between the first Γ and the loop. The literal is `mulatot`, not `mulatsot`. My guess is that the left half of the loop, seen at a strip boundary, was read as a `)`. Consequence: uncertainty 11 is wrong, and the "alternative" *mulatsz ott* has no support. *Mulatott* is simply what is written (with the usual single t). Remove RBOWL from row 26, rewrite item 11, and correct the sign count.

2. **major — Row 6: the third sign is Γ, not F.** SOLUTION.md item 6 says it is "a clear F (r)" and treats *mehetek* as a slip. `review/work/r6a.png` (4x) shows a plain Γ with a heavy top bar and no middle arm; the F later in the same row (*mert*) shows the difference. The literal is `hetek`, so *mehetek* is exactly as written. Change the ledger token to GAMMA (no `?`) and delete item 6's slip claim.

3. **minor — Row 15: `foglelva` is literally `foglalva`.** Item 8 says the sign after g-l has "bars crossed by the wave, read e". `review/work/r15f.png` (7x) shows two clean bars, `=`, with no third bar and no crossing: it is a. Change the token to 2BAR and drop that clause. The first sign of the word (long-barred F for f) remains a disclosed oddity.

4. **minor — Row 18, the blot after c.** The ledger gives it no value and item 9 says nothing is secure. On `review/work/y18.png` it has the long diagonal and the crossing tail of the tailed x (z), retraced dark. That suggests the old spelling *czeruzával*. Record it as `TAILX?` or at least name this reading; the word is unaffected.

5. **minor — An undisclosed normalization.** Row 3 is literally `talalja`; normalized.txt prints *találják* and item 14 does not list it. Keep *találja soraim*, as on the sister card HCP1217 (*találja soraim*), or list the change.

6. **minor — Punctuation of rows 14–15.** *…hamarabb, igaz? El vagyok foglalva, hogy nem tűnik-e…* is an editorial break. *Igaz, el vagyok foglalva* ("True, I am busy") follows the words at least as well, and it joins the excuse to the sentence before. Offer it, or adopt it. Then the English "I am so busy" would need changing too, since *úgy* is not in that clause.

7. **minor — "Over the stamp" is the wrong description.** Perforated stamp remains and a torn corner are still on the card (`review/work/st.png`), so S1–S6 lay *under* the stamp, as on HCP1216. Only the pre-printed green triangle is written over. Correct this in SOLUTION.md, the translations and the ledger header.

8. **minor — The plain-hand text is incomplete.** Item 15 gives the address as "Tóth Jolánka úrleánynak", but a violet handwritten first line lies under the cancel (`review/work/zhand.png`): *Szép…*, probably *Szépreményű* as on the sister card's address "Szépreményű Tóth Jolánka kisasszonynak" (HCP1243 SOLUTION.md). The rectangular cancel is upside down and ends *-TA-ÚJPEST P.U.*, the Rákospalota-Újpest station cancel named on HCP1288; "Újpest-related" can be firmer, keeping the lost start marked as restored.

9. **minor — The ledger is not strictly "one token per written sign".** `5 [bar]` in row 12 looks like one numeral with a detached top stroke (`review/work/z12.png`). GYLOOP (13 tokens) is on this card a ς followed by a separate y-shaped sign in most places (rows 1, 17, 20), not "joined", and LRBOWL (5 tokens) is c + s. Say the 624 counts tokens, and fix the key description. The final HP of row 26 is also a looped, 8-like form (`review/work/v26.png`), unlike every other h/p; flag it, though *vasárnap* is secure.

10. **minor — Row 11, date signs.** The first sign is not a plain 8: it has a flat, open top over a closed lower loop (`review/work/z11a.png`). Uncertainty 3 calls the date logic unexplained, but does not offer that this could be a flat-topped 3, which would make the order 3rd then 5th sensible. I cannot decide this from the shape; list it. Also, the Π in `beozat?t?a` has a Γ, a short stroke under the bar, a long stroke from the bar's end and a further faint stroke. "Two fused t" is one guess among several (Γ + n is another), and the reading must stay open, as the solver says.

11. **minor — Status wording.** Three spots are unread, and one of them is the place he is writing from, and another the sense of a whole clause. The status line and the PDF must call this a partial reading of those clauses, not just "whole card read". Item 12 is rightly hedged: the dark sign at the end of T1 is an L when turned, not a Γ, and its dark ink matches row 1, not the faint margin. *-ok* is therefore a supply, and *mulathat* itself rests partly on word sense.

## Could not verify

- Words for `beozat?t?a`, `sesen` and `szra|oma`. I found none, and I confirm the signs of the last two are clear. The row 11 stretch is retraced, and I cannot certify every stroke there.
- The year. No date is legible. The round cancel shows an 8, but its reading as day and its place are not secure, so I cannot relate it to the 8th of row 11.
- Identity of Feri with the writers of other cards.
- *Csókolja szám* (S1–S2): the signs are right; the sense is odd, as item 13 discloses. I have no better reading.

## What must change before FINAL

Fix findings 1, 2 and 3 in the ledger and re-run the command. Update items 6, 8, 11 and the sign count, and apply the smaller wording fixes above. The normalized text changes only in findings 5 and 6; no second review is needed for those edits unless the solver changes the reading further.
