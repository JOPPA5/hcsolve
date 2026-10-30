# HCP 1291 (cpc_1913-08-31_HU__HU_Jasz Arokszalas_jolanka-41): Feri to Jolánka Tóth, an apology for writing so rarely

Human solver: Tomáš Pavuk

**Status: all cipher text on the card is read, with the small uncertainties listed below; independent review 1 verdict REVISE, all findings addressed. Decipherment with a known family key.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1291 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1291), from Tobias Schrödel's collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, date 1913-08-31, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was used or seen.

The picture side is a tinted photograph of a couple with a printed Hungarian verse, Két szív ha földobog ("When two hearts leap"). It is ordinary print, not cipher.

The address side carries the cipher text in 22 rows on the left half and 6 more rows on the place of the stamp, which has been removed. The address is in plain writing: as far as can be made out, Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás ("To the Hopeful Miss Jolánka Tóth, Jászárokszállás"); the first word lies under a postmark and is not secure.

The card has two postmarks. A round date stamp in the middle shows …SZAPÁTI (Jászapáti) 913 AUG 31. A second, larger strike sits at the stamp position, with `BU…` and `913` legible and its place and day not. So 31 August is the date of the Jászapáti strike; whether that was the day of sending, transit or arrival is not known.

The card belongs to the family of cipher cards addressed to Jolánka Tóth, several of them solved in this repository (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). The sender is taken to be the Feri of HCP 1216 from the first name, closing formula, key and addressee; the two hands were not compared in detail. Nothing is claimed about the writer's work or the troop trains he mentions.

