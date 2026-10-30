# HCP 1371 / pc_hcp_52 — Caesar (+1) love postcard, 22 July 1907

Status: **whole message read; independent review 1 verdict ACCEPT.** Two initial groups are kept literal (see Uncertainties). The salutation group, first transcribed `N. h.`, is now `N. L.` (see Response to review 1).

## Origin

HC Portal cryptogram 1371 (`pc_hcp_52`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). No published solution of this card was found or used; my only search was the repo and the orchestrator's register check.

Picture side: printed view "Crescent Gardens, Harrogate", no cipher. Address side: halfpenny Edward VII stamp, postmark ...BORNE (the sister cards give WIMBORNE; only the tail is legible here), 22 JY 07; addressed to Mr. W. Abbott, Stokelake Farm, Chudleigh, Devon (portal spelling "W. Abboú"). The message is written across the left half (rotate 90 degrees anticlockwise: `work/crops/reading.png`). 22 July 1907 was a Monday, matching the plain heading "G. H. Monday" and the plain side note "July 22nd -07". Same couple and formulae as the accepted sister cards hcp-1386, 1377, 1384, 1397, 1399, 1403.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by subtracting one.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Heading and side date are ordinary writing. The key was taken as a hypothesis from the sister cards and confirmed here: it turns every word on this card into English with no per-word adjustment.

## Transcription and plaintext (all ciphertext on the card)

| Line | Ciphertext | Literal plaintext |
|---|---|---|
| plain | G. H. Monday | (not enciphered) |
| 1 | Nz. Pxo N. L. Cpz | MY OWN [N. L.] BOY |
| 2 | Mfuufs up-Ebz. | LETTER TO-DAY. |
| 3 | "tqmfoeje" Mpwf | "SPLENDID" LOVE |
| 4 | & Lt.. Gspn. Zpvs | [& Lt..] FROM YOUR |
| 5 | Pxo. N. L. Hjsm | OWN [N. L.] GIRL |
| plain | July 22nd -07 | (not enciphered) |

46 enciphered letters, all decoded by the one key; 6 letters of initial groups kept literal.

English (the plaintext language; the portal lists Unknown): *"G. H. Monday. My own N. L. Boy, letter to-day 'splendid'. Love & Lt.. from your own N. L. Girl. July 22nd 1907."*

Slovak: *„G. H. pondelok. Môj vlastný N. L. chlapec, list dnes ‚skvelý'. Láska & Lt.. od tvojho vlastného N. L. dievčaťa. 22. júla 1907."*

