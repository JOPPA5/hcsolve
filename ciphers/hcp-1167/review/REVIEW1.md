REVISE

# Review 1 of hcp-1167

Reviewer: Claude Opus 5.5, 2026-11-02. The message, key and signature stand. One sign is mistranscribed and changes a word; the fix is one token plus the matching text.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1167/work/decode.py`: hashes OK, 345 signs, 341 by table, 4 by sense. Its output matches the claimed plaintext line by line.
- Independent decode: `review/work/indep.py`, with the key retyped from the hcp-1174 and hcp-1165 tables and `5.` = l. Same letters, apart from `melben` (uncertainty 5). The key is complete: no sign in the transcription falls outside it.
- Pixels: I read all 18 cipher lines from my own crops of `work/hires/..._adr.jpg` (`review/work/b0a` to `b5b`, 1.5x of the original, about 3.7x of the overview), blind to the solver's crops, and compared them sign by sign with `work/transcription.txt`. Enlargements of every doubtful sign are in `review/work/z_*.png` and `y_*.png`. Because NOTES.md warned of log entries written before crops displayed, I checked lines 7 to 14 and the four by-sense signs with particular care.
- The four by-sense signs are all confirmed as disclosed: line 7 first `5` has no comma (`b1b.png`, `y_l7e.png`); line 9 `4` has no dot (`b2a.png`, `z_hogy.png`); line 9 final `8` has no comma (`z_l9e.png`); line 12 `3` has no dot, and the only dot there belongs to the following `1.` (`z_szov.png`). Each is a true mark omission, and `lehet`, `hogy`, `lehet`, `szóval` are the only sensible words.
- Language and context: connected, ordinary Hungarian, no forced words. Names (Margitka, Mariska, ángyika, Árpád), the Mezőkövesd to Szomolya route and the closing fit hcp-1174, 1178 and 1165. Date 1916. III/11. is legible (`y_date2.png`) and matches the file name. Address reading confirmed. The picture side has no writing (`y_pic.png`).
- Sources: the portal attaches no solution and none is used. The solver states that the linked article was not checked.

## Findings

1. **major: `1 4. 1 7,` on line 12 should be `.1 4. 1 7,`, so the word is `úgyis`, not `így is`.** `z_iy.png` shows a firm, deliberate dot directly left of the 1, the same form as `.1` in `tudja` (line 7) and `hűséges` (line 17), and separated from everything else. It is not a speck, and no other sign claims it. Per the key this gives `u`: `már úgy is / úgyis régen nem beszélgettünk`, "we have not talked for a long time anyway". This fits the sense better than `így is` ("even so"), and the existing translations ("as it is", "aj tak") already render úgyis rather than így is. hcp-1152 (FINAL status not checked by me; its SOLUTION reads this form) has `úgyis` with the same `.1`. Fix `work/transcription.txt`, the plaintext and the uncertainty text. This is one word and the reading stands, but as written the card's sign and the published word disagree.
2. **minor: uncertainty 6 is wrong as a result.** `.1` occurs three times, not twice (`tudja`, `úgyis`, `hűséges`). The counts of 345 and 341 do not change.
3. **minor: `megyek` last vowel not disclosed.** In `z_megy.png` the lower dot of `1:` is clean, but the upper dot touches the start of the following 7. `1:` is right (the alternative `1.` gives `megyak`), but this is a call the reader should be told about.
4. **minor: uncertainty 7 misdescribes the card.** It says `fel megyek` is "written with no gap of its own", but there is a clear gap after `5,` on line 10 (`b2b.png`), and the transcription itself places a `|` there. The conclusion that it is one word, `felmegyek`, is grammar and not a fact about the writing. The gaps also seem more regular than "no reliable word gaps" suggests. Reword.
5. **minor: fused commas not mentioned.** The `6,` in `számtalanszor` (line 16, `y_l16.png`) and the `6,` of `nem` on line 13 have the comma fused into the tail of the 6 rather than written separately. This is the writer's habit and I accept `6,`, since the plain 6 has no tail (`majd`, `tudja`). A one-line note would explain it, since this is a mark call of the same type as the four disclosed ones.
6. **minor: `[a?]` is correctly disclosed, not confirmed.** `y_word.png` shows a short, malformed word with the green number under it, and a blotted `kis`. I cannot see a clean `a` either. `és a kis Mariskát is` remains by parallel with hcp-1178. It is one word alone, so the card is complete under the run's rule.
7. **minor: hcp-1165 is cited as support but is not finished.** It has REVISE at review 1 and no FINAL. The agreement is real, but say that this card is still open, or lean on hcp-1174 and 1178.

Accepted without a finding: `5.` = ly or l (uncertainty 5: the dot is visible on line 3, same word either way); `imádód`; no `a` for `Mariskáit`, the mark is the accent of á; the first sign of line 12 is `7.`, heavily inked, with the dot clearly below it (`z_szov.png`).

## Could not verify

- The postmark: the date strip on the stamp is too broken to read (`y_pm.png`); only a fragment such as `13` or `16` is visible. The date rests on the writer's own line.
- Whether the HistoCrypt article discusses this card (not checked by me or by the solver).
- The exact kin relation of `ángyika`, and the identity of Róza.
