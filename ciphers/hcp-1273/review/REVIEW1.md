REVISE

# Review 1 of HCP1273 (Claude Opus 5.5, reviewer, 2026-11-01)

The solution is right in substance: key, cipher type, letter, sender and addressee all hold. But four tokens of the ledger are wrong against the pixels, and two of those errors produced forced readings in the normalized text and translations ("mennyem" = heaven, "mer[t]" = for). Corrected, the passage reads better and with fewer emendations. All fixes are concrete, so REVISE, not REJECT.

## What I verified and how

- **Solver's command**: `python3 -I ciphers/hcp-1273/work/decode.py`. All four hashes OK. Output is identical to the literal text and normalized text in SOLUTION.md.
- **Independent reading**: I went through all 22 rows on my own enlarged crops of the hi-res address scan (`review/work/rc.py`, `review/work/crops/`: L0–L6, R0–R6, Bfull, Bright, plus sign zooms), with the HCP1216 key. Every row was read; bar counts (a = 2, e = 3) were checked sign by sign where the sign was not obscured. My reading is `review/work/ledger_reviewer.txt`.
- **Comparison**: `python3 -I review/work/check.py` (from the cipher directory) gives solver 478 tokens, reviewer 477, exactly 4 differences (findings 1–4). Agreement on the other 474 tokens.
- **Key**: the table matches HCP1216. No new value is needed and every sign is covered, apart from the point in finding 8. Rows 21–22 do run along the bottom edge under the address as claimed.
- **Claimed restorations, on the pixels**:
  - row 2 sign before gy (`r2end`): a vertical stroke crossed by bars, unclear, as disclosed;
  - row 2 final lattice e: as disclosed;
  - row 8 heavily retraced first sign: d is consistent, disclosed;
  - row 15 blot after v (`r15`): thin top bar plus a blot, a/e undecidable, as disclosed;
  - row 16 e of nem under the pink blot (`r15b`): bars are visible through it, two strokes of n beside it; acceptable;
  - row 16 literal `ülésese` (`r16b`, `r16c`): all three e are clean three-bar signs, s twice; the letters are correct (see finding 5 for their interpretation);
  - row 21 end, *vele* under the collector's stamp: consistent.
- **Row 4 *csak*** (`r4`): two bars linked by a diagonal, as disclosed.
- **Cursive note** (`note`): *csokolom / szamtalan / szor sirig / hű pene / ketse / Fer…* I also cannot read "pene" and "ketse"; the solver's disclosure is honest. This is plain text, a single unread word plus a doubtful one, and it does not block completeness.
- **Postmark** (`postmark`): MAJ is legible; the day digit looks like 4, consistent with the file name 1912-05-04. The year is illegible.
- **Language and context**: real Hungarian of the period with the family's spelling habits, Feri to Tóth Jolánka, formal *ön*, closing formula matching HCP1216. Word-count claims in "Why it is correct" check out (Jolánkám ×3, vasárnap/-i ×3).

## Findings

1. **major: row 10 has one m, not two; the word is *enyém*, not "mennyem".** Ledger: `L A G O M M E N Y E M`. On the card (`r10m`) only one group of three strokes stands between the o of *csillagom* and the three-bar e. That gives `csillagom enyem`: *ha itt lett volna az én csillagom, enyém volna a táncterem* = "if my star had been here, the dance hall would have been mine". This needs no emendation. "Mennyem" ("my heaven") depends on an m that is not on the card, plus a doubled n. Fix the ledger, normalization, all translations, and delete `menyem → mennyem` from the spelling list.

2. **major: row 11 is *már*, not "mer[t]".** Ledger: `M E F E GY`. The sign after mm is two hooked bars (`r11mar`, `r11a`), clearly two, while the e right after the r has three. Read `M A R E GY O R A K O R` = *már egy órakor hazamentem* = "already at one o'clock I went home". This removes the emendation *mer[t]* and the non-sequitur "for I went home at one o'clock". Fix the ledger, normalization, translations and spelling list.

3. **major: row 8 is *sokszor elgondoltam*, not "sokszor[al] gondoltam".** Ledger: `F A L G`. The sign after r has three clear bars (`r8e`): e. Read *sokszor elgondoltam* = "I often thought to myself". The bracketed "[al]" and the speculation about dialect *sokszorral* came from a misread sign. Remove them.

4. **minor: row 6 last word is literally `aval`, not `avel`.** The sign before the final l has two clean bars (`r6end`): a, so `A V A L`. Normalization *avval* stands, but the ledger, the literal text and the spelling note `avel → avval` must change to `aval → avval`.

5. **minor: two avoidable emendations in rows 15–16; a better division should be considered.** The solver treats `ülésese` as a dittography and deletes *-es-*, and leaves `be` open. No sign needs deleting: *… ülése, s e miatt nem mehetek le* ("…meeting, and because of that I cannot come down"), with *s* = "and", *e miatt* = "because of this". Likewise `egyletbe` can be *egyletbe(n)*, dialect -be for -ben ("in the association"), which needs no omitted l: *vasárnap lesz az egyletbe választmányi ülése, s e miatt nem mehetek le*. The first division is the stronger of the two; `egyletbe` is a proposal and should be stated as such if adopted, with the bel-/bál- alternatives kept in the uncertainty note.

6. **minor: the claimed a/e safeguard is incomplete.** Uncertainty 8 covers a/e only after gamma, and "Why it is correct" says the words confirm the reading. Findings 2–4 are bar-count errors in clean signs *not* after gamma, in each case made in the direction of an expected or imagined word. After fixing, state that bar counts were rechecked; the transcription note already says it was not blind.

7. **minor: "Why it is correct" and the status line must follow the changes.** The text "continuous Hungarian with no gap" stays true, but the English and Slovak must be regenerated, including "the dance hall would have been my heaven" and "for I went home". The Slovak *s kým som súhlasil* for *akit elfogadtam* is loose; "koho som prijal(a)" (whom I accepted/took on as partner) is closer, and matches the English.

8. **minor: key table does not match the ledger for ny.** The table says the joined cy sign is "gy (ny after n)", but in rows 10 and 15 the sign after n is the plain y-form, without the c-loop, and the ledger has `N Y`. HCP1216 lists "low descender y" as its own class. Add that row to the table.

## Corrected passage (for the solver to check against the crops)

`… de sokszor elgondoltam, ha itt lett volna az én csillagom, enyém volna a táncterem. Már egy órakor hazamentem.`

## What I could not verify

- Whether any published solution exists: I did not consult the HistoCrypt paper cited on the portal or search the literature. The solver says the same; the portal shows no solution.
- Faint accents are not transcribable at this resolution, so all acute accents remain editorial.
- The sign before gy in row 2 (*[í]gy* or *egy*): undecidable; rests on sense.
- The vowel in row 15 under the blot; the words "pene" and "ketse" in the cursive note; the postmark year.
- The picture side: I did not check it; the statement that it has printed captions and no cipher is the solver's.

## Conclusion

Apply findings 1–5 and 7–8. No sign needs a new value and no clause is unread, so after those fixes the card can count as complete.
