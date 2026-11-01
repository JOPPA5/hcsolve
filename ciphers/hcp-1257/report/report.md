# HCP 1257 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-69): Feri to Jolánka Tóth, on a rumour in Jászárokszállás

Human solver: Tomáš Pavuk

**Status: complete reading with one unread name (row 27); independent review 1 verdict REVISE, all findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1257 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1257), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-69, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was found. There was no earlier work on this number.

The picture side is a tinted photograph of a man and a woman seated apart, with a dove flying between them, and a printed Hungarian verse (Repülj, repülj kis madárkám…). It has no cipher text. The whole message is on the address side, in green ink and invented signs. Rows 1 to 26 fill the left half, and rows 27 to 30 run on under the printed address line to the right edge. Eight short rows (S1 to S8) lie under the stamp, which has come away and left them partly as an offset; they continue from the end of the message, not from row 26. The address is in clear: Szépreményű / Tóth Jolánka / úrleánynak / Jász Árokszállás. So is one line of cursive along the right edge. The postmarks show only fragments, so this report claims no date.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the clear address and the right-edge line (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth in Jászárokszállás, several of which are deciphered in this repository (for example HCP 1216, 1217, 1243, 1247, 1301). They share one key, and this card is signed Feri, as HCP 1216 is. It was therefore read with a **known, transferred key**, not by a new key recovery.

## Method

- **Key.** The sign classes and values were taken unchanged from the finished card HCP 1216. No sign on this card needed a new value.
- **Transcription.** Every row was read manually (no OCR) from enlarged crops of the un-converted original of the address side, and recorded in a sign ledger with one token per written sign (`work/ledger-opus.txt`): 38 rows, 819 tokens. The transcription is not blind, because the writer's formulas were known from the family.
- **Decoding.** One command checks the SHA-256 of the scans, decodes the ledger with the key, and prints the literal rows and the normalized text: `python3 -I ciphers/hcp-1257/work/decode_opus.py`
- **Review.** A separate Claude Opus 5.5 agent re-ran the command, wrote its own decoder from HCP 1301's key file, and got the same output on all rows. It then compared the ledger with its own crops of the card (see the review section below).

The writer spells phonetically and carelessly: he drops letters, writes no visible accents on many vowels and sometimes repeats a syllable. The literal decipherment is kept as written, and the normalized Hungarian is editorial. In it, [square brackets] mark letters not on the card, and {braces} mark what is not understood.

## Key

Simple monoalphabetic substitution of Hungarian with invented graphic signs. The labels are conventional names for the handwritten shapes.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S, or closed loop) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl (only with right bowl) | cs | three short strokes | m | gamma/corner | t |
| short tick + long stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | long stroke + short tick to the right | h / p | hooked long sign | y |
| hooked descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | | | | |

"gy" is g + y, and "sz" is s + z. Dots over o and u give ö and ü. Acute accents are mostly faint and are supplied in normalization. The h and p sign is one near-homograph, told apart only by word sense.

## Plaintext

Literal decipherment as printed by the command. `h` stands for the h/p sign, and {..} marks a sign discussed below.

```text
01 szeretetedesjolankamen
02 belatomhogykellemetlen
03 lehetetmaganakmikorazt
04 mondjavalakihogymastbol
05 dogitoknemmagatedesemazt
06 tanacsolommaganakhogy
07 csakaztmonjanekihogysza
08 badazuth{i}gyjeelnemszerez
09 nekikannyiörömetmintha
10 aztlatjakmagan{blot}hogyfajdal
11 matok{o}ztakmaganakvele{e}n
12 iscsakaztmondomhogybol
13 dogemberakielhoditja
14 muszajeztudmindenki{n}ek
15 hogymiterzeklegyenma
16 gaedesemegesznyugodt
17 enbennemnemcsalodiksoha
18 mertmihejttehetsegeslesz
19 egybekelesünnekköltsegeit
20 megszereznirötönfelese
21 gemeteszembarnarholnah
22 volnaedesemsorarötön
23 valaszolokcsakbel{i}egettu
24 d{y?}nehezenszerezniedesjo
25 lankammegazakerehateheti
26 gyarabanirjonarolaferfi
27 rölamikororakarirhatenfelkennemvagyokhagujtsesmo{646}za
28 rnevetekezbeeztaraga{l}matakoregeszarokszalastudjacsak
29 aztszeretnemtudnimertragodnakmindenrajtamtalanmagajob
30 bantudjasoraitvarvamardog{i}madojaferi
S1 csoko{l}      S2 lomsza     S3 mtalan    S4 szorima
S5 [d]ojaferi   S6 gondol     S7 jonneh{a} S8 ram
```

