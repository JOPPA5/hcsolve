# HCP 1021 — solution (round 1)

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1021 — `cpc_1901-03-13_DE_Roggenburg_DE_Weyarn_`,
status **Not solved** when captured (2026-10-26), tags Postcard / T. Schrödel Collection / Pigpen.
Postcard from Roggenburg to Fräulein … Schmid, Weyarn (Bavaria), postmarked 13 Mar 1901.
No individual solution is attached on the portal; the linked Schrödel (HistoCrypt 2021) overview
paper was checked earlier without finding this card's reading. The reading below is our own.

## Cipher and key

**Standard Pigpen (Freemason) cipher, German.** The cipher line along the top edge of the picture
side was written with the card **turned 180°**: the signs stand on the frame line and the five
comma-like word dividers hang below it. Read with the card rotated, left to right (= right to left
on the stored scan), with the textbook key:

```
 A | B | C        J.| K.| L.        \ S /         \ W. /
---+---+---      ---+---+---      T  X  U      X.  X  Y.
 D | E | F        M.| N.| O.        / V \         / Z. \
---+---+---      ---+---+---
 G | H | I        P.| Q.| R.
```

(Letter = shape of its cell; a dot inside = second grid.) Signs used on this card: A ⌟, B ⊔, D ⊐,
E □, F ⊏, G ⌝, H ⊓, I ⌜, L ⌞·, N □·, O ⊏·, R ⌜·, S V, U <.

The letter A is written both as a plain ⌟ (glyph 28) and twice (glyphs 11, 24) as a ⌟ whose
horizontal meets the vertical slightly above its foot, so it looks like a T lying on its side —
these were the "tee_right" signs that blocked the earlier attempt.

## Plaintext

Cipher text (card rotated, word dividers as spaces):

```
RAD[x]FAREN SOLL LEBEN ALL HEIL GRUS
```

`[x]` = one sign heavily struck through by the writer (cancelled; not read).

German, normalised: **Radfahren soll leben! All Heil! Gruß**

- English: *Long live cycling! "All Heil!" Greetings.*
- Slovak: *Nech žije cyklistika (bicyklovanie)! „All Heil!" Pozdrav.*

"All Heil!" was the customary greeting of German cyclists' clubs around 1900 (general historical
knowledge, not taken from a source in `source/`), which fits "Radfahren soll leben".

## Reproduce

From the repository root:

```bash
python3 -I ciphers/hcp-1021/work/solve_1021.py
```

It checks the SHA256 of `source/picture.jpg`, `source/address.jpg` and `source/metadata.md`,
holds the full sign-by-sign transcription (29 positions, ids of `work/transcript.json`, shapes
described in the rotated reading orientation) and the standard Pigpen key, and prints the
plaintext. Output saved in `work/solve-output.txt`.

## Uncertainties

1. **Glyph 26 is cancelled** by the writer (a large X over it); the underlying sign was not read
   and is omitted. Possibly a mis-written letter (e.g. an H of "Radfahren"), but that is a guess.
   Without it the word is the spelling "Radfaren" (or the writer's omitted *h*).
2. **The T-shaped A (glyphs 11, 24)** is read as A (⌟ with the horizontal drawn a little high).
   Shape alone is not decisive; the reading rests on "ALL HEIL" and "FAREN" and on the plain ⌟ = A
   at glyph 28 in the same word "RAD".
3. **Stray marks**: a small dot just outside the lower-left corner of glyph 27 (⊐) and an ink blot
   above the top bar of glyph 4 (⌝). Both lie outside the cell, so they are not read as
   cell-dots (which would give M and P and no words). Disclosed reading choice.
4. **GRUS**: the last word has four signs, G R U S, followed by a long vertical stroke (end mark,
   like the other dividers). Read literally as "GRUS" = *Gruß*; no second S is restored.
5. Orientation: the 180° turn is supported by the descending commas, by the signs standing on the
   frame line, and by the fact that the same key then yields German words throughout; read in the
   scan's orientation the standard key gives no words.
6. The ordinary cursive pencil writing in the margins (left, right, bottom) is plain German
   handwriting, not cipher; it was not transcribed and is not part of this claim.

## Why it is believed correct

- One textbook key, no free parameters except the orientation, turns all 28 uncancelled signs into
  six words that form a coherent German sentence: *Radfahren soll leben! All Heil! Gruß*.
- Word lengths match the writer's own dividers exactly (8+1 cancelled, 4, 5, 3, 4, 4).
- Repeated signs behave consistently: ⌞· = L six times (glyphs 18, 17, 16, 10, 9, 5: SOLL, LEBEN, ALL, HEIL), □ = E four times,
  □· = N twice, ⌜· = R three times, V = S twice.
- The content (cyclists' greeting) fits a 1901 Bavarian picture postcard.

## Credit

The scans, metadata and the 29-position geometry boxes (`work/transcript.json`), plus the earlier
custom-alphabet experiments, were produced by the earlier OpenAI GPT solver (GPT-6 Astra /
GPT-6.1 Sol), which did not reach a reading. The 180° orientation, the identification of the
T-shaped sign as A, the transcription verification on enlarged crops and the decipherment were
done by Claude Opus 5.5 on 2026-10-29/30.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent, 2026-10-30) gave the verdict **ACCEPT**; its independent
transcription and decode agreed in all 29 positions. All six findings are minor. Response by
Claude Opus 5.5, 2026-10-30:

1. **T-shaped A (glyphs 11, 24).** Agreed, and addressed in the report: new script
   `work/report_figs.py` makes `work/report-glyphs.png`, 6x tiles of glyphs 28, 24, 11 (and 27, 4,
   26) rotated 180°, so a reader can compare the plain ⌟ of glyph 28 with the two sideways-T forms.
   The reading A is unchanged and stays listed as Uncertainty 2.
2. **Cancelled glyph 26.** No change; the wording ("not read; an H is only a guess") is kept. Its tile
   is in `work/report-glyphs.png`.
3. **Stray dots at 27 and 4.** No change in reading; both tiles are in `work/report-glyphs.png` and the
   point is kept in the report.
4. **L count.** Fixed: "⌞· = L six times (glyphs 18, 17, 16, 10, 9, 5)" in *Why it is believed
   correct*. Re-ran `python3 -I ciphers/hcp-1021/work/solve_1021.py`: output unchanged,
   `RAD[x]FAREN SOLL LEBEN ALL HEIL GRUS`.
5. **"All Heil" unsourced.** No source in hand to cite without a fresh search; the report keeps it
   explicitly labelled as general historical knowledge (cyclists' clubs' greeting around 1900) and
   notes the reading does not depend on it — the words decode from the key alone.
6. **Language and register type.** The report states the language as German (portal: Unknown). The
   register entry uses type "Pigpen", as for the standard-Pigpen card hcp-1476/1497.

The decoded text is unchanged by the review.
