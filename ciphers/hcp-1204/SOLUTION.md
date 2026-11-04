# HCP1204 — Jolánka to Feri (Holecz Ferenc): the gossip of "Magyarné"

**Status: PARTIAL. Not handed over (no DONE marker).** All ciphertext is transcribed and the key is established, and most of the card reads as coherent Hungarian, but four points stay open at once (a word in row 15, a word in the stamp block, the sense of the opening of row 25, and the place of row 26). The batch standard allows only one lone un-understood word, so this is not claimed as complete. By Claude Opus 5.5, 2026-11-02. No earlier work existed on this number; no published solution was found or used. Portal: Not solved, no transcription or solution attached.

## Cipher type and key

Hungarian, monoalphabetic substitution with invented graphic signs: the Jolánka family key (HCP1216 and sisters), here written by Jolánka herself (plain sender line at the top: Feladó Tóth Jolánka, Jászárokszállás). The key transfers, with these card-specific findings:

- two bars a; three bars e; three strokes m; two strokes n; F-sign r; gamma t; wave l; 6 b; tall+short h/p (one sign, as in the family); low-bar cross j; loop with curl o (dots ö/ő); loop without curl i (dot i/í); long+short parallel d; hook k; "1"-hook v; right bowl s; right bowl + crossed sign sz; upright cross f.
- **Differs from the HCP1216 table:** the left bowl (e-shaped) is **g** here (lapját *meg*, *alig*, *igaz*, *leg-*). The S-loop descender is gy (hogy, nagyon); after n/g/t it is only the y of ny/gy/ty.
- bowl joined to "1"-hook = cs (*csak*); the same joined sign gives c in *percig*.
- One crossed sign carries u and z (*tudja, úgy* / *azt, kérdezem*); the family's tail difference is not kept consistently, so the ledger sets the value by word (tokens Xu/Xz). This is a disclosed word-sense call.

**Type note (2026-11-03, Claude Opus 5.5):** the stamp is lifted and the stamp box holds nine rows of the same cipher (see "Stamp-box message" below), so the card type is **MASC + Steganography**. The card stays PARTIAL; it has no register entry and none is created.

## Reproduction

```sh
python3 -I ciphers/hcp-1204/work/decode.py
```

Checks hashes, decodes `work/ledger.txt` (manual sign ledger from enlarged crops, `work/crops/`), prints literal rows and `work/normalized.txt`.

## Hungarian (normalized; [ ] = open)

Édes Ferikém, édes egyetlen reményem! Lapját megkaptam, amit köszönök. Alig vártam már lapját. Már azt hittem, hogy tényleg igaz, amit a Magyarné pletykált. De nem írom meg, miket beszélt, csak majd szóval elmondom. De most már látom, hogy a legnagyobb ellenségeim közé számíthatom a Magyarnét. Hogy mi öröme telne benne, ha mi nem volnánk jóba, aszt nem [tudom], de hogy nagyon rajta van, hogy csak össze tudna veszíteni magával, azt a beszédeiből kiveszem. Drága életem, most meg csak azt kérdezem magától: hogy írtam a [? "agazjásnak"], mert ebből ered az egész, ha írt úgy; mer maga tudja, hogy miféle beszéd. De én mer nem hallgatok az itteni pletykákra, mert ha arra hallgatok, úgy én mindenkivel haragba lehetek. És megszeretném tudni, édesem, hogy mikor láthatom viszont; talán, mint az előbbi levelembe írtam, így tehetne, nagyon boldog lennék már ma, ha láthatnám csak öt percig is. [Amiért ama hetén így, ellenbe] se vegye legalább, hogy olyan idegen levelet írtam [vál…], édesem. Részemről a boldog viszontlátásra, szerető hű kedvese üdvözli a távolból Jolánka.

Bottom-left line: mert az előtt beszélt.

## English (working)

My sweet Feri, my sweet only hope! I received your card, for which I thank you. I could hardly wait for your card. I already thought that what Mrs Magyar gossiped was really true. But I will not write what she said; I will tell you by word of mouth. But now I see that I can count Mrs Magyar among my greatest enemies. What pleasure she would take in our not being on good terms, that I do not [know], but that she is very much bent on setting me at odds with you, that I gather from her talk. My dear life, now I only ask you: how I wrote to [?], because the whole thing comes from this, if she wrote so; for you know yourself what sort of talk it is. But I no longer listen to the gossip here, because if I listened to that I could be on bad terms with everyone. And I should like to know, darling, when I can see you again; perhaps, as I wrote in my earlier letter, you could do it so; I would be very happy even today if I could see you for just five minutes. [Sense uncertain:] at least do not take to heart that I wrote such a strange letter [?], darling. For my part, until a happy reunion; your loving, faithful sweetheart greets you from afar, Jolánka. Bottom line: because she spoke before.

## Slovak (pracovný)

Môj sladký Ferko, moja sladká jediná nádej! Váš lístok som dostala, za čo ďakujem. Sotva som sa ho dočkala. Už som si myslela, že je naozaj pravda, čo klebetila Magyarová. Ale nenapíšem, čo hovorila, poviem to až ústne. Teraz však vidím, že Magyarovú môžem počítať k svojim najväčším nepriateľom. Akú radosť by mala z toho, keby sme neboli zadobre, to [neviem], ale že veľmi usiluje, aby ma s Vami pohnevala, to z jej rečí vyrozumievam. Drahý môj život, teraz sa Vás pýtam len: ako som napísala [?], lebo z toho pochádza všetko, ak napísala tak; veď sám viete, aké sú to reči. Ale ja už nepočúvam tunajšie klebety, lebo keby som na ne dala, mohla by som byť pohnevaná so všetkými. A chcela by som vedieť, drahý, kedy Vás znova uvidím; možno, ako som napísala v predošlom liste, by ste to tak mohli urobiť; bola by som veľmi šťastná už dnes, keby som Vás mohla vidieť čo len na päť minút. [Zmysel neistý:] aspoň si neberte k srdcu, že som napísala taký cudzí list [?], drahý. Z mojej strany do šťastného videnia, milujúca verná milá Vás pozdravuje z diaľky, Jolánka. Spodný riadok: lebo predtým hovorila.