The initial groups are left unexpanded in both versions. Punctuation in the sentences is editorial.

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1371/work/decode.py
```

It checks the SHA-256 of the files in `source/` and `work/hires/`, decodes every token of `work/transcription.json`, checks the inverse round trip and prints the plaintext with the letter counts. It decodes a manual transcription made from the pixels, not the image itself. The crops named below are in `work/crops/`.

## Uncertainties

1. **`N. L.` (lines 1 and 5, same form both times; `l2b.png`, `l6b.png`; first transcribed `N. h.`).** The slot is the one read `E. L.` / `E.h.` on sister cards (hcp-1386, 1387, 1399) and `N. L.` on hcp-1402, the closest parallel. Here the first sign is an arched capital, the form of N in `Nz`, without the loop of the E on hcp-1399; a capital M or E in a hurried form is not excluded. The second is a short dash, then a slanted stem with a small foot, which is the lead-in, stem and foot of the L on hcp-1402 (`work/v2/crops/nl_salutation.png` there). The foot is only a small hump, so h is not excluded, and the dash may be either a stop or the lead-in. Kept literal. Shifted values (M. K.) are shown by the decoder; no expansion is claimed, and it is not established whether the group is enciphered.
2. **`& Lt..` (line 4; `l5a.png`).** Three signs and two dots, kept literal.
   - The first looks like a large V with a hooked top. I read it as this writer's ampersand, because its strokes run in the same direction as the "&" on hcp-1386 (`work/crops/nl.png` there): down from the upper left, then a thin stroke up to the right. The form itself differs: the family's ampersand varies (a filled drop with a rising stem on hcp-1386, a reversed c on hcp-1399) and this one is an open hooked V. The better support is the slot (see the last point below). This is the weakest letter identification on the card: a plain V or an N is not excluded.
   - The second is a hooked, looped capital L, as on hcp-1399.
   - The third is a small c-like sign with a flat top stroke, read as t by analogy with `N & Lt` on hcp-1399; c or r is not excluded.
   - The same closing slot on sisters reads `N. & L.`, `M. & L.`, `N & Lt`. Here the first member of that slot seems to be replaced by the spelled word `Mpwf` = LOVE, followed by `&` and an L group; hcp-1395 deciphers `M. & L.` to L. & K., editorially "love & kisses". If the group here is enciphered, it gives `& Ks` and the phrase would be "Love & Ks", perhaps "love & kisses". This parallel makes that the most likely sense, but it is a hypothesis, not a reading, and the plaintext above does not use it.
3. **`Pxo` (line 1, `l2a.png`).** The o is an inked-in blob with no visible counter; the same word is clear in line 5. Read as o from its size and position, not from a counter. No separator dot follows it.
4. **j in `tqmfoeje` (`l4a.png`, `x_j.png`).** A long slash with a hooked tail and no loop, the same j as in `Hjsm` on this card and on sisters; it is not the looped f of this hand. An f would give SPLENDED, not a word. A separate dot above and to the right is taken as the dot of this j, or as stray punctuation; closing quotation marks follow.
5. **`Hjsm` (`x_end.png`).** H, slash j with a hooked tail, large s, and a flattened m that can look like "2u". The ink is pale here. The arrangement matches hcp-1376 (`work/crops/z_girl.png` there) and hcp-1389, whose m is similarly flattened, though the first stroke of this m is more flag-like.
6. **`Mfuufs` and `Mpwf`.** The capitals are three-stroked (M), not the one-legged N of `Nz`. N would give METTER and NOVE, so the capitals are decided by these word shapes as well as the strokes.
7. **Final e of `tqmfoeje` (`review/work/x_oeje.png`).** Both e have ink-filled eyes, and the last has no open eye and looks c-like at 4x. c would give SPLENDIB, not a word, so it is read as e.
8. **Wording.** "Letter to-day 'splendid'" has no verb; nothing is added. Heading initials could be C. H. (hcp-1386 reads C. H.; hcp-1397, 1377 G. H.); here the loop reads as G. They are not part of the cipher.

## Why it is correct

One fixed shift, with no parameter tuned to this card, gives English for all 46 letters, including an 8-letter word (`tqmfoeje` = SPLENDID) that does not occur in the couple's stock formulae. The closing is the couple's formula ("from your own ... girl"), and the Monday heading agrees with the postmark date and the calendar.

## Pen marks that are not ciphertext

A hand-drawn line runs under `"tqmfoeje"`, ends in a blob, and the tail of the j touches it; it looks like underlining of the quoted word, which fits the quotation marks. A second line runs under line 5 from the flourish of the date. Neither is treated as a cipher sign.

## Credits

Solved by Claude Opus 5.5 acting as solver, 2026-10-30. No earlier work on this number exists. The key and the comparison shapes come from sister-card work in this repo (OpenAI GPT solver and Claude Opus 5.5).

## Response to review 1

Verdict ACCEPT, four minor findings. All four are addressed. None changes a decoded letter. After the edits, `python3 -I ciphers/hcp-1371/work/decode.py` still reports hashes OK and 46 enciphered + 6 literal letters.

1. **`N. h.` versus hcp-1402: agreed, fixed.** I compared `hcp-1402/work/v2/crops/nl_salutation.png` with `review/work/a2.png`. Both show an arched N, a short dash, and a slanted stem with a small foot. The foot is smaller here than on hcp-1402, but the structure is the same. The transcription (`work/transcription.json`), the table and both translations now read `N. L.`, and uncertainty 1 cites hcp-1402 and keeps h open. The group stays literal, so the decoded text is unchanged; only the bracketed literal and its shifted display (M. K.) differ.
2. **`& Lt..` support: agreed, fixed.** Uncertainty 2 now says only the stroke direction is shared, adds the structural parallel of the closing slot and hcp-1395, and lists r as an alternative for the third sign. The "& Ks" sense stays a labelled hypothesis.
3. **Final e of `tqmfoeje`: agreed, fixed.** Added as uncertainty 7.
4. **Pen marks: agreed, fixed.** New section "Pen marks that are not ciphertext"; both lines are visible in `work/crops/reading.png`.

Nothing the reviewer could not verify is claimed as verified here: expansions of the initial groups, the first letters of the postmark town, and the identity of the writers remain open.
