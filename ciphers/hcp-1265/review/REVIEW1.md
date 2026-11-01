REVISE

# Review 1 of HCP1265 (reviewer: Claude Opus 5.5, 2026-11-01)

The cipher, the key and nearly all of the reading are confirmed. One word group is misread: the end of row 25 reads *Ilonának vigye le*, not *Ilona ne [i]s vigye le*. Two signs are wrong in the ledger, and the Hungarian, both translations and uncertainty item 2 follow them. Fix these and the card stands.

## What I verified and how

- Command: `python3 -I ciphers/hcp-1265/work/decode.py` runs. All four SHA-256 checks print OK. The output matches the literal block and normalized text in SOLUTION.md, 597 signs in 34 rows.
- Key: the table in SOLUTION.md agrees with the HCP1216 table. No sign outside the key occurs on the card, apart from the writer's deletion in S2.
- Own transcription and decode: `review/work/my_decode.py` holds my own row reading in a separate glyph alphabet (made while viewing the crops, with the solver's ledger open, so it is a check rather than a blind second reading). 596 signs plus the deletion. 31 of 34 rows agree exactly. The differences are row 25 (finding 1), row 20 (finding 2) and row 21 (the sign the solver also marks as unsure, item 4).
- Pixels: I cropped the whole of work/hires/..._adr.jpg at 2.5-6x (`review/work/crop.py`, crops in `review/work/crops/`): rows 1-26, the stamp box, and every restoration in items 1-11. Where the portal stamp lies over rows 23-26 I made a red-minus-green map that removes the stamp (`review/work/inkmap.py`, crops I23, I24, I25, I25a, I26).
- Under the stamp, rows 23, 24 and 26 are correct as transcribed (*Jolánkám*, *nehogy meg*, *intézkednek*). Only row 25 differs.
- Disclosed restorations I accept as honest calls: row 6 *nyéron*, row 7 ring-headed k, row 10 n by sense, row 12 retraced e, row 16 *ezt*, row 21 t by sense, rows 24 and 26 blotted d, and the stamp box S1, S3, S4, S5, S6, S8. Each is a real sign, and each is flagged where the shape is off.
- S2 tail: the deletion is opaque; nothing can be read. *Le* before it does complete *Isten vele*.
- Plaintext: genuine Hungarian of the period with this writer's known habits. Words run across row breaks without forcing. The content fits the family (Feri, Jolánka, Ilonka, Berény, Haraszti).
- Sources: portal status Not solved as recorded in source/metadata.md. No sign of an undisclosed published solution. Picture side checked: printed verse, no cipher.
- Citations checked: *Harasztin* on HCP1305, opening formula on HCP1305, Jászberény on HCP1272, *kedéjes* on HCP1212, cousin Ilonka on HCP1272: all present. For HCP1263, see finding 3.
- Counts: *hogy* ×11, *Jolánkám* ×2, *Árokszállás* ×2, *levegő* ×2, *nem* ×3: confirmed by script.

## Findings

1. **Major. Row 25 end is `ilonanakvigye`, not `ilonanesvigye`; the clause is mistranslated.** In the ledger the signs after `I L O N A N` are `E )`. In the ink map (review/work/crops/I25.png; colour version Z25.png) the portal stamp's letters *OF* are gone and the two signs are plain:
   - The sign read as e has **two bars only**, and no third bar can be hidden: the gap above and below is clean paper in the ink map. It is a.
   - The sign read as `)` is a **full section mark S**, with a top arm running right and a foot hooking left, the same as the k of row 26 end in I26.png. The right bowl has neither stroke. It is k.
   So the row gives `i l o n a n a k v i g y e | l e`, with a tick over the first a of the ending: **Ilonának vigye le**, "let [her/you] take [it] down to Ilona". This is the same -nak form as `ilonkanak` in row 5. It removes the supplied [i] and the forced *ne [i]s*, and it needs no restoration at all.
   Fix: change row 25 of ledger.txt to `... N A N A K V I G Y E`; update the literal block, normalized.txt, the Hungarian, English and Slovak; rewrite item 2, which states "Signs read" and offers a third bar on the wrong sign. The negative "let Ilona not even take" must go. The object of *vigye* is unstated and may relate to the open word *kedel*, so the clause should be reconsidered as a whole; NOTES should record the correction.

2. **Minor. Row 20 sign is not a d as ledgered, so *Ide* is weaker than stated.** In Z20.png the sign after *i* is heavily retraced: a long stroke with a blotted head, then a clearly shorter stroke to its right. The d of this card is the reverse, short first and long second (row 25 `kedel`, row 9 `kedek`). The shape is closer to the h/p class (or a retraced n), and it may be a correction over another sign. The three bars after it are correct. Item 3 should say the sign class itself is unsure, giving *Ide / Ipe / Ihe / Ine* as candidates and that a person's name is inferred only from *ő mondta*. The ledger's D# note, "d with a blotted or doubled long stroke", and item 10's "short tick still visible" do not hold for this sign. The [Ida?] suggestion can stay as a suggestion.

3. **Minor. Two citations to HCP1263 are wrong.** "Why it is correct" says the opening formula is the same on HCP1263 and 1305, and that *Bár igaz, hogy* occurs on HCP1263. HCP1263/SOLUTION.md contains neither *kedvében* nor *igaz*. The formula is on HCP1305; *Bár igaz* is on HCP1283 and HCP1288. Correct the references.

4. **Minor. Some blots are not disclosed, and one restoration is not marked in the translations.**
   - Row 12: the u of *hagyjuk* is a heavily retraced cross (Z12a.png). Only *-juk* fits, but it is written as a plain X in the ledger and is absent from the uncertainty list.
   - Row 23: the a of *Jolánkám* has a blot on its lower bar (I23.png). The two bars still show, so this is a note only.
   - The translations give "God's ordinance" unmarked, though *re[nde]lése* needs three supplied letters. Bracket it, or say in item 6 that the sense rests on the restoration.

## Could not verify

- *kedel* (row 25). The signs are confirmed exactly as the solver gives them: k, e with tick, d, e, l. I have no better reading, and the guess *kedély* remains unsupported, as the solver says. It stands alone in its clause, and the rest of the clause reads, so it does not make the card partial.
- The identity of the person in row 20, and what is to be taken to Ilona.
- The postmark date: nothing beyond a large 17 is legible to me either.
- The ticks over e and a as accents: too sparse to test systematically; they do not change a word.

## Recommendation

After fixing finding 1 and the minor findings, the card can go to FINAL as complete: the changed reading is a direct correction of two signs and needs no new round unless the clause is reinterpreted beyond that.
