REVISE

# Review 1 of HCP1244 (Feri / Holes Ferenc to Jolánka Tóth, Easter 1912)

Reviewer: Claude Opus 5.5, 2026-11-01. Round 1. The solution (DONE1) is by another Claude Opus 5.5 session, not by this reviewer.

Summary: the key, the row text and the sense of the card stand, and I could not refute the decipherment. One sign is mis-transcribed or at least undisclosed: the last sign of row 14 is not a plain t. That sign changes the clause *Adós sohsem maradt* and removes the problem the solver flagged in item 10. It needs a fix before FINAL. The other findings are minor.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1244/work/decode_opus.py` ran. All four SHA-256 hashes report OK. The 18 printed rows equal the block in SOLUTION.md, and the normalized text equals `work/normalized-opus.txt`.
2. **Independent decode.** `review/work/verify.py` holds my own sign-by-sign reading of all 18 rows, made from my crops (`review/work/crops/t0L…t5R.png`, 2x from `work/hires/*_adr.jpg`), in a private sign alphabet with the table re-keyed from HCP1216's SOLUTION.md. Result, accents aside: 18 rows, 281 signs, 0 letter differences from the solver. This was not a blind read, since I had seen the solver's text first. Finding 1 is a difference on the same sign that the letter comparison hides, because I kept the solver's t in the script so the diff would show everything else.
3. **Key.** The key is the HCP1216 table unchanged. Every ledger token is in it. There is no f, and c occurs only inside cs. The table is consistent: no sign has two values except the disclosed h/p.
4. **Pixels, every row at 2x.** I also zoomed 4–5x on row 14 end, row 17 end, the row 15 blot and h, row 11 *vela* (green channel too), row 6 *anym*, and row 14 *soh-*. Line A1 *szeretettel* reads sign by sign: s, z, e (three small bars), r, e, t, e, t, t, e, l.
5. **Restorations checked against pixels:**
   - Row 15 [s]: the blot does keep the top-left hook and bottom-left foot of the right bowl, with a slit. Accepted as disclosed.
   - Row 9 blotted t: the dark diagonal plus the top bar running right is consistent with gamma. Accepted as disclosed.
   - Row 10 h: thick stroke plus tick. Accepted.
   - Row 4 end: this l is a wave with a rounded start and a deep trough, not a chevron. *alo|mason* accepted.
   - Row 6 *anym*: two strokes plus a low wedge. m is the only sign that gives a word. Accepted as disclosed.
   - Row 6 end: third stroke curved. Accepted as disclosed.
   - Row 13: a doubled pale diagonal on z. Accepted as disclosed.
6. **Language and context.** The Hungarian is real period colloquial language. *Tudatom, hogy szerencsésen megérkeztünk* is the family's formula (HCP1278, 1243). *Csókolom a távolból* in the stamp box is confirmed on HCP1278. Gyöngyös(püspöki) and a workshop are confirmed on HCP1271. *Holes* is confirmed on HCP1268 and HCP1309.
7. **Date.** Easter 1912 computes to 7 April. Rotated 180° (`crops/pm180.png`), the postmark shows `91… 4Pn 1?`, which I read as `(1)91(?) APR 1(0 or 6)`. The month is April, which supports the portal's file date. The year's last digit is not legible and the day digit is 0 or 6.
8. **Picture side.** Printed verse headed *Szerenád. Ábránd.*, number 2317, no cipher.
9. **Sources.** The portal shows Not solved and SOURCES.md records no attached solution. I found no sign of an unacknowledged published solution.

## Findings

1. **major: row 14, last sign is not a plain gamma; *maradt* may be *maradj*.** See `review/work/crops/r14end.png`, next to the d+j ligature in `r17end.png`.
   - After a (`=`) and r the group is short stroke, long stroke, third stem. A **horizontal base bar runs from the long stroke through the foot of the third stem and past it**, with the stem standing near its middle. This is the same construction as the row 17 d+j ligature, where the solver reads inverted T = j.
   - The stem also has a bar going right at its top, into a pink wet smear. So the sign has both the gamma's top and the inverted T's base. The base bar has a darker core, which suggests a second pass of the pen.
   - None of the other t signs on the card has a base bar. The ledger gives `4 7`, and SOLUTION.md does not mention it. Its "Why it is correct" says the only non-key matter is the row 17 ligature and that no sign is left over. That is not true of this sign.
   - For j: *Adós sohsem maradj, a csók soha sem árt. Ha csókot kap, babám, csak add vissza mindjárt.* ("Never stay in debt, a kiss never harms…"). This gives the clause a subject (you), matches the informal imperative *add vissza*, and removes the problem of item 10. The tick after the sign (finding 2) then works as a comma. Note *sohase(m)* with an imperative is colloquial.
   - For t: the gamma top is there, and *maradt* rhymes with *árt / mindjárt*, which *maradj* does not. A correction in either direction is possible.
   - Required: re-examine the sign, add the base bar to the ledger (for example a token for a t/j overwrite), state both readings in SOLUTION.md with this evidence, and revise item 10, the normalization, the English and the Slovak according to the choice. Also consider the division *Adós sohsem maradt/j a csók*, where *csók* is the subject of a t reading. The bare statement "no stated subject" should go. Update "Why it is correct".

2. **minor: marks in rows 14 and 15 left out of the ledger.** Row 14 has a tick after the last sign. Row 15 has a clear round dot after final t (`r14end.png`, t5R), and the dot looks like a period. Row 14 *soh-* has a short high arc between h and s (`r14h.png`), not in the ledger, which may be an apostrophe (*soh'sem*). These bear on the punctuation chosen in the normalization, which puts a full stop after *maradt*; the tick suggests a comma. Disclose them. Item 16 covers accents only.

3. **minor: row 11 *vela*.** The green channel (`r11vela_g.png`) shows two firm bars and no third, so the literal sign is a, not a pale or doubtful e. The family's usual close is *Isten vele, a viszontlátásra* (HCP1216 and others). The better normalization keeps the letter that is on the card: *Isten vel[e] a viszontlátásra*, with the e dropped, rather than turning a into e and losing the article. At the least, give it as an alternative in item 8.

4. **minor: row 8 normalization *úrlányaitól*.** It should be *mester úr lányaitól* (two words). The translation is already right.

5. **minor: translation details.**
   - *kiöntözte-e már magát* is literally "has he/someone sprinkled you yet", with a singular subject. "Have you been sprinkled" hides that. Note it.
   - The switch from formal *kap* to informal *add* in the last sentence is not disclosed. *Ha csókot kap babám* can also be third person ("if my baby gets a kiss"). The Slovak *dostaneš* flattens this.
   - Add a line, and keep it with the decision on finding 1.

6. **minor: item descriptions.**
   - Item 5 calls the third bar of the second e a "low pale tick"; it is a firm wedge (`crops/r7e.png`). The reading is unaffected.
   - Row 15 h is heavily inked and blobbed, undisclosed. The reading is unaffected.
   - Item 12 can be improved: the postmark month is APR, not "4" (see check 7).

7. **Stamp box: no objection.** I agree one word stays unread (e-|…|-tel). Lines 4–5 look like `n/m-e-l-e-t` + `tel`, and I have no reading to offer either. *a t[áv]ol* is a restoration, as stated, and the tear does take those letters. *Feri* and *Ferencz* are as disclosed. This note is plain, not cipher, and one word alone does not make the card partial.

## What I could not verify

- Whether the top bar of the row 14 sign is pen stroke or smear edge: the wet blot sits on it. The original card would settle it.
- The full ring text and year digit of the postmarks, and the stamp-box word (e-…-tel).
- My transcription was not blind, so it is weak evidence for the ordinary rows, though I found no difference there. The text's coherence is the stronger evidence.

## Verdict rationale

REVISE: the decipherment stands, and a fix is needed for one mis-recorded sign with its effect on one clause, plus small disclosures. After the fix the card is complete and may take a register entry, if the solver reports both row 14 readings and picks one.
