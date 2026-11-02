REVISE

# HCP1205, review round 1 (Claude Opus 5.5, reviewer, 2026-11-02)

Summary: the card is Hungarian in the Jolánka family key and the bulk of the reading stands. It is not finished, though. Eleven points can be corrected on the pixels, and several of them replace weak or forced readings with ordinary Hungarian (*persze*, *kelméből*, *5-ikén*, *azt hiszem*, *rokonál*, *csak ha nem megyek, haragszanak*). One clause in row 25 stays unread after those corrections. Unless the solver resolves it, the card counts as **partial** under the run rule and gets no register entry.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1205/work/decode.py` runs, all four SHA-256 checks pass, and its 43 rows are byte-identical to the literal block in SOLUTION.md (`review/work/verify.py`).
- **Independent decoder.** `review/work/verify.py` holds a key table typed separately and reproduces all rows. 1241 signs, no token outside the key, index of coincidence 0.0714, which is ordinary for Hungarian. This only shows that the ledger maps as claimed. The ledger itself was tested on the pixels.
- **Own transcription of contested rows.** The same script decodes my sign-class reading of rows 05, 08, 13, 21, 24, 25 and U6-U7. Output: `hiszem`, `megyek5iken`, row 13 ending `ha`, `{p}ersze`, `...felelte hogy`, `aroko`, `kelmebölne`.
- **Pixels.** Crops of `work/hires/` at 2-5x are in `review/work/crops/`. U1-U8 come from the 180-degree rotation (`review/work/c.py r ...`). I read every row at about 2x, sign class by sign class, and read each uncertainty and restoration at 3-5x. Rows 01-19, 22-23, U1-U8 and S1-S8 hold apart from the points below.
- **Orientation and block layout.** Confirmed. The signs past the divider at the end of rows 06-07 are upside-down ends of U1-U2, as NOTES says.
- **Context.** The clear address reads Tek. Holecz Ferencz úrnak, M.Á.V. fékező, Iskola utcza 34, Rákos Palota Ujfalu. *pletyka* is a real Hungarian word, and *vasutasné* and the railwaymen's dances fit a brakeman. The signature Jolánka is in cipher in S8. No published solution was used, as far as I can see.

## Findings

1. **Row 21 `M?ersze` is `persze` (major).** Crop `z20.png`, second row. The first sign is tall + short, the family's h/p sign, followed by three bars, F, s+z, three bars. *p-e-r-sz-e* = **persze**, "of course". The solver forced an unsupported m and built *mer' sze*. The clause is: *Persze a rokonság kíváncsi magára*. Fix ledger, normalization, all translations and Uncertainty 2.

2. **U6-U7 `kel` + `m?ebol` is one word, `kelméből` (major).** Crops `u4.png`, `u3.png`. The word runs over the row end: *simább kel|méből*, "of smoother cloth". There is no *kel[l]*, no extra m and no *ebből*. The clause is: *Csak ne olyan durva sötétkéket, mint legutóbb volt, simább kelméből.* This removes Uncertainty 3 entirely.

3. **Row 08 `Yiken` should be `5-ikén` (major, strong probability).** Crop `z8.png`. The sign has a flat top flag to the right, a belly and a tail to the left: a written digit 5. It is unlike the zigzag of *pletyka* (`z23.png`/`d1.png`). Clear figures inside cipher are normal in this correspondence (HCP1267). *Pestre megyek 5-ikén, ott leszek, de még nem tudok pontos időt írni, hogy mikor megyek* is plain sense: she has a date but no exact time. *[e]gyikén* needs a dropped e and an implied noun. Note the date in the solution. Also normalize `meg nem tudok` to *még nem tudok*, "I cannot yet".

4. **Row 13 final `Y` is not a sign (major).** Crop `z13.png`. The loop at the end of row 13 is the tail of the gy of *úgy* at the end of row 12. The stroke runs without a break from the X-side loop through the S curve down into that loop, the normal form of this hand's gy (compare the end of row 09). Row 13 ends at `ha`. The reading is *Majd ha vasutasné leszek*, with no dropped *egy*.

5. **Row 25 final `Y` is an `o` (major).** Crops `e5.png`, `e4.png`. The last sign has loop plus shoulder, the same form as the o signs in the row. With row 26 this gives `aroko|nal` = *a rokonál* (*rokonnál*), "at the relative's". The bracketed *rokon[ok]nál* falls away, and with it the stated dependence on Y in rows 08, 13 and 25-26.

6. **End of row 24: three signs missed (major).** Crop `e5.png`. After `felelte`, the row turns up into the corner and continues with double slash, loop + hook and gy: `hog` = *hogy*. The ledger stops at `felelte`. The text is *azt felelte, hogy csak jöjjön hozzájok*. The solver has used double slash for h in *hogy* before (row 09), so its own rule covers this. The claimed count of 1241 signs and "the whole card" both need correcting.

7. **Row 27 end is wrongly split and misread (major).** Crops `end27.png`, `e2.png`. The last sign has a left flag, a down-curve and a foot: the k sign, not the wave. The word is `haragszanak`, not `haragszanál`. Word division should be *csak ha nem megyek*, not *csak, hanem megyek*. The clause is: *de ezeknél nem jó kedvemből leszek, csak ha nem megyek, haragszanak*, "but I will not be with them gladly; it is only that if I did not go, they would be angry." The closing direct question *Haragszanál?* in the informal 2nd person, on a card that uses *maga* throughout, is an artifact.

8. **Row 05 `HiszeN` is `hiszem` (minor).** Crop `r5.png`. After three bars stand three strokes, m, not tall + short. With row 4 this reads *az[t] hiszem, harmadrészét én is elküldtem*, "I think I have sent a third of that too". Fix the translations. One of the five N tokens goes, which weakens the claimed "h, p and also n" class.

9. **Rows 21-22 word division changes the sense (major for the translation).** `eshanem ugy` is *és ha nem úgy jelenik meg, mint az ízlésük szerint, mindjárt megvan a pletyka*, "and if you do not appear as is to their taste, straight away there is gossip." The normalized *és hanem úgy* is not Hungarian, and the English and Slovak turn a condition into an instruction. No sign changes.

10. **Rows 25-26 remain partly unread, so completeness is the issue (major).** With findings 5-7 applied, these words still have no construction:
    - Tail of the *mintha* sentence: the first sign of `m?ene` is tall + short, as in row 21, so *menne* rests on sense alone (Uncertainty 1 does not say this).
    - `egYin`: the sign after gy looks like loop + shoulder (o class), not Y + i (`e7.png`). So `egyon/egyön` is at least as good, and neither is settled.
    - `jöne n?ekegdet is`: *ne kegyedet is* is forced. This writer says *maga* everywhere, and *kegyed* occurs nowhere else. Under the solver's own double-slash-as-h rule, `eg//et` is **egy hét**, as in *egy hétig* in row 23; *...nekem(?) egy hét is* should be tested, as should *jönének*.
    - `otahon? en`: the blotted sign is three thick bars with an accent over them (`e8.png`) and does not settle *ő* against *én*.
    The solver asked the reviewer to rule. As it stands, that stretch is a whole un-understood clause, not one isolated word. Under the run rule that makes the card **partial with no register entry**, unless the solver resolves it and can show the reading on the pixels. If it stays open, say so in the status line and in the report; the title claim "whole card read" cannot stand.

