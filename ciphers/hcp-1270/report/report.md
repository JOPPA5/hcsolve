# HCP 1270 (jolanka-72): Feri to Jolánka Tóth, an army medical review and a possible farewell

Human solver: Tomáš Pavuk

**Status: partial. The whole card is transcribed and all of it reads as connected Hungarian except the last clause of row 30, which is not understood. Independent review 1 verdict REVISE, findings addressed, no letter of the decipherment changed. No register entry is submitted.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1270 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1270), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-72, from Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language unknown, recipient Tóth Jolánka, with no date, transcription or solution.

The picture side is a tinted photograph of a violinist playing to a young woman, with a printed gold caption in plain Hungarian: *Ezüsttükrös kávéházban ....* and the verse *Gyere cigány, gyere, néked / Elmondok egy bús emléket / Csendesen ....* ("In the silver-mirrored coffee house ... Come, gypsy, come, to you I will tell a sad memory, quietly ..."). It holds no cipher.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address is in plain writing: *Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás*. A rectangular Újpest postmark stands beside the stamp position; no date can be read. The stamp was torn off and took ink with it. The cipher text is in green ink: 24 rows in the left panel, 6 rows across the whole card below the address, and 8 short rows in the stamp square.

![Address side: the cipher panel at left and along the bottom, the stamp square at top right (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the family of cipher cards from Feri to Jolánka Tóth, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). The signature Feri, the closing formula and the addressee all match. This was a read with a **known, transferred key**, not a new key recovery. No published reading of this card was found or used.

## Method

The key comes unchanged from the family, as set out in HCP 1216. No earlier work exists on this number. Claude Opus 5.5 read all rows from 2x to 3x enlargements of the un-converted address scan and recorded every written sign in a ledger (848 tokens; `work/ledger.txt`). The ledger is manual; no OCR was used. A small script checks the SHA-256 of the images and decodes the ledger. Words broken across rows helped confirm the row order, for example *felül|vizsgálatakor* (rows 16–17), *kö|nyen* (26–27) and *a | sor* (27–28).

The literal decipherment below keeps the writer's spelling. The normalized Hungarian is editorial: he drops double consonants, and acute accents and many dots cannot be seen, so they are supplied.

## Key

Hungarian simple monoalphabetic substitution with invented signs. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma / corner | t |
| long stroke + short tick | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short tick | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | opposed bowls or closed ring | cs | | |

One sign serves for both h and p. Dots over o and u give ö and ü. On this card *gy* and *ny* are written with two signs each, g+y and n+y. *sz* is written s+z.

## Plaintext

Literal decipherment, one row per written line. `h` stands for the h/p sign and `[x]` marks a damaged sign whose value is a restoration.

```text
01 szeretetedesjolankamkecsesso           16 vahanemsikerülafelül
02 raitmegkahtammelyetköszö               17 viszgalatakorlegjobb
03 nökszehenamisorailetoen                18 ba[n]leszhaelbucsuzunkegy
04 rögtönvalaszoltamigaz                  19 mastolesenmajdbucsut
05 hogynahigutazotezalah                  20 mondokmindennekesugy
06 azsebembeedesemsajnalato               21 eltünö[k]hogyhiremsem
07 matkelkifejeznemhogyo                  22 haljasenkimertakormar
08 janrosszulvegzödötamulat               23 latomazthogyüldözaba[l]
09 sagedesemhakesikavalaszom              24 sorseshaenekemnincssze
10 aztcsakelfoglaltsagomnak
11 tuladonitsahalaisten
12 nakezidöszerintnincs
13 semmibajomamiazorvo
14 sivizitetiletimegnem
15 voltamöszintenmegval
25 rencsemnemteszemszerencsetlennemagatisbiztatoszavam
26 melmegmagaboldoglehetmasferfimeletismertanöiszivkö
27 nyenfe[l]ejtdeazthagyjukutoljaratalanerrenemkerüla
28 sorkedvesemamia[m]enetelemetiletiugyaladolognagyonsze
29 retnekmennihogylathassamdeaztartviszahogynincsked
30 vemrevaloruhamsohamostvazazoltonyamitmabistud
stamp: [cs]okol [j]as[z][a]m talan szor s[z]ere [t]oked vesse feri
```

### Hungarian (normalized)

Szeretett édes Jolánkám! Kecses sorait megkaptam, melyet köszönök szépen. Ami sorai[t] [i]lletően, rögtön válaszoltam, igaz, hogy napig utazott ez a lap a zsebembe. Édesem, sajnálatomat kell kifejeznem, hogy olyan rosszul végződött a mulatság. Édesem, ha késik a válaszom, azt csak elfoglaltságomnak tulajdonítsa. Hála Istennek, ez idő szerint nincs semmi bajom. Ami az orvosi vizitet illeti, még nem voltam. Őszintén megvallva, ha nem sikerül a felülvizsgálatakor, legjobban lesz, ha elbúcsúzunk egymástól, és én majd búcsút mondok mindennek, és úgy eltűnök, hogy hírem sem hallja senki, mert akkor már látom azt, hogy üldöz a balsors, és ha énnekem nincs szerencsém, nem teszem szerencsétlenné magát is. Biztató szavam mel[?] még maga boldog lehet más férfi mellett is, mert a női szív könnyen felejt. De azt hagyjuk utoljára, talán erre nem kerül a sor. Kedvesem, ami a menetelemet illeti, úgy áll a dolog, nagyon szeretnék menni, hogy láthassam, de az tart vissza, hogy nincs kedvemre való ruhám, ⟨clause unread: `sohamostvazazoltonyamitmabistud`⟩.

Under the stamp: [Cs]ókol[j]a s[zá]mtalanszor s[z]ere[t]ő kedvese Feri.

### English

My beloved sweet Jolánka! I received your graceful lines, for which I thank you kindly. As for your lines, I answered at once, though it is true this card travelled in my pocket for some days (literally *napig*, "for a day" or "up to the day"; a number may be understood). My darling, I must express my regret that the party ended so badly. My darling, if my answer is late, put it down only to my being busy. Thank God, at present nothing is wrong with me. As for the medical inspection, I have not been yet. To be frank, if it does not go well at the review board, it will be best if we say goodbye to each other, and I will then say farewell to everything and vanish so that no one hears of me, for then I will see that ill fortune pursues me; and if I have no luck, I will not make you unhappy too. My word of comfort [`mel`, unresolved]: you can still be happy with another man as well, for a woman's heart forgets easily. But let us leave that for last; perhaps it will not come to that. My dear, as for my going there, things stand like this: I would very much like to go so that I can see you, but what holds me back is that I have no clothes to my liking, ... [last clause unread; only the fragments *most* "now", *az öltöny* "the suit", *amit* "which" are firm].

Under the stamp (partly restored): Kisses you countless times, your loving sweetheart, Feri.

### Slovak

Moja milovaná, sladká Jolánka! Vaše pôvabné riadky som dostal, za čo pekne ďakujem. Čo sa týka Vašich riadkov, odpovedal som hneď, pravda, že tento lístok cestoval niekoľko dní v mojom vrecku (doslova *napig*, „jeden deň“ alebo „do dňa“; možno sa rozumie počet). Drahá, musím vyjadriť ľútosť, že sa zábava skončila tak zle. Drahá, ak moja odpoveď mešká, pripíšte to iba mojej zaneprázdnenosti. Vďaka Bohu, toho času mi nič nie je. Čo sa týka lekárskej prehliadky, ešte som tam nebol. Úprimne povedané, ak sa to na superrevízii nepodarí, najlepšie bude, ak sa rozlúčime, a ja potom dám zbohom všetkému a zmiznem tak, že o mne nikto nebude počuť, lebo vtedy už uvidím, že ma prenasleduje nešťastie; a ak nemám šťastie, neurobím nešťastnou aj Vás. Moje povzbudivé slovo [`mel`, nevyriešené]: Vy ešte môžete byť šťastná aj s iným mužom, lebo ženské srdce ľahko zabúda. Ale to nechajme nakoniec, azda k tomu nedôjde. Drahá, čo sa týka môjho odchodu, je to tak: veľmi by som chcel ísť, aby som Vás videl, ale to ma zdržiava, že nemám šaty podľa svojej chuti, ... [posledná veta neprečítaná; isté sú len zlomky *most* „teraz“, *az öltöny* „ten oblek“, *amit* „ktorý“].

Pod známkou (čiastočne doplnené): Bozkáva Vás nespočetnekrát Váš milujúci milý, Feri.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1270/work/decode.py
```

The command checks the SHA-256 of the four image files, decodes `work/ledger.txt` (848 tokens) and prints the literal rows and the normalized text.

## Uncertainties

1. **Row 30, last clause: unread.** Every sign of `sohamostvazazoltonyamitmabistud` is legible, but only *most*, *az öltöny* and *amit* are firm. An earlier conjecture, *soha most va[n] az öltöny, amit ma[ga] is tud[ja]* ("never now, there is the suit that you too know"), needs three changes against the signs, still lacks syntax, and is withdrawn. Other segmentations tried also gave no sentence: `v azaz`, `sopa`, `-tun`, *bő* for `bi`, and *vez* (the first a of `vaz` has a small extra tick between its bars). The clause runs into the corner of the card. No Hungarian speaker has checked it.
2. **Row 26 `mel`.** Clear signs, literally *mel*. *Mert* would need two letters not on the card, and the writer spells *mert* correctly elsewhere, so the word stays unresolved. It may be a stray word or *mel[y]* ("which") with y dropped. The sense of the sentence does not depend on it.
3. **Blotted signs.** `ba[n]` (row 18), `eltünö[k]` (row 21), `ba[l]` in *balsors* (row 23) and `fe[l]ejt` (row 27) rest on word sense. In `a[m]enetelemet` (row 28) three overinked strokes are visible.
4. **Row 3.** Literal `amisorailetoen`: the normalized *sorai[t] [i]lletően* adds a t and an i not on the card.
5. **Near-homographs.** The h/p calls (*kaptam, szépen, napig, lap* against *hogy, ha, hála, lehet, hírem*), the d/n calls (*idő, mondok, üldöz, végződött, dolog*) and the k/g calls (row 24 *enekem*, row 16 *sikerül*) rest on word sense. *lap* in row 5 has a false start before it. The sign after *de* in row 29 lies between a and s; read *az tart* by sense. Row 7 ends with a blotted cross taken as a cancelled j.
6. **Stamp rows.** Largely damaged. *Csókolja számtalanszor szerető kedvese Feri* is the family closing and fits what survives, but much of S2 is restoration, its first sign is only a broken angle, and S1 has more faint residue at its right end.
7. **Date and sender.** Nothing on the card gives a date. The *felülvizsgálat* (medical review) suggests military service. A link with the First World War is an inference only: sister card HCP 1272 has 1912-04-30 in its portal name, so a peacetime call-up is equally possible.

## Review summary

A separate Claude Opus 5.5 agent reviewed the work. It re-ran the command, wrote its own decoder with its own token map, read every row sign by sign on its own 2x to 4x crops, and found no misread sign that changes a word. Its verdict was **REVISE**, with one major and six minor findings:

- The last clause of row 30 is unread, so the card must be labelled partial. Accepted; further attempts failed, and the conjecture and continuous translation of the clause were removed.
- `Mer[t]` in row 26 hid an emendation against a clear sign. It is now shown as unresolved, and *biztató szavam* opens the next sentence.
- The row 3 normalization, the sense of *napig*, the k/g near-homography and the restored stamp letters were disclosed or bracketed.
- Wrong counts in the argument for correctness were fixed (*hogy* 6 times; `ilet-` 3 times).

No sign, key value or ledger entry changed. The changes concern the normalized text, the translations and the disclosures.

## Credits

- **Claude Opus 5.5, 2026-11-01:** key transfer, transcription, decipherment, response to review and this report.
- **Claude Opus 5.5, separate reviewer agent:** independent review.
- The family key was captured and transferred on earlier cards by the OpenAI GPT solver and completed there by Claude Opus 5.5.

## Sources

- HC Portal record 1270, General, Description and Attachments tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1270 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3870/conversions/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-72_pic-large.jpg (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/3871/conversions/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-72_adr-large.jpg (source/address-large.jpg).
- Family key: ciphers/hcp-1216/SOLUTION.md.
