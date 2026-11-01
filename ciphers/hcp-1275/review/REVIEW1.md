REVISE

# Review 1 of HCP1275 (Feri to Jolánka Tóth), Claude Opus 5.5, 2026-11-01

The cipher, the key and most of the reading are right. Two things must change before FINAL: the status has to become partial, because rows 2–4 hold a whole unread clause (finding 1), and rows 20–21 are mistranslated (finding 2).

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1275/work/decode_opus.py` passes all four SHA-256 checks. It prints the rows in SOLUTION.md exactly and reports 721 signs. I recounted the tokens: 721.
- **Independent reading.** I read rows 1–27, the edge and the stamp block from my own 2–6x crops of `work/hires/*_adr.jpg` (`review/work/crop.py`, `red.py`, `review/work/crops/`). The red channel was used for the stamp block. I recorded the reading in my own sign codes (`review/work/my_reading.txt`) and decoded it with `review/work/indep.py`. This is not a blind reading: I saw the ledger first, and read the signs against it.
- **Diff against the ledger.** 718 characters agree, with 6 differing spans:
  - row 3, row 24: signs I also leave open
  - row 10, row 27: real differences (findings 3 and 4)
  - row 23: h versus p, which my code does not separate (finding 6)
  - S6: finding 5
- **Key.** Every value matches `ciphers/hcp-1216/work/graphic-key.json`, except that h/p is one sign class here, which is disclosed. The g sign really is the angular lightning shape on this card. No sign outside the table was needed. The letter distribution fits Hungarian (IC 0.065; e 99, a 80, t 50 of 713 letters). The key covers the whole ciphertext.
- **Layout.** E1 *ogsagat* reads correctly up the right edge (rotated crop `e1.png`). The corner cluster after *minde* is a squeezed g + y. The stamp block is under a lifted stamp, as claimed.
- **Plaintext.** Real period Hungarian with the writer's own spellings. The long passages in "Why it is correct" are all on the pixels. Addressee (Tóth Jolánka, Jászárokszállás, in clear on the address side) and signature fit the family. *sírig hű* recurs on HCP1216.
- **Picture side.** Printed only. The verse there (*Két szív ha földobog…*, the rich may hope while the poor stays alone) matches the card's complaint about the richer rival. The solver does not use this; it is worth a line of context in the report.
- **Sources.** I found no sign of a published solution. The portal attaches none and the solver says so.

## Findings

1. **major: rows 2–4 are a whole unread clause, so the card is partial as it stands.** SOLUTION.md's status line says "whole message deciphered". Its Uncertainties section asks the reviewer to judge whether this makes the card partial. It does.
   - What Jolánka is said to have said, *a nagy kör, hogy nem hallgat a h?ely, kár*, has no established sense. It rests on a blotted sign (`{n}`, row 2, `n1.png`: a smear with a tail, not recognisably n), an unknown word and an unresolved *kör/kor*.
   - The next sentence, *Ez nem lehet oka…*, answers exactly this content, so the argument around it does not supply it.
   - Under the run's rule, a whole unread clause is partial and gets no register entry. The status line and the report must say partial, unless a revision resolves the clause.
   - The three-word count also understates the problem: `alokutja` and `eden` are separate gaps on top of this clause.
   - One lead to test, hypothesis only: *kár* is assumed, and the row 3/4 break may fall inside a word. `h{?l}ely|kar` could be one word, given the writer's constant a/e swaps. In that case *kár* ("a pity") disappears from the translation.

2. **major: rows 20–21 are mis-divided and mistranslated.** The signs read `amit ir nem tudok semit irni`. The first *ir* has a visibly long tick (`s5a.png`), so *ír* is favoured, and *nem* (n, e, m) is clear.
   - The solver joins these into *írnem*, then emends that to *írnom tudok*, and lists it as a spelling normalization. This invents a form the card does not need and gives "what I could write: I can write nothing".
   - The plain division gives: *A vasutasnak a lányáról, amit ír, nem tudok semmit írni, mert nem tudom, miről van szó*. That is: "About the railwayman's daughter whom you write of, I can write nothing, because I do not know what it is about."
   - Fix the normalized text, all three translations and the *irnem tudok* entry in the normalization list. The new reading also shows that Jolánka's letter raised the subject.

3. **minor: row 10 last sign is three bars, not two.** Crop `z10.png` shows three bars after the inverted T, so the signs read *szerencseje*, not `szerencseja`. Normalization is unaffected, but the ledger and the literal row are wrong. The solver's list of a/e swaps should not count it.

4. **minor: row 27 `D O' I' S`.** Both signs after d have the same crossed form and each carries a tick (`z27b.png`). I read i i, giving `viszakildiis` = *visszaküldi is*, with no need for the solver's "extra o dropped". Correct the ledger or justify the o against a dotted i on this card.

5. **minor: undisclosed doubtful sign at S6.** The third sign of `seferi` is blotted and sits at an angle (`rS6.png`). It could pass for a slanted upright cross, but the f value comes from the expected name Feri, not from a clean shape. It is entered in the ledger as plain F. Mark it `{f}` and list it under the sign calls that rest on word sense or context.

6. **minor: ledger header and the p call.** The header says the sign is coded H, but row 23 has a bare P. That is the only p on the card, and it is correct by sense (*fénykép-*), but the token is a word-sense decision. Say so in the header, or use `{p}`.

7. **minor: row 25 *még lesz örökítve*.** `meg` is an ordinary verbal prefix: *meg lesz örökítve*, "it will be immortalized". The translation "will yet be made everlasting" comes from reading *még*. Fix the normalized text and all translations. Also, row 4 *még szeretet volt* is one choice, and *meg szerettél volt* is not excluded by the signs. Note this under the weak passage.

8. **minor: token counting at doubtful places.** The signs below are disclosed, and I agree they are context-based. The sign count of 721 is therefore approximate, and the SOLUTION claim "all 721 signs" should be softened.
   - Row 27 `{t} U:`: the pixels show a single wide arch running into the bottom edge, plus two dots and a faint stroke (`z27.png`). This is not a separate t and ü. *tűzbe* is very likely from context (*teszi vagy visszaküldi*) but is not a sign reading.
   - Row 25 `R {z}`: one overwritten composite (`z25.png`), probably not two signs, and no s is visible for *[sz]ivem*.
   - Row 24 `{g} {t}`: the second sign has a detached falling tick, not the gamma shape.

9. **minor: context.** SOLUTION.md gives no date. The file name says 1913-08-13 and the postmark shows 913. The date should be stated with its evidence. The postmark itself is not fully legible.

## Restorations judged on the pixels

| Place | Judgment |
|---|---|
| Row 2 `{n}` | Blot; *nagy* is context only (finding 1) |
| Row 3 `{?l}` | Wave-like under the postmark; plausible, not certain. *e, l, y* after it are clear |
| Row 12 `{d}` | Faded smear before two clear bars; disclosed |
| Row 13 `boldo ojan` | Faded o-like sign, not g; disclosed correctly |
| Row 22 extra curl over o | Agreed |
| S1 `sir{i?}[g]` | *s r* clear; second sign faded; the sign at the tear is a loop form, compatible with i. g hidden: honest restoration, supported by the formula |
| S2–S5 | Read as claimed |

## What I could not verify

- The sense of `h?ely`, `alokutja` and `eden`. I found no parallel in the finished family texts I searched, and I cannot offer a reading.
- Whether marks at the torn edge below S6 are ink. They look like printed stamp remains, as the solver says.
- Whether the arch in row 27 was once two signs before the card edge cut it.
- The reader's actual identity of Feri or the "railwayman's daughter".
- The family's a/e-swap habit as an explanation for individual words here. It is plausible but cannot be proved word by word.
