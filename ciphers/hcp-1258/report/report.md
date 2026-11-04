# HCP 1258 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-70): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered (29 rows and the 7 rows under the stamp, 796 letters); independent review 1 verdict REVISE, findings addressed. One word of the closing, Fe[ri], rests on sense more than on clean signs.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1258 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1258), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-70, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the catalogue row listed it as **Not solved**, category Substitution, language Unknown, recipient Tóth Jolánka, with no transcription or solution. The card's detail page timed out in capture, so its tabs were not read one by one.

The whole message is on the address side, in green ink in invented signs: 25 rows in the left block, 4 rows across the foot of the card, and 7 short rows in a box drawn at the stamp place. The stamp is missing. The address (Tóth Jolánka, Jászárokszállás) is in plain hand; its first line was not read. The postmark gives no readable date, so the card is undated. The picture side has a printed verse beginning Messze vagyok de sohasem feledlek and no cipher text.

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards from Feri to Jolánka Tóth in Jászárokszállás, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key, so this card was read with a **known, transferred key**. The key was established on those cards, partly by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), with later work by Claude Opus 5.5. No published solution of this card was found, and the AI Decipherment Register had no record of it on 2026-11-01.

## Method

Claude Opus 5.5 read every sign by hand from enlarged crops of the high-resolution original and recorded it as a sign ledger, one token per written sign (`work/ledger-signs.txt`). This is not OCR, and it is not blind, because each sign was classed with the key in view. Hard places were settled by rereading shapes, never by changing the key: the numeral 2 in row 12, lefekszek, átalszom in rows 13–14, and the stamp box, where a green smear covers some signs. Each hard call is listed under Uncertainties.

The command `python3 -I ciphers/hcp-1258/work/decode_opus.py` checks the file hashes, maps the ledger through the key and prints the literal rows and the normalized text. The normalized text is an editor's file, with word division, accents and spelling supplied by hand.

## Key

Monoalphabetic substitution with graphic signs. The labels are names for handwritten shapes. Register type: **MASC + Steganography** (changed from MASC on 2026-11-03), because the closing message is written in the box at the stamp place, where the stamp would hide it.

| sign class (ledger token) | letter | sign class (ledger token) | letter | sign class (ledger token) | letter |
|---|---|---|---|---|---|
| two bars (BAR2) | a | section mark (SECT) | k | F-like (FLIKE) | r |
| six (SIX) | b | wave (WAVE) | l | right bowl (RBOWL) | s |
| left bowl (LBOWL) | c | three short strokes (STROKE3) | m | gamma/corner (GAMMA) | t |
| long stroke + short tick (TICK) | d | two short strokes (STROKE2) | n | plain cross x (XPLAIN) | u |
| three bars (BAR3) | e | cursive loop (LOOP) | o | chevron (CHEV) | v |
| cross, upright or tilted (CROSS) | f | tall stroke + short (TALL) | h / p | low descender (DESC) | y |
| open loop with descender (GLOOP) | g | dotted crossed curve (CURVE) | i | crossed diagonal, x with tail (XTAIL) | z |
| inverted T (INVT) | j | joined loop + descender (LOOPDESC) | gy | opposed bowls (OPPBOWL) | cs |

Dots over o/u give ö/ü; a double mark gives ű; acute marks are faint and mostly supplied in normalization. JOINTY is the joined ty sign seen only in row 22.

The h and p signs are near-homographs and d and n differ in stroke length, so some calls rest on word sense (Uncertainty 4).

## Plaintext

Literal decipherment, row by row (h stands for the h/p sign; [x] is a restored hidden sign):

