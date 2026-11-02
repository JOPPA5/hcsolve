# HCP1313: Jolánka-family postcard of 7 April 1912. PARTIAL decipherment, not complete

**Status: partial, improved by the revision of 2026-11-02 (see the last section): rows 10-12 are now read; rows 6 end to 7 and the end of row 8 to row 9 remain unread. No marker created, no register entry.** Claude Opus 5.5, 2026-10-30 and 2026-11-02. No earlier work exists on this number; no published solution was seen. Portal: Not solved, no attachment.

## Cipher and key
Hungarian, simple monoalphabetic substitution with invented graphic signs: the shared Jolánka key of hcp-1216 (see its SOLUTION.md for the sign table; also hcp-1301). On this card the key decodes fluent Hungarian in rows 1-6 and 13-17, so the family attribution is firm. Extra points seen here: left bowl + right bowl written separately for cs (*becses*, row 5), closed small circle for cs (row 2), ly as a joined wave + descender (row 3, reading from sense).

## What is read (normalized; signs read on enhanced crops from work/hires, see NOTES.md)
Secure:

> Kedves Jolánkám! Becses levelezőlapját megkaptam, melyért fogadja őszinte köszönetemet. Becses sorait nagyon szépen [...]

> [...] Édesem, én már húsvétkor megmondtam, rossz idő lesz. Isten vele, a viszontlátásra.

English: "Dear Jolánka! I received your esteemed postcard, for which please accept my sincere thanks. Your esteemed lines very nicely [...] [...] My sweet, I told you already at Easter that the weather would be bad. God be with you, goodbye."

Slovak: „Milá Jolánka! Dostal som Váš vážený lístok, za ktorý prijmite moju úprimnú vďaku. Vaše vážené riadky veľmi pekne [...] [...] Moja sladká, ja som už na Veľkú noc povedal, že bude zlé počasie. S Bohom, dovidenia."

## What is NOT read (rows 6 end to 12)
Literal working strings only. These are not a plaintext; `?` marks a doubtful sign, `[ ]` an unresolved one.

- r6 end: `h? a? gy?` after *szépen*; the *-en* of *szépen* lies in a blot, and *sorait* has only faint traces of `it`.
- r7: `z e s z e k r e? s z [ ] e [ ] ... e i s u [blot]`, no parse. *én is úgy* is only a guess for the tail.
- r8: `e r e z n e k m i n t [ ] e d? o`: *éreznék mint* is tentative, the tail is not read.
- r9: `e s o r o [k?] [ ] g z a n [ ] a k o`
- r10: `e d/n v o l ... e k a l ...`, then signs under the wash
- r11: `h o g a 6 6 e m b e r [ ] / ...`: the doubled 6 is unexplained (bb, or the digits 66)
- r12: `l a g e b a r e i k o z o /`

## Reproduction
There is no one-command decoder, because the reading is incomplete. Crops: `work/enh.py`, `work/enh2.py`, `work/rows.py`, `work/seg.py`, `work/z.py` (run with the codex runtime python, -I).

## Other uncertainties
- Row 13 *hús*: the u lies in wash. *húsvétkor* is supported by the date (7 April 1912 was Easter Sunday), which is context, not a pixel reading.
- Row 15 *lesz*: the z is an upright cross, read from sense (f-class shape). Row 15 spells *rosz* (one sz written).
- Row 16 *viszont*: the o was not clearly seen.
- The red plain text on the address side and in the stamp box is unenciphered and was not transcribed here.

## Revision 2026-11-02

Second attempt ordered by the human; Claude Opus 5.5. This section supersedes the row 8 to 12 strings and the translations above. New crops: `work/rev2/` (`strip.py`, `rect.py`, `rect2.py` from the local-normalised enhancement; `pca.py`, `pz.py` colour PCA on the wash). The red channel and PCA do not separate text from wash, because both are the same red dye; the normalised green view stayed the most legible.

### Newly read: rows 10 to 12

The break was segmentation. The "h o g a 6 6" of row 11 is the end of a word divided across rows, and row 12 ends with a t that lies off the row, in the wash past the ruled line.

| row | signs as read | normalized |
|---|---|---|
| 10 | e n · v o l n e k · a · l e g · b o l | én volnék a leg-bol- |
| 11 | d o g a b b · e m b e r · a · v i | -dogabb ember a vi- |
| 12 | l a g · e b e r e i · k o z o t | -lág e[m]berei közöt[t] |

Hungarian: "... én volnék a legboldogabb ember a világ emberei között."

Calls in this passage, all disclosed:

