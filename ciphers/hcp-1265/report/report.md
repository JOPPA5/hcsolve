# HCP 1265 (cpc_--17_HU__HU_Jasz Arokszalas_jolanka-86): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: the whole card is read and every sign has a value; one word (kedel) is transcribed but not understood, and one name (Ide) rests on an unsure sign. Independent review 1 verdict REVISE; its findings are addressed here.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1265 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1265), portal name cpc_--17_HU__HU_Jasz Arokszalas_jolanka-86, from Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a tinted photographic card of a young man reading a letter, with a woman's portrait and a printed Hungarian verse headed Sokszor úgy szeretnék sírni…. It carries no cipher.

The address side has the plain address Szépreményű (written Szepremenyü) Tóth Jolánka úrleánynak, Jász Árokszállás: "To the Young Lady of Fair Hopes, Jolánka Tóth, Jászárokszállás". The postmark shows a large 17, with no legible month or year.

The card has 26 rows of cipher in red ink at the left and along the bottom. Rows rise to the right, and rows 23 to 26 run on under the address to the right edge, where the portal stamp overlies them. Eight more short rows fill the stamp box: they were hidden under the postage stamp (now lifted), a steganographic farewell in the same cipher signs (see Plaintext). A stamp-box audit on 2026-11-03 re-checked them on fresh crops and changed no sign.

The card belongs to the large "Jolánka" correspondence, in which a man called Feri writes to Jolánka Tóth in one invented-sign alphabet. The key was transferred from finished sister cards (HCP 1216 and others), so this is not a new key recovery. Earlier work on those cards was by OpenAI GPT-6 Astra / GPT-6.1 Sol and Claude Opus 5.5; there was no earlier work on this number. No plaintext was taken from sister cards, and no published solution of this card was found.

![Address side with the cipher rows, the stamp box and the plain address (source/address-large.jpg)](../source/address-large.jpg)

