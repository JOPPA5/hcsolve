ACCEPT

# Review 1 — hcp-1101 (Basel, 11 II 1898, to Marie Müller)

Reviewer: Claude Opus 5.5, 2026-11-03.

## What I verified and how

1. **Hashes and command.** I ran the single command from SOLUTION.md
   (`.../python3 -I ciphers/hcp-1101/work/decode.py`). All four SHA-256 checks print OK. I also computed them with
   `shasum -a 256` and they match SOURCES.md. The script writes `work/redfilter.png` and prints the six hidden lines
   plus the open text, which are exactly the lines in SOLUTION.md.
2. **Independent filter.** `review/work/verify.py` is my own script. It uses a different crop and a hard
   threshold on the R channel (below 110 becomes black, above 190 becomes white). Its output is `review/work/rf_all.png`, with enlargements
   `z_l12a.png` and `z_l12b.png` at 3x. In this view the red lattice, the crosses and the fake loops vanish completely, and the
   black ink reads continuously. I read every line on my own before comparing it with the solver's text:
   - `Weñ der früche Morgen lächelt`: the nasal bar over n is clear. "früche" really has f-r-ü-c-h-e at 3x, and the solver
     discloses it.
   - `Weñ des Abends Kühle fächelt`: "Abends" has a lower-case-style a. "Kühle" ends in an e with a loop, and nothing follows it.
   - `Immer-immer denk ich dein`: the hyphen is visible.
   - `In der Mitternächte Hülle`: there is a stray slash after "Hülle", which is a pen stroke and not a letter.
   - `Selbst in meiner Träume Stille`
   - `Mischt dein schönes Bild sich ein.`
   My reading agrees with the solver's word for word, and none of it rests on context.
3. **Open text (colour crops `z_top.png`, `z_bottom.png`).** "11/II/98." and "das isch suber" are confirmed. "Mit freundl. Gruss" is
   confirmed, with "Mit" overwritten (an extra t/f stroke), as the solver disclosed. The initials "H. B." sit in a hand-drawn oval, and the overlapping grey circle
   is the Schrödel/HCPortal collection stamp.
4. **Address side.** Pre-printed "Deutsche Reichspost / Postkarte" form, Swiss Helvetia 5 c stamp, Basel postmark 11 II.
   The address reads "Fräulein Marie Müller, Basel, Dornacherstrasse 2?4" (the house number is partly under the collection stamp). The stamp edges show
   no writing. As with the solver, I cannot lift the stamp.
5. **Language and context.** The six lines are a correct German trochaic verse with the rhymes lächelt/fächelt,
   Hülle/Stille and dein/ein. "isch suber" is genuine Swiss German. The date matches the postmark, and the Basel address matches the Swiss stamp.
6. **Type.** There is no substitution: the concealment is a red lattice drawn over black ink, and it is read through red glass.
   `Steganography` is an allowed register label and it is correct here. `MASC + Steganography` would be wrong, because nothing is
   enciphered. The human's note about stamp-box steganography on the Jolánka series does not change this card.
7. **Published solution.** My web search for the opening lines found no source of the verse and no published solution of this card,
   which agrees with the solver.

## Findings

1. (minor) The address side is a German "Deutsche Reichspost" printed card form that was franked and posted in Switzerland. The postcard publisher
   is Vogel, Leipzig, and the view on the picture side is credited to "R. Loës ph." SOLUTION.md does not mention the German form.
   It is worth one line in the report as context; it does not affect the reading.
2. (minor) "früche": the letters are certainly there. The solver's explanation (a slip for "frühe") is reasonable, and it is disclosed as resting on word
   sense. A dialect spelling is also possible: Swiss "früech" for früh. The solver could note this as an alternative, but the meaning is unchanged.
3. (minor) The stray slash after "Hülle" (line 4) and the hyphen in "Immer-immer" are pen marks. The solver keeps the hyphen and drops the
   slash, which is fine. The report could mention the slash in one line for completeness.

## What I could not verify

- Whether anything is written under the stamp, because it cannot be lifted from the scan.
- The literary source of the verse. Neither the solver nor I found one.
- The identity of "H. B." and the full house number.
