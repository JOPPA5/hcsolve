# HCP 1360 / pc_hcp_41 — Caesar shift (+1 written, −1 to decrypt), 3 July 1907

Status: **whole message read; review 1 verdict REVISE, findings addressed (see Response to review 1).** One abbreviation group (2 letters) is kept literal.

Credit: all reading and decoding by Claude Opus 5.5 acting as solver, 2026-10-30. The source capture was by the orchestrator (also Claude Opus 5.5). There is no earlier work on this number. The key and the reading habits come from accepted sister cards (hcp-1366, 1367, 1386…1407), which earlier GPT and Claude sessions solved.

No published solution was used. The portal status is Not solved and it attaches no solution or transcription (`source/metadata.md`); the orchestrator's register check found no record. I did no separate web search.

## Origin

- Picture side: printed "St. Paul's Cathedral, London"; no handwriting.
- Address side (message read rotated 90° counter-clockwise, `work/msg_flat.png`): Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon. The portal spells the recipient "W. Abboú". Farm name read as on the sister cards.
- Halfpenny Edward VII stamp, two strikes of a WIMBORNE postmark, time 10 PM. The date part of the postmark is not legible.
- Plain date at the foot: "July 3rd 07", which agrees with the portal date 1907-07-03. That day was a Wednesday, which agrees with the plain heading "G. H. Wednesday."
- Language: English (portal: Unknown). Same couple and hand as the W. Abbott series.

## Cipher and key

Caesar substitution: each plaintext letter is written as the next letter of the alphabet. To decrypt, subtract one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "G. H. Wednesday." and the date are in clear. The group `M. h.` is an abbreviation and is kept literal, as on sister cards (`M-h` on hcp-1367 and hcp-1369).

## Transcription and plaintext (all ciphertext on the card)

| Line | Ciphertext | Plaintext |
|---|---|---|
| heading (clear) | G. H. Wednesday. | G. H. Wednesday. |
| 1 | Nz. Pxo. Mpwjoh Cpz | MY OWN LOVING BOY |
| 2 | J. Gffm wfsz | I FEEL VERY |
| 3 | Ejtbqqpjoufe. up | DISAPPOINTED TO |
| 4 | Ebz. "Op Mfuufs". | DAY "NO LETTER". |
| 5 | Zpvs. **M. h.** Hjsm. | YOUR [M. h.] GIRL. |
| date (clear) | July 3rd 07. | July 3rd 07. |

56 enciphered letters, all decoded by the one key; 2 abbreviation letters kept literal.

Reading (line-end "to / day" = "to-day"):

- English: *"My own loving boy, I feel very disappointed to-day: 'no letter'. Your [M. h.] girl."*
- Slovak: *„Môj vlastný milujúci chlapec, dnes som veľmi sklamaná: ‚žiadny list'. Tvoje [M. h.] dievča."*

