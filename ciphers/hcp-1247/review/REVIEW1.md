REVISE

# Review 1 of hcp-1247 (Claude Opus 5.5, reviewer, 2026-11-01)

The solution stands as a reading: Hungarian, Jolánka-family key, 26 rows plus the edge run, coherent throughout. Concrete sign-level fixes are needed in six places, and one clause (row 19) has a reading that the key contradicts. None of them overturns the message. No text in the rows outside row 19 changes in sense.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1247/work/decode.py`: all four SHA-256 checks print OK, and the output matches the literal block and normalized text in SOLUTION.md exactly.
- Key: compared the SOLUTION.md table with `ciphers/hcp-1216/work/graphic-key.json` and the hcp-1216 SOLUTION.md table. It is the family key, unchanged. (Exception on h/p: see finding 6.)
- Own crops from the hi-res address side, with my own shear pass, at 1.65x to 5x: `review/work/crops.py`, `c2.py`, `c3.py`, `c4.py`, output in `review/work/c/`.
- Own sign-by-sign reading of rows 1–26 in my own glyph codes, decoded with my own key table and compared with the solver's ledger: `python3 -I review_decode.py` from `review/work/`. This was not blind, since I had read the solver's text first. Result: 22 of 26 rows are identical sign for sign. Rows 8, 17, 19 and 20 differ (findings 1, 2, 5, 6).
- Right-edge run and under-stamp box checked sign by sign (`edge1.jpg`, `edge2.jpg`, `stamp.jpg`, `bb0/3/4/5.jpg`).
- Language: the text is ordinary period Hungarian with this writer's consistent loss of double consonants. Word repetition holds. Row-break joins and the turn at the corner into the edge run hold.
- Picture side: printed verse and a couple, plain Hungarian print; no cipher and no handwriting there.
- `register-exclusions.json` has no entry for 1247; it is not in `skip.txt`. Portal status and attachments are as SOURCES.md reports (taken from the capture, not re-rendered).

## Findings

1. **major — row 19, *lesz* is contradicted by the key.** The first sign of row 19 is a section mark, the same shape as the k at the start of row 18 directly above (`review/work/c/k1819.jpg`) and the k of *inkább* later in row 19. Under the key the section mark is k; s is the right bowl, which this writer never replaces with a section mark on this card. The ledger's token `S` and the literal *sez* therefore misstate the sign, and SOLUTION note 6 ("k/s-class") blurs it. The literal is *ke[overwritten sign]*, followed by a chevron with an extra foot, so the row joins to *…a le|ke?* and not to *lesz*. The overwritten third sign is a blot of at least two signs; a z-cross over something F-like is possible, so a form of *kerül* ("costs") is worth testing but I do not claim it. Fix: ledger `K E ?`; print this word as uncertain in the literal, normalized, English and Slovak texts; the sense "about 50 K" rests on the digits alone. This is one uncertain word with the rest of the clause reading, so it does not make the card partial.

2. **minor — row 20, a sign was dropped.** The row ends m-a-j and then a short stroke plus long stroke, the d sign (`review/work/c/z20e.jpg`). The writer wrote *majd* in full. The ledger stops at J, and note 13 lists *maj → majd* as a writer's spelling, which is false. Fix: add `D` to row 20 and delete that item.

3. **minor — under stamp B3 is *edesem*, not *edesam*.** The sign before the final m has three bars (`review/work/c/bb3.jpg`), the lowest a short one. The ledger's `A` and note 13's *édesam → édesem* are wrong. The "édesem ×5" claim is true only with this correction: the ledger as it stands has four.

4. **minor — under stamp B4 is more readable than stated.** The "point" and "stroke" are one sign: a tick left of a long stroke, the d form (compare B3, `bb3.jpg` and `bb4.jpg`). The ledger's `.` is not punctuation. The following tailed 2-like sign matches the i of B5 *viszot*, and the last sign is the descending g. So the end of the word reads *-dig* (…*o-d-i-g* if the loop is o), with only the first one or two signs and the exact form of the loop open. I cannot find a word I would stand behind. Fix: ledger `? ? D I G` or similar, drop "could also be something other than letters", report the partial reading.

5. **minor — row 17, second sign is probably three bars.** Bars at the spacing of a three-bar sign show at the top and bottom, with the middle one lost in the rust stain and a purple trace visible (`review/work/c/z17s.jpg`; top-to-bottom span about 31 px native, as for the neighbouring e, against about 19 px for a two-bar a). The literal is then *hetem*, and *tölt|hetem* needs no emendation. Note 8 should say so.

6. **minor — row 8, the "p" of *szép* has the d shape.** It is short stroke left, long stroke right (`review/work/c/z8.jpg`), the form of *de* and *édes*. The card's h and p have the opposite order: long left, short right (*hagytam*, *lapot*, *napig*). On this card the two forms are separated cleanly enough that a reader should be told. *szép* stands on word sense as a slip, but note 5 and the ledger token should say the pixels show d. The key table's "tall stroke + short (h/p/d near-homographs)" also understates this. The family key lists the forms apart.

7. **minor — "the money" is an inference presented in the title.** Nothing in rows 7–12 says money. *szép csomó lehet*, *mennyit küldött* and *összeolvasom* fit a pile of cards or letters she has sent at least as well: time flies, there must be a fair pile, I can't yet say how many, I'll count them up. The 50 K belongs to the ball and is a separate topic. Note 5 admits the inference, but the title states it and "(money, from the following sentence)" is not good evidence. Fix: neutral title; give both senses in the uncertainty list; the English "how much" should be "how much/how many".

8. **minor — undisclosed normalization.** Literal *mondhatnem* is left as *mondhatném*. The standard form is *mondhatnám*. Either normalize it and list it in note 13, or keep it and say why.

9. **minor — small errors in "Why it is correct" and the description.** "Formal *Ön* address": the text uses *maga*, the less formal register. "*mulat-* ×4": three in the ledger (rows 13, 15, 21–22). The ledger header's joined `GY` token: on this card g and y are two separate signs (`review/work/c/z1e.jpg`), which also makes "one token per sign" slightly untrue. Note 11's "fourth short stroke" after the m of *Jolánkám*: I see only three strokes, the third set apart.

10. **minor — plaintext context not reported.** SOLUTION.md gives no account of the plain address side: Tóth Jolánka, Jászárokszállás, with a Rákospalota boxed mark. The Rákospalota mark gives the writer's likely area and is worth noting beside *vasutasné* and *feljön*; the printed verse on the picture side is also unmentioned. Record these for the report without claiming an identification.

## Restorations, judged on the pixels

- *[l]* of *fogla[l]va* (edge): hidden by the stamp; the gap fits one sign. Disclosed; accepted.
- *[Is]ten* (B1): the row visibly starts *t-e-n* at the stamp edge. *Is-* is inference from the formula. Disclosed; accepted as a restoration, not a reading.
- *e* at the start of B3: three blobs are visible at the stamp edge. It is read, not restored, as the ledger has it.
- *viszo[n]tlát[ásra]*: *viszot / lat* is visible (first v partly at the stamp edge) and the rest is under the tape. Disclosed as inference; accepted.
- *mulat[ok]*, *[a]*, *az* for *a*: editorial and disclosed, except as changed by finding 1.

No "completion" or "response to review" sections exist yet; this is the first round and all the work is by one solver.

## What I could not verify

- Whatever lies under the tape and the stamp fragment, including any signature.
- The date: only part of the postmark is legible, and 1913-09-19 comes from the portal file name.
- Whether a published solution exists: I did no independent web search. SOURCES.md and the orchestrator's register check report none.
- My reading was not blind, so agreement in 22 rows shares the solver's expectations. The ambiguous signs are the ones listed above.
- The first signs of B4, and the overwritten sign in row 19.

## Register

Once the fixes are in, this qualifies as a complete reading under the run's rule: the unread items are isolated words, and the end of the note is physically hidden. Type label `MASC`. No published solution was seen.
