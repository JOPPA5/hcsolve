# HCP1309 — Feri to Jolánka Tóth: a new job at Rákospalota, and his address

**Status: complete reading with disclosed residual points; review 1 verdict REVISE, findings addressed below.** Claude Opus 5.5, 2026-10-30. Earlier work on this number: none. The key comes from the finished Jolánka cards (HCP1216, 1212, 1213, 1217, 1218, 1243, 1301). Those cards were started by the OpenAI GPT solver and completed by Claude Opus 5.5; here the key was only reused, and every sign of this card was read afresh. The portal shows *Not solved* and attaches no transcription or solution, and no published solution of this card was found.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the Jolánka family). The key is that of `ciphers/hcp-1216/SOLUTION.md`, with no change and no new sign value:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| long + short stroke | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | long + short stroke | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | opposed bowls | cs | | |

Dots or a double tick over o give ö/ő. A single tick over bars gives é/á. On this card *gy* is written as two signs (g + y).

The address block, the return address *Rákos Palota / Tavasz u. 2 sz.* and the printed picture-side words are in clear.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1309/work/decode.py
```

It checks the SHA-256 of both `source/` scans and both hires originals, decodes `work/ledger.txt` with the key above, and prints the literal rows and then `work/normalized.txt`. The ledger is a manual transcription from enlarged crops (`work/crops/`, made by `work/crop.py`). It is not OCR. The normalized text is editorial.

## Literal decipherment

```
01 szeretetedesjolakamki          11 lankamhogymulat[o]t
02 vanomhogyjoegéseg              12 vasarnapénbenvoltam
03 bentaljasoraimtu               13 pesten{del}bélval
04 datomhogymárél                 14 töltöltötemad[e]lutant
05 jötemszentmihajrol             15 kedvesjolankamirjon
06 ésmostrakospalota[n]           16 hogymiujság[a]rok
07 dolgozomésittisla              17 szalasbaedesebecses
08 komerölmegbövennemir           18 soraitvarva[c]zim
09 hatokmertcsakszomba            19 holesferi   + in clear: Rakos Palota
10 tontudoktobetkedvesjo          20 in clear: Tavasz u 2 sz
stamp field: is[t]enve / le{smear}leéde / sem / csoko / lomszam / talanszor
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy jó egészségben találja soraim. Tudatom, hogy már eljöttem Szentmihályról, és most Rákospalotán dolgozom, és itt is lakom. Erről meg bőven nem írhatok, mert csak szombaton tudok többet. Kedves Jolánkám, hogy mulatott vasárnap? Én benn voltam Pesten, Bélával töltöttem a délutánt. Kedves Jolánkám, írjon, hogy mi újság Árokszállásba[n]. Édes, e becses sorait várva. Cím: Holes Feri, Rákos Palota, Tavasz u. 2 sz.

Under the stamp: Isten vele … édesem! Csókolom számtalanszor.

## English

My beloved sweet Jolánka! I wish that these lines of mine find you in good health. I am letting you know that I have already left Szentmihály, and I now work at Rákospalota and live here too. I cannot write at length about this, because only on Saturday can I [write/tell] more. Dear Jolánka, how did you enjoy yourself on Sunday? I was in town, in Pest, and spent the afternoon with Béla. Dear Jolánka, write and tell me what is new in Árokszállás. Sweet one, awaiting these precious lines of yours. Address: Holes Feri, Rákospalota, Tavasz utca 2.

Under the stamp: Farewell … my darling! I kiss you countless times.

## Slovak

Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky zastihli v dobrom zdraví. Oznamujem Vám, že som už odišiel zo Szentmihályu a teraz pracujem v Rákospalote a aj tu bývam. Obšírne o tom nemôžem písať, lebo až v sobotu budem môcť [napísať] viac. Milá Jolánka, ako ste sa zabávali v nedeľu? Ja som bol v meste, v Pešti, a popoludnie som strávil s Bélom. Milá Jolánka, napíšte, čo je nové v Árokszállási. Sladká, čakajúc na tieto Vaše vzácne riadky. Adresa: Holes Feri, Rákospalota, Tavasz utca 2.

Pod známkou: S Bohom … moja drahá! Bozkávam Vás nespočetnekrát.

