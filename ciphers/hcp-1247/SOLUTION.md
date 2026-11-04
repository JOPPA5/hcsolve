# HCP1247 — to Jolánka Tóth: too busy to reply, the ball, "my sweet little wife"

**Status: main message and right-edge continuation read, with one uncertain word in row 19 (overwritten by the writer); the under-stamp note is read except the start of one word and its end, which runs under the tape.** Solved by Claude Opus 5.5, 2026-11-01. There was no earlier work on this number. The portal shows *Not solved*, with no transcription or solution attached, and no published solution of this card turned up. The key is the existing Jolánka-family key from the finished cards (hcp-1216 and others); the plaintext is new.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka postcard family, MASC).

*Type note (2026-11-03):* the register type is now **MASC + Steganography**, because a cipher message is hidden in the stamp box under the (now torn-away) stamp; see the section "Stamp-box message (2026-11-03)". The key is transferred unchanged from `ciphers/hcp-1216/SOLUTION.md`:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| short stroke left + long stroke right | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | long stroke left + short right (one shape) | h, p | low descender | y |
| descending open curve | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | — | — | opposed bowls | cs |

On this card gy is written as two signs, g then y. Dots over o/u give ö, ő, ü, ű. Other accents are mostly unmarked and are supplied in normalization. "50 K." is written in plain digits and letter.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1247/work/decode.py
```

It checks the SHA-256 of the four image files, decodes `work/ledger.txt` (one token per written sign, corrected after review 1, a manual transcription made from enlarged crops of the hi-res address side) and prints the normalized text `work/normalized.txt`.

## Literal decipherment (as printed by the command)

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

## Hungarian (normalized)

Szeretett édes Jolánkám! Egyetlen reményem! Ne haragudjon, hogy egyes sorait válasz nélkül hagytam, de nagyon el vagyok foglalva. Ugye bár, édesem, milyen gyorsan telik az idő. Gondolom, hogy szép csomó lehet. Sajnálom, de még egyelőre nem tudom megírni, hogy maga mennyit küldött; mihelyt ráérek, rögtön összeolvasom és megírom. Édesem, ami a mulatságot illeti, én csak úgy mentem volna, ha magával mulattam volna, mert ha magával nem tölthetem el, akkor nem érdemes költeni. Legkevesebb a leke[?] vagy 50 K. Na, ba' inkább lemondok a rendezőségről, majd ha feljön, édesem, magával mulat[ok], ha a körülmények engedik. Azt hiszem, maga is szórakozni jön fel, higgye el, édesem. Én szeretném már legjobban, ha vasutasné, vagy jobban mondva az én édes kis feleségének mondhatnám. Ezt [a] lapot két napig írtam, gondolhatja, mennyire el vagyok fog[l]alva.

Under the stamp: [Is]ten vele, édesem! […]dig viszo[n]tlát[ásra] (runs under the tape).

## English

Beloved sweet Jolánka! My only hope! Do not be angry that I left some of your lines without an answer, but I am very busy. Isn't it so, my sweet, how fast time passes. I suppose there must be a fair pile by now. I am sorry, but for the moment I cannot write how much (or how many) you have sent; as soon as I have time I will count it all up at once and write. My sweet, as for the ball, I would only have gone if I had been enjoying myself with you, because if I cannot spend it with you, then it is not worth spending. The least [one uncertain word] about 50 K. Well, I would rather give up being on the organizing committee; when you come up, my sweet, I will enjoy myself with you, if circumstances allow. I think you too are coming up to have some fun, believe me, my sweet. What I would like most is to be able to call you a railwayman's wife, or rather to say this to my sweet little wife. It took me two days to write this card, you can imagine how busy I am.

Under the stamp: God be with you, my sweet! […]-dig (word only partly read) until we meet again.

## Slovenčina

Milovaná sladká Jolánka! Moja jediná nádej! Nehnevajte sa, že som niektoré Vaše riadky nechal bez odpovede, ale som veľmi zaneprázdnený. Však áno, moja sladká, ako rýchlo letí čas. Myslím, že už to bude pekná kôpka. Ľutujem, ale zatiaľ neviem napísať, koľko ste poslali; len čo budem mať čas, hneď to všetko spočítam a napíšem. Moja sladká, čo sa týka zábavy, išiel by som len vtedy, keby som sa zabával s Vami, lebo ak to nemôžem stráviť s Vami, potom sa neoplatí míňať. Najmenej [jedno neisté slovo] asi 50 K. Nuž, radšej sa vzdám miesta v usporiadateľskom výbore; keď prídete hore, moja sladká, budem sa zabávať s Vami, ak to okolnosti dovolia. Myslím, že aj Vy prídete hore zabaviť sa, verte mi, moja sladká. Najradšej by som chcel, aby som to mohol povedať železničiarovej manželke, alebo lepšie povedané mojej sladkej malej žienke. Túto pohľadnicu som písal dva dni, môžete si predstaviť, ako som zaneprázdnený.

Pod známkou: S Bohom, moja sladká! […]-dig (slovo prečítané len čiastočne) do videnia.

## Plain text on the card (not cipher)

Address side: *Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás* ("To the fair-promising Miss Jolánka Tóth"), in the same purple pencil; the first word is written across the postmark and is read with the help of the same formula on HCP1245, 1251 and 1252. Boxed mark *RÁKOSPALOTA-Ú…* (cut off at the stamp), as on HCP1216, which gives the writer's likely area, near Budapest, and fits *feljön* ("comes up") and *vasutasné*; that is an inference, and no identification is claimed. Round postmark *JÁSZÁROKSZÁLLÁS*, only partly legible. Picture side: a tinted photograph of a couple, printed title *Oh csak még egyszer összejönnénk…* ("Oh, if only we could meet once more…") and a four-line printed verse, Hungarian print, no cipher and no handwriting.

## Stamp-box message (2026-11-03)

Audit on 2026-11-03 of the original hi-res address side (`work/hires/…_adr.jpg`, crops in `work/stamp-2026-11-03/`, made by `crop.py` there). The stamp is **lifted (torn away) with writing under it**: only a strip of the green stamp at the left edge of the box and a corner under old tape at bottom right remain. The hidden note is written in the **cipher signs** (same key, same purple pencil), six short rows inside the dotted stamp box; no plain Hungarian is under the stamp. It was already read on 2026-11-01 (rows B1–B6 of `work/ledger.txt`, decoded by the reproduction command); this audit re-read it from the pixels and confirms that reading without change.

- Literal: `[i][s]ten / vele / edesem / ??dig / viszot / lat(tape)`
- Hungarian (normalized): *[Is]ten vele, édesem! […]dig viszo[n]tlát[ásra].*
- English: God be with you, my sweet! […]-dig (one word only partly read), until we meet again.
- Slovak: S Bohom, moja sladká! […]-dig (slovo prečítané len čiastočne), do videnia.

Still unread: the first two signs of B4 (a crossed curve with a right arm, without a visible dot, then an arched loop); they give none of *addig*, *mindig* and the like, so no word is adopted. The end of B6 (*-ásra* and any signature) is under the old tape and cannot be read. *Is-* in B1 stays a disclosed restoration (hidden by the stamp fragment). The stamp-box text is covered by the existing ledger and reproduction script; nothing was added to them.

## What remains uncertain

1. **Under the stamp, row B4: one word only partly read.** Its end is clear: tick + long stroke d, the tailed 2-like i (as in B5 *viszot*), descending g, so *-dig*. Before that stand a crossed curve with a right arm and an arched loop (possibly o), which I cannot assign. The ending suggests *addig*, *mindig* and the like, but the visible first signs do not give any of them, so I adopt none.
2. **Under the stamp, end of the note.** Rows B5 and B6 read *viszot / lat…* (the *n* of *viszont* is not written, or is merged into the loop) and then run into the old tape over the torn stamp. *-ásra* and anything after it, such as a signature, is hidden. The first v in B5 shows only its right stem beside the stamp. *viszontlátásra* is an inference from those visible letters, not a reading of the hidden part.
3. **Restorations of physically hidden signs:** *Is-* of *Isten* (B1: the row starts at the stamp fragment, *Isten vele* being the family's formula) and the *l* of *foglalva* on the right edge (under the stamp perforation; only a trace of purple shows).
4. **Row 25, sentence join.** The literal is *ha vasutasné vagy jobban mond az én édes kis feleségének mondhatném*. The case does not agree (*vasutasné* nominative, *feleségének* dative), so the exact sense is uncertain: "to be able to call you" in the English is a smoothing, and the Slovak follows the literal more closely. *mond az* is normalized to *mondva az*.
5. **Row 8, *szép csomó* ("a fair pile").** The pixels show the d shape (short left, long right), so the literal is *szed*; the h/p shape on this card has the opposite order (*hagytam, lapot, napig*). *szép* is a reading on word sense, as a slip. What the pile is, is not stated: nothing in rows 7–12 says money. It may be money, or cards and letters she has sent (*mennyit küldött*, *összeolvasom*). The 50 K belongs to the ball and is a separate topic.
6. **Row 18–19, one uncertain word.** The first sign of row 19 is the section mark k, as at the start of row 18, not s. The literal is *a le|ke[?]*: the third sign is a blot of at least two overwritten signs (a z-cross over something F-like is possible), then the chevron of *vagy* with an extra foot. A form of *kerül* ("costs, comes to") is worth considering but I do not claim it. The sense "about 50 K" rests on the digits alone. This replaces the earlier *az lesz*.
7. **Row 19, *ba'*.** Literal *na ba inkább*; the b is clear. The expected *na de* does not fit, so I take *ba'* as a shortened *bár*. A stray stroke stands before the *o* of *lemon-dok*.
8. **Row 17, start.** In the rust stain: long stroke with dot companion (h), then bars at the spacing of a three-bar sign with the middle one lost (span about 31 px native against about 19 px for a two-bar a), then a corner. Literal *hetem*, so *töl-t|hetem* needs no emendation; e is probable, not certain.
9. **Row 15.** Literal *mulatam*, with the chevron of *volna* partly written over the last stroke of the m. Normalized *mulattam*.
10. **Row 21–22, *mulat[ok]*.** The ending *-ok* is not written; the literal *mulat* could be a slip. *Ezt [a] lapot*: the article is supplied.
11. **Row 1.** The last sign of the row has a small extra tick and could be taken for r, but *egyet|len* needs t. The m of *Jolánkám* has three strokes, the third set apart.
12. **Row 17, *érdemes*.** The m is blotted by overwriting; the word is clear from context.
13. Other writer spellings normalized: *szeretet* → szeretett, *menyit* → mennyit, *mihej* → mihelyt, *egyenlőre* → egyelőre, *öszeolvasom* → összeolvasom, *ile|ti* → illeti, *higyje el* → higgye el, *joben* → jobban, *fel|esegenek*, *akor* → akkor, *menyire* → mennyire, *mondhatnem* → mondhatnám. Word division, punctuation and most accents are editorial. The h/p shape and the d shape are kept apart on this card; h or p at each h/p sign rests on word sense (*hogy, ne haragudjon, lapot, napig*).
14. The sender is not named in what is visible; 1216's *Feri* uses the same *higgyje el, édesem*, but I claim no identification. The date comes from the portal file name (1913-09-19); only part of the postmark is legible.

## Why it is correct

- The key was not fitted to this card: the unchanged family key turns all 26 rows and the right-edge continuation into connected Hungarian. Only one word in row 19 and the start of one word in B4 stay unread.
- Repeated words decode the same across rows: *hogy*, *édesem* ×5, *magával* ×3, *el vagyok foglalva* twice, *megír-* ×2, *mulat-* ×3.
- The text is coherent across row breaks and across the corner (*mennyire* at the bottom-right, *el vagyok foglalva* up the edge). It also fits the family: polite *maga* address, under-the-stamp closing as on hcp-1216 and sister cards, the writer's habit *higgyje el*, loss of doubled consonants.
- The plain "50 K." agrees with the talk of spending on the ball (*nem érdemes költeni*).

## Response to review 1

Verdict REVISE. I checked each finding on the reviewer's crops (and my own for the paratext). All ten are accepted; none is disputed. After the fixes `python3 -I ciphers/hcp-1247/work/decode.py` passes all four hash checks and prints the literal block above. The reading of the message is not substantially changed: one word (row 19) is withdrawn to uncertain, and the rest is sign-level correction.

1. **Row 19, *lesz*: fixed.** `review/work/c/k1819.jpg` shows the same section mark at the start of rows 18 and 19; I had misstated it as s. Ledger is now `K E ?`. The word is printed as uncertain in the literal, normalized, English and Slovak texts; note 6 rewritten. The *kerül* idea is recorded as a possibility only.
2. **Row 20, *majd*: fixed.** `z20e.jpg` shows short + long stroke after j. `D` added; *maj → majd* deleted from note 13.
3. **B3 *edesem*: fixed.** `bb3.jpg` shows three bars, the lowest short. Token changed to `E`; note 13 corrected. *édesem* ×5 now holds in the ledger.
4. **B4: fixed.** `bb4.jpg`: the "point" and "stroke" are one d sign. Ledger is `? ? D I G`, note 1 rewritten and "something other than letters" dropped. *-dig* is reported; no whole word is claimed. The normalized text gives *[…]dig*.
5. **Row 17: fixed.** `z17s.jpg` supports three bars with the middle lost. Ledger *hetem*; note 8 updated.
6. **Row 8: fixed.** `z8.jpg` shows the d shape. Ledger token is `D`, literal *szed*, and *szép* stays as a reading on sense, stated in note 5 and the ledger header. The key table now gives d and h/p as two shapes.
7. **"The money": fixed.** Title made neutral; English and Slovak now say "fair pile" / "kôpka" and "how much (or how many)"; note 5 gives both senses and separates the 50 K.
8. **mondhatnem: fixed.** Normalized to *mondhatnám* and listed in note 13.
9. **Small errors: fixed.** *maga* for "formal *Ön*"; *mulat-* ×3; the note on row 1 now says three strokes. G and Y are now separate tokens throughout the ledger, and the key table says so; the printed letters do not change.
10. **Plain context: fixed.** New section "Plain text on the card". While checking it I read the address's first word as *Szépreményű*, from the formula on sister cards.