## Open points (why this is partial)

1. **Row 15:** after *írtam* the signs read a g a a g z j á s n a k. Probably a name in the dative with a false start; not identified.
2. **Row 25 opening:** signs read a m í r t a m a h e t é n, then a sign (short stroke tied to a cross), í gy, e l e n b e. *Amiért ama hetén így, ellenbe* is a parse, not a secure reading: the triangular i of *amirt*, the tied sign, and the division are all doubtful. *Se vegye legalább, hogy olyan idegen levelet írtam* is secure in letters, though *vegye* rests on faint signs at the card edge (gy light) and the sense wants a missing phrase such as "to heart".
3. **Stamp row 1:** the stamp area is smeared. *írtem* is read with first signs damaged; after *v á l* about four signs are unreadable (*válasz* fits but is not read). The accent and d e s of *édesem* are visible, its second e is taken across the row break with the left end smeared.
4. **Row 26** sits under row 25 at the bottom left edge and breaks off at x about 957; its place in the text is uncertain, it may be an afterthought. The e of *beszélt* shows two bars only, cut by the edge.
5. **Row 10:** the sign before *u t o m* is a cross with a bar to the right, literally f or j; *tudom* is the sense, not a sign match.

Smaller disclosed points: hidden or smeared signs restored ({x} in the ledger): a of *igaz* (row 4 blot), a of *maga* (row 17), m of *mikor* (row 22, blotted first strokes), a of *az* (row 23), a of *ha* (row 24, blot), v of *levelet* (row 25, blot), e of *beszélt*, r of *-ről*, v, h, ü at the smeared stamp left edge. Row 24 ends *percigi*: the s of *is* is not seen. Row 22 *láthatom* is followed by an extra stroke tied into the v. Row 24 start: *ma* is stacked at the left margin. Writer's spelling kept: *hallgatok* written *halgatok* and *helgatok*, *aszt*, *mer*, *Mogyarné* (o for a, normalized Magyarné), *lenék*, *tehetne(n)*, *láthatnén*, *írtem*.

## Stamp-box message (2026-11-03)

Audit by Claude Opus 5.5 of the original scan (work/hires/*_adr.jpg; crops in work/stamp-2026-11-03/: box.png 1.5x, top.png and bot.png 3x, row1_red4x.png red channel 4x). The stamp has been lifted; the bare paper inside the red dashed stamp frame (top right) carries **nine rows in the cipher signs**, no plain Hungarian. A grey postmark arc runs over the top row. The rows were already in the ledger (S1-S9) and decoded by `work/decode.py` (re-run 2026-11-03, unchanged, still passes); this audit re-checked every row by eye against the crops and agrees with the ledger. The stamp text continues the last main-text sentence (row 25 ends *…olyan idegen levelet*).

Literal (ledger; {x} = sign restored at the smeared left edge, [..] = unread):

```
S1 {í}rtem vál[..] éde      S2 s{e}m részem       S3 {r}ől a boldig
S4 {v}íszontlátás           S5 ra szerető         S6 {h}ű kedvese
S7 {ü}dvözli a              S8 távolból           S9 Jolánka
```

Normalized Hungarian: *[…levelet] írtam vál[…], édesem. Részemről a boldog viszontlátásra, szerető hű kedvese üdvözli a távolból Jolánka.*

English: *[…that I wrote such a strange letter] [?], darling. For my part, until a happy reunion; your loving, faithful sweetheart greets you from afar, Jolánka.*

Slovak: *[…že som napísala taký cudzí list] [?], drahý. Z mojej strany do šťastného videnia, milujúca verná milá Vás pozdravuje z diaľky, Jolánka.*

Stays unread: in S1, after *v á l*, two to four signs are smeared under the old stamp gum and the postmark (red-channel crop shows only a wave and blurred bars); *válasz* would fit but is not read. This leaves the word, not a whole clause, open. Restored signs: í (S1), e (S2), r (S3), v (S4), h (S6), ü (S7) at the smeared left edge, each the only letter that makes the word. Writer's forms kept: *írtem*, *boldig*, *víszontlátás*.

## Plain text on the card

Top edge, unenciphered: Feladó Tóth Jolánka, Jászárokszállás. Address: Tek. Holecz Ferencz úrnak, M.Á.V. fékező, Iskola utca 34, Rákos Palota Újfalu. Picture side, printed: Szerelem törvénye 5. § Csókolni nem bűn, engem! The date in the postmark is not legible.

## Why the readable part is correct

The family key, with one changed sign value, gives long stretches of idiomatic Hungarian with no fitting: *pletykált/pletykákra* twice, *Magyarné* twice, *beszédeiből kiveszem, haragba lehetek, csak öt percig is*, and the formula *szerető hű kedvese üdvözli a távolból Jolánka*. The persons fit the family: Feri writing to Jolánka on HCP1216, here her reply to him.
