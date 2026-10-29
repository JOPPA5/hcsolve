# Danish archival witness search, 2026-10-28

Research helper to the HCP 494 solver. This note records new source discovery, not a decipherment. It does not alter the target transcription, key, plaintext claims, immutable `source/`, or review state.

## Main result

A previously unexamined **309-image collection of original cipher keys** is publicly available from Rigsarkivet: **Tyske Kancelli, Udenrigske Afdeling, Chiffer (1670-1709)**, old reference **TKUA Almindelig del 3, no. 112**, Vejledende Arkivregistraturer XI p. 49. DAISY explicitly says the entire series is scanned. The catalogue date is approximate and the description says it is a mixture of many cipher keys. This is a new candidate corpus, **not evidence that a matching HCP 494 key is present**.

- [DAISY series 2132747](https://daisy.rigsarkivet.dk/arkivserie_detaljer?ngid=35775&heid=2132747&henid=2132747)
- [Scan viewer, image 1](https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=19852193#260610,48691476)

The live rendered viewer displayed **1/309** and the same collection title. Its public navigation script supplied the page-index and image-reference endpoints. These are the Danish archive's public viewer resources, not the HC Portal API. All 309 image URLs were returned by the image-reference listing; no image identifiers were guessed.

Downloaded scans: `danish-witness-2026-10-28/keys/001.jpg` through `309.jpg`, **357,208,875 bytes** total. `download-manifest.json` records each viewer page, observed public URL, local relative path, byte count and SHA-256. `key-image-references.json` and `key-index-bs.json` preserve the archive's listings. `fetch_keys.py` downloads only those URLs. `contact_sheets.py` makes numbered, downscaled screening sheets without changing scan content. Root and other helpers are screening disjoint ranges; their visual findings belong in separate notes.

## Lincker letters: more precise information weakens the 1672 witness lead

The full [VA IX inventory](https://www.rigsarkivet.dk/wp-content/uploads/2022/06/Vejledende-Arkivregistraturer-IX-Privatarkiver-fra-tidsrummet-1660-1800.pdf), printed p. 38 (PDF page 44), lists **14 letters from Georg Lincker to Conrad Biermann von Ehrenschild, 1670-84**. That range alone does not establish a 1672 letter.

The digitized detailed inventory for **Privatarkiv 5139** narrows the dates on printed p. 11 (viewer image 12): **1670 (2), 1674 (4), 1675 (4), 1676, 1680, 1683, 1684**. These sum to 14. **No 1672 letter is listed.** This is a finding about the inspected inventory, not proof that no other relevant letter survives.

- [Detailed inventory entry](https://arkivalieronline.rigsarkivet.dk/da/other/index-creator/23/1343634/23330944)
- [Inventory viewer, relevant image](https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=23330944#558916,91052827)
- [Direct relevant scan](https://api.rigsarkivet.dk/ao/v1/images/91052827)
- Local full scan: `danish-witness-2026-10-28/ehrenschild-inventory/012.jpg`.

All 22 inventory pages were downloaded and hashed in `ehrenschild-download-manifest.json`; the title page and relevant pages were visually inspected. This is a digitized **inventory**, not scans of the letters. Current [DAISY letter series 4512732](https://daisy.rigsarkivet.dk/arkivserie_detaljer?ngid=1343634&heid=4512732&henid=4512732), *Breve fra andre (1662-1697)*, showed original-paper media only. No scan link was observed on that record; do not infer undigitized everywhere.

## Other precise catalogue leads

The full [VA XI inventory](https://www.rigsarkivet.dk/wp-content/uploads/2022/06/Vejledende-Arkivregistraturer-XI-Tyske-Kancelli-II.pdf) and current DAISY records were read. Relevant pages 82-83 and 130-131 were rendered and visually checked.

| Holding | Confirmed scope | Scan observation / limitation |
| --- | --- | --- |
| [Brandenburg-Preussen, Georg Lincker's archive, series 11630681](https://daisy.rigsarkivet.dk/arkivserie_detaljer?ngid=35775&heid=11630681&henid=11630681) | 1668-73; VA XI p. 83, no. 117. Royal orders 1668-73; received letters 1670; drafts of reports 1669-70; drafts to Conrad Biermann 1669. | Original-paper media only in inspected record. The overall date span does not make its report drafts cover 1672. |
| [Brandenburg-Preussen reports, series 11630634](https://daisy.rigsarkivet.dk/arkivserie_detaljer?ngid=35775&heid=11630634&henid=11630634) | 1556-1770; VA XI p. 82 explicitly lists Georg Lincker's reports for 1670-72. | Partly scanned. The [linked viewer](https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=19852269) index lists 1556-1660 then 1693-95 and later; **no 1672 volume is listed**. Saved `relations-index-top.json`. |
| [Hamburg, report drafts, series 11644950](https://daisy.rigsarkivet.dk/arkivserie_detaljer?ngid=35775&heid=11644950&henid=11644950) | 1677-92, with 1678, 1682-83, 1685-86 and 1691 missing; VA XI p. 119 nos. 95-96. | Original-paper media only; starts five years after target. |
| [Hessen, Georg Lincker's embassy archive, series 11650600](https://daisy.rigsarkivet.dk/arkivserie_detaljer?ngid=35775&heid=11650600&henid=11650600) | 1677; credential and copies of documents about his mission; VA XI p. 131 no. 26. | Original-paper media only; not a 1672 witness. |
| [Cipher keys, series 12170240](https://daisy.rigsarkivet.dk/arkivserie_detaljer?ngid=35775&heid=12170240&henid=12170240) | 1539-1693, including an explicitly described group used from 1670 onward; named correspondents include Aizema, Tromp, Petkum, Rantzau, Reetz, Pastorius, Gjoe, Juell, Gabel, Ahlefeldt, Meyercron, Klingenberg, Lente and Schwartz. | Original-paper media only. Description dates most undated keys to late 1660s/1670s; no Lincker identified in description. No matching key inspected. |
| [Cipher keys, series 1094657](https://daisy.rigsarkivet.dk/arkivserie_detaljer?ngid=35775&heid=1094657&henid=1094657) | 1650-1848, shared by the German Chancery and later Foreign Affairs department. | Original-paper media only; broad scope, no HCP494-specific evidence. |

## Identity caution

VA XI printed p. 131 distinguishes **Georg Lincker** (reports 1677, 1683) from **Johan Henrik Lincker** (reports 1677, 1686-87). The latter's mission also appears on p. 130 under 1676. The target record's secretary Linker/Lincker must **not** be silently identified with either man. This search found no signature, explicit cross-reference or handwriting comparison establishing the target sender's given name. Shared surname and diplomatic context are research leads only.

## Preservation and access limits

- All new downloads and generated screening artifacts are under `work/danish-witness-2026-10-28/`. No existing source file was changed.
- The two inventory PDFs exceeded the web tool's size limit; direct public downloads succeeded. Text extraction was supplemented by visual checks of material pages.
- No original Lincker letter was recovered in this bounded search. No new plaintext word or numeric nomenclator assignment follows from these catalogue findings.
- A script verifies all key image files are JPEG data and records hashes. Screening is visual triage, not a transcription of all 309 pages.
- No archive staff were contacted; no orders, account actions, messages or external writes were made.