## In clear on the card

- Address, in clear: *Szépreményű Tóth Jolánka úrhölgynek, Jász Árokszállás.*
- Return address, in clear: *Rákos Palota, Tavasz u. 2 sz.*
- Printed on the picture side, in green: *Találkozhatnánk? Csütörtökön* ("Could we meet? On Thursday"). This is the printed text of the card, not part of the message.

## Uncertainties

**Open points**

1. **Surname (row 19): Holes, with H resting on a sister card.** The signs are a long + short stroke, o, l, e, s, then Feri. On this card the first sign is only the d/h/p class. H comes from HCP1303, another Feri card, which has in plain pencil, after the cipher, *cím Holes* (the same "address: name" construction) and then a faint word. The review of HCP1303 sees that word beginning *Fe…* and notes that the capital of *Holes* is not a textbook H and looks somewhat like this hand's J. The sign on this card rules J out, because cipher j is the inverted T. So the two cards support each other: the d/h/p class here, a capital read as H there. HCP1296 is signed in plain writing `[H?]al[o/e]s Ferenc`, a weaker parallel with an uncertain vowel. That the three names are one man is likely, not proved. HCP1303 is not finished and HCP1296 leaves the identity open, so I cite them as cross-references, not proof.
2. **Stamp field, row S2: part unread.** After *le* (completing *vele*) a red smear covers a stretch, and then *le* is written again before *édesem*. The bars after the first *l* also run into the smear. I cannot say what stood in the smear, or whether the second *le* is a repeat. It is marked {smear}, and the normalization shows an ellipsis. The unread material is not only a stretch of S2: in an enhanced channel (`review/work/crops/smear.png`), below the first *le* and left of *sem*, there is a hook-like sign and a long bar. These are remains of further signs or set-off between S2 and S3, and I cannot read them.
3. **Struck-out stretch, row 13.** The writer deleted some signs with two lines; they begin j, o and are not read. The dotted i sign at the end of the stretch is crossed by the lower line, so I treat it as deleted too. If it were kept, the next word would be *ibélval*, which gives no sense.
4. **Row 17 `ebecses`.** All signs are clear. The stretch reads *édes e becses*. I take it as *Édes, e becses sorait várva*. The alternative is a stray e before *becses*. The sense is the same.

**Calls that rest on word sense (d/h/p, n, s)**

5. The long + short class is one shape here, and d also appears with the short stroke on the left. *dolgozom* (row 7) and *délutánt* (row 14) are written with the long stroke first, the same shape as p in *Rákospalotán* and *Pesten*. *mihajrol* (row 5) has the h written with the short stroke first, a d-like shape. Each value is chosen because only it makes the word.
6. **Row 6, last sign.** It is two strokes with a short second one, ledger `[n]`. This fits n by sense (*Rákospalotán*), but the shape is close to the d/h/p class, and neither of those gives a word.
7. **Row 3, the s of *soraim*.** The sign's top is touched by the loop of the i in the row above, so it looks like a section mark (k). I read a right bowl; *soraim* is the family's formula (*találja soraim*, HCP1213, 1217, 1315, 1317).

7a. **Row 7, final a of *la|kom*.** There are two bars, but a red dot sits on the divider rule where a third bar would fall (`review/work/crops/r7.png`). As three bars it would be e, giving *lekom*, which is no word, so a stands on sense.

**Overwritten or damaged signs**

8. **Row 11 `[o]` of *mulatott*.** The sign is heavily overwritten between two t signs. The cursive-o outline is visible, but the sign is not clean; the value rests partly on sense.
9. **Row 14 `[e]` of *délutánt*.** Three bars are written over an earlier sign, apparently o, as a correction. A pale red blot touches the a of *-tánt* on the margin line, but the bars can be seen.
10. **Row 16 `[a]` of *Árokszállás*.** Not a clean a: two bars with slanted strokes between them, a #-like block, apparently bars written over two strokes. The same blot-like form is seen in the stamp field in *számtalanszor* (S6), where a is required. The g just before it is written over another sign, probably a six.
11. **Row 18 `[c]` of *cím*.** Over-inked left bowl with a dot to its left. The word was recovered from sense: it stands directly before the name and the address. The spelling *czím* is the normal old one, and HCP1303 has the same word in clear before a name (*cím Holes*). Row 18 also opens with an over-inked s.
12. **Stamp field.** In S1 the t of *Isten* is smeared but the sign's top and stem are visible. In S6 the lower part of the last o is rubbed off, and the r stands on the stamp's perforation line with its stem partly lost.