### Hungarian (normalized)

Szeretet[t] édes Jolánkám! Én belátom, hogy kellemetlen lehetett magának, mikor azt mondja valaki, hogy mást boldogítok, nem magát, édesem. Azt tanácsolom magának, hogy csak azt mondja neki, hogy szabad az út. Higgye el, nem szerez nekik annyi örömet, mintha azt látják magán, hogy fájdalmat okoztak magának. Vele én is csak azt mondom, hogy boldog ember, aki elhódítja. Muszáj ezt tud[nia] mindenkinek, hogy mit érzek. Legyen maga, édesem, egész nyugodt, énbennem nem csalódik soha, mert mihelyt tehetséges lesz egybekelésünknek költségeit megszerezni, rögtön feleségemmé teszem. Bár már holnap volna! Édesem, sora[ira] rögtön válaszolok, csak bélyeget tud[o]k nehezen szerezni, édes Jolánkám. Még az a kérés[em], ha teheti, gya[k]rab[b]an írjon arról a férfiről, amikor akar írhat. Én féltékeny nem vagyok. Ha {Gujtsesmoza}rné vette kezébe ezt a rágalmat, akkor egész Árokszállás tudja, csak azt szeretném tudni, mért rágódnak minden[en] rajtam, talán maga jobban tudja. Sorait várva mar[a]dok imádója Feri.

Under the stamp: Csókolom számtalanszor. Imá[d]ója Feri. Gondoljon néha rám.

Right edge, in clear: Tisztelem Bélit és kedves mamáját.

### English

My beloved sweet Jolánka! I see that it must have been unpleasant for you when someone says that I make another woman happy and not you, my darling. I advise you to tell him only that the road is free. Believe me, it will not give them as much joy as if they see on you that they have caused you pain. I too say to him only that happy is the man who wins you. Everyone must know what I feel. Be quite calm, my darling: you will never be disappointed in me, because as soon as it is possible to raise the costs of our wedding, I shall make you my wife at once. If only it were tomorrow already! Darling, I answer your lines at once, only stamps are hard for me to get, sweet Jolánka. One more request: if you can, write more often about that man; you can write when you like. I am not jealous. If Mrs {Gujtsesmoza-r} has taken this slander in hand, then all of Árokszállás knows it. I would only like to know why they gnaw at everything about me; perhaps you know better. Awaiting your lines I remain your adorer, Feri.

Under the stamp: I kiss you countless times. Your adorer, Feri. Think of me sometimes.

Right edge, in clear: My respects to Béli and to your dear mother.

### Slovak

Moja milovaná sladká Jolánka! Chápem, že Vám muselo byť nepríjemné, keď niekto hovorí, že robím šťastnou inú, nie Vás, drahá. Radím Vám, aby ste mu povedali len to, že cesta je voľná. Verte mi, neurobí im to takú radosť, ako keby na Vás videli, že Vám spôsobili bolesť. Aj ja mu hovorím len toľko, že šťastný je muž, ktorý si Vás získa. Každý musí vedieť, čo cítim. Buďte, drahá, úplne pokojná, vo mne sa nikdy nesklamete, lebo len čo bude možné zaobstarať náklady na našu svadbu, hneď si Vás vezmem za ženu. Keby to bolo už zajtra! Drahá, na Vaše riadky hneď odpovedám, len známky ťažko zháňam, sladká Jolánka. Ešte mám prosbu, ak môžete, píšte častejšie o tom mužovi, môžete písať, kedy chcete. Ja nie som žiarlivý. Ak túto ohováračku vzala do rúk pani {Gujtsesmoza-r}, potom to vie celý Árokszállás. Chcel by som len vedieť, prečo sa vŕtajú vo všetkom, čo sa ma týka, možno to Vy viete lepšie. V očakávaní Vašich riadkov zostávam Váš ctiteľ Feri.

