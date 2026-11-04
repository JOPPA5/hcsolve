# HCP1265 — Feri to Jolánka Tóth: clothes, Berény or Árokszállás, Haraszti, take care of yourself

**Status: complete reading, corrected after review 1 (verdict REVISE).** Solver: Claude Opus 5.5, 2026-11-01. One word (*kedel*, row 25) is read sign by sign but not understood; all other points are listed below.

Credit: there is no earlier work on this number. The key was transferred from finished sister cards (HCP1216 and family; earlier work there by OpenAI GPT-6 Astra / GPT-6.1 Sol and Claude Opus 5.5). The portal shows status *Not solved* with no transcription or solution attached, and no published solution of this card was found. Sister cards were used for the key, and for the place names Haraszti (HCP1305) and Berény and the name Ilonka (HCP1263, 1272); no plaintext was copied from them.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the "Jolánka" family, same key as HCP1216, 1212, 1213, 1217, 1218, 1243, 1301), plus a plain-text address. The key was not changed for this card:

Type note (2026-11-03): the card carries a hidden message in the stamp box, written in the cipher signs under the (now lifted) stamp, so the register type is **MASC + Steganography**.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| short tick + long stroke | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short tick | h / p | wavy-top loop with descender | y |
| zig-zag hook | g | loop with dot | i | crossed diagonal | z |
| inverted T | j | | | | |

On this card g and y are always two signs (*hogy* = h o g y). Ticks over the loop give ö/ő. Acute accents are sparse and are supplied in normalization.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1265/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (597 written signs in 26 main rows plus 8 rows in the stamp box) and prints the literal rows, then `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the un-converted scan (`work/crops/`), not OCR. Word division is editorial.

## Literal decipherment

```
01 szeretetedesjolankam             14 semitszamitaniazjo
02 kivanomhogyalegjobb              15 hogykimentharaszti
03 kedvebentalaljasoraim            16 ralegalabszivjaezt
04 tudatomhogymairtamaz             17 ajotanyailevegot
05 ilonkanakmegigertem              18 barigazhogyaroksza
06 hogymajdanyeronvagy              19 lasbasenincsroszleve
07 arokszalasbavagybe               20 gősidekivelminden
08 renybemostazontöre               21 naptalalkokmertegy
09 kedekhogyegykicskiru             22 hejrejarunkebedelni
10 hazkodhasakhogynezzek            23 őmondtahogynagyonjolnezkijolankamcsakvi
11 kivalahogydeezthagy              24 gyazonmagaradragacsilagomnehogymegfaz
12 jukmertezistenrelese             25 onakedelnemsokattörődökugyanilonanakvigye
13 azegesznemjoelöre                26 lenemtudomhogyintezkednek