**Writer's spelling, normalized**

13. *szeretet* → szeretett; *jolakam* → Jolánkám (n omitted); *egéseg* → egészség; *talja* → találja; *él|jötem* → eljöttem (the é is ticked on the card); *jötem* → jöttem; *mihajrol* → Mihályról; *komerölmeg* (rows 7–8, la|kom + eről meg) → lakom, erről meg; *bövennem* → bőven nem ("at length"); *tobet* → többet; *mulat[o]t* → mulatott; *ben* → benn; *bélval* → Bélával; *töltöltötem* → töltöttem (dittography of *töl*); *szalasba* → (Árok)szállásba[n], which the writer may well have meant as written, in spoken Hungarian; *cím* is normalized from *czim*.
14. *Szombaton tudok többet* has no infinitive on the card; *írni* (or similar) is understood, and is given in brackets in the translations.
15. *Szentmihály* is taken as a place name, presumably Rákosszentmihály next to Rákospalota, but the card does not say which Szentmihály. The date is not legible on the card; the portal filename suggests 1912.
16. **Postmarks.** The card has two strikes, both unread. In a ring right of the stamp three capitals show, read as `?AL`, where the first is a closed O/D-like form. A reading PAL(OTA) would need a P whose stem cannot be seen, so it is not claimed. Top centre, a faint strike shows only broken characters and a barred block. Neither gives a place or a date.

## Why it is correct

- The family key was applied unchanged. It gives Hungarian across all 19 rows and the stamp field, with no new sign value. The only stretches without a reading are the writer's deletion and the smear.
- The family formulas appear in their usual places: *találja soraim*, *Tudatom*, *Isten vele*, *csókolom számtalanszor*.
- The cipher text agrees independently with parts of the card in clear. *Rákospalota* in row 6 matches the clear return address. *Árokszállás* in rows 16–17 matches the address block. The word *cím* stands just before the clear address, where a label is expected.
- Repeated words decode the same way: *hogy* ×4, *kedves Jolánkám* ×2.

## Response to review 1

Verdict REVISE. All seven findings are addressed; the decoded letters did not change. The ledger gained one accent (row 4), and the reproduction command was re-run after the changes: all four hash checks print OK.

1. **Surname (major): fixed.** The claim that no sister card gives the surname was false, and I withdraw it. I viewed `review/work/crops/s1303.png`: *cím Holes* stands in plain pencil on HCP1303. Normalization and all translations now give *Holes Feri*, and Uncertainty 1 says H rests on HCP1303 while this card gives only the d/h/p class. It also reports what the HCP1303 review found: its capital is not a textbook H. This card excludes the J alternative, since cipher j is the inverted T. Uncertainty 11 now cites the same clear word.
2. **Row 7 final a: fixed.** I confirmed the two bars and the red dot on the rule (`r7.png`) and added item 7a.
3. **Stamp residue: fixed.** I confirmed the hook-like sign and long bar in `smear.png`. Uncertainty 2 now says the unread material extends below S2, and that I cannot read it.
4. **Accents: fixed.** I confirmed the tick above the gap after the a in `r4.png` and take it as the accent of *már*: the ledger is now `A:tick`, and literal row 4 reads `datomhogymárél`. The ticked é of *él* is added to item 13.
5. **Formula citation: fixed.** I confirmed that `hcp-1212/SOLUTION.md` has no *talál-* form and dropped HCP1212. *találja soraim* is in HCP1213, 1217, 1315 and 1317.
6. **Postmarks: fixed.** Item 16 describes both strikes, unread. I saw the same forms in `PM.png` and `pm_r.png`.
7. **Normalization: fixed.** *bőven nem* replaces *bővebben nem*; the English and Slovak follow it, and item 13 is corrected.

I also adopted two corrections from the review's checks. In Uncertainty 7 the sign touching the s is the i of row 2, not a y-descender. In Uncertainty 10 the row 16 sign is described as the #-like block it is.
