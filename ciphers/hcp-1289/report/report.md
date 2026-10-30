# HCP 1289 (cpc_--22_HU__HU_Jasz Arokszalas_jolanka-87): Feri to Jolánka Tóth, money or love

Human solver: Tomáš Pavuk

**Status: deciphered in full (824 signs, 29 rows and 8 rows under the stamp), with five restored signs and a few doubtful ones listed below; independent review 1 verdict REVISE, findings addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1289 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1289), portal name cpc_--22_HU__HU_Jasz Arokszalas_jolanka-87, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt proceedings, https://ecp.ep.liu.se/index.php/histocrypt). When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date, language and sender unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a tinted photograph of a man in evening dress at a table, leaning towards a woman, with the printed Hungarian verse *Sokszor úgy szeretnék sírni* ("Often I would so like to cry"). It carries no cipher text. The message is on the address side, written in reddish ink in invented signs: 25 rows in the left block, 4 long rows across the whole card under the address, and 8 short rows in the box under the stamp. The address is in clear: *Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás*. The postmark shows Árokszállás and "22"; the month and year are not legible, so the card is undated. The sender signs only "Feri".

The card belongs to a family of postcards in invented signs addressed to Jolánka Tóth, several of them deciphered in this repository (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). The key was transferred from those cards; it is not a new key recovery. A Feri signs HCP 1216 and a Sándor appears on HCP 1216 and 1217, but no identification of the persons is claimed. No earlier reading of this card was used. The portal attaches none, the orchestrator's check of the AI Decipherment Register on 2026-10-30 found no record, and no search of the wider literature was made.

