# Structure of the 1672 Lincker nomenclator from its 26 glossed codes (local analysis)

Output of `python3 -I code_structure.py source/bourdeau/codes.txt` is in `output.txt`.

## 1. Key 255 (1666) as the family template

Read in full from `source/full/key255.jpg` and `key255-0014/15/16.jpg`. The list is **by category and rank, not alphabetical**, and each new category starts a new run, once on a round number:

| codes | content (as read on the scans) |
|---|---|
| 180–190 | sovereigns in rank order: Kayser 180, König in Frankreich 181, Spanien 182, Schweden 183, Kön. Dennemarck 184, Engelland 185, Polen 186, Moscowiter 187, Cossaggen 188, Holländer 189, Venetianer 190 |
| (191–199 unused) → 200–225 | electors and princes: Chur Mainz 200, Trier 201, Cöln 202, Baiern 203, Sachsen 204, Brandenburg 205, Pfalz 206, Braunschweig-Wolfenbüttel 207, Zell 208, Hannover 209, Pfalz-Neuburg 210, Waldeck 211, … Hessen-Cassel 215, Darmstadt 216, Bischof zu Münster 217, Paderborn 218, Fürst von Anhalt 219, … named persons 221–225 (R. v. Canstein 224, Canzlar Jena 225) |
| 226–236 | countries: Teutschland, Römisch Reich, Frankreich 228, Spanien, Portugal, Engelland 231, Hollandt 232, Ostfriesland, Westfriesland, Böhmen |
| 237–273 | regions, seas, rivers (Westphalen … Mark Brandenburg 252, Holstein 253, Mecklenburg 254 … Donau, Rhein, Elbe … Oder 273) |
| 274–281 | Reichskreise and small territories |
| 282–308 | towns (Rinteln … Berlin 288 … Copenhag 295 … Hamburg 298 … Münster 303 … Ziegenhain 308) |
| 309–386 | vocabulary, **alphabetical**: Action 309, Allijrte 310, Alliance 311, Ambassade 312 … Verfassung 386 |
| 387–407 | numerals Ein … Zehen Tausend |

Key 253 (same file) has a list 300–409 with Chur Cölln 303 and Alliance 330, i.e. the family also makes lists that begin at 300. The 1236 lists (c. 1715) are different in kind: 601 = le Pretendant / 576 = Bremen / 602 = Mr. Martine / 625 = Vestung (mixed names and words), or 601 = Gnad / Holstein = 666 (alphabetical dictionary with names interleaved).

## 2. What the 26 occurrences show (table in output.txt)

* 17 distinct codes (preferred 427 reading), 26 tokens; **15 tokens / 8 codes lie in 601–653**, and every referent there belongs to the Danish–Brandenburg negotiation of spring 1672: Dennemarck 601, [Kayser] 602, Statthalter (Ahlefeldt) 625, Blumenthal 630, Holstein 634, Plön 641, Churbrandenburg 651 and 653.
* Within that block the order is D, K, S, B, H, P, C – not alphabetical; within 700 it is Schweden 768, Hollandt 774, General Staaten 775 – not alphabetical either. A single alphabetical list gives 36 inversions among 14 glossed codes: **rejected**.
* Key 255's rank order of sovereigns (Schweden before Dennemarck) is violated (Dennemarck 601 < Schweden 768): the 1672 list is **not a renumbered 255**.
* "255 unchanged + appendix above 407" is rejected: the only code inside 180–407 is 303, which must be the feminine noun *alliance* ("eine estroite 303") but is Münster in 255 (Alliance = 311); and the writer used a >407 code for every one of the four words that 255 already had (Frankreich 228, Hollandt 232, Holstein 253, Dennemarck 184/212).
* The only sign of alphabetical ordering is 303 = alliance: 255 opens its vocabulary with Action 309, Allijrte 310, Alliance 311, so a vocabulary block starting at 300 with the same A-words puts Alliance at 302–303.

## 3. Best-supported model: purpose-built topical blocks by hundreds

