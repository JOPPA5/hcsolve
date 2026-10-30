# HCP 1359 / pc_hcp_40 — Caesar −1 English love postcard, 9 May 1907

Status: **whole message read; review 1 (ACCEPT) addressed.** The capital of `Foe` = END rests on sense and a form parallel; the closing group `M. & L.` and a trailing `t` are kept literal and unexpanded, as on hcp-1361. See the Response to review 1.

> **My own dearest, I am about the end of this stock. M. & L. [t] From your own girl.**

## Origin

HC Portal cryptogram 1359 (`pc_hcp_40`), portal status *Not solved*, no transcription or solution attached (`SOURCES.md`, `source/metadata.md`). No published solution of this card was found or used. Picture side: printed view "The Promenade and Beach. Morecambe", no handwriting. Address side: E.S. London No. 468, halfpenny Edward VII stamp; postmark on the stamp shows "…ORNE" (partly), 10 PM and 9, month and year not legible on this scan (`work/crops/stamp.png`). By parallel with hcp-1392 of the same day (`[WI]MBORNE 10 PM MY 9 07`) the office is probably Wimborne; that name and the month and year come from the sister card, not from this scan. Addressed in clear to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (portal spelling "W. Abboú"; metadata left unchanged). Plain heading "G. H. Thursday." and plain date "May 9th 07": 9 May 1907 was a Thursday, and the date agrees with the portal. The grey A–Z disc and building logo are a scanning overlay. The same writer sent hcp-1392 on the same day ("Sending a card to Y— instead of letter"); the formulae `Nz Pxo Efbsftu` and `Gspn zpvs pxo … Hjsm` recur on the accepted sister cards.

## Cipher and key

Monoalphabetic Caesar shift, as on hcp-1386…1407: each plaintext letter is written as the **next** letter of the alphabet; decrypt by subtracting one.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext (all writing in the message area; rotate 90° counter-clockwise, `work/crops/reading.png`)

| Ciphertext | Literal plaintext |
|---|---|
| *(plain)* G. H. Thursday. | G. H. Thursday. |
| Nz. Pxo. Efbsftu | MY. OWN. DEAREST |
| J. bn. bcpvu. uif | I. AM. ABOUT. THE |
| Foe. pg. uijt | END. OF. THIS |
| tupdl. M. & L. t | STOCK. [M. & L.] [t] |
| Gspn. Zpvs. Pxo | FROM. YOUR. OWN |
| Hjsm. | GIRL. |
| *(plain)* May 9th 07 | May 9th 07 |

52 cipher letters decoded with the one key; 3 letters (`M`, `L`, `t`) kept literal.

English (the plaintext language; the portal lists Unknown): *"G. H., Thursday. My own dearest, I am about [at] the end of this stock. M. & L. [t]. From your own girl. May 9th 07."* The likely sense is that she is nearly out of this stock of postcards. That is an inference: the card does not say what the stock is.

