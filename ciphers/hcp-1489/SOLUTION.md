# HCP 1489 (pc_hcp_170): null cipher, a birthday greeting

Postcard ("Clifton" Post Cards, E. W. Savory, Bristol, hand-coloured series 0361; ½d Edward VII stamp; HULL machine postmark, 8.45 PM, AUG, year digits not fully legible) to Miss A. Stainforth, 61 Hopwood Street, Freehold Street, Hull. The message is seven lines of printed capitals on the left of the address side, a cursive signature, and printed "LET." after it. Portal status when captured: Not solved; no transcription or solution attached; no published solution of this card was found.

## Cipher type and key

**Null cipher (letters of the plaintext kept in order, with meaningless letters inserted).** There is no substitution: every plaintext letter stands as itself. Between plaintext letters the writer inserted one to several null letters, and he also split the line into decoy "words" (e.g. `OTU TH VIX LOV AI ESS`, `OUT WTOFE`, `THUS`). The key is the set of signal positions, given in `work/key.json`. In the lines below, CAPITALS are plaintext and lowercase letters are nulls:

| Line | Letters in sequence, card spacing removed | Plaintext |
|---|---|---|
| 1 | `sDEolAReuNANvostilar` | DEAR NAN |
| 2 | `ugivWIoTutHvixLOVaiEss` | WITH LOVE |
| 3 | `rANDliBESToviWIroSHdlESoi` | AND BEST WISHES |
| 4 | `vFxOlRzYO2vUReuBjpIRTHus` | FOR YOUR BIRTH- |
| 5 | `oDpArYyyFogROqlMiarn` | -DAY FROM |
| 6 | `wYlyOnnUuvRospioutwtofe` | YOUR |
| 7 | `wriorbbkir` | (nulls) |
| | signature, cursive: *Jick* | Jick |
| | printed after the signature: `LET.` | (unexplained, see uncertainties) |

The card's own spacing (approximate, read from work/message.jpg) is a decoy that cuts across the plaintext words, but it sometimes exposes them, as with `NAN`, `WI`, `TH`, `RAND`:

```text
1  S DE OLAR EU NAN VOSTILAR
2  UGIV WI OTU TH VIX LOV AI ESS
3  RAND LI BESTOVI WIROSHDLESOI
4  VFXOLRZYO 2 VUREUBJPIRTHUS
5  ODP ARYYY FOGROQLM IARN
6  WYLY ONNUUVROSPI OUT WTOFE
7  WRIORBB KIR      (signature: Jick)   LET.
```

## Plaintext

**English (original):** Dear Nan, with love and best wishes for your birthday, from your Jick.

**Slovak:** Milá Nan, s láskou a najlepšími želaniami k narodeninám, tvoj Jick.

(The word "Jick" is the cursive signature, written outside the cipher; it is reported literally.)

## Command (from the repository root)

```sh
python3 -I ciphers/hcp-1489/work/decode.py
```

It checks the SHA-256 of all three files in `source/` against `work/source-sha256.json`, applies `work/key.json` to `work/transcription-v2.json`, prints each line with plaintext in capitals and nulls in lowercase, asserts that the extracted letters equal the stated words, prints the plaintext, and runs a seeded chance test (2000 random reorderings of the same 144 signs).

## Transcription

My own reading of `source/address-large.jpg` (rotated, 5x enlarged crops of every line), in `work/transcription-v2.json`: 144 signs in 7 lines. Differences from the earlier transcription (`work/transcription.txt`, GPT):
- The leading `I` of lines 1, 2 and 3 is not part of the message. In lines 1 and 2 it is the sideways `L` and `H` of the HULL postmark, which lies over the line starts; in line 3 it is the end of the printed underline below "Carte Postale" (see review/work/l3start.png). Omitted.
- Line 1 sign 5 is an `L` with a stroke through it (GPT read `E`); line 4 sign 17 is read `J` but has a top hook and may be `S`. Both are nulls either way.
- Line 4 reads `VFXOLRZYO2VUREUBJPIRTHUS`: the 4th sign is a narrow O (not Q), the 13th an overwritten R (not Q).
- `LET.` after the signature is kept apart from line 7.

## Uncertainties

1. **"NAN" or "DEAREST"** (line 1). Line 1 reads `SDEOLAREUNANVOSTILAR`, spaced on the card approximately as `S DE OLAR EU NAN VOSTILAR`. Two readings are possible and they exclude each other, because N-A-N (signs 10-12) lies between the E (sign 8) and the S-T (signs 14-15) of DEAREST:
   - **DEAR NAN** (adopted): N-A-N stands as its own visible group directly after DEAR, where the addressee's name belongs; Nan is the usual pet form of Ann/Annie, and the recipient is Miss A. Stainforth.
   - **DEAREST** (alternative): D-E-ol-A-R-E-unanvo-S-T, 7 letters in 15 signs, with NAN then a null run. "Dearest, with love and best wishes ..." is equally good English.
   Chance tests (decode.py, 2000 reorderings of all 144 signs): DEAREST within 15 signs 0/2000; NAN within 3 signs 30/2000. That comparison favours DEAREST, but it is not like-for-like (a 7-letter subsequence against a 3-letter one, anywhere in the card). A matched test (work/salutation_test.py: DEAR kept fixed, the other 137 signs shuffled, 20000 trials, looking only at the 9 signs after DEAR) gives E-S-T in order 1.0 % of the time and N-A-N as an adjacent group 0.04 % of the time; on the card both occur. Neither is plausibly chance on its own, so the choice rests on the layout and the address: NAN is the writer's own visible group and matches the recipient. The rest of line 1 (`VOSTILAR`) and the start of line 2 (`UGIV`) give no further word under the adopted reading; under DEAREST, `OSTILAR`'s S-T would be signal letters.
