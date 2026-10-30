# HCP 1355 / pc_hcp_36 — Caesar (+1) love postcard, 30 March 1907

Status: **whole message read (81 enciphered letters); two writer's spellings and a few disclosed sign-level points below.** Solver: Claude Opus 5.5, 2026-10-30. There was no earlier work on this number. No published solution of this card is known or was used: the portal shows Not solved with no attached transcription or solution (`source/metadata.md`, `SOURCES.md`), and the orchestrator's register check found no record. No separate web search for this card was made.

## Origin

Picture side: printed view "English Lakes. Honister Crag" (the caption's last word looks like "Cray" at this size), no handwriting. Address side: Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (portal spelling "W. Abboú"), halfpenny Edward VII stamp, postmark WIMBORNE / 10 PM / MR 30 / 07, matching the portal date 1907-03-30. That day was a Saturday, as in the plain heading, and the postmark hour fits "evening". The next day, 31 March 1907, was Easter Sunday (computed), which fits an early church service on Sunday morning. Language: English (portal: Unknown).

## Cipher and key

Caesar shift, the same one used on the W. Abbott series (for example hcp-1386, 1407): each plaintext letter is written as the next letter of the alphabet. Decrypt by subtracting one, A→Z.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading is ordinary writing and is not shifted. The message is written across the left half of the address side; read it with the card turned 90° counter-clockwise (`work/reading.png`). Line 6 begins in the far left margin, beyond the printed text.

## Transcription and plaintext

| Line | Ciphertext | Plaintext |
|---|---|---|
| heading (clear) | C. H. Saturday evening. | C. H. Saturday evening. |
| 1 | Nz. Efbsftu. kvtu | MY. DEAREST. JUST |
| 2 | Cffo. gps. b. tuspmf | BEEN. FOR. A. STROLE |
| 3 | J. bn. hpjoh. up | I. AM. GOING. TO |
| 4 | Fbsmz. Tfswjdf. | EARLY. SERVICE. |
| 5 | Tvoebz. Npsjoh | SUNDAY. MORING |
| 6 | Xjui Mpwf. Gspn. zpvs | WITH LOVE. FROM. YOUR |
| 7 | Hjsm. | GIRL. |

Reading (spelling normalised): *C. H. Saturday evening. My dearest, just been for a stroll. I am going to early service Sunday morning. With love from your girl.*

English is the original language.

Slovak: *C. H., sobota večer. Môj najdrahší, práve som bola na prechádzke. Idem na rannú bohoslužbu v nedeľu ráno. S láskou tvoje dievča.*

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1355/work/solve.py
```

It checks the SHA-256 of the files in `source/` and `work/hires/` against `work/source-sha256.json`, then decodes `work/transcription.json` with the key and prints each line and the count of 81 letters.

## Uncertainties

All are in the literal transcription as stated. The writer's spellings are not altered in the decode; they are normalised only in the Reading.

1. **MORING (`Npsjoh`).** Literal plaintext lacks the syllable NI/NO. After `s` come the long `j` stroke (its tail curls back below the line), a round `o`, then `h`, the same sequence as the end of `hpjoh` in line 3. No `o` fits in the gap between `s` and `j`. Read as the writer's slip for MORNING.
2. **STROLE (`tuspmf`).** Between `p` and the final long `f` the strokes count as one `m`, but they are cramped and heavily inked, so `tuspmmf` (STROLLE) cannot be excluded. Either way the word is taken as "stroll".
3. **Final `s` of `gps`.** Only a dark blob survives where the pen ran dry; this stretch of the line is very faint. It is read as `s` because FOR is the only fit, so treat it as close to a restoration. The separate short dash after it is the writer's stop.
4. **Capital `F` of `Fbsmz`.** No sister card gives a capital cipher F for comparison. The sign is a bowl on a long diagonal stem running up to the right, which differs from the `G` of `Gspn` (the stem stops at the bowl) and matches the second `f` of `Cffo`. If it were a G the word would be FARLY, which is not a word.
5. **Heading initial.** It may be G instead of C: the sister cards are themselves divided between "C. H." and "G. H." It is clear text, reported as written and not expanded. Its last word is dark but cramped: the first strokes rise high and the later letters run together, so "evening" is a probable reading, not a clear one, supported by the 10 PM postmark. It is clear text, outside the 81 letters.
6. **`X` of `Xjui`.** The `X` is the crossed sign only. The large hook below it is the tail of the following long `j`, a stroke rising from the hook to the top right, the same form as in `hpjoh`, `Tfswjdf` and `Npsjoh`. The word therefore has its four letters with no unusual form. The fit is also supported by the identical phrase `Xjui Mpwf. Gspn` in the transcription of hcp-1356 (hypothesis from that card; this card's strokes were read independently). The `i` carries a detached dot.
7. **Faint strokes.** The ink fades patchily in `gps`, `tuspmf`, `Tfswjdf`, `Mpwf` and `Hjsm`. Apart from point 3 and the `w` of `Mpwf`, the letter shapes remain visible. That `w` is a pale grey smudge and one short dark stroke running on to `f`, so its form cannot be read in full as it can in `Tfswjdf`; it is read partly from fit. LOVE is safe, since `M`, `p` and `f` are clear.
8. Unlike many sister cards, this one has no `Pxo` and no initial groups (E. L., N. & L.); none were omitted.

## Why I believe it is correct

One fixed shift, with no card-specific adjustment, turns all 81 letters into English, including long words (DEAREST, SERVICE, SUNDAY, GOING, EARLY). The sentence is coherent and uses the couple's phrases (MY DEAREST, FROM YOUR GIRL). Saturday evening agrees with the postmark, and early service on Sunday morning agrees with the following day being Easter Sunday, a fact not used in the decipherment. Hand, addressee, Wimborne postmark and period match the accepted cards in this series.

## Response to review 1

Verdict ACCEPT, no blocker or major findings. I checked each finding against the reviewer's crops of the hires scan and agree with all four. No cipher letter, line or stop changed.

1. **`w` of `Mpwf` (minor): fixed.** `review/work/z_love.png` shows a pale smudge plus one short dark stroke. Uncertainty 7 now names it next to the `s` of `gps` as a sign-level weak point.
2. **`X` of `Xjui` (minor): fixed.** `review/work/c_l6a.png` shows the long stroke rising from the hook to the top right, so the hook belongs to `j`. Uncertainty 6 is corrected and reduced.
3. **Last word of the heading (minor): fixed.** `review/work/y_even.png` shows dark, cramped writing, not faint. Uncertainty 5 now says cramped and probable.
4. **Line number (minor): fixed.** The note in `work/transcription.json` now says line 6. SOLUTION.md was already right.

After these edits `python3 -I ciphers/hcp-1355/work/solve.py` still prints "source hashes OK", the same seven lines and "81 enciphered letters decoded".
