ACCEPT

# hcp-1195 – review round 1 (Claude Opus 5.5, reviewer, 2026-11-03)

Verdict: ACCEPT. The reading is correct: a home-made rune-style monoalphabetic substitution with German plaintext. Every
sign on the card decodes with one table, and the text is coherent period German. It contains the Goethe line "Langen und
bangen in schwebender Pein" (Klärchen's song, Egmont). The remaining points are minor: one translation error and a few
calls that rest on word sense and should say so plainly.

## What I verified and how

1. **Solver's command.** I ran `python3 -I ciphers/hcp-1195/work/decode.py`. All four SHA-256 checks print OK. Its output
   matches the 12-line plaintext in SOLUTION.md word for word.
2. **Independent decoder.** I wrote `review/work/indep_decode.py`. It has no word-level fix tables and prints each
   homograph as a set: (AO) and (FV). I ran it on `work/transcription.txt`. It finds 29 sign codes and 198 tokens, and every
   token is mapped; no sign is left over. Each word has exactly one German reading among the homograph choices (for example
   (FV)(AO)RIGE gives only VORIGE, and (AO)NTW(AO)RT gives only ANTWORT). So the solver's RESOLVE/FIX tables make no hidden
   choices. Recurring words decode the same each time: BRIEF twice (lines 1 and 10), MORGEN twice (line 9), and the
   endings -END/-ENDE.
3. **Transcription against the scan.** I compared it with the hires original `work/hires/..._pic.jpg` (3468x2298), using my
   own crops in `review/work/` (L01–L12 for each line, halves at 2x, details at 3–4x):
   - Line 1 HERZLICHST (L01_hz.png): ↓, then a hook L, then a Γ with a dot inside, then the asterisk H overlapping the
     header flourish, then the bolt S and ↑. The Γ-with-dot sign occurs only here. Its value "IC" is inferred from the
     word, as the solver discloses.
   - Line 2 GLIECHZIETIG (L02_gl.png): a dotted one-twig G, the hook L, I, E, H marked "2" and the angle C marked with a
     "1"-stroke, then ↓ I E ↑ I and a dotted G. The reorder marks are real and are applied correctly.
   - Line 3 (L03_a/b.png), lines 4–5 (L04_*, L05_bang.png, L05_sch.png), line 6, lines 7–10 and line 12: I checked each
     sign in order. All agree with the transcription.
   - E against H: the dotted E in BANGEND is a stem with one slanted crossbar and dots. It is clearly different from the
     three-armed asterisk H in SCHEBEN.
   - E against K (L08_meine.png, L03_karte.png): K is a one-sided twig, as in KARTE. E (the Y-form) has a slanted bar that
     crosses the stem. In MEINE the left part of the bar is faint, but it is there.
   - B against dotted B (P in PIEN) and plain against dotted Π (U/Ü in FÜR, ÜBER, FÜRCHTETE) are visible.
4. **Disclosed restorations.** I judged each one on the pixels (see the findings): the line-8 overwritten sign with its
   star and the footnote (foot.png), the first sign of LANGEND (L04_lang.png), and the two S of KUSS under the collector
   stamp (L11_b.png, kuss_thr.png).
5. **Context.** 25 Feb 1900 was a Sunday (Python `datetime`), so "vorige Sonntagskarte" fits. On the address side, the
   postmark TEPL and the Wien arrival mark 26.2.00 fit the date "Tepl 25/II 00" written on the picture side. The address
   side reads Herrn Anton Schönfelder, Wien IV, Favoritenstrasse 64, Th. 29. It is plain handwriting with no cipher.
6. **Sister card hcp-1194.** It is read only. It has the same sender and recipient, the same alphabet, and was solved
   independently. It agrees on H, E, R, Z, D, N, K, F, B, I, T, L, S, M, and also on the ᛅ sign carrying A. Its signature
   reads "RASA", which under this card's A/O homograph could well be ROSA. That supports the A/O merger found here. Note
   that 1194 reads G as a looped or flagged sign, while this card uses a dotted K for G. This does not contradict 1195, but
   whoever finishes both cards should compare the two.
7. **Published solution.** None is referenced. The portal status is Not solved and no solution is attached. Nothing in the
   solver's files suggests an undisclosed source.

