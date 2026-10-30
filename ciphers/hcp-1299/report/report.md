# HCP 1299 (cpc_-12-03_HU__HU_Jasz Arokszalas_jolanka-96): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (776 signs, all with a value); one word, *ojot*, stays unexplained. Independent review 1 verdict REVISE; all findings addressed, key unchanged.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1299 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1299), portal name cpc_-12-03_HU__HU_Jasz Arokszalas_jolanka-96, part of Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, with date and language unknown, recipient Tóth Jolánka, and no transcription or solution attached.

It is a romantic picture postcard: a man and a woman in an embrace, captioned *Szeretni édes...* ("Sweet it is to love..."), with a printed verse (scanned sideways):

*Óh milyen boldogság / Szeretni, szeretni! / Nem tudnálak soha / Tégedet feledni.*

("Oh what happiness / To love, to love! / I could never / Forget you.")

The address side is in plain writing: *Tóth Jolánka úrleánynak, Jász Árokszállás* (the town Jászárokszállás in Hungary). The cancellation reads RÁKOSPALOTA-Ú..., and its date cannot be read, so the card is undated. Next to it stands a line of plain handwriting, tentatively *Szép reményi…*, with the end struck through; it is not cipher and its purpose is unknown.

The whole message is on the address side in invented signs: 29 rows, the last two running under the address to the right corner, one continuation up the right edge read from the bottom, and eight short rows in the stamp box. The stamp is lost, which exposes the short rows in the printed stamp box, written across the publisher's triangular mark.

The card belongs to the "Jolánka" family: cards to the same woman, signed Feri, with one key. Several are deciphered in this repository (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). The key was **transferred** from those cards; this is not a new key recovery. No reading of this card was supplied or consulted.