1. Row 11 first sign, tall stroke plus short: the h/p/d family; d from word sense only (*boldogabb*).
2. Row 10 end, *b o l*: bowl with stem, leaf-shaped loop and a wave running through the ruled line, all at the wash edge. Shapes fit; the certainty comes from the join with row 11.
3. Row 10 *e* of *leg*: faint bars, count not secure; e from sense.
4. Row 10 *n* of *volnék*: two short strokes joined to the end of the wave.
5. Row 11 end, *i*: a large curved sign under the wash past the ruled line, x about 1620-1680. Its shape is not sharp; i rests on *világ*.
6. Row 11 sign before *v*: two bars, so a. The earlier "e" alternative is not supported.
7. Row 12 *eberei*: no m sign exists between e and b, so the m is the writer's omission, not a hidden sign. Normalized e[m]berei.
8. Row 12 *t*: stem crossing the ruled line with a head bar in the wash at x about 1650-1730; the t sign, one only, so *közöt* is normalized közöt[t].

The chevron for v, the 9-shaped g, the 6 for b, the x for z and the section mark for k match the same signs elsewhere on this card. The doubled 6 in row 11 is simply bb, not digits.

### Still unread

- **Row 6 middle and end.** *n a gy o n* and *szépen* are weaker than the earlier text claimed. Only `r a`, then `n`, then `s z e` (accent on e) are clear; a blot follows, then strokes and `a`. *Szépen* is a possible reading, not a secure one. The row ends with something like `h a`.
- **Row 7 before *én is úgy*.** `? a s z e k`, then a slanted sign (r or the h/p family), then doubled strokes, a hook and a cross. No parse. The first sign is a faint stroke with an arm, not identified. The *n* of *én* would lie in a wash patch. *Én is úgy* itself rests on `e [n] i s u [gy]`, where the gy is a blob.
- **Row 8 after *éreznék*.** `m i n t a`, then tall stroke plus short (h/p/d), then o. The i and n are faint. Whether the word is *mint a* or a misspelled *mintha* is open, since no h stands between t and a.
- **Row 9.** Clear signs: `e s o r o` (the second o has a dot, so possibly ö), a blot with a short stroke beside it (k, or h/p/d), a sign with two bars and a descender not found in the family key, then `g z a n`, then `k a k o`. The first k has its lower part in the wash. Tried and rejected as unproven: *és örökre* (the printed verse on the picture side ends *Mindörökre*), *igazán*, *csak ő*, *hazánk*. Each needs a sign to be other than it looks or a letter to be supplied. No word is claimed.

These are whole clauses, so the card stays partial under the completeness rule. The clause between *éreznék* and *én volnék* is the core of the sentence and is not understood.

### Current best text

> Kedves Jolánkám! Becses levelezőlapját megkaptam, melyért fogadja őszinte köszönetemet. Becses sorait nagyon [szépen?] [...] én is úgy éreznék, mint[ha?] [...] én volnék a legboldogabb ember a világ e[m]berei közöt[t]. Édesem, én már húsvétkor megmondtam, rossz idő lesz. Isten vele, a viszontlátásra.

Stamp box, plain script in red: **csókol|lom szám|talan|szor** (Csókolom számtalanszor). Line 3 is mostly under a blot; only its end is clear, and *szám* comes from the set phrase, which recurs on hcp-1216. The final r of line 5 looks like s.

English: "Dear Jolánka! I received your esteemed postcard, for which please accept my sincere thanks. Your esteemed lines very [nicely?] [...] I too would feel as [if?] [...] I would be the happiest person among the people of the world. My sweet, I told you already at Easter that the weather would be bad. God be with you, goodbye." Stamp box: "I kiss you countless times."

Slovak: „Milá Jolánka! Dostal som Váš vážený lístok, za ktorý prijmite moju úprimnú vďaku. Vaše vážené riadky veľmi [pekne?] [...] aj ja by som sa cítil, ako [keby?] [...] bol by som najšťastnejší človek medzi ľuďmi sveta. Moja sladká, ja som už na Veľkú noc povedal, že bude zlé počasie. S Bohom, dovidenia." V rámčeku na známku: „Bozkávam Vás nespočetnekrát."

### Unenciphered text, now transcribed

- Address side, plain red script: Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás. The first word's ending is faint and its reading is supported by the same formula on a sister card.
- Picture side, printed: Megyek, megyek messze földre! Elbujdosok, eltávozok Mindörökre. Sirassatok engem orgonavirágok. Card number 2802/5.

### Superseded items

The row 8 to 12 "literal working strings" above. The note that *én is úgy* is only a guess stands. The claim that rows 1-6 are secure is narrowed to rows 1-5 and the first signs of row 6. The note that the red plain text was not transcribed no longer applies.

Reproduction: still no one-command decoder, because the reading is incomplete. Crops: `work/rev2/rect.py` and `work/rev2/rect2.py` (codex runtime python, -I), which need `work/crops/enh_full.png` from `work/enh.py`.