## Findings

1. **minor – Slovak translation has the genders wrong.** The card is addressed to "Herrn Anton Schönfelder", so the
   recipient is male, yet the Slovak says "aby si mi odpustila" (feminine). The writer signs "Dein Lieb" on a love card.
   The sister card's signature reads Rasa/Rosa, which points to a female writer, yet the Slovak has "obával som sa"
   (masculine).
   - Fix: "aby si mi odpustil", and either "obávala som sa" with a note that the writer is probably female, or a
     gender-neutral wording.
   - The English translation is fine.
2. **minor – the L of LANGEND rests on word sense.** At 4x (L04_lang.png) the first sign of LANGEND does not have the
   usual hook-L shape seen in LIEBEN, GLIECH, FOLGT and LIEB. The dark stroke is a stem with a diagonal running down to the
   right, with a dot at the upper right. There are erased traces on the left. This looks closer to the λ-type N than to L.
   - SOLUTION.md uncertainty 6 says only that it is "written over faint traces".
   - It should say plainly that the letter L is supplied by the Goethe line and the word sense, not by the sign's shape.
3. **minor – the two S of KUSS cannot be confirmed from the pixels.** The collector stamp's grey lettering ("Schrödel")
   lies over both signs. Even thresholding (kuss_thr.png) does not separate the pencil strokes from the stamp ink. K and U
   are clear. SS is very probable from "Mit Kuss".
   - Uncertainty 4 says the dark pencil parts "fit the lightning S". That is slightly too strong: they are compatible
     with it, nothing more.
   - It should call SS a restoration from context.
4. **minor – the footnote gloss.** At 3x (foot.png) the footnote reads: asterisk, "=", then a Kurrent letter, then a full
   stop. The letter has a lead-in, one tall down-stroke and a w-like connector ending in a short stroke. No i-dot can be
   seen clearly; the short final stroke could be a displaced one. So "i" is possible but not certain.
   - The solver already says that MEINE is the only sense, which is right.
   - The text should say that the gloss reading "i" rests partly on MEINE, and not use the gloss as independent proof.
5. **minor – faint signs under the stamp in ANTWORT and MORGEN.** In line 7, the R and the final T of ANTWORT lie under
   the stamp ring (L07_ant.png). They are faint but compatible. In line 9, the last N of the second MORGEN lies at the
   stamp edge. These calls are fine but should be listed with the KUSS signs as "under the stamp, compatible only".
6. **minor – distinctions resting on faint strokes.** The E against K difference (a bar crossing the stem, or a one-sided
   twig) is a real distinction on this card, and the transcription applies it consistently. But in MEINE (final sign) and
   FÜRCHTETE the left half of the bar is faint. The list of context calls should mention it beside the A/O and F/V
   homographs.

There is no blocker or major finding. These are documentation fixes for the report and SOLUTION.md. None of them changes
the plaintext.

## Steganography and hidden writing

- **Picture side.** The image, the margins, the caption "Bergbleameln" and the edges carry nothing besides the cipher
  text, the header date and the footnote.
- **Under the stamp.** The 5 Heller stamp sits on the address side, and nothing beneath it can be seen on the scan, as the
  solver discloses.
- **Register type.** No hidden message was found, so if this goes to the register the type is plain MASC, not
  "MASC + Steganography". The stego note in the user's message concerns the Jolánka series, not this card.
- **Register entry.** 1195 is not in register-exclusions.json, so an entry is allowed once the card is FINAL.

## What I could not verify

- Whether anything is written under the affixed stamp.
- The exact pencil shape of the two S signs in KUSS, and of the faint R and T of ANTWORT, under the collector stamp.
- The precise Kurrent letter of the footnote gloss.
- How "IC" is carried by the single Γ-with-dot sign in HERZLICHST: as a ligature, or as C with I left out.
- A web search for a published solution. I did not repeat it. The solver reports none, and the portal attaches none.

Reviewer files: `review/work/indep_decode.py` and the crops `review/work/L*.png`, `foot.png`, `kuss_thr.png`,
`cmp_K_Ey.png`, `pic_overview.png`, `adr_overview.png`.