```text
 01 szeretettédesjolankám
 02 kivanomhogyalegjobbkedve
 03 betalaljasoraimhogytelt
 04 avasarnahédesemdeszeretném
 05 máraviszontlatasörömeit
 06 élveznidesajnoslevagyok
 07 kötvenemakorcsinaloksza
 08 badotamikorakarok.odaha
 09 zavanmegabélamostvanaki
 10 mulattasanekemnemalegjobb
 11 vasarnahomvanmertesik
 12 azessöéséjel2oratoldelig
 13 fojtonaztammostmeglefek
 14 szekatalszomavasárnahot
 15 ezazénvasarnahomitéde
 16 semaztsetudjaazember
 17 sokszorhogymikorvan
 18 vasarnahédesemigazán
 19 örülöhogyujraszorakoz
 20 hatommagavalédesem
 21 csakarakéremmagátédesem
 22 nehalgasonsemifélehlety
 23 karanezavarjasemiabodog
 24 sagunkatteljesbizalommal
 25 legyenirntammihejtojan
 26 hejzetbeleszekhogyfeleség[e][m]etehesemhögtönotleszek
 27 merténjobbanvaromaztahejzetminttalanmagaédesem
 28 mertmagatöbbszörmondtahogyráérmégelégfiatalahogy
 29 szükséeseténlegtöbb1éve[t]varjoncsooljakedvessef.e
 s1 istanvele
 s2 édesem
 s3 marad[o][k]
 s4 hűkedv[e]
 s5 seéssiri
 s6 huimádo
 s7 jaferi
```

Hungarian, normalized:

Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvébe találja soraim. Hogy telt a vasárnap, édesem? De szeretném már a viszontlátás örömeit élvezni, de sajnos le vagyok kötve: nem akkor csinálok szabadot, amikor akarok. Odahaza van még a Béla, most van a kimulatása. Nekem nem a legjobb vasárnapom van, mert esik az eső, és éjjel 2 órától délig folyton áztam. Most meg lefekszek, átalszom a vasárnapot. Ez az én vasárnapom. Itt, édesem, azt se tudja az ember sokszor, hogy mikor van vasárnap, édesem, igazán. Örülö[k], hogy újra szórakozhatom magával, édesem. Csak arra kérem magát, édesem, ne hallgasson semmiféle pletykára, ne zavarja semmi a bo[l]dogságunkat. Teljes bizalommal legyen ir[á]ntam: mihelyt olyan helyzetbe leszek, hogy feleségemmé tehessem, rögtön ott leszek, mert én jobban várom azt a helyzet[et], mint talán maga, édesem, mert maga többször mondta, hogy ráér még, elég fiatal, ahogy szüksé[g] esetén legtöbb 1 évet várjon. Csó[k]olja kedvese, Fe[ri].

Under the stamp: Isten vele, édesem! Maradok hű kedvese és sír[ig] hű imádója, Feri.

## Translation

English:

My beloved sweet Jolánka! I hope my lines find you in the best of spirits. How was your Sunday, my darling? How I would love to enjoy the joys of seeing you again, but sadly I am tied down: I cannot make free time when I want to. Béla is still at home; he is having his fling now. Mine is not the best of Sundays, because it is raining, and from 2 at night until noon I was getting soaked the whole time. Now I shall lie down and sleep through Sunday. That is my Sunday. Here, my darling, one often does not even know when it is Sunday, truly, my darling. I am glad that I can enjoy your company again, my darling. I ask only this of you, my darling: do not listen to any gossip, let nothing disturb our happiness. Have complete trust in me: as soon as I am in a position to make you my wife, I shall be there at once, for I long for that state of things more than perhaps you do, my darling, since you have said several times that there is still time, that you are young enough to wait a year at most if need be. Kisses you, your sweetheart, Fe[ri].

Under the stamp: Farewell, my darling! I remain your faithful sweetheart and, unto the grave, your faithful admirer, Feri.

Slovak:

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky našli v najlepšej nálade. Ako prebehla nedeľa, drahá? Ako rád by som si už užil radosti z opätovného stretnutia, ale žiaľ som viazaný: nemôžem si urobiť voľno, kedy chcem. Doma je ešte Béla, teraz si užíva. Ja nemám najlepšiu nedeľu, lebo prší, a od 2 v noci do poludnia som stále mokol. Teraz si ľahnem a nedeľu prespím. To je moja nedeľa. Tu, drahá, človek často ani nevie, kedy je nedeľa, naozaj, drahá. Teším sa, že sa môžem znova zabávať s Vami, drahá. Prosím Vás len o to, drahá, nepočúvajte žiadne klebety, nech nič nekazí naše šťastie. Dôverujte mi úplne: len čo budem v takom postavení, aby som Vás mohol urobiť svojou manželkou, hneď tam budem, lebo ja na ten stav čakám viac než možno Vy, drahá, veď ste viackrát povedali, že ešte je čas, že ste dosť mladá na to, aby ste v prípade potreby počkali najviac 1 rok. Bozkáva Vás Váš milý Fe[ri].