Pod známkou: Bozkávam Vás nespočetnekrát. Váš ctiteľ Feri. Myslite niekedy na mňa.

Pravý okraj, nešifrovane: Moja úcta Bélimu a Vašej milej mame.

## What remains uncertain

- **Row 27, the name (unread).** `gujtsesmo{646}za` + `rné` is a woman's married name in -né. It is reported literally and not identified, and the division is editorial. Three digit-like marks, 6 4 6, in the card's green ink, stand under and after the o, and their purpose is unknown. This is the only item on the card not understood. The sentence around it reads.
- **Row 8, higgye el.** The second sign is overwritten: a filled body with one separate dot above and an arm to the right. o never carries a single dot in this hand, so it is read i, and the word agrees with the same writer's `higyjeel` on HCP 1247. The body itself is not legible. This call was made after the review and has not been checked by the reviewer.

![Row 8: the overwritten sign after h (upper left), with the clear i and ö of row 9 below it for comparison (work/crops/row8-i-compare.jpg)](../work/crops/row8-i-compare.jpg)

- **Row 26, gya[k]rab[b]an.** All signs are clear, but the word needs a k and a b added. It is read from sense; the word is used elsewhere in this family (HCP 1250, 1256, 1308).
- **Calls that rest on word sense, not shape.** Every h/p sign. The d/n pair in édes. Row 14 n in mindenkinek, a joined Lambda-like sign on the printed line. Row 28 l in rágalmat, a washed-out Y-shaped remnant. Row 11 vele én, three bars with a stray stroke; "vele" is slightly loose for "to him". Row 11 o in okoztak, crowded and overwritten.
- **Single signs.** Row 21 már is written with two strokes (`nar`). Row 24 `d{y?}` has a hook but no crossing, normalized tud[o]k. Row 30 mar[a]dok has a g-like sign and a missing a; the i of imádója lies under a stain. Row 23 i in bélyeget has its top on a stain. Row 10 has an ink blot taken as having no letter value.
- **Under the stamp.** S5 [d] is a true restoration: the sign is hidden at the torn stamp edge. S1 final l and S7 final a are very faint.
- **Other.** Béli is not identified. The card has no legible date. felkennem → féltékeny nem is an interpretation, because the card lacks té and y. The Hungarian judgment was made by AI agents, and no native speaker has checked it.

## Review and what changed

Independent review 1 (a separate Claude Opus 5.5 agent, verdict **REVISE**) confirmed that the key is right and covers the whole text: its own decoder gave 0 differing rows. It found no blocker. It corrected the ledger on the pixels:

- Row 26 is `gyaraban`, not `gyeraban`, so gyakrabban needs only a dropped k and a single b. This was the one major finding.
- Row 5 is `magat`, not `maget`.
- Row 15 has one t, not two.
- Row 7 is `monja`, with one sign fewer than `mondja`.
- Three normalized forms were corrected: Szeretet[t], férfiről, sora[ira].
- The description of the row 28 sign was corrected, and the row 23 sign was listed as uncertain.

All of these were accepted after checking the crops. Two further changes came from the solver's response and have **not** been through review:

- The reviewer noted that `jeel` might relate to higgye el on HCP 1216. Closer inspection of the row 8 sign led to the reading higgye el described above, replacing the unread `hogy {jeel}`.
- The reviewer warned that the ledger had been filled partly from expected words, so all rows were re-read. That found row 29 `talan`, not `talen`.

These amount to six signs corrected in the ledger (two removed) and one flagged. The sense of the letter did not change, apart from one formerly unread word in row 8. No second review round was run.
