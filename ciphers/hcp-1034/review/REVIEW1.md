ACCEPT

# Review 1 — hcp-1034 (Münster to Bremen, 5 Sept 1904)

Reviewer: Claude Opus 5.5, 2026-11-03. The solver was also Claude Opus 5.5, so this is the same model checking its own work. I worked only from the scans and my own crops.

## What I verified and how

1. **The solver's command.** I ran `python3 -I ciphers/hcp-1034/work/decode.py` from the repo root. All four SHA-256 checks print OK. The output matches the plaintext claimed in SOLUTION.md character for character:
   `Indem ich mich fur deineliebe auf merk sam keit herzlich bedan. ke, ver bleibe ich mit Grusz und kusz dein tr. fritz.`
2. **An independent decode.** `review/work/verify.py` uses my own names for the glyphs and my own row transcription, which I read from the crops listed under point 3. It decodes to the same text. It also keeps the hyphen in "herzlich-bedan." (finding 1) and marks the one forced sign in "auf" as `[c->u]`. I count 92 cipher signs, the same as the solver. The key is consistent:
   - Every glyph class maps to exactly one letter.
   - Four letters have two drawn forms: i (upward and downward dotted triangle), e (hollow and inked D), b (N zigzag and V with a hook) and k (c with a hook tick, and a circle with a bar and a tick). The tick is the shared feature of both k forms.
   - No glyph is given two letters, except the single oval in "auf".
3. **Transcription against the pixels.** I made my own crops at 2–3x from `work/hires/..._pic.jpg`: `review/work/A1, A2, B1b, B2, Bsp, C1, C2, DE.png`. I checked every row sign by sign.
   - Row A: "Indem ich mich für deine liebe". The u in "für" has a mark over it (ü). The signs of "liebe" are all visible to the left of the printed figure.
   - Row B: "auf merk sam keit herzlich-bedan." The repeated first and last sign in "herzlich" (the L with a hook) is clear.
   - Spire sign: a circle with a bar and a tick, the same form as the k in "keit" and "Kuß". Reading it as an abandoned "k" is plausible and does not change the text.
   - Row C: "ke, ver bleibe ich mit Gruß und". Row D: "Kuß". Row E: "dein tr. Fritz."
   - The long diagonal strokes that cross rows B and C are descenders of the Kurrent lines above. They are not cipher signs.
4. **Plain Kurrent text.** I read it independently from crops p1, p1r, p2, p2r and p3: "Liebe Tilly! Du mußt heute schon mit einer Karte zu-/frieden sein, da es schon sehr spät ge-/worden ist, und du doch / morgen einen Brief bekommst." Dated "Münster, d. 5/9 1904." This agrees with the solver's reading, and no clause is left unread.
5. **Address side.** "Fräulein Mathilde Meyer in Bremen Caprivi Str. 6". The stamp is a 5 Pf Germania with the cancel MÜNSTER 5.9.04, and the arrival mark is BREMEN 6.9.04. I found no cipher on this side. Tilly is a pet form of Mathilde, the 1904 date fits the stamp and the cancels, and the picture of Handorf near Münster fits the place.
6. **Language.** The cipher text is a fluent, conventional letter closing in German of 1904 ("Indem ich mich ... herzlich bedanke, verbleibe ich mit Gruß und Kuß dein treuer ..."). It continues the plain text sensibly. Writing ß as s+z (Kurrent ſʒ) is period practice, and it independently confirms the values s and z.
7. **Sources.** The portal shows Not solved with no attached solution. SOLUTION.md says so, and I found no sign that a published solution was used.

## Findings

1. **minor – the hyphen in row B is not transcribed.** A short horizontal dash joins the last sign of "herzlich" to the first sign of "bedan." (crop B2.png). It is not in the transcription in SOLUTION.md or in decode.py. It is punctuation only and changes no letter, but the transcription should show it, or note it as a joining stroke.
2. **minor – U1 is correctly disclosed, and the pixels support the solver's caution.** The second sign of "auf" is a closed narrow oval, the same as the c in every "ich". The writer's u ("für", "Gruß", "und", "Kuß") is clearly open at the top. So this really is a c-glyph used where u is needed: a writer's slip or a sloppy u. Reading it as u rests on word sense alone, and SOLUTION.md says so. No change is needed, but the report should give the open-top/closed-oval contrast as the evidence.
3. **minor – the stamp has not been checked for steganography.** The address-side scan cannot show what is under the stamp. SOLUTION.md says this, which is correct. Hidden writing under the stamp is common on other series in this collection, and the human relayed a note about it for the Jolánka series. The report should say plainly that a hidden message under the stamp cannot be excluded from the scan alone. The register type stays MASC, because nothing on the visible card shows steganography.

## What I could not verify

- Whether there is writing under the stamp. The physical card would be needed.
- Whether the dark figure at the end of row A (U3) covers a sign. Its tone matches the printed picture, and the sentence is complete without one.
- Who "Fritz" was. The scans give no surname.

## Verdict

ACCEPT. The reading is correct, the key is consistent and covers all 92 cipher signs, and the plain Kurrent part is fully read. Only the minor transcription and reporting points above remain. Register type: MASC.