![Address side: 22 cipher rows at the left, six on the stamp position, both postmarks, plain address (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: printed verse, no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

![Stamp corner: six cipher rows under the former stamp, and the second postmark with BU… and 913 (work/stamp-corner.png)](../work/stamp-corner.png)

## Method

The key was not recovered here: it was transferred unchanged from the finished sister cards, above all HCP 1216. Every sign of this card was nevertheless read afresh from enlarged crops of the high-resolution original scan. The result is a manual sign ledger (`work/ledger.txt`), not OCR. The ledger has 444 written signs, one of them only probable (row 3), and one hidden sign is restored. A script (`work/decode.py`) checks the hashes of the images and decodes the ledger:

```text
python3 -I ciphers/hcp-1291/work/decode.py
```

The reviewer made an independent row-by-row transcription from its own crops and compared it by script with the ledger. That comparison produced most of the corrections listed under Review. After the corrections, the two transcriptions differ only in how uncertain signs are marked.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs. Digraphs are spelt with two signs (gy = g+y, sz = s+z, ny = n+y). Accents are marks over the sign and are mostly faint.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | left bowl | c | right bowl | s |
| tall + short stroke | h / p | wave | l | gamma/corner | t |
| three bars | e | three short strokes | m | plain cross x | u |
| upright cross + | f | two short strokes | n | chevron | v |
| open loop with descender | g | cursive loop | o | low descending curve | y |
| dotted crossed curve | i | inverted T | j | crossed diagonal (x with tail) | z |
| short + tall stroke | d | | | | |

The strokes of d and of h/p come in opposite order on this card, as the sample below shows: d is a short high stroke followed by a long one running below it, and h/p is a tall stroke followed by a short one. Only h against p rests on word sense (p in laphoz and nap, h elsewhere). n is a level pair.

![Sign samples from this card: top row d, middle row h/p and n, bottom row d of row 13 and n (review/work/gallery.png)](../review/work/gallery.png)

## Plaintext

Literal decipherment, row by row. {x} = value depends on word sense; {a?} = probable faint sign; [x] = restoration of a hidden sign.

```text
01 szeretettedesjolankam
02 egyetlenremenyemkivanom
03 hogy{a?}legjobbegessegbenes
04 kedvebentalaljasoraim
05 neharagu{j}onhogyijenrit
06 anirokdeugyelvagyok
07 foglalvahogynemju
08 tokhozzamostsok
09 katonavonatvaesugy
10 elvagyokfglavahogy
11 aligvarohogyle
12 fekheehezalaphozis
13 marnegyedszefogokhoz
14 zaazertkerem{m}agat
15 edesemlegyenelne
16 zesselirantammert
17 jobbanszeretnekin
18 kabbmin{d}{e+n}apirnimi{n}t
19 hogykenytelenvagyok
20 ijenritkanirni
21 kivanokjomulatast
22 szeretökedvessefer
S1 istenve
S2 leedesem
S3 maradok
S4 sirig
S5 hukedves
S6 s[e]fer{i}
```

### Hungarian (normalized)

Szeretett édes Jolánkám, egyetlen reményem! Kívánom, hogy {a} legjobb egészségben és kedvében találja soraim. Ne haragudjon, hogy ilyen ritkán írok, de úgy el vagyok foglalva, hogy nem jutok hozzá. Most sok katonavonat va[n], és úgy el vagyok f[o]gla[l]va, hogy alig váro[m], hogy lefekhe[ssek]. Ehhez a laphoz is már negyedsze[r] fogok hozzá. Azért kérem magát, édesem, legyen elnézéssel irántam, mert jobban szeretnék inkább mindennap írni, minthogy kénytelen vagyok ilyen ritkán írni. Kívánok jó mulatást. Szerető kedvese, Fer[i].

Under the stamp: Isten vele, édesem! Maradok sírig hű kedvese, Feri.

### English

My beloved sweet Jolánka, my only hope! I wish that my lines find you in the best of health and spirits. Do not be angry that I write so rarely, but I am so busy that I cannot get round to it. There are many troop trains now, and I am so busy that I can hardly wait to be able to lie down. Even this card I am setting about for the fourth time already. So I ask you, my darling, to be indulgent with me, for I would much rather write every day than be forced to write so rarely. I wish you a good time. Your loving sweetheart, Feri.

Under the stamp: Farewell, my darling! I remain, faithful unto the grave, your sweetheart, Feri.

### Slovak

Moja milovaná, sladká Jolánka, moja jediná nádej! Želám si, aby Vás moje riadky zastihli v najlepšom zdraví a nálade. Nehnevajte sa, že píšem tak zriedka, ale som taký zaneprázdnený, že sa k tomu nedostanem. Teraz je veľa vojenských vlakov a som taký zaneprázdnený, že sa sotva dočkám, kedy si budem môcť ľahnúť. Aj k tomuto lístku sa púšťam už štvrtýkrát. Preto Vás prosím, drahá, buďte ku mne zhovievavá, lebo oveľa radšej by som písal každý deň, než by som bol nútený písať tak zriedka. Želám Vám dobrú zábavu. Váš milujúci milý, Feri.

Pod známkou: S Bohom, drahá! Zostávam do hrobu verný, Váš milý, Feri.

## Uncertainties

Signs:

- **Row 3:** two faint grey marks in a gap between hogy and legjobb, probably a pale a; they may be staining. The text reads with or without it.
- **Row 5 `haragu{j}on`:** a bar with stems, between j and f in shape; j by sense (haragujon for haragudjon).
- **Row 14 `{m}agát`:** three strokes, the first with a crossbar; m by sense.
- **Row 18 `min{d}{e+n}ap`:** an overwritten sign read as e and n fused, and before it a sign with the h/p shape, read d by sense. Mindennap is not in doubt.
- **Row 18 `mi{n}t`:** faint strokes, two or three; n by sense (minthogy).
- **Row S6:** one sign under the stamp remnant is restored as e (compare kedvesse, row 22), and the final hook is read i by sense. Row 22 ends Fer with clean paper after it.

Editorial steps, where the writer omitted or shortened something:

- **Row 11 `varo`:** the writer left out the final m, váro[m].
- **Rows 11–12 `lefekhe`:** read lefekhe[ssek], "that I may lie down", cut short. The ending is not on the card. The alternative lefek[üdjek]. De ehhez… would need an h-shaped sign to be d. The sense barely changes.
- **Row 13 `negyedsze`:** negyedsze[r] with final r omitted. The d is less clearly proportioned than others on the card, and the word confirms it.
- **Rows 9, 10:** va[n], and f[o]gla[l]va (row 7 spells the word in full).
- **Spellings:** egessegben, ijen, ritán (rows 5–6), ehez, kedvesse, hu are normalized; most accents are not visible and are supplied.

Not established: the place and day of the second postmark, the role of the 31 August date, and the identity of Feri beyond the matches above.

## Why it is believed correct

The key comes from other cards and yields connected, idiomatic Hungarian with formal address across the whole card, with no sign left without a value. The text is one continuous argument: an apology, the reason, a request for indulgence. Repeated words decode identically (hogy ×6, el vagyok f…a ×2, ilyen ritkán ×2), and the closing sírig hű kedvese … Feri matches HCP 1216. Addressee and place match the plain address.

## Review and what changed

An independent Claude Opus 5.5 reviewer tried to refute the reading, using its own crops and transcription. Its verdict was **REVISE**: it upheld the cipher type, key, message and translations, but found the ledger wrong at several signs. The solver confirmed the sign findings on the crops and made these changes:

- **Row 11:** an m that is not on the card was removed; it had been supplied from context. The text is now váro[m].
- **Row 13:** the sign read n is d, so the awkward `négy(en)sze[r]` became negyedsze[r], which is the "fourth time" the translation already said.
- **Key:** the claim that d, h and p look alike was wrong for this hand; the shapes above were stated instead.
- **Row 12:** following from that, the sign after fek is h, not d. lefek | de ehez became lefekhe[ssek]. Ehhez…. The reviewer offered this as an alternative to be listed; the solver adopted it as the main reading.
- **Row 18:** the d of mindennap was marked as read by sense.
- **Row 4:** a dropped l was restored, so talalja; the "misspelling" talaja was the solver's error.
- **Row 3:** a probable faint a was entered.
- **Row 21:** the "isolated slash" is the stem of the t, and no longer counts as an extra mark.
- **Context:** the second postmark was added.

The message is unchanged apart from the rewording of the clause about lying down. Since these corrections were made after the review, the final text has been compared by script with the reviewer's transcription, but has not had a second review round.
