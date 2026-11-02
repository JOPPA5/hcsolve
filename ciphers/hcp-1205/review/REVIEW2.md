REVISE

# HCP1205, review round 2 (Claude Opus 5.5, reviewer, 2026-11-02)

Summary: all thirteen findings of round 1 are fixed on the card, and the new reading of rows 25-26 mostly holds. The one open word group is not open: the tall + short sign in *jöneNek* is the ordinary p, the same form as in *pedig* in the same row, and the group reads **nagyon jó népek**, "very good people". *Egy hét is pedig a rokonnál leszek* is then a sound sentence, not a fragment, and the current translation of it is wrong. No clause stays unread. Once these fixes are in, the card is complete and needs no third round. Type label for the register: MASC.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1205/work/decode.py` runs, all four hashes OK. Its 43 rows are byte-identical to the literal block in SOLUTION.md (`review/work/check2.py`). 1239 signs, as claimed.
- **Independent decoder.** `review/work/check2.py` has its own token table and gives the same 43 rows, with no token outside the key. Counts: H 30, P 6, N 5, D 5, M 2, Y 3, G 24, digit 5 once. This shows the ledger maps as claimed; the ledger itself was tested on the pixels.
- **Pixels.** New crops of `work/hires/` in `review/work/crops2/` (`review/work/c2.py`), 2-6x:
  - all of rows 23-27, strip by strip (`f0`-`f4`) and sign by sign in the new reading (`g1`-`g3`, `g5`, `g6`, `h1`, `h2`);
  - struck sign, row 24 (`s1`);
  - sample rows 04-06, 14-15, 19-20 (`k1`, `k3`-`k5`, `n1`);
  - stamp block (`st`, `s0`);
  - upside-down block, top rows after rotation (`u3`).
  These agree with the ledger, apart from the findings below.
- **Fixes from round 1, checked in the ledger and text.** Row 05 `Hiszem`, row 08 `5`, row 13 ending `Ha`, row 21 `Perszea`, row 24 ending `DoG`, row 25 ending `aroko`, row 27 `Hanem meGek Haragszanak`, U6-U7 *kelméből*, and the verse. All present and matching the crops.
- **Solver's new calls on the pixels.**
  - *menne*: the m is a free stroke plus a joined pair, three strokes (`h2`). Confirmed; the solver is right and my round 1 reading of tall + short was wrong.
  - *nagyon*: n, a, G, o, n (`g1`). Confirmed. The tick under the a is detached and could belong to row 26, as Uncertainty 3 says.
  - *egy hét is*: k e G, long + short slash, e, Γ, i, s (`g3`, `g6`). The last sign is the right bowl s, not a g loop, so *hétig* is excluded.
  - Row 20 *látom, mivel*: the Γ has the gy tail from row 19 crossing it, and the count of six strokes holds (`k5`).
  - S1 *i s*: both signs are faintly visible (`s0`), so this rests on pixels as well as sense.
- **Context.** The clear address, the signature Jolánka in cipher in S8, *vasutasné* for a M.Á.V. brakeman, and *pletyka* all fit. No sign of a published solution being used. The sister-card spelling *reményem* is disclosed as such.

## Findings

1. **Row 25 `jöneNek` is `jó népek` (major).** Crops `g2.png`, `g5.png`, `g6.png`. The sign after *jon e* is a long tall stroke plus a short tick, identical in form to the first sign of *pedig* in the same row (`g6`, right side). The two equal strokes of the plain n stand next to it, just before the three bars (`g2`), and look clearly different. So the family's own value p applies, and no "also n" is needed: j-o, n-e-p-e-k = **jó népek**, with the *é* unmarked as usual. *Nagyon jó népek* "very good people" says who the *idegenek* are, and follows naturally on *csak jöjjön hozzájok, mintha otthonra menne*. Change `N` to `P` in the ledger, and *nénék* to *népek* in normalized.txt and all three translations (English "Very good people."; Slovak "Veľmi dobrí ľudia."). *Jönnének* and *jönne nek(i)* fall away. Delete Uncertainty 1 as a doubtful group; keep only a note that the unmarked o is read *jó*. This ruling is on the pixels plus sense: the sign form is the evidence and the word confirms it.

2. **`egy hét is pedig` is a sentence, and the translations are wrong (major for the translation).** No sign changes. *Egy hétig idegeneknél leszek* in row 23 is answered by *Egy hét is pedig a rokonnál leszek*, "And for a week too I shall be at the relative's." *Pedig* here is the ordinary linking "and/whereas", not "although", and the comma after *is* in the normalized text cuts the sentence apart. The plan of the visit then makes sense: a week with strangers, who are very good people, and a week with the relative, *de ezeknél nem jó kedvemből leszek*, "but with these I shall not be gladly". The contrast holds only on this reading. Uncertainty 1's "fragment that the writer leaves hanging" must go, and English and Slovak must be rewritten (Slovak *hoci* removed). Normalized: *... mintha otthonra menne. Nagyon jó népek. Egy hét is pedig a rokonnál leszek ott, ahonnan maga egyszer a Bélát is kihívta, de ezeknél nem jó kedvemből leszek, csak ha nem megyek, haragszanak.*

3. **The key note "in this hand also n" is overstated (minor).** After finding 1, four N tokens remain: rows 04 (two), 06 and 14. Row 14 `ugaN` is a plain pair of equal strokes (`k4.png`), so it should be `n`. Row 06 *Nagyon* does show a taller first stroke with a tick (`n1.png`), and row 04 is similar, so these few may stand. State the class as three tokens at most, chosen by sense, and take it out of the table line unless the solver can defend it. Update the ledger header and the N count.

4. **`Why I believe` and the status line (minor).** The status line says "one doubtful word group remains in row 25". With 1 and 2 applied it should say the card is read whole, with the doubtful points listed below it. The title stays as it is. Word the *ott, ahonnan* call as sense-based: it rests on a blotted vowel.

5. **Row 26 blot (minor).** Crop `h1.png`. The blotted sign shows one thin bar over one thick blob. I cannot see three bars, and I withdraw my round 1 "three thick bars". Two bars, a, cannot be excluded, and that gives plain *ahonan* = *ahonnan*, with no dialect *honnen*. Mention this in Uncertainty 2: the sign is either a or e, and the word is the same.

6. **Row 24 strike (minor).** Crop `s1.png`. The struck sign is overwritten with a cross-hatch, and the next sign is a pair of strokes taken as `M`. A third stroke under the hatch would make this a plain m, or the writer may have corrected a false start. The word *meglátogasson* is not in doubt. Say so in Uncertainty 5 and move `M` for this token out of the "two strokes read m" note if this is accepted.

## What I could not verify

- The writer's intended vowel under the row 26 blot, and the digit in row 08 beyond shape and sense.
- Who Béla was, and what *kihívta* means here: summoned or challenged.
- Accents, word by word: they are too loose.
- The date: the postmark gives nothing usable.
- I did not read every sign of every row again this round, since round 1 did. U1-U8 were sampled, not re-read in full.
- I did not read the HistoCrypt article, so I cannot say whether it prints this card.

## Disclosure and honesty

Restorations and sense-based calls are disclosed. The reader is told the reading was not blind and what work was done. The solver also corrected me on the m of *menne*. Its ranking of Uncertainty 1 was honest, but the value used there was forced: it reached for n when the sign's own value gave a word.

## For the solver

These fixes are local: one token, plus word division and translation of one sentence. If they are made as written, verdict REVISE leads to report, register entry and FINAL; no further round is needed under the README. Type label MASC.
