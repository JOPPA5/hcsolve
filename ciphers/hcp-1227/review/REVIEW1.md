REVISE

# Review 1 of HCP1227 (Feri to Jolánka Tóth): reviewer Claude Opus 5.5, 2026-11-02

Verdict: **REVISE**. Cipher type, key and the reading as a whole stand: this is the Jolánka key and connected Hungarian. Three concrete ledger errors must be fixed. One of them (row 3) means two signs in the ledger are not on the card and changes a word of the plaintext and its translations. The closing under the stamp is also segmented wrongly: the visible signs point to the family formula "a boldog viszontlátásig", not to a word ending "-ból".

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1227/work/decode.py`: all four hash checks print OK; the literal rows match the SOLUTION.md block and the normalized text matches the Hungarian section. It prints 519 tokens, 7 lost.
2. **Independent decoder.** `python3 -I ciphers/hcp-1227/review/work/decode_review.py` holds my own sign-class transcription of rows 1 to 24 and takes values only from the sister file `ciphers/hcp-1301/work/graphic-key.json`, then diffs against the solver's ledger with h/p folded. Result: 24 rows, 477 letters against 479, identical except rows 3, 8 and 9 (findings 1 to 3). Every sign has a key value except the digits 2, 8 and the one stray stroke in row 22. The transcription is not blind, since I had read the ledger first; each difference was confirmed on a separate enlargement.
3. **Transcription against the scan.** My crops of work/hires/*_adr.jpg are in review/work/: all main rows at 2x (`a1`–`a13.png`), rows 3, 8, 9, 15, 22 at 3–5x (`r3`, `r8`, `r8b`, `r9b`, `r15b`, `r22start`, `r22end`), stamp block (`st.png`; red channel `st_r.png`; green-minus-red `st_gr.png`; `s3l*.png`, `s3t.png`, `s4t.png`). Results for the disclosed hard spots:
   - row 7: the digits 2 and 8 and the accent over a are clear; the blotted k + e is as described. `28-án` stands.
   - row 10 and row 18: six strokes before `eg` in each, as stated.
   - row 15: two touching F signs, `arra` stands. Row 19: the blotted first sign is as described; j is contextual and disclosed.
   - row 22: five strokes between b-e and e (the third and fourth nearly touch), as stated.
   - rows 22 to 24 layout: confirmed, and sharper than the solver says. After `vonaton` come gamma + two bars at the higher level (`ta`), then `l k o z n i cs a k i s` runs on; the two bars just below them are the a of `abba`, then 6 6 two-bars, then `l e s z e k`. Read as one apparent three-to-four-bar stack at normal zoom, so this confirms there is no missing or extra sign there.
   - stamp: `isten / vele ede / …a b o l / …g v i / s…t / latasig / feri`: every sign the solver claims as visible is there. The dot under `o` in S3 is the dot of the i in S4, as the reading implies. z, o, n of S5 are not separable from the printed triangle (see finding 5).
4. **Key coverage and family.** The key is unchanged; literal numerals in the schedule are a precedent on HCP1301 (its SOLUTION.md, rows 7–8: 5 and 7), as claimed. Repetition counts in the solver's list (hogy ×6, nem ×4, etc.) are correct.
5. **Language and context.** Natural period Hungarian with the family's formal address, spelling habits (`mer`, `abba`, `gyöne`) and closing formula. Rákospalota-Újpest fits; the Nyugati side of the line is geographically sensible, and the train meeting fits Jászárokszállás. Feri is the sender on sister cards (HCP1211, 1213, 1216) and the Rákospalota link is consistent with HCP1216.
6. **Sources.** Portal status Not solved, no attachment. No published solution is used and the key origin is credited.
7. **Plain text.** Address reads Szép reményű / Tóth Jolánka / úrleánynak / Jász Árokszállás; the first word's Sz and ép are visible despite the box. Picture captions as stated.

## Findings

1. **Row 3: two phantom signs; `elfogadok` is not on the card (major).** The ledger has `m m e l e l f o g a d o k`. The scan (`review/work/r3.png`, and `a1.png` + `a2.png`) shows two groups of three strokes, then one three-bar sign, one wave, the cross: `m m e l f o g a d o k`. Literal row: `nagyörömmelfogadok`. So *nagy örömmel fogadok*, "which I receive with great joy", not *elfogadok* "accept". Fix the ledger, literal block, normalized text, English ("receive"/"welcome") and Slovak ("prijímam" can stay only as receive, not as accept). The token count falls by 2 and the "no key letter had to be changed" claim is unaffected.
2. **Row 8: sign before `m` is two bars, not three (major).** `review/work/r8.png`, `r8b.png`: after the gamma of `het` stands a clear two-bar a with a hooked top bar, unlike the three-bar e's earlier in the same row. Literal is `hatehetamszombaton`, not `hetem`. Item 6 then under-reports the distance from *héten*: both the a and the m differ from it. Correct the ledger and restate item 6. *e héten* remains the sense, but it is now an emendation of two signs; *e hét ám szombaton* (with the particle ám) is an alternative needing no sign change, though less idiomatic. The solver should weigh and disclose both. The meaning "this week on Saturday" holds either way.
3. **Row 9: `vale` should be `vala` (minor).** `review/work/r9b.png`: two bars (the lower one with a split pen stroke), not three. Literal `valahol`; the ledger's e is also an undisclosed normalization as it stands, and the fix removes that.
4. **Stamp closing: segmentation "…ból / …g" and the bare "[...]" are the wrong analysis (major).** S3 ends `a b o l`, S4 ends `g`, S5–S6 give *viszontlátásig*. That is the family formula: Isten vele, édesem, a boldog viszontlátásra (HCP1205; also "a boldog viszontlátásra" on HCP1213). Division `[…] a bol | [do]g vi | szont | látásig` gives *Isten vele, éde[sem], a bol[do]g viszontlátásig*, "God be with you, my sweet, until the happy reunion". This fits every visible sign and needs only about 3 lost signs in S3 (s, e, m) and 2 in S4 (d, o), within the solver's estimates of about 4 and 3. The solver's item 1 ("…ból", "cannot establish whether S3 belongs to the same phrase as S4") and its English and Slovak "[...]" should be replaced by this as a clearly labelled restoration from the family formula, not a reading: I could not confirm s, e, m, d, o on the pixels. Traces remain left of the a in S3 (`s3t.png`), but they do not decide any sign. With this, the card has no unread clause: the lost signs lie within words of a known formula, and the sense is complete.
5. **S5 restoration (minor, disclosure already adequate).** The stated status of `[zon]` is right: s and t are clear, and I could not separate z, o, n from the triangle's printed letters. Keep it labelled as restored.
6. **Status and Why sections (minor).** "No key letter had to be changed" is fine, but after the fixes also say that *héten* is emended. The status line should drop "disclosed physical gap" framing once finding 4 is applied, and should say restored signs in place of "gap".
7. **Dating note, item 15 (minor).** On my crop `cancel.png` only the day 26 is readable; no month stands clear. So the month comes from the portal file name alone, not from the cancel: state that.
8. **Picture edge line, item 14 (minor).** Rotated (`review/work/gold_rot.png`), the worn line is in the same gold italic style as the printed captions, and has no cipher signs. "Probably a worn printed caption" is the better statement; I too cannot read it.
9. **Translation of `találkozásom` (minor).** Literal is "my first meeting", not "our"; acceptable as free rendering, but the solver may want to note it. *mér* = *mért* and *túl vasutas ruha* remain interpretive, and those are disclosed.

## What I could not verify

- Signs s, e, m (S3), d, o (S4), z, o, n (S5): not recoverable on these scans.
- Whether `túl vasutas ruha` means a railway uniform; the text supports it but does not prove it.
- The year and month of the cancel, and hence whether the 28th could be tested against a calendar.

## Registry note for the solver

After findings 1 to 4 are fixed, the card meets the completeness rule (no unread clause). A new DONE round is not strictly required by these changes if they are made exactly as above, since they alter only one word plus emendation notes and the labelling of the closing formula; that decision is the solver's under README step 5.
