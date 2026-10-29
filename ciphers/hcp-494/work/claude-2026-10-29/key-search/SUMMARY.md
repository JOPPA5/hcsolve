# HCP 494 – search for the expanded 1672 Hessian nomenclator: synthesis

Date: 2026-10-29. Synthesis of seven search angles (hcp-siblings, arcinsys-hessen, printed-sources,
code-structure, hannover-celle, danish-side, community-prior) plus the verification votes cast on the
three leads originally rated "medium". Raw inputs: `leads.json` in this folder. Each angle's own
MANIFEST.md, downloads and scripts are in its sub-folder.

Goal of the search: a key whose list contains 601 = Dänemark, 634 = Holstein, 768 = Schweden,
829 = Berlin …; or another letter/copy enciphered with it carrying a contemporary decipherment; or any
witness that fixes a code value independently of the black interlinear glosses.

## 1. Verdict

**No.** Neither the 1672 list nor any witness to it was found. No key in any public copy of the HCP, DECODE,
Arcinsys (Hessen, Niedersachsen), Rigsarkivet or GStA catalogues is dated or described in a way that
matches, no printed source quotes the letter or any 303–834 code with its value, and no prior or parallel
solver (Cipher-Atelier, Bourdeau, AI Decipherment Register) holds anything beyond the gloss-derived
readings already in SOLUTION.md. All 26 code values therefore still rest on the undated black glosses
plus context, exactly as before this search. Every lead that an angle rated "medium" was downgraded to
"weak" by the verifiers (two votes each; details in section 3); the survivors list handed to this
synthesis was empty. What the search did produce is (a) a precise map of what is *not* there, (b) a
small set of unscanned archival units that a human could order, none with catalogue evidence that it
contains the list, (c) two transcription/gloss checks the solver can do on the scan, and (d) a
structural model of the missing list usable as a 10-second screening criterion for any future scan.

## 2. Surviving leads, ranked (all weak)

Ranking is by expected payoff for *this* goal, not by how interesting the item is. "Strong" would
require having seen the document; "medium" a catalogue entry that makes it likely; nothing here reaches
either.

### 2.1 HStAM – Lincker's enciphered relation to Landgräfin Hedwig Sophie, 15 April 1676 (Fabricius 1909)
- URL: https://archive.org/details/historisktidsskriftdk8s2 (Knud Fabricius, "Griffenfeld og Fuenmayor",
  Historisk Tidsskrift 8. r. bd. 2, 1909–10, **p. 142 n. 1** and p. 156 n. 1 – one document, cited
  "Rel. 15/4. Marburg Ark."; the angle's "p. 149, Rel. 7/?" was an OCR misread, corrected by verifier 1
  from the page images).
- What it is: the only printed proof that an enciphered Lincker report with numeric codes survives in
  Marburg and that a reader in 1909 could resolve one code ("177 [dette Chiffer betyder: Reyne Mere]").
- Why only weak: different correspondent (Landgravine, not Vultejus), four years later, French gloss
  versus German/Latin glosses on 494, code 177 lies outside both key 255's list (180–407) and 494's
  observed range (303–834); Fabricius gives no shelfmark and does not say whether he used a key sheet or
  an archival gloss. The repo's earlier rendered Arcinsys searches list Lincker-to-Landgravine files only
  for 1668 and 1677 (4 f Staaten D Dänemark 141, 145; 145 = Vorprovenienz "Landgräfin Hedwig Sophie,
  Paket 7"), none for 1675–76.
- What a human must request, from whom: Hessisches Staatsarchiv Marburg (poststelle@hstam.hessen.de):
  Lincker's relation of 15 April 1676 to the Landgravine (probably 4 f Staaten D, Dänemark, in the
  Hedwig Sophie packets near Nr. 141/145) and *any key or gloss sheet filed with it*; while asking, also
  ask whether a key filed as "Lincker 1672" or with the Dänemark despatches 1670–1676 exists.
