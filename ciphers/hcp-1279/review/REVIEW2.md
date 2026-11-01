REVISE

# Review 2 of HCP1279 (Claude Opus 5.5, reviewer, 2026-11-01)

All five sign fixes and the text fixes from review 1 are in and correct. *Három hé[t]* (?) survives testing as a disclosed conjecture. Two things need fixing. The stamp reading *vágyó* overlooks a closer parallel in the same family, *vagyo[k]*. The ledger also has one wrong sign in row 20, and correcting it removes a listed uncertainty. Neither fix touches the key or the body of the letter, and the card does not need a third full review for them.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1279/work/decode.py`: hashes OK, 647 signs, output identical to the literal and normalized blocks in SOLUTION.md.
- New decoder `review/work/decode_review2.py` (own table and loop over the ledger): same rows, 647 signs, every token has a value except the disclosed `*`. Counts on the decoded text: hogy 8, mert 3, pénz (`henz`) 3, csak 4, maga 4, kívánja 2, matching the claims. This checks the decoding, not the ledger; the ledger is the solver's transcription, so I checked it on the pixels.
- Fresh crops from the hi-res address scan (`review/work/crop2.py`, `review/work/crops2/`): stamp field `st`, `s2z` (6x); rows 10-11 `r10`, `r10b`, `r10x` (8x), `r11s`; row 20 `r20b`, `r20x` (7x); rows 6, 18, 25, 27 (`r06`, `r18`, `r25`, `r27m`, `r27e`); sample bands rows 1-4 (`b1`), rows 14-17 (`b2`), rows 28-29 (`b3`).
- Review 1 fixes rechecked against the ledger: rows 1, 9, 14, 19 and S3 are as I found them, and *édesem* and *jó tanácsokat* read.
- Sample bands: rows 1-4, 14-17, 28-29 agree with the ledger sign by sign at this scale. Row 25 has r, h, t, a loop with no dot. Row 27 `elküldöm dom` is written as stated: after the three strokes of m come a short + long d, a loop and three strokes again.
- Row 3 blot and rows 5-6 under the postmark are truly hidden and disclosed. Row 6 `y`, `i` (dot visible above the loop), h, é, n, z agree.
- Sister cards: HCP1297 `sakharomhetmulva`, HCP1263 *3 hét múlva*, HCP1251 *szétvélasszon*, *bérmijen*, HCP1308 stamp field read directly from their SOLUTION.md files.
- 1279 is not in skip.txt or register-exclusions.json. The portal capture shows no attached solution; no sign of a published solution being used.

## Rows 10-11, *[h]érom hé[t]* (?): tested, acceptable as conjecture

- `r10x`: after k there is a green stroke from lower left rising under the postmark line, with a short green mark right of it. The stroke is about 58 px long, the same as the long stroke of the h sign in the same row (`hogy`, about 59 px). The short mark is only about 18 px visible against 40 px for a full tick, but its upper part would lie under the postmark. Short + long (d) and two equal strokes (n) fit less well. The solver's `[H]` is fair, and it is not invented: the ink is there.
- `r11s`: first sign: tall stroke, then a shorter one whose base stands higher, the same arrangement as h in row 10 `hogy` and row 25 `ruhát`. So the pixels lean to h, slightly more than the solver claims; `NH` is still the honest ledger token.
- Three clear bars in `erom`: agreed, e for á is a real cost. Dropped final t: agreed.
- The (?) and the listed costs are honest. Under this run's rule this is one conjectural word in a sentence that otherwise reads, so it does not make the card partial.

## Findings

1. **major. Stamp S2: *vágyó* is not the best word, and the parallel cited for it points elsewhere.** Uncertainty 6 cites HCP1308 for `csokjaiert` but omits what follows it on that card: `csokjaiert / vagyo / ...`, normalized there as *Csókjaiért vagyo[k] sírig hű imádója, Feri*. This card has the same structure: `csokjai|é vegyo | kedvesse | feri`, which gives ***Csókjaié[rt] vagyo[k] kedvese Feri***, "for your kisses I am your sweetheart, Feri". It is the same formula from the same family, with the same `vagyo` without k at the end of a stamp row; here the next row even begins with k. "No alternative found" is therefore wrong, and "longing for your kisses" must not stand as the only rendering. Adopt *vagyo[k]* as the first reading, with *vágyó* as the alternative (see finding 3), both with (?), and amend all three languages. The letters do not change.

2. **minor. Row 20 sign 7 is two bars, not three: `volxaaza`, *vol[n]a az a*.** Crops `r20b`, `r20x`: after the scribble there are two faint bars, with clean paper between them and no middle bar, then two darker bars, z, two bars. The ledger token `E` should be `A`. Row 20 then reads `itvol{x}aazaherczhogy`: the scribble stands where the n belongs and every other letter of *volna az a* is on the card. Uncertainty 11 ("the three-bar sign is not accounted for") falls away. Change the ledger, literal block and uncertainty 11. Whether the scribble hides an n stays unread and should be said.

3. **minor. Stamp S2 signs 3 and 6 are described more firmly than the pixels allow.** `s2z`: sign 3 has a top bar, then a black blot with two lobes. "All three bars are visible" overstates it: two lobes of about the same reach fit two bars, but a single lower bar of a two-bar a under the blot cannot be excluded. So sign 3 should be `AE` in the ledger, and the "e for á" cost may not exist at all. Sign 6 is a loop with a separate tick at its upper right. The tick is not in the ledger or the uncertainties. It could be an accent, which would favour ó and *vágyó*, or stray; it is the one point in favour of the alternative. Record it. Either way the verb stem stands.

4. **minor. Uncertainty 5(c) says "the same writer" while the closing paragraph says identity is not claimed beyond name and key.** HCP1297 dates from 1912 and HCP1263 from 1913, against April 1914 here, so they support the phrase, not the event or the number. Reword as "same family", and say so.

5. **minor. *ami erre [kell]* supplies a word not on the card.** It is bracketed, but it is not in the uncertainties; rows 6-7 run directly `amierre | de`. Add it to the list.

## After the fixes

With findings 1-5 applied, the disclosed points are one conjectural word (*három hé[t]*), the stamp word with two named readings, and text physically lost under the stamp (S0) or postmark. By this run's rule that counts as complete, and the register label MASC fits. I see no reason for REJECT. If the solver makes only these changes, it can go to `FINAL` under README step 5 (REVISE, findings addressed).

## What I could not verify

- The number in row 10; `herom he` is a conjecture and three is not proven by the pixels.
- Row 6 hidden signs (annyi/ennyi), S0, and whatever was under the stamp.
- The scribble in row 20; `dom` in row 27 as dittography; `tetürem` in row 4 as *elveszte[m] türe[lme]m[et]*.
- Rows outside my sample were checked at band level in review 1 only. The picture side was not rechecked in this round.
- Hungarian judgement is mine; no native reader checked it.
