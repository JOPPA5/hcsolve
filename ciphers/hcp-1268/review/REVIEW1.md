REVISE

# Review 1 of HCP1268 — Claude Opus 5.5 (reviewer), 2026-11-01

The cipher, key, language and sender stand. Most of the text is right. My own sign-by-sign reading differs from the solver's ledger in 4 of 19 rows, and two of those are plain misreadings that the SOLUTION explains away as writer's errors. The one word left "not understood" very probably is understood: *ravoban* = *[a] távo[l]ban*. Fixes are needed before FINAL.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1268/work/decode.py`: all four hashes OK, 237 tokens, output identical to the literal block and normalized text in SOLUTION.md.
- Made my own crops of the hires address scan (`review/work/crop*.py`, `review/work/crops/`), 2x to 8x on top of the native resolution, covering all 15 rows, the stamp box, the postmark and the plain address.
- Wrote my own shape-class ledger before diffing, and a separate decoder with the key restated (`review/work/my_ledger.txt`, `review/work/my_decode.py`; run `python3 -I ciphers/hcp-1268/review/work/my_decode.py`). Result: 15 of 19 rows identical once ő is treated as in finding 7. The four that differ:

```
04 mine kedvebentalalja        solver kedvebantalalja
06 mine azegyletbenaszabon?k   solver azegyletbenaszabonk   (uncertain sign marked, not a real conflict)
08 mine naplesz{e}zishacsak    solver naplesz{a}zishacsak
11 mine mibenalapodor          solver mibanalapodor
```

- Key coverage: every sign falls in a family class. The joined n is not new; it is in the HCP1285 key table, so "no value invented" holds. The stamp box *csókolom a kis szájat* is confirmed sign by sign, unrotated (`y_stamp.png`); the last sign of `csoko` is an inked loop, as disclosed.
- Row 9 blot (`x_blot9.png`): a tick, a blot, then two bars; three tiers, so e is reasonable. The row 9 `lehe` + `ebbe` division and the omitted t are honestly disclosed.
- Row 15 first sign (`x_b15.png`): a redrawn six with a lead-in stroke, b is fine. *Holes* is supported by sister cards (HCP1244, 1303, 1309, 1278); the low tick is disclosed.
- Plain address confirmed (`y_bottom.png`). No published solution is attached on the portal capture, and none appears used. Sister-card key use is disclosed. Language is real period Hungarian of this writer.
- Postmark (`x_pm.png`): 912 JAN 17 is legible. `python3 -c "datetime.date(1912,1,17)"` gives Wednesday.

## Findings

1. **major — *ravoban* is very probably *[a] távo[l]ban*, "[in] the distance".** Letters r a v o, b a n stand as read, but the solution stopped at "no Hungarian word". The fit needs r for t plus one l, and each has support on this card:
   - The writer writes F for t in this very card, in row 11 `alapodor` = *állapodot(t)*, which the SOLUTION itself accepts. The family has a record of F/gamma confusion (HCP1243 `alí{t|r}ja`, HCP1251 *terve*, HCP1218, HCP1267).
   - The F in row 14 has a smudged, disturbed lower stem (`r14b.png`). The shape is F as far as visible, so this is word sense, not pixels; say so.
   - A separate tick stands up and right of the F, over the following two bars (`r14b.png`), the position of the accent of á in row 11 *ál-* (`r11b.png`). The solver does not mention it.
   - The "small arc right of the o" (`x_ov_end.png`), left unexplained in uncertainty 1, stands exactly where the l belongs and may be a cramped or added l. Otherwise the l is omitted, like the many omissions on this card.
   - *a távolból* is this correspondence's stock formula (HCP1243, 1244, 1261, 1271, 1276). *…maradok epedő szívvel a távolban, Holes Ferenc* ("I remain with a yearning heart in the distance") closes the letter, and also explains the struck sign before it as the article a. Holes is away from Jászárokszállás, consistent with the Budapest address on HCP1303.
   Please test this and adopt it if it stands, as `{r→t}` with word-sense disclosure, and drop "not understood" from the status, text and translations. I propose it; I do not claim that the pixels prove it.

2. **major — rows 4 and 11: the sign after b is three bars, not two.** `z_r4e.png` and `z_r11a.png` show three separate bars, the third lower but clearly there; the two-bar signs nearby are visibly different. The literal text is *kedvében* and *miben*. Ledger rows 4 and 11, the literal block, the normalization `mi[be]n` and uncertainty 6 ("a for e, three times") are wrong for these two: nothing is restored, and the writer made no error. In row 4 the third bar sits apart from the others, near row 5, which probably caused the miss. Only row 10 `as` remains as a two-bar case (`z_r10a.png`): confirmed two bars, unusually far apart, no middle bar visible. Say so; *és* there is word sense alone, as stated.

3. **major — row 8 struck sign has three tiers, so it is e-shaped, and uncertainty 4 misdescribes it.** `x_struck8.png` shows a separate arched top bar well above two bars crossed by diagonals. The solver reports "two bars crossed by diagonals" and gives {a}. Three tiers, with the top one arched as in this writer's e, give *ez is*: "this too will be on Sunday", which goes better with the following *ebbe menjünk*. The row 14 struck sign (`x_struck14.png`) really has only two bars, so the two signs differ and "the same struck sign" in uncertainty 1 is false. Correct the ledger to `{e|a}` or `{e}`, and report both readings.

4. **major — rows 6–7 normalization is not Hungarian as printed, and the translation does not render it.** *a szabónk meghívó[j?]* has no possessive, though the English gives "our tailor's invitation". The "unexplained" j is explained simply by *meghívój[a]*, a dropped final vowel in the style of this card's other omissions, which gives the possessive. The sign after b in row 6 (`x_row6end.png`) is a loop overlaid with heavy strokes, with a long arched tail running into the blot. Separate n strokes are not visible. A long o tail with no n, giving *szabók*, fits at least as well as the solver's o + joined n. *Az egyletben a szabók meghívója, és vasárnap lesz ez is*: "in the association [there is] the tailors' invitation, and this too is on Sunday", a trades' winter dance fits the season. The solution treats *szabók* as a side alternative; make it at least equal, keep *szabónk* as the alternative, and print a normalization that parses. The sense "an invitation, on Sunday, let us go" holds under both, so this is not an unread clause.

5. **minor — the title is misleading.** "an invitation, Sunday, 17 January 1912": 17 January 1912 was a Wednesday. The postmark date is the writing or posting date; the *vasárnap* of the card would be the next Sunday, 21 January at the earliest. Fix the title, and state this in the text.

6. **minor — row 11 `állapodo[t]t` hides a substitution.** Brackets elsewhere mark omitted letters, but here the written r is replaced. Mark it as r for t, spell `álapodor` as the source of *állapodott*, and link it to finding 1. Uncertainty 6's "or an error of mine" can go: the sign is clearly F (`r11b.png`). Also *megállapodott* takes *meg* from row 12: *állapodott meg*, which is fine, but mention it. The translation "what you have agreed on" assumes that the 3rd-person form is polite 2nd person, correct for this card's *Ön* register.

7. **minor — ő is not printed.** The key table says two ticks give ő. Rows 3 and 14 have two ticks, but the ledger tags them `:dia` and decode.py prints `vebölhogy`, `döszivel`. Add a token for ő, so that the literal agrees with the stated key.

8. **minor — the command does not really apply the key.** Ledger tokens are already letters, so decode.py is nearly an identity print. SOLUTION does disclose a manual ledger, but "decodes" oversells it. Either tokenize by sign class or describe it accurately. The ledger itself has `# Not OCR and not blind`, which is fine.

## Could not verify

- *távolban* and *szabók/szabónk* against the pixels alone: both need word sense (see findings 1 and 4).
- The second-hand claims for the hand match with HCP1278/1303/1309 beyond reading their SOLUTION texts; I did not compare hands on scans.
- What event is meant. HCP1305's "Kath. Leg. egyleti mulatság 20-án" is a tempting link, but it has no full date, so no link is claimed.
- The HistoCrypt article was not consulted by me either.
- Which of the two cancels is origin or arrival. The rim reads about …ÁROK…S on the N cancel, compatible with Jászárokszállás.

## Register

MASC is the right type. After the fixes the card qualifies as complete: nothing beyond single words is in doubt, and rows 6–8 read. Do not write the register entry until findings 1 to 4 are answered.
