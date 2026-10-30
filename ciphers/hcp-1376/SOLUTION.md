# HCP 1376 / pc_hcp_57 — Caesar (+1) love postcard, 9 Nov 1907

Status: **whole message read; review 1 verdict ACCEPT, no decoded letter changed.** Residual points are listed under Uncertainties. The largest is the first word of the sentence in rows 2-4: the letters give `Jt` = IS, while the sense needs IT.

## Origin

HC Portal cryptogram 1376 (`pc_hcp_57`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). Picture side: printed "Glastonbury Abbey looking West", no handwriting. Address side: halfpenny Edward VII stamp, postmark WIMBO[RNE] / 10 [PM?] / NO 9 / 07, which agrees with the portal date 1907-11-09; that day was a Saturday, matching the plain heading "G. H. Saturday". Addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (the portal's "W. Abboú" is a misreading; metadata left unchanged). The message is on the address side (rotate 90° counter-clockwise, `work/crops/msg.png`). The circular disc and building logo on the scans are a scanning overlay. No published solution of this card was found or used.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet; decrypt by subtracting one. Same key, hand and formulae as the FINAL sister cards hcp-1386…1407 (checked by sign comparison with `ciphers/hcp-1386/work/crops/band6.png`).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "No. 3. G. H. Saturday" is ordinary writing. `2 hrs.` is left plain by the writer. `E-L.` and `N. & L.` are abbreviations kept literal, as on the sister cards.

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Px[o] E-L. | MY. OWN [E-L.] |
| Jt. xbt. qptufe | IS. WAS. POSTED |
| 2 hrs. Cfgpsf. | 2 hrs. BEFORE. |
| dmfbsjoh. | CLEARING. |
| "Ju't. b. Nztufsz" | "IT'S. A. MYSTERY" |
| Nz. N. & L. gspn. Zpvs. | MY. [N. & L.] FROM. YOUR. |
| E-L. Hjsm. | [E-L.] GIRL. |

54 letters read and decoded, 1 restored under a blot (`[o]`), 9 kept literal.

English reading: *"My own E-L. [It] was posted 2 hrs before clearing. 'It's a mystery.' My N. & L. from your E-L. girl."*

Slovak: *„Môj vlastný E-L. [Bolo to] podané 2 hodiny pred vyberaním schránky. ‚Je to záhada.' Moje N. & L. od tvojho E-L. dievčaťa."*

"Clearing" is taken as the emptying of a post box. The sentence evidently answers a complaint that an earlier card arrived late, but that context is inferred, not on the card. The square brackets mark the emendation of the literal IS to "It" (uncertainty 1). The "10" on the postmark stands above NO; sister cards report WIMBORNE 10 PM, but the letters after 10 are not legible here, so the hour bears on the remark only as a guess.

(English is the plaintext language; the portal lists it as Unknown.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1376/work/decode.py
```

It checks the SHA-256 of the two `source/` scans and the two `work/hires/` originals, decodes every token of `work/transcription.json`, checks the inverse round trip, and prints the literal plaintext above with the letter counts.

## Uncertainties

1. **`Jt.` = IS, sense requires IT.** The second sign is a tall stroke with a hooked foot and a detached dash at upper right, certainly the same form as the final t of `xbt`, and looser kin of the joined final t of `Ju't`, which has no free hooked foot; it is not the low u of `qptufe` and `Ju't` (`work/crops/z_ju.png`, `z_xbt.png`, `z_jut.png`). The first sign has a large closed loop at the top, whereas the J of `Ju't` is a plain stroke with no loop (`review/work/z2_jt.png`, `z4_jut.png`): the two "J"s are different forms. The decoder prints the literal IS. IT is the intended sense. The word may be plain "It" left unshifted like `2 hrs.`, with the looped sign as the writer's capital I; the difference in form favours this. It may instead be a slip for `Ju`, or a half-shifted slip (I shifted to J, t left unchanged). All three come to the same sense, and the card cannot decide between them. The dash could also be a separator (it recurs after `hrs.` and in `E-L`), so the shape is the only evidence for t.
2. **`Px[o]`.** P (very large bowl, as in `Pxo` on hcp-1386) and x are read. In the place of the o stands a solid oval blot, much larger than this writer's full stops (`work/crops/z_pz.png`). I read it as an ink-filled o and restore OWN from the formula `Nz. Pxo. E. L.`; this is a disclosed restoration. If the blot is only a heavy stop, the group is an abbreviated `Px.` = OW.
3. **`hrs.`** read as plain h, r, s (`z_hrs.png`), with the numeral 2. Shifted they would give GQR, so it is taken as not enciphered.
4. **`dmfbsjoh`.** First sign: left loop plus tall stroke, read as d; a capital U-like reading gives no word. The loop `o` carries a long top stroke running into the ascender of the `h`. The j has a very long descender ending in a V-shaped foot on the long horizontal line below (`z_clearing2.png`).
5. **Non-letter marks.** A long horizontal line with an arrowhead runs under line 4, and the top of the `J` of `Ju't` touches it; its purpose is unknown. A heavy dot below line 4 sits directly above the top of the `J` of `Ju't` and is probably a dot on that J, not punctuation of line 4; a short tick to the right of `clearing` is treated as a stray mark. Neither affects the plaintext. The raised tick in `Ju't` is read as an apostrophe.
6. **`E-L.` and `N. & L.`** are not expanded; nothing on the card proves a meaning.
7. **`Zpvs.`** is partly overwritten by the descender loop of the f of `Nztufsz` The Z and the p stem are clear; p, v, s are pale and partly hidden, the v resting partly on the formula, since v and u cannot be told apart here (`z_zpvs.png`, `review/work/z5_zpvs.png`). The sign count, the general shapes and the same group on hcp-1386 fit; YOUR is not in doubt. The m of `Hjsm` is flattened, the same form as on hcp-1386 (`z_girl.png`).
8. **Heading number** after "No." reads 3, with 2 or 7 not excluded; it is not ciphertext. It may be a running number of the card, which nothing here can test. Heading initial G (not C) follows the glyph on this card and sister practice.

## Why it is correct

One fixed shift turns every enciphered token into English, including the long words POSTED, BEFORE, CLEARING and MYSTERY, the last of which has a repeated letter pattern and was not derived from any sister card. The rest of the message matches the couple's formulae on accepted sister cards ("My own E. L.", "My N. & L. from your", "E. L. girl"). The sentence is coherent and period-appropriate for postal English, and the postmark and weekday agree with the heading. The only fully legible token that does not decode to the expected word is `Jt` (point 1).

## Credits

All work on this card by Claude Opus 5.5 acting as solver, 2026-10-30. Scans captured by the orchestrator the same day. Key and formulae were compared with the sister cards hcp-1386…1407, on which earlier work is credited in their own files.

## Response to review 1

Verdict ACCEPT, six minor findings. No token, key entry or decoded letter changed; `work/transcription.json` and `work/decode.py` are untouched. The command was re-run after these edits and its output is unchanged (54 letters read, 1 restored, 9 literal; hashes OK).

1. **`Px[o]` / wording.** Fixed. The reading stays a disclosed restoration, and the reviewer's measurement (blot about 30 x 22 px, stops about 10 x 7 px) supports it. "Why it is correct" now says "the only fully legible token".
2. **Plain "It" alternative.** Agreed and added to uncertainty 1. On the crops the first sign of `Jt` has a closed loop and the J of `Ju't` has none (`review/work/z2_jt.png`, `z4_jut.png`). The looser likeness to the joined t of `Ju't` and the half-shifted slip are also stated. The transcription keeps `Jt` and the literal IS.
3. **Silent "It".** Fixed. The English and Slovak lines now bracket the emendation.
4. **Heavy dot.** Agreed. Uncertainty 5 now reads it as probably belonging to the J of `Ju't`. Plaintext unaffected.
5. **`Zpvs`.** Agreed. Uncertainty 7 is restated, including that v rests partly on the formula.
6. **Postmark.** Fixed. On `review/work/z11_pm.png` I see the 10 above NO and no legible letters after it, so it is recorded as 10 [PM?] and the context stays inferred.
