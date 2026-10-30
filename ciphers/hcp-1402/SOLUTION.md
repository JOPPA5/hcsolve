# HCP 1402 / pc_hcp_83 — Caesar (+1) love postcard, 28 Jan 1908

Status: **whole message read; handed to review (DONE1).** Three abbreviation groups (`N. L.` twice, `N. & L.` once) are kept literal, as on the sister cards; nothing else is unresolved.

## Origin

HC Portal cryptogram 1402 (`pc_hcp_83`), portal status *Not solved*, no attached transcription or solution (see `SOURCES.md`, `source/metadata.md`). Picture side: printed Tuck's "Oilette" view *The Norfolk Broads / On the Waveney*, no handwriting. Address side (rotate 90° CCW, `work/reading.png`): halfpenny Edward VII stamp, postmark **WIMBORNE / 10 PM / JA 28 / 08**, which agrees with the portal date 1908-01-28 (a Tuesday) and with the ordinary heading "G. H. Tuesday."; addressed to Mr Abbott, Stokelake Farm, Chudleigh, S. Devon (portal spells the recipient "W. Abboú"; metadata left unchanged). The card belongs to the same correspondence as hcp-1386…1407 (a girl writing to W. Abbott, 1907–08, same key, same formulae "My own … boy", "from your own … girl"). No published solution of this card was found or used.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet (encryption +1). Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "G. H. Tuesday." is ordinary writing and is not shifted. The abbreviation groups are printed literally, with their shifted values (M. K., M. & K.) shown alongside by the command; which (if either) is meant is not established, as on hcp-1386/1401/1404.

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Pxo. N. L. Cpz. | MY. OWN. [N. L.] BOY. |
| Mfuufs uijt. | LETTER THIS. |
| npsojoh xbt. | MORNING WAS. |
| GJOF. Nboz uibolt | FINE. MANY THANKS |
| Nz. N. & L. gspn. | MY. [N. & L.] FROM. |
| zpvs Pxo N. L. | YOUR OWN [N. L.] |
| Hjsm. | GIRL. |

59 enciphered letters, all decoded by the one key; 6 abbreviation letters kept literal. Dots follow the manuscript and are not significant.

English reading: *"My own N. L. boy, letter this morning was FINE. Many thanks. My N. & L. from your own N. L. girl."*

Slovak: *„Môj vlastný N. L. chlapec, list dnes ráno bol VÝBORNÝ. Veľká vďaka. Moje N. & L. od tvojho vlastného N. L. dievčaťa."*

(The plaintext language is English; the portal lists the language as Unknown.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1402/work/v2/decode.py
```

It checks the SHA-256 of all three files in `source/`, decodes every token of `work/v2/transcription.json` with the key, checks the inverse round trip, and prints the plaintext above with the letter counts (output saved in `work/v2/plaintext.txt`). Enlarged crops supporting each reading are in `work/v2/crops/`. The older `work/decode.py` / `work/transcription.json` are the earlier partial transcript, kept for history.

## Uncertainties

1. **Abbreviation `N. L.`** (salutation and closing). Written `N-L`: a two-arch capital N (same form as the N of `N. & L.` and of `Nz`), then an L whose horizontal lead-in stroke looks like a dash, slanted stem and looped foot — the same L as in `N. & L.` (`crops/nl_salutation.png`, `nl_closing.png`, `n_amp_l.png`). It is clearly not the curly E of the `E. L.` group on sister cards hcp-1386/1401/1404. Earlier work described it as "M/N-like initial plus 1/l/t-like stroke"; a "No. 1" reading is rejected because the second sign has the L's foot and lead-in. M instead of N is not wholly excluded but the sign has two arches. The group is not expanded.
2. **`N. & L.`** before FROM: abbreviation, kept literal (same group as on hcp-1386 and hcp-1403). Expansions are not claimed.
3. **`GJOF`** is written in capitals (copybook G, long-slash J, small O, swash F; `crops/gjof.png`); FINE is the only reading of these four signs that makes English, and the writer's capitals for emphasis are retained.
4. **Final t of `uibolt`** stands at the card edge; it has the short looped t of the same word written by the same hand on hcp-1386 (`crops/uibolt_end.png`). **`uijt`**: u, i, j (descending slash with V foot), t (tall upstroke) — `crops/uijt.png`.
5. Heading initials G. H. (C. H. on some sister cards; hcp-1397 review preferred G. H.); not enciphered, not expanded. The sender's identity is not claimed.

## Why it is correct

One fixed shift, already accepted on sister card hcp-1397 (FINAL) and used throughout this correspondence, turns every enciphered token into English (59/59 letters) with no exceptions, including long words (LETTER, MORNING, THANKS) and the couple's recurring formulae ("My own … boy", "My N. & L. from your own … girl"). The message fits a 1908 sweetheart postcard and the weekday in the heading matches the dated postmark.

## Credits

Earlier partial work (portal capture, rotation, 57-letter partial transcript, key identification) by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26. Completion (re-transcription from the pixels, reading of the abbreviation groups as N. L. / N. & L., the second `Nz` on line 5, the postmark, new decoder) by Claude Opus 5.5 acting as solver, 2026-10-29.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent, 2026-10-30): verdict **ACCEPT**, four minor findings, no blocker or major. The reproduction command was re-run after this response (`python3 -I ciphers/hcp-1402/work/v2/decode.py`): unchanged output, 59 enciphered letters + 6 abbreviation letters, hashes OK. No decoded letter changed.

1. **Closing `N. L.` (minor) — accepted, wording changed.** Re-examined `work/v2/crops/nl_closing.png`: after the two-arch N and the dash comes a short slanted stroke with only a small foot; it is less clearly an L than the second sign of the salutation group (`nl_salutation.png`) or of `N. & L.`. Uncertainty 1 above is hereby amended: the closing group is read **N. L. by analogy with the salutation**; a reading N. 1 / N. l is not excluded on the pixels. Either way the group is an abbreviation kept literal and does not affect the enciphered text.
2. **Final `t` of `uibolt` (minor) — accepted.** On `work/v2/crops/uibolt_end.png` the last sign at the card edge is a short loop without a visible cross, closer in shape to an e. The reading t (THANKS) rests on context and on the writer's habit on sister cards; this is stated plainly in the report. Uncertainty 4 above is amended accordingly (the earlier phrase "has the short looped t" overstated the visual evidence).
3. **NOTES.md 2026-10-26 entry without spaces (minor) — acknowledged.** The entry was written that way by the earlier GPT session; it is left as the historical log (not rewritten). Its content is summarised readably in the 2026-10-29 entry, and the report does not copy it.
4. **"letter this morning was FINE" (minor) — accepted.** The sense is "(your) letter this morning was fine", i.e. the writer received the recipient's letter that morning and liked it; the report gives this gloss next to the literal wording.

Decision: verdict ACCEPT, all findings addressed without substantive change → report, register entry, FINAL.
