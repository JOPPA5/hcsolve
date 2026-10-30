REVISE

# Review 1 – hcp-1565 (pc_hcp_246), Anna Tichá / Pepouš family card, 19 Feb 1903

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. The solver's key and overall reading hold, and the five overprinted margin spans read in the "Completion and handover" section are confirmed on the pixels. But the single command fails. The completions were never carried into the transcription, the literal or the command. I also found four ordinary signs misread in rows nobody had re-examined, and three of them change words of the plaintext. The fixes are concrete, so the verdict is REVISE, not REJECT.

## What I verified and how

1. **The single command.** I ran `python3 ciphers/hcp-1565/work/decode.py` from the repo root (and from the cipher directory). Both runs **failed**:
   `AssertionError: ('hash mismatch', 'ciphers/hcp-1565/NOTES.md')` (exit 1). The 2026-10-29 completion appended to NOTES.md and SOLUTION.md without refreshing `work/manifest.json`. The script also only audits `work/transcription.json`, which still holds the six `<UNK>` spans. Even after a hash fix it would not produce the plaintext claimed in the completion section.
2. **Independent decoder.** I wrote `review/work/decode_review.py`, with the key typed from the SOLUTION.md table rather than from `work/key.json`. I ran it on the solver's `work/transcription.txt` and on my own corrected transcription `review/work/transcription-reviewer.txt`. On the solver's file it reproduces the solver's literal exactly. The key is a consistent 22-class monoalphabetic substitution with a marked CH sign, and all 22 classes occur. Every resolved sign maps, with no leftovers apart from the opaque `<UNK>` markers.
3. **Transcription against the scan.** I rotated `source/picture.jpg` 90° counter-clockwise (`review/work/ccw.png`) and made LANCZOS and NEAREST enlargements at 3–12x, all in `review/work/`:
   - every completion span (U01–U06): `left4x.png`, `m01_start.png`, `m04_start.png`, `m05_start.png`, `m04_mid5x.png`, `m05_end6x.png`
   - every margin row: `margin2x.png`, `m03_kvetink.png`, `kvetinku_end12x.png`, `m03_blaz6x.png`
   - all four bottom rows in full: `bot_left3x.png`, `bot_right3x.png`, `h01_dik6x.png`, `h01_drahe6x.png`, `h02_zpus7x.png`, `h02_vasnive6x.png`, `h04_douf6x.png`, `h04_f10x.png`

   Apart from the signs in findings 2–5, H01–H04 and M01–M05 match `work/transcription.txt` sign by sign.
4. **Language and context.** This is natural Czech from about 1903, a love letter from Pepouš to "Anunka" (Anna Tichá, teacher in Žirovnice). It fits the family. The stavitelský věneček at the Hotel Monopol is plausible period social life. The handwritten date 19./II.1903 agrees with the portal date 1903-02-19.
5. **Sources and credit.** The key is the published family key (HCP1520, Maxim Egorov / Cipher-Atelier). This is disclosed as known-key transfer. The portal attaches no solution for this card.

### My corrected reading (literal, from review/work/transcription-reviewer.txt)

```
H01 vrely pac a pusu za drahe roztomile psanko tvoje, jehoz obsah mne velice oblazil.
H02 skoda, ze te nemohu za ne vasnive zpusovati? odpovim dopisem dle moznosti co nej-
H03 drive: mam jiti pristi tyden do stavitelskeho venecku v hotelu monopolu. obedvam
H04 s nekolika cleny vyboru, kteri mne dutklive zvou. douvam vsak, ze se venecku vyhnu.
M01 posilam amorka, aby sdelil me anunce,
M02 ze ji mam vasnive rad a aby pilne
M03 zaleval kvetinku nasi blazici lasky.
M04 tisic. pozdravu a dlouhych pus posila
M05 vecne tvuj pepou♡.
```

## Findings

1. **Major: the single command fails and does not produce the claimed plaintext.**
   - `decode.py` aborts on the NOTES.md hash (see item 1 above).
   - Its literal still contains `<UNK:U01>`…`<UNK:U06>`, while the completion section claims a complete reading.
   - `work/transcription.json`, `transcription.txt`, `literal-czech.txt`, the `<!-- literal-start -->` block and the manifest all need updating to the completed and corrected transcription. The command must then be re-run so that it passes.
