# HCP 1399 / pc_hcp_80 — Caesar shift (+1 written, −1 to decrypt)

**Status: complete reading of the message; two initial groups reported literally. Review 1: ACCEPT (three minor findings, addressed below; no letter changed). Closed with FINAL.**

Credit: source capture, the Caesar −1 identification and the transcription of all 46 enciphered letters were done earlier by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol, 2026-10-26), using a hypothesis from the related card HCP1400. Claude Opus 5.5 (2026-10-29) re-checked every word on enlarged crops, transcribed the initial groups literally, read the postmark, wrote `work/transcription-v2.json` and `work/solve.py`, and completed this handover. No published solution of this card exists to our knowledge (portal status Not solved, no attached transcription/solution); none was used.

## Source and context

- Portal record 1399, name pc_hcp_80, status Not solved, recipient "Dean", date unknown (source/metadata.md).
- Picture side: printed "St. Philips Church & Monument, Birmingham" (Copyright F.F. & Co.); no handwriting.
- Address side (read rotated 90° counter‑clockwise): Miss Dean, Queen's House (reading of the house name uncertain), Wimborne, Dorset. Halfpenny Edward VII stamp; postmark `7.30 PM / [F]E 2 / 08`, office name ending `…ON ABBOT` (Newton Abbot), upper arc partly legible (work/z-postmark.png). 2 February 1908 was a Sunday, which agrees with the written heading "S. 7. Sunday." The month letters are partly obscured: only `E` is clear, so "FE" is a reading consistent with the weekday, not an independent date proof.
- The message is in English. Same cipher habits (Caesar −1, "Nz Pxo"/"Zpvs Pxo", initial groups with "&" before "gspn") as the W. Abbott card run HCP1386–1407 (Chudleigh, near Newton Abbot, 1907–08) and the other "Dean" card HCP1400. The writer of this card is therefore very probably the Abbott correspondent writing to Miss Dean; this is context only and is not used to read any letter.

## Cipher and key

Simple Caesar substitution: each plaintext letter is written as the next letter of the alphabet. Decrypt by shifting back one:

