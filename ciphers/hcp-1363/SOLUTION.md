# HCP 1363 / pc_hcp_44 — Caesar (+1) love postcard, 19 July 1907

Status: **whole message read; review 2 verdict ACCEPT (closed as FINAL).** The line-1 word changed from `Mpwfs` (LOVER) to `Mpwjoh` (LOVING) after review 1. One pale letter and the closing groups are disclosed below.

> **My own loving boy, many thanks for cards of Windsor. Love & Lt.. from Y. O. M. h. girl.**

## Origin

HC Portal cryptogram 1363 (`pc_hcp_44`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). No published solution of this card was found or used; the only checks were this repo and the orchestrator's register check.

Picture side: printed "Royal Baths, Hospital, Harrogate", no handwriting. Address side (Boots "Pelham" Series): halfpenny Edward VII stamp, postmark with the town name lost, 10 PM, JY 19, 07, agreeing with the portal date 1907-07-19, which was a Friday, matching the plain heading. Addressed in clear to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (portal spelling "W. Abboú"). The disc and building logo on the scans are a scanning overlay. The message is on the left half; rotate 90 degrees counter-clockwise (`work/crops/message_ccw.png`).

This is the companion of hcp-1366: same day and postmark time, same card series, same Harrogate subject, and that card is headed "No. 1." while this one is headed "No. 2."

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by subtracting one.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The key was taken as a hypothesis from the sister cards (hcp-1366, 1371, 1386 and others) and confirmed here: every word gives English without per-word adjustment. The heading is ordinary writing.

## Transcription and plaintext (all ciphertext on the card)

| Line | Ciphertext | Literal plaintext |
|---|---|---|
| plain | Friday. No. 2. | (not enciphered) |
| 1 | Nz. Pxo Mpwjoh Cpz | MY OWN LOVING BOY |
| 2 | Nboz. uibolt - | MANY THANKS |
| 3 | gps. dbset. pg. | FOR CARDS OF |
| 4 | Xjoetps. Mpwf. | WINDSOR. LOVE |
| 5 | &. L. t.. gspn. | & [Lt..] FROM |
| 6 | Z. P. M. h. Hjsm | Y. O. [M. h.] GIRL |

55 enciphered letters, all decoded by the one key; 4 abbreviation letters kept literal (L, t, M, h). Separator dots follow the card and are not sentence punctuation. Z. P. are treated as enciphered and L, t, M, h as literal because Z. P. has an expansion in the closing slot (Y. O., probably Your Own, which hcp-1366 writes out as `Zpvs. Pxo`), while `Lt..` and `M. h.` have no established expansion either way, so they stay as written. "Ks" for `Lt` remains a hypothesis (uncertainty 3).

Ink that is not text: a grey horizontal streak with a dark upright blot under `gps` (`review/work/c1.png`), which is a smear and a blot, and a long dark line under `Hjsm` running to the card edge (`review/work/g.png`), a pen flourish or card defect. Neither bears a letter. The `-` after `uibolt` is covered in uncertainty 5.

English (the plaintext language; the portal lists Unknown): *"Friday. No. 2. My own loving boy, many thanks for cards of Windsor. Love & Lt.. from Y. O. M. h. girl."*

Slovak: *„Piatok. Č. 2. Môj vlastný milujúci chlapec, veľká vďaka za pohľadnice Windsoru. Láska & Lt.. od Y. O. M. h. dievčaťa."*