![Address side: cipher rows, address in clear, stamp box (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, printed verse only, shown as scanned (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

No earlier work exists on this number. Claude Opus 5.5 identified the family from the address and the sign shapes, took the sign classes from HCP 1216 and transcribed the card by hand from enlarged crops of the un-converted scan. This is not OCR, and the transcription was made with the emerging sense in view. The ledger of 824 signs and a short decoder check the source hashes and print the literal text:

```sh
python3 -I ciphers/hcp-1289/work/decode_opus.py
```

The first reading corrected several signs from context checks (chevron v, not j; crossed diagonal z, not x), and the review corrected more (see below). The key was never changed to fit the text.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs and no word division. On this card *gy* is written as two signs (g + y) and *sz* as right bowl + z. Accents are written only irregularly, and the labels below are conventional names for handwritten shapes.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S-shape (flat top) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left + right bowl pair | cs | three short strokes | m | gamma/corner | t |
| stroke + tick at left, or joined | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + tick at right | h / p | low descender (y-shape) | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | dots over o / u | ö / ü | | |

On this card *gy* is written as two signs (g + y). *sz* is right bowl + z. Acute marks are irregular and are supplied in normalization. A small blot or tick above a sign is not a letter. Some detached short strokes are in a darker ink; a few sit where an acute belongs (over the a of *ráérek*, row 28; beside the e of *édes*, row 10).

## Literal decipherment

`[x]` restored, hidden sign; `(x)` struck out by the writer; `x?` doubtful sign; h stands for the h/p sign.

```text
01 dragacsilagombecsesso
02 raitmegkahtammelyetköszö
03 nökottobivagyiskedisora
04 itismegkahtamdee?lfeledtem
05 megkoszönnibarsorairavala
06 szoltambocsassamegfeledekeny
07 segemetsoraibolol[v]asomhogy
08 keresemhajlan[d]oj?eljesite
09 tenimelynekigazanörülök
10 eshogadjakösznetemetedes
11 egyetlelremenyemaztmar
12 nemiskelmondanomhogymil(y)
13 forronesszivbölszeretem
14 magatedesaztmarugyistud
15 jaeshogyahezgyözevagy
16 szerelemezcsakegytesz
17 minketboldodogamerrhi
18 jabavaköztünaforrosze
19 retethenznelk[ü]lnemtele
20 jesülhetegyesülesülesünk
21 mostmarmindentörekve
22 semazhogyaztahenztmeg
23 szerezzehogyfefesegeme
24 tehessemmertcsakakkor
25 leszaboldogsagunkteljes
26 tehatarakeremazistenthogyezthagymegszerezniminel
27 elö?bbhogyminelelöbbboldogoklbarmostisazokvagyunkasan
28 dormegraerekmegfoglalkoznicsakmikettenleg?yszer?etetel
29 egymasirantistenveleedesemenisszeretnekmartalalkozn[i]

stamp box: cskolom | akisszajat | gondoljon | neh[a]ram | edesem | mi?nten | magara | feri
```

## Plaintext (normalized Hungarian)

Word division, punctuation, accents and spelling are editorial. Square brackets mark endings the writer omitted.

Drága csillagom! Becses sorait megkaptam, melyet köszönök. Utóbbi, vagyis keddi sorait is megkaptam, de elfeledtem megköszönni, bár soraira válaszoltam; bocsássa meg feledékenységemet. Soraiból olvasom, hogy kérésem hajlandó teljesíteni, melynek igazán örülök, és fogadja köszönetemet, édes egyetlen reményem. Azt már nem is kell mondanom, hogy mily forrón és szívből szeretem magát, édes, azt már úgy is tudja, és hogy a pénz győz-e vagy szerelem, ez csak egy tesz minket boldoggá, mert hiába vak ösztön a forró szeretet, pénz nélkül nem teljesülhet egyesülésünk. Most már minden törekvésem az, hogy azt a pénzt megszerezzem, hogy feleségemé tehessem, mert csak akkor lesz a boldogságunk teljes. Tehát arra kérem az Istent, hogy ezt hagy[ja] megszerezni minél előbb, hogy minél előbb boldogok l[együnk], bár most is azok vagyunk. A Sándor[ral] meg ráérek még foglalkozni, csak mi ketten légy[ünk] szeretettel egymás iránt. Isten vele, édesem, én is szeretnék már találkozni.

Under the stamp: Csókolom a kis száját. Gondoljon néha rám, édesem, mint én magára. Feri.

## English translation

My dear star! I received your esteemed lines, for which I thank you. I also received the later ones, that is, your Tuesday lines, but I forgot to thank you, although I answered your lines; forgive my forgetfulness. I read in your lines that you are willing to fulfil my request, at which I am truly glad, and accept my thanks, my sweet only hope. I need not even tell you how ardently and from the heart I love you, sweet, you know that anyway, and whether money wins or love, only one of them makes us happy, for blind instinct, the ardent love, is in vain: without money our union cannot be fulfilled. Now my whole endeavour is to get that money, so that I can make you my wife, for only then will our happiness be complete. So I pray to God to let me get this as soon as possible, so that we may be happy as soon as possible, although we are so even now. As for Sándor, there is no hurry, I can still deal with him later [ending and sense inferred]; let only the two of us be loving towards each other. Farewell, my darling, I too would like to meet at last.

Under the stamp: I kiss your little mouth. Think of me now and then, darling, as I think of you. Feri.

## Slovak translation

Moja drahá hviezdička! Vaše vážené riadky som dostal, za čo ďakujem. Dostal som aj tie neskoršie, teda utorkové riadky, ale zabudol som sa poďakovať, hoci som na Vaše riadky odpovedal; odpusťte mi moju zábudlivosť. Z Vašich riadkov čítam, že ste ochotná splniť moju prosbu, z čoho sa naozaj teším, a prijmite moju vďaku, moja sladká jediná nádej. Ani Vám už nemusím hovoriť, ako vrúcne a zo srdca Vás milujem, sladká, to už aj tak viete, a či zvíťazia peniaze alebo láska, len jedno z toho nás urobí šťastnými, lebo márna je slepá náruživosť, vrúcna láska: bez peňazí sa naše spojenie nemôže naplniť. Teraz je celé moje úsilie v tom, aby som tie peniaze získal, aby som Vás mohol urobiť svojou ženou, lebo len vtedy bude naše šťastie úplné. Preto prosím Boha, aby mi to dal získať čo najskôr, aby sme čo najskôr boli šťastní, hoci aj teraz takí sme. So Šándorom sa ešte stihnem zaoberať neskôr, s tým sa neponáhľam [koncovka a zmysel sú odvodené]; len my dvaja buďme k sebe láskaví. S Bohom, drahá, aj ja by som sa už rád stretol.

Pod známkou: Bozkávam Vaše malé ústa. Myslite niekedy na mňa, drahá, tak ako ja na Vás. Feri.

## Uncertainties

Restorations (hidden signs, each with one letter that makes a word):

1. **Row 7 ol[v]asom**: a blot covers the chevron; only its lower strokes show.
2. **Row 8 hajlan[d]ó**: a dark blot covers the sign.
3. **Row 19 nélk[ü]l**: a dark blot covers the cross; the two dots remain above it.
4. **Stamp row 4 néh[a]**: a pink blot covers the lower part; only the top bar shows.
5. **Row 29 találkozn[i]**: the last row runs into the worn card corner; the i is lost.

Calls that rest on word sense:

6. **h/p sign**: read p in *megkaptam* (rows 2, 4) and *pénz* (rows 15, 19, 22); read h in the rest. The sign alone does not separate them.
7. **Row 10 *hogadja* → fogadja**: the first sign is a clear h/p sign, not the f-cross. *fogadja köszönetemet* is the only sense I can find; this is a writer's error or a wrong sign, not a clean match.
8. **Row 3 *ottobi* → utóbbi** ("the later"): the first sign is the o-loop. Glossed by the following *vagyis keddi*. This is an interpretation of a misspelling; I found no other word.
9. **Row 4 *de e?lfeledtem* → de elfeledtem**: the sign after *de* has two bars and a detached darker stroke below and to the left of them. I read the stroke as an offset third bar, so e. It cannot be shown to belong to the sign. Without it the sign is a, a slip for e. The word is *elfeledtem* in both cases. The former parallels *ades* and *vale* are withdrawn: both are plain e.
10. **Row 17 *merr* → mert**: the sign after r looks like a second F with a hook, not a gamma. **Row 17 *boldodoga* → boldoggá**: the writer repeated *-do-*. The stroke group after *a* is read as m (three strokes) of *mert*; a reading *boldogan* + *e…* was tried and gives no continuation.
11. **Row 18 *köztün* → ösztön** ("instinct"): the two dots over the first o are clear; there is no s before z, and ü stands for ö, as written. The phrase *vak ösztön* is my best reading. Its syntax with *a forró szeretet* is loose.
12. **Row 28, *a Sándor meg ráérek meg foglalkozni***: every sign is read and the verb forms are as written, *ráérek* first person and *foglalkozni* in full. *Sándor* falls across rows 27 and 28. The written *Sándor* has no case ending. *foglalkozni* governs -val/-vel, so I supply *Sándor[ral]*, and I take the second *meg* as *még* ("still"; no accent seen). That gives the idiom *ráérek még foglalkozni*, "I can still do it later, there is no hurry". Both steps are inference. Who Sándor is and what the matter is are not stated.
13. **Dropped endings**, supplied in brackets: *l[együnk]* (row 27 has only a wave), *légy[ünk]* (row 28), *hagy[ja]* (row 26), *Sándor[ral]* (row 28). Reading the lone *l* as the start of *legyünk* is an inference. In *légy* (row 28) the sign marked g? is flatter than the other g signs and could be k by shape; it is read g from context.
14. **Stamp row 6**: the second sign has no visible dot and is close to z. It is read i from *mint én*. The final strokes are read n, with a small extra tick. Stamp row 3: the last sign, read n, has a tick like the h/p sign.
15. **Other writer spellings, as written and normalized**: *csilagom*, *kedi*, *megkoszönni*, *kösznetemet* (ö omitted), *egyetlel* (wave where n is expected), *kel*, *hezgyöze* → pénz győz-e (n omitted), row 8 to 9 *j?eljesite|teni* → teljesíteni (syllable repeated; the first sign is an I-beam with both the foot of j and the top bar of t, most likely a correction between the two, not a plain j for t), row 19–20 *tele|jesülhet* → teljesülhet, row 20 *egyesülesülesünk* → egyesülésünk (repeat), row 22 *azta* → azt a, row 23 *szerezze* → szerezzem (m omitted), row 23 *fefesegeme* → feleségemé (f-cross where l is expected, clear on the card), row 26 *ara* → arra, row 28 *szer?etetel* → szeretettel (single t; the sign marked r? is closer to the gamma than to the F, under the grey portal stamp, so r rests on word sense), stamp *cskolom* → csókolom. In row 27 the second *elöbb* has clear dots; the first has two marks above it that may be dots (marked ö?). In row 12 the writer struck out the last sign, read y (*mily*).
16. **Normalization** (word division, punctuation, accents) is editorial, and the translations follow it.
17. **Date and sender**: the postmark shows Árokszállás and "22"; month and year are not legible. Sender only "Feri". He may be the Feri of HCP1216, and a Sándor also appears there and on HCP1217, but no identification is claimed. The address (*Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás*) is in clear. The picture side has the printed verse *Sokszor úgy szeretnék sírni* ("Often I would so like to cry"), which is not cipher text.

## Review and what changed

An independent Claude Opus 5.5 agent ran the decoder, decoded with its own key table, read all 37 rows from its own crops and compared them with the ledger. Its verdict was REVISE: the key and the overall reading stand, but five signs were misread and one was missing.

- Row 28 was corrected from *ráér és … fog[lal]kozni* to *ráérek … foglalkozni*, with a k and a wave sign restored to the ledger (823 to 824 signs). This changed the subject of the clause. The solver then took *meg* as *még* and supplied *Sándor[ral]*, giving "I can still deal with Sándor later"; that sense is inferred.
- *ades* became *edes* (row 10) and *vale* became *vele* (row 29); both are plain three-bar e. This removed the parallels cited for a slip in row 4, where a detached stroke is now reported and the sign is marked doubtful.
- Dots that had been missed were added: *köztün* (row 18), *köszö|nök* (row 2), *elöbb* (row 27, firm on the second, possible on the first).
- The I-beam sign in row 8, the r of *szeretetel* and the g of *légy* are now flagged as doubtful or sense-based.

The review's open points stay open: the exact meaning of the Sándor clause, the misspellings *hogadja* and *ottobi*, *merr* in row 17, the date and the identity of the sender. The corrected reading was not put through a second review, as the changes affect one clause of the translation and transcription details, not the cipher or the key.