Slovak: *„G. H., štvrtok. Môj najdrahší, som asi na konci týchto zásob. M. & L. [t]. Od tvojho vlastného dievčaťa. 9. mája 1907."*

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1359/work/decode.py
```

It checks the SHA-256 of the four image files, decodes every cipher token of `work/transcription.json`, checks the inverse round trip, and prints the plaintext, the counts and the alternative for the uncertain sign.

## Uncertainties

1. **Capital of `Foe` = END (weakest point; `work/crops/z_cap.png`).** The sign is a large left curl running into a stem, plus a long stroke at the writer's usual slant rising from the foot. Its outline is V-like, and read literally as V the word is `Voe` = UND, not a word. It is not the writer's plain F, which has an arch and a crossbar (`work/crops/cmp_Friday_hcp1368.png`), and it has no crossbar here. It is also not his two-stem capital V of `Vtvbm` on hcp-1373 (`work/crops/cmp_Vtvbm_hcp1373.png`), which has no such left curl. The enciphered capital F of `Fbsmz` = EARLY on hcp-1355 has the same construction: left curl, arch over into a stem running down-left to a foot, and a long straight stroke rising up-right. Here the rising stroke leaves the stem lower, which gives the V-like look (`review/work/cmp_F_1355_vs_1359.png`). hcp-1355 is not closed, so this is a parallel, not an accepted control. F therefore rests on that form parallel and on sense: END is the only word found that fits the following `oe` and "about the … of this stock".
2. **Third letter of `Foe`.** A small sign with a filled eye, read e; c would give ENB, not a word. No other lowercase e occurs on this card for comparison.
3. **`bcpvu` = ABOUT (`work/crops/z_about.png`).** The c has a small top flag and a hairline to the long p stem, which sits close to the following signs. The strokes can be misread as `befpvu`, which gives no word.
4. **`Efbsftu` (`work/crops/z_dear.png`).** The s here is c-shaped, not the clearer s of `Gspn` and `Zpvs`. The final letters are pale; the long bar above is the crossing of t. The formula word is also on hcp-1392 of the same day.
5. **`uijt` (`work/crops/z_this.png`).** The last letter is the uncrossed t recorded on hcp-1387. Of the three dots nearby, two belong to i and j. The third sits level with the top of the t and to its right, not low like this card's periods, so it may be a detached t-crossbar like the dash of the trailing `t`, which would support t. It is slightly rounder than that dash, so this is not certain. It has no effect on the plaintext.
6. **`M. & L.`** is kept literal and unexpanded. The capital was first recorded as N. It has hook, stem, leg and a further short stroke, one more than the one-legged N of `Nz` on this card (`review/work/z_caps_N2.png` against `z_caps_N.png`), so it is transcribed M, the same test used on hcp-1361 and hcp-1368. The extra stroke is short, so N is not fully excluded; hcp-1392 of the same day and others report `N & L`. Shifted, the group gives L. & K. Finished cards treat it two ways: as enciphered (hcp-1368 `M. & L.t` = L. & K.S; hcp-1395 `M. & L.` = L. & K., both read as probably "love and kisses") or as literal (hcp-1361, hcp-1407). "Love and kisses" is a family hypothesis and is not claimed for this card.
7. **Trailing `t` (`work/crops/z_Lt.png`).** A curved stroke with a detached short dash at its top right, read as t by parallel with hcp-1368 (FINAL, with a clearly crossed t) and hcp-1366 (not closed, same stroke with dash). hcp-1392, of the same day, has no t. It may instead be a mark. It is not counted as a decoded letter. If the group is enciphered, as on hcp-1368, it is the S of L. & K.S.
8. **Stroke before `Hjsm` (`work/crops/z_tail.png`).** A long, dry, pale curve with a dark foot stands just after the date. It is treated as a pen stroke or bracket separating the date, not as a letter. A closing slot before "Girl" exists on some sister cards (`N^b` on hcp-1392), so a lost abbreviation is not excluded; nothing readable is there.
9. **Sense of "about the end".** The phrase lacks "at"; the reading is literal.
10. **Dots** are as in the manuscript; `tupdl` has two dots after it. Their value is not significant.

## Why I believe it is correct

One fixed shift, unchanged from the accepted cards, gives English for all 52 letters, including non-formula words ABOUT, THE, OF, THIS and STOCK. The sentence is fresh, not one of the couple's stock phrases, and it fits a writer who is sending a card every day. The frame "My own dearest … from your own … girl" and the heading/date agree with the sister cards and the calendar. The one letter that needed a judgement, the F of END, is disclosed above.

## Credit

Transcription and decipherment by Claude Opus 5.5 on 2026-10-30; no earlier work exists on this number. Key and family parallels come from the accepted sister cards in this repo.

## Response to review 1

Verdict ACCEPT. I rechecked each finding on the scans and crops; none changed a decoded letter. The reproduction command was re-run after the edits: source hashes OK, 52 cipher letters, 3 literal, round trip OK, same six rows apart from the literal capital below.

1. **Sister capital F: accepted, fixed.** I compared `review/work/cmp_F_1355_vs_1359.png` myself. The construction agrees, the rising stroke leaves lower here, and both differ from the V of `Vtvbm`. Uncertainty 1 and "Why I believe it is correct" are corrected; hcp-1355 is cited as a parallel because it is not closed.
2. **"Accepted sister cards" for the t: accepted, fixed, with one update.** Since the review, hcp-1368 has been closed (FINAL), so the review's statement that it is open no longer holds. hcp-1366 is still open. Uncertainty 7 now says which is which, and that hcp-1392 has no t.
3. **Third dot near `uijt`: accepted, fixed.** On `review/work/z_uijt.png` the mark is level with the top of the t. Uncertainty 5 now says it may be a detached crossbar, uncertain.
4. **Postmark: accepted, fixed.** Wimborne is added in Origin, labelled as taken from hcp-1392. The crop shows only "…ORNE", 10 PM and 9.

**One change beyond the findings, not re-reviewed.** While checking finding 2 I read the final state of hcp-1368, whose closure came after this review. It rejects N for this group by counting downstrokes. Applied to this card, the group capital has one more stroke than the N of `Nz`, so the literal group is now `M. & L.`, not `N. & L.`, and `work/transcription.json` was updated. The review had noted that M is not excluded. This is one letter inside a literal, unexpanded group, it changes no decoded letter or the count, and the group stays literal. Uncertainty 6 records both family treatments.
