# HCP1313: Jolánka-family postcard of 7 April 1912. PARTIAL decipherment, not complete

**Status: partial. No marker created.** Claude Opus 5.5, 2026-10-30. No earlier work exists on this number; no published solution was seen. Portal: Not solved, no attachment.

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
