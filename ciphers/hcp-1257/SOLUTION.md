# HCP1257: Feri to Jolánka Tóth, on a rumour in Jászárokszállás

**Status: complete reading with one unread name (row 27); revised after review 1.** Claude Opus 5.5, 2026-11-01. Solver: Claude Opus 5.5. There is no earlier work on this number. The portal shows *Not solved* and attaches no transcription or solution; no published solution of this card was found.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the Jolánka postcard family. The key was transferred from the finished card HCP1216 (sign classes there) and confirmed on this card; no sign needed a new value. The sender signs Feri, as on HCP1216.

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

"gy" is g + y; "sz" is s + z. Dots over o/u give ö/ü. Acute accents are mostly faint and supplied in normalization.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1257/work/decode_opus.py
```

It checks the SHA-256 of the two source scans and the two hi-res originals, decodes `work/ledger-opus.txt` (one token per written sign: 30 main rows, 8 rows under the stamp) with the key, and prints the literal rows and then `work/normalized-opus.txt`. The ledger is a manual transcription from enlarged crops of the hi-res address side (`work/crop.py`, `crop2.py`, `z.py`, output in `work/crops/`).

## Layout of the card

Rows 1 to 26 fill the left half. Rows 27 to 30 run on under the printed address line to the right edge. Rows S1 to S8 are under the stamp, which has come away and left them partly as an offset. They run on from the message end, not from row 26.

## Literal decipherment (as printed by the command)

```
01 szeretetedesjolankamen           16 gaedesemegesznyugodt
02 belatomhogykellemetlen           17 enbennemnemcsalodiksoha
03 lehetetmaganakmikorazt           18 mertmihejttehetsegeslesz
04 mondjavalakihogymastbol          19 egybekelesünnekköltsegeit
05 dogitoknemmagatedesemazt         20 megszereznirötönfelese
06 tanacsolommaganakhogy            21 gemeteszembarnarholnah
07 csakaztmonjanekihogysza          22 volnaedesemsorarötön
08 badazuth{i}gyjeelnemszerez       23 valaszolokcsakbel{i}egettu
09 nekikannyiörömetmintha           24 d{y?}nehezenszerezniedesjo
10 aztlatjakmagan{blot}hogyfajdal   25 lankammegazakerehateheti
11 matok{o}ztakmaganakvele{e}n      26 gyarabanirjonarolaferfi
12 iscsakaztmondomhogybol           S1-S4 csoko{l} lomsza mtalan szorima
13 dogemberakielhoditja             S5-S8 [d]ojaferi gondol jonneh{a} ram
14 muszajeztudmindenki{n}ek
15 hogymiterzeklegyenma
27 rölamikororakarirhatenfelkennemvagyokhagujtsesmo{646}za
28 rnevetekezbeeztaraga{l}matakoregeszarokszalastudjacsak
29 aztszeretnemtudnimertragodnakmindenrajtamtalanmagajob
30 bantudjasoraitvarvamardog{i}madojaferi
```

## Hungarian (normalized)

Szeretet[t] édes Jolánkám! Én belátom, hogy kellemetlen lehetett magának, mikor azt mondja valaki, hogy mást boldogítok, nem magát, édesem. Azt tanácsolom magának, hogy csak azt mondja neki, hogy szabad az út. Higgye el, nem szerez nekik annyi örömet, mintha azt látják magán, hogy fájdalmat okoztak magának. Vele én is csak azt mondom, hogy boldog ember, aki elhódítja. Muszáj ezt tud[nia] mindenkinek, hogy mit érzek. Legyen maga, édesem, egész nyugodt, énbennem nem csalódik soha, mert mihelyt tehetséges lesz egybekelésünknek költségeit megszerezni, rögtön feleségemmé teszem. Bár már holnap volna! Édesem, sora[ira] rögtön válaszolok, csak bélyeget tud[o]k nehezen szerezni, édes Jolánkám. Még az a kérés[em], ha teheti, gya[k]rab[b]an írjon arról a férfiről, amikor akar írhat. Én féltékeny nem vagyok. Ha {Gujtsesmoza}rné vette kezébe ezt a rágalmat, akkor egész Árokszállás tudja, csak azt szeretném tudni, mért rágódnak minden[en] rajtam, talán maga jobban tudja. Sorait várva mar[a]dok imádója Feri.

Under the stamp: Csókolom számtalanszor. Imá[d]ója Feri. Gondoljon néha rám.

In clear, right edge: Tisztelem Bélit és kedves mamáját.

## English

My beloved sweet Jolánka! I see that it must have been unpleasant for you when someone says that I make another woman happy and not you, my darling. I advise you to tell him only that the road is free. Believe me, it will not give them as much joy as if they see on you that they have caused you pain. I too say to him only that happy is the man who wins you. Everyone must know what I feel. Be quite calm, my darling: you will never be disappointed in me, because as soon as it is possible to raise the costs of our wedding, I shall make you my wife at once. If only it were tomorrow already! Darling, I answer your lines at once, only stamps are hard for me to get, sweet Jolánka. One more request: if you can, write more often about that man; you can write when you like. I am not jealous. If Mrs {Gujtsesmoza-r} has taken this slander in hand, then all of Árokszállás knows it. I would only like to know why they gnaw at everything about me; perhaps you know better. Awaiting your lines I remain your adorer, Feri.

Under the stamp: I kiss you countless times. Your adorer, Feri. Think of me sometimes.

Right edge, in clear: My respects to Béli and to your dear mother.

## Slovak

Moja milovaná sladká Jolánka! Chápem, že Vám muselo byť nepríjemné, keď niekto hovorí, že robím šťastnou inú, nie Vás, drahá. Radím Vám, aby ste mu povedali len to, že cesta je voľná. Verte mi, neurobí im to takú radosť, ako keby na Vás videli, že Vám spôsobili bolesť. Aj ja mu hovorím len toľko, že šťastný je muž, ktorý si Vás získa. Každý musí vedieť, čo cítim. Buďte, drahá, úplne pokojná, vo mne sa nikdy nesklamete, lebo len čo bude možné zaobstarať náklady na našu svadbu, hneď si Vás vezmem za ženu. Keby to bolo už zajtra! Drahá, na Vaše riadky hneď odpovedám, len známky ťažko zháňam, sladká Jolánka. Ešte mám prosbu, ak môžete, píšte častejšie o tom mužovi, môžete písať, kedy chcete. Ja nie som žiarlivý. Ak túto ohováračku vzala do rúk pani {Gujtsesmoza-r}, potom to vie celý Árokszállás. Chcel by som len vedieť, prečo sa vŕtajú vo všetkom, čo sa ma týka, možno to Vy viete lepšie. V očakávaní Vašich riadkov zostávam Váš ctiteľ Feri.

Pod známkou: Bozkávam Vás nespočetnekrát. Váš ctiteľ Feri. Myslite niekedy na mňa.

Pravý okraj, nešifrovane: Moja úcta Bélimu a Vašej milej mame.

## Not enciphered

Address, in clear: *Szépreményű / Tóth Jolánka / úrleánynak / Jász Árokszállás*. Right edge, in clear cursive, as above; the pen wrote something close to *tisztelen*, normalized *tisztelem*, and *mamáját* curls up the corner with its end cramped. Béli is not identified. Picture side: printed Hungarian verse only (*Repülj, repülj kis madárkám…*), no cipher. The postmarks are not legible enough to give a date; I claim none.

## Uncertainties

Residual point, isolated in a sentence that reads:

1. **Row 27 the name** `gujtsesmo{646}za` + `rné`: a woman's married name in -né. It is reported literally and is not identified; the division is mine, and *Gujt… Smozárné* or another split is possible. Three digit-like marks, 6 4 6, in the card's green ink, sit under and after the o, and I cannot tell whether they are a correction, a false start or something else. The sign before them is o; the sign after them is a dark blotted z.

Words emended from sense, each with a stated basis:

2. **Row 8 `h{i}gyjeel`** → *higgye el* ("believe me"). This was unread before review 1 (`hogy jeel`). The second sign is overwritten: a filled body, but with one separate round dot above and an arm to the right (`work/crops/row8-i-compare.jpg`). o never carries a single dot in this hand, and ö has two. So I read i, but the body itself is not legible. The same writer spells `higyjeel` on HCP1247 and `higgyjeel` on HCP1216. This call was made after the review and has not been checked by the reviewer.
3. **Row 26 `gyaraban`** → *gya[k]rab[b]an* ("more often"): all signs clear; a dropped k and a single b, the kind of omission seen in *rötön*. The word is used in this family (HCP1250, 1256, 1308). It is read from sense but needs no other change.

Sign calls that rest on word sense, not on the shape alone:

4. **h/p:** every h/p sign is read from sense, including p in row 21 *holnap* and h in *hogy, mihejt, tehetséges*.
5. **d/n:** the two signs differ in stroke length. *édes* in row 1 (near-equal strokes) and *édesem* are read d from sense.
6. **Row 14 `mindenki{n}ek`:** the n is a joined Lambda-like sign on the printed dividing line, which also looks like v. *mindenkinek* gives the word; *mindenkivek* gives none.
7. **Row 11 `vele{e}n`:** three bars with a stray oblique stroke across them, read e, giving *vele én is*. "Vele" ("with him") is slightly loose for "to him", and this reading rests on sense.
8. **Row 11 `ok{o}ztak`:** k and the following o are crowded and overwritten; only a small hooked stroke stands for o.
9. **Row 28 `raga{l}mat`:** a washed-out Y-shaped remnant; the shape alone does not give l, and the dot under it is the accent of *mért* in row 29. Read l from sense only.
10. **Row 21 `nar`:** *már* is written with only two strokes (n), a slip or an m short of a stroke. Normalized *már*.
11. **Row 24 `d{y?}`:** the sign after d has the hook of y but no crossing, and may be an unclosed o. Normalized *tud[o]k*. The k is not on the card.
12. **Row 30 `mardog{i}`:** the sign read g has a straight tail, like g and unlike this hand's k; normalized *mar[a]dok*, with the a omitted by the writer. The i of *imádója* lies under a brown stain, with its dot and right arm visible.
13. **Under the stamp:** the rows are an offset and partly faint. **S5 [d] is a restoration**: the sign is physically hidden at the torn stamp edge and only d makes *imádója*. S1 final l and S7 final a are very faint. S1 ends in l and S2 begins with l, so *csókolom* has a doubled l or a misread faint sign at the end of S1.
14. **Row 10:** an ink blot between *magán* and *hogy*, taken as having no letter value. It may hide a cancelled sign; the sentence is complete without it.
15. **Row 23 `bel{i}eget`:** the top of the sign lies on a stain and no separate dot can be seen. The bottom loop favours i over y. It makes no difference to *bélyeget*.
16. **Row 7 `monja`:** one two-stroke sign between o and j, read n by stroke length; *mondja* is the normalized form.

Writer's spellings normalized: *szeretet* → szeretet[t], *lehetet* → lehetett, *ezt ud* → ezt tud[nia] (one t, ending dropped), *miterzek* → mit érzek, *monja* → mondja, *higyjeel* → higgye el, *gyaraban* → gya[k]rab[b]an, *mihejt* → mihelyt, *egybekelésünnek* → egybekelésünknek, *rötön* → rögtön (g absent, twice), *gemé* → feleségemmé, *sora* → sora[ira] (or *sorá[ra]*), *bélieget* → bélyeget, *kére* → kérés[em], *arola* → arról a, *ferfi|röl* → férfiről, *felkennem* → féltékeny nem (the card has `felkennem`; *té* and *y* are missing, an interpretation), *amikor or akar* → amikor akar (repeat), *vete* → vette, *akor* → akkor, *rágodnak* → rágódnak.

## Why it is correct

- One known family key, unchanged, turns 38 rows of sign into continuous Hungarian with no gap in the message; words run across row breaks (*bol|dogítok*, *ma|ga*, *fájdal|mat*, *feleségem|é*, *job|ban*, *Jo|lánkám*).
- The text is specific and coherent: a rumour, advice on answering it, the promise of marriage, the shortage of stamps, a local slander, and the place *Árokszállás*, which matches the address on the card.
- The formulas match the family: *gondoljon néha rám* (HCP1254, 1216, 1217), the sender Feri, the formal address.
- The whole of the ciphertext is covered, including the rows under the address line and under the stamp.

## Response to review 1

Verdict REVISE. I checked each finding on the reviewer's crops and accept findings 1 to 7. I took up the suggestion in finding 8 and went further. `python3 -I ciphers/hcp-1257/work/decode_opus.py` was re-run after the changes: all four hashes OK, 38 rows, 819 tokens, every token has a value, and the literal block and Hungarian above match its output.

1. **Row 26 `gyaraban`: fixed.** `r26b.jpg` shows two bars after g y, the same as the a after F; the two dots below are the ö of row 27. Ledger, literal row and uncertainty 3 corrected. The text now prints *gya[k]rab[b]an*; *gyorsabban* is dropped.
2. **Row 5 `magat`: fixed.** Two bars with an accent tick after g. *magét* removed from the spellings.
3. **Row 15 one t: fixed.** m, i, one gamma, accented three bars, F, z. *mitterzek* removed.
4. **Row 7 `monja`: fixed.** One two-stroke sign between o and j. Ledger is now `M O N J A`; added to the spellings and to uncertainty 16.
5. **Normalized forms: fixed.** *Szeretet[t]*, *férfiről*, *sora[ira]*.
6. **Row 28 sign description: fixed** in uncertainty 9.
7. **Row 23 sign: listed** as uncertainty 15, and marked `I?` in the ledger.
8. **Row 8: taken further; changes the reading.** The reviewer proposed `je|el`. On 8x enlargement the sign after h in `hogyjeel` is a filled body with one separate dot and a right arm (`work/crops/row8-i-compare.jpg`, with the clear i and ö of row 9 beside it). That gives `higyjeel`, *higgye el*, the writer's own spelling on HCP1247. The clause now reads *…szabad az út. Higgye el, nem szerez nekik annyi örömet…* The previous "hogy {jeel}" is withdrawn. The call depends on the dot, not on the filled body, and the reviewer has not seen it.

**Further re-check, as the reviewer asked (the ledger had been filled partly from expected words).** I re-read all 30 rows on the reviewer's 2x crops, and rows 6 to 8 and 29 closer up. One more error turned up: **row 29 is `talan`, not `talen`** (`work/crops/row29-talan.jpg`: two bars after l). *talen* is removed from the spellings; this is also new since the review. Stroke runs were re-counted (row 6 *tanácsolom magának* has six strokes for m m; row 9 *annyi*; row 17 *bennem nem*; row 19 *ünnek*) and agree with the ledger. The limit the reviewer stated still applies: outside the detail crops, one further stroke-level slip in an ordinary row cannot be excluded.

The reading is not substantially changed: six signs corrected in the ledger (two of them removed) and one further sign flagged, one formerly unread word now resolved, and the sense of the letter otherwise as reviewed. So I finish without a second round, and the two post-review calls (rows 8 and 29) are stated as such here and in the report.
