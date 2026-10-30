# HCP 1380 / pc_hcp_61 — Caesar (+1) love postcard, 6 April 1907

Status: **whole message read; review 1 verdict ACCEPT, closed (FINAL).** The ampersand is literal. See the response to review 1 at the end.

## Origin

HC Portal cryptogram 1380 (`pc_hcp_61`), portal status *Not solved*, no attached transcription or solution; language listed as Unknown (it is English). Picture side: "Margate, Lifeboat Memorial", no cipher. Address side: halfpenny Edward VII stamp, postmark WIM[BORNE], 10 PM, AP 6 07 (portal date 1907-04-06, a Saturday, matching the plain heading "Sat: afternoon"). Addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon (portal spelling "W. Abboú"). The message is in the left half, written sideways (rotate 90° counter-clockwise, `work/crops/msg.jpg`). The pencil "(10)" at the top is not message text. No published solution of this card was found or used.

Same recipient, postmark town and key as the accepted Caesar cards hcp-1386…1407; the key was tested on this card, not assumed: it decodes every token.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet; decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

"Sat: afternoon" and the address are ordinary writing. The "&" is left unshifted (same sign on hcp-1386 and hcp-1403).

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Efbsftu. J. bn. | MY. DEAREST. I. AM. |
| wfsz. Tpssz bcpvu | VERY. SORRY ABOUT |
| ofxt. Jo. dpef. &. | NEWS. IN. CODE. &. |
| ipqf Zpv. xjmm | HOPE YOU. WILL |
| ublf. hsfbu dbsf | TAKE. GREAT CARE |
| "Cz. wfsz. tqfdjbm | "BY. VERY. SPECIAL |
| Sfrvftu." Zpvs. pxo | REQUEST." YOUR. OWN |
| mpwjoh. Hjsm. | LOVING. GIRL. |

97 enciphered letters, all decoded by the one key. "Cz wfsz tqfdjbm Sfrvftu" is in quotation marks and underlined by the writer.

English: *My dearest, I am very sorry about news in code & hope you will take great care, "by very special request". Your own loving girl.*

Slovak: *Môj najdrahší, veľmi ma mrzí tá správa v šifre a dúfam, že si budeš veľmi dávať pozor, „na veľmi zvláštnu žiadosť". Tvoje vlastné milujúce dievča.*

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1380/work/decode.py
```

It checks the SHA-256 of the two `source/` scans and the two originals in `work/hires/`, decodes every token of `work/transcription.json`, checks the inverse round trip, and prints the table and the reading.

## Uncertainties

1. **`bcpvu`, second sign.** ABOUT needs `c`. The sign's upper part is a solid ink wedge with no visible counter (`review/work/raw_be2.png`), and it matches the `c` with a heavy top flag in the same word on hcp-1359 (`ciphers/hcp-1359/work/crops/z_about.png`). It is the only lowercase `c` on this card, and it is close in form to the card's `e` (`work/crops/z_come.png`). The word ABOUT is not in doubt.
2. **`dpef` = CODE.** Letter 2 is the looped stem plus bowl used for `p` in `Zpv`, `Zpvs`, `pxo`, so `dbtf` (CASE) is excluded. Letter 3 has an open eye and a hairline exit; read as `c` the word would be COBE, which is nothing, so it is `e`. The sense of "news in code" is my interpretation (presumably news the two exchanged in this cipher).
3. **`Tpssz`.** The capital is the `t` form with top bar (as `t` in `ofxt`, `tqfdjbm`), followed by the separate looped `p`; not `Gps`. The second `s` is faint but present. The dark blob before it, first taken as a separator inside the word, is most likely the foot of that `s`. Separators on this card are approximate in general; no word depends on them.
4. **`Jo`.** The J is faded but matches the `J` of line 1 stroke for stroke; `U` is rejected. The `o` is faint with a dark top.
5. **The sign after `dpef.`** is ink on this card, read as "&". Its loop, crossing stem and tail match the ampersand of hcp-1373 (`ciphers/hcp-1373/work/crops/w_and.png`), and the wheel-watermark median shows no such form at that place (`review/work/amp_vs_wm.png`). This doubt is closed.
6. **The `n` of `bn`** is angular, close to an `x` or `z` shape (`review/work/raw_bn.png`), and is the only lowercase `n` on the card, so nothing on this card confirms its form. AM rests on the context and on `J. bn` on sister cards, not on the shape.
7. **Faded letters** (`s` of `Zpvs`, `x`, `o` of `pxo`, `w` of `mpwjoh`, `m` of `Hjsm`) are readable at 5–6× but thin; the wheel watermark on the portal scan overlies parts of lines 2–5. No letter is restored.

## Why it is correct

One fixed shift turns all 97 letters into English, including long words that could not arise by chance (DEAREST, SPECIAL, REQUEST, LOVING). Key, closing formula ("your own … girl"), recipient, farm and postmark town agree with the accepted sister cards, and the postmark date is a Saturday, as the heading says.

## Credits

Download and capture by the orchestrator; transcription, key test and decoder by Claude Opus 5.5 acting as solver, 2026-10-30. Key family from the accepted cards hcp-1386…1407. No earlier work on this number.

## Response to review 1

Verdict ACCEPT, with four minor findings. I rechecked each on the reviewer's crops. The words read are unchanged.

1. **`bepvu` / `c`: fixed.** Agreed. The "closed loop" I described is not there: `review/work/raw_be2.png` shows a solid wedge, like the flagged `c` of hcp-1359's `bcpvu`. The transcription is now `bcpvu`, the plaintext is ABOUT, the "ADOUT" literal and the writer's-slip suggestion are withdrawn, and `work/decode.py` no longer has the ADOUT substitution. Uncertainties 1 and 2 were rewritten.
2. **Dot in `Tpss.z`: fixed.** Agreed from `review/work/t_sorry.png`: the blob sits where the first `s` also ends in a pooled foot. The transcription is now `Tpssz`, and `work/transcription.json` and uncertainty 3 say separators are approximate. No trailing dot was added to `xjmm`, and the `pxo` mark stays unrecorded, because no word depends on them.
3. **`n` of `bn`: fixed.** Agreed from `review/work/raw_bn.png`. Uncertainty 6 now says the reading rests on context and sister cards, not on the shape.
4. **Pointer for the `&`: fixed.** Uncertainty 5 now cites hcp-1373's `w_and.png` and the reviewer's median result, and closes the doubt.

I re-ran `python3 -I ciphers/hcp-1380/work/decode.py` after the edits: 4 hashes OK, 97 letters, output as in the table above.
