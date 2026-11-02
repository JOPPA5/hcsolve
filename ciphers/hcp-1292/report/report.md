# HCP 1292 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-75): Feri to Jolánka Tóth, a denial about a railwayman's daughter

Human solver: Tomáš Pavuk

**Status: whole card read with one lone word open (szororni) and one word blacked out by the writer; independent review 1 verdict REVISE, all eight findings addressed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1292 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1292), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-75, part of Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is print only: "Két szív ha földobog" and the verse "Tavasszal szép minden virág". It carries no cipher. The address side has the plain handwritten address **Szépreményü / Tóth Jolánka / úrleánynak / Jász Árokszállás** ("Miss Jolánka Tóth, of fair promise", a courtesy formula; Jászárokszállás is in Hungary). The rest of that side is filled with 31 rows of cipher signs, and nine more rows stand under the torn-off stamp. The postmark is only partly legible (…GALÁNTA) and gives no year, so the card is undated.

The writer signs Feri. He belongs to a family of cipher postcards to Jolánka Tóth in one hand and one key, several of which are finished in this repository (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). The key was **transferred unchanged** from those cards; this is not a new key recovery. No reading of this card was supplied or consulted, and no published solution was found.

![Address side with the plain address, the cipher rows and the removed stamp (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, print only (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is **manual** and was not blind to the family key: each row was read sign by sign from enlarged crops (red channel, autocontrast, 3 to 8 times) of the un-converted high-resolution scan of the address side. The letters are in work/ledger.txt, and the normalized text in work/normalized.txt. The command `python3 -I ciphers/hcp-1292/work/decode.py` checks the hashes of the scans and prints these two files. It does not decode from sign tokens, so it records the reading and proves nothing by itself.

A first attempt on 2026-10-30 stopped at partial. A second pass on 2026-11-02 resolved rows 20 to 23 (notably vasutasnak, "of a railwayman", from the plain x sign for u and two bars for a), and the stamp block. Review then corrected three passages (see below).

## Key

Monoalphabetic substitution with invented graphic signs, in Hungarian. Names of the shapes are mnemonic.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma corner | t |
| long stroke + short tick | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

Dots over o and u give ö and ü, and a double mark gives ű. Acute marks are often faint and are partly supplied in normalization. h and p are near-homographs and d and n differ mainly in stroke length; those calls rest on word sense (kaptam, panaszkodni, de).

## Plaintext

Letters as read, row by row (S = under the stamp). gy and cs are joined signs; braces mark a doubtful sign, a vertical bar a stain or the blacked-out block, a tilde the writer's filler dashes. Word divisions are not written on the card.

```text
01 szeretetedesjolakámbecses
02 soraitme{g}kaptammelynek
03 nagyonmegörültemédesem
04 iga{z}anörülökhogymegontenyem
05 nekmondhatomhigyjeeledé
06 semmennyirefejdalmatokozot
07 azatudathogyelkelvesztenem
08 megátédesénisborbankeres
09 {t}amavigasztalastésmajd
10 nemazéletembekerültmert
11 tegnapéjelegykicsitmámo
12 rosfejelmentemszolga
13 latbaéselaludtamafeken
14 ésazistenörzothogyakocsi
15 alanemkerültemdeazthagy
16 jukmertnempanaszkodni
17 akarokhaneminkamö{r}öme~~
18 metkifajeznihogyujrabol
19 dogitazatudathogyremel
20 hetamhetekmegédesemhogy
21 jelhogyse{m}ifélvasutasnak
22 {a}lanyorolnemtudokéssem~~
23 {m}ifelelanyrolmarsokzor
24 fogadtamhüségem{|}becsület
25 szovaldeúgy{l}atomaz|
26 marnemérsemitdeigmegazt
27 hiszemnem{v}esztettemelbe
28 csültemetönelötdeannaltöbetérazönbecsületszavaénel
29 lötemhogyhaesetlegcserbehagyezteleveletfomszorol
30 szorornidecsakesküvöjenapjanmertadignemvomkétségbe
31 szavátéseztkérdemmivelbizonyihetombeszerelmemet
S1 istenve
S2 leédesem
S3 marakto
S4 vebra
S5 iskedves
S6 seessi
S7 righű
S8 imado
S9 jaferi
```

Normalized Hungarian (square brackets are editorial):

> Szeretett édes Jolánkám! Becses sorait megkaptam, melynek nagyon megörültem, édesem. Igazán örülök, hogy még önt enyémnek mondhatom. Higgye el, édesem, mennyire fájdalmat okozott az a tudat, hogy el kell vesztenem magát, édes. Én is borban kerestem a vigasztalást, és majdnem az életembe került, mert tegnap éjjel egy kicsit mámoros fejjel mentem szolgálatba, és elaludtam a féken, és az Isten őrzött, hogy a kocsi alá nem kerültem. De azt hagyjuk, mert nem panaszkodni akarok, hanem inkább örömemet kifejezni, hogy újra boldogít az a tudat, hogy remélhetek még, édesem. [Higgye] el, hogy semmiféle vasutasnak a lányáról nem tudok, és semmiféle lányról. Már sokszor fogadtam hűségem[et] becsületszóval, de úgy [l]átom, az [blacked out] már nem ér semmit, de így meg azt hiszem, nem vesztettem el becsületemet ön előtt, de annál többet ér az ön becsületszava én előttem. Hogyha esetleg cserbe hagy, ezt a levelet fo[go]m szóról [szororni: sorolni?], de csak esküvője napján, mert addig nem vonom kétségbe szavát, és ezt kérdem: mivel bizonyíthatom be szerelmemet?

> Under the stamp: Isten vele, édesem. Mara[do]k továbbra is kedvese és sírig hű imádója, Feri.

## English

My beloved sweet Jolánka! I received your valued lines, which made me very glad, my darling. I am truly happy that I can still call you mine. Believe me, darling, how much pain the knowledge caused me that I must lose you, sweet one. I too sought consolation in wine, and it nearly cost me my life, for last night I went on duty a little tipsy and fell asleep on the brake, and God preserved me from falling under the wagon. But let us leave that, for I do not want to complain but rather to express my joy that the knowledge makes me happy again that I may still hope, my darling. Believe me that I know of no railwayman's daughter of any kind, nor of any girl at all. I have already many times sworn my fidelity on my word of honour, but I see that [blacked out] is no longer worth anything, yet even so I believe I have not lost my honour before you, but all the more is your word of honour worth before me. If you should happen to abandon me, I shall [recite? the verb is an unexplained word, szororni] this letter word by word, but only on your wedding day, for until then I do not doubt your word, and I ask this: how can I prove my love?

Under the stamp: God be with you, my darling. I remain still your sweetheart and your admirer faithful to the grave, Feri.

## Slovak

Moja milovaná, sladká Jolánka! Vaše vzácne riadky som dostal a veľmi som sa im potešil, drahá. Naozaj sa teším, že Vás ešte môžem nazývať svojou. Verte mi, drahá, akú bolesť mi spôsobilo vedomie, že Vás musím stratiť, milá. Aj ja som hľadal útechu vo víne, a takmer ma to stálo život, lebo včera v noci som išiel do služby trochu podnapitý a zaspal som na brzde, a Boh ma ochránil, že som sa nedostal pod vozeň. Ale nechajme to, lebo sa nechcem sťažovať, ale skôr vyjadriť radosť, že ma opäť oblažuje vedomie, že ešte smiem dúfať, drahá. Verte mi, že o nijakej dcére železničiara neviem, ani o nijakom dievčati. Už mnohokrát som na čestné slovo sľúbil vernosť, ale vidím, že [začiernené] už nemá žiadnu cenu, no aj tak si myslím, že som pred Vami nestratil česť, ale o to väčšiu cenu má Vaše čestné slovo predo mnou. Ak by ste ma náhodou opustili, tento list budem slovo po slove [odriekavať? sloveso je nevysvetlené slovo szororni], ale len v deň Vašej svadby, lebo dovtedy nespochybňujem Vaše slovo, a pýtam sa: čím môžem dokázať svoju lásku?

Pod známkou: S Bohom, drahá. Zostávam naďalej Váš milý a do hrobu verný ctiteľ, Feri.

## What remains uncertain

- **szororni (rows 29 to 30)** is the one un-understood word. All its signs are legible, it is an infinitive after fo[go]m, and the rest of the clause reads. A garbled sorolni ("to recite") is a conjecture only: at sign level it needs an added sz-form and r written for l. The verb in both translations is therefore a guess.
- **Row 25** ends in a word thoroughly blacked out by the writer. It cannot be recovered and the syntax does not need it.
- **Row 20 to 21, hogy jel:** the signs are hogy jel, normalized [Higgye] el from the same phrase in row 5. This rests on word sense and the parallel.
- **Rows 21 and 23:** the third stroke of se{m}i lies exactly on a vertical stain, and the first sign of row 23 is under a blot with two strokes visible. Both m's are word-sense restorations; semmiféle itself is safe.
- **Under stains,** read from traces or word sense: g in row 2, z in row 4, t in row 9, v in row 27, r in row 17, the first a of row 22, l of lanyorol, and l in row 25.
- **Writer's slips,** normalized editorially: Jolakám, inkam, bizonyihetom, fajezni, sokzor, vom for vonom, feken, megát for magát, töbet, the doubled l of el|lötem, kedves|se, and marakto vebra for maradok továbbra. Row 24 has an extra stroke after hűségem.
- The date and the identity of Feri are not established. His job on the railway follows from the text only.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) made its own crops, read all 31 rows and the 9 stamp rows at about 3.4 times, and every disputed place at 5 to 8 times, and decoded its own sign tokens for the disputed rows with its own statement of the key. Verdict: **REVISE**. The story and the key stood. All eight findings were accepted:

1. Rows 28 to 29: not "becsületszavánál előttem" but **az ön becsületszava én előttem**, with no sign changed. This reverses the sense: her word of honour is worth more before him.
2. Row 30: the sign before de has a dot and is i, not o. The interjection "no de" is withdrawn.
3. szororni is the real open word and is declared as such, with sorolni as a conjecture.
4. Row 8: megát is **magát**, the object of vesztenem ("that I must lose you, sweet"). The former open word and its stray clause are gone.
5. Row 31 reads szavát, not szevét, as a ledger correction.
6. The m's of rows 21 and 23 are labelled as word-sense restorations.
7. Row 28 has a single 6 (töbet), and kedves|se is listed as a slip.
8. The limits of the reproduction command are stated plainly.

![Row 30, the dotted i before de (review/work/g1.png)](../review/work/g1.png)

The reviewer could not verify the intended verb in row 30, the blacked-out word, or the stain-covered signs beyond word sense, and did not compare the handwriting with other Feri cards. Its check of ordinary rows was by eye, not a blind second transcription of the whole card.
