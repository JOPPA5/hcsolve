# HCP 1247 (cpc_1913-09-19_HU__HU_Jasz Arokszalas_jolanka-44): a love letter to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered with two small gaps. All 26 main rows and the right-edge continuation read as connected Hungarian, except one overwritten word in row 19. The note under the stamp is read except the start of one word and its end, which runs under old tape. Independent review 1 verdict REVISE; all ten findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1247 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1247), portal name cpc_1913-09-19_HU__HU_Jasz Arokszalas_jolanka-44, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language unknown, sender unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card turned up, and the AI Decipherment Register had no record of it on that date. The date 1913-09-19 comes from the portal file name; the postmarks are only partly legible.

The picture side is a tinted photograph of a couple with the printed title Oh csak még egyszer összejönnénk… ("Oh, if only we could meet once more…") and a four-line printed verse. It has no cipher and no handwriting.

The whole message is on the address side, in purple pencil and invented signs. It runs in rows across the left half, along the bottom edge to the right corner, up the right edge, and ends in the box under a stamp that was torn away, where old tape now hides the last signs. The address is in plain writing: Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás ("To the fair-promising Miss Jolánka Tóth"). The first word is written across the postmark and is read with the help of the same formula on HCP 1245, 1251 and 1252. A boxed mark RÁKOSPALOTA-Ú… (cut off at the stamp) and a round JÁSZÁROKSZÁLLÁS postmark are visible. HCP 1216 carries Rákospalota too, which suggests the writer lived near Budapest; he does not name himself in what is visible, and no identification is claimed.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the plain address, the postmarks and the remains of the stamp (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth, many of which are deciphered in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery. The plaintext is new.

## Method

There was no earlier work on this number; all of it was done on 2026-11-01 by Claude Opus 5.5. The key was taken unchanged from HCP 1216. The work was a careful manual transcription, without OCR. The un-converted high-resolution scan of the address side was sheared by about 0.045 so that the rows lie level, then cropped and enlarged 2–5×. A blue-minus-green channel separated the purple pencil from the grey collection stamp on the bottom rows. Every written sign was recorded in a ledger, one token per sign (`work/ledger.txt`, 690 tokens, 679 of them letters), and a short script decodes the ledger and checks the hashes of the images:

```text
python3 -I ciphers/hcp-1247/work/decode.py
```

The writer spells by ear: he loses double consonants (menyit for mennyit, akor for akkor) and marks few accents. The literal decipherment keeps this; the normalized Hungarian is editorial.

## Key

Cipher type: MASC + Steganography (updated 2026-11-03). Hungarian simple monoalphabetic substitution with invented signs, with a further cipher note hidden in the stamp box under the stamp. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma / corner | t |
| short stroke left + long right | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | long stroke left + short right | h / p | low descender | y |
| descending open curve | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | opposed bowls | cs | | |

One sign serves for both h and p. On this card gy is written as two signs, g then y. Dots over o and u give ö, ő, ü and ű. "50 K." is in plain digits and letter (K for korona).

## Plaintext

Literal decipherment, row by row (`?` = unread, square brackets = hidden sign restored):

```
01 szeretetedesjolankamegyet         14 tiencsakugymentemvol
02 lenremenyemneharagudjon           15 nahamagavalmulatamvol
03 hogyegyessoraitvalasz             16 namerthamagavalnemtölt
04 nelkülhagytamdenagyonel           17 hetemelakornemerdemes
05 vagyokfoglalvaugyebar             18 költenilegkevesebbale
06 edesemmijengyorsante              19 ke?vagy50k.nabainkablemon
07 likazidögondolomhogy              20 dokarendezösegrölmajd
08 szedcsomolehetsajnalomde          21 hafeljönedesemmagavalmu
09 megegyenlörenemtudommeg           22 lathaakörülmenyekengedik
10 irnihogymagamenyitkül             23 azthiszemmagaisszorakoznijönfelhigyjeeledesem
11 dotmihejraerekrögtön              24 enszeretnemmarlegjobbanhavasutasnevagyjoben
12 öszeolvasomesmegirom.             25 mondazenedeskisfelesegenekmondhatnem.ezt
13 edesemamiamulatsagotile           26 lapotketnapigirtamgondolhatjamenyire
right edge, upwards: elvagyokfogla[l]va
under the stamp: [i][s]ten / vele / edesem / ??dig / viszot / lat(tape)
```

Normalized Hungarian:

Szeretett édes Jolánkám! Egyetlen reményem! Ne haragudjon, hogy egyes sorait válasz nélkül hagytam, de nagyon el vagyok foglalva. Ugye bár, édesem, milyen gyorsan telik az idő. Gondolom, hogy szép csomó lehet. Sajnálom, de még egyelőre nem tudom megírni, hogy maga mennyit küldött; mihelyt ráérek, rögtön összeolvasom és megírom. Édesem, ami a mulatságot illeti, én csak úgy mentem volna, ha magával mulattam volna, mert ha magával nem tölthetem el, akkor nem érdemes költeni. Legkevesebb a leke[?] vagy 50 K. Na, ba' inkább lemondok a rendezőségről, majd ha feljön, édesem, magával mulat[ok], ha a körülmények engedik. Azt hiszem, maga is szórakozni jön fel, higgye el, édesem. Én szeretném már legjobban, ha vasutasné, vagy jobban mondva az én édes kis feleségének mondhatnám. Ezt [a] lapot két napig írtam, gondolhatja, mennyire el vagyok fog[l]alva.

Under the stamp: [Is]ten vele, édesem! […]dig viszo[n]tlát[ásra] (runs under the tape).

English translation:

Beloved sweet Jolánka! My only hope! Do not be angry that I left some of your lines without an answer, but I am very busy. Isn't it so, my sweet, how fast time passes. I suppose there must be a fair pile by now. I am sorry, but for the moment I cannot write how much (or how many) you have sent; as soon as I have time I will count it all up at once and write. My sweet, as for the ball, I would only have gone if I had been enjoying myself with you, because if I cannot spend it with you, then it is not worth spending. The least [one uncertain word] about 50 K. Well, I would rather give up being on the organizing committee; when you come up, my sweet, I will enjoy myself with you, if circumstances allow. I think you too are coming up to have some fun, believe me, my sweet. What I would like most is to be able to call you a railwayman's wife, or rather to say this to my sweet little wife. It took me two days to write this card, you can imagine how busy I am.

Under the stamp: God be with you, my sweet! […]-dig (word only partly read) until we meet again.

Slovak translation:

Milovaná sladká Jolánka! Moja jediná nádej! Nehnevajte sa, že som niektoré Vaše riadky nechal bez odpovede, ale som veľmi zaneprázdnený. Však áno, moja sladká, ako rýchlo letí čas. Myslím, že už to bude pekná kôpka. Ľutujem, ale zatiaľ neviem napísať, koľko ste poslali; len čo budem mať čas, hneď to všetko spočítam a napíšem. Moja sladká, čo sa týka zábavy, išiel by som len vtedy, keby som sa zabával s Vami, lebo ak to nemôžem stráviť s Vami, potom sa neoplatí míňať. Najmenej [jedno neisté slovo] asi 50 K. Nuž, radšej sa vzdám miesta v usporiadateľskom výbore; keď prídete hore, moja sladká, budem sa zabávať s Vami, ak to okolnosti dovolia. Myslím, že aj Vy prídete hore zabaviť sa, verte mi, moja sladká. Najradšej by som chcel, aby som to mohol povedať železničiarovej manželke, alebo lepšie povedané mojej sladkej malej žienke. Túto pohľadnicu som písal dva dni, môžete si predstaviť, ako som zaneprázdnený.

Pod známkou: S Bohom, moja sladká! […]-dig (slovo prečítané len čiastočne) do videnia.

Stamp-box audit (2026-11-03). The original scan was checked again at the stamp box: the stamp is torn away and the cipher note under it (six short rows in the same signs and pencil) was re-read from the pixels. The reading above is confirmed without change: [Is]ten vele, édesem! […]dig viszo[n]tlát[ásra] — "God be with you, my sweet! […]-dig, until we meet again." No plain Hungarian is written under the stamp. Because a message is hidden under the stamp, the register type is MASC + Steganography.

## What remains uncertain

- **Row 18–19, one word.** The literal is a le|ke[?]: section mark k, three bars e, then a blot of at least two overwritten signs (a z-cross over something F-like is possible). A form of kerül ("costs, comes to") is possible but not claimed. The sense "about 50 K" rests on the digits.
- **Under the stamp, row B4.** The word ends -dig (d, i, g). Its first signs, a crossed curve with an arm and an arched loop, are not assigned. Addig or mindig come to mind, but the visible signs do not give them, so neither is adopted.
- **End of the note.** Rows B5–B6 read viszot / lat…, then the tape begins. Viszontlátásra is an inference from those letters, and a signature may lie hidden.
- **Restored signs.** Is- of Isten (hidden by the stamp fragment, restored from the family's formula) and the l of foglalva on the right edge (under the perforation).
- **Row 8, szép csomó.** The pixels show the d shape, literal szed; szép is a reading on word sense, as a slip. What the "fair pile" is, is not stated. It may be money, or cards and letters she has sent.
- **Row 25.** The case does not agree: vasutasné is nominative, feleségének dative. "To be able to call you" in the English smooths this. Mond az is normalized to mondva az, and mondhatnem to mondhatnám.
- **Row 19, ba'.** Literal na ba inkább; taken as a shortened bár.
- **Row 17.** The middle bar of the e in hetem is lost in a rust stain; the spacing fits three bars.
- **Rows 21–22, mulat[ok].** The ending is not written. The article in Ezt [a] lapot is supplied.
- Word division, punctuation and most accents are editorial. The choice between h and p rests on word sense.

## Review

A separate Claude Opus 5.5 agent reviewed the solution. It re-ran the command, compared the key with HCP 1216, and read all 26 rows in its own sign codes from its own crops (not blind, since it had seen the solver's text). Twenty-two rows agreed sign for sign. The verdict was **REVISE**, with one major and nine minor findings, none overturning the message. All were checked on the scans and accepted:

- **Row 19:** the first sign is k, not s, so the earlier reading lesz ("will be") was withdrawn and the word is now marked uncertain.
- **Row 20:** a dropped d was restored; the writer spelled majd in full.
- **Under the stamp:** B3 is edesem, not edesam. B4 was partly read as -dig; its "point" was part of a d.
- **Row 17** is hetem, needing no emendation. **Row 8** has the d shape, which is now stated, and the key table now separates d from h/p.
- **"The money"** was removed as a stated fact; the text does not say what she sent.
- Corrections to the supporting claims: maga, not Ön, as the address; three, not four, mulat- forms; g and y as separate signs. Mondhatnem is now disclosed as normalized, and the plain text on the card is described.

The reviewer could not check what lies under the tape, the date, or the overwritten sign, and it did no independent web search for a published solution.