- Draft German request (one line, for the strongest archival lead):
  > „Sehr geehrte Damen und Herren, zu HStAM 4 f Staaten D, Dänemark Nr. 125 (Sekretär Georg Lincker an Kanzler Vultejus, Hamburg 4./14. Mai 1672, teilweise chiffriert mit Zahlencodes 303–834) bitte ich um Auskunft, ob (a) in den Dänemark-Akten Nr. 120–145 bzw. in 4 d (Chiffren) ein Chiffrenschlüssel mit den Einträgen 601 = Dänemark, 634 = Holstein, 768 = Schweden, 829 = Berlin oder ein Vermerk „Lincker 1672“ überliefert ist und (b) die von K. Fabricius (Hist. Tidsskrift 8. R. 2, 1909, S. 142 Anm. 1) zitierte chiffrierte Relation Linckers an Landgräfin Hedwig Sophie vom 15. April 1676 samt beiliegendem Schlüssel oder Dechiffrierung ermittelt und als Scan bereitgestellt werden kann.“
- Files: printed-sources/downloads/historisktidsskriftdk8s2.txt (lines 10546–10552, 11136–11141).

### 2.2 HStAM 4 d Nr. 1237 (DECODE records 4741/4742) – the one 4 d key volume nobody in this project has seen
- URL: https://de-crypt.org/decrypt-web/RecordsView/4741?showdetail=
- What: Hstam_4_d_nr_1237_01 (3 pp., "Simple substitution, Transposition, Nomenclatures; Numerical") and
  _02 (2 pp., "Nomenclatures, Polyphonic; Numerical"), dated 1700–1799 by DECODE; images need a login.
  HCP has no key from Nr. 1237. DECODE's dating of this series is coarse (Nr. 1236 is dated "1715 –"
  although it holds 1670s-style lists), so the label does not exclude 1672, but nothing links it either.
- Request: a human with a DECODE login opens the five images and applies the screening criterion in
  section 5; or include Nr. 1237 in the HStAM e-mail above. No agent login.
- Files: community-prior/decode-record-4741.html, decode-record-4742.html, decode-search-Hessen.html.

### 2.3 Arcinsys Hessen – enumerate the Dänemark sub-nodes and the 4 d fonds in a browser
- URL: https://arcinsys.hessen.de/arcinsys/showItemsList.action?nodeId=g201874 (Dänemark);
  parent 4 f node s147411; record of the letter: showArchivalDescriptionDetails.action?archivalDescriptionId=3352629.
- What: the list views are DataTables POSTs that could not be reproduced with curl (all variants return
  "Arcinsys | Fehler"); 120 brute-forced record IDs gave 15 other Dänemark files (none 120–135, none
  Lincker, none scanned). The 4 d (Chiffren) and 4 f Staaten B (Brandenburg) fondsIds are still unknown
  (not in 6790–6850). The provenance string "Kanzler Vultejus, Paket 5" is the best search key for the
  physically adjacent 1672 Vultejus papers.
- Request: a human (or a browser-capable session, not this one) expands the Dänemark sub-nodes
  for Linker/1670–1676 and the scan icon, and searches "Vultejus Paket". Locates candidate files only;
  supplies no code values by itself.
- Files: arcinsys-hessen/3352629.html, page_g143363.html, fonds/6830.html, MANIFEST.md.

### 2.4 Two checks on the scan itself (agent/solver, no archive needed)
- **768 or 678?** Cipher-Atelier's frozen reading of letter-cipher passage B begins "[678?]"; SOLUTION.md
  reads 768 (gloss Schweden/Sueco). Zoom source/full/0003–0004 at the head of passage B and record the
  digits. If 678, the gloss "Sueco" still stands but the number used for screening changes.
- **Slot alignment of the 447 602 gloss.** On the 3x crop the struck "Hauß" sits over 447 and
  "Braunschw." over 602, with the correction "Kayser" written in the 602 slot. Confirm on
  source/full/0004.jpg at full resolution; if upheld, 602 = Kayser (gloss, slot-aligned) and 447 remains
  an unresolved title/qualifier. Note that the code-structure angle also silently re-read occurrence 21
  from 447 (grade H in source/bourdeau/codes.txt) to 427 to fit its model; the solver should not adopt that.
