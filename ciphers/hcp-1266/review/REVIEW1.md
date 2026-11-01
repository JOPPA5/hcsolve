REVISE

# Review 1 of HCP1266 (Claude Opus 5.5, reviewer, 2026-11-01)

The decipherment stands: the key, the transcription and the literal rows are correct. The normalized Hungarian and both translations need fixing: they contain one word that is not on the card, ignore a visible accent, and very probably join a sentence wrongly. All three are concrete edits, and the card's meaning changes only slightly.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1266/work/decode.py` ran. All four hashes are OK, and the printed rows equal the literal text in SOLUTION.md.
- **Independent decode.** `review/work/my_decode.py` holds my own glyph-name transcription, written from my crops (`review/work/crop.py`, `crop2.py`, `review/work/crops/`) of the hires address scan and decoded with my own table. I read all 27 rows, 21 main and 6 in the stamp box, not a sample. This is 330 signs of 28 types. **All 27 rows match work/ledger.txt, 0 differing.** I had seen the solver's text first, so this is a sighted check, not a blind one.
- **Key coverage.** Every sign has a value except the single overwritten sign in row 21. The key is consistent at every occurrence I checked.
- **Each disclosed sign call, on enlarged crops:**
  - Rows 7, 8 *kapom, piros*: both signs really are short-left + long, the d form. Compare the tall + right-tick p in *holnap* and *palota*. Correctly disclosed.
  - Row 17 *de*: really the tall + right-tick form. Correctly disclosed. The stated parallel in HCP1216 row 5 is real (its item 3).
  - Row 20: three b's confirmed (kozelebb + bovebben).
  - Row 21: the sign is as described, and the final three strokes under the portal stamp are m.
  - Stamp box S2–S4: *jon né / ha rám / min én* confirmed, with acutes visible on né and én.
- **Printed picture-side text and clear address:** agree with the solver's account. The address reading is plausible.
- **Language and context.** The Hungarian is real and natural, and *fékező*, *orvosi vizit*, Rákospalota and the railway theme are coherent. No published solution was found or used; the portal attaches none.

## Findings

1. **major: a word not on the card ("ma") is in the normalized text and in both translations.** Row 19 is literally `m e g i r n i m a j d l e g`, which has only one *ma*, the start of *majd*. The solver prints *megírni ma, majd legközelebb* and translates "today" (English) and "dnes" (Slovak). This *ma* is not marked with [ ] and is not a disclosed supply. Evidence: `review/work/crops/z19.png` and `z18.png`. Fix: *megírni, majd legközelebb bővebben*; drop "today"/"dnes".

2. **major: row 18 begins *még*, not *meg*.** A clear acute stroke stands directly above the first e of row 18 (`review/work/crops/z18.png`, top left). The writer marks such acutes elsewhere on this card (*dé-*, *hé-*, row 15 *még*, row 16 *hét*, *né*, *én*). The correct text is *a címet még nem tudom megírni*, "I cannot yet give the address", which fits a move still to happen. Change the Hungarian, English and Slovak. The "Why it is correct" bullet lists *megnem* as a repeat of *meg*; that example should go.

3. **major (sense): sentence division at row 12/13.** Literal `utazokisevel / megkezdemazuj` is split by the solver as *utazok is evvel. Megkezdem az új jövőt*, giving the strained "travelling with it", referred back to the exam. The natural reading is *és már csütörtökön utazok is. Evvel megkezdem az új jövőt, édesem*: "and on Thursday I am already leaving. With this I begin the new future, my sweet." The signs do not change, and uncertainty item 10 should be rewritten. If the solver keeps its division, it must say why and give this one as the alternative.

4. **minor: the row 21 normalization hides supplied letters.** Literal is `ve{?}desem`. *vele{?}, édesem* prints l, e and é as if written, whereas at most one sign stands between *ve* and *desem*. Write something like *Isten ve<le>, <é>desem*, with the {?} sign in place, and say that *vele* is an inference. A dot stands above this sign and it has a stem and bars, so it may be a correction of another sign; item 5 mentions the dot, which is enough.

5. **minor: *vo[l]tam* is probably not an error.** *vótam* is an ordinary colloquial or dialect form of *voltam*. Note this rather than listing it only as an omission.

6. **minor: *czimet* is normalized to *címet* without comment.** The *cz* is an old spelling. It should be listed among the writer's spellings in item 9, and it gives weak support for a date before the spelling reform. Do not treat it as a date.

7. **minor: "the second cancellation is not readable" is slightly too strong.** Fragments are visible at the top edge, including a rotated numeral (6 or 9) (`review/work/crops/zpm.png`). I could not read a date from them either, so "not legible as a date" is the fair wording.

8. **minor: the wording "taken unchanged" oversells the key transfer.** HCP1216 lists joined gy and cs signs and describes g differently, while this card writes g+y and c+s as separate signs. The solver mentions this under the table, but "unchanged" should be softened to "same letter values; writing of digraphs differs".

## Register

After findings 1–3 are fixed, the card meets the completeness rule: every clause reads, and the open points are single signs (row 15 marks, row 21 sign). Type `MASC` fits. No entry may be written until the response is done.

## Could not verify

- Row 15 *még i[tt] lakom*: the pale wave and the dot-and-dash after the i (`review/work/crops/z15.png`) are as the solver describes. I cannot explain them either, and the *tt* remains an emendation. The sense "still live here" fits the next clause.
- Row 21: the identity of the overwritten sign.
- The date of the card, and the first purple line. The second purple line looks like *Ferencz*.
- That the sender is the Feri of HCP1216: the hands were not compared, and the solver says so.
- *piros zászló* as a railwayman's signal flag, as period railway practice: plausible, not checked against a source.
- Acute accents throughout were not exhaustively logged. Finding 2 shows they can matter, so the solver should recheck the remaining *meg/még* cases. Rows 13 and 19 show no accent in my crops.