Pod známkou: S Bohom, drahá! Zostávam Vaším verným milým a až do hrobu verným ctiteľom, Feri.

## Uncertainties

The crops named below are in `work/crops2/`.

![End of row 29, with the end of row 28 above it: the closing read as kedvese, Fe[ri] (work/crops2/r29tail.png)](../work/crops2/r29tail.png)

1. **Closing of row 29 (the least secure place).** After várjon the literal signs are c-s, o, o, l, j, a, k, e, d, v, e, s, s, e, cross, dot, e, and the row ends at the worn corner (crop r29tail, crop xe). The reading is Csó[k]olja kedvese, Fe[ri], a family closing (HCP1213, 1301: Csókolja … kedvese Feri).
   - csó[k]olja: both middle signs have the loop-with-tail outline of this writer's hurried o (compare hogy at the end of row 28, crop hogy28). The second is overinked and looks written over something (crop blr). A k cannot be seen. Either it is under the blot or it was omitted, as this writer often omits letters. csalja is excluded by the o signs.
   - kedvese: written k e d v e s s e. The second s is a right bowl with a hooked top, the same form as the s that opens row 29 (crop r29start). It is not k: the k of szükség in the same row and of kedves are section marks. So the reviewer's kedves kezé[t] fails at that sign. Doubled s for single is this writer's habit (row 12 essö, and doubled letters in row 10 kimulattása).
   - Fe[ri]: the small cross is the one soft call. By shape alone it could be plain x (u) or a tilted f, and it lacks the long tail of z. It is close to the tilted f of fiatal in row 28 just above (crop f28), and only f gives a word. The dot beside it has no value here (stray, or a point after an initial). The last sign is a squeezed three-bar e at the corner, its bottom bar detached. The letters ri are not on the card: nothing continues on the right edge, so they ran out of room or were dropped. This word rests on sense and the formula, not on clean signs. The full signature Feri stands in the box. If it is rejected, one word of the closing stays unread and the message is not affected.
2. **Restorations of physically hidden signs.**
   - Row 26 at the tear: feleség[e][m]é. A fragment of one sign and the last stroke of m are visible. The tear leaves room for about two signs, so the writer probably wrote single m, as he usually does.
   - Row 28 final hogy: the g and the y are both visible on crop hogy28. The y runs heavily into the worn corner. Round 1 said the g was in the tear; that was wrong, and the ledger is right to show it unbracketed.
   - Row 29: the t of évet is in the tear; the end of its bar is visible.
   - s3: marad[o][k]. One small wedge and a vertical trace survive in a green smear, so two signs are restored here, which is more than the one-letter rule allows. maradok is chosen from sense with hű kedvese; literally only marad is certain. The wedge resembles the wedge-shaped ó of s6 imádója, which supports the o.
   - s4: the final e of kedve[se] is in the smear; the se that follows opens s5.
3. **Wiped and blotted places.**
   - Row 12: az eső and és lie in a wiped patch. és is a ghost three-bar with its accent plus a ghost s, read only under enhancement.
   - Row 14: a solid blot stands between át and alszom. It is taken as covering no letter of the word, or a slip; átalszom does not need a further sign.
   - Row 9: the a of Béla has its top bar clear and its lower bar under a blot.
   - Row 17: the n of van is a faded, smudged shape at the right edge, read from sense and the ghost of two strokes.
   - Row 18: the é sits under a heavy blot; its bars can be seen around it. Row 22: the o-n of halgason is blotted.
   - Row 6: the y of vagyok is smudged and postmarked. Rows 7–9 near x 1500 are under a green wash but legible.
