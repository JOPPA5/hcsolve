# Danish-side key search, 2026-10-29 (Claude subagent)

Angle: Rigsarkivet (TKUA Hessen, Griffenfeld, cipher-key series) and Danish printed sources, looking for the expanded 1672 Hessian nomenclator or a Danish deciphered copy of a Lincker report. Everything here is untrusted downloaded data. All fetches 2026-10-29 UTC. Full SHA-256 in `sha256.txt`.

| file | URL | what it is |
|---|---|---|
| daisy-11650592.html | https://daisy.rigsarkivet.dk/arkivserie_detaljer?ngid=35775&heid=11650592&henid=11650592 | DAISY record, TKUA "Hessen: Gesandtskabsrelationer med bilag" 1537-1763 (VA XI p. 131 no. 25). Media: Original, Papir only. No scan. Contents list: Georg Lincker 1677, 1683; J. H. Lincker 1677, 1686-87. Nothing 1672. |
| daisy-11650571.html | https://daisy.rigsarkivet.dk/arkivserie_detaljer?ngid=35775&heid=11650571&henid=11650571 | DAISY record, TKUA "Hessen: Akter og dokumenter vedr. det politiske forhold" 1528-1749 (VA XI p. 130 nos. 17-20). "Dele af arkivserien er scannet" -> Arkivalieronline epid 19852381. |
| viewer-19852381.html | https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=19852381 | viewer shell for that series |
| indeks-top-19852381.json | https://api.rigsarkivet.dk/ao/v1/billedviser/indeks-top?epid=19852381 | public viewer index: only folders "1528 - 1564" and "1587 - 1663" are scanned. The packet 1670-1749 (Dalwig 1670, Habbaeus 1671, Brunswick alliance 1673, J. H. Lincker 1676 ...) is NOT scanned. |
| ep-beskrivelse-19852381.json | https://api.rigsarkivet.dk/ao/v1/billedviser/ep-beskrivelse?epid=19852381 | series description for the viewer |
| daisy-search-griffenfeld.html | https://daisy.rigsarkivet.dk/arkivskaber_eller_arkivserie_liste?soegetekst=Griffenfeld | DAISY search attempt; returned only the search form (no result rows). Not pursued further. |
| dl-jorgensen/jorgensen-griffenfeld-kb.pdf (39.2 MB, 583 pp.) + jorgensen.txt (pdftotext) | https://www.kb.dk/e-mat/dod/130022060261-bw.pdf | A. D. Jørgensen, Peter Schumacher Griffenfeld (Kbh. 1893-94), Royal Library digitisation (one volume). Grepped for Lincker/Linker/Lynker/chiffer. |
| dl-runeberg-dnt6/0680.html ... 0700.html | https://runeberg.org/danotrak/6/NNNN.html | Danmark-Norges Traktater VI (1665-1675), Laursen 1923, OCR pages 668-688 = chronological list and index. Grepped for Hessen/Kassel/Lincker/Chiffer. |

## Results (negatives included)

- No Danish holding found that is scanned online and could contain the 1672 Hessian key or a deciphered Hessian report.
- TKUA Hessen relations (11650592): Lincker reports only 1677, 1683 (Georg) and 1677, 1686-87 (J. H.); unscanned.
- TKUA Hessen political acts (11650571): the 1670-1749 packet is unscanned; the scanned part stops in 1663.
- Jørgensen, Griffenfeld: Lincker appears only as Danish resident in Berlin 1674-76 ("den danske resident i Berlin, Georg Lincker"), with letters to Bierman 1674-75 cited from TKUA "Brandenburg" and "Georg Linckers indberetninger fra Jan. 75". No 1672 item, no cipher key, no Hessian cipher mentioned (the one "chiffer" hit is unrelated, p. ~9735 of the OCR).
- DNT VI index: Hessen-Kassel appears only for the marriage treaty 5 Mar 1667 (p. 164), the 12 Sep 1672 Brunswick defensive alliance (Emperor, Denmark, Brandenburg, Celle, Wolfenbüttel, Landgravine Hedwig Sophie; p. 474) and Trier's accession 12/22 Jul 1674 (p. 507). No Lincker, no cipher text, no Hessian report printed.
- Fridericia, Adelsvaeldens sidste Dage (1894) covers 1648-1660 only (archive.org adelsvaeldenssid00frid) -> irrelevant for 1672, not downloaded.
- Bidrag til den store nordiske Krigs Historie covers 1699-1720 -> irrelevant, not searched.
- HathiTrust (Cloudflare 403) and Google Books (429 / sorry-page) blocked search-inside for DNT VI; runeberg OCR used instead.
- Web searches for "Lincker" + Rigsarkivet/Griffenfeld/Hamburg 1672 returned only unrelated 18th-c. Lincker files (Sachsen-Anhalt) and the jurist N. C. von Lyncker.
