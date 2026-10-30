# HCP 1405 / pc_hcp_86 — solution (Caesar −1, English)

Postcard (Tuck's "Scottish Lochs", Loch Awe with Kilchurn Castle), postmarked Wimborne 7 Feb 1908, to W. Abbott (portal: "W. Abboú"), Chudleigh, S. Devon. One of the run of cipher postcards to W. Abbott (hcp-1386 … 1407). Portal status: Not solved; no transcription or solution attached; no published decipherment found. The portal gives the language as Unknown; the plaintext is English.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "G. H. Friday" is ordinary writing and is not shifted (7 Feb 1908 was a Friday, matching the postmark FE 7 08). Three short groups — `El`, `N. & L.`, `Mu` — are the couple's recurring abbreviations; they are kept literal (shifted values printed alongside), as on sister cards hcp-1386, 1390, 1393, 1403.

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Pxo. El Cpz. | MY. OWN. [El] BOY. |
| J. ibwf. Cffo. | I. HAVE. BEEN. |
| wfsz. cvtz. | VERY. BUSY. |
| up-Ebz. | TO-DAY. |
| Nz. N. & L. Zpvs | MY. [N. & L.] YOUR |
| Pxo. Mu Hjsm | OWN. [Mu] GIRL |

43 enciphered letters, all decoded by the one key; 6 abbreviation letters kept literal. The picture side has no handwriting.

**English:** "My own El. boy, I have been very busy to-day. My N. & L. — your own Mu. girl."

**Slovak:** „Môj vlastný El. chlapec, dnes som mala veľa práce. Moje N. & L. — tvoje vlastné Mu. dievča.“

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1405/work/v2/decode.py
```

It checks the SHA-256 of every file in `source/`, reads the manual transcript `work/v2/transcription.json`, decrypts every enciphered token with the key, verifies the round trip, and prints the plaintext above (saved in `work/v2/plaintext.txt`). The transcript is a manual visual reading from enlarged crops (`work/v2/crops/`), not OCR.

## Uncertainties

1. **Abbreviations kept literal, not expanded.** `El` (salutation; = "E. L." of hcp-1386/1403), `N. & L.` (closing; = hcp-1386), `Mu` (before GIRL; = hcp-1390/1393). Whether they are plain initials or enciphered (Dk, M. & K., Lt) is not established; no expansion is claimed.
2. **`Mu`**: a capital M followed by small strokes and a tall stroke, crossed by the printed upside-down publisher line ("Art Publishers to their Majesties"). The second sign (u or h) is not secure; the group is identified by its shape and slot with the sister cards.
3. **`z` forms**: in `Cpz` and `wfsz` the z is a small "1"/"2"-like sign (the same shape in both); in `cvtz` and `Ebz` it is the clearer 2-like z. The z of `wfsz` lies partly under the grey portal watermark.
4. **Line 4 `up-Ebz`** is faint; E, the 6-like b and 2-like z are visible, as in `up-Ebz` on hcp-1406/1407.
5. **`Hjsm` (GIRL)**: H, then a cramped sign with a descender running under the printed publisher line, then s and m. The second letter (j → I) is not individually secure on the pixels; it is read from the word shape and the series formula "your own … girl" (hcp-1386, 1390, 1393).
6. **Heading initial** G or C (plain, not part of the cipher).
7. Punctuation and capitals in the English sentence are editorial; the literal output keeps the writer's dots.

## Why this is correct

- One fixed shift, the same as on the accepted sister card hcp-1397 and the other Abbott cards, turns every enciphered group into an English word; no word-specific substitutions.
- The words form a coherent, typical 1908 lovers' postcard and repeat this couple's formulas exactly: "My own El. boy" (hcp-1386), "N. & L. … your own … girl" (hcp-1386), "Mu. girl" (hcp-1390/1393).
- The heading "Friday" agrees with the postmark date 7 Feb 1908.

## Credit and correction of earlier work

Earlier partial work in this directory (OpenAI GPT solver, 2026-10-26; `work/decode.py`, `work/transcription.json`) found the key and read I HAVE BEEN and TO-DAY, but misread the greeting as `Nz Pxo Efbs` (MY OWN DEAR), misread line 3 as `up-Ebz` and left line 4 and the closing unresolved. Claude Opus 5.5 (2026-10-29) re-read every line from enlarged crops: greeting `El Cpz` (… El. BOY), line 3 `wfsz. cvtz.` (VERY BUSY), line 4 `up-Ebz` (TO-DAY), closing `Nz. N. & L. Zpvs / Pxo. Mu Hjsm`. The earlier files are kept unchanged for the record.

## Response to review 1

Review 1 (Claude Opus 5.5, verdict ACCEPT) raised four minor findings. The reading is unchanged; `python3 -I ciphers/hcp-1405/work/v2/decode.py` was re-run on 2026-10-30 and still prints the same six lines, "43 enciphered letters decoded + 6 abbreviation letters kept literal; hashes OK".

1. **`Hjsm` second letter (minor) — fixed.** Added uncertainty 5 above: the j of Hjsm is cramped under the printed line and read from word shape and the series formula. On the enlarged crop `work/v2/crops/l6e.png` the H is followed by a stroke with a long descender (consistent with a cursive j), then s and m; no other letter gives an English word in the slot "your own … ___".
2. **`El` vs `E. L.` (minor) — no change needed.** Already disclosed in uncertainty 1; the group is kept literal and not expanded.
3. **Same-provider review (minor) — agreed.** The register entry and the report state that the round-1 completion and the review were both done by Claude Opus 5.5 (separate agents), with the earlier GPT-6 Astra work credited; no cross-provider review is implied.
4. **Heading initial G/C (minor) — no change needed.** Already disclosed (uncertainty 6); the heading is plain writing and not part of the cipher.
