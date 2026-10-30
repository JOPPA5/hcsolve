# HCP1311 — Feri to Jolánka Tóth: sorry to have missed the ball at Árokszállás

**Status: complete reading of the 28 main rows; the 7-row closing under the stamp is only partly read, and its end rests on the family formula (residue disclosed below). Review 1 (REVISE) addressed, see the last section.** Written 2026-10-30 by Claude Opus 5.5. All work is Claude Opus 5.5's; there was no earlier work on this number. The key comes from the finished family cards (hcp-1216 and others). The portal shows *Not solved*, with no transcription or solution attached, and no published solution was found.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family, same key as hcp-1216, 1212, 1213, 1217, 1218, 1243, 1301 (legend in `ciphers/hcp-1216/SOLUTION.md`). Word division is not written; accents appear only occasionally, as ticks or dots. Findings specific to this card:

- k has two forms: the section mark (8-like) and an S-hook. The S-hook is distinct from g (ς), and this holds on all rows.
- y is the long-tailed sign, also used for initial i in *imádója* (row 27).
- i and o are the same loop, and only the dot separates them. An undotted loop is read i once, on word sense (row 22).
- The tall stroke with a right tick (h/p) and with a left tick (d) are exchanged twice; see items 2 and 3 below.

Sign table for this card (shape names are the family's; the ledger uses one letter-named token per written sign):

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark or S-hook | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three strokes | m | corner, Γ | t |
| tall stroke, tick at left | d | two strokes | n | plain cross x | u |
| three bars | e | loop without dot | o | chevron | v |
| tilted or upright cross | f | loop with two dots | ö | long tail, hooked head | y |
| ς | g | loop with dot | i | crossed diagonal | z |
| inverted T | j | tall stroke, tick at right | h / p | opposed bowls | cs |

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1311/work/decode.py
```

It checks the SHA-256 of the four scans, decodes `work/ledger.txt` (one token per written sign, 512 signs) and prints the literal rows and `work/normalized.txt`. The command does not apply a separate key: the ledger tokens are already named by letter under the table above, so the ledger is the reading and the command only renders it. The normalized text is a stored editorial file. The ledger is a manual transcription from enlarged crops of the original scan, not OCR.

## Literal decipherment (as printed)

```
01 szeretetedesjolánkamki        15 hestreamimarcsak2½
02 vanomhogyalegjobbegesseg      16 honahlasanmajdel
03 bentalaljasoraimkedvesjo      17 mulikaziskedvesem
04 lankamhogymulatotta           18 irjo{n?}{h?}ogymulatot
05 mulatsagbaremelemjol          19 azthiszemutolsoarok
06 bareniselmehete{m?}vol        20 szalasomulatsagba
07 naigazansajnalomhogy          21 voltmostenmost
08 nemkadtammegegynah            22 mastirokmivelnem
09 halelöbbmintirtam             23 tudokmitirirjon
10 isletvolnaanyiszabad          24 sokathogysokat
11 sagomhogyelmehetem            25 tudakval{e?}szolni
12 volnaheezenmar                26 {i?}stenveledesem
13 nemlehetsegitenimajd          27 yma{d?}{o?}{j?}a   (right of 25-26)
14 mulatunkhafeljön              28 {f?}er

Under the stamp (· = unresolved sign):
S1 udvö{z?}{l?}i··   S2 szam   S3 talan   S4 szor
S5 szer{e?}          S6 ··{k?}ed   S7 {v?}ese{f?}{e?}ri
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb egészségben találja soraim, kedves Jolánkám. Hogy mulatott a mulatságba[n]? Remélem, jól. Bár én is elmehet[t]em volna! Igazán sajnálom, hogy nem kaptam meg egy nappal előbb, mint írtam, [akkor] is lett volna annyi szabadságom, hogy elmehet[t]em volna, de ezen már nem lehet segíteni. Majd mulatunk, ha feljön Pestre, ami már csak 2½ hónap, las[s]an majd elmúlik az is, kedvesem. Írjon, hogy mulatott; azt hiszem, utolsó Árokszálláso[n] mulatságba[n] volt. Most én most mást írok, mivel nem tudok mit ír[ni]. Írjon sokat, hogy sokat tud[j]ak válaszolni. Isten vele, édesem! Imádója Fer[i].

Under the stamp (tentative, see item 1): Üdvözli [..] számtalanszor szere[tő?] [k?]ed[v?]ese [F?]eri.

## English

Beloved sweet Jolánka! I wish that my lines find you in the best of health, dear Jolánka. How did you enjoy yourself at the dance? Well, I hope. If only I could have gone too! I am truly sorry that I did not get it one day before I wrote; I would then have had enough leave to go, but nothing can be done about that now. We will have our fun when you come up to Pest, which is only 2½ months away; that too will slowly pass, my dear. Write how you enjoyed yourself; I think that was your last dance at Árokszállás. Now I am writing about something else, since I do not know what to write. Write a lot, so that I can answer a lot. God be with you, my sweet! Your adorer, Feri.

Under the stamp (tentative, see item 1): [Your] loving sweetheart Feri greets [you] countless times.

## Slovak

Milovaná sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšom zdraví, drahá Jolánka. Ako ste sa zabavili na zábave? Dúfam, že dobre. Keby som tam bol mohol ísť aj ja! Naozaj ľutujem, že som to nedostal o deň skôr, než som písal; potom by som bol mal dosť voľna, aby som mohol ísť, ale s tým sa už nedá nič robiť. Zabavíme sa, keď prídete hore do Pešti, čo už je len 2½ mesiaca; pomaly aj to prejde, drahá moja. Napíšte, ako ste sa zabavili; myslím, že to bola Vaša posledná zábava v Árokszállási. Teraz píšem o inom, lebo neviem, čo písať. Píšte veľa, aby som mohol veľa odpovedať. Zbohom, sladká moja! Váš ctiteľ, Feri.

Pod známkou (neisté, pozri bod 1): Nespočetnekrát [Vás] pozdravuje Váš milujúci milý Feri.

## Uncertainties

1. **Stamp block (S1–S7), the main residue.** The stamp was torn away, with a black triangular postage-due mark and tear patches over the writing. The reading *szerető kedvese Feri* is the family closing (hcp-1307 *Szerető kedvese, Feri*); it is a hypothesis that fits the visible signs, and it is not proved by them.
   - Clear: *ü d v ö*, then a heavy blot; *szám*, *talan* (the l lies in the triangle), *szor*.
   - S1: the blot and the next stroke are read z, l **by sense only**, and the final i is clear. Two marks at the right edge (a single diagonal bar, then a smudged cross) are **unresolved**. They lie at the level of S2, so they may not belong to S1.
   - S5: *s z e r* is clear; the last sign is three bars in a teal smudge, so e is probable. There is blank paper after it, so no t stands in this row (the former *szeret* is withdrawn).
   - S6: a hooked or looped head with a long tail and a right arm ending in a down-hook, then two long strokes. Both are **unresolved**. The head is close to the y of row 2 *hogy*, but *t* and *ő* are not visibly written. *szere[tő]* needs this group to be a t+o ligature with the two strokes as ő marks, and no such ligature or long ő mark is proved on this card. The next sign is brown ink in the smudge with an S-like course; k (S-hook) is **tentative**, and a third stroke of m cannot be excluded. Then three bars and a clear d, so the row ends *…ed*. *imád* is withdrawn: the sign before d has three bars, so it is e, not a. A residual alternative reading is literal *y m e d*, which gives no word.
   - S7: at the left edge there is only the top of a sign beside the tear, a short hook whose right arm ends free; v is **compatible, not read**. Then *e s e*: the third bar of the second e is visible at the tear. Then a long diagonal with a stroke running in from low left, which is the layout of the tilted cross of row 28, with the crossing under the tear; f is **tentative**. Next come three bar levels (e, the second one short), a clear r, and a loop with its dot at upper right (i). The ending *…ese [f]eri* is therefore much better supported than the former *[éd]esem*, which is withdrawn.
   - In all, 4 tokens are unresolved (two in S1, two in S6) and 7 are uncertain (z, l, e, k, v, f, e); t is not visible at all. Nothing here affects the main message. *édese Feri* (his sweetheart) would suit S7 equally if the left fragment is not v.
2. **Row 8 *kaptam*:** the sign has its tick at the left, which is the d form (literal *kadtam*). Read p on word sense.
3. **Row 12 *de*:** the sign has its tick at the right, the h/p form (literal *he*). Read d on sense, the same substitution disclosed on hcp-1216 row 5. Rows 15–16 *Pestre*, *hónap* and rows 8–9 *nap|pal* rest on sense for the h/p choice.
4. **Row 22 *írok*:** the first loop has no dot, so literally it is *o* (*orok*). Read i on sense: *mást írok, mivel* gives the only coherent clause. The sign has the long straight arm of the i forms rather than the hooked top of o, so the shape also favours i. This is the least certain call in the main text.
5. **Row 6 *elmehetem*:** after *t e* the strokes are overwritten by a thick F-like correction; the sign is read m as in row 11, where the same word is clean.
6. **Row 25:** the sign before *szolni* has three levels (long top bar, blotted middle bar, two pieces at the third level), so it is literally e; the ledger now says so. *válaszolni* (a) is a sense call against the sign: a slip or a blotted correction.
6a. **Row 26 first sign:** a compressed crossing at the card corner with no loop and no dot. *Isten* is certain from sense; the sign itself is not a clean i.
6b. **Row 18 after *irjo*:** three strokes (the third short) with a dot, a blotted cross, then a tall stroke with a foot and no clean tick. *irjon hogy* stands on sense: the n and the h are sense calls, and the third stroke is unaccounted for (perhaps a correction of m to n).
7. **Row 27:** the middle of *imádója* is under a green smudge. Signs d, o, j are read with the family formula as support (*imádója* on hcp-1213); y, m, a and the final a are clear.
8. **Row 28:** the first sign is a low tilted cross, not the upright + of row 14; literal u gives no word, so f is by sense (the same case as hcp-1216 item 5). The row ends *fer* with blank paper to the right, so the i is simply not written; the name is taken as Feri, as on family cards and at the end of S7.
9. **Writer's habits, normalized:**
   - Struck or blotted signs (no value): row 4 start and row 18 after *irjon*.
   - Row 14: the n of *jön* is written over.
   - Row 1 *szeretetedes* (*szeretett édes*), row 26 *veledesem* (*vele édesem*): a shared letter.
   - Doubled consonants single: *anyi*, *lasan*, *letvolna*, *mulatot*, *szalaso-*, *elmehetem*.
   - *nap|pal* is split across rows 8–9 with both p written; rows 19–20 *Árok|szállás* is split.
   - *mulatsagba* lacks n; row 20 *szállásom ulatságba* shares one m stroke group, normalized *Árokszálláso[n] mulatságba[n]*.
   - Row 23 *mit ir irjon* is read as *mit ír[ni]. Írjon*; *tudak* is *tud[j]ak*.
   - "[akkor]" in row 10 is an editorial supply for the translation.
   - Row 21 *most én most* is as written.
10. **Plain parts:** the address reads *Tóth Jolánka úrleánynak, Jász-Árokszállás*. A green cursive word of about ten letters above the cancellation, running under the box, is overprinted and I could not read it; it does not appear to be ciphertext. The picture side has only a printed verse (*Ezüsttükrös kávéházban*) and the publisher's number. The cancellation date is not legible, and the railway box reads *…LOTA-ÚJPEST P.U.* (Rákospalota-Újpest).

## Why it is correct

- The family key, applied unchanged, turns all 26 message rows, and the signature rows 27–28, into continuous Hungarian with only the sense calls listed above; the S-hook k / ς g split holds across the card.
- Repeated words decode identically: *hogy* ×6, *mulat-* ×5, *kedves-* ×2, *elmehetem* ×2, *sokat* ×2.
- The content fits the context: Árokszállás is the addressee's town and appears in her address; the *Pest* trip, *Isten vele*, *imádója Feri* and the opening formula match sister cards (hcp-1216, 1213).

## Response to review 1

Verdict REVISE. All findings addressed. The 28 main rows keep their reading; only the tentative closing changes. `work/decode.py` re-run after every change: the hashes pass and it prints the rows above, 512 signs. New crops: `work/crops3.py`, `work/crops4.py`, output in `work/crops2/`.

1. **S6 — fixed.** Agreed. `work/ledger.txt` now has `S6 ! ! ?K2 E D`, and *imád* / adores / zbožňuje are gone. The fourth sign has three bars (e). The stroke count differs slightly from the review: two clear strokes, then the third "stroke" is brown ink with an S-like course, so a k is possible (`crops2/k_smudge.png`). I rechecked *szerető* as you asked: see item 1. One disagreement of detail: the head of the sign is not a free shape, since it is close to the y of row 2 *hogy* (`work/crops/b00L.png`).
2. **S7 — fixed.** Literal *r i* recorded, and the hypothesis tested. The low left stroke is separate from the third bar of the preceding e, which lies at the tear (`crops2/f_s7.png`), so *esem* has no room for an m before the diagonal. The ending is *…ese [f]eri*, and the sharing of *[éd]* is dropped. A new observation: a hook fragment at the left of S7 (`crops2/v_frag.png`) is compatible with v, which gives the family closing *szerető kedvese Feri*. This is marked uncertain, since v, k and f are all tentative and t is unseen. S5's *?T* is also withdrawn.
3. **Row 25 — fixed.** Token is now `?E`; item 6 states the sense call.
4. **Row 26 — fixed.** Token `?I`; item 6a.
5. **Row 28 — fixed.** Token `?F`; item 8 corrected: blank paper, i not written.
6. **Counts — fixed.** *hogy* ×6, *mulat-* ×5, and the 26/28 rows wording.
7. **nap|pal — fixed.** Both p written.
8. **Row 18 — fixed.** Tokens `?N ~x~ ?H`; item 6b.
9. **Command — fixed.** Sign table added, and the Reproduction section says plainly that the ledger is the reading.

Could not verify, as in the review: the green cursive word (item 10 said short; it runs to about ten letters and under the box, and is unread), the date, and anything under the torn stamp.
