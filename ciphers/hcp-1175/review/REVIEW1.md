ACCEPT

# Review 1, hcp-1175 (reviewer: Claude Opus 5.5, 2026-11-02)

The digit block is solved. The reading holds on the pixels, sign by sign, and the key is the family key. Only minor corrections remain. One judgement call needs attention before the register entry: finding 1, the dotted `mert` line.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1175/work/decode.py` ran clean. Hashes OK, 57 signs, 52 by the hcp-1174 table and 5 by the 4 extra signs. Raw output: `hamégegyszerel / indulokésodanem / érhetekakoraz / utonföblövöm / magam`, which matches the claimed plaintext.
- **My own decode.** `review/work/ind_decode.py` holds my own reading of the five lines and parses its key out of the table in `ciphers/hcp-1174/SOLUTION.md`, not from the solver's script. Output: `hamége[4.]szerel / ind[.1]lokésodanem / érhetekakoraz / [.1]ton[4]ö[1,]lövöm / magam`. Only `4.`, `.1` (twice), `4` and `1,` fall outside that table. My token list was typed from my crops and came out identical to `work/transcription2.txt`.
- **Transcription.** I read all 57 signs on my own 2x crops of `work/hires/` (`review/work/a1-5.png`, `b1-4.png`), and the critical ones at 4x and 5x (`u_l4.png`, `z.png`). There is no disagreement:
  - L2 sign 4: a round dot stands clear of the 3, 35 px at 2x from the foot of the 1 and well away from the 3, so it belongs to the 1. `3.` plus `1` would give `invilok`, which is no word.
  - L4 sign 1: a dark ink blob left of the foot of the 1, the same ink as the digit. The brown loop lies below it and does not make it.
  - L3 last sign: the 9 is followed by a real comma stroke, rising higher than usual. Bare `9` = p would give `ap`.
  - L4 sign 5: the 4 is bare (no comma), and the comma after it belongs to the 0, so `f` + `ő`. L4 sign 7: the comma belongs to the 1, giving `b`.
  - L1 sign 2: a tiny speck above the dot of `1.` is too small to be the upper dot of `1:`.
- **Key coverage.** Every sign of the block is keyed; no sign is left over and no value is forced. The key is single-valued on this card.
- **Language.** The sentence is natural Hungarian. A 57-sign run with no word divisions parses into one grammatical sentence with only two spelling slips (`akor`, `főb`), and both are disclosed.
- **Open text and address.** Read on `h.png`, `v_all.png`, `v4.png`, `v4b.png`, `m.png`, `mb.png`, `addr.png`, through the brown strokes: Kedves Ángyika; the four verse lines; Távolban a vágyam- / nekem; Ha te is itt volnál / velem; Légy szives irjál / mert; Sz. A.; the address. All agree with the solution. `vágyam` is clear, with its accent and its hyphen at the line end.
- **Postmark.** Rotated crop `pm_r.png` shows OKT 25, with the year smudged, as the solution says.
- **Dotted line.** The ink-isolated strip `dots.png` gives 8 marks, the m, 5 marks. I counted these independently. A sixth mark seemed to appear at the right, but `r1.png` shows it is the foot of the `u` of `u. p.` in the address, so the count stands. Marks are evenly spaced, and no letters are hidden under the brown strokes.
- **Context.** Writer and addressee fit the family: same Szegedi Jánosné / Szomolya / Bogács address as hcp-1176 and 1179, same signature as 1178 and 1179. The top line of hcp-1179 ("nem mehetek megint", as filed there) fits the failed journey in this sentence.
- **Published solutions.** The portal lists none, and the solver used none. The HistoCrypt article remains unchecked, as disclosed.

## Findings

1. **minor (judgement call for the register): the `mert . . . m . . .` line against the completeness rule.** The status says complete. The run's rule makes a card partial for a whole unread clause, unenciphered text included, and allows an un-understood item only if it stands alone and the rest reads. The clause content is genuinely unknown. I accept complete for three reasons: nothing written is unread, since the marks are not letters; the string is one even, unbroken run with no visible word space; everything else on the card reads. So the single-item allowance applies. This is a call about the rule, not a fact about the card. The solver should state it in those terms, and the report should say plainly that the clause is withheld and unknown. If the human reads the rule more strictly, the card is partial and gets no entry. "Every written word reads" is true and can stay.
2. **minor: Uncertainty 3 is false as stated.** It says "Four signs occur only here" and calls them new, and "Why I believe" treats them as fixed only by their words. All four are ordinary family signs. Tables on FINAL cards of hcp-1135…1179 list `4.` on 32 cards, `1,` on 28, `4` = f on 21 and `.1` on 19. hcp-1138, for example, gives `4.` in hogy, úgy, ángyika and `.1` in úgy, május, kapuba, with `4` = f in its table. The error is on the cautious side, and correcting it strengthens the solution. Replace "new / only here" with "not in the hcp-1174 table, attested on sister cards" and cite a few.
3. **minor: the date note is not pencil.** The solution twice calls `1915 (X.25.)` pencil, and Uncertainty 8 suggests a later collector. On `date.png` it is pen, with blue ink pooled at stroke ends. The colour is that of the address and of `u. p.`, and the 5 has the same detached top stroke as the digit block. It is probably the writer's own hand, so the year is better grounded than the solution says. The third digit of the year has a blot and a crossing stroke and needs a note; 1915 is read from the date of the card family, not from a clean digit.
4. **minor: `Ángyika` is not glossed.** The translations treat it as a name. FINAL sisters hcp-1138, 1144, 1165 and 1167 gloss ángyika as a kin word (sister-in-law or aunt by marriage). Add that gloss in the English and Slovak translations and in Uncertainty 2. It also explains the opening better: the card is addressed to the kinswoman, the digits are for Margit.
5. **minor: description of the dots.** Uncertainty 1 says two marks are taller ticks and that the conjecture's l gets none. I see three raised marks: position 3 before the m (the tallest), and positions 2 and 4 after it. Position 3 falls on the `b` of `főbelövöm`, a tall letter, which the solution does not mention. Position 1 (`f`) and position 5 (`l`) are low, and the raised marks after the m do not fit `agam`. So the marks do not imitate letter heights consistently. The conjecture stays a conjecture, as the solver rightly says.

## What I could not verify

- The HistoCrypt article linked by the portal: not read.
- The printed source of the verse, if there is one.
- The sense of `Távolban a vágyam- / nekem` beyond the plain reading, which is letter-sure but slightly odd.
- The meaning of the dotted line.
- The postmark year: smudged.
- Who made the brown overstriking, or when.
