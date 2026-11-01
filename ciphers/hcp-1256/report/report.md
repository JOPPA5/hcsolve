# HCP 1256 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-68): Feri to Jolánka Tóth, lonely in Pest

Human solver: Tomáš Pavuk

**Status: complete reading of the message with the known family key; one short stretch of the sign-off (about ten signs) is read literally but not understood. Independent review 1 verdict REVISE; all eleven findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1256 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1256), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The portal cites the HistoCrypt article at https://ecp.ep.liu.se/index.php/histocrypt/article/view/166.

The card is one of a group of Hungarian cipher postcards to Jolánka Tóth at Jász-Árokszállás (Jászárokszállás), several of them signed by Feri. The address side is in plain red ink: **Tóth Jolánka úrleánynak szeretettel, Jász-Árokszállás** ("To Miss Jolánka Tóth, with love"), with the plain word **Szépremény** ("fair hope") at the top. The whole left side and a strip across the bottom are in cipher. The writer also wrote eight short cipher rows on the stamp area; a stamp was later removed, leaving only fragments, so these rows are visible today.

The picture side has only a printed verse (*Aranyeső*, "Huzok az ujjadra aranyos karikagyűrűt") and no cipher.

![Address side with the cipher text; the eight short rows sit on the stamp area at the top right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The date is not established. The cancellation is inverted and only partly visible, and it was not read. The mention of St Stephen's Day shows only that the card was written before a 20 August.

## Method

The key was **transferred unchanged** from the finished family card HCP 1216; this is not a new key recovery. No reading of this card was supplied or consulted, and no published solution was met.

The transcription is **manual**. The solver read 25 main rows and 8 stamp-area rows sign by sign from enlarged crops of the un-converted scan and recorded them in a ledger with one token per written sign (`work/ledger-opus.txt`). A short script (`work/decode_opus.py`) checks the hashes of the images, applies the key and prints the literal rows and the normalized text:

```sh
python3 -I ciphers/hcp-1256/work/decode_opus.py
```

Word divisions, accents and normalized spellings are editorial. The cipher has no word spaces; the words run on across row ends.

## Key

Simple monoalphabetic substitution with invented graphic signs. Dots over o and u give ö and ü, and acute accents appear only as occasional ticks.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| two bars | a | six-like sign | b | left bowl | c |
| long + short tick | d | three bars | e | upright cross | f |
| open loop with descender | g | tall stroke + short tick | h / p | dotted crossed curve | i |
| inverted T | j | section mark, small "5" | k | wave | l |
| three short strokes | m | two short strokes | n | cursive loop | o |
| F-shape | r | right bowl | s | corner | t |
| plain cross | u | chevron | v | low descender | y |
| crossed diagonal | z | | | | |

The digraphs are spelled out: gy as g + y, cs as c + s. The h/p sign is a near-homograph: h or p is decided by word sense, as are some d/n calls.

## Plaintext

Literal decipherment, row by row (h stands for the h/p sign; `[x]` is a sign hidden by the stamp remnant; `{?}` an unsettled sign; `{-}` the bar of a hidden sign):

```text
01 szeretetedesjolankam
02 kivanomhogyalegjobb
03 kedvebentalaljasoraim
04 hogymulatotvasarnah
05 jobbanmintenmertenmar
06 egeszelarvulokebeahast
07 bemertegyetlenszora
08 koztatomtolismegvagyok
09 fosztvaamenyibefagerjoska
10 hazamentesmostnincssenkim
11 barjobaratotkönyensze
12 rezhetekcsakhogyhezbe
13 kerülesnekemmostmar
14 ojanbaratranincsszük
15 segemvoltamsandor
16 nalfeloraigbeszegett
17 veleaztlehetmondani
18 hogyminderölbeszelunk
19 aztismontahogymiertnem
20 megyekgyakrabbanhozza
21 herszeenaztmondtamugyistudomhogynemerrabeszel
22 getniedesemakerfenykehetjövöhetenmekküldömva
23 sarnahfogomlevetetnimagamszombatonvettemruhatiscsak
24 kolgozhassakakormajdcsakrendbejövökistvankirajra
25 szandekozokhazamennihavalamiközbenemjön
S1 [i][s][t]enve
S2 leedesem
S3 aboldog
S4 viszot
S5 lat{a/e}sig
S6 {?}arsoka
S7 {-}eszimado
S8 jaferi
```

**Hungarian (normalized; square brackets mark letters the writer omitted or the stamp hides):**

Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Hogy mulatott vasárnap? Jobban, mint én, mert én már egész elárvulok ebbe a Pestbe, mert egyetlen szórakoztatómtól is meg vagyok fosztva, amennyiben Fáger Jóska hazament, és most nincs senkim. Bár jó barátot könnyen szerezhetek, csakhogy pé[n]zbe kerül, és nekem most már olyan barátra nincs szükségem. Voltam Sándornál, fél óráig beszé[l]gett[ünk]. Vele azt lehet mondani, hogy minde[n]ről beszélünk. Azt is mon[d]ta, hogy miért nem megyek gyakrabban hozzá. Persze én azt mondtam, úgyis tudom, hogy nem ér rá beszélgetni. Édesem, a kér[t] fényképet jövő héten megküldöm; vasárnap fogom levetetni magam. Szombaton vettem ruhát is. Csak dolgozhassak, akkor majd csak rendbe jövök. István királyra szándékozok hazamenni, ha valami közbe nem jön.

Under the stamp: [Ist]en vele, édesem, a boldog viszo[n]tlátásig. {?arsoka[?]ész} imádója Feri.

**English:**

My beloved sweet Jolánka! I wish that my lines may find you in the best of moods. How did you enjoy yourself on Sunday? Better than I did, for I am growing quite orphaned in this Pest, since I have been deprived even of my only entertainer: Jóska Fáger has gone home, and now I have nobody. True, I could easily get a good friend, only that costs money, and I have no need of that sort of friend any more. I was at Sándor's; we talked for half an hour. With him one can say that we talk about everything. He also asked why I do not go to see him more often. Of course I said that I know anyway that he has no time for chatting. Darling, the photograph you asked for I will send next week; on Sunday I am going to have my picture taken. On Saturday I also bought clothes. If only I can work, then I shall get back on my feet in the end. For King Stephen's Day [20 August] I intend to go home, if nothing comes up.

Under the stamp: God be with you, darling, until the happy reunion. [? unread word or phrase] your admirer, Feri.

**Slovak:**

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Ako ste sa zabavili v nedeľu? Lepšie než ja, lebo ja už celkom osirievam v tejto Pešti, keďže som prišiel aj o svojho jediného zabávača: Jóska Fáger odišiel domov a teraz nemám nikoho. Dobrého priateľa si síce ľahko zaobstarám, lenže to stojí peniaze a takého priateľa už teraz nepotrebujem. Bol som u Šándora, pol hodiny sme sa rozprávali. S ním sa dá povedať, že sa rozprávame o všetkom. Spýtal sa aj, prečo k nemu nechodím častejšie. Pravdaže, ja som povedal, že aj tak viem, že nemá čas na rozprávanie. Drahá, fotografiu, o ktorú ste žiadali, Vám budúci týždeň pošlem; v nedeľu sa dám odfotografovať. V sobotu som si kúpil aj šaty. Len nech môžem pracovať, potom sa nakoniec dám do poriadku. Na Štefana kráľa [20. augusta] mám v úmysle ísť domov, ak do toho niečo nepríde.

Pod známkou: S Bohom, drahá, do šťastného zvidenia. [? neprečítané slovo alebo slovné spojenie] Váš ctiteľ Feri.

## What remains uncertain

- **Sign-off (S6–S7).** Before *imádója* stands `{?}arsoka`, a sign hidden by a stamp fragment, and `esz`: about ten signs, one word or a short phrase. Neither solver nor reviewer could read it, and no guess is offered as a reading.
- **Restoration.** *Ist-* of *Isten vele* is hidden by the stamp remnant and restored from the visible `en ve | le` and the family's formula.
- **Letters supplied.** *pé[n]zbe*, *mon[d]ta*, *a kér[t]*, *viszo[n]tlátásig* and *beszé[l]gett[ünk]* (where *-ünk* is inferred from row 18). Only *a kér[t]* affects the sense.
- **Word-sense calls.** *Pest* emends a clearly written a (`hast`). *dolgozhassak* begins with a k-shaped sign (`kolgozhassak`). Row 18 `minderöl` is read *minde[n]ről* ("about everything"); *mind erről* ("all about this") is the alternative. The h/p choice throughout rests on sense.
- **Single signs.** S5 has a or e in *látásig*. Row 22 *héten* has a blot over one stroke of n. Row 18 *beszélünk* has an overwritten sign read as u(ü), without visible dots.
- **Unverified.** The family name Fáger (possibly Fágér) cannot be checked, and "Szépremény" may be a motto, a name or a place.

## Why it is believed correct

The key from HCP 1216, applied unchanged, turns the 25 main rows into running colloquial Hungarian of the period. Long sequences such as *szórakoztatómtól is meg vagyok fosztva* and *István királyra szándékozok hazamenni* cannot arise by chance. Repeated words decode identically (*hogy*, *csak*, *most*, *vasárnap*), and Sándor, Feri, the closing formula and the formal address all fit the family.

## Review and what changed

An independent Claude Opus 5.5 agent reviewed the card. It ran the command, read all 33 rows on its own crops and decoded them with its own script, using the key table only from HCP 1216. It found no wrong key value but gave verdict REVISE with eleven findings. Its reading was not blind, since it had seen the ledger first. The changes were:

- Row 22 is *a kér[t] fényképet* ("the photograph you asked for"), not *akár fényképet* ("even a photograph"): the accent tick stands over an e.
- Row 24 is `akor` = *akkor* ("then"), not `asor`: the second sign is k, which removed a listed uncertainty.
- Row 21 has a second three-bar sign, so it reads *Persze én azt mondtam*.
- Rows 19 and S4 are transcribed as written (`monta`, `viszot`), with the letters supplied in brackets.
- The last sign of S1 is e, so the card has ordinary *vele*.
- Row 18 now prefers *minde[n]ről*, and the sign in S5 is left open as a or e.
- The address now includes *szeretettel*, the gy and cs signs are recorded as the two signs they are, and the justification for *Pest* and the extent of the unread sign-off are stated more exactly.

After the changes the reviewer's reading and the ledger agree in every row except S5, the sign deliberately left open.
