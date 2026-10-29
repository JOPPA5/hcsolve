- g201874.html | https://arcinsys.hessen.de/arcinsys/showItemsList.action?nodeId=g201874 | 2026-10-29T07:51:42.246473Z | sha256 ded7da2c119d045dd8b85eac2a9be0fe269584302e873387a0e810f13f27e59d | arcinsys HTML page
- g143363.html | https://arcinsys.hessen.de/arcinsys/showItemsList.action?nodeId=g143363 | 2026-10-29T07:51:42.466318Z | sha256 c1c79e52af59301717f46fceba30a74d420b418f47dee3aa10e946d44c59f32e | arcinsys HTML page
- table_g143363.json | https://arcinsys.hessen.de/arcinsys/itemsList_queryTableData_RD.action?nodeId=g143363 (POST) | 2026-10-29T07:53:21Z | sha256 1cfee712eb22d7322b45d883d70e80e361c6948e529a853afaaa53c647c5099a | DataTables JSON of navigator node
- ids/*.html | https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=3352600..3352665 | 2026-10-29T07:53:38Z | record detail pages (sha256 via shasum ids/*)

## Batch downloads (2026-10-29, Claude subagent, angle: arcinsys-hessen)
- fonds/<id>.html | https://arcinsys.hessen.de/arcinsys/showFondsDetails.action?fondsId=6790..6850 | 2026-10-29T07:57:10Z | fonds detail pages (6830 = 4 f Staaten D, 6831 = Staaten E, 6791 = Staaten C; HStAM 4 d not in this range)
- cp_143363.html, cp_201874.html | showClassificationPointDetails.action?classificationPointId=143363 / 201874 | classification point pages (no item lists, server-rendered header only)
- page_*.html, ajax_*.html, table_*.json, table2_*.json, simple_Linker*.html/json, idsearch_D126.html | navigator / search attempts; all item-list requests returned 'Arcinsys | Fehler' (10076-byte error page)
- apd_*.html | archivportal-d.de searches/item | blocked by Anubis JavaScript proof-of-work (no content)
- cj*.txt | curl cookie jars (session only)

## Method note
Record detail pages (showArchivalDescriptionDetails.action?archivalDescriptionId=N) are server-rendered and fetchable with curl; the 'Digitalisate öffnen' link (digitalMediaViewer.action?archivalDescriptionId=N) marks online scans. All LIST views (navigator nodes, simple search, signature search) are DataTables fed by POST itemsList_queryTableData_RD.action / search_doSearch.action with a 'tableStateJson' body + CSRF; every variant tried returned the generic error page, so sibling enumeration by hierarchy was not possible without a browser. Arcinsys IDs are not assigned by signature order (IDs 3352580-3352700 mix 4 f Staaten D/E, HHStAW, HStAD), so brute-forcing neighbours of 3352629 found only 15 other Dänemark records (11, 29, 38, 51, 100, 107, 144, 169/187, 188, 193, 218, 235, 248 - none 120-135, none Linker, none with scans).
sha256 of every file: see sha256sums.txt
