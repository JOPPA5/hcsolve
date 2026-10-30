REJECT

# Review 1 – HCP 1534 (pc_hcp_215), Pepouš to Anna Tichá, 20 Oct 1903

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Round 1, against DONE1.

## Summary

The key is the known Anna Tichá family key and it is applied correctly. Most of the
card is transcribed faithfully. However, **four words in the transcription do not match
the pixels**. All four are replaced by a different but plausible Czech word. Three of
them also give a much better reading than the solver's. The pattern shows that parts of
the last third of the card were filled in from context instead of being read sign by
sign. The decoder's round-trip and hash checks cannot catch this, because they only
check the manual record against itself.

The overall reading (a love letter from Pepouš about a Cecilian society meeting and
office work) stands. Still, the literal plaintext, the counts and the translations are
wrong in four places. The solution also claims that the full text was transcribed and
that the card is complete. I return REJECT so that the solver checks the whole card
again sign by sign and a second review round confirms it. A plain REVISE would let the
corrections go to FINAL without another check.

## What I verified and how

1. **Solver command.** `python3 ciphers/hcp-1534/work/decode.py` runs (exit 0). It prints
   the 24 rows exactly as given in SOLUTION.md and reports "564 indexed marks; 563
   assigned units; 1 unresolved overink; 3 CH units; 566 assigned base letters; token
   round-trip OK". Output saved as `review/work/theirs.txt`.
2. **Independent decoder.** `review/work/mydecode.py` builds the key from scratch. It
   asserts that every entry agrees with the finished family key
   `ciphers/hcp-1545/work/key.json` (with ř = H = CH). It then decodes
   `work/transcription.json`. The result (`review/work/mine.txt`) is identical to the
   solver's output for all 24 rows. The run covers 564 units, every key label is used and
   no unknown labels remain. **The key is consistent and covers the whole transcription.**
