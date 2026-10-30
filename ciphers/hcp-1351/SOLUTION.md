# HCP 1351 / pc_hcp_32 — Caesar −1 English love postcard, 16 Feb 1907

Status: **whole message read; review 1 verdict ACCEPT.** 69 of 70 letters are read on form, 1 on form plus context (Uncertainties 1).

## Origin

HC Portal cryptogram 1351 (`pc_hcp_32`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). Picture side: printed "Wimborne Minster, Nave East", no handwriting. Address side: Frith's Series card, halfpenny Edward VII stamp, postmark (WIM)BORNE, 1 PM, FE 16 07, agreeing with the portal date 1907-02-16, which was a Saturday, matching the plain heading "G. H. Saturday". Addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon (portal spelling "W. Abboú", left unchanged in metadata). The message runs across the left half (rotate 90° anticlockwise: `work/crops/reading.png`). The grey disc and building logo are a scanner overlay, not part of the card. No published solution of this card was found or used.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the next letter of the alphabet. Decrypt by subtracting one. The key was taken as a hypothesis from sister cards of the same couple (hcp-1386 and others; `Nz` = MY, `Hjsm` = GIRL, signature `Mpp` = LOO on hcp-1398) and holds on every word here. One sign, the second of `Xjmm`, rests on form plus context (Uncertainties 1); all others are read on form.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Plaintext |
|---|---|
| G. H. Saturday *(plain, underlined)* | G. H. Saturday |
| Nz. Efbsftu Cpz. | MY. DEAREST BOY. |
| uxfmwf. Xfflt. up ebz. | TWELVE. WEEKS. TO DAY. |
| uijoht. Xjmm. Cf. | THINGS. WILL. BE. |
| Mppljoh. Vq. | LOOKING. UP. |
| Gspn. Zpvs. Mpwjoh. | FROM. YOUR. LOVING. |
| Hjsm. Mpp. | GIRL. LOO. |

70 enciphered letters, all under one key. The dots are the writer's habit and are not significant.

English (the plaintext language; the portal lists Unknown): *"G. H. Saturday. My dearest Boy, twelve weeks to-day things will be looking up. From your loving Girl, Loo."*

Slovak: *„G. H. sobota. Môj najdrahší chlapče, o dvanásť týždňov odo dneška sa veci obrátia k lepšiemu. Od tvojho milujúceho dievčaťa, Loo.“*

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1351/work/decode.py
```

It checks the SHA-256 of the two `source/` scans and the two `work/hires/` originals, decodes `work/transcription.json`, checks the inverse round trip and prints the table above.

## Uncertainties

1. **Second sign of `Xjmm`** (`work/crops/will_second_sign.png`). A looped descender with its return stroke is visible, matching this writer's j, but the tails of `Xfflt` from the line above run into exactly this spot and I cannot confirm the dot. There is only a dark junction where f's left eye would stand, so f cannot be strictly excluded. `Xfmm` = WELL makes no sense here; j = WILL is the only reading that gives a sentence. Read as j on context plus the descender form.
2. **Word division and meaning.** `up ebz` is written as two words, read "to-day". "Twelve weeks to-day" is taken as twelve weeks from the day of writing, which would be Saturday 11 May 1907 (computed), perhaps a wedding or reunion date. Nothing on the card says what the event is, and "twelve weeks ago to-day" is not what is written.
3. **`Mpp` = LOO.** The first p here and in `Mppljoh` has a small eye to the right of the stem, as the p in `Zpvs` and `Mpwjoh`, whereas f has its eye to the left (`work/crops/f_vs_p.png`, `signature_Mpp.png`). The capital has three downstrokes, as the M of `Mpwjoh` on this card, where the N of `Nz` has two, so it is M and not N. `Mppljoh` needs the same pair of signs for the checked word LOOKING. Same signature as hcp-1398. Whether "Loo" is a pet name, and for what, is not established.
4. **Heading initials** G. H. are taken as plain by inference, not tested on their own: they stand in the same line as the plain "Saturday", Caesar −1 would give the meaningless F. G., and hcp-1352 has the same form, "G. H. Friday". Their meaning is unexplained; sister cards vary between C. and G. readings. The pencil "3" at top left of the address side is not in the writer's ink and is treated as a later or sequence mark, not ciphertext.

## Why it is correct

One fixed shift gives clean English for all 70 letters, including long words (DEAREST, TWELVE, THINGS, LOOKING, LOVING), with no change to the key. 69 letters are read on form and 1, the second sign of `Xjmm`, on form plus context. The formula "My dearest ... from your ... girl" and the signature LOO match accepted sister cards of the same correspondence. The plain weekday matches the postmark date, and place and recipient match the series. The sentence is one a sweetheart of 1907 could plausibly write.

## Credits

Capture by the orchestrator (Claude Opus 5.5), 2026-10-30. Transcription, decipherment and this write-up by Claude Opus 5.5 acting as solver, 2026-10-30. The shift and recurring groups come from the repo's accepted sister cards.

## Response to review 1

Verdict ACCEPT, four minor findings. No letter of the transcription or plaintext changed. `python3 -I ciphers/hcp-1351/work/decode.py` was re-run after these edits: hashes OK, same six lines, 70 letters.

1. **`Xjmm` wording: fixed.** Status, the key paragraph and "Why it is correct" now say that 69 letters are read on form and 1 on form plus context. I looked at `work/crops/will_second_sign.png` again and agree: a junction and a descender, no dot of its own. The blotch inside the loop is not claimed as the dot, since the reviewer places it over the stem of the j of `Mppljoh`.
2. **`Mpp` capital: fixed.** Uncertainties 3 now gives the M against N argument (three downstrokes against two in `Nz`).
3. **Slovak vocative: fixed.** "chlapec" is now "chlapče".
4. **G. H. as an inference: fixed.** Uncertainties 4 now states the grounds and that the initials were not tested on their own.