- Files: community-prior/ca-VERIFIED_REPLAY_RESULTS.json; code-structure/gloss-447-602-crop-x3.png,
  gloss-834-crop-x3.png.

### 2.5 NLA Hannover – Celle Br. 76 Nr. 127 (1674, Bernstorff to Kassel/Mannheim, "Chiffreschlüssel beiliegend")
- URL: https://www.arcinsys.niedersachsen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=2486626
- What: real, obtainable (Original + Sicherungsfilm, no scan), but it is Celle's own mission file; the
  enclosed key is by default the Celle envoy key, and the only bridge to Hesse is key 255's uncertain
  endorsement "1676 mit dem Herzog zu Cell[?]" – and key 255's list already does not fit 494.
- Request: NLA Hannover, scans of the enclosed key (a few folios); low priority long shot.
- Related, weaker still: Celle Br. 92 Nr. 122 (Schütz) and Nr. 124 ("andere Chiffren und Schlüssel",
  undated), node g126524; NLA WO 2 Alt Nr. 2837/2838 (Wolfenbüttel Chiffern (1641) 1675–1725, Kassel not
  named). Files: hannover-celle/celle76-127.html, celle92-chiffren-p1.html, wo2alt-3961961.html.

### 2.6 Rigsarkivet – unscanned TKUA packets (content corroboration only, Danish keys)
- TKUA Hessen A II no. 20, 1670–1749 packet (DAISY 11650571; scanned part stops at 1663): Dalwig 1670,
  Habbaeus 1671, Brunswick alliance 1673, J. H. Lincker 1676. TKUA Brandenburg-Preussen, Georg Lincker's
  reports 1670–72 (DAISY 11630634; VA XI p. 82; scanned part skips 1661–1692). A Lincker report to
  Copenhagen from late April/May 1672 would corroborate the gloss content (Ahlefeldt, Blumenthal, Plön,
  Holstein) but would use a Danish key. Reading-room order only.
- Files: danish-side/daisy-11650571.html, indeks-top-19852381.json, dl-jorgensen/jorgensen.txt.

### 2.7 HC Portal – unharvested key ids 57–91 and 152–205
- Gaps in the public harvest (keys_index.txt); keys 266–288 appeared after the harvest, so an approved
  Marburg key could in principle turn up there. A human checks the rendered Cipher keys page filtered to
  Marburg; no API probing. Nothing indicates such a key exists.

