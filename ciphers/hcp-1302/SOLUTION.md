# HCP1302 — Feri(?) to Jolán Tóth: PARTIAL decipherment

**Status: PARTIAL. No DONE marker.** Claude Opus 5.5, 2026-10-30. No earlier work exists on this number. The portal shows Not solved and attaches no solution or transcription.

## Cipher and key

Hungarian, monoalphabetic graphic substitution of the Jolánka family. The key is the one in `ciphers/hcp-1216/SOLUTION.md` and `ciphers/hcp-1301/SOLUTION.md`, transferred unchanged. The plain address side reads Tóth Jolán[ka] úrleány[nak], Jász-Árok[szállás]. Hand and ink fit the family.

Variants on this card: k appears as both the 8-shape (kám) and an S-shape (kor, kis); g appears with a looped head in row 3. Dotted and undotted crossed curves were both met, so i/o rest partly on the marks and on word sense.

## Reproduction

```sh
python3 -I ciphers/hcp-1302/work/decode_opus.py
```

This checks all four scan hashes and prints `work/ledger-opus.txt`. The ledger is a manual reading from pixels, not OCR.

## Reading (normalized; the unread parts are marked)

Szeretet(t) édes Jolánkám! Hogy találta magát vasárnap? Én elég jól mulattam, igaz, hogy én hamar feltalálom magam. Itt volt [Á]rokszállásból kis angyalka is, és elég jól mulatott. Fél ötkor mentek el a mulatságból, én is hatkor mentem haza. Csak az fáj, hogy nem Jolánkámmal mulathattam, de ezen nem segíthetünk, már mi nem zárhatjuk ki a cselédeket se a mulatságból. **[unresolved: jöjöne z…? …anot majdnem legy kevertné ?? eg]** Isten vele, a viszontlátásra.

Under the stamp (rows partly erased; only the visible letters are claimed): csókol[o]m számta|lan…r | … | imádó… | ja Feri. The likely formula *csókolom számtalanszor … imádója Feri* is a hypothesis from sister cards, not a reading.

## English (of the read part)

Beloved sweet Jolán! How did you enjoy yourself on Sunday? I had quite a good time; it is true that I quickly find my feet. A little angel from Árokszállás was here too, and she had quite a good time. They left the party at half past four, and I too went home at six. Only it hurts that I could not have my fun with my Jolán, but this cannot be helped, for we cannot shut the servants out of the party either. [unresolved passage] Farewell, until we meet again.

## Slovak (čítaná časť)

Milovaná sladká Jolán! Ako ste sa zabavili v nedeľu? Ja som sa zabavil celkom dobre, pravda, ja sa rýchlo nájdem. Bol tu z Árokszállásu aj malý anjelik a zabával sa celkom dobre. O pol piatej odišli zo zábavy, aj ja som o šiestej išiel domov. Len to ma bolí, že som sa nemohol zabávať so svojou Jolán, ale tomu nepomôžeme, veď ani slúžky nemôžeme vylúčiť zo zábavy. [nevyriešené miesto] S Bohom, dovidenia.

## Why it stops (the blockers)

1. **Row 18 after *mulatságból*** (x about 2000-2400): `j ö j ö n e`, a z-shaped sign, a large O, then a dotted crossed curve overlapped by a 5-shaped sign with a tick above, then signs read `a n . o t`, then `majdnem`. The z and O may be the numeral 20, which would suggest a date form such as *20-i* or *20-ig*, but no sentence comes out of it. *jöjön* is itself only a guess at *jöjjön*.
2. **Row 19 before *Isten***: `legy kevertné`, then two heavily overwritten blots, then `eg`. No sound Hungarian emerged. Forcing *légy kedves* is ruled out, because the signs are clearly r and v, with no d.
3. **Stamp rows S3-S5** are partly erased and row S4 is not read.

Together these are a whole clause, so this is not a small residual and the card is not handed over.

## Other uncertainties in the read part

- Row 1: the first sign is a struck or overwritten cross before *sz*; no value given.
- Row 1: only one t in *szeretet(t)*.
- Row 2: the sign after *tala* is a stretched form unlike the usual wave; read l from word sense.
- Row 3: g of *magát* is a looped variant, by word sense.
- Row 6: the a of *magam* is a heavy two-bar sign with a vertical stroke, by word sense.
- Rows 6-7: *volta rok|szalasbol* is divided as *volt [Á]rokszállásból*; the a stands for Á and one t is shared. Word sense, but it fits the address.
- Row 8: literal *kais es*; normalized *(angyal)ka is, és*. The word split across rows 7-8 is an interpretation. *Kis angyal* may be a nickname or a person.
- Row 11: *6atkor*: a six sign is followed by *atkor*. It is either b written for h or the numeral 6; normalized *hatkor*.
- Row 14: *Jolánkámal* normalized with mm.
- Row 15: *de e ezen*: one e is doubled in writing (*de ezen*).
- Row 17: the last sign of *cselédeket* is a thick F-like shape with a detached dash; t rests on word sense. Literal r is possible.
- Row 18: *se* for *sem*.
- Row 19: *viszontlátacsra*: left and right bowls appear where s is expected; normalized *viszontlátásra*.
- The date is not read; the cancellation is faint.

## Why the read part is believed

The key was transferred unchanged and gives continuous, idiomatic Hungarian over about 16 of 19 rows, with the closing formula matching sister cards. *Árokszállás* agrees with the plain address. No published solution was found or used.
