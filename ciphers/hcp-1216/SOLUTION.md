# HCP1216 — Feri to Jolánka Tóth: waiting for a letter, passing Vámosgyörk

**Status: complete reading; review 1 verdict ACCEPT, minor disclosure points addressed (see Response to review 1).** Updated 2026-10-30 by Claude Opus 5.5.

Credit: the source capture (2026-10-12), the transfer of the Jolánka-family key from HCP1301/HCP1243, and passes 1–5 of the reading (2026-10-12/13) were done by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol); see NOTES.md. Those passes left rows 4–5, the sign after "menni" (row 18) and the sign before "og" (row 21) unresolved. On 2026-10-30 Claude Opus 5.5 re-checked every row on enlarged crops of `source/address.jpg`, corrected the ledger (rows 4, 5, 9, 18, 21) and closed those gaps. No external plaintext was used; the portal shows status *Not solved* and attaches no transcription or solution; the orchestrator's AI-register check (2026-10-29) found no record of this card.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the "Jolánka" postcard family, same key as finished cards HCP1213, 1217, 1218, 1243, 1301). Accents are written as marks over the base sign. Sign classes (names as in `work/as-seen-provenance.json`):

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| long stroke + short tick (joined) | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short (h/p near-homograph) | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal (x with tail) | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

Diacritics: dots over o/u give ö/ü; a double mark gives ű; acute marks are faint and are supplied in normalization.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1216/work/decode_opus.py
```

It checks the SHA-256 of both source scans, decodes the sign ledger `work/ledger-opus.txt` (one token per written sign, all 23 main rows plus 6 rows under the stamp) with the key above, prints the literal letters row by row, and then prints the normalized text `work/normalized-opus.txt`. The ledger is a manual transcription made from the pixels (not OCR, and not blind: earlier readings were known).

## Literal decipherment (as printed by the command)

```
01 szeretettedesjolankam          13 hogyjolnezkimerbi
02 nemtudommirevelnihogy          14 zonyregennemlattam
03 nemirmarszerdaihostais         15 amultkorhogyerement
04 elmentesme{m|n}ostisneküznöm    16 temojannezemreesett
05 kelsoraitdehighiggyjeel        17 vamosgyörkmelletel
06 edesemugyvaromminta            18 men{|}ennideleküzdottem
07 zsidokamessiastedesegye        19 fajdalmammertbiz
08 tlenremenyemhogyvan            20 tatottazatudathogy
09 egessegesealligvarom           21 nemsokafelfogjonni
10 hogyviszontlathas              22 esakorviszontlathatomistenveleaviszont
11 sammulthetenbeszeltem          23 latasra  (up the right edge)
12 asandorralmondta               stamp: csokolom szamta lanszor sirighű kedvese feri
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Nem tudom, mire vélni, hogy nem ír. Már szerdai posta is elment, és mé[g] most is nélkülöznöm kell sorait. De higgye el, édesem, úgy várom, mint a zsidók a Messiást. Édes egyetlen reményem, hogy van, egészséges-e? Alig várom, hogy viszontláthassam. Múlt héten beszéltem a Sándorral, mondta, hogy jól néz ki, mer[t] bizony régen nem láttam. A múltkor, hogy erre mentem, olyan nehezemre esett Vámosgyörk mellett elmenni, de leküzdöttem fájdalmam, mert biztatott az a tudat, hogy nemsoká fel fog jönni, és akkor viszontláthatom. Isten vele, a viszontlátásra.

Under the stamp: Csókolom számtalanszor. Sírig hű kedvese, Feri.

## English

My beloved sweet Jolánka! I do not know what to make of your not writing. The Wednesday post has already gone, and even now I must do without your lines. But believe me, my darling, I wait for them as the Jews await the Messiah. My sweet, only hope, how are you, are you well? I can hardly wait to see you again. Last week I spoke with Sándor; he said you look well, for indeed I have not seen you for a long time. The last time I came this way it was so hard for me to pass by Vámosgyörk, but I overcame my pain, because I was encouraged by the knowledge that you will soon come up [to town], and then I can see you again. Farewell, until we meet again.
Under the stamp: I kiss you countless times. Your sweetheart, faithful unto the grave, Feri.

## Slovak

Moja milovaná, sladká Jolánka! Neviem, čo si mám myslieť o tom, že nepíšete. Už aj stredajšia pošta odišla a ešte stále sa musím zaobísť bez Vašich riadkov. Ale verte mi, drahá, čakám na ne, ako Židia čakajú na Mesiáša. Moja sladká jediná nádej, ako sa máte, ste zdravá? Sotva sa dočkám, kedy Vás znova uvidím. Minulý týždeň som hovoril so Šándorom, povedal, že vyzeráte dobre, lebo veru dávno som Vás nevidel. Keď som tadiaľto minule išiel, tak ťažko mi padlo prejsť popri Vámosgyörku, ale premohol som svoju bolesť, lebo ma povzbudzovalo vedomie, že čoskoro prídete hore a potom Vás znova uvidím. S Bohom, dovidenia.
Pod známkou: Bozkávam Vás nespočetnekrát. Váš do hrobu verný milý, Feri.

## Uncertainties (all disclosed; none changes the sense)

The writer drops and repeats letters; every sign is transcribed as written and the normalization is editorial:

