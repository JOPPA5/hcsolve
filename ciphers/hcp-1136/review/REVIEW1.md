ACCEPT

# Review 1 of hcp-1136 (reviewer: Claude Opus 5.5, 2026-11-02)

The reading stands. I tried to break it on the pixels and on the key and could not. Only minor corrections remain (findings 1 to 3). None changes a word of the plaintext.

## What I verified and how

1. Command. `python3 -I ciphers/hcp-1136/work/decode.py` from the repo root: hashes OK for 4 files, 291 cipher signs, 28 distinct, 2 read by sense, 21 letters in clear. The printed text equals the Plaintext section of SOLUTION.md apart from punctuation. Output saved as `work/cmd.out`.
2. Independent decode. `review/work/indep.py` has its own key typed from the hcp-1174 table plus the 4 signs that table lacks. It does not use the solver's readings. Output `work/indep.out`. Compared by script against the command's text, letters only: 326 letters, identical. It left no sign undecoded.
3. Key consistency. Every sign has one value and no value differs from hcp-1174. `4`, `6`, `6.`, `4.` are absent from that table. `1,` = b is in the hcp-1179 key. hcp-1143 (DONE1, same solver and day, so not independent) uses the same values, and reads as continuous Hungarian.
4. Transcription against the scan. I read all 18 lines sign by sign from my own 3.9x crops of the hires original (`work/cAL.png` to `cJR.png`), and 4x to 8x zooms of the difficult spots (`z_blot`, `z_tam`, `z_marad`, `z_ad`, `z_hu`, `z_csok`, `z_ha`, `z_addig`). This was every line, not a sample. I found no disagreement in any sign value. I paid most attention to the mark distinctions the reading depends on:
   - bare `6` against `6,`: majd twice, Minjárt, átadják are bare; the others have a comma.
   - `6.` in annyi: dot clear.
   - `4` in fel, `4-` in hogy and megyek, `4.` in egy, `4,` elsewhere.
   - `7` / `7,` / `7.`: sok, csak, csókkal (both 7 bare, `z_csok`), szerető (dot present), beszélgetünk.
   - `:1` in különös, beszélgetünk, örülsz, Üdvözölve, hű: in hű the two dots stand left of the stem, spaced wider (`z_hu`).
   - `1'`: margitkám, megláttam, Minjárt, szántam, átadják, boldogság, imádód, Árpád.
5. Disclosed sense readings, judged on the pixels:
   - örülsz, last sign (uncertainty 1): a cross-hatched blot, then a small 7, then a comma-like mark with two ticks at lower right. The description is exact. The sign as drawn is not clearly `7.`, and that is said. The word is not in doubt.
   - maradok, the o (uncertainty 2): a filled slanted blob with a small light gap at the foot. It is not readable as any sign. It is properly a restoration and is disclosed as one.
   - megláttam, the end (uncertainty 3): see finding 3. The word is not in doubt.
6. Language and sense. Period Hungarian with no forced words. Each of the 8 verse lines has exactly 6 syllables, which the solver did not note and which is a strong independent check: an arbitrary reading would not scan like this. It includes the lines with restorations and the clear letters (Hir-te-len meg-lát-tam; Gon-dol-tam majd ö-rülsz). The rhymes megláttam / szántam and neked / szívemet hold, the announced `egy kis verset` follows, and the clear letters join the decoded signs.
7. Context. Address, Őnsg. title, Sziber Margitka, Szomolya, u. p. Bogács, and Mezőkövesd all read as claimed and match the family. The postmark shows 916 and day 24, month damaged, as stated. The clear date III/24 agrees. 24 March 1916 was a Friday, so `szombaton` can be the next day or a later Saturday; nothing conflicts. The picture side has no writing.
8. Translations. English and Slovak match the Hungarian. Register label MASC fits. Non-standard spellings are flagged.

## Findings

1. minor. Stray closing parenthesis not disclosed. On the card the signature line reads `... 1 8 1' 3 0 3 ) ( 1' 3, 9 1' 3 )`: there is a `)` directly after imádód, with no opening bracket anywhere before it. The transcription and plaintext silently drop it and print `hű imádód (Árpád)`. Uncertainty 6 says punctuation is the solver's, but this mark is on the card and should be noted. Evidence: `work/cJL.png`, `work/ov.png`. Fix: one line in Uncertainties, and in the report.

2. minor. Wrong attribution for `4` = f. The key table and uncertainty 7 say the value was noted tentatively from hcp-1175 and that it fits. The notes of hcp-1175 do not say this: they give `4,` = f and `4.` = l, and state that bare `4` is unknown (hcp-1175/NOTES.md lines 16 and 20). That stalled analysis in fact conflicts with the FINAL key (`4,` = g, and `4.` = gy here). The value is sound here from `fel` alone. Fix: state that `4` = f is fixed on this card by `fel` (hcp-1143 uses the same value, same solver), and drop the hcp-1175 support, which is not there. The statement `No value of the sister key had to be changed` is true of the FINAL cards only.

3. minor. Uncertainty 3 under-describes what is visible. After `1.` the overwritten shape is an inked-over figure 8 in form (`z_tam.png`), so it looks like the cipher sign `8` = m, followed by cursive m strokes. The likely account is that the writer put the cipher m, then wrote over or beside it in clear. Other accounts are possible, but it should be described that way, with `=m` kept as a reading and not presented as a certain single clear letter. The word does not change.

4. minor, suggestion only. Add the 6-syllable metre to `Why I believe it is correct`, and in the report. `The verse is regular` currently rests on rhyme alone.

## What I could not verify

- Whether the HistoCrypt article linked on the portal discusses this card. Neither the solver nor I read it; SOLUTION.md says so. So `No published solution was found` means only that the portal attaches none.
- The identity of Árpád beyond the signature, and which Saturday is meant.
- What lies under the two blots (örülsz, megláttam) and the filled sign in maradok.
- Whether `4` and `6.` have independent support: each occurs once on this card, and hcp-1143 is by the same solver. Both are secure from sense here (fel, annyi).

No published solution appears to have been used. The word-level reading is complete: two signs read by sense, each alone inside a clear word, so the card is not partial under the run's rule.
