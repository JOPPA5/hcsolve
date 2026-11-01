REVISE

# Review 1 of HCP1256 (Feri to Jolánka Tóth), Claude Opus 5.5, 2026-11-01

**Summary.** The solution stands: the HCP1216 key turns the whole card into running Hungarian, and I found no wrong key value. But the ledger has five sign-level errors (two inserted signs, one dropped sign, two misread signs), and one clause is mistranslated. The fixes below are small, and one of them removes a listed uncertainty. They should be made before FINAL. No new review round is needed unless the solver changes more than this.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1256/work/decode_opus.py`: all four hashes OK. The output is identical to the literal block in SOLUTION.md, and the normalized text matches `work/normalized-opus.txt`.
- **Independent decode.** `review/work/my_decode.py` (run from the cipher directory) holds my own sign-by-sign reading in separate shape codes, with the key taken only from the table in `ciphers/hcp-1216/SOLUTION.md`. It diffs that reading against the solver's literal text (`review/work/solver-literal.txt`). Over 33 rows and about 711 letters, 5 rows differ, and these are the differences in findings 2, 3, 4 and 5. This was not blind: I had read the ledger first. The crops were my own.
- **Pixels.** All 25 main rows and 8 stamp rows were read on my own crops of `work/hires/*_adr.jpg` (`review/work/L*.png`, `R*.png`, `T*.png`, `S.png`, 2–2.8x), and every disputed sign on 3.8–5x crops (`z*.png`, `zs*.png`).
- **Key coverage.** Every sign falls in a family class. The only exceptions are the two unsettled signs in S6/S7 and the three stamp-hidden signs in S1.
- **Language and context.** The text is real colloquial Hungarian of the period. Sándor, Feri, the closing formula and the formal address fit the family. István király = 20 August is correct.
- **Solver's flagged calls, confirmed on pixels:**
  - row 8 overwritten v
  - row 15 *voltam* (two bars, with a pink smear)
  - row 16 `beszegett` (a real period follows it)
  - row 18 crossed sign before `nk`
  - row 19 overwritten i of *miért* and final `nem` (the first m stroke joins the tail of the e)
  - row 21 two-lift t of *tudom*
  - row 22 d-shaped p of *fényképet*, and the blot on *héten*
  - S1: the first three signs are hidden, so that restoration is genuinely a restoration
- **Picture side.** Printed verse only, no cipher.
- **Published solutions.** No sign that one was used. The portal attaches none, and the transfer from HCP1216 is credited.

## Findings

1. **Major: row 22 *akár fényképet* is a mistranslation; read *a kér[t] fényképet*.** The signs are a, k, e, r, and the accent tick stands over the e (`T2.png`, around x=590; same tick form over the e of *fény*). The card has *kér*, so *akár* needs an a-for-e emendation against a written é. *Édesem, a kért fényképet jövő héten megküldöm* = "Darling, the photograph you asked for I will send next week" needs only the omitted t (this writer drops letters; see `pézbe`, `viszot`). It also explains the rest of the sentence, whereas "I will even send you a photograph" is forced. Fix the normalized text, the English, the Slovak and uncertainty 11. Disclose that the t is supplied.

2. **Major: row 24 `asor` is misread; the second sign is k, so the word is `akor` = *akkor*.** SOLUTION says "All four signs are clear", and the ledger has `)`. On `z24.png` the sign is the S-shaped k, the same form as the last sign of *hassak* and of *csak* in the same row, not the right bowl seen twice in *-ss-* just before it. *Csak dolgozhassak, akkor majd csak rendbe jövök.* Change the ledger, delete uncertainty 2, and remove the `{a sor / akkor?}` hedge from the normalized text.

3. **Major: two ledger tokens have no pixels behind them, so these are undisclosed restorations.** The ledger states that one token is one written sign, and [x] is reserved for restoration.
   - Row 19 has `O N D T A`, but only two equal strokes stand between o and t (`z19.png`). Compare row 21 *mondtam*, which has both n and the short+long d. The card reads `monta`.
   - S4 has `Z O N T`, but no strokes stand between o and t (`zs4.png`). The card reads `viszot`, as in *viszo[n]tlátásig*.
   Transcribe what is written, put the supplied letters in brackets in the normalization, and list both under uncertainties. The sense is unchanged.

4. **Major: row 21 drops a visible sign.** After z there are two separate three-bar signs, then n (`z21.png`): literal `herszeen`, not `herszen`. That is *Persze én azt mondtam* ("Of course I said..."), not *persze(n)*. Fix the ledger, the normalization, the translations and uncertainty 11.

5. **Minor: S1 last sign is e, not a.** It has three widely spaced bars (`zs1.png`, y about 100/200/295). The literal is `…enve | le`, ordinary *vele*. Delete the claim in uncertainty 4 that `va` is a writer's spelling.

6. **Minor: undisclosed alternative in row 18.** The literal `minderöl` is normalized *mind erről* and translated "this is all we talk about", but *erről* has no antecedent in the letter. *mindenről* with n omitted ("we talk about everything") fits better, and the same writer omits n in `pézbe` and `viszot`. It is a word-sense call either way, so disclose it and say which reading is preferred.

7. **Minor: S5 `latesig` is not secure.** After the t's arm I can see only two bars attached (`zs4.png`), so `latasig`, the ordinary spelling, is at least as likely. Do not assert a writer's spelling here; mark the sign uncertain.

8. **Minor: the justification in uncertainty 7 is overstated.** Row 6 `hast` has two crisp, widely separated bars (`z6.png`), so "not always crisp" does not apply here. *Pest* is an emendation of a clear a, resting on sense. That is acceptable, but it should be stated in those terms.

9. **Minor: address incomplete.** After *úrleánynak* stands the unenciphered word *szeretettel* ("with love"), partly under the collection stamp (`addr.png`). SOLUTION replaces it with an ellipsis. Give it.

10. **Minor: the "one token per written sign" claim is inaccurate for GY.** *gy* is written as two separate signs, the open loop g plus the y sign (rows 2, 4, 7), and *cs* as two opposed bowls. Row 9 shows the y sign alone. "Joined forms" in the key description is misleading for this hand.

11. **Minor: the size of the unread sign-off is not proven.** `?arsoka` + hidden sign + `ész` spans about ten signs across a stamp fragment. "One word" is an assumption, since it may be two. I could not read it either. It is a short gap in the sign-off and the rest reads, so I do not count it as an unread clause. SOLUTION should say "one word or short phrase", and the headline claim should say the same.

## What I could not verify

- The unread sign-off (S6–S7) and the first three signs of S1, which are physically hidden.
- The family name *Fáger*: the signs are clear, and the e carries a tick, so it may be *Fágér*. The person is not identifiable.
- The date: the cancellation was not read by the solver, and I did not read it either.
- Whether the pink overpainting under the g of row 16 hides an l.
- Whether row 24's first sign is a misformed d or a real k slip. It looks like k, and *dolgozhassak* rests on sense, as disclosed.

## Register

Once the fixes are in, this can be treated as a complete reading under the batch rule. The solver should use the existing label `MASC`.
