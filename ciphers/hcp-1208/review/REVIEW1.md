REVISE

# Review 1 of HCP1208 (Claude Opus 5.5, reviewer, 2026-11-02)

Summary: the key, the type and rows 1 to 18 stand, including the difficult rows under the postmark. The closing sentence is misread. Row 20 is not *banatom* and row 21 is not *szretok*: the signs give **bezarom** and **sirig**, so the card ends with the family's standard formula, *Ezzel bezárom soraim, maradok sírig hű kedvese, Feri*. This removes the solver's uncertainties 6 and 7 and one of the "a/e slips" in 8. Fixes are concrete and small, but the normalized text and all translations change in the last sentence.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1208/work/decode.py`: all four hashes OK, output equals the literal block in SOLUTION.md, 421 tokens, 1914-10-15 is a Thursday (*holnap, azaz pénteken* fits).
- Made my own crops from `work/hires` adr scan with my own violet/black separation and saturated colour: `review/work/ink.py`, lists `b.txt`, `c2.txt`, `c3.txt`, output in `review/work/crops/`. Every row was read at about 2.7x, and rows 4, 5, 7, 9, 10, 19, 20, 21 at 4 to 6x. `review/work/panel.py` builds a same-scale sign comparison (`crops/panel.jpg`).
- Independent decoding: `review/work/redecode.py` holds my transcription as **sign classes**, not letters, decodes with the hcp-1216 table and diffs against the solver's ledger. Run from the cipher directory: `python3 -I review/work/redecode.py`. Result: 419 signs against 421. Rows 4 and 12 differ only by the h/p token convention. The real differences are rows 19, 20 and 21, below. In row 21 my table prints k for the 5-shape; see finding 2.
- Key coverage: every sign on the card falls in the hcp-1216 table; no new value is needed. This confirms the solver's claim of an unchanged key.
- Rows under the postmark, judged separately: row 4 *ezt a lapot*, row 5 *mert maga is*, row 9 *hogy a vona-* and row 10 *lemondjak és így* all have visible pencil strokes in the expected places. In row 10 the d (tick left, long stroke), the j (base and stem) and the a (two bars, split by the 6) are all there. Row 9 end is the weakest and is correctly disclosed as such.
- Spot checks of literal slips: *talelja* (row 3), *pentakan* (row 12), *elmehtek* (row 14: tall + short, then gamma), *hoz édesem* (row 15), *viszsza* in row 18 are real, as the solver says. Stamp rows confirmed, including the final d of *Ferid* (tick left of the long stroke).
- Picture side: print only, text as stated. Postmark date and the plain address name/town confirmed. Hidden published solution: none indicated; the portal metadata attaches none.
- Family formula search: `grep "bezárom soraim"` over hcp-12xx and hcp-13xx SOLUTION.md gives 19 cards; *bezárom soraim, maradok sírig* gives hcp-1228, 1237, 1249. *bánatos soraimmal* occurs on no card except this one.

## Findings

1. **major: row 20 is *bezarom*, not *banatom*.** Sign by sign (`crops/r20a.jpg`, `crops/r20b.jpg`, `crops/panel.jpg`):
   - sign 2 has three bars (e), not two;
   - sign 3 is the crossed z (left arm to an apex, stem down, long diagonal across its foot). It has the same topology as the z of row 19 and is nothing like n, which is two plain strokes;
   - sign 4 is two bars (a);
   - sign 5 has a stem, a top bar and a faint low arm, so F-like r. The low arm is weak; gamma t is the alternative, but gives no word.
   So row 20 reads b e z a r o m s o r a i m, *bezárom soraim*. The ledger tokens A N A T must become E Z A R. Uncertainty 6 falls away, and its statement that *Ezzel bánatos soraimmal maradok* is "the closing formula of the family's letters" is false: the formula is *Ezzel bezárom soraim*. The solver's reading was forced to sense and three signs were mistranscribed to get it.

2. **major: row 21 is *sirig hű*, not *szretok hű*.** Ledger `S Z R E T O K` must become `S I R I G` (`crops/r21b.jpg`, `crops/panel.jpg`).
   - Sign 9 is i, not z: closed loop at lower left, crossing stroke, dot above. It matches the i of row 17, row 2 and the stamp. No z on this card has a loop.
   - The next sign is r, as read.
   - The heavy blot is a loop at lower left with a crossing bar and an upward stem: an overwritten i. I see no three bars (e), gamma (t) or separate o in it. This one sign rests partly on sense and must be disclosed as such.
   - The 5-shape is g, by the solver's own note that g and k are close in this hand (uncertainty 9). It explains the "k" the solver could not explain in uncertainty 7.
   The inserted [s] and the omitted-e story go away. English: "faithful unto the grave", not "loving and faithful". Slovak likewise. Sign count becomes 419 (row 20 unchanged in length, row 21 two fewer); check the 421 in SOLUTION.md.

3. **minor: row 19 has e, not a.** The sign after *het* has three clear bars (`crops/r19a.jpg`), so literal *hetel*, and no slip. Remove *al → el* from uncertainty 8 and fix the ledger (`H E T E L`). *de ha lehet, elmegyek* stands with no emendation.

4. **minor: normalized text must follow.** It should read, at the end: *de ha lehet, elmegyek. Ezzel bezárom soraim[at], maradok sírig hű kedvese, Feri.* with matching English ("With this I close my lines; I remain, faithful unto the grave, your sweetheart, Feri.") and Slovak. With this, uncertainty 6's alternative about *ezel* is settled: *ezel* opens the new sentence. The "Why it is correct" section cites "isolated points" and the *hű kedvese* close; update it. This agreement with the family formula is now stronger evidence than the one given.

5. **minor: row 7 d of *dolog* is not "a long stroke with a tick".** I find the long stroke, crossed by the cancellation line, with a small round mark to its **right** (`crops/r7a.jpg`, `crops/d.jpg`). On this card the d tick sits on the left; a short mark on the right is the h/p form. No left tick is visible. *dolog* is certainly the word, but uncertainty 3 should say the d rests on sense alone, not on the pencil separation.

6. **minor: row 15 *hozzá[d]*.** Only h o z is written, then *édesem*. The bracket marks d alone though z and á are also not there. The card otherwise uses formal *maga*, so plain *hoz[zá]* is the closer normalization (the sense "to you" is unaffected); if *hozzád* is kept, say that it breaks the register of the rest, although *Ferid* on the stamp is also familiar.

7. **minor: command is not a real decoder.** `work/ledger.txt` is written in plaintext letters, so decode.py applies no key: it lowercases tokens and prints a static `normalized.txt`. It verifies hashes and prints, but "decodes" overstates it. This is why misreadings driven by sense could pass unnoticed. Say so in SOLUTION.md, or add sign-class tokens.

8. **minor: accents.** The ledger marks only one acute, yet marks are visible over the e of *még* at the ends of rows 14 and 15 (`crops/R6.jpg`, `crops/R7.jpg`). "Acute marks are mostly not visible" is overstated. Mark these two.

## What I could not verify

- The address number group under the collector's stamp (*5 sz. II. e. 5 a*): not resolved; tentative, correctly disclosed; no bearing on the message.
- Row 9 *a vona-* and row 4 *lapot*: the strokes fit, but a sign-by-sign check is limited by the postmark; these rest partly on sense, as disclosed.
- Row 20 sign 5 (r against t) and the row 21 blot (i): see findings 1 and 2.
- The h/p and g/k calls remain word-sense decisions, as disclosed. Row 10 *lemondják* against *lemondjak*: no accent visible, disclosed.
- What "our train" refers to; nothing on the card explains it.

## Register note

No entry should be written until findings 1 to 4 are applied. After that the card is a complete reading (the only soft points are single signs), of type MASC.