1. **Row 4 `me{m|n}ostis`**: after *m e* comes a sign of two strokes plus a short low tick (read as m, n not excluded), then a faint cursive o. Normalized *még most is* ("even now"); the g is **not** on the card (writer's omission, supplied in brackets).
2. **Row 4 `neküznöm`** (n e k ü z n ö m, all signs clear) is normalized *nélkülöznöm* ("I must do without"); the writer omitted *l…lö*. This is an interpretation of a misspelled word, not a reading of hidden signs. (Alternative *ne küzdöm* is excluded: the sign after z is two short strokes n, not d.)
3. **Row 5 `de hig higgyje el`**: the first sign is a slash with a small separate tick at its upper right. That arrangement is closer to the h/p sign (stroke + tick on the right, as in *hogy*, *hostais*) than to the d of row 6 *édesem* (tick on the left). It is read as d **from context**, not from a clean sign match: *de* is the only reading that gives sense. Then *hig* is written and immediately restarted as *higgyje* (dittography). Normalized *De higgye el* ("but believe me"); the literal *higgyje* has a superfluous j, dropped in normalization. The earlier alternative *ne így hagyja el* is excluded by the signs.
4. **Row 18 `men{|}enni`**: the row reads *m e n*, an isolated single stroke, then *e n n i*. The writer repeated *-en-* with a false start between the repeats: literal (stroke ignored) *el-menenni*. Normalization *elmenni* (with *el* at the end of row 17) therefore deletes both the stray stroke and the repeated *en*. The sign before *e leküzdöttem* is a single slash, read as the reduced d of row 5/6 → *de leküzdöttem*.
5. **Row 21**: the sign before *og* is a cross, but **tilted**: its shape lies between the upright f-cross (*fel* just before it, *fajdalmam* row 19) and the diagonal u-cross (*úgy*, row 6). It is read as f **from context** (*fel fog jönni*, "will come up"); u would give no word. The ö of *jönni* shows no visible dots and is supplied in normalization.
6. **Row 9**: `egessegese` = *egésséges-e* (the earlier ledger missed the final -e); `allig` has a doubled wave (l), normalized *alig*.
7. Other writer spellings normalized: *ojan* → olyan, *nezemre* → nehezemre (h omitted), *mer* → mer[t], *erement | temojan* → erre mentem, olyan (the t at the row break is deleted), *mellet* → mellett, *akor* → akkor, *kel* → kell, *egessegese* → egészséges-e (z of *-ész-* omitted by the writer), *higgyje* → higgye (j dropped), *hostais* → posta is (h/p near-homograph). Accents (á, é, í, ó, ú) are mostly invisible at this scan resolution and are supplied.
8. **Right-edge corner**: *viszont* ends at the bottom-right corner and *látásra* runs up the right edge (rotated); the t at the corner is a single curved stroke at reduced visibility.
9. The sender is "Feri" (signature under the stamp); no identification with other cards' senders is claimed. Rákospalota cancellation and Jászárokszállás address agree with the family's other cards; the date is not legible on the card.

## Why it is correct

- The same key, transferred unchanged from five reviewed/finished cards of the family, turns every sign of all 23 main rows and the 6 stamp rows into Hungarian; no sign is left without a value except one stray stroke (item 4).
- The text is coherent, idiomatic early-20th-century Hungarian love-letter prose with formal *Ön* address (*ír, higgye el, van*), and its details fit the context: Sándor also appears on HCP1217, Vámosgyörk is a railway junction on the Budapest–Hatvan–Miskolc line near the addressee's region, and the closing formulas (*Isten vele, a viszontlátásra; csókolom számtalanszor; sírig hű kedvese*) are typical of the family.
- Repeated words decode identically at different places (*hogy* ×6, *viszontlát-* ×3, *nem* ×4).

## Response to review 1

Review 1 (Claude Opus 5.5, 2026-10-30) gave verdict **ACCEPT** with five minor findings. None changes the plaintext or the translation; all are disclosure points. Responses (Claude Opus 5.5, 2026-10-30):

1. **Row 21, f of *fog* (minor) — accepted, fixed in Uncertainties item 5.** Rechecked on `review/work/r21_fog.png` and `r21_full.png`: the sign before *og* is indeed a tilted cross, unlike the clean upright `+` of *fel* in the same row. Item 5 now says that f is a contextual choice on an ambiguous shape. The ledger token stays `+` (the chosen value); the reading is unchanged.
2. **Row 5, d of *de* (minor) — accepted, fixed in item 3.** The tick sits at the upper right, as on the h/p sign, not on the left as on the d of *édesem*. Item 3 now presents *de* as contextual.
3. **Row 18, *elmenni* (minor) — accepted, fixed in item 4.** Item 4 now states that the normalization deletes a repeated *-en-* as well as the stray stroke (literal *el-menenni*).
4. **Incomplete list of normalizations (minor) — accepted, fixed in items 3 and 7.** Added *kel* → kell, *egessegese* → egészséges-e (z omitted), *higgyje* → higgye (j dropped), and the deleted t at the row break in *erement | temojan*.
5. **Diacritics marked but not seen (minor) — partly disagree, ledger header clarified.** The ledger does **not** mark a diaeresis on *jönni* in row 21: its row 21 tokens are `... J O N N I`, and the literal output of the command prints *jonni*; the ö there is supplied only in the normalization (now said explicitly in item 5). For the ö of *neküznöm* (row 4) I agree with the reviewer that only one dot is seen on `review/work/row4c.png`; the ledger convention `:diaeresis` means "a dot mark is seen over the sign" (one or two dots), and the ledger header now says so, and names this sign. No token changed.

Re-ran `python3 -I ciphers/hcp-1216/work/decode_opus.py` after the edits: both hash checks print OK and the literal rows and normalized text are unchanged (the only edited work file is a comment line of the ledger).