```
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext

| Line | Ciphertext | Plaintext |
|---|---|---|
| heading (plain) | S. 7. Sunday. | S. 7. Sunday. |
| salutation | Nz Pxo **E.h.** | MY OWN [E.h.] |
| 1 | Nboz uibolt | MANY THANKS |
| 2 | gps "Txffut" | FOR "SWEETS" |
| 3 | uijt npsojoh. | THIS MORNING. |
| 4 | **N & Lt** gspn | [N & Lt] FROM |
| 5 | Zpvs Pxo **E.h.** | YOUR OWN [E.h.] |

Reading: *My own E.h., many thanks for "sweets" this morning. N & Lt from your own E.h.*

English translation: "My own [E.h.], many thanks for the 'sweets' this morning. [N & Lt] from your own [E.h.]."

Slovak translation: „Môj vlastný [E.h.], veľká vďaka za ‚sladkosti‘ dnes ráno. [N & Lt] od tvojho vlastného [E.h.].“

All 46 enciphered letters decode under the single key (one shift, round‑trip checked). Strong word checks: Nboz uibolt → MANY THANKS, Txffut → SWEETS, uijt npsojoh → THIS MORNING, gspn → FROM, Zpvs Pxo → YOUR OWN.

## Single command (from the repo root)

```sh
python3 -I ciphers/hcp-1399/work/solve.py
```

It checks the SHA-256 of every file in source/ (work/source-sha256.json), decodes `work/transcription-v2.json`, round‑trip checks each word, and prints the plaintext above with the initial groups shown literally plus their Caesar −1 equivalents. It decodes a manual transcription, not pixels. (The older `work/decode.py` / `transcription.json` are the earlier GPT partial version, kept for the record.)

## Uncertainties (all disclosed)

1. **`E.h.` (salutation and closing, same form both times; work/z-salutation-eh.png).** A looped capital like a cursive E, a dot, a clear h, a dot. Kept literal. If it is enciphered like the words, it would be `D.g.`; if written plain, `E.h.`. Which it is, and what it stands for (a pet name/initials used by both writer and recipient), is not established; no expansion is claimed. The sister card HCP1386 has a comparable group transcribed "El." in "My own El. Boy / Your own El. Girl".
2. **`N & Lt` before FROM (work/z-closing-initials.png, z-closing-line.png).** The first capital has the same form as the writer's cipher N in Nz/Nboz (M not excluded); the middle sign is a small reversed‑c ampersand; then a capital L followed by a short t‑like letter with a detached cross‑stroke (h not excluded). Kept literal. Caesar −1 would give `M & Ks`; the same shorthand group appears on HCP1395, 1402, 1403, 1407. An expansion such as "[many/much love] & kisses" is plausible but **not claimed**.
3. `gspn` (work/z-gspn.png) is crossed by the descender of the g and the line above; the letters g‑s‑p‑n are read, and FROM agrees with the "… from your own …" closing of the sister cards.
4. Heading `S. 7.` is ordinary writing (meaning unknown, not shifted). The house name in the address is uncertain and not part of the message.
5. Quotation marks around "Txffut" and the full stop after npsojoh are visible on the card. Case and spacing follow the manuscript; punctuation in the English sentence is editorial.

## Why we believe it is correct

One fixed shift turns every enciphered word on the card into ordinary English that forms a coherent short thank‑you note, with the same salutation/closing formulas and cipher as a whole run of related cards. No letters are inserted; the only unexpanded material is two initial/abbreviation groups, reported literally. The postmark date (Sunday 2 Feb 1908, Newton Abbot) agrees with the heading "Sunday" and with the 1907–08 Abbott correspondence.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave **ACCEPT** with three minor findings. Response by Claude Opus 5.5 as solver, 2026-10-30. No ciphertext letter, key or decoded word changed; `work/transcription-v2.json` and `work/solve.py` are unchanged, and `python3 -I ciphers/hcp-1399/work/solve.py` was re-run after this response: source hashes OK, same six lines, 46 enciphered letters.

1. **`N & Lt`: the "t" deserves a weaker label — agreed.** On work/z-closing-initials.png and the reviewer's review/work/r_nlt.png the sign after the looped L is a small loop with a short trailing stroke. It can be a t whose cross is written as a trailing dash (as at the end of `uibolt`), but it can equally be a flourish or full stop after L. The group is therefore read as **`N & Lt` or `N. & L.`, with equal weight**; `N. & L.` is exactly the group transcribed on the sister cards hcp-1386 and hcp-1403. Under Caesar −1 the two readings give `M & Ks` and `M. & K.` respectively. The literal output of solve.py keeps `N & Lt` as transcribed, and this alternative is part of uncertainty 2. Neither reading is expanded.
2. **Family treatment and better parallels — agreed, added.** The same closing slot (initials + "&" + initial before `gspn`) is treated differently across the family: hcp-1395 reads its `M. & L.` as ciphertext, giving `L. & K.` (expanded there editorially as "love & kisses"), while hcp-1386 (`N. & L.`), hcp-1403 (`N. & L.`), hcp-1407 (`M. & L.`) and this card keep the group literal. (The earlier list "HCP1395, 1402, 1403, 1407" in uncertainty 2 above should read 1386, 1395, 1403, 1407: no such group is recorded in hcp-1402/SOLUTION.md.) Both treatments are possible here; on this card the enciphered option gives `M & Ks` / `M. & K.`, which does not yield the clean `L. & K.` of hcp-1395, which is one reason it is kept literal. For `E.h.`, the closest parallel is hcp-1400, also addressed to Miss Dean, whose salutation begins `Nz E.h. …` (hcp-1400/SOLUTION.md); this supports the literal `E.h.` reading better than the `E. L.` of hcp-1386.
3. **`gspn` partly overwritten — agreed, kept.** Uncertainty 3 stands: the g's descender and the stroke from the line above cross s and p, which are only partly separable; the word is read as `gspn` = FROM from its length, the visible shapes and the fixed "… from your own …" formula of the sister cards. The report repeats this and does not present the word as fully clear.

Unverified points listed by the reviewer (postmark month, the office name's upper arc, the meaning of `E.h.`, `N & Lt` and `S. 7.`, the house name, a search for publication outside the portal) remain open and are stated in the report.
