# HCP 1269 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-71): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered; everything on the card is transcribed, and one word of the last clause stays unread. Independent review 1 verdict REVISE; six sign errors and smaller slips corrected, key and sense of the card unchanged.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1269 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1269), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-71, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The HistoCrypt paper was not consulted for this reading.

The picture side shows a young violinist in evening dress, with a girl in a pale dress leaning on her hand. Its printed title and verse, in gold, are not cipher: Ezüsttükrös kávéházban / Üldögélek elmélázva / Csendesen… ("In the silver-mirrored café I sit lost in thought, quietly…").

The address side is plain in part: **Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás** ("To the promising Miss Jolánka Tóth, Jászárokszállás"). Szépreményű is a courtesy epithet known from other cards of this family. The message is on the same side in green ink and invented signs: 27 rows across the left half, four rows across the full card width under the address, a short row running up the right edge, and six short rows under the stamp. The edge row is followed by the plain words folyt. köv. ("to be continued"), so the letter went on on another card. The postmarks cannot be read at this resolution, so the card is undated.

The card belongs to the correspondence of a young man, Feri, with Jolánka Tóth, of which many cards are deciphered in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301).

![Picture side, turned upright (work/picture-upright.png)](../work/picture-upright.png)

![Address side with the cipher text, the plain address and the rows under the stamp (source/address-large.jpg)](../source/address-large.jpg)

## Method

The key was **transferred unchanged** from the finished Jolánka cards, chiefly HCP 1216; this is not a new key recovery. No plaintext of this card was supplied or consulted.

The transcription is manual. The solver enlarged the un-converted portal scan 2 to 5 times in overlapping crops and recorded each written sign by its key value in a sign ledger of 32 rows and 6 stamp rows (775 letter signs). A short script checks the hashes of the images and decodes the ledger. Because the ledger records values rather than independent shape codes, a reader's expectation can creep in; review finding 10 says so, and the review round was aimed at exactly that risk.

Rows 28 to 31 run under the address, and row 32 reads upwards along the right edge.

## Key

Hungarian, simple monoalphabetic substitution with invented signs, with a hidden message written in the stamp box under the (now lifted) stamp (register type MASC + Steganography; type updated 2026-11-03 after a stamp-box audit that confirmed the six stamp rows read below).

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl (only in opposed bowls here) | c | three short strokes | m | gamma/corner | t |
| long stroke + short tick | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | opposed bowls | cs |

Dots over o and u give ö and ü, two ticks give ő, and a tick over two bars gives á. Other accents are mostly not written and are supplied. The h/p sign and the close d/n pair are told apart by word sense and stroke length; the words concerned (megkaptam, szépen, csepet, Pestre, lapot; dolkoznom, rendelkezik, mindig) are unambiguous.

## Plaintext

Literal decipherment row by row (`h` stands for the h/p sign, `{?}` for an unreadable sign):

```text
01 zseretetedesjolankam-
02 kivanomhogyalegjobbeges
03 segbentalaljasoraimb.
04 soraitmegkahtammelyet
05 köszönőgszehen.edesemön
06 tevedhaaztgondoljahogy
07 becsessorainemszolgenak
08 orömemrelegyenabbabar
09 mimertenmindigalegna
10 gyobborömelolvasomso
11 raitedesemigazansajnalom
12 hogytovabraisazonkelgon
13 dolkoznomhogymiindi
14 tottaarahogyaztirja
15 mertazegesznekazazoka
16 hogyegyszerjobbanraermas
17 kormegegycsehetsemerek
18 ra.edesemhiszaztenis
19 szeretnemhogyminele
20 lőbelmehessekcsakhogy
21 enfelattemmasrendel
22 kezikmajdmeggyozö
23 dikrolahafeljönekhest
24 rehogymenyiszabadom
25 vanedesemnemakarom
26 munkajabazavarnivarhat
27 magaakorishao{?}tvegzok.
28 csakmarotvolnek.edesemennemirtamaztalahotidegenan
29 csakkerzeztemhogymitgondolthogyaztamegjegy
30 zestcsinaltaeshaiketdesekvanakőztünkabolnegon
31 doljonmindenroszstamitmarnemszabadtehate
32 lezegymasrol
stamp: üdvozli / atavol / bo{?}ze / retőked / vesse / feri
```

### Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb egészségben találja soraim. B[ecses] sorait megkaptam, melyet köszönök szépen. Édesem, ön téved, ha azt gondolja, hogy becses sorai nem szolgálnak örömemre. Legyen abban bármi, mert én mindig a legnagyobb örömmel olvasom sorait. Édesem, igazán sajnálom, hogy továbbra is azon kell gondolkoznom, hogy mi indította arra, hogy azt írja, mert az egésznek az az oka, hogy egyszer jobban ráér[ek], máskor meg egy csepet sem érek rá, édesem. Hisz azt én is szeretném, hogy minél előbb elmehessek, csak hogy én felettem más rendelkezik. Majd meggyőződik róla, ha feljön(ne) Pestre, hogy mennyi szabadom van. Édesem, nem akarom munkájába zavarni, várhat maga akkor is, ha ot[t] végzek. Csak már ott volnék. Édesem, én nem írtam azt a lapot idegen[?], csak kérdeztem, hogy mit gondolt, hogy azt a megjegyzést csinálta. És ha [i] két[ke]dések vannak köztünk, abból ne gondoljon minden rosszat, mit már nem szabad tehát [? unread: …tehate lez] egymásról.