4. **Readings resting on word sense.**
   - h/p: p in vasárnap (rows 4, 11, 14, 15, 18), and pletykára; h elsewhere. Row 26: the sign before ögtön is the clear h/p sign (stroke plus separate dot), where sense wants r: literal högtön, normalized rögtön. This is the writer's slip or an unusual form, not a clean sign match.
   - d/n: n in row 29 esetén and d in row 12 délig are by word sense.
   - Row 13: the first sign of folyton is a tilted cross taken as f (u gives no word).
   - s6: the sign written for ű of hű is the cross without visible dots; i of imádója has its dot lost in the smear; the ó is an unusual small sign with a wedge; s7 opens with tilted j.
   - s1: Isten shows two bars under the long t stroke (literal istan), the third bar being merged or omitted.
   - Row 22: the ty of pletykára is a joined sign seen only here.
5. **The writer's spellings, normalized.** ojan/mihejt/hejzet (j for ly), fojton, éjel, akor, semi, halgason, ara, tehesem, ot, itédesem (itt), essö (eső), kimulattása, kedvébe (for -ben), örülö (k omitted), bodog- (l omitted), irntam (á omitted), helyzet (acc. -et omitted in row 27), szüksé (g omitted), siri (g omitted: sír[ig], a shortening noted on sister cards). The small two-dot a in row 5 (már a) sits squeezed between r and v. Most accents are not visible and are supplied.
6. **Row 28 ahogy.** After fiatal the card has a separate two-bar a before hogy (crop hogy28), so the literal text is fiatalahogy. Round 1 missed this sign. It is printed as ahogy. As a plain word that means "as", which fits poorly; the sense wanted is ahhoz, hogy ("young enough to …"), so this is taken as a telescoped form of that phrase or a slip. The translation follows that sense. The sentence does not change otherwise.
7. **k/g.** In row 24 -ságunkat the k-position sign looks like g; it is kept as literal g and normalized k. In row 13 the s of most has a longer stem than usual.
8. **Not part of the cipher.** The address (Tóth Jolánka, Jászárokszállás) is in plain hand; its first line is not read here. The picture side has a printed verse beginning Messze vagyok de sohasem feledlek. The postmark shows a line with 91 and C, not a date. The stamp is missing. The print number 6432 at the foot is a printer's mark overlaid by row 26's last sign.

## Why the reading stands

All 796 letters take a value from the family key without any new sign value, and the result is running Hungarian in Feri's spelling. The text is specific: rain, a soaked night, a Sunday slept through, a plea to ignore gossip, and a marriage promise that answers her remark about waiting a year. The numerals 2 and 1 fit their phrases. Family formulae recur (Kívánom, hogy a legjobb kedvébe találja soraim, Isten vele, édesem, sírig hű, imádója, Feri), and repeated words decode alike (édesem ×7, hogy ×7 in the round 1 count).

## Review and what changed

A separate Claude Opus 5.5 agent re-ran the command, recounted the ledger, made its own crops and read rows 1–29 and the box against the ledger and key. Its verdict was **REVISE**: the decipherment stands, but two things needed fixing. It did not re-derive the key and its pass was not blind.

- **Row 28 (major):** a written a after fiatal was missing from the ledger. Added; the text now reads ahogy, and the letter count went from 792 to 796 with the row 29 changes below.
- **End of row 29 (major):** the closing had been left largely unread. The two middle signs of the first word are now read as o, giving Csó[k]olja. The reviewer suggested testing kedves kezé[t]; that was tested and not adopted, because the hooked sign has the form of s, not k, and the cross has no z tail. The closing is read as kedvese, Fe[ri] instead. **This last reading was made after the review, so no reviewer has checked it.**
- **Command (minor):** the ledger held letters, not signs. It now holds sign classes and the command applies a key table.
- **Disclosures (minor):** a wrong note on the g of row 28 was corrected, and smudged signs in rows 17, 18 and 22 were added. A likeness that supports s3 marad[o][k] is cited.

The message body was otherwise not changed by the review.

Stamp-box audit (2026-11-03): the stamp is lifted, and under it is the 7-row closing in cipher signs, given above under Under the stamp. The reading was checked again on new crops and is unchanged. Only the register type changed, from MASC to MASC + Steganography.

Credit: transcription, key transfer and decipherment on this card by Claude Opus 5.5; independent review by a separate Claude Opus 5.5 agent.