11. **Row 20 `aron` does not match the strokes (minor).** Crop `z20c.png`. Between the o and the i of *mivel* I count six strokes (2 + 1 + 3), while `n` + `m` accounts for five. One stroke is unaccounted for and undisclosed. The sign taken as r has only one clear bar, plus the crossing tail of the gy above, so Γ (t) must be considered too. *Áron* is an un-understood word; disclose it as such, with the stroke count. Alone it does not block completeness.

12. **Ledger clean-up (minor).**
    - Row 24: `u?H` claims an h sign that is not separately there. Crop `x24.png` shows one flagged X directly followed by loop + hook and gy. The stroke above it comes from row 23. Record it as one composite sign needed for *hogy*.
    - Rows 23 and U2, and S3 `dog`: *egy*, *vagy* and *boldog* are written with the same tailed glyph or the plain form; the ledger's g/G/Y choices should be stated consistently. Row 27 `gY` is the ordinary gy glyph split into two tokens.
    - Uncertainty 5 must be rewritten: after findings 3-5 the zigzag y is supported by *pletyka* only.
    - S7: *oj nagyon* = *oly nagyon*, no *[an]* needed.

13. **Picture side (minor).** SOLUTION mentions a printed verse but never gives it. It begins "Két sziv ha földobog". It is printed, not cipher. Transcribe it, or state plainly that it is left out, since the completeness rule covers unenciphered parts.

## Proposed text for the solver to verify (not a fix by me)

*Most kaptam meg magától e kétszázadik lapot. Szeretném tudni, hogy én mennyit küldtem magának, azt hiszem, harmadrészét én is elküldtem. ... Pestre megyek 5-ikén, ott leszek, de még nem tudok pontos időt írni, hogy mikor megyek. ... Majd ha vasutasné leszek, ha ugyan leszek ... Persze a rokonság kíváncsi magára, és ha nem úgy jelenik meg, mint az ízlésük szerint, mindjárt megvan a pletyka. ... és azt felelte, hogy csak jöjjön hozzájok, mintha otthonra menne, [unread clause], pedig a rokonnál leszek ... de ezeknél nem jó kedvemből leszek, csak ha nem megyek, haragszanak. ... simább kelméből.*

## What I could not verify

- The digit in row 08 is read as a shape. A y-reading cannot be excluded outright, though the sense and the shape both favour 5.
- The blotted sign in row 26 and the clause in rows 25-26 remain open.
- The sign before `mivel` in row 20 remains open.
- Accents are too loose to check word by word.
- The postmark on the top right gives no usable date. I did not attempt to read the stamp ghost further.
- I did not read the linked HistoCrypt article, so I cannot say whether it prints this card.

## Disclosure and honesty

The solver's uncertainties are candid and rank rows 25-26 first, correctly. Findings 1-7 are, however, cases where a sign was fitted by word sense when a plainer reading was on the card, and the "Why I believe it is correct" section should not claim the three Y-dependent words. After these changes the key still needs no new value, apart from a clear figure.

Register note: no entry until finding 10 is resolved. If it is, the type label is MASC.