2. **Null runs.** After FROM YOUR the card has 22 more letters (`OSPIOUTWTOFE WRIORBBKIR`) plus `LET.`. A word search with the 3000 commonest English words found no coherent continuation (only accidental fragments like OUT, OF, TO, which the writer seems to have planted as decoys, as he did with THUS and TH). I treat them as nulls and the cursive signature as the end of the sentence ("from your Jick"). `LET.` is printed in the same capitals after the signature; its purpose is unknown (padding, or a private abbreviation). If any of these runs carries meaning, it is not in this solution. Put plainly: **the words after FROM YOUR are not established.** The reading "from your Jick" assumes the signature completes the sentence; the 22-letter tail could hold a word the writer meant, but none was found (YOURS TRULY does not occur in it; LOVINGLY occurs only spread over 79 signs, which is meaningless).
3. **Choice of positions.** Where the same letter occurs twice in a short span (e.g. WI-o-T-ut-H or WI-otu-T-H) the exact position of a plaintext letter is a matter of choice; the key takes the earliest one. This does not change the plaintext.
4. **Overwritten signs.** In line 4 the `O` after `Y` and the `R` after `U` are written heavily over another stroke (corrections); they are read O and R. The `2` in line 4 is a digit, a null.
5. **Signature.** A cursive capital with a top loop and a long descender (J form), a dotted i, c, k: read *Jick*. The portal capture (source/metadata.md) and the earlier GPT notes say "Jack"; on a 5x crop (review/work/signature.png) the second letter has a clear separate dot and no closed bowl, so it is an i, and "Jack" is rejected, though a mis-dotted a cannot be fully excluded. *Dick* cannot be excluded either if the writer formed his D in this way.
6. The postmark year is not fully legible; the card is Edwardian (Edward VII ½d stamp, so 1902–1910).

## Why it is correct

- The 36 letters WITH LOVE AND BEST WISHES FOR YOUR BIRTHDAY occur in order within a 73-letter stretch of the card; in 2000 random reorderings of the same 144 signs this phrase never fits into a window that short (decode.py output). The same holds for FROM YOUR (8 letters in 23 signs, 0/2000). These cannot be chance.
- DEAR stands at the very start (D-E-ol-A-R), as the salutation must.
- The result is a complete, ordinary Edwardian birthday greeting: salutation, wish, closing, signature. No substitution or other key is needed, and no letter is changed.
- An earlier monoalphabetic hill-climb (this session, English quadgrams) gave no English, and the letter frequencies (many V, Y, Q, W, U) fit random filler mixed into English rather than a substitution.

## Credit and earlier work

The images were captured and the first transcription and route-transposition tests (rail fence, grid routes, skips; none gave a reading) were made by an OpenAI GPT solver on 2026-10-26 (see NOTES.md, `work/try_routes.py`, `work/route-results.json`). The null-cipher identification, the revised transcription and the reading are by Claude Opus 5.5, 2026-10-30.

## Response to review 1

Review 1 (verdict REVISE) accepted the body of the reading and asked for disclosure fixes. Each finding:

1. **(major) DEAREST not disclosed.** Agreed and fixed. Uncertainty 1 now lists "Dearest, with love ..." as the alternative salutation, explains that it and NAN exclude each other, and states both statistics. I added DEAREST to the chance test in `work/decode.py` (window 15 on the card, 0/2000 random reorderings), and wrote `work/salutation_test.py`, a like-for-like test of the 9 signs after DEAR (DEAR fixed, rest shuffled, 20000 trials): E-S-T in order 1.0 %, N-A-N adjacent 0.04 %. So the reviewer's comparison (0/2000 against 30/2000) overstated the case for DEAREST: matched by window and condition, NAN as an adjacent group is the rarer event. Neither is chance on its own; I keep DEAR NAN for the layout (the writer's own `NAN` group) and the address (Miss A. Stainforth), and mark DEAREST as a real alternative. The sentence "no further word I could establish" was removed. The body of the message is unchanged.
2. **(minor) Line 3 leading I.** Fixed: the Transcription section now says the GPT `I` at the start of lines 1, 2 and 3 was dropped, line 3's being the end of the printed underline below "Carte Postale" (reviewer's crop review/work/l3start.png, which I checked). NOTES.md updated.
3. **(minor) Signature Jick/Jack.** Fixed: Uncertainty 5 now records that the portal capture and the GPT notes say "Jack", and why it is rejected (separate dot, no closed bowl on the 5x crop), with "Jack" and "Dick" left as residual possibilities.
4. **(minor) LET. and the tail.** Fixed: Uncertainty 2 now says plainly that the words after FROM YOUR are not established, with the 22-letter count corrected (the DONE1 text said 25) and the YOURS TRULY / LOVINGLY checks recorded.
5. **(minor) Cosmetics.** The comment in decode.py now says 144 signs. The table header now says "Letters in sequence, card spacing removed", and the card's own spacing is shown separately above the plaintext. I also noted the two null signs the reviewer flagged as ambiguous (line 1 sign 5 L/E, line 4 sign 17 J/S).

Re-run after the fixes (`python3 -I ciphers/hcp-1489/work/decode.py`): source hashes OK, 144 signs, 51 plaintext letters, 93 nulls, plaintext `DEAR NAN WITH LOVE AND BEST WISHES FOR YOUR BIRTHDAY FROM YOUR + signature Jick`; earlier chance-test figures unchanged (DEAR 20/2000, long phrase 0/2000, FROM YOUR 0/2000, NAN 30/2000), plus DEAREST 0/2000.

Not addressed (reviewer could not settle them either): the postmark year digit, and the corner triangle marks and circled 6, which I also take to be collector annotations outside the cipher.
