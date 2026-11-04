# HCP1233 — Feri to Jolánka Tóth: first exam passed, sleepless and going to bed

**Status: complete reading with disclosed sense calls and one restored word (*hál'*, no l written); reviewed twice, findings of review 2 addressed.** Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. The portal shows status Not solved and attaches no transcription or solution; no published solution was seen. The key was transferred from the finished Jolánka cards (HCP1216 and sisters); the ledger here is a new transcription of this card made from the pixels.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka family, register type MASC). Same key as HCP1216, 1243, 1301:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls ( ) | cs | three short strokes | m | gamma corner | t |
| long stroke + tick on the left | d | two strokes | n | plain cross x | u |
| three bars | e | tilted or upright cross | f | chevron | v |
| open loop with descender | g | long stroke + tick on the right | h / p | low descender | y |
| dotted crossed curve | i | inverted T (also a T-like and a leaning form) | j | crossed curve with hook | z |
| cursive loop | o | | | | |

Two points on this hand: the three bars are sometimes crossed by a stroke (rows 2, 5), read as e/é. The T-like first sign of *tudatom* (row 2) is taken as a t variant from sense. Dots/ticks over o and u give ö, ő, ü; other acutes are faint and supplied in normalization.

**Type note (2026-11-03):** register type changed from MASC to **MASC + Steganography**: the closing (rows 22–26) is written inside the stamp box, under the place of the postage stamp, which is now lifted; see "Stamp-box message (2026-11-03)" below.

Writing order: 19 rows on the left half; rows 18 and 19 run the full card width along the bottom; the text turns up the right edge (row 20), runs upside down along the top edge from right to left (row 21), and the signature fills the stamp box (rows 22–26).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1233/work/decode.py
```

It checks the SHA-256 of all four images, decodes `work/ledger.txt` with the key and prints the literal rows and `work/normalized.txt`. The ledger is a manual transcription (not OCR), so the command proves the key application, not the sign reading.

## Literal decipherment

```
01 szeretetedesjolan             14 hogytudjakva
02 kamtudatomhogyel              15 lamiejszahig
03 sővizsgammasi                 16 benavonatonis
04 kerrelvegzödöt                17 tanultamhogy
05 hedigojelőkeszü               18 akezemrafagyottakönyvrede[h]a[i]st[e]n
06 letlenültalalt                19 neknemtanultamhiabamostmarlefek
07 mertnemszami                  20 sz?[o]mertketnahotanem   (right edge)
08 tottamracsakszom              21 aludtamistenvela           (top edge)
09 batontudtammeg                22 csokol   (stamp box)
10 hogymahetfon                  23 jasza
11 vizsgaleszes                  24 mta
12 nagyinutanna                  25 lansz
13 keletneznem                   26 orfe[r][i]
```

h in rows 5, 20 stands for the h/p sign (pedig, nap). [x] = value from word sense or a damaged trace, not from a clean shape; ? = a visible mark with no value. In the normalized text [x] marks a letter that is a sense call or is not written at all: valami[t] has no t, [h]á[l]' has no l.

## Hungarian (normalized)

Szeretett édes Jolánkám! Tudatom, hogy első vizsgám ma sikerrel végződött, pedig oly előkészületlenül talált, mert nem számítottam rá, csak szombaton tudtam meg, hogy ma, hétfőn vizsga lesz, és nagyon utána kellett néznem, hogy tudjak valami[t]. Éjszakáig benn a vonaton is tanultam, hogy a kezem ráfagyott a könyvre, de [h]á[l]' Istennek nem tanultam hiába. Most már lefeksz[o/e]m, mert két nap óta nem aludtam. Isten vele. Csókolja számtalanszor Feri.

## English

My beloved sweet Jolánka! I inform you that my first exam ended successfully today, although it found me so unprepared, because I was not counting on it; only on Saturday did I learn that the exam would be today, Monday, and I really had to look into it so as to know something. Until nightfall I studied, on the train too, so that my hand froze to the book, but thank God I did not study in vain. Now I am going to bed, because I have not slept for two days. God be with you. Feri kisses you countless times.

## Slovak

Moja milovaná, sladká Jolánka! Oznamujem Vám, že moja prvá skúška sa dnes skončila úspešne, hoci ma zastihla takého nepripraveného, lebo som s tým nepočítal; až v sobotu som sa dozvedel, že dnes, v pondelok, bude skúška, a musel som sa na to poriadne pozrieť, aby som niečo vedel. Až do noci som sa učil, aj vo vlaku, takže mi ruka primrzla ku knihe, ale vďakabohu som sa neučil márne. Teraz už idem spať, lebo už dva dni som nespal. S Bohom. Bozkáva Vás nespočetnekrát Feri.

## Stamp-box message (2026-11-03)

Stamp-box audit by Claude Opus 5.5 on the un-converted scan `work/hires/…_adr.jpg` (crops in `work/stamp-2026-11-03/`: `box_2x.png`, `mask_rows22_23_3x.png`, `mask_rows24_26_3x.png`, the latter two with the purple-ink mask). The postage stamp has been lifted: the paper inside the dotted box is clean, with torn paper scars at its edges, and only a corner of a green stamp (letters "FI…" of the value) remains at the lower left, still carrying the black cancellation. The writing in the box was therefore under the stamp: hidden writing, in the cipher signs only (no plain Hungarian in the box).

It is rows 22–26 of the ledger, already read sign by sign in rounds 1–2 and confirmed again today from the crops; no new letters were added and `work/decode.py` is unchanged.

- Literal: `csokol | jasza | mta | lansz | orfe[r][i]`
- Hungarian (normalized): Csókolja számtalanszor Feri.
- English: Feri kisses you countless times.
- Slovak: Bozkáva Vás nespočetnekrát Feri.

What stays uncertain is as before (uncertainties 2 and 11): in *Feri* the f is close to plain u and r, i run through stamp residue; the signs of row 24 cross the printed triangle (m and a t stem visible). No clause is unread. The rest of the letter is on the open card; only the closing is hidden under the stamp.

## Unenciphered parts of the card

Picture side: printed title "Kis házikóm ablakánál" and a printed verse only, no handwriting. Address side, in plain handwriting: Tóth Jolánka úrleány[nak], Jász-Árokszállás. An upper-left note is read tentatively as "Szigorúan magán" ("strictly private"): the first word is not certain. The postmark is only partly legible (letters PAL and SO, compatible with the Rákospalota cancellation of HCP1216, not established); no date is legible.

## Uncertainties

Signs damaged by the portal stamp:

1. **Row 20, end of *lefeksz-m*.** The stamp letters EU are thin and do not hide anything. After clear s, z there is a dash without a value (`?`), then the flourish of the address, then a small closed loop on a stem with a short bar (review/work/c2.png, c3.png), then the clear m of *mert*. No m stands here, and none could be hidden, so one m is shared by the word and *mert*. Two options, neither firmer: (a) the loop is o, giving colloquial *lefekszom*; (b) the dash is the bottom bar of an e of which two more bars lie in the flourish (review/work2/x20am.png shows three short strokes at one x, at about the bar spacing of e), giving standard *lefekszem*, with the loop sign left over. The flourish cannot settle this. The ledger keeps what is visible (`?`, [O]) and the normalized text writes *lefeksz[o/e]m*. The sense "I am going to bed" rests on *lefek-* and *mert* either way.
2. **Row 26, *Feri*.** e has two clear bars plus a blot at the damaged spot, so e is fair, not clean. The first sign is a nearly equal-armed tilted cross, close to plain u; f rests on the name, as at the fog point of HCP1216. The next sign has stem and arm like r and the last a long curve through the stamp residue for i. The reading matches the signature of HCP1216, but no identity of the two senders is claimed.

Calls resting on word sense:

3. **Row 2 *első*:** the crossed three-bar sign is read as e; it is split over rows 2–3 (*el|ső*).
4. **Row 12 *nagyin*:** the sign after y has the open form of i with a dot, not the closed o loop. Written i is kept in the literal; normalized *nagyon*.
5. **Row 13 *kelet néznem*:** corrected in review. The first sign is k, not b (`work/resp/cmp_k_b.png`). *kelet* is *kellett* with both doubles dropped, as in *végzödöt* and *szeretet*. No t or missing verb remains unexplained.
6. **Row 15 *valami* + *éjszahig*:** h stands where k is expected, read as a slip for *éjszakáig* (or *éjszakig*). The final t of *valamit* is not written. The word division *valami(t). Éjszakáig* is editorial; the alternative division gives *valami éjszakáig* with the same words.
7. **Row 16 *is*:** the i has no visible dot and could be taken as z in form; *vonaton is* decides it.
8. **Rows 18 and 19, *de hál' Istennek*: a restored word.** Replaces the earlier *de ha [m]ost annak*. This is the weakest passage; `work/resp/row18_tail.png` shows it. What stands on the card after *könyvre* is `d e [?] a [i/o] s t [e] n | n e k`. **No l is written.** Taken literally the card has *de ha Istennek* (or *de ya Istennek*), which is not idiomatic, so *hál'* (*hála Istennek*) is a restoration from sense, of the kind withdrawn at *[m]ost* in round 1, and it is marked as such. Sign by sign:
   - d: stem and tick on the left. e: top bar joined to a V-shaped lead-in stroke, then two weak lower bars. The lead-in has no value.
   - [h]: **not a clean h; the shape is close to y.** A long y in row 14 also runs past the crossing, so the stem proves nothing. Only the short stroke to the right of the crossing (about 45 px, larger than the h tick of rows 14 and 17) favours h, and the rest of the case is sense. Value from sense, with y as the alternative shape.
   - a: two clear bars.
   - [i]: the sign shared by i and o, with an unusually long, straight upper arm. Round 2 counted this arm as a separate l; review 2 showed it is part of the sign (`review/work2/cmp_loop.png`, `sign_join.png`). The descender starts where the arm ends, and the ö and i of this hand have the same ductus: arm up to an apex, descender, loop, tail. The dot is not clear. Value from sense.
   - s, t: clear. `review/work2/cmp_isten.png` sets row 21 *isten* above this place: same sequence of forms.
   - [e]: three staggered bars in a regular step. Round 1 saw two. The top bar stands apart near the card corner, so *isten* versus *istan* rests on this bar and on sense. The reviewer's own coordinate mapping confirms the bars belong here, not to row 20.
   - n, then *nek* in row 19: clear.
   *hál' Istennek* (hálistennek) is the common spoken contraction of *hála Istennek*, and *nem tanultam hiába* then says the study paid off, which fits the passed exam. No better word was found: *de ha* and *de hát* give *Istennek* no role. Sense calls here: [h], [i], [e], plus the supplied l. *de*, *a*, *st*, *n*, *nek* and the rest of the clause are read from clean signs. Neither the solver nor the reviewer found this word on a sister card (searched 1212, 1213, 1216, 1217, 1218, 1243, 1301).
9. **Row 20 *nap óta*:** p is the h/p sign, *nap* from sense. A stray long stroke stands between *nem* e and the m at the corner, without a value. A small v-like mark right of the staggered bars at the corner (`review/work2/t4.png`, card x about 3195 to 3220, y about 1860 to 1873) also has no value: a stray mark or the start of row 20. The m itself turns the corner (three strokes, rotated); *nem aludtam* decides.
10. **Row 21 *vela*:** two bars are visible plus a smudge at the very card edge, where a third bar may be cut, so *vele* may be what was written; normalized *vele*.
11. **Stamp box rows 23–25:** the signs of row 24 lie across the blue triangle; the purple-ink mask shows m, a stem of t, and bars. *számtalanszor* fits every visible trace. The l at the start of row 25 is a clear wave.
12. Writer's spellings normalized: *szeretet edes* → Szeretett édes, *végzödöt* → végződött, *ojelő-* → oly elő-, *utanna* → utána, *kelet* → kellett, *ben a* → benn a, accents supplied.
13. Dates: nothing on the card gives a year; "Monday" and "Saturday" are in the text only.

## Why it is correct

- The family key, transferred unchanged, turns the card, including the margins that wrap around it, into consecutive Hungarian with one continuous story (an unexpected exam, night study, sleeplessness). Exceptions are the sense calls in rows 18, 20 and 26 listed above, of which row 18 includes a supplied letter (the l of *hál'*), and the two marks without a value (row 20 dash, corner mark).
- The margin reading order was found from the signs themselves: *lefek|sz-*, *nem | aludtam* and *Isten vele* join across the turns.
- Repeated words decode identically: *hogy* ×4 (rows 2, 10, 14, 17), *vizsga* ×2, *tanultam* ×2, *nem* ×3 (rows 7, 19, 20).
- The formal address (*Isten vele*, *csókolja*) and closing are those of the family's cards.

No published solution was used.

## Response to review 1

Verdict REVISE. Rechecking the findings on 7x crops changed the reading, so this goes back as DONE2. `python3 -I ciphers/hcp-1233/work/decode.py` was re-run: all four hashes OK, the rows above match its output. New crops: `work/resp/`.

1. **Row 18 tail / row 19 (major): fixed by a new reading.** I agree the old clause was not established and withdraw *de ha [m]ost annak*. The reviewer's "de hát most annak" is not needed either. New reading *de hál' Istennek nem tanultam hiába*: see uncertainty 8. (a) The hook is disclosed as unexplained and h is a sense call. The stem past the crossing and the right tick still separate the sign from y. (b) No m is needed. (c) No vowel change: the sign after t has three bars, not two. (d) The translations now follow from the Hungarian. Two signs were overlooked in round 1: the straight stroke over the loop, and the top bar of e.
2. **Row 20 (minor to major): fixed.** The tokens [E] [M] are gone. The ledger now gives what is there: `?` for the dash and [O] for the loop. The word "physically hidden" is withdrawn. Note that the bar at the card corner, near row 20 in position, is taken into row 18 as the top bar of e: rotating the crop shows it belongs to the staggered three-bar group, not to the row 20 line.
3. **Rows 12, 13 (minor): fixed, better than asked.** The b of round 1, which the review also accepted, is wrong. The first sign of row 13 is k: compare `work/resp/cmp_k_b.png`, left to right row 13, k of rows 2, 4 and 14, then b of row 16. The word is *kelet(t)*, so the sentence has its finite verb and is no longer elliptic. Only i for o in *nagyin* and *utanna* remain as spellings.
4. **Row 26 f (minor): fixed.** Now listed as a sense call in uncertainty 2, with the reviewer's better view of r and i.
5. **Row 21 (minor): fixed** in uncertainty 10.
6. **Slovak (minor): fixed** (*takého*), and the clause is retranslated.
7. **"Why it is correct" (minor): fixed.** The first bullet is reworded and *nem* has an exact count.

Note: the *[l]* of item 1 above and "no letter is inserted" are withdrawn; see review 2 finding 1.

## Response to review 2

Verdict REVISE. All findings are accepted; the words and the meaning of the letter do not change, so this goes to FINAL, as the reviewer allowed. `python3 -I ciphers/hcp-1233/work/decode.py` re-run after the fixes: all four hashes OK, output matches the rows and the normalized text above. Ledger: 349 tokens, 6 of them bracketed.

1. **Row 18, [L] is not a sign (major): fixed, I agree.** On `sign_join.png` and `cmp_loop.png` the arm and the descender meet at one apex, and without the arm the loop has no top, a form found nowhere else on the card, while the "l" has no wave. `[L]` is removed from `work/ledger.txt`, and the stroke is merged into [I]. The literal row is now `de[h]a[i]st[e]n`, the normalized text `de [h]á[l]' Istennek`. Uncertainty 8 now says that no l is written, that *hál'* is a restoration from sense, and gives the real count: three sense calls and one supplied letter.
2. **First sign of *hál'* (minor): fixed.** Uncertainty 8 no longer uses the stem past the crossing as evidence. h rests on the short right stroke and on sense, with y named as the alternative shape.
3. **Row 20, dash (minor): fixed.** Uncertainty 1 gives both options, *lefekszem* and *lefekszom*, as equal. The normalized text writes *lefeksz[o/e]m*. The "Why it is correct" bullet no longer cites a full *lefek|szem*; the join across the turn is *lefek|sz-*, which holds on both options. The English and Slovak do not change.
4. **Corner mark (minor): fixed.** Listed in uncertainty 9 as a mark without a value. It is visible on `t4.png` and I assign it nothing.
5. **Wording (minor): fixed.** "Why it is correct" says row 18 includes a supplied letter. Row 26 e is now "two clear bars plus a blot". The status line is rewritten.

Reviewer's note on the register rule applied: one restored word in a clause that otherwise reads, disclosed, so the card counts as complete.