Stamp box: istenve | le[deleted] | dragamcso | kolom | szamta | lanszo | imadoja | feri
```

Rows 23 to 26 run on under the address to the right edge of the card.

Plain text on the card: *Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás* (written *Szepremenyü*; "To the Young Lady of Fair Hopes, Jolánka Tóth"). Picture side: printed verse, no cipher. The postmark date is not legible (a large 17 is seen, without month or year).

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Tudatom, hogy ma írtam az Ilonkának, megígértem, hogy majd a nyáron vagy Árokszállásba vagy Berénybe [elmegyek]. Most azon törekedek, hogy egy kics[it] kiruházkodhassak, hogy nézzek ki valahogy. De ezt hagyjuk, mert ez Isten re[nde]lése, az egész; nem jó előre semmit számítani. Az jó, hogy kiment Harasztira, legalább szívja ezt a jó tanyai levegőt, bár igaz, hogy Árokszállásba[n] se[m] nincs rossz levegő. S Ide [név, bizonytalan; Ida?], kivel minden nap találk[oz]ok, mert egy helyre járunk ebédelni, ő mondta, hogy nagyon jól néz ki, Jolánkám. Csak vigyázzon magára, drága csillagom, nehogy megfázzon. A kedel [?] nem sokat törődök ugyan, Ilonának vigye le, nem tudom, hogy intézkednek.

In the stamp box: Isten vele, [deleted] drágám! Csókolom számtalanszo[r]. Imádója, Feri.

## English

My beloved sweet Jolánka! I wish that my lines find you in the best of moods. I let you know that today I wrote to Ilonka; I promised that in the summer I would [go] either to Árokszállás or to Berény. Just now I am striving to clothe myself a little, so that I may look like something. But let us leave that, for this is God's [ordinance], all of it; it is not good to count on anything in advance. It is good that you went out to Haraszti; at least you are breathing that good farmstead air, though it is true that the air is not bad in Árokszállás either. And Ide [name unsure; Ida?], whom I meet every day because we go to the same place for lunch, told me that you look very well, my Jolánka. Only take care of yourself, dear star of mine, so that you do not catch cold. With the *kedel* [unread word] I do not concern myself much, it is true; take [it] down to Ilona, I do not know how they are arranging things.

In the stamp box: Farewell, [deleted] my dear! I kiss you countless times. Your adorer, Feri.

## Slovak

Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Oznamujem Vám, že dnes som písal Ilonke; sľúbil som, že v lete [pôjdem] buď do Árokszállása, alebo do Berénya. Teraz sa snažím trochu sa oblečiť, aby som aspoň nejako vyzeral. Ale nechajme to, lebo toto je Božie [riadenie], celé to; nie je dobré dopredu s ničím rátať. To je dobre, že ste išli do Harasztiho; aspoň dýchate ten dobrý vzduch zo salaša, hoci pravda, ani v Árokszállási nie je zlý vzduch. A Ide [meno neisté; Ida?], s ktorou sa každý deň stretávam, lebo chodíme obedovať na to isté miesto, povedala, že vyzeráte veľmi dobre, moja Jolánka. Len si dávajte pozor, drahá hviezdička moja, aby ste neprechladli. S *kedel* [neprečítané slovo] sa síce veľmi nezaoberám; zaneste [to] dole Ilone, neviem, ako to zariaďujú.

V rámiku na známku: S Bohom, [prečiarknuté] moja drahá! Bozkávam Vás nespočetnekrát. Váš ctiteľ, Feri.

## Uncertainties

Writer's habits (dropped and doubled letters) are as on sister cards. Every sign is transcribed as written, and the normalization is editorial.

1. **Row 25 `akedelnem`, the main open point.** All signs are clear (a k e d e l, then *nem*), and the first e carries a tick. The word is left unread in the normalized text and the translations. Two guesses, neither adopted: *kedél* (kedély "mood"), against which this writer spells ly as j (*hejre* here, *kedéjes* on HCP1212) and which lacks the instrumental that *törődik* needs; and *keddel* (kedd + -del, "with Tuesday"), which has that case ending and fits this writer's single consonants (*keden* for kedden on HCP1307), but nothing on the card mentions a Tuesday and the tick over the e is not explained. The rest of the clause (*nem sokat törődök ugyan*) reads.
2. **Rows 25–26 `ilonanakvigye | le`** (corrected in review 1; DONE1 had `ilonanesvigye`). The two signs after *Ilon-a-n* lie under the portal stamp's letters OF. With the stamp removed they are a (two bars, clean paper above and below) and a full section mark k (top arm and left foot): *Ilonának vigye le*, with a tick over the first a of the ending. No restoration is needed. *Vigye* is third person, so it is either formal "you" (Jolánka, as in *vigyázzon*) or a third person who is not named. What is to be taken down is not stated. It might be connected with the unread *kedel*.
3. **Row 20 `sidekivel`.** The sign after *i* is heavily retraced: a long stroke with a blotted head, then a shorter stroke to its right. This is the reverse of this card's d (short, then long; `kedel`, `kedek`), so the sign class itself is unsure, and it may be a correction over another sign. It is closer to h/p or a retraced n, so *Ide / Ihe / Ipe / Ine* are all candidates; d is provisional. Three clear bars follow, overlapping the row above. That a person is named here is inferred only from *ő mondta*. *Ida* would need two bars; the sign shows three. The name is reported literally, with [Ida?] as a suggestion, and no such person appears on sister cards.
4. **Row 21 `naptalalkok`.** The fourth sign is blotted and crossed, between F (r) and the corner (t), so t rests on word sense; r would give *ralalkok*. The h/p before it is blotted. *találkok* is taken as *találkozok*.
5. **Row 10 `nezzek`.** The first sign has the d shape (short tick + long stroke); it is read n by word sense, as d/n are near each other in this family (*dezzek* is no word).
6. **Row 12 `relese`.** *Isten rendelése* needs *-nd-* supplied, so the sense "God's ordinance" rests on a restoration and is bracketed in the translations. The e after r is heavily retraced, and something could be hidden beneath it, but the visible sign is a single three-bar sign.
7. **Row 16 `ezt`.** The e is blotted or retraced; the bars still show. Only *ezt* fits *ezt a jó tanyai levegőt*.
8. **Row 6 `nyeron`** has three bars with a tick, so the writer wrote *nyéron*, normalized *nyáron*. **Row 7** the k of *Árokszállás* has a ring head (seen only here); row 18 has the normal k in the same word.
9. **Row 6–7:** the verb after *Berénybe* is not written; [elmegyek] is supplied in the Hungarian and bracketed in the translations.
10. **Rows 24–26:** the d of *drága* and of *intézkednek* is under a blot, with the short tick still visible. Each is a restoration where only d makes the word. The same holds for *nap* (item 4); it does not hold for *Ide* (item 3), where no short first tick is seen.
11. **Stamp box.** S1: the bars of *Isten* are unusual (the corner's arm is detached, the e shows two bars), and the second stroke of n is under a blot. S2: the rest of the row is the writer's own heavy deletion, unreadable, and it is not reconstructed. S3: the first sign is 9-shaped and the third is overwritten; *drágám* is by word sense (the first sign could be compared with the ring-headed k of row 7, but *krágám* is no word). S4: the m of *csókolom* has a small third stroke. S5: s is a plain slash. S6: the s is an hourglass-shaped retraced sign; the r of *számtalanszor* is not written. S8: the f is a tilted cross and the r has no lower arm; *Feri* agrees with the sister cards.
12. Other spellings normalized: *szeretetedes* (szeretett édes), *legjobb* is written with double b, *kics* (kicsit), *hasak* (hassak), *semit* (semmit), *rosz* (rossz), *sokatt* (sokat), *csilagom* (csillagom), *megfazon* (megfázzon), *vigyazon* (vigyázzon), *Arokszalas* (Árokszállás), *hejre* (helyre, ly as j), *se nincs* (sem nincs).
13. *Haraszti* (row 15): the h/p sign could give *paraszti*; h is chosen because *Harasztin* is on HCP1305 as a place Jolánka visits, and *-ra* fits a place. *Berény* is on HCP1263 and 1272.
14. **Blots with no effect on the word.** Row 12: the u of *hagyjuk* is a heavily retraced cross; only *-juk* fits. Row 23: the a of the second *Jolánkám* has a blot on its lower bar; both bars still show.

## Why it is correct

- The key, unchanged from reviewed sister cards, turns all 597 signs into Hungarian; no sign class is left without a value.
- The opening *Kívánom, hogy a legjobb kedvében találja soraim* is the same formula as on HCP1305 and 1218, and it comes out without any adjustment. *Bár igaz* also occurs on HCP1283 and 1288, and *Isten vele* and *Feri* are the family's closing.
- The text runs on across line breaks with no forcing: *be|rénybe*, *töre|kedek*, *kiru|házkodhassak*, *hagy|juk*, *Haraszti|ra*, *Árokszá|lásba*, *leve|gő*, *vi|gyázon*, *megfáz|on*, *vigye|le*, *csó|kolom*, *szám|ta|lanszo*.
- Repeated words decode identically: *hogy* ×11 (with *nehogy*), *Jolánkám* ×2, *Árokszállás* ×2, *levegő* ×2, *jó* ×3, *nem* ×3.
- Names and places fit the family's context: cousin Ilonka, Berény, Haraszti, the addressee at Jászárokszállás, the writer Feri.

## Stamp-box message (2026-11-03)

Stamp-box audit, Claude Opus 5.5, 2026-11-03, ordered by the human. The stamp has been lifted; the box (printed dotted frame, upper right of the address side) holds eight short rows in the same red ink and the same cipher signs as the main text. No plain-Hungarian writing is in the box. The message was already read in full in the DONE1/FINAL version and is in `work/ledger.txt` (rows S1–S8), so `work/decode.py` already reproduces it; it was re-run today and still passes (597 signs in 34 rows). Fresh crops of the original at 3x: `work/stamp-2026-11-03/box_top_3x.png`, `box_bot_3x.png`, `overview.png`. The re-check found no sign to change.

- Literal: `istenve | le[deleted] | dragamcso | kolom | szamta | lanszo | imadoja | feri`
- Hungarian (normalized): Isten vele, [törölve] drágám! Csókolom számtalanszo[r]. Imádója, Feri.
- English: Farewell, [deleted] my dear! I kiss you countless times. Your adorer, Feri.
- Slovak: S Bohom, [prečiarknuté] moja drahá! Bozkávam Vás nespočetnekrát. Váš ctiteľ, Feri.

Unread: the rest of row S2 after *le* is the writer's own heavy deletion (solid ink smear) and cannot be read; nothing is reconstructed. The r of *számtalanszor* is not written. The other irregular signs are listed under Uncertainties, item 11.

## Response to review 1

Review verdict REVISE. I rechecked each finding on the reviewer's crops (review/work/crops/I25.png, Z25.png, Z20.png, Z12a.png). All four are accepted. After the changes `python3 -I ciphers/hcp-1265/work/decode.py` runs, all four hash checks print OK, and it gives 597 signs in 34 rows with the literal block above.

1. **Row 25 end (major): fixed.** Agreed. In the stamp-free ink map the sign I had as e has two bars and clean paper where a third would be. The sign I had as `)` has a top arm and a left foot, so it is k. Ledger, literal block, normalized.txt, Hungarian, English, Slovak and item 2 are changed to *Ilonának vigye le*. The supplied [i] and the "let Ilona not even take" translation are gone. Reconsidering the clause as a whole, I no longer print *kedél[lyel?]* or "mood": *kedel* stays unread, and item 1 gives the two guesses without adopting one. No other sign in the clause changes.
2. **Row 20 sign (minor): fixed.** Agreed. In Z20.png the long stroke comes first and the shorter second, the reverse of this card's d. The ledger token is now `D?` (provisional d, class unsure); item 3 lists *Ide / Ihe / Ipe / Ine* and says the name is inferred only from *ő mondta*; item 10 no longer groups this sign with the d's that show a tick. The literal letters do not change.
3. **HCP1263 citations (minor): fixed.** The opening formula is cited to HCP1305 and 1218, and *Bár igaz* to HCP1283 and 1288.
4. **Undisclosed blots and unmarked restoration (minor): fixed.** Row 12 u is token `X#`; rows 12 and 23 are in the new item 14; "God's [ordinance]" and "Božie [riadenie]" are bracketed and item 6 says the sense rests on the restoration.

The reading changes by the two signs of finding 1 and the translation of that clause; no further round is needed, as the review recommends. A direct re-read of row 25 under the stamp agrees with the reviewer.
