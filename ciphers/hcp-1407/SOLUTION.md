# HCP 1407 / pc_hcp_88 — Caesar shift (+1 written, −1 to decrypt)

**Status: complete reading of the enciphered message; two short initial groups in the closing are reported literally. Review 1 verdict ACCEPT; closed (FINAL).**

Credit: source capture (all three portal tabs, 2026-10-26), the Caesar −1 identification, the 49-letter transcription and the `up-Ebz` → TO-DAY resolution (by comparison with HCP1406) were done by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol, 2026-10-26). Claude Opus 5.5 (2026-10-29) re-checked every sign on 2–5× enlarged crops, read the postmark, classified the closing initial groups as literal (following the convention of the sister cards HCP1386, 1399, 1403), wrote `work/transcription-v2.json` and `work/solve.py`, and completed this handover. No published solution of this card is known (portal status Not solved; no attached transcription/solution); none was used.

## Source and context

- Portal record 1407, name pc_hcp_88, status Not solved, date 1907-05-14, recipient "W. Abboú" (source/metadata.md).
- Picture side: printed Tuck's "Oilette" Dartmoor series II, *The River Lyd*; no handwriting.
- Address side (read rotated 90° counter-clockwise, `work/reading.jpg`): Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (farm name read as on sister cards HCP1386/1403; see response to review 1). Halfpenny Edward VII stamp; postmark `WIMBO[RNE]` / `6.30 PM` / `MY` / `07` (the day digits lie mostly under the stamp edge and are not independently legible). 14 May 1907 was a Tuesday, agreeing with the written heading "G. H. Tuesday." and the dated foot "May 14th 1907". Wimborne (Dorset) is also the address of Miss Dean on the sister card HCP1399; this is context only.
- Language: English. Same writer and cipher habits as the W. Abbott series HCP1386–1407 (1907–08): Caesar −1, "Nz Pxo", "up-Ebz", initial group with "&" before "gspn".

## Cipher and key

Simple Caesar substitution: each plaintext letter is written as the next letter of the alphabet. Decrypt by shifting back one:

```
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Heading and date are written in clear.

## Transcription and plaintext

| Line | Ciphertext (as written) | Plaintext |
|---|---|---|
| heading (clear) | G. H. Tuesday. | G. H. Tuesday. |
| 1 | Nz. Pxo. Efbsftu. | MY OWN DEAREST. |
| 2 | Nboz. uibolt. gps | MANY THANKS FOR |
| 3 | dbse: up-Ebz. | CARD TO-DAY. |
| 4 | **M. & L.'** gspn. zpvs | [M. & L.] FROM YOUR |
| 5 | Pxo. **N.-1** Hjsm | OWN [N.-1] GIRL |
| date (clear) | May. 14th 1907. | May 14th 1907. |

Reading: *G. H. Tuesday. My own dearest, many thanks for card to-day. [M. & L.] from your own [N.-1] girl. May 14th 1907.*

English (already English): "My own dearest, many thanks for the card today. [M. & L.] from your own [N.-1] girl."

Slovak: „Môj najdrahší, veľká vďaka za dnešnú pohľadnicu. [M. & L.] od tvojho vlastného [N.-1] dievčaťa.“

## Reproduction (one command, from repo root)

```sh
python3 -I ciphers/hcp-1407/work/solve.py
```

It checks the SHA-256 of every file in `source/` against `work/source-sha256.json`, then decodes `work/transcription-v2.json` with the key above and prints the plaintext. Output:

```
source hashes OK
heading  G. H. Tuesday.
line1    MY. OWN. DEAREST.
line2    MANY. THANKS. FOR
line3    CARD: TO-DAY.
line4    [M. & L.'] FROM. YOUR
line5    OWN. [N.-1] GIRL
date     May. 14th 1907.
49 enciphered letters decoded; [..] = initial groups kept literal
```

The transcription is manual (no OCR); the script only applies the key.

## Uncertainties

1. **Closing group before FROM, `M. & L.'`** (line 4). First capital has two arches (M); N is not fully excluded (sister card HCP1399 reads the same group as N). Then a reversed-c ampersand, a capital L, and a small raised tick (comma/apostrophe-like; possibly the reduced t of HCP1399's "Lt"). Kept literal. Under the shift it would give L. & K.; an expansion such as "[much love] & kisses" is plausible but **not claimed**.
2. **Group between OWN and GIRL, `N.-1`** (line 5). A capital N-like letter (one arch, as in the writer's cipher N of Nz/Nboz; M not excluded), a short baseline dash, then a raised 1/l-like stroke. Best described neutrally as "N/M with a raised tick"; the raised stroke may be the same reduced t/apostrophe mark as after L in line 4, so a gloss "No. 1" is weak. Kept literal and not expanded. The parallel HCP1406 closing has a similar unresolved E/No-like group.
3. **`uibolt`**: the final t is a short reduced upward stroke attached to the base of the l, without a visible cross-bar; the word THANKS also occurs as `uibolt` on sister cards (e.g. HCP1399).
4. **`up-Ebz`**: the cursive b and z of Ebz resemble the digits 6 and 2; they are read as letters because the same E, b, z forms occur in Efbsftu/Nboz/Nz on this card and the identical group `up-Ebz` occurs on HCP1406.
5. Heading initials "G. H." (clear text) are not identified; the farm name (Stokelake) is a context reading only. Neither affects the decipherment.

## Why this is correct

- One fixed key decodes all 49 enciphered letters into fluent, period-typical English with no exceptions.
- The structure (salutation, thanks, closing "from your own … girl") is the formula of the whole W. Abbott series, decoded with the same key.
- The clear heading weekday (Tuesday), the dated foot (May 14th 1907), the postmark (MY … 07) and the portal date agree.
- Only the two short initial groups are not decoded; they are reported literally and every reading alternative is disclosed above.

## Response to review 1

Review 1 (review/REVIEW1.md) verdict **ACCEPT**, three minor findings, no blocker or major. No decoded letter changed.

1. **Closing initial groups (minor) – agreed, wording changed.** Uncertainty 2 now describes the line-5 group neutrally as "N/M with a raised tick" and notes that the raised stroke may be the same reduced t/apostrophe mark as after L in line 4; the gloss "No. 1" is no longer offered as the likely reading. Both groups stay literal, as before.
2. **Farm name (minor) – agreed.** Re-checked on the reviewer's 3× crop (review/work/z_addr.png): the word before "Farm" reads S-t-o-k-e-l-a-k-e, i.e. **Stokelake**, the same farm named for Mr W. Abbott of Chudleigh on HCP1386 and HCP1403. The context section is corrected. Context only; it does not affect the decipherment.
3. **Postmark day (minor) – agreed.** The context section and "Why this is correct" now give the postmark as WIMBO[RNE] / 6.30 PM / MY / 07 and say the day is not independently legible. The date 14 May 1907 rests on the written foot date, the Tuesday heading (14 May 1907 was a Tuesday) and the portal date.

Reproduction re-run after these edits (only SOLUTION.md text changed; work/ untouched): `python3 -I ciphers/hcp-1407/work/solve.py` still prints `source hashes OK` and the same seven lines and `49 enciphered letters decoded`.