`Lt..` and `M. h.` are left unexpanded. Punctuation in the sentences is editorial.

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1363/work/decode.py
```

It checks the SHA-256 of the files in `source/` and `work/hires/`, decodes every token of `work/transcription.json`, checks the inverse round trip and prints the plaintext with the letter counts. It decodes a manual transcription made from the pixels, not the image itself. Crops are in `work/crops/`.

## Uncertainties

1. **`Mpwjoh` (line 1; `work/review1/cmp_mpwjoh_1363.png`).** Replaces the first reading `Mpwfs`. The ink is dark and every sign is present: M, p, w; a stroke rising to a sharp top and falling straight below the line to a hooked foot (j, foot as in `Xjoetps`); a thin closed lens on the baseline (o); a stroke rising from it, turning sharply and falling to a low blob (h, stem and low foot as in `M. h.` on line 6, with the o's exit stroke leading into the top). This h is wider than the line-6 h because of that entry stroke; the same wide form is in accepted `Mpwjoh` on hcp-1361 and 1367. Review 2 tried to refute this on the pixels and could not: the word is accepted on this card.
2. **Sister cards.** hcp-1360 line 1 (FINAL) and hcp-1366 line 1 (DONE2, not yet accepted at the time of writing) now also read `Mpwjoh`. Earlier first readings on those cards differed; this card's old `Mpwfs`, which one review there cited, is withdrawn. I did not change either directory.
3. **`&. L. t..` (line 5; `crops/w6l.jpg`, `faint2.jpg`, `review/work/r2/z_amp_L.png`, `z_tdots.png`).** The ink runs out here. The & is a pale arc joined to a darker slanting stroke, and the L is a very pale hooked, looped capital with a pale stem. Neither would be readable alone; they are identified by matching the shape and slot of `& Lt..` on hcp-1366 and hcp-1371, read on this card's own pale strokes. A dot stands after the & area and another after the L, with a small wedge at the L's foot (ink, no letter); the form `L. t..` matches hcp-1361. The small sign is the same c-like stroke with a dash at its top right, read t by that parallel. It is followed by two marks kept as `..`: the first about twice as wide as the second, with a tail to the lower left, so possibly a dot run into a stroke. The group is literal and stays unexpanded either way; c is not excluded. r is also possible for the small sign, as on hcp-1371. Shifted, the group gives "Ks", which might mean kisses; that is a hypothesis and the plaintext does not use it. Hypothetical support: hcp-1395 reads `M. & L.` in this slot as enciphered, L. & K., editorially "love & kisses".
4. **`Xjoetps`, end (line 4; `crops/windsor.jpg`).** X, j (slash with hooked foot), o, c-shaped e, t (zigzag with a detached dash), p are visible, the p with a pale long stem and bowl. The final s is only a very pale reduced stroke rising to the right from the p's bowl. WINDSOR is otherwise unforced, and no other letter gives a word, but the s is the weakest sign of the word. The stems in this area overlap the pale L of the next line; I have assigned them by direction and ink.
5. **Final t of `uibolt` and `dbset`; dash (lines 2, 3; `crops/cmp0.jpg`).** The last tall stroke of `uibolt` has no bar on the stem, so it is read t on the strength of THANKS. The `-` after it stands about 50 px past the stem (the detached bar of `Xjoetps` is about 10 px off), so it is either a line-filling dash or a displaced t-bar; it is kept as a dash and carries no letter. `dbset`: oval plus tall stem (d), tall stem with bowl (b), then s and e run together, and a final tall stroke with no bar on the stem as t, so on shape alone it is indistinguishable from l. A dot sits up and to the right of that stem (`review/work/c2.png`, about (505,165)), where this hand puts its detached bar; it may be a bar remnant or a stray dot. The same word is `dbset` on hcp-1368 and 1400. The first sign is looped and could look like a capital. The s/e pair is run together, so this word rests partly on the parallel and on the sense.
6. **`pg.` (line 3; `crops/l4b.jpg`).** The p is clear; the g is pale. A dot sits between them, taken as stray; the same word has no such dot on sisters. Other isolated dots near this line are likewise taken as blots or as belonging to the line below.
7. **`Z. P.` (line 6).** Decoded as enciphered initials Y. O., probably "Your Own" in the usual closing slot, but that expansion is an inference and the plaintext keeps the initials. Read as literal, they would be the letters Z. P., which appear in no formula I found.
8. **`M. h.` (line 6; `crops/l7.jpg`, `review/work/f.png`).** The first sign has a long stem and two further downstrokes, three in all, like the M of `Mpwjoh` and unlike the two-stroke N of `Nz` and `Nboz`; compare `M-h` on hcp-1369 and hcp-1367. N is possible, and L for the second sign is not excluded. Kept literal. Shifted: L. g.
9. **Postmark.** The town name is not legible on this card; WIMBORNE on sisters is not assumed here.

## Why it is correct

One fixed shift, not tuned to this card, gives English for all 55 letters. `Nz Pxo Mpwjoh Cpz` = MY OWN LOVING BOY is word for word line 1 of accepted hcp-1360, 1361 and 1367, and `Nboz uibolt gps dbset pg Xjoetps` = MANY THANKS FOR CARDS OF WINDSOR is a fresh sentence, not a stock formula, and suits a couple who exchanged view postcards. Heading, day of the week, and numbering agree with the postmark and with "No. 1." on hcp-1366; the closing follows the formula on hcp-1366 and hcp-1371. The text is short, so the proof rests on the shared key and on THANKS, CARDS and WINDSOR.

## Credits

Solved by Claude Opus 5.5 acting as solver, 2026-10-30. The reading `Mpwjoh` for this card was first suggested in the hcp-1360 reviewer's note and confirmed here on this card's pixels. No earlier work on this number exists. The key and comparison shapes come from sister-card work in this repo (OpenAI GPT solver and Claude Opus 5.5).

## Response to review 1

Verdict REVISE. `python3 -I ciphers/hcp-1363/work/decode.py` re-run after the fixes: hashes pass, 55 enciphered + 4 literal letters, line 1 prints MY OWN LOVING BOY.

1. **`Mpwfs` / LOVER (major): fixed, but differently from the suggested fix.** The review is right that LOVER is unsupported, and I withdraw it. I disagree that the sign should stay unresolved, and with one premise: `Mpwf` is not secure here. The error began one sign earlier. The f of this hand has a closed foot loop (line 4 `Mpwf`, panel 2 of `work/review1/cmp_mpwjoh_1363.png`). The long stroke in line 1 has none: it ends in a hooked foot, which is the j of `Xjoetps` (panel 3). The "small closed loop" I took as the start of s is the o, and the rise, turn and fall to a blob is the h. The outline matches accepted `Mpwjoh` on hcp-1361 and hcp-1367 sign for sign (panels 5 and 6). The hcp-1360 reviewer's note and `hcp-1360/review/work/cmp_mpwjoh.png` pointed to this comparison; I repeated it with my own crops. It also accounts for the same form recurring in this slot, which was the review's decisive point: it is one word, not a single sign, and on hcp-1361 and hcp-1367 the slot holds LOVING, not an initial. Candidates h, z and e are dropped because no separate sign exists. The h candidate of hcp-1360 was close, since the shape does contain the final h. Headline, table, both translations, counts (now 55) and `work/transcription.json` are updated. Because a headline word changed and no reviewer has adjudicated it on this card, I hand it back as DONE2.
2. **First sign of `N. h.` (minor): fixed.** Transcribed `M. h.`, N possible. Literal group, no word changes. The shifted form in uncertainty 8 is corrected to L. g.
3. **t and dash (minor): fixed.** Uncertainty 5 now covers the barless final strokes of `uibolt` and `dbset`, the dot near the `dbset` stem, and the dash after `uibolt`, seen on `review/work/b.png` and `c2.png`. I found no evidence that decides between dash and displaced bar.
4. **`& Lt..` support (minor): fixed.** hcp-1395 and r as an alternative are in uncertainty 3, labelled as hypothesis. The reason for the enciphered/literal split is stated under the transcription table.
5. **Unmentioned marks (minor): fixed.** Both are listed as non-text under the transcription table.

The review's own check `review/work/my_decode.py` retyped `Mpwf?`, so its "whole ciphertext covered" holds for the old segmentation; the re-check should retype this word. The review's sign-by-sign confirmation of `Mpwf` holds for line 4, not for line 1.

## Response to review 2

Verdict ACCEPT. All three findings are minor and none changes a word. I checked them on `review/work/r2/z_pxo.png`, `z_amp_L.png` and `z_tdots.png`. After the fixes `python3 -I ciphers/hcp-1363/work/decode.py` still passes the hashes and gives 55 enciphered + 4 literal letters, with the same plaintext.

1. **Stale uncertainties 1 and 2: fixed.** Uncertainty 1 now records the review's acceptance. Uncertainty 2 gives the present state of hcp-1360 (FINAL, `Mpwjoh`) and hcp-1366 (DONE2, `Mpwjoh`). "Why it is correct" now cites hcp-1360.
2. **Separator dots: fixed.** The crop shows no dot after the o of `Pxo`, so the token is now `Pxo`. It shows a dot after the & area and a dot after the L, plus a wedge at the L's foot, so the tokens are now `&.` and `{L.}`, and uncertainty 3 notes the wedge. `work/transcription.json` is updated, and `work/decode.py` now accepts a dot after the `&` token. No letter is affected.
3. **Description of `t..`: fixed.** Uncertainty 3 now gives the first mark as about twice the width of the second, with a tail to the lower left, possibly a dot run into a stroke. The group stays literal.

The points the review could not verify stay open and are disclosed: the meaning of `Lt..` and `M. h.`, the expansion of `Y. O.`, the postmark town, and the existence of the Windsor cards.
