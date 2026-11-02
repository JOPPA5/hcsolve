# HCP1234 — Feri to Jolánka Tóth: a practice card with a love verse in cipher

**Status: complete reading; review 1 verdict ACCEPT, no change to the reading.** Written 2026-11-02 by Claude Opus 5.5.

Credit: transcription and decipherment of this card by Claude Opus 5.5, 2026-11-02; there is no earlier work on this number. The key was transferred unchanged from the finished Jolánka cards (HCP1216 with its legend, also 1212, 1213, 1217, 1218, 1243, 1301), which were solved by the OpenAI GPT solver and completed by Claude Opus 5.5. The portal shows status Not solved and attaches no transcription or solution. No published solution of this card was found or used.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the Jolánka postcard family). Portal language "Unknown" is resolved: Hungarian. Sign classes as in HCP1216:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| long stroke + short tick on the LEFT | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + tick on the RIGHT | h / p | low descender | y |
| hook with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | (sz = s + z, gy = g + y, ny = n + y, two signs) | | | |

Dots over o/u give ö/ü. Acute ticks are written on some vowels. Not all are written, and the rest are supplied in normalization. No new sign value was needed. On this card the plain x and the "z" cross are not separable by shape; u or z is chosen by the word (see item 7).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1234/work/decode.py
```

It checks the SHA-256 of both source scans and both hires originals, decodes the hand-made sign ledger `work/ledger.txt` (449 signs, 20 main rows plus 6 rows in the stamp box), prints the literal rows, then prints `work/normalized.txt`.

## Literal decipherment (spaces editorial; h = the h/p sign)

```
01 szeretet édes jolankam          11 csokal teszek ra hecsétet
02 gyakorlatot tartok              12 A csókadas nem szégyen
03 az írasban hogy el ne           13 hanem inkáb erény
04 felejtsem tudatom hogy          14 ha csokot adsz babám
05 nem sikerült hazamen            15 sohasem légy szerény
06 ni délelőt írok egy             16 Nem kérek én lehetetlent
07 harat a gondolataimbol          17 csuhan azt hogy szeres
08 boldog csak ugy Lehetek én      18 hedig ez okvetlenül kell
09 hogy ha te leszel az enyem      19 hogy te boldog lehess
10 nem szeretek mast csak téged    20 isten vele a viszontlátásra imádoja feri
stamp box: hit remeny / és szeretet / kösse össze / szivonket / imadoja / feri
```

## Unenciphered text on the card

- Address, plain Hungarian: Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás ("To the promising young lady Jolánka Tóth, Jászárokszállás").
- Picture side, printed verse: Van nekem egy tikom [sic, apparent misprint of titkom; normalized titkom] / Rejtegetem titkon / Csak az fejthetné meg, / Kinek e levél megy! ("I have a secret, I hide it in secret; only the one this letter goes to could solve it.") The verse fits a cipher card.
- Postmarks: Jászárokszállás, DEC 16 legible. The year is not read: 1913 is only the date in the portal file name (1913-12-16), not a reading of the card, and the digit just before DEC looks like a 1, with the same foot as the 1 of 16, which would suit a year ending in 1. The other digits are not legible, so this is a doubt, not a correction; a second postmark begins GYÖ... and is cut off, so its place is not identified.

## Hungarian (normalized; brackets = letter not on the card)

Szeretet[t] édes Jolánkám! Gyakorlatot tartok az írásban, hogy el ne felejtsem. Tudatom, hogy nem sikerült hazamenni délelőt[t]. Írok egy párat a gondolataimból.
Boldog csak úgy lehetek én, hogy ha te leszel az enyém, nem szeretek mást, csak téged. Csók[k]al teszek rá pecsétet.
A csókadás nem szégyen, hanem inkáb[b] erény. Ha csókot adsz, babám, sohasem légy szerény.
Nem kérek én lehetetlent, csupán azt, hogy szeres[s], pedig ez okvetlenül kell, hogy te boldog lehess.
Isten vele, a viszontlátásra. Imádója Feri.

Under the stamp: Hit, remény és szeretet kösse össze szívünket. Imádója Feri.

## English

My beloved sweet Jolánka! I am practising the writing so that I do not forget it. I let you know that I did not manage to get home in the morning. I am writing down a few of my thoughts.
I can only be happy if you become mine; I love no one else, only you. I set a seal on it with a kiss.
Giving a kiss is no shame, rather a virtue. When you give a kiss, my baby, never be modest.
I ask nothing impossible, only that you love me, yet this is absolutely needed so that you may be happy.
God be with you, until we meet again. Your adorer, Feri.

Under the stamp: May faith, hope and love bind our hearts together. Your adorer, Feri.

## Slovak

Moja milovaná sladká Jolánka! Cvičím sa v tomto písme, aby som ho nezabudol. Oznamujem, že sa mi nepodarilo dostať sa domov predpoludním. Píšem niekoľko svojich myšlienok.
Šťastný môžem byť len vtedy, ak budeš moja; nemilujem nikoho iného, len teba. Bozkom na to dávam pečať.
Dať bozk nie je hanba, ale skôr cnosť. Keď dávaš bozk, zlatko, nikdy nebuď skromná.
Nežiadam nič nemožné, len aby si ma milovala, a to je nevyhnutne potrebné, aby si bola šťastná.
S Bohom, dovidenia. Tvoj ctiteľ Feri.

Pod známkou: Nech viera, nádej a láska spoja naše srdcia. Tvoj ctiteľ Feri.

## Uncertainties (none changes the sense)

1. **Row 5, s of sikerült.** The sign is overwritten: a heavy right bowl with a slash through it. The bowl fits s and the word needs s. Read from word sense. Row 12, s of szégyen, is a similar heavy overwrite, which looks like a bowl fused with the cross; *szégyen* is the only word and it rhymes in sense with *erény*.
2. **Row 6, ő of délelőt.** A heavy overwritten blot: a loop with two strokes above it, read as ő (double mark). Word sense supports it. The writer wrote one t.
3. **Row 7, p of párat.** Overwritten, with a long stroke, hairline and short stroke on the right. It is the h/p sign; p is from sense.
4. **h/p calls resting on word sense** (the sign is one and the same): p in *párat, pecsétet, csupán, pedig*; h elsewhere (*hogy, ha, hanem, hit, hazamenni, sohasem, lehetek, lehetetlent, lehess*).
5. **Row 8, l of lehetek.** Not the usual wave but a cursive Latin l-like loop with a lead-in. A blot also touches the h in that word. Read from *lehetek én*. It may be a plain Latin letter, like item 6.
6. **Cursive capitals.** Row 12 opens with a cursive A and row 16 with a cursive N (followed by cipher signs e m), which are Latin capitals, not cipher signs. Each stands exactly where a new sentence of the verse begins. Value from shape and sense.
7. **u/z.** The crosses are not reliably distinct on this card; *az, hazamenni, szeretek* etc. and *tudatom, csupán, úgy* are chosen by word sense. Dotted forms (sikerült, okvetlenül) are clear.
8. **S4 szivonket** has an o sign (no dots visible) where standard Hungarian has ü. Normalized *szívünket*; either the writer omitted the marks, or the form is a dialect *szívönket*. The k in this word has a closed, 8-like shape, read as k from sense.
9. **Row 19, final ss.** The last two bowls are written in brown with the last one overwritten in purple. Read as s s; *lehess* rhymes with *szeress*.
10. **Writer's spellings normalized:** szeretet → szeretett, délelőt → délelőtt, csokal → csókkal, inkáb → inkább, szeres → szeress; csókadás is taken as one word (kiss-giving). Most accents are supplied.
11. Word division, punctuation and the verse layout are editorial. The card has a few commas and full stops, not transcribed in the ledger. Row 19 also has one long single dash between *te* and *boldog*, far longer than a bar of a or e; it has no letter value and is not in the ledger. Faint ticks are recorded only approximately in the ledger, since no reading depends on them.
12. The ledger was transcribed by hand with the family key known, so the reading is not blind.
13. Foxing specks (rows 11, 12) are paper damage, not signs. *Isten vele* (formal) after *te* (informal) in the verse is what the card says. The verse's source, if it is a known folk verse, was not traced.
14. **Stamp row 3, second bowl of *össze*.** It has a straight rising left stroke and looks close to the chevron v of S4 (*sziv-*), and the z and e after it nearly touch. Read as s from *kösse össze*, which is certain from sense; the ledger keeps s.
15. **Row 14, *o* of csokot and *d* of adsz.** Flagged `!` in the ledger only because the strokes are heavy. Both are legible; neither call depends on sense beyond the shape.
16. Sender Feri is named on the card, and HCP1216 is also signed Feri; identity with the sender of other family cards is plausible but not proved.

## Why it is correct

- The family key, transferred unchanged, turns all 449 signs into Hungarian with no unknown sign value and no unread clause.
- The middle of the card scans as rhymed verse, which the decipherer did not impose: *erény / szerény*, *szeress / lehess*. A forced reading would not rhyme. The stamp box gives the known triad *hit, remény, szeretet* (faith, hope, love, 1 Corinthians 13).
- Repeated words decode identically (*hogy* ×5, *imádója Feri* twice, *boldog* twice, *szeretet* twice).
- The context fits: address to Jolánka Tóth at Jászárokszállás, the printed verse about a secret only the addressee can solve, and the opening remark that he is practising "the writing" so as not to forget it, which refers to the cipher itself. Closing formulas (*Isten vele, a viszontlátásra*) and the signature Feri match the family.

## Response to review 1

Verdict ACCEPT, five minor findings, none changes a letter of the plaintext. I checked each on the reviewer's crops. `work/ledger.txt`, `work/decode.py` and `work/normalized.txt` are unchanged; the command was re-run and still prints OK for all four hashes and 449 signs.

1. **Printed verse, tikom: agreed, fixed.** `review/work/crops/verse.png` clearly shows "tikom" in line 1 against "titkon" in line 2. The unenciphered section now gives the print with [sic] and the normalization.
2. **Dash in row 19: agreed, fixed.** `crops/dash.png` shows a single long stroke between the e of *te* and the b of *boldog*. Recorded in uncertainty 11 as having no letter value.
3. **össze, stamp row 3: agreed, fixed.** `crops/st3b.png` shows the shape described. Added as uncertainty 14.
4. **Ledger flags on row 14: agreed, fixed.** Added as uncertainty 15, so every `!` in the ledger now has an entry in the uncertainties. The flags stay in the ledger, which is left as handed over.
5. **Date: agreed, fixed.** On `crops/pmdate.png` DEC 16 is clear, and the sign before DEC looks like a 1. The postmark line now treats 1913 as the portal's date only. The report does the same.
