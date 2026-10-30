# HCP 1460 (pc_hcp_141) — solution

Postcard (picture side: Westminster Abbey, Coronation Chairs), postmarked
South Tottenham 8 PM, 7 Mar 1905, to Miss Ovington, 23 Gloucester Rd,
Sth Tottenham. English. No transcription or solution is attached on the
portal (status Not solved); no published solution was found or used.

## Cipher type and key
Per-line **transposition** (portal category "Transposition" is right). Each
written line is read: first letter, last letter, second letter,
second-to-last letter, ... and so on to the middle. The route restarts on
every line. Equivalently, to encrypt a line the writer put plaintext letters
1,3,5,... left to right, then letters ..., 6, 4, 2 (even-numbered letters in
reverse). No substitution; no keyword. Word spacing is removed.

## Transcription (work/transcription.txt, read from source/address-large.jpg)
```
DaSdeiare
Ftewseihtgldarha
ewtteocrtenChhid
lsngtnhsadahita
akdegveouyitmes
hsogauainsotltrnci
```
89 letters, all read from the pixels (enlarged crops 4-12x). The small `s`
written under the last line between `n` and `o` is the writer's own
insertion mark and is included at that point.

## Plaintext (strict route output)
```
DearSadie
Fatherwasdelight
edwiththeConcert
lastnightandhas
askedmetgivyeuo
hiscongratulations
```
Reading: **"Dear Sadie, Father was delighted with the Concert last night and
has asked me t[o] give you his congratulations. Ys H.A.r"**

- English (original language): as above.
- Slovak: „Milá Sadie, otec bol nadšený včerajším koncertom a požiadal ma,
  aby som Ti odovzdal(a) jeho blahoželanie. Tvoj(a) H. A. r."

Closing `Ys H.Ar` (= "Yours", initials) is plain text, reported literally; the
writer is not identified.

## Command (run from the repo root)
```
python3 -I ciphers/hcp-1460/work/decode_full.py
```
It checks the SHA-256 of the files in source/, decodes every line of
work/transcription.txt, checks the inverse (encryption) roundtrip, checks
that the "asked me" line is an exact anagram of `askedmetgiveyou`, and prints
the editorial reading.

## Uncertainties (all disclosed)
1. **Scribal slip in line 5 (`akdegveouyitmes`).** The strict route gives
   `askedmetgivyeuo`. The 15 written letters are exactly the letters of
   "asked me t give you" (one `o`; the `o` of "to" was never written).
   Correct encryption of `askedmetgiveyou` would be `akdegv yuoe itmes`; the
   card has `akdegv eouy itmes`, i.e. the four middle letters, written as one
   joined cluster `eouy`, are in reverse order. No letter is added or
   changed; only this order slip is interpreted, and "t[o]" is an editorial
   bracket. The writer evidently filled in the joined middle clusters last
   (all lines show this). This uncorrected order reversal is a different
   kind of error from line 6, where the writer omitted a letter and
   corrected it himself with the inserted `s`.
2. Line 6, second sign of the joined cluster: on the scan it is ambiguous
   between cursive `u` and `n` (entry upstroke, pointed tops); earlier work
   read it `n`. It is read `u` because the route requires it
   (`congrat-u-lations`), not because the pixels decide it.
3. Line 4 first sign read as cursive `l`; line 2 first sign as cursive `F`
   (resembles `I`). Line 5 second sign read as `k`: on the scan it is an
   `h`-like form with a small knot in the arch, similar to the `h`s of
   line 3, so `k` is plausible but largely route-driven (`as-k-ed`).
   Line 3 begins `ewtt`: a plain `t` followed by a separate hooked/looped
   sign, which is given the value `t` from the route and context
   (`wi-t-h t-he`); it is not a crossed double `t`.
4. Closing initials `H.A.r` uncertain in form; not part of the cipher.
5. The picture side carries no cipher text.

## Why it is correct
Every one of the 89 letters is used exactly once under one simple, uniform
route that restarts per line; five of six lines decode with no deviation into
fluent period English, and the sixth is an exact anagram of the obvious
phrase with a disclosed four-letter order slip. The content (a concert, a
father's congratulations) fits a 1905 local postcard to a young woman.

## Credit
The route key and the first four lines (greeting + three body lines) were
established by the earlier OpenAI GPT solver (2026-10-26), who left the last
two lines unresolved. Claude Opus 5.5 (2026-10-29) re-read all lines from the
scan, read line 6 (`u` and the inserted `s`), decoded the last two lines and
documented the line-5 slip.

## Response to review 1

Verdict ACCEPT with four minor findings; all accepted, wording fixed in
the Uncertainties section above. The transcription, key and plaintext are
unchanged; `python3 -I ciphers/hcp-1460/work/decode_full.py` re-run after
the edits, output unchanged.

1. **Line 6 `u`/`n` (minor) — fixed.** Re-examined `review/work/l6_u2.png`
   (enlarged): the sign has an entry upstroke and pointed tops and is
   indeed ambiguous; the claim "cups at the bottom" overstated it.
   Uncertainty 2 now says "ambiguous u/n; read u as the route requires".
2. **Line 5 `k` (minor) — fixed.** Uncertainty 3 now describes the sign as
   an `h`-like form with a knot and states the `k` reading is largely
   route-driven.
3. **Line 3 `tt` (minor) — fixed.** Re-examined `review/work/l3_tt.png`:
   a plain `t` then a separate hooked sign before `e`. Description
   corrected; the hooked sign's value `t` is marked context-supported.
   Transcription `ewtte...` (16 letters) is unaffected.
4. **Analogy (minor) — fixed.** Uncertainty 1 no longer calls line 6 "a
   similar slip"; it distinguishes the uncorrected order reversal (line 5)
   from the self-corrected omission (line 6).
