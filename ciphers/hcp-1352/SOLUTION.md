# HCP 1352 / pc_hcp_33 — Caesar −1 English postcard, 1 Feb 1907

Status: **whole message read: 97 of 97 enciphered letters, one key; review 1 verdict ACCEPT, plaintext unchanged.** Eight words need a disclosed sign-level normalisation (four of them the same a-shaped sign). See Uncertainties.

All transcription and decipherment by Claude Opus 5.5 (2026-10-30); no earlier work exists on this number. No published solution was found: the portal shows status *Not solved* with no transcription or solution attached (`SOURCES.md`, `source/metadata.md`), and the orchestrator's AI-register check of 2026-10-30 has no record for it.

## Origin

HC Portal cryptogram 1352 (`pc_hcp_33`), date 1907-02-01, language listed as Unknown. Picture side: printed "Ludlow Castle" (Valentine's Series), no handwriting. Address side: halfpenny Edward VII stamp, postmark WIMBORNE 10 PM FE 1 07; Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. The portal's "W. Abboú" is a catalogue spelling. The message runs up the left half of the address side (turn the card 90° counter-clockwise). The grey wheel over the card is the portal's watermark, not part of the card.

## Cipher and key

Monoalphabetic Caesar shift, the same key as the Abbott sister cards hcp-1386…1407 (and the hcp-1355… run): each plaintext letter is written as the **next** letter. Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading `G. H. Friday` is ordinary writing, not shifted. 1 Feb 1907 was a Friday, which agrees with the postmark. What `G. H.` means is unknown: it is kept as written, and the card gives no way to tell whether it is an abbreviation, a place or a name. If it were shifted it would be F. G., which helps no more.

## Transcription and plaintext (all ciphertext on the card)

`As seen` gives the sign shapes; `(→ …)` is the form the key is applied to, wherever the two differ.

| Line | As seen | Plaintext |
|---|---|---|
| — | G. H. Friday | (plain heading) |
| 1 | Ualf. (→ Ublf) dasf. (→ dbsf) J. Ibwf. nbef. | TAKE. CARE. I. HAVE. MADE. |
| 2 | op. njtublft. J. bn. wfsz | NO. MISTAKES. I. AM. VERY |
| 3 | nvdg. (→ nvdi) bnvtfe. xjui pvs | MUCH. AMUSED. WITH OUR |
| 4 | ofx?. (see 3 below) qmbo. Nz. mpwf. | NEW. PLAN. MY. LOVE. |
| 5 | po. a. (→ b) Qptu. dase. (→ dbse) Ipx. | ON. A. POST. CARD. HOW. |
| 6 | ojdf. uift. (→ uijt) gt. (→ jt) Tfdsfu. M.p.p. | NICE. THIS. IS. SECRET. L.O.O. |

97 enciphered letters; nothing kept literal.

**English (original language; punctuation editorial):** "G. H. Friday. Take care. I have made no mistakes. I am very much amused with our new plan. My love on a post card. How nice this is. Secret. Loo."

**Slovak:** „G. H. Piatok. Dávaj pozor. Neurobila som žiadne chyby. Veľmi ma baví náš nový plán. Moja láska na pohľadnici. Aké je to milé. Tajné. Loo."

(The Slovak uses feminine forms because the sister cards are signed "your own … girl"; this card itself does not state the writer's sex.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1352/work/decode.py
```

It checks the SHA-256 of the two `source/` images and the two `work/hires/` originals, reads the manual transcription `work/transcription.json`, decrypts every enciphered token, verifies the round trip, and prints the plaintext, the letter counts and every sign-level normalisation. Output is saved in `work/plaintext.txt`. The transcription is a manual reading of enlarged crops (`work/crops/`), not OCR.

## Uncertainties

The writer's cipher is not perfectly clean on this card. Each point below is a place where the key does not apply to the sign shape as it stands.

1. **a-shaped sign for cipher b (4 places: `Ualf`, `dasf`, `a`, `dase`).** Elsewhere b has a tall stem (`Ibwf`, `nbef`, `bn`, `bnvtfe`, `qmbo`, `njtublft`). Here the sign is a bowl with no ascender of its own, so literally "a", which would decode to Z. Either this is a short form of b, or the writer left plain A unshifted. Both give the same plaintext. In `Ualf` the bowl may instead use the right stem of the U as its stem, which would make it a true b.
2. **`nvdg` read as MUCH, and `gt` read as IS (same sign).** The last sign of `nvdg` and the first sign of `jt` have one shape: a closed top bowl and a long descender with a return loop (`review/work/cmp_g_j.jpg`). As a g it would decode to MUCF and FS. The word requires i in the first place and j in the second, and the real j of `xjui` is y-shaped, so this is not a plain j. The simpler account is that it is this writer's looped form of j, used once where i was meant: the writer's i and j signs overlap, and `nvdg` is one sign from `nvdi`. A slip of shifting H backwards (H→G) is a weaker guess. Both places are corrections by sense ("very much amused", "this is"), and neither changes the plaintext.
3. **`ofx` read as NEW.** The last sign is two crossed strokes: a slanted stem and a long, nearly flat bar. It is read as a flat x (W). It could equally be taken for a t, which would give NES, not a word. "our new plan" is the only reading found.
4. **`uift` read as THIS.** The third letter has a tall ascender and a long looped descender, which is an f shape (THES). It is taken as a long j, close to the looped sign of the next word (point 2). The i before it is dotted. This is a correction by sense.
5. **`Nz` / `njtublft` / `xjui` / `ojdf`.** Medial j is undotted and y-shaped throughout. In `njtublft` its tail ends in a blob. These are read as j because y would give X and no words.
6. **Capitals.** `Qptu` has a 2-like Q. `Tfdsfu` starts with a detached heavy bar over a curve, read as T; C or G would give no word. `bn` has an n that could be taken for u (AT), but "I am" is required by the sentence.
7. **`M.p.p.` read as the signature `Mpp` = LOO.** The p's are clear, each followed by a dot. The capital has three downstrokes (hooked first stroke, arched second, third ending in the tail; `review/work/z_M.jpg`), one more than the N of `Nz` on this card and the same as the m of `mpwf`, so it is M as it stands and needs no correction. The signature `Mpp` also stands on hcp-1398 and hcp-1353 (both FINAL) and is read on hcp-1350 and hcp-1354, which have not closed; hcp-1350 also counts three downstrokes. That Loo is a pet name is conjecture, and the dots between the letters are unusual for this signature.
8. **Meaning.** "Secret" stands as its own word with periods on both sides, so whether it qualifies the card or the plan is not determined. That "our new plan" means the cipher itself is a plausible interpretation given "I have made no mistakes" and "on a post card", but it is not established.

## Why this is believed correct

The key was not fitted to this card: it is the established Caesar −1 of the Abbott correspondence, and this card has the same recipient and the same Wimborne postmark. It turns the whole text into connected, ordinary English with no leftover noise. 89 of the 97 letters decode from the sign as labelled in the `As seen` column, and every one of the 8 normalised signs is listed above. That figure is softer than it looks: it includes signs labelled by sense where the shape allowed a choice (the 2-like Q of `Qptu`, the T of `Tfdsfu`, the y-shaped j, the n/u of `bn`; points 5 and 6). What depends on sense rather than on shape is therefore all listed. The date fits: 1 Feb 1907 was a Friday, as in the plain heading.

## Response to review 1

Verdict ACCEPT. All four findings are minor and I addressed all of them. The plaintext does not change.

1. **Final capital: fixed, I agree.** On `review/work/z_M.jpg` I count three downstrokes, so the "two humps" description was wrong. The as-seen form in `work/transcription.json` and the table is now `M.p.p.`, it is no longer a normalisation, and point 7 is rewritten. The sister statement is corrected: hcp-1353 has closed since the review and now also counts three feet, so the FINAL parallels are hcp-1398 and hcp-1353, while hcp-1350 and hcp-1354 remain open.
2. **Same sign treated two ways: fixed, I agree.** On `review/work/cmp_g_j.jpg` the first sign of `jt` and the last of `nvdg` are the same shape. The as-seen form is now `gt`, normalised to `jt`, and point 2 covers both places and prefers the reviewer's simpler account. The reviewer's figure of 7 words and 90 letters assumed finding 1 alone. With this sign added the count is again **8 words, 89 of 97 letters**, a different set from the one in DONE1.
3. **G. H.: fixed.** The Cipher and key section now states that its meaning is unknown and what a shift would give.
4. **Softness of the figure: fixed.** The final section now says that the 89 includes signs labelled by sense and points to uncertainties 5 and 6.

Re-run after the fixes: `python3 -I ciphers/hcp-1352/work/decode.py` reports hashes OK, 97 enciphered letters, the same six plaintext rows, and the 8 normalisations `Ualf, dasf, nvdg, ofx, a, dase, uift, gt`. `work/plaintext.txt` is refreshed.