| block | content | evidence |
|---|---|---|
| 300– | vocabulary, alphabetical | 303 alliance; 255's A-words; 253's list starts at 300 |
| 400– | titles / qualifiers | 427 Herzog (with 641: "Herzog [von] Plön"); 447 = first half of the two-code Emperor designation, built like 427 + 641 |
| 500– | other powers / lands | 576 Frankreich (entry 76 of the block, so a long block) |
| 600– | the negotiation: Denmark, Emperor, Danish court persons, Holstein, Plön, Brandenburg | 601, 602, 625, 630, 634, 641, 651, 653 |
| 700– | northern / maritime powers | 768 Schweden, 774 Hollandt, 775 General Staaten (adjacent) |
| 800– | towns and/or a supplement of frequent items | 829 Berlin, 834 Rex Daniae (cf. HCP 267: King of Denmark 235/338/583) |

**601 vs 834.** Compatible, no re-examination needed. 601 is used locatively ("in <601> Adell, Bürger und Bauern") and as a party; the glosser rendered it K. Dennemarck / der König in Dennemarck / Dennemarck according to context. 834 appears only as a party beside the Emperor, and the gloss literally reads **"Rey Danae"** in the black hand (`gloss-834-crop-x3.png`), i.e. Latin *Rex Dan[iae]* – not a town name, so the towns-block reading of the 800s does not touch it. Country and sovereign as separate entries is the family norm (255: Kön. Dennemarck 184 / Dennemarck 212; 266: Dennemarck 185 + king; 280: 532/533 vs 534/535). Consequence: 601 = *Dennemarck* (country/crown), 834 = *König in Dennemarck*.

**602.** On the enlarged crop (`gloss-447-602-crop-x3.png`) the struck "Hauß" stands over 447 and the struck "Braunschw." over 602; the correction "Kayser" is written exactly where "Braunschw." was. Both of the glosser's readings therefore treat 447 602 as ⟨word⟩ ⟨name⟩, and the correction concerns the name slot. Prediction: **602 = Kayser (or Römischer Kayser / Österreich) as the second entry of a non-alphabetical parties block that opens with Dennemarck 601**; 447 = a qualifier/title 20 entries after Herzog 427 (Römisch[er], Kayserlich, Haus, Ihro …; H→R or H→K fits ~20 entries if the 400 block is alphabetical). "Herzog von Plön" and "Römischer Kayser" would then be encoded identically: title code (400s) + name code (600s).

**427 vs 447.** Two different entries under the preferred transcription; the model does not need 447 = Herzog. If a reviewer upholds 447 at occurrence 21, then 447 = Herzog and 602 is a house – the weaker reading, since the Dano-Brunswick alliance was already concluded (31 March 1672) and the one "unter Handen" on 4 May was Denmark–Emperor.

## 4. Ten-second screening criterion

MATCH if a candidate list (a) is numbered above 800, (b) has **601 = Dennemarck/Dänemark with Kayser (Röm. Kayser / Österreich) at 602**, and (c) has Holstein at 634 or Churbrandenburg at 651. Supporting: Alliance = 303 at the head of an alphabetical vocabulary starting at 300; Schweden 768; Berlin 829; Plön 641; a Statthalter entry in the 620s.
REJECT on sight: one alphabetical run with names interleaved; numbering ends below 834; 601/634/651 are vocabulary words or syllables; 601 = le Pretendant or Gnad (the 1236 lists); French "Chiffre pour M. …" with four-digit groups.
Physical expectation: a German two-column list with dash leaders, like 255 pp. 14–16, 500+ entries (300–8xx), so about 7–9 pages, whose first column starts at 300 (not 180), probably endorsed for Secretarius Lincker / Dänemark 1672 – the mission file HStAM 4 f Staaten D Dänemark (Nr. 125 and neighbours) is the first place to ask for it, 4 d 1234–1236 the second.

## 5. Limits

All values rest on the black glosses of an undated later hand plus context; no code value is independently fixed. The block model is built from 17 numbers and cannot be proved from them; it is a search heuristic. The 625 gloss remains only partly legible (grade M) and 602 / 447 remain unresolved.