3. **Transcription against the scan.** I rotated `source/picture.jpg` 90° counterclockwise
   (PIL ROTATE_90, 674×1024, same frame as the solver's boxes) →
   `review/work/upright.png`. I cropped all 24 rows at 4–6× (`R_*.png`, `H_*.png`) and
   enlarged 30 or so individual words at 7–16× (`Z_*.png`). For the U02 overink I also
   binarised the pixels (`bin.py`). I read every row against the transcription. The
   glyph forms used for checking come from clear same-card examples. Teardrop "ı/ɑ" is
   s=C (CISTOU, SRDECKO). Looped-ascender h is R (VRELY). b-shape is P (PRACE). p-shape
   is B (BLAZI). "9" is q=Z (KDYZ, ZA). "y" is 4=I. Tall "б" is 6=A. "n" with a lead-in is
   n=M (MNE).
4. **Corrected decode.** `review/work/reviewer_corrections.py` applies only the four
   corrections below to a copy of the record (`transcription_reviewer.json`) and decodes
   it (`mine_corrected.txt`). The result has 565 indexed marks, one more than the solver's
   564, because UPRIMNYCH has one more unit than ULIBNYCH.
5. **Evidence sheet:** `review/work/review1-evidence.png` (enlarged crops of each finding).

## Findings

### 1. L04 `q6p6f2` ZABAVU is wrong; the scan shows `qbh6f2` = ZPRAVU — **blocker**
At 12× (`Z_l04a.png`) the word is clearly "9 b h б f 2". The 2nd sign is b-shaped (P), not
the descender-p B, and it is not a 6. The 3rd sign is the looped h (R). The text reads
"…který se na slíbenou delší **zprávu** nesmírně těší" ("…who looks forward very much to
the promised longer message"). That fits a postcard writer much better than "zábavu".
The editorial Czech and both Slovak translations must change.

### 2. L02 `284pm1H` ULIBNYCH is wrong; the scan shows `2bh4nm1H` = UPRIMNYCH — **blocker**
At 7× (`Z_l02.png`) the word is "2 b h y n m 1 ř": **eight** cipher units, not seven.
There is no 8 (L) and no p (B). The n-then-m pair is the same as in the clean MNE in U02.
The reading is "tisíc dlouhých, **upřímných** pus". The solver's "úlibných" (a rare word)
was produced from context. This changes the unit count: 564 → 565 indexed marks.

### 3. S13 `t3c6rm2` DOSAHNU is wrong; the scan shows `t3s484n` = DOCILIM — **blocker**
At 10–12× (`Z_s13.png`, `Z_s13b.png`, binarised) the second word is "t 3 ɑ y 8 y n.". The
third sign is the teardrop s (C), as in CISTOU and VCEREJSI, not the round c (S). The
5th sign is a clear 8 (L), not r (H). The 4th and 6th signs are 4 (I). The last sign is
n (M). This gives "sotva toho **docílím**", a good Czech synonym of the solver's guess.
Five of seven labels in this word were wrong. The unit count does not change.
NOTES.md says that S12/S13 crops were "generated" and "verified". This word was
evidently not compared with them.

### 4. L03 `f5hm5` VERNE is wrong; the scan shows `f5sm5` = VECNE — **major**
At 12× (`Z_l03a.png`) the third sign is the short teardrop s (C). It has no tall looped
ascender, so it is not h (R). The reading is "**věčně** jeho Pepouš". This is exactly the
closing formula and exactly the misreading that review 1 of the sister card hcp-1525
corrected (R11 `f5hm5`→`f5sm5`). The solver had that precedent available.

### 5. The completion section claims "complete reading" while the header still says PARTIAL; counts are inconsistent — **major**
The opening says "PARTIAL solver candidate". The "Completion and handover" section says
"complete reading". The decoder still prints `[?]MNE` and counts the overink as
unresolved. The handover also adds a second, different Slovak translation ("Láska tvoja
ma, miláčik…", "sladkých bozkov") without removing the first. After findings 1–4, both
translations are wrong in any case. The solver should keep one status, one literal
text, one editorial text and one translation. The decoder output and the counts
(565 marks after finding 2) must agree with that status.

### 6. U02 overink before MNE: the completion reading is acceptable but should be described precisely — **minor**
My binarised view (`bin.py` on 380,84–425,112) shows a heavy blob. It has an n-like arc
on its right and a **descender stroke** reaching about 7 px below the baseline. After it
come a clear m (N) and 5 (E). The clean `nm5` in the same row has the same three
positions. So I agree that the word is MNE with three units and that "láska tvoje mne …
blaží" needs nothing more. However, n has no descender. The descender suggests that the
writer first began another sign with a descender, for example p=B as an early start of
"blaží", and overwrote it with n. The claim "re-inking, not a separate sign" should be
stated as a probable correction of a different sign, with this uncertainty. The decoder
should either print MNE and count the n, or keep `[?]`. It should not do both at once
in the way it does now.

### 7. S01 VASKERI first vowel may be 5/E — **minor**
At 16× (`Z_vas.png`) the 2nd and 5th signs of `f?cg5h4` look much alike. Both have a short
flag at the top and no tall б-ascender like the clear 6 in ZA or DRAHY. I cannot rule
out VESKERI (veškeří). The solver should compare this sign again with the clear 5 and 6
forms and either keep the anomaly with this caveat or read 5. MILAVANE (L01, `Z_mil.png`)
looks like a real б (6) in the 4th position, so I accept it as a writer anomaly.

### 8. Overinked signs not all disclosed — **minor**
The first sign of L03 `c84p5m32` (SLIBENOU) is a heavy blot, probably a correction to c.
In U04 `b274s4n` the 7 is written over another stroke. In S10 AVSAK the overinked third
sign has an f-like descender loop under the c bowl, which suggests that f was corrected to c.
The readings are plausible, but SOLUTION.md should list them as corrections, like the
U02 and S10 cases.

## Readings I confirmed (spot checks at 6–16×)

U01–U07 match the transcription sign for sign, including JENZ (`75mq`, final "9" =
q as in KDYZ), SCHUZI (`cH2q4`, ř-glyph), CECILSKOU, OBKLOPUJICIM and CISTOU. In the right
margin S01–S12 match: SJEDOU, UDOVE VE SVETE, SIREM ROZTROU-, SENI. DOUFAL (shallow-v F;
same shape as the family F), JSEM ZE DO TE, DOBY BUDU, ASPON S KON-, CERTEM SVE, PRACE
HOTOV, AVSAK PRO NA-, VAL PRACE KAN-, CELARSKE SOTVA, and TOHO in S13. In L01–L04 the rest
matches: SVE TAK VASNIVE MILAVANE SRDECKO VRELE K SOBE / TISKNE A TISIC DLOUHYCH, … PUS MU
POSILA / … JEHO PEPOUS, KTERY SE NA SLIBENOU DELSI / … NESMIRNE TESI.

Corrected literal tail (reviewer's reading, for the solver to verify):

```
CELARSKE SOTVA
TOHO DOCILIM.
SVE TAK VASNIVE MILAVANE SRDECKO VRELE K SOBE
TISKNE A TISIC DLOUHYCH, UPRIMNYCH PUS MU POSILA,
VECNE JEHO PEPOUS, KTERY SE NA SLIBENOU DELSI
ZPRAVU NESMIRNE TESI.
```

## Context and honesty

- Language is natural Czech of c. 1903 (srdéčko, holubička, schůze cecilská, údové).
  The date 20. X. 1903 and the addressee Anna Tichá (Žirovnice) fit the family.
  The Cecilian society (Jednota cecilská / church-music movement) is a plausible
  context for "výroční schůze cecilská", but nothing on the card confirms it.
- Key provenance (HCP1520–27 transfer; Maxim Egorov's published partial generic key) and
  the later F comparison with card 199 are disclosed. I found no undisclosed use of a
  published target solution.

## What I could not verify

- The writer's intent under the overinks (U02, S10, U04, L03). They are judged as corrections from
  the pixels only.
- 5 vs 6 in VASKERI (finding 7) cannot be decided with certainty at this scan resolution.
- Diacritics/punctuation were not checked exhaustively. They are not cipher units.
- Historical identity of Pepouš and the precise "koncert své práce" remain unestablished,
  as the solver states.