The group is not expanded in either version.

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1360/work/decode.py
```

It checks the SHA-256 of the files in `source/` and `work/hires/`, decodes every token of `work/transcription.json`, checks the inverse shift, prints the plaintext with the letter counts and writes `work/plaintext.txt`. It decodes a manual transcription of the pixels, not the image itself.

## Uncertainties

1. **`Mpwjoh` (line 1; `review/work/cmp_mpwjoh.png`, `z_mpwf.png`).** M, p and w are clear, the w compressed. The last three signs are pale, written while the pen was failing, and part of them lies on a watermark band. Their outline is still that of the accepted word on hcp-1361 and hcp-1367: j as a long stroke with a foot under the line, o as a thin closed lens, h rising, turning sharply and falling to a dark blob. My first reading `Mpwf` + `h.` was wrong (see Response to review 1).
2. **`Op` (line 4; `review/work/z_O.png`).** The O is pale and crosses a watermark band. It is a stem rising to a tip, a thin arch to the right and a short return stroke, with no closed loop like the O on hcp-1366. `Op` = NO rests on the sense ("disappointed", then LETTER); I have no better reading. The p is clear.
3. **`M. h.` (line 5; `work/crops/f_nh.png`, `review/work/z_nh2.png`).** The first sign has an arched stem and two further short strokes, one more than the N of `Nz`, so it is transcribed M, the build of `M-h` on hcp-1367 and hcp-1369. N stays possible. The second sign is a tall stroke with a short hump, preferred as h; L stays open because the same slot is read L on some sisters. Kept literal and not expanded, and it is unknown whether the group is enciphered; shifted it would be L. g. A round spot on the band after the first sign may be the period or foxing, and no certain period follows the h. No word depends on this.
4. **`Pxo` (line 1; `work/crops/z_pxo.png`).** The P has a long flourish that runs into the underline. The x is two crossing strokes merged with the foot of the P. The o is clear. Only OWN fits, and it is the stock opening of the series.
5. **`Ejtbqqpjoufe` (line 3; `g3a`–`g3c` crops).** The j and the t are entangled with the descenders of `Gffm` above, and the second j is pale. All twelve letters are placed, and no other English word fits this length and pattern (q q, f e).
6. **Quotation marks.** Two clear ticks after `Mfuufs`. Marks before `Op`, under the line 3 descenders, are less sure: part of them is the foot of a j from line 3, and two opening ticks remain plausible. I read quotation marks around "no letter"; the writer also quotes phrases on sisters (hcp-1386, 1380). No letter depends on this.
7. **"to / day".** `up` ends line 3 and `Ebz` opens line 4. The sisters write `up-Ebz`. No hyphen is visible here.
8. **Heading.** The heading initials read G. H.; some sisters have C. H. The heading is not part of the cipher.
9. **Postmark date** is not legible; the date rests on the writer's plain date and the portal.

## Why I believe it is correct

One fixed shift, not tuned to this card, gives English for all 56 letters. The 12-letter `Ejtbqqpjoufe` = DISAPPOINTED and the double `ff`, `qq`, `uu` patterns cannot arise by chance. The message is a fresh sentence, not just the couple's formula, and it is coherent: she feels disappointed because no letter came to-day. The opening `Nz Pxo Mpwjoh Cpz` is word for word that of hcp-1361 and hcp-1367, the closing `Zpvs M. h. Hjsm` matches the formula of the series (hcp-1367, 1369), and the weekday, plain date and portal date agree.

## Response to review 1

Verdict REVISE. All five findings are addressed. I re-examined `review/work/cmp_mpwjoh.png`, `z_mpwf.png`, `z_nh2.png` and `z_O.png` myself before changing anything.

1. **Major, `Mpwf` + `h.` is `Mpwjoh`: fixed, I agree.** After `Mpw` the ink shows a long stroke falling to a foot under the line, a thin closed lens on the baseline, and a stroke rising, turning and falling to a dark blob. Those are j, o, h, with the same outline as the accepted word on hcp-1361 and hcp-1367. My stated rejection, "no o loop and no final h", was wrong: I had taken the j for the stem of f and the o and h for a separate sign. The transcription, table, reading and both translations now read MY OWN LOVING BOY, and uncertainties 1 and 2 are rewritten as a pale-ink disclosure. The old reading stays on record as a dead end in `NOTES.md`.
2. **Major, headline and coverage claims: fixed.** Status, table note and the closing argument now say one literal group (2 letters) and 56 enciphered letters. `python3 -I ciphers/hcp-1360/work/decode.py` reports 56 and 2, and `work/plaintext.txt` was regenerated.
3. **Minor, the O of `Op`: fixed.** It is now uncertainty 2. The shape in `z_O.png` is as the reviewer says, so the capital rests on context.
4. **Minor, `N. h.` to `M. h.`: fixed.** I count the same three strokes in `z_nh2.png`. Transcribed `M. h.`, N stays possible, and the spot after the first sign and the missing certain period are disclosed.
5. **Minor, opening quotation ticks: fixed.** Uncertainty 6 now notes the j foot.

The reviewer's note on hcp-1363 and hcp-1366 concerns other directories, so I changed nothing there.