![Address side with all the cipher text (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, scanned sideways (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, sign by sign, from enlarged crops of the un-converted scan; there is no OCR. The family key decoded the text at once. Word sense guided the division into words, and it decided the few signs listed under Uncertainties, so the reading is not blind. The ledger (work/ledger.txt) holds one token per written sign, and one command checks the source hashes, decodes the ledger and prints the result:

```
python3 -I ciphers/hcp-1299/work/decode.py
```

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family, same key as HCP1216, 1212, 1213, 1217, 1218, 1243, 1301. The key was taken over from those cards and fitted without change; as on the sister cards, *gy* is written as two signs.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl (only inside cs) | c | three short strokes | m | gamma/corner | t |
| long + short joined | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + separate short (h/p near-homograph) | h / p | low descender | y |
| open loop with descender | g | crossed curve (dot often displaced) | i | crossed diagonal with tail | z |
| inverted T | j | opposed bowls | cs | | |

Dots over o/u give ö/ü. Acute marks and the ő/ű double marks are mostly not distinguishable and are supplied in normalization. q, w, x are unused.

## Plaintext

Literal decipherment. `[x]` is a sign hidden by a blot, `{x}` a sign written above the line by the writer as a correction. E1 runs up the right edge; the eight short rows stand under the stamp.

```
01 szeretetedesjolankamedesegyet     16 vemmikorbecsessoraitel
02 lenremenyemkivanomhogy            17 olvastamcsakeztsajnaltam
03 alegjobbegessegbentalaljaso       18 hogymiert[n]incsitazazan
04 raimsajnalattalveszem[t][u][d]o   19 gyalkaamelikesoroket
05 masulhogyutobbisoraojke           20 irjahogyszivemhezölel
06 sönvalaszoltamvolna               21 hetnemhogyhaderezhetne
07 barenmikormegkaptamrög            22 teljesenboldognakma
08 tönvalaszoltammert                23 gathigyjeeledesemugyfaj
09 azthiszemedesemhogyma             24 aszïvemhogynemletha
10 gaisojotnehezenvarja              25 tomcsakaztszeretnemtud
11 soraimintamijennehe               26 nimedigkelmegazegyütle
12 zenvaromamagabecsesso             27 tünkigazenarvaszivemnekcsodalomedesemhogyojha
13 rai[t]higyjeeledesemszo           28 marbelenyugszikhogyhaegyicsitesetlegkesikalapom
14 valkisemlehetfejezniazt           29 abolkelazt[f]e{l}teteleznihogykönyenefelejtenehaasor
15 azerzesemielfogtaszi              E1 sszetvalasztanabenünket   (up the right edge)
Under the stamp: istenvele | edesem | csokolja | szamta | lanszor | sirig | hukedves | seferi
```

## Hungarian (normalized)

Square brackets mark letters supplied by the editor.

Szeretet[t] édes Jolánkám, édes egyetlen reményem! Kívánom, hogy a legjobb egésségben találja soraim. Sajnálattal veszem tudomásul, hogy utóbbi sora[ira] oly későn válaszoltam volna, bár én, mikor megkaptam, rögtön válaszoltam, mert azt hiszem, édesem, hogy maga is ojot[?] nehezen várja soraim, [m]int a[hogy] milyen nehezen várom a maga becses sorait. Higyje el, édesem, szóval ki sem lehet fejezni azt az érzésem, mi elfogta szívem, mikor becses sorait elolvastam. Csak ezt sajnáltam, hogy miért nincs it[t] az az angyalka, a melyik e sorokat írja, hogy szívemhez ölelhetném, hogy had[d] érezhetné teljesen boldognak magát. Higyje el, édesem, úgy fáj a szívem, hogy nem láthatom. Csak azt szeretném tudni, med[d]ig kel[l] még az együt[t]létünkig az én árva szívemnek. Csodálom, édesem, hogy oj[=oly] hamar belenyugszik, hogy ha egy [k]icsit esetleg késik a lapom, ab[b]ól kel[l] azt [f]eltételezni, hogy kön[n]yen e[l]felejtene, ha a sors szétválasztana ben[n]ünket.

Under the stamp: Isten vele, édesem! Csókolja számtalanszor sírig hű kedvese, Feri.

## English translation

My beloved sweet Jolánka, my sweet only hope! I wish that my lines may find you in the best of health. I learn with regret that I am supposed to have answered your last lines so late, although when I received them I answered at once, because I believe, darling, that you too wait for my lines as impatiently as I wait for your precious lines. Believe me, darling, words cannot even express the feeling that seized my heart when I had read your precious lines. I regretted only this: why is that little angel who writes these lines not here, so that I could press her to my heart, so that she might feel herself completely happy. Believe me, darling, my heart aches so that I cannot see you. I should only like to know how long my orphaned heart must still wait until we are together. I am surprised, darling, that you so quickly accept that if my card is perhaps a little late, one must conclude from it that [I] would easily forget [you] if fate parted us.

Under the stamp: God be with you, darling! Kisses you countless times your sweetheart, faithful unto the grave, Feri.

## Slovak translation

Moja milovaná, sladká Jolánka, moja sladká jediná nádej! Želám si, aby Vás moje riadky našli v najlepšom zdraví. S ľútosťou beriem na vedomie, že som vraj na Vaše posledné riadky odpovedal tak neskoro, hoci keď som ich dostal, odpovedal som hneď, lebo si myslím, drahá, že aj Vy tak ťažko čakáte moje riadky, ako ja ťažko čakám Vaše vzácne riadky. Verte mi, drahá, slovami sa ani nedá vyjadriť ten pocit, ktorý mi zovrel srdce, keď som dočítal Vaše vzácne riadky. Ľutoval som len to, prečo tu nie je ten anjelik, ktorý píše tieto riadky, aby som ho mohol pritisnúť k srdcu, aby sa mohol cítiť úplne šťastný. Verte mi, drahá, tak ma bolí srdce, že Vás nemôžem vidieť. Chcel by som len vedieť, ako dlho ešte musí moje osirelé srdce čakať, kým budeme spolu. Čudujem sa, drahá, že sa tak rýchlo zmierujete s tým, že keď môj lístok možno trochu mešká, treba z toho usudzovať, že by som [Vás] ľahko zabudol, keby nás osud rozdelil.

Pod známkou: S Bohom, drahá! Bozkáva Vás nespočetnekrát Váš do hrobu verný milý, Feri.

## Uncertainties

- **Row 10 *ojot*:** clear signs, odd form; perhaps *oly*/*olyan* ("so"), perhaps a false start. Left literal. The sense "(so) hard" does not depend on it.
- **Row 29 *könyene felejtene*:** there is no n before the last e, so the text has no negation. Normalized *könnyen e[l]felejtene*, "would easily forget". The verb is 3rd person: grammatically formal "you", or a slip for 1st-person *felejteném*. The sense favours "I", since he is the late correspondent, but the card does not settle it, and the translations bracket the pronoun.
- **Blots:** row 4 *[t][u][d]o*, row 13 *rai[t]*, row 18 *[n]incs* have outlines that fit; the blot in row 29 hides one sign completely, and its f is supplied from sense only. The ending of row 5 *sora[ira]* is also supplied, for the verb *válaszoltam*.
- **Calls that rest partly on word sense:** the h/p sign (p in *kaptam* and *lapom*, h elsewhere); some faint a/e (two or three bars), such as *válaszoltam* and *mert*; the d and o of *csodálom*; row 24 *letha-*, a heavily inked sign, read *láthatom*; row 28 *esetleg*, whose t comes close to the f shape; row 18 *it*, where *ott* is possible and changes little.
- **Kept as written:** *sorokét* in row 19 (normalized *sorokat*), and the writer's spellings *mijen*, *melik*, *higyje*, *kel*, *medig*, *együtle*, *aból*, *benünket*.
- **Date:** not legible. No date is claimed.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-ran the command, decoded the ledger through the key file of HCP 1216 with its own script (all values agreed), read every row from the scan, and tested the language. Verdict: **REVISE**. The key and nearly all of the reading stood, but five signs were misread and one was omitted. All were checked on the scan and accepted:

- Row 27 *Csinálom* is *csodálom*, "I am surprised": the d has a long lower stroke, and the i had no dot.
- Rows 27–28 *oj ha / már* is one word split over the line: *oj hamar* = *oly hamar*, "so quickly".
- Rows 18–19 *az ezen gyalka* (an unknown word) is *az az an|gyalka*, "that little angel": two bars, not three, in two places.
- Row 29: the earlier *könnyen ne felejtene*, "would not easily forget", read a negation that is not on the card. It is now "would easily forget", which reverses the clause.
- Row 29: an interlinear l of *feltételezni*, missed before, was added to the ledger.
- Row 21: one bar more gives *érezhetné*.
- Also added: the plain handwriting and the verse in full, and the corrected sign count.

These fixes removed two of the three "not understood" items and made the closing sentence read naturally. The solver then did a full a/e pass over the card, as the reviewer suggested; no further sign changed. The key was not altered at any stage.
