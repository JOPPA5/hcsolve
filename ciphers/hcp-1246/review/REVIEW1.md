REVISE

# Review 1 of HCP1246 (Jolánka family, Feri to Tóth Jolánka, 1913)

Reviewer: Claude Opus 5.5, 2026-11-01. Own files are in `review/work/`.

**Summary.** The cipher type, the key and the reading stand. The one group the solver left unread is solvable: it is the set phrase *avatatla[n] kéz*, so the card can be complete. Two more signs are misread in the ledger, and one word of plaintext (*előtte*) was dropped from the normalized text and all translations. No finding overturns the decipherment.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1246/work/decode.py` ran. All 4 SHA-256 checks are OK. Every printed main row appears verbatim in the SOLUTION.md literal block (`review/work/check2.py`).
- **Key and coverage (`review/work/indep.py`).** The ledger has 36 rows and 778 signs. All 22 sign classes are in the family key (`hcp-1216/work/graphic-key.json`), with nothing left over. The same script diffs the ledger letters against the normalized text, which is how finding 2 surfaced.
- **Claimed repeats.** hogy ×9, édesem ×4, nem ×7, ijesmit ×2, mert tudom ×2 are all confirmed.
- **Pixels.** I read all main rows on 2.2× contrast-enhanced crops of the hi-res address side (`b0..b5 L/R`), plus the stamp box (`stamp.jpg`) and the rotated right edge (`edge.jpg`).
  - Checked sign by sign: rows 1-4, 12-15 and 25-28, and the stamp box. The rest was checked less closely against the ledger.
  - Zoomed at 4×: rows 12, 20, 23, 25, 27, 28 (`z*.jpg`, `r28*.jpg`).
  - Apart from findings 1, 3 and 4, the ledger agrees with what I see, including the blotted m in row 8.
- **Restorations.** Row 17 *f[o]g*: the sign is entirely under the blot, and *foglalkozni* is the only sensible word. It is properly marked. The blotted first sign of row 20 keeps its dot and crossed shape, so i is fine.
- **Context.** The clear address reads "Nagysága Tóth Jolánka úrleánynak, Jász Árokszállás", postmark 913 SEP. Language, formulas and the signature Feri fit the family. The portal has no solution, and I saw no sign of a published one being used.

## Findings

1. **major: row 28 `a vetatlakez` is *avatatla[n] kéz*.** The clause reads *még egy lapját sem olvasta avatatla[n] kéz, csak én*: "not one of your cards has been read by an uninitiated (unauthorized) hand, only by me". *Avatatlan kéz* is a standard Hungarian phrase, and it fits a writer boasting that his cipher cards stay private.
   - Crops `r28a-c.jpg` show: t a | a v [cut sign] t a t l a k é z.
   - The cut sign is the one the solver already says "could be two bars (a)". Two strokes are visible and the card edge cuts below them, so a is possible. Only a reading from the phrase settles it, and that should be disclosed.
   - After the final a of *avatatla* comes the section mark k, then three bars with a visible accent tick over them, so the *é* of *kéz* is written. The solver's alternative split `-k ez` should go.
   - The n of *avatatlan* is **not on the card**: section mark k follows a directly. It must be marked as an omission, `avatatla[n]`, in line with the writer's other dropped letters.
   - The article "a" and the "by the [unread word]" wording in all translations go away. Item 1 of Uncertainties and the status line must be rewritten. With this the card is complete.

2. **major: *előtte* dropped from the plaintext (row 14).** The ledger and the pixels both give `viselkedjen elötte es` (`L O: T T E` is clear; signs seen in `b3L.jpg`). `normalized.txt`, the Hungarian text and the English and Slovak translations all omit it. `indep.py` shows it as the only multi-letter deletion: `delete 'lkedjene' [lottee]`. It should read *egész hidegen viselkedjen előtte* ("behave quite coolly in front of her"). It is not disclosed anywhere. It also supports the reading that the "she" who then gives up is Mrs Mocsár.

3. **major: row 27 sign misread: `mondanim` is `mondanom`.** On `z27.jpg` the sign after d-a-n is the undotted cursive loop O (top-left curl, closed lower loop). It is not the crossed curve I, which is dotted on this card (compare `z12.jpg`). The reading is `mondanom magának`, with both m groups belonging to real words. So Uncertainty 8's "superfluous three-stroke m, a false start" is an artifact of the misread, and normalizing to *mondani* is wrong. Correct the ledger token and read *azt ne[m] kell mondanom magának*. *nekel* should be shown as *ne[m] kell*, an omitted m; the current *ne kell* is not good Hungarian for this sense.

4. **minor: row 12 sign misread: `tenacsolom` is `tanacsolom`.** `z12.jpg` shows only two bars after the second gamma (`ijesmit t a n a c s o`); the top bar sits close under the gamma's arm but there is no third stroke. Correct the ledger token from E to A and drop *tenacsolom* from the list of writer's spellings. Findings 3 and 4 are both signs listed as writer errors that turned out to be ledger errors, so the solver should re-read the remaining signs in that list.

5. **major: row 23 `jöm` normalized to *jöjjek* without brackets.** Nothing on the card gives -jjek; the normalized text replaces letters silently, and the English rests on that.
   - On `z23.jpg` the strokes after jö are two very heavily over-inked strokes and one light one, and the following E is over-inked too, so this spot was reworked and the stroke count is less firm than Uncertainty 3 says.
   - *Írja meg, mikor jön* ("Write when you are coming") is at least as natural, since she is the one coming up to Pest; the solver does not list it.
   - Mark the word as uncertain, keep the literal in the normalized text or bracket it, and give both senses in the translations.

6. **minor: undisclosed or inexact normalization.** These come from the `indep.py` diff.
   - *felkeressem*: the card has one s (`felke-re|sem`), and indicative *felkeresem* needs no added letter. Use it.
   - Stamp box `hükedves|seferi` has a doubled s across rows (*kedvese*), which is not listed in Uncertainty 8.
   - *Mocsárnénak* is written `mocsarnenek`, also not listed.

7. **minor: Slovak.** *do šťastného zhľadania* is not idiomatic Slovak; use *do šťastného zvidenia* or similar. *Guľáša* wrongly inflects a surname as the common word; keep *Gulyása* / *na Gulyása*.

8. **minor: row 25 *állású r[u]hát* stays an interpretation.** I see a l a s u r h a t, as the ledger has it. It needs an omitted u (or metathesis of *ur* for *ru*), and *jobb állású* for a garment is not confirmed by any sister card. It is properly disclosed and I have no better reading. Keep the caveat, and do not present "better-fitting suit" more firmly than that.

## Could not verify

- Whether the cut sign in row 28 had a third stroke (off the card).
- The original stroke count at row 23 under the over-inking.
- The *állású ruhát* sense; no period dictionary was consulted.
- The accent on the sign in row 20 (*ígérnem*): a tick is visible and *ígérnem* fits, but the call rests on word sense.
- Rows 5-11, 16-19 and 21-22 were compared with the ledger at 2.2×, not zoomed at 4×.

## After the fixes

The solver should correct the ledger (rows 12, 27), decide row 28, update `normalized.txt` and all translations, and answer each finding. Since the fixes settle details rather than change the solution, `FINAL` after addressing them is reasonable. A complete-card register entry is justified once finding 1 is adopted.