2. **Major: H01 word 2 is `b6s` = PAC, not `t4g` = DIK.**
   - In `h01_dik6x.png` the word is a tall "b" with a bowl, then a clear "6", then the small ı/o-shaped sign.
   - The "b" is the same shape as the first sign of `b2c2` (pusu). It has none of the crossbar of the `t` in `th6r5` (`h01_drahe6x.png`).
   - The "6" is the same shape as the standalone "6" (= a) that follows.
   - The last sign is the small s-class sign seen in `f584s5` (velice).
   - The text reads "Vřelý **pac** a pusu", the common Czech "pac a pusu" ("a paw/handshake and a kiss"). "Dík" was supplied from context, and three of its three signs disagree with the pixels.
3. **Major: H02 `q82c3f6d4` (ZLUSOVATI) is `qb2c3f6d4` = ZPUSOVATI.**
   - In `h02_zpus7x.png` the second sign has an ascender and a bowl, i.e. "b" (P), partly under the watermark band. It is not the closed "8" (L).
   - "zpusovati" (to cover with kisses, from pusa) is a real colloquial verb and makes good sense: "Škoda, že Tě nemohu za ně vášnivě zpusovati".
   - This removes the "unclear word". The completion section's editorial "zlíbati" is an invented substitution and must go.
4. **Major: M03 `g f5d4mg5` is `gf5d4mg2` = KVĚTINKU.**
   - The last sign (`m03_kvetink.png`, `kvetinku_end12x.png`) has the "2" (U) form, the same as in `b2c2` and `f32`. It is not the flat-topped "5" seen two signs earlier in the same word.
   - No word space separates g from f5.
   - The phrase is "aby pilně zaléval květinku naší blažící lásky", accusative and fully grammatical. The "k vetinke / KVETINKE?" uncertainty and the "květinku split across the space" speculation are both resolved by the pixels.
5. **Major (pixel decides the disclosed alternative): M03 `p86q4c4` is `p86q4s4` = BLAZICI.**
   - In `m03_blaz6x.png` the sixth sign is the small ı-shaped s-class sign. It is clearly different from the round "c" in `m6c4` (naší) right before it.
   - So s → C, BLAZICI = blažící. The solver's preferred c/S reading (BLAZISI) is wrong.
   - The editorial text already says "blažící", but the literal, the transcription and the "preferred" statement contradict it.
6. **Minor: completion spans U01–U05 confirmed, and the reliance on context should be stated.**
   - U02 `q685f68` (ZALEVAL), U03 final `s` (TISIC), U04 `b3q` (POZDRAVU, third sign the 9-like q = Z) and U05 `f5sm5` (VECNE) are legible through the postmark dots.
   - U01: of `b3c486n` (POSILAM), the first sign is a tall b-form under heavy dots, and the "c" is blackened by a stamp dot. Its shape still fits, but this span relies partly on context, and SOLUTION.md should say so.
   - U06 is a drawn heart after `b5b32` (pepou). Reading it as a pictorial final Š is reasonable editorially. It is not a cipher sign, and it should not be counted as a mapped unit.
7. **Minor: DOUVAM / editorial "Doufám".**
   - The fourth sign of `t32f6n` (`h04_f10x.png`) has a horizontal stroke through the stem at x-height. That stroke could be a crossbar (a distinct F sign) or the ligature from the preceding "2".
   - Normal V signs in this hand (`f6cm4f5`, `h02_vasnive6x.png`) show a similar lead-in stroke, so I cannot decide this at this resolution.
   - Keep the literal DOUVAM and mark "Doufám" in the editorial text as an editorial correction. The completion section currently writes "Doufám" with no flag.
8. **Minor: SOLUTION.md contradicts itself.**
   - The opening sections still say "partial… six unresolved source regions… 381 mapped units… not FINAL", and they carry "zlusovati" quoted in the editorial text and in the Slovak translation.
   - The appended completion says "complete reading" and gives a different editorial text ("zlíbati", "Doufám").
   - SOLUTION.md needs one current plaintext, one translation (the Slovak one still contains all the `<UNK>` spans), updated counts and an updated uncertainty list.
9. **Minor: a hand-off note.** `.watch.log` shows that the reviewer launch for DONE1 failed (401). This had no effect on the content, which is recorded here for completeness.

## What I could not verify

- Whether the U06 heart replaces a final "š" or is pure decoration (the editorial "Pepouš" rests on the sister cards).
- Whether the DOUVAM sign is a separate F sign (finding 7).
- The historical identity of the Hotel Monopol and the "stavitelský věneček" (the place is not named on the card).
- The postal markings on the address side, which I did not re-read. They are not cipher text.