### 2.8 Printed-source follow-ups (locate files, not code values)
- Ribbeck, FBPG 13 (1900) pp. 31–48 (Lincker's reports Jan 1673–1674, unread; OCR unusable) for any
  cipher remark or signature; Decker 1981 pp. 297, 312 for HStAM signatures of Lincker's 1672–75 reports;
  GStA I. HA GR Rep. 63 Nr. 328 (Blumenthal's Copenhagen mission Mar–May 1672) for cross-checking events.

## 3. Leads refuted or downgraded, and why

| Lead (angle, original strength) | Outcome | Why |
|---|---|---|
| Fabricius 1909: Lincker 1676 relation with 177 = Reyne Mère (printed-sources, medium) | downgraded to weak (votes: 1 not refuted / 1 refuted, both → weak) | Citation genuine but misplaced (p. 142 n. 1, "Rel. 15/4", one document not two). No shelfmark; 1676, Landgravine channel, French gloss, code 177 outside both known ranges; no catalogue entry for a 1675–76 Lincker file; unknown whether a key or a gloss supplied the value. |
| Code-structure model: "mission-specific topical nomenclator" (code-structure, medium) | refuted as a *lead* (2/2) ; kept as screening heuristic | Built entirely from the 26 glosses it should test, so fixes nothing independently. Its "first place to ask", 4 f Dänemark Nr. 125, is a one-letter Sachakte fully online (6 METS images: wrapper, ff. 2–4, docket, 1738 print) with no key sheet. No catalogue entry makes a key in neighbouring numbers likely. The model's tidiest result relies on re-reading occurrence 21 (447, grade H) as 427. |
| Celle Br. 76 Nr. 127, 1674 Bernstorff key (hannover-celle, medium) | refuted as medium (2/2) → weak | Celle's own outgoing mission file; enclosed key is by default the Celle envoy key; no mention of Lincker, Vultejus, Hamburg, Dänemark, 1672 or 1676; only bridge is key 255's uncertain endorsement, and 255's list does not fit 494 anyway. No scan. |
| Register entry "pc_hcp_494" (community-prior) | not a lead | Mislabelled record of cryptogram 1813 (Polish postcard 1910, image file pc_hcp_494_adr.JPG). Tell the register maintainer when submitting the 494 entry. |
| Bourdeau hesse1672 page, 23 Oct 2026 update (community-prior) | not independent | Added excerpt uses exactly the code values of SOLUTION.md, credited to the same reading.txt/codes.txt; names no key. |
| Cipher-Atelier commits 11 and 20 Oct 2026 (community-prior) | nothing new | Docs-only; frozen data unchanged; still key 255 alphabet only, 634 unresolved. |
| 4 f Schweden keys 117–128, 139, 140; 4 d 1226 (245/246), 1232 (251) (hcp-siblings) | excluded by content | 1633 alphabet or c. 1705–1722 lists (Prinzessin Ulrica, Marlborough, Cadogan, Czaar; French list Dannemarc 575 / Holstein 589 / Suede 617 / Berlin 570). |
| 834 as a town (code-structure) | dropped | Gloss reads "Rey Dan(ae)" = Rex Daniae. |

## 4. Negatives – what was checked, result (merged)

| Source / query | Result |
|---|---|
| HCP harvest index.json (1,493 records): all hstam records (31), all records 1660–1690 | Only 494 and 495 (4 f Schweden Nr. 116, 1630, solved monoalphabetic) in 4 f; 522 (4 d 1234_0003, c. 1660) is a sample of the inspected 1234 file; no record of any archive dated 1668–1680 besides 494 |
| HCP harvest keys (177 JSONs) tabulated by fond/folder/date | All Marburg; only key 255 dated 1660–1690; folders 4 d 1218/1219/1220/1223/1224/1226/1227/1228/1231/1232/1234/1236, 4 f Schweden 116/253/271, 5 Nr. 19784, 3; all cryptograms_id = [] (no key↔cryptogram link) |
| HCP keys 117–128, 139, 140 (4 f Schweden) – 39 images fetched, 8 viewed | 1633 or 1705–1722; French list Dannemarc 575, Holstein 589, Suede 617, Berlin 570 – incompatible |
| HCP keys 245/246 (4 d 1226), 251 (4 d 1232) | c. 1705–15 (Cadogan, Camisards, Czaar); 251 French syllabic table (Berlin 788, Danemark 799) |
| HCP keys 206, 242, 247–250 (4 d 1223/1224/1227/1228/1231) | Dated 1715–1730 by metadata; not viewed |
| HCP key records 253/254/255; record 494 | cryptograms_id = []; cipher_key_id null; status Partially solved |
| Arcinsys Hessen: list views for g143363, g201874; simple search "Linker" 1665–1680; signature search Dänemark 126; navigatorjson | All DataTables/JS; every curl variant (GET, POST, CSRF, session) returns "Arcinsys | Fehler"; no rows |
| Arcinsys Hessen: brute-force archivalDescriptionId 3352580–3352700 | IDs not in signature order; 15 other Dänemark files (Nr. 11, 29, 38, 51, 100, 107, 144, 169/187, 188, 193, 218, 235, 248), none 120–135, none Lincker, none scanned |
| Arcinsys Hessen: fondsId 6790–6850 | Only 4 f Staaten C–Z; 4 d and 4 f Staaten B not in range |
| Arcinsys Hessen full text "Chiffre/Chiffren/Ziffer…" 1670–1677; "Celle" 1675–77; "Lüneburg Celle Georg Wilhelm" 1672–77 | Only HStAM 4 f Dänemark 125 itself and HHStAW 150/787 (Nassau); no 4 f Braunschweig-Lüneburg 1676 file with cipher |
| HStAM 4 f Dänemark 125 record + METS (3352629) | One-letter Sachakte under "Dänemark > Zeremoniell; Titel", Vorprovenienz "Kanzler Vultejus, Paket 5", exactly 6 images, no key sheet |
| Archivportal-D (several queries, item pages) | Anubis proof-of-work wall for curl/WebFetch; via other angle's hits: only 1536/1540s Philipp-era keys (HStAM 3, 1763; 3, 2848) |
| Search engines restricted to arcinsys.hessen.de / archivportal-d (5 queries) | arcinsys.hessen.de not indexed; nothing 1668–1680 |
| WebSearch ×5 (Lincker/Vultejus/Hessen-Kassel Chiffre 1672/Rendsburg 1672/Lincker Landgräfin Marburg Chiffre) | No printed text, no 1670s Hessian nomenclator; only biographical scraps |
| Google Books API (6 queries) | HTTP 429 quota – NOT covered |
| HathiTrust full-text (3 queries; DNT VI search-inside) | Cloudflare challenge – NOT covered |
| MDZ OCR search | No curl-reachable endpoint – NOT covered |
| archive.org full-text API (5 queries) | 0 hits; "Lincker" alone yields only the works used plus homonyms |
| cryptiana German ciphers page | Hesse only 1609–10 and Rabenhaupt 1646; Brunswick 1683; nothing 1670s, no 500–900 codes |
| Fabricius HT 8.r.2 other cipher passages | French/Danish Griffenfeld cipher, not Hessian |
| Ribbeck FBPG 13 (1900) pp. 29–30 | No cipher remark; pp. 31–48 unread; OCR unusable |
| Fridericia 1894; Bidrag til den store nordiske Krigs Historie; Laursen DNT on IA; Rommel vol. 10 | Out of date range / not on IA |
| DNT VI (runeberg OCR, chronological list + index) | No Lincker; Hessen-Kassel only 1667, 12 Sep 1672 (p. 474), 1674 (p. 507); no deciphered report printed |
| Jørgensen, Griffenfeld (kb.dk PDF, 583 pp., full grep) | Lincker only 1674–76 as Danish resident in Berlin (TKUA "Brandenburg"); nothing 1672, no cipher |
| TKUA Hessen Gesandtskabsrelationer 1537–1763 (DAISY 11650592) | Georg Lincker 1677, 1683 only; unscanned |
| TKUA Hessen political acts 1528–1749 (DAISY 11650571), scan index epid 19852381 | Only 1528–1564 and 1587–1663 scanned; 1670–1749 packet offline |
| DAISY search "Griffenfeld"; VA IX private archives for Griffenfeld/chiffer | Form without rows; no Griffenfeld cipher-key archive listed |
| Web searches Lincker + Rigsarkivet/TKUA/Griffenfeld/Hamburg 1672 | Unrelated (18th-c. Lincker files LASA; jurist N. C. von Lyncker) |
| NLA HA Celle Br. 76 (Hessen) full Akten listing, 8 pages | Only Nr. 127 (1674) mentions a key; no 1672 file, no 1676 file; nothing digitised |
| Arcinsys Niedersachsen cipher-term searches 1660–1690 (several) | Celle Br. 76 Nr. 127; Cal. Br. 24 Nr. 7480 (Swedish mission 1671–74); WO 2 Alt 2837/2838; Celle Br. 92 Nr. 125 (1687); OS Rep 110 I Nr. 61; StAB 2-Dd 8 – none names Hessen-Kassel; interface caps at 20 rows |
| Arcinsys Niedersachsen "Hessen Kassel"/"Kassel"/"Landgraf Hessen Celle"/"Chiffre Hessen" 1670–1677 | No Hessian diplomatic file with cipher; "Chiffre Hessen" = 0 rows |
| Arcinsys Niedersachsen "Lincker OR Linker OR Lyncker" 1600–1750 | Only Celle Br. 92 Nr. 79, 90 (1679, Danish resident) and Celle Br. 44 Nr. 40 (secretaries' Bestallungen; same man unverified) |
| Celle Br. 92 structure (g126520–g126524), Chiffren section Nr. 116–125 | Keys for Bothmer, Caprara, Fabrice, Leuckfeldt, Schrader, Schütz, Sternberg, "alte schwedische Schlüssel für Neuhaus und andere"; no Hessen/Dänemark; no scans |
| NLA online viewer for Celle Br. 76 Nr. 127, Br. 92 Nr. 116–125, WO 2 Alt 2837/2838 | Original + Sicherungsfilm only |
| GStA PK midosasearch I. HA Rep. 11 Hessen-Kassel | search.htm HTTP 500; tree XML missing; via archivportal-d only Rep. 11 Staatsverträge (1667, 1672 Braunschweig ratifications) |
| archivportal-d "Lincker" (122), "Chiffre Hessen" (18), "Chiffreschlüssel" (24), "Chiffre 1672" (0), "Resident Hamburg hessen" (26), "Bernstorff Kassel 1674" (0) | No Staatsarchiv Hamburg record on Lincker; no 1660–1690 key naming Hessen-Kassel/Celle/Dänemark/Brandenburg; Lincker hits = Danish-service records (GStA Rep. 63 Nr. 348 Dec 1676; LASH Abt. 7 Nr. 2047; LASA Urbich letters 1693–99) |
| Cipher-Atelier repo: 10 commits 6–20 Oct 2026, patches of 507a4d91 and 3afd45a3, README, VERIFIED_REPLAY_RESULTS.json, research index | Docs-only; frozen; key 255 alphabet only; 634 unresolved; passage B head read "[678?]" |
| Bourdeau hesse1672.html (29 Oct) vs 23 Oct copy; catalogue entry 341 | Only an appended excerpt with SOLUTION.md's values; no key; entry unchanged |
| AI Decipherment Register JSON (337 entries) | No entry for the Lincker letter; "pc_hcp_494" = cryptogram 1813 |
| DECODE public RecordsList (10,106): Lincker, Vultejus, Daenemark/Dänemark, 1672, Hessen, Marburg | Only the known HStAM 4 d series (1218–1238); 4 d 1237_01/_02 the sole uninspected volume (1700–1799); 1235_01 "1670 –" already covered; images need login |
| WebSearch extended: "Lincker" "Vultejus"; hcportal 494 + 634/Holstein/ablauff; cipherbrain/scienceblogs/cryptiana/de-crypt/hcportal domains | Only Cipher-Atelier, Bourdeau, hcsolve itself, Antal–Mírka HistoCrypt papers (Thirty Years' War keys), Cipherbrain 2021 Rabenhaupt 1646 |
| Code-structure: single alphabetical list; renumbered 255; 255 + appendix >407; alphabetical inside 600/700 blocks; fixed-offset homophones | All rejected (36 inversions; rank order reversed; 303 must be alliance not Münster; D K S B H P C not alphabetical; no constant offset) |

## 5. The code-structure model and its screening criterion

What the 17 distinct codes (26 tokens) permit, from the local analysis (code-structure/output.txt,
reproducible with `python3 -I code_structure.py` from outside the folder):

- Key 255 (1666) is organised by category and rank: sovereigns 180–190, electors/princes 200–225,
  countries 226–236, regions 237–273, Kreise 274–281, towns 282–308, alphabetical vocabulary 309–386,
  numerals 387–407. The 1672 codes fit neither a single alphabetical dictionary (36 inversions), nor a
  renumbered 255 (601 Dennemarck < 768 Schweden reverses 255's rank order), nor 255 + appendix (303 must
  be the feminine noun *alliance*, which is 311 in 255; 303 = Münster there; the writer never used an
  available 255 code for Frankreich/Hollandt/Holstein/Dennemarck).
- What fits is a purpose-built list in topical hundreds blocks: 300 vocabulary (alliance 303, same
  A-words as 255's 309–311), 400 titles (Herzog 427; 447 an unresolved title/qualifier), 500 powers
  (Frankreich 576), 600 the Danish–Brandenburg negotiation (601 Dennemarck, 602 [Kayser], 625
  Statthalter [Ahlefeldt], 630 Blumenthal, 634 Holstein, 641 Plön, 651/653 Churbrandenburg – 15 of 26
  tokens), 700 northern powers (768 Schweden, 774 Hollandt, 775 General Staaten), 800 Berlin 829 and
  Rex Daniae 834 (country and sovereign as separate entries is the family norm; the 834 gloss literally
  reads "Rey Danae").
- Caveat (from the verifiers): the model is built from the glosses it is meant to test, fixes no value
  independently, and its cleanest form re-reads occurrence 21 (447, grade H) as 427. It is a search aid
  only.

**Screening criterion for any candidate key scan (10 seconds):** accept for closer reading only a
numeric list that (1) runs above 834, (2) has Dennemarck at 601 with Kayser (or Römischer Kayser /
Österreich) beside it at 602 in a non-alphabetical parties block, (3) shows Holstein 634 or
Churbrandenburg 651/653, and (4) starts its vocabulary around 300 (alliance ≈ 303). Reject purely
alphabetical runs, lists ending below 834, French dictionaries, and the 1236-type lists
(601 = le Pretendant / Gnad, 768 = lar, Holstein 666, 576 = Bremen). Do not require "König in
Dennemarck" at 601; a second Denmark-king entry in the 800s (834) is expected.

## 6. Open questions

1. Is the code at the head of letter-cipher passage B 768 or 678? (scan zoom; section 2.4)
2. Does the slot alignment "Hauß" over 447 / "Braunschw." → "Kayser" over 602 hold on source/full/0004.jpg?
   Is 447 a title/qualifier (Römisch, Kayserlich, Haus) or an article? (section 2.4)
3. Which HStAM series holds Lincker's relations to Hedwig Sophie of 1675–76 (Fabricius's "Rel. 15/4"), and
   is a key or gloss sheet filed with them? Is 177 = Reyne Mère from a key or an archival gloss?
4. Does HStAM 4 d Nr. 1237 (DECODE 4741/4742) contain a 1670s numeric list?
5. Which Arcinsys sub-nodes of "Dänemark" (g201874) hold Dänemark 120–135 (1670–1676), do any have scans,
   and which other files share the Vorprovenienz "Kanzler Vultejus, Paket 5"? What are the fondsIds of
   HStAM 4 d and 4 f Staaten B?
6. Whose key is enclosed in Celle Br. 76 Nr. 127 (1674)? Do Celle Br. 92 Nr. 122/124 or NLA WO 2 Alt
   2837/2838 contain any Hessian key? Where is the Celle-side record of the 1676 contact named on key
   255's endorsement (Celle Br. 76 has no 1676 file)?
7. Do Ribbeck's unread pp. 31–48 (FBPG 13) or Decker 1981 pp. 297/312 give HStAM signatures for Lincker's
   1672–75 reports (which would identify further enciphered Lincker files)?
8. Does TKUA Brandenburg-Preussen hold a Lincker report to Copenhagen from April/May 1672, and is any
   Hessian–Danish correspondence 1670–73 in TKUA Hessen A II no. 20 enciphered with a Hessian key?
9. Do HCP key ids 57–91 / 152–205, or keys approved after 23 Sept 2026, include a Marburg key? (rendered
   portal only)
10. Google Books, HathiTrust and MDZ were not actually searched (quota / Cloudflare / no API); a human or
    browser-enabled pass should repeat "Lincker" Vultejus and "Linckern" Dänemark 1672 there.
11. Does the 1672 list begin at 300 (like key 253's 300–409 list) or also carry a 180–299 section the
    letter does not use? Are 651/653 two entries or doubled homophones? Which hand wrote the black glosses,
    and did the glosser hold the key (the Latin "Rey Danae"/"Sueco" suggest an informed reader)?

## Files

- `leads.json` – raw inputs of all seven angles incl. verification votes.
- Sub-folders `hcp-siblings/`, `arcinsys-hessen/`, `printed-sources/`, `code-structure/`,
  `hannover-celle/`, `danish-side/`, `community-prior/` – each with MANIFEST.md (URL, UTC date, sha256).
