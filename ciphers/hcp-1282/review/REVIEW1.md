REVISE

# Review 1 of HCP1282 (reviewer: Claude Opus 5.5, 2026-11-01)

The cipher, the key and most of the reading are confirmed. The card is a genuine Jolánka-family letter from Feri. Three places in the ledger or reading are wrong or better read otherwise, and fixing them removes most of the "not understood" clause. Corrections are concrete, so this is REVISE, not REJECT.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1282/work/decode.py`. All four SHA-256 checks print OK; the 21 literal rows are identical to the block in SOLUTION.md.
- Wrote my own transcription and decoder, `review/work/decode_review.py` (shape codes, own key table, not derived from `work/ledger.txt`); output in `review/work/decode_review.out`. It agrees with the solver on rows 1-4, 6, 11, 13, 15-18, 20. Differences are in rows 7, 8, 9, 10, 12, 14, 19, 21 and are the findings below.
- Read every row on my own crops of `work/hires/*adr.jpg` at 2.4x (`review/work/b1L.png` to `b8.png`), then 3.5-6x at contested spots (`z*.png`, `q*.png`), and channel-separated/high-pass views of the row 18-19 blot (`z19b.png`, `blot_hp.png`).
- Key: unchanged family key from HCP1216 fits all letter signs. Language is real early-20th-century Hungarian with this writer's known habits. Long words (*becsületszavam, változás, masamód, előkelő, epedő szívvel*) come out unforced and are visible sign by sign.
- Context: recipient Tóth Jolánka and sender Feri agree with the family. Ilona also occurs in hcp-1259 and hcp-1265. The address side reads Tóth Jolanka, Jászárokszállás. I found no published solution and no sign that one was used.

## Findings

1. **major: row 9/10 `varrone|be` is misread; the signs give `varroda|be`, *varrodába*.** See `review/work/q9.png`. The sign after the o is not a lone heavy n: it is a short thick stroke plus a long stroke, the same d-class shape as in *adom* (row 18, `z19m.png`). The upper part of the long line is the right leg of row 8's v running into it, which is what the solver took for a stain. The last sign shows two bars only, with ink drips and the ruled line through it, so it is a, not e. Result: *egy előkelő varrodába*, "to a distinguished dressmaking workshop". This also removes the unexplained *-be* on a person. d rests on the sign class and on sense (d/h/p near-homographs); a third bar under the drips is not visible. Update ledger, literal, normalized text, all translations, uncertainty 2, and the "Why it is correct" word list (*varrónő*).

2. **major: row 14 ledger contains a phantom K; the sign is a short stroke.** See `review/work/z14.png`. Row 14 ends `x | nn | S | short stroke | e | nn`: only one k sign after *vagyun*. The ledger has `X N K K E N`. So the text is `vagyunk / én`, and the invented "[S] én" (uncertainty 5) must go. The same short stroke, unrecorded, stands before the capital in row 7 (`z7.png`, under the gamma) and row 10 (`z10.png`, after `be`). All three fall at sentence breaks, so it is most likely a sentence divider. The claim "no sign left without a value" is therefore not accurate: record these three strokes in the ledger as a punctuation token. The blob in row 12 between `titka` and `a` is probably a full stop as well and is unrecorded.

3. **major: rows 19-20 `is van vele` should be reconsidered as *Isten vele*; the solver's reasons against it do not hold.** See `review/work/z19a.png`, `z19b.png`, `blot_hp.png`.
   - The visible stem leaves the blot slanting down and to the left, as the gamma t stems do. Every visible v in this hand has its right leg going down and to the right or vertical (rows 1, 18, 21). The stem therefore fits t, not "the right leg of v".
   - Two bars show below the blot, about 25 px apart. The three-bar e here has gaps up to about 29 px (`z14.png`), and a top bar would fall inside the blot. "The two-bar sign points to *van*" is thus not evidence.
   - NOTES says channel separation "shows no ink under it". That shows nothing: known strokes also vanish inside the blot, namely the stem itself, the top of the row 19 s, and the lower part of the row 18 s, which the solver restores anyway. The blot hides ink in all channels.
   - *Isten vele* is the standard closing of this correspondence (hcp-1216, 1259 and others), and it ends the sentence just where the writer leaves a visible gap before *édesem* in row 20. *bennem is van vele* gives no sense.
   Proposed: `is[te]n vele`, marked as a restoration of hidden signs: i, s, t (stem only), e (two of three bars), n. This is probable, not proven. Report it as the preferred reading with *is van* as the rejected alternative.

4. **major: the remaining uncertainty must be restated.** With finding 3 the sentence becomes *Becsületszavam adom írásban is, hogy nem {r} bennem. Isten vele.* The F-like sign is clear (`z19m.png`), `bennem` is clear. The clause lacks a verb; the expected sense ("that [you will] not [be disappointed] in me") is a guess only and must stay labelled as one. Under the orchestrator's rule this is a single un-understood word or omission, not a whole unread clause, so the card may count as complete if the rest stands. Rewrite uncertainty 1, translations and the English/Slovak bracket.

5. **minor: *vár|i* (rows 8-9) is glossed by invention.** The signs are secure. "she sews [is placed]" and the Slovak equivalent have no support: *vari* as a form of *varr* is a guess, and this word now stands in front of *egy előkelő varrodába*. Say plainly that *vári* is not understood. One alternative is the adjective/place form *vári* ("of the Vár" district), also unproven. Do not translate it as a verb without brackets.

6. **minor: diacritics in row 8.** The second o of `eloszor` has two dots (`b3R.png`) and the first a tick mark, so the literal should be *először*. The ledger's plain O is wrong for both.

7. **minor: the capital in rows 7 and 10.** The sign is called an unenciphered cursive capital I. In shape it is close to the family y sign (compare the y in row 1 and in gy, `z7.png`). So it may be a key sign used for capital I rather than clear text. Ilona and Irma stand either way; the claim that it is unenciphered needs softening.

8. **minor: row 15 `z`.** The heavy sign (`q15.png`) is a forked stroke, not a clean crossed diagonal. *[e]zintúl* needs two emendations. *szintúl* ("likewise") is a possible alternative. Disclose it next to uncertainty 5.

9. **minor: English of the close.** "you for whom I long with a yearning heart" has the wrong subject: *aki Önre epedő szívvel gondol* is the writer, "[me,] who thinks of you with a yearning heart". The Slovak has it right. Also *Ami minket illet* is the normal spelling of "A mi minket illet".

10. **minor: stamp box.** *csókolom számtalanszor* and *Feri* are clear; *hű* is good. The rest is not secure, and the solver's note is inconsistent: *sze[r]elmese* claims a missing r while "sze-/relmes/e" contains one. Line 6 (`work/crops/stamp_red.png`) shows two letters before Feri, with an ascender, not a lone e. Line 5 begins with a letter closer to m/n than r. State the reading of lines 4-6 as tentative; *kedvese* (hcp-1216) does not fit better on my view but cannot be excluded.

## Confirmed as disclosed

Row 13 *máskülöm-ben*; crosses as j in rows 5 and 20 (sense-based; the row 20 one may be a sloppy inverted T); row 18 final s from its top hook only; row 21 heavy signs in *néha* and *aki* (sense-based); the blob after *önre* is no letter; the sign before it has three bars, so e is right (`q21.png`); row 10 extra arc under *masamód*'s a.

## Could not verify

- What lies under the row 18-19 blot; finding 3 is an inference from what surrounds it.
- The year of the postmark (day/month "ÁPR 11" is legible on the postmark; the year is not).
- Whether the stroke of findings 2 is meant as punctuation; only its position suggests so.
- The identity of Ilona and Irma, and any printed or portal solution beyond what the capture shows; I did not re-open the portal.
