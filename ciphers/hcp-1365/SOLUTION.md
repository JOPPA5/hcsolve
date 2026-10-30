# HCP 1365 / pc_hcp_46 — Caesar (+1) love postcard, July 1907

Status: **whole message read; review 1 verdict ACCEPT, no decoded letter changed.** Disclosed residual points below; the weakest are two letters (`w` and the second `f`) of the overwritten word `gpsfwfs`.

## Origin

HC Portal cryptogram 1365 (`pc_hcp_46`), portal status *Not solved*, language Unknown, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). Picture side: printed view "West Park Promenade and Prospect Hotel, Harrogate", no cipher. Address side (Boots Cash Chemists "Pelham" Series): halfpenny Edward VII stamp, postmark WIMBORNE / 10 AM? / JY 22 / 07, addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (portal spelling "W. Abboú"). 22 July 1907 was a Monday, so the plain heading "Sunday" fits a card written the day before and posted next morning. Same writer and address as the accepted Caesar cards hcp-1386…1407 (for example hcp-1386, also postmarked Wimborne). No published solution of this card was found or used.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the next letter of the alphabet; decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "G. H. Sunday." is ordinary writing. `&` and the initials `M. L.` (twice) are kept literal, as the initials group is on sister cards.

## Transcription and plaintext (all ciphertext on the card)

Message is on the left of the address side; turn the card 90° counter-clockwise (`work/reading.png`).

| Ciphertext | Literal plaintext |
|---|---|
| Nz Pxo M. L. Cpz. | MY OWN [M.] [L.] BOY. |
| J. bn. Tpssz up | I. AM. SORRY TO |
| ifbs zpv. bsf Opu. | HEAR YOU. ARE NOT. |
| xfmm. Nboz | WELL. MANY |
| uibolt. gps. dbse. | THANKS. FOR. CARD. |
| & gpsfwfs. zpvs | & FOREVER. YOUR |
| Pxo. M. L. Hjsm. | OWN. [M.] [L.] GIRL. |

70 enciphered letters; 4 initial letters and `&` kept literal.

English (the plaintext language): *"My own M. L. boy, I am sorry to hear you are not well. Many thanks for card, & forever your own M. L. girl."*

Slovak: *„Môj vlastný M. L. chlapec, je mi ľúto, že počujem, že sa necítiš dobre. Veľká vďaka za pohľadnicu, a navždy tvoje vlastné M. L. dievča."*

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1365/work/decode.py
```

It checks the SHA-256 of the two `source/` scans and the two `work/hires/` originals, decodes `work/transcription.json`, checks the inverse round trip and prints the plaintext and letter count.

## Uncertainties

1. **`gpsfwfs` = FOREVER (line 6) is the weakest word.** It is tangled and crossed by the long descenders of `gps` from the line above (`work/crops/w_mid8.png`, `w_right9.png`). Seen: g, p, s, first f with looped descender, and the final s. The `w` is not separately legible: I take it from the oval with an inner hook after the first f. The second f is a long heavy stem crossing that oval. It has **no loop**, unlike the looped f of `ifbs`, `bsf` and `xfmm`, so it is a weak match for f, not a plain form match; its top meets a descender from the line above, so this stroke's assignment to line 6 rather than line 5 is an interpretation. The card has no other `w` to compare with. FOREVER is the only word I found that fits the visible start and end and the sense; it is a contextually supported reading, not a sign-by-sign one, for those two letters. Word division (FOR EVER) cannot be determined.
2. **`Nboz` = MANY (line 4).** N, b and o are clear. The z's own top stroke, diagonal and long foot are mostly visible below a blot (`work/crops/many.png`, `review/work/z_many.png`), so z is read, not merely restored. Above it sits a heavy separate bar, at the point where the gray descender of `Opu` from the line above lands. That bar is unexplained. The dot after N is the blotted foot of N's second leg, not punctuation.
3. **`uibolt` = THANKS (line 5), final `t`.** Only a short faint upstroke rises from the foot of the l, with no crossbar and a blot beside it (`review/work/z_thanks.png`). The sign is not independently readable; the word forces it.
4. **`dbse` = CARD (line 5), final `e`.** The sign is a compact cross shape, a bar over a hooked tail, not a looped e, and looks more like this writer's x (`review/work/z_cardend.png`). Ciphertext `e` occurs nowhere else on this card, so there is no control here. CARD is forced by "many thanks for" and is the spelling on sister cards (`dbse` on hcp-1392).
5. **`M. L.`** kept literal; meaning unknown. The first initial has hook, stem and two legs after it, unlike one-armed N of `Nz`, so I read M; N remains possible (sister cards write `N. & L.`, `E. L.`). If shifted they would be L. K. The second initial is a looped L, somewhat k-like.
6. **`Opu` = NOT:** O and p are joined (loop into the p stem), and the u is faint; `opu` is the only sensible reading in "are not well". Capitalisation of the O is uncertain and without significance.
7. **`Cpz` = BOY:** the capital is a looped C, as on hcp-1386; p and the z with flat foot are in ligature.
8. Heading initials G or C (hcp-1386 and 1397 discuss the same doubt). Punctuation dots follow the manuscript and are not significant. The postmark hour is hard to read.

## Why it is correct

One fixed shift turns every enciphered token into English, with long words (SORRY, and THANKS with its last letter forced) and a coherent sentence. FOREVER is not counted as evidence for the key, because two of its letters are contextual. The shift also reproduces the formulae of accepted sister cards (`Nz Pxo … Cpz`, `zpvs Pxo … Hjsm`). The hand, addressee, Wimborne postmark and date fit that correspondence. The transcription was made from enlarged crops of `work/hires/pc_hcp_46_adr.JPG`.

## Credits

Capture, transcription and decipherment: Claude Opus 5.5, 2026-10-30. Key family and formulae taken as hypotheses from the accepted sister cards (hcp-1386 and others), then tested on this card. No earlier work on this number.

## Response to review 1

Verdict ACCEPT, five minor findings. All were addressed in this file; none changes a decoded letter, so `work/transcription.json` and `work/decode.py` are unchanged. I looked at the reviewer's crops (`z_fv`, `z_many`, `z_thanks`, `z_cardend`) and agree with each finding. `python3 -I ciphers/hcp-1365/work/decode.py` re-run: 4 hashes OK, 70 enciphered letters, same output.

- **F1 (FOREVER, unlooped stem): accepted.** Uncertainty 1 now says the stem has no loop, that the card offers no `w` for comparison, and that FOR EVER cannot be excluded. The word stays labelled contextual. Its reading is unchanged because no better word fits.
- **F2 (`Nboz`, z): accepted.** Uncertainty 2 now says the z is largely visible under the blot and that the heavy bar is a separate, unexplained stroke.
- **F3 (`uibolt`, final t): accepted.** Now listed as uncertainty 3.
- **F4 (`dbse`, final e): accepted.** Now listed as uncertainty 4.
- **F5 (FOREVER as evidence): accepted.** Removed from the evidence under "Why it is correct", where it is now expressly not counted.

The numbering of the other uncertainties moved accordingly.
