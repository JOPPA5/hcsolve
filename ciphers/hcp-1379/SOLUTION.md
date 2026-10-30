# HCP 1379 / pc_hcp_60 — Caesar (−1) love postcard, 9 April 1907

Status: **whole message read (52/52 enciphered letters); review 1 verdict ACCEPT, no letter changed.** Solved by Claude Opus 5.5 on 2026-10-30; no earlier work on this number. No published solution of this card was found or used; the portal shows no attached transcription or solution (status Not solved).

## Origin

HC Portal cryptogram 1379. Picture side: Frith's printed view "Loch Long. Highland Cattle", no cipher. Address side: halfpenny Edward VII stamp, postmark WIMBORNE, 10 PM, AP 9 07 (agrees with the portal date 1907-04-09 and the plain heading; 9 April 1907 was a Tuesday, which the command checks). Addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon (the portal spells him "W. Abboú"; metadata unchanged). The grey wheel over the scan is the portal's watermark, not part of the card. The message runs along the left of the address side; rotate 90° counter-clockwise (`work/reading.png`).

Same correspondence as the Caesar cards hcp-1386…1407 (Wimborne, same hand and formulae). English, although the portal says Unknown.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the next letter of the alphabet; decrypt by subtracting one.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading/date line "C. H. Tues. April 9th" is ordinary writing and not shifted (as on hcp-1386, 1390).

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Efbsftu J. ipqf | MY. DEAREST I. HOPE |
| Zpv. bsf. gffmjoh | YOU. ARE. FEELING |
| cfuufs: Mpwf | BETTER: LOVE |
| gspn Zpvs. Pxo | FROM YOUR. OWN |
| Hjsm. | GIRL. |

Plain heading on the card: C. H. Tues. April 9th.

Reading: *"My dearest, I hope you are feeling better. Love from your own Girl."*

Slovak: *„Môj najdrahší, dúfam, že sa cítiš lepšie. S láskou tvoje vlastné dievča."*

(English is both the plaintext and the English translation.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1379/work/decode.py
```

It checks the SHA-256 of the two `source/` scans and the two `work/hires/` originals, decodes every token of `work/transcription.json`, checks the inverse round trip, and prints the plaintext, the letter count and the weekday of the date.

## Uncertainties

1. **`Mpwf`, first letter.** The capital is crowded: arched first stroke, arch into a heavy leg, and a short third stroke crossing it, then a tail into p (`work/crops/w3.png`, `w3color.png`). I read three legs = M, against the two-legged N of `Nz` on line 1 (`work/crops/Nz.png`). It is the least clean letter on the card. Read as N it would give MOVE, which makes no sense here; the same word in the same place on hcp-1397 is read `Mpwf gspn zpvs. Pxo. Hjsm`, with the same outline. The sister card is supporting evidence, not the reading.
2. **`Mpwf`, third letter.** Compressed minims; w is the only one of u/v/w that gives a word.
3. **`gffmjoh`.** The `m` is a small compressed cluster and is the weakest part of the word; g, f, f, j, o, h are clear enough and only L gives FEELING.
4. **`Efbsftu`** and **`cfuufs`.** The `ftu` of the first and the `uu` (four minims) of the second are run together; the outlines fit and `Efbsftu` is frequent on the sister cards.
5. **Split nib.** On `gspn` and the end of `Mpwf` the ink splits into double lines; no letter is affected.
6. **Punctuation** is the writer's dots as seen and partly editorial. The mark after `cfuufs` looks like two dots (taken as a colon); a faint ditto-like mark between `gspn` and `Zpvs` is left out of the transcription as probably not meaningful. Capitals in the transcription are as they look; the translation's punctuation is mine.
7. **"C. H."** in the heading is not expanded. It is plain text and recurs on sister cards; its meaning is unknown. The first initial is also uncertain: a large loop with a low curved finish running into a small descending stroke, so it may be G, not C (sister reviews are divided). The transcription keeps C. Plain text, so the decipherment is unaffected.
8. No restorations: nothing is supplied that is not on the card. Two letters, the `w` of `Mpwf` and the `m` of `gffmjoh`, are chosen by word sense from compressed minims (items 2 and 3); every other letter is read from the strokes.
9. **Pencil "(11)"**, circled, at the upper left of the address side, in a different medium from the message: probably a later collector's or archive number. Not message content and not enciphered.

## Why I believe it is correct

One fixed shift, used by the sister cards of the same couple, turns all 52 letters into a complete, grammatical, ordinary message with no leftover groups. The sentence is a natural message to someone unwell and uses this writer's known formula ("Love from your own Girl", hcp-1397). Postmark, heading and weekday agree.

## Response to review 1

Verdict ACCEPT, three minor findings, all fixed in this file. No change to `work/transcription.json` or `work/decode.py`; no letter of the reading changed. `python3 -I ciphers/hcp-1379/work/decode.py` re-run after the edits: 4 hashes OK, same five lines, 52 letters, Tuesday.

1. **Heading initial C vs G: fixed.** I looked at `review/work/n_head.png`: the descending finish is there and G cannot be excluded. Disclosed in Uncertainty 7; the transcription keeps C, as a stated choice.
2. **"Every letter is read from the pixels": fixed.** Uncertainty 8 now says that `w` and `m` are chosen by word sense. No other letter makes a word in either place.
3. **Pencil "(11)": fixed.** I confirmed it on the address side (`review/work/adr_small.png`). Added as Uncertainty 9 and mentioned in the report.