![Picture side with the printed verse; no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual. The solver read every row by eye from enlarged crops of the un-converted scan, and recorded 597 written signs in 34 rows (26 main rows plus 8 in the stamp box) in a sign ledger. No OCR was used. The family key was then applied without change. Word division, accents and the normalized spelling are editorial; the card has no word breaks.

The reviewer cropped the whole card again and made its own reading in a separate glyph alphabet, with the solver's ledger open, so this is a check rather than a blind second reading. For the rows under the portal stamp it computed a red-minus-green map, which removes the green stamp and leaves the red ink. That map exposed the one misreading in the first version (see Review summary).

## Key

Cipher type: **MASC + Steganography** (updated 2026-11-03). Simple monoalphabetic substitution with invented graphic signs, Hungarian plaintext; a second, hidden message is written in the same signs in the stamp box, under the stamp (now lifted). The labels below are conventional names for handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| short tick + long stroke | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short tick | h / p | wavy-top loop with descender | y |
| zig-zag hook | g | loop with dot | i | crossed diagonal | z |
| inverted T | j | | | | |

The same sign serves for h and p; the word decides between them. On this card g and y are always two signs (hogy = h o g y). Ticks over the loop give ö and ő. Acute accents are sparse and are supplied in the normalization.

## Plaintext

Literal decipherment, one group per written row:

```text
01 szeretetedesjolankam             14 semitszamitaniazjo
02 kivanomhogyalegjobb              15 hogykimentharaszti
03 kedvebentalaljasoraim            16 ralegalabszivjaezt
04 tudatomhogymairtamaz             17 ajotanyailevegot
05 ilonkanakmegigertem              18 barigazhogyaroksza
06 hogymajdanyeronvagy              19 lasbasenincsroszleve
07 arokszalasbavagybe               20 gősidekivelminden
08 renybemostazontöre               21 naptalalkokmertegy
09 kedekhogyegykicskiru             22 hejrejarunkebedelni
10 hazkodhasakhogynezzek            23 őmondtahogynagyonjolnezki-
11 kivalahogydeezthagy                 jolankamcsakvi
12 jukmertezistenrelese             24 gyazonmagaradragacsilagom-
13 azegesznemjoelöre                   nehogymegfaz
                                    25 onakedelnemsokattörődök-
                                       ugyanilonanakvigye
                                    26 lenemtudomhogyintezkednek

Stamp box: istenve | le[deleted] | dragamcso | kolom | szamta |
           lanszo | imadoja | feri
```

Rows 23 to 25 are one row each on the card; they are wrapped here only to fit the page.

Normalized Hungarian:

**Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Tudatom, hogy ma írtam az Ilonkának, megígértem, hogy majd a nyáron vagy Árokszállásba vagy Berénybe [elmegyek]. Most azon törekedek, hogy egy kics[it] kiruházkodhassak, hogy nézzek ki valahogy. De ezt hagyjuk, mert ez Isten re[nde]lése, az egész; nem jó előre semmit számítani. Az jó, hogy kiment Harasztira, legalább szívja ezt a jó tanyai levegőt, bár igaz, hogy Árokszállásba[n] se[m] nincs rossz levegő. S Ide [név, bizonytalan; Ida?], kivel minden nap találk[oz]ok, mert egy helyre járunk ebédelni, ő mondta, hogy nagyon jól néz ki, Jolánkám. Csak vigyázzon magára, drága csillagom, nehogy megfázzon. A kedel [?] nem sokat törődök ugyan, Ilonának vigye le, nem tudom, hogy intézkednek.**

**In the stamp box: Isten vele, [deleted] drágám! Csókolom számtalanszo[r]. Imádója, Feri.**

English translation: **My beloved sweet Jolánka! I wish that my lines find you in the best of moods. I let you know that today I wrote to Ilonka; I promised that in the summer I would [go] either to Árokszállás or to Berény. Just now I am striving to clothe myself a little, so that I may look like something. But let us leave that, for this is God's [ordinance], all of it; it is not good to count on anything in advance. It is good that you went out to Haraszti; at least you are breathing that good farmstead air, though it is true that the air is not bad in Árokszállás either. And Ide [name unsure; Ida?], whom I meet every day because we go to the same place for lunch, told me that you look very well, my Jolánka. Only take care of yourself, dear star of mine, so that you do not catch cold. With the kedel [unread word] I do not concern myself much, it is true; take [it] down to Ilona, I do not know how they are arranging things.**

**In the stamp box: Farewell, [deleted] my dear! I kiss you countless times. Your adorer, Feri.**

Slovak translation: **Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Oznamujem Vám, že dnes som písal Ilonke; sľúbil som, že v lete [pôjdem] buď do Árokszállása, alebo do Berénya. Teraz sa snažím trochu sa oblečiť, aby som aspoň nejako vyzeral. Ale nechajme to, lebo toto je Božie [riadenie], celé to; nie je dobré dopredu s ničím rátať. To je dobre, že ste išli do Harasztiho; aspoň dýchate ten dobrý vzduch zo salaša, hoci pravda, ani v Árokszállási nie je zlý vzduch. A Ide [meno neisté; Ida?], s ktorou sa každý deň stretávam, lebo chodíme obedovať na to isté miesto, povedala, že vyzeráte veľmi dobre, moja Jolánka. Len si dávajte pozor, drahá hviezdička moja, aby ste neprechladli. S kedel [neprečítané slovo] sa síce veľmi nezaoberám; zaneste [to] dole Ilone, neviem, ako to zariaďujú.**

**V rámiku na známku: S Bohom, [prečiarknuté] moja drahá! Bozkávam Vás nespočetnekrát. Váš ctiteľ, Feri.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1265/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the four image files, decodes the manual ledger work/ledger.txt with the key, and prints the literal rows, the sign count (597 signs in 34 rows) and the normalized text. It does not read the images; the transcription step is manual and was checked in review.

## Uncertainties

- **Row 25 kedel, the one word not understood.** All signs are clear (k, e with tick, d, e, l). Two guesses, neither adopted: kedél (kedély, "mood"), against which this writer spells ly as j and which lacks the instrumental that törődik needs; and keddel ("with Tuesday"), which has that ending and fits the writer's single consonants (keden for kedden on HCP 1307), but nothing on the card mentions a Tuesday.
- **Rows 25–26, what is to be taken down to Ilona** is not stated, and vigye may be formal "you" or a third person who is not named. It might relate to kedel.
- **Row 20 Ide.** The sign after i is heavily retraced, with the long stroke first, the reverse of this card's d, so Ide / Ihe / Ipe / Ine are all candidates. That a person is named is inferred only from ő mondta. Ida would need two bars; the sign shows three. No such person appears on sister cards.
- **Row 21 találkok.** The fourth sign is blotted and crossed, between r and t; t rests on word sense. Találkok is taken as találkozok.
- **Row 12 re[nde]lése.** The sense "God's ordinance" rests on three supplied letters. The e is heavily retraced.
- **Calls made by word sense:** the first sign of nézzek (row 10) has the d shape and is read n; the h of Haraszti could be p; the blotted d of drága and intézkednek shows only its tick. Rows 6 to 7 have no verb after Berénybe, so [elmegyek] is supplied.
- **Stamp box.** Several signs are irregular or overwritten (Isten, drágám, számtalanszo, Feri), and each is read by word sense. The rest of row S2 is the writer's own heavy deletion. Nothing can be read under it, and it is not reconstructed.
- **Spelling.** The writer drops and doubles letters as on sister cards. Examples normalized: szeretetedes, kics, hasak, semit, rosz, csilagom, megfazon, vigyazon, hejre, se nincs. The form nyéron (for nyáron) is as written.
- The date of the card and the civil identity of Feri, Ilonka and Ilona are not established. Ilona may or may not be the Ilonka of row 5.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. It ran the reproduction command, made its own reading of all rows (31 of 34 agreed exactly at once), confirmed the key against HCP 1216, checked the stamp box and every disclosed restoration, and recomputed the repeated words. Its four findings were accepted, and the solver rechecked them on the crops:

- **Major: end of row 25.** The first version read `ilonanesvigye`, Ilona ne [i]s vigye le, "let Ilona not even take [it] down". The portal stamp had hidden the two signs. In the stamp-free map they are a (two bars) and k (full section mark), so the row reads Ilonának vigye le, "take [it] down to Ilona", with no restoration. The clause was re-translated, and the earlier gloss of kedel as "mood" was withdrawn; the word now stays unread.
- **Minor: row 20.** The sign is not a clean d; it is now marked as unsure and the candidates are listed.
- **Minor: citations.** Two references to HCP 1263 were wrong and now point to HCP 1305, 1218, 1283 and 1288.
- **Minor: disclosures.** The retraced u of hagyjuk, the blot on the a of Jolánkám in row 23, and the restored re[nde]lése are now marked.

Two signs of 597 changed. The reviewer stated that this direct correction needs no second round, and the card was closed on that basis.

## Sources

- HC Portal record 1265, General, Description and Attachments tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1265 (source/metadata.md). The portal's reference: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- Address side: https://api.hcportal.eu/media/3856/conversions/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-86_adr-large.jpg (source/address-large.jpg); original at https://api.hcportal.eu/media/3856/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-86_adr.jpg
- Picture side: https://api.hcportal.eu/media/3855/conversions/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-86_pic-large.jpg (source/picture-large.jpg); original at https://api.hcportal.eu/media/3855/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-86_pic.jpg
- Family key and context: ciphers/hcp-1216 (key), hcp-1305, hcp-1263, hcp-1272 in this repository.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-01: no record for this number.