folyt. köv. (plain)

Under the stamp: Üdvözli a távolból szerető kedvese Feri.

### English

My beloved sweet Jolánka! I wish that my lines find you in the best of health. I have received your d[ear] lines, for which I thank you very much. Darling, you are mistaken if you think that your dear lines do not give me joy. Whatever may be in them, I always read your lines with the greatest pleasure. Darling, I am truly sorry that I must keep wondering what prompted you to write that, for the cause of the whole thing is that at one time I have more leisure and at another not a drop of it, darling. Why, I too would like to get away as soon as possible, only someone else has charge of me. You will see for yourself, if you come up to Pest, how much free time I have. Darling, I do not want to disturb you at your work; you can wait until I finish there. If only I were there already. Darling, I did not write that card [? through / to a stranger], I only asked what you thought, that you made that remark. And if there are doubts between us, do not from that think every bad thing, which one must no longer [? assume] of each other.

To be continued.

Under the stamp: Greetings from afar from your loving sweetheart, Feri.

### Slovak

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky našli v najlepšom zdraví. Vaše m[ilé] riadky som dostal, za čo veľmi pekne ďakujem. Drahá, mýlite sa, ak si myslíte, že Vaše milé riadky ma netešia. Nech je v nich čokoľvek, vždy čítam Vaše riadky s najväčšou radosťou. Drahá, naozaj ma mrzí, že musím stále rozmýšľať nad tým, čo Vás viedlo k tomu, aby ste to napísali, lebo príčina toho všetkého je, že raz mám viac času a inokedy ani kvapku, drahá. Veď aj ja by som chcel čo najskôr odísť, len nado mnou rozhoduje niekto iný. Presvedčíte sa o tom, ak prídete hore do Pešti, koľko mám voľna. Drahá, nechcem Vás rušiť pri práci, môžete počkať, kým tam skončím. Keby som tam už bol. Drahá, ten lístok som nenapísal [? cez cudzieho / cudziemu], len som sa pýtal, čo ste si mysleli, že ste urobili tú poznámku. A ak sú medzi nami pochybnosti, nemyslite si z toho všetko zlé, čo už nesmieme [? predpokladať] jeden o druhom.

Pokračovanie nabudúce.

Pod známkou: Pozdravuje Vás z diaľky Váš milujúci milý, Feri.

## What remains uncertain

1. **Rows 31–32, the one unread word.** `…szabad tehate | lez egymasrol`: szabad, tehát and egymásról read, the remainder `e-le-z` does not. Feltételez(ni) ("to assume") suits the sense, but the signs do not spell it; the English and Slovak give it as a guess only.
2. **Row 28 `idegenan`.** The stem idegen ("stranger") is clear, the ending is not: "through a stranger", or a slip for idegennek ("to a stranger").
3. **Row 30 `haiketdesek`.** Read ha két[ke]dések ("if doubts"), with a restored syllable. The dotted i between ha and két is unexplained: a false start or an unfinished small word.
4. **Row 23 `feljönek`.** The signs are clear and ha feljön is the family's stock phrase, but the ending `-ek` is odd.
5. **Restored signs.** Row 27 `o{?}t`, under a blot, is restored as ot[t]. Stamp row 3 `bo{?}ze`, under the postmark, is restored as távolból szerető.
6. **Writer's slips normalized.** Among them zseretet for szeretett, köszönőg for köszönök, felattem for felettem, kerzeztem for kérdeztem, roszsta mit for rosszat, mit, vesse for kedvese, and vanakőztünk for vannak köztünk, where one k serves two words. The row 1 third sign and the row 22 first sign are overwritten.
7. **Undated.** The postmark is not legible.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the decoder, wrote its own, read rows 1–13 and 26–32 and the stamp sign by sign on its own crops, and checked rows 14–25 at lower zoom. It confirmed the key and the language, and found no sign of forcing the text, but returned **REVISE** with ten findings:

- **Major: row 23.** `h e z a l` was a misreading of ha fel-, so the clause is the family's plain ha feljön… Pestre, not an "eljön" reached by correction.
- **Minor sign corrections.** Row 30 is `vanak` plus a single k with ő, not `vanek k-`. Row 28 már is spelled correctly, as is row 15 egésznek; both had been wrongly listed as the writer's slips. Stamp row 5 has five signs, not four. The cross in row 32 is z, not undecided. The vowel in row 28 `idegenan` is a.
- **Details.** The i of row 30 has a dot; the plain word above the address is Szépreményű, not a name; ticks over o in rows 5 and 20; a written point in row 18; two overstated word counts.

All findings were rechecked on the scans and accepted. The solver also read rows 14–25 again at higher zoom and found nothing more. The key did not change, and the sense of the card did not change. The unread word stays unread.
