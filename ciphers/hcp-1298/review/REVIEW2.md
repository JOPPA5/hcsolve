REVISE

# Review 2 of HCP1298 (Claude Opus 5.5, reviewer, 2026-10-30)

The reading stands, and it can get better. The one "unknown word", `szra|oma`, comes from two mistranscribed signs, and I missed them too in round 1, where I called those signs clear. The word is *soraim*, the same word as in row 3: *hogy ott írom soraim, ahol nem lehet tentet szerezni*, "that I write my lines there, where no ink can be had". The new row 11 reading *a postás és én* holds on the pixels. The verb before it stays tentative.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1298/work/decode.py`: all four hashes OK, 622 tokens, rows identical to SOLUTION.md.
- **Independent decoder.** `review/work/r2/dec2.py` is a new table typed by me that does not read `work/key.json`. Its output (`own.txt`) has no diff against the solver's rows (`sol.txt`) with the ? marks removed. Every token decodes, apart from two value-less marks (`[flourish]`, `[tick]`). This tests the arithmetic only.
- **Pixels.** Crops from the hi-res address scan, 2.4x to 6x, are in `review/work/r2/` (scripts c.py to c6.py). I read sign by sign: rows 3, 4, 5, 8, 10, 11, 16, 17, 20, 21, 23 and the stamp place. These were the round 2 changes, every open item, and a sample of ordinary rows. Rows and margins not re-read here were compared in round 1 and have not changed since, except for the fixes checked against that review.
- **Disclosure.** No published solution is used. The key's origin and the earlier family work are stated.

## Findings

1. **major: rows 20–21 `szra|oma` is a transcription error; the word is *soraim*.** Evidence is `review/work/r2/compare_soraim.png`, `z20end.png`, `z21start.png`, `r3soraim.png`.
   - Row 20, sign after the `)`: the ledger has TAILX. It is one arched stroke running down to the lower left in a narrow retraced loop, with an arm to the right. The tailed x of this card (rows 4, 5, `w5b.png`) has a crossing stroke with a tail running on below the crossing. That tail is absent here. So this is not z but a sign of the loop class.
   - Row 21, first sign: the ledger has LOOP. Its long straight top bar, closed lower loop and crossing arm are the DOTLOOP form (compare row 11's second sign and S6, `n3.png`), not the rounded-top o. No dot is visible, but dots are also missing on *feri* (S6) and on the i of row 3 *soraim*.
   - Result: `s o r a | i m a hol`, six signs matching row 3 `RBOWL LOOP FSIGN 2BAR DOTLOOP 3STROKE`, and row 3 uses the same bare accusative (*találja soraim*). `ott … ahol` becomes a plain correlative.
   - **What rests on what:** "not z" and "loop class" rest on shape. The o / i call within that class rests on word sense, because the row 20 sign also resembles the undotted i of row 3. Mark both tokens `?`.
   - Tested in `review/work/r2/ledger-proposed.txt` (`20 … RBOWL LOOP? FSIGN 2BAR`, `21 DOTLOOP? 3STROKE 2BAR HP …`): 622 tokens, row 20 ends `…sora`, row 21 begins `imaHol…` (H = the h/p sign).
   - Consequences: update the ledger, literal rows, normalized text, all translations, uncertainty 3, "Why I believe" and the status line. Delete the claim that where he writes from is an unread place-name, and withdraw "signs clear". English: "that I write my lines there, where no ink can be had". Slovak: "že svoje riadky píšem tam, kde sa nedá zohnať atrament".

2. **minor: status must be reassessed.** With finding 1, the only word-level gap is the verb of row 11. "One word not understood" and "where Feri writes from is not established" no longer apply. Whether one tentative verb keeps the card partial is the solver's call under family practice, but it should rest on that verb alone, and it must be stated in those terms.

3. **Confirmed, no change: *a postás és én* (uncertainty 2).** `p11.png` shows `/' ∂ ) Γ = ) ≡ ) ≡ ||` cleanly: two bars after Γ, three bars after each later `)`. No sign changes. *És* is spelled the same in rows 9 and 12, and the clause runs on naturally into *5-ikén kaptam kézhez*. A heavy tick stands above the last e (`e10b.png`), which could be the accent of *én*, or a stray stroke; it is weak evidence and worth a line.

4. **minor: row 10 d is better than claimed (uncertainty 7).** `e10a.png` shows a short stroke set left of a long one, the same form as the d of row 4 *kedvesem* (`w4.png`), not two equal strokes as in n. Drop the `?` and rewrite item 7. Reading *édesem* stands.

5. **minor: the key note undersells the d / p difference.** It says d and p are "the same kind of sign". On this card the tick is on the left of the stroke in d and on the right in h/p (`w5b.png`, `sam23.png`). The two are separable by shape, so word sense is needed only for h against p.

6. **minor: 3 or 8 (uncertainty 3a) stays undecided, and is honestly described.** `n3.png`: flat top bar, diagonal, closed lower loop. Printing 3 is defensible on date order, and the solver calls it a choice. *-ikán* fits both numerals (*harmadikán*, *nyolcadikán*), so that gives no help. The Epiphany question also suits a card written just after 6 January, in line with the round cancel's 8, though I read neither month nor place there.

7. **minor: row 11 verb, keep it tentative and say more.** `w11.png`: after the b the strokes run together, and the supposed e is a dark hooked stroke plus one faint bar. Faint bars after the z and the Π with its extra faint stroke look like correction. So *behozta*, with the extra strokes as a corrected false start, is at least as good as *be[h]ozatta*, and it is the commoner word with a postman as subject. Offer both. Neither has a visible h. The English "brought in" actually renders *behozta*, so the normalization and translation should agree.

## Could not verify

- The verb of row 11, and the numeral 3 or 8.
- The year and month of the cancels; the identity of Feri beyond the family.
- *Csókolja szám* (S1–S2): the signs are as stated, the sense stays odd, as disclosed.
- *válasz[oltam]*, a supply for literal `valaszan`.
- That the dot is really absent from the row 21 sign rather than lost; the paper there shows nothing.

## What must change before FINAL

Apply finding 1 in the ledger and everything derived from it, re-run the command, and apply findings 2, 4, 5 and 7. If the solver makes only these changes, no third review is needed; any further change of reading should go back as DONE3.
