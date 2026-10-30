# HCP 1353 / pc_hcp_34 — Caesar −1 English note, 7 Feb 1907, signed "Loo"

Status: **whole message read; independent review 1 verdict ACCEPT; four minor findings addressed, no letter changed.** All work on this card by Claude Opus 5.5 (2026-10-30); there is no earlier work on this number. No published solution was found or used; the portal attaches none (status Not solved, see `SOURCES.md`).

> **Just a little surprise from Loo.**

## Origin

Picture side: printed view "The Minster & Grammar School, Wimborne", no cipher. Address side: halfpenny Edward VII stamp, postmark WIMBOR[NE] 10 PM FE 7 07 (the end of the town name is off the visible arc; the printed view and the sister cards make it safe), addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (portal spelling of the recipient: "W. Abboú"). The portal date 1907-02-07 agrees. The message is on the left half of the address side, written along the card; rotate 90° counter-clockwise (`work/reading.png`).

The same addressee and origin, and the same key, occur on the Caesar cards hcp-1355…1407. The signature `Mpp` also occurs on hcp-1398.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Plaintext |
|---|---|
| kvtu. b. mjuumf | JUST. A. LITTLE |
| tvsqsjtf. gspn. Mpp | SURPRISE. FROM. LOO |

26 enciphered letters, all decoded by the one key. Dots are the writer's word-dots and carry no meaning.

Not enciphered: "Feb. 7th 1907" along the left edge, and a pencilled "(1)" at top left (probably a later owner's number; not interpreted).

**English (original language):** "Just a little surprise from Loo." (dated Feb. 7th 1907)

**Slovak:** „Len malé prekvapenie od Loo." (7. februára 1907)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1353/work/solve.py
```

It checks the SHA-256 of the files in `source/` and `work/hires/`, decodes `work/transcription.json`, checks the inverse round trip, and prints the plaintext.

## Uncertainties

1. **`b` looks like a digit 6.** Taken alone it could be a 6, or a shifted 5 ("just 5 little…"). I read it as cipher `b` = A. The `b` of the plain "Feb." on this same card has the same shape (ascender plus closed low bowl; `review/work/date.png`), which is the best evidence. The identical phrase `b. mjuumf` also stands on hcp-1375 (FINAL), and SURPRISE is singular, which excludes a number above one.
2. **`tvsqsjtf` is the hardest group, and its end has no final `t`.** It lies over the printed grey watermark, and the ink is thin. `t`, `v`, `s` are clear. `q` is a bowl with a tail. `s` is heavy but clear. `j` is the long descending looped form, as in `mjuumf` on line 1. The next `t` has its top bar at the right and a stem running down-left to a hooked foot; the stem is longer than the `t` of `kvtu`, which is the one unusual shape in the group. The last sign is the same `f` as in `mjuumf` (ascender, descending loop, right-hand bar). I find no further letter after it, so the group is SURPRISE, not SURPRISES (the bar of the `f` might be taken for one by a reader who expects a plural). See `work/crops/l2a.png`, `work/crops/surp.png`.
3. **`Mpp`.** The second `p` stands in much fainter ink, probably as the pen ran dry, and each `p` has a dot-like mark inside the bowl. The first `p` lies over the grey watermark band. Both have the stem and right-hand bowl of the `p` in `gspn`. The capital is compressed, but at 10x it has a looped first stroke and three feet (left, short middle, right; `review/work/m.png`), so it is an `M` and matches the looped capital of the `Mpp` signature on hcp-1398 (`../hcp-1398/work/closing.png`). The only alternative, capital `N`, would give `Npp` = MOO, a conceivable pet name (hcp-1352 records M.O.O as a literal alternative), but the stroke count and the hcp-1398 signature exclude it here. See `work/crops/tail.png`. "Loo" as a pet name (perhaps for Louie or Louisa) is conjecture.
4. **Final `u` of `kvtu`.** Its minims end in a raised finial, so a `w` shape is conceivable, but `kvtw` decodes to nothing; the same word `kvtu` is on hcp-1383 (FINAL) and hcp-1370 (review verdict REVISE, not closed).
5. The nature of the "surprise" is not stated. The card itself may be it; that is my inference only.

## Why it is correct

One fixed shift, not tuned to this card, gives a complete grammatical English sentence from all 26 letters. The key is the one established on the Abbott cards closed after review: `kvtu` recurs on hcp-1383, `b. mjuumf` on hcp-1375, `gspn` on both, and `Mpp` on hcp-1398 (all FINAL as of 2026-10-30), while `tvsqsjtf` is a fresh word that no formula predicts. Wimborne postmark, addressee and date fit the correspondence.

## Credits

Scans and metadata captured by the orchestrator (Claude Opus 5.5), 2026-10-30. Transcription and decipherment by Claude Opus 5.5 as solver. The key and the sister readings come from the cards named above, which were read earlier in this repo.

## Response to review 1

Verdict ACCEPT. All four findings are minor and I addressed all of them. No letter of the ciphertext or plaintext changed.

1. **Word dot after `tvsqsjtf`: fixed.** I see the faint dot on the reviewer's `review/work/d.png` and on `work/reading.png`, between the end of the `f` and the `g`. It is now in `work/transcription.json` and in the table above: `tvsqsjtf. gspn. Mpp`.
2. **"Accepted Abbott cards": fixed.** "Why it is correct" now names only cards that are closed and says which word each supplies. Marker states have moved since the review: hcp-1375, 1383 and 1398 are now FINAL. hcp-1370 has review verdict REVISE and is not closed, so uncertainty 4 labels it that way.
3. **Capital of `Mpp`: fixed.** I agree with the reviewer's count on `review/work/m.png`: a looped first stroke and three feet. Uncertainty 3 now says so, states that `Npp` gives MOO, and excludes it on the stroke count and the hcp-1398 signature.
4. **Evidence for `b`: fixed.** Uncertainty 1 now leads with the `b` of "Feb." on this card (`review/work/date.png`).

Re-run after the fixes: `python3 -I ciphers/hcp-1353/work/solve.py` prints `source hashes OK`, `tvsqsjtf. gspn. Mpp → SURPRISE. FROM. LOO` and `26 enciphered letters decoded; round trip OK`.
