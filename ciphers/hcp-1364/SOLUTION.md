# HCP 1364 / pc_hcp_45 — Caesar (+1) love postcard, 17 July 1907

Status: **whole message read; review 1 (REVISE) addressed, see the response below.** Two abbreviation groups (`M. L`, `M-L.`) are kept literal, as on the sister cards; every other letter is read and decoded. The initial of the groups was first read N and is now read M, with N not excluded.

## Origin

HC Portal cryptogram 1364 (`pc_hcp_45`), portal status *Not solved*, language Unknown, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). Picture side: printed coloured view "Hotel Majestic, Harrogate", no writing (a dark blot in the sky is damage, not a sign). Address side: Boots Cash Chemists "Pelham" Series card, halfpenny Edward VII stamp, postmark WIMBORNE / 10 PM / JY 17 / 07, agreeing with the portal date 1907-07-17, which was a Wednesday, matching the plain heading. Addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon (the portal spells the recipient "W. Abboú"). The large grey alphabet disc over the scan is the portal's watermark. Same hand, same recipient and same formulae as the Caesar cards hcp-1386…1407. No published solution of this card was found or used.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter. Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "G. H. Wednesday" is ordinary writing, not shifted. `M. L` / `M-L.` are abbreviations kept literal (shifted they would be L. K.), as the same groups are on sister cards hcp-1347 and hcp-1383 (read M) and hcp-1402 and hcp-1368 (read N).

## Transcription and plaintext (all ciphertext on the card)

Read on the address side turned 90° anticlockwise (`work/reading.png`).

| Ciphertext | Plaintext |
|---|---|
| G. H. Wednesday | (plain heading) |
| Nz. Pxo. M. L Cpz | MY. OWN. [M. L] BOY |
| Mfuufs. wfsz. | LETTER. VERY. |
| ojdf. up Ebz. | NICE. TO DAY. |
| Zpvs. Pxo M-L. | YOUR. OWN [M-L.] |
| Hjsm | GIRL |

38 enciphered letters, all decoded by the one key; 4 abbreviation letters kept literal.

English: *"G. H. Wednesday. My own M. L. boy, letter very nice to-day. Your own M-L. girl."*

Slovak: *„G. H., streda. Môj vlastný M. L. chlapec, list dnes veľmi milý. Tvoje vlastné M-L. dievča."*

The plaintext language is English; dots follow the manuscript (rechecked in review) and are not significant (the writer dots nearly every word). The sentence has no verb on the card ("letter very nice to-day"); no word is missing from the pixels.

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1364/work/decode.py
```

It checks the SHA-256 of all files in `source/`, decodes every token of `work/transcription.json`, checks the inverse round trip, and prints the plaintext and letter counts.

## Uncertainties

1. **`M. L` / `M-L.`** Abbreviations, meaning unknown, not expanded. The initial has hook, stem and two further short legs in both places, one leg more than the N of `Nz` and the same build as the M of `Mfuufs` (`work/crops/cap_compare.png`, left to right: `Nz`, salutation, closing, `Mfuufs`), so it is read M; N is not excluded, because the extra leg is short and the legs run together in ink, and sister cards hcp-1402 and hcp-1368 keep N. The second sign is a slanted stem with a small foot, close to a plain l or a 1: L is the reading from the sister groups, but 1 is not excluded (hcp-1402 records the same doubt for its closing form) and hcp-1349 and hcp-1366 report `h` in this slot. In the closing group a dash stands where the salutation has a dot; on hcp-1402 such a stroke is taken as the L's lead-in, and this card does not decide which it is. The only dot of the first group stands between the initial and the L, near the L's stem. Whether the groups are shifted at all is undecided.
2. **Capital of `Mfuufs`.** The first sign is a three-stroke M, the writer's form for this word (compare `work/crops/letter.png` with `ciphers/hcp-1386/work/crops/mfuufs.png`); N would give METTER. The sign is compact, so the word shape helps decide it.
3. **`Pxo` on line 4.** The foot of the P and the x run together (`work/crops/l5b.png`); the x's two crossing strokes and the o are visible, and the word is the same as `Pxo` on line 1.
4. **Heading initials.** G. H. as read here, matching the G. H. of hcp-1397 and hcp-1402; their meaning is unknown and they are not enciphered.
5. Who wrote it is not stated; "girl" comes only from the signature formula. Harrogate on the picture and Wimborne on the postmark are not connected by anything on the card.

## Why it is correct

One fixed shift with no card-specific tuning turns every enciphered token into English (38/38 letters), including LETTER, VERY, NICE, OWN, YOUR and GIRL. Salutation and close repeat the couple's formula on accepted cards (hcp-1402: `Nz. Pxo. N. L. Cpz.` … `zpvs Pxo N. L.`, then Hjsm; the groups there are read N). The plain heading "Wednesday" matches the postmark date.

## Credits

Solved by Claude Opus 5.5 as solver, 2026-10-30; no earlier work on this number. Key and formula hypotheses came from the accepted sister cards in this repo and were tested on this card's pixels.

## Response to review 1

Verdict REVISE. All five findings are accepted. No enciphered letter changed: the 38 letters decode as before. Only the four literal abbreviation letters and the punctuation of row 1 changed.

1. **Abbreviation initial (major): fixed.** I looked at `review/work/cap_compare.png`, `l1b.png` and `l4b.png`. Both group initials have an extra short leg at the foot, which the `Nz` capital lacks and the `Mfuufs` capital has. My claim "as in `Nz`" was wrong, and I had applied opposite criteria to one form. Now `M. L` / `M-L.`, N not excluded. The shifted value is L. K. Updated `work/transcription.json`, the table, both translations and Uncertainty 1. The comparison is copied to `work/crops/cap_compare.png`.
2. **Punctuation (minor): fixed.** `work/reading.png` and `review/work/cap_end.png` show no dot after `Cpz` and no dot after the L of the first group. Row 1 is now `Nz. Pxo. M. L Cpz`. I checked the dots of the other rows against `work/reading.png` and they stand as transcribed.
3. **Sister citation (minor): fixed.** hcp-1384 removed. The cipher section now cites hcp-1347 and hcp-1383 (M) and hcp-1402 and hcp-1368 (N).
4. **hcp-1383 citation for `Mfuufs` (minor): fixed.** Removed. The comparison with hcp-1386 stays. hcp-1383 is now cited only for the M reading of the group (its uncertainty 2), which it does support.
5. **L caveat (minor): fixed.** Uncertainty 1 now says 1 is not excluded and that hcp-1349 and hcp-1366 report `h` in this slot.

`python3 -I ciphers/hcp-1364/work/decode.py` was re-run after the changes: hashes pass, 38 enciphered letters and 4 literal letters, plaintext unchanged except for `[M. L]` and `[M-L.]`.
