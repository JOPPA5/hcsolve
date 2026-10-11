# Sources
- `source/metadata.md`: parent solver's live three-tab browser reading2026-10-11, https://crypto.hcportal.eu/dashboard/cryptograms/332 . Status Not solved, including Unsolvable tag and note about key not included; recorded as source claims.
- `source/cryptogram.jpg`: copied unchanged from browser-downloaded /Users/tomaspavuk/Downloads/39081655399535-large.jpg . Displayed URL https://api.hcportal.eu/media/925/conversions/39081655399535-large.jpg . This is the portal's displayed1024px large conversion, not the original upload. No solution encountered or searched.
- Context read2026-10-11: Antal, Zajac and Grošek, *Diplomatic Ciphers Used by Slovak Attaché During the WW2*, HistoCrypt2020, https://ep.liu.se/ecp/171/004/ecp2020_171_004.pdf . Read existing parent-saved text at batches/analysis-395-396/context-paper.txt without modifying that file. Sections2.1–2.3 describe C, XQ/R and machines; not a published HCP-332 solution. Cipher C specifically reverses plaintext order before grouping, and its documented header includes C+random letter/date/letter count; TRC alone does not establish this system.
- Independent Slovak/German model resources and licenses: batches/scoring-sol61/SOURCES.md and german/source/, gathered for generic language scoring; not target plaintext/solution sources.

## Primary Enigma experiment sources (2026-10-11; no target solution)

- https://py-enigma.readthedocs.io/en/latest/guide.html : author documentation and exact communication vectors, plus ring/window convention.
- https://github.com/gremmie/enigma : untouched MIT licensed simulator downloaded from codeload master to work/enigma/vendor/py-enigma.zip; source/license retained. Independent verification/control generation only.
- https://www.ciphermachinesandcryptology.com/en/enigmatech.htm : Dirk Rijmenants technical account, rotor wiring, displayed-letter turnover and double-step sequence.
- https://www.cryptomuseum.com/crypto/enigma/files/enigma_wiring_catalog.pdf : declassified NSA primary catalog, wide reflectorA wiring EJMZALYXVBWFCRQUONTSPIKHGD. Permutation/involution checked, not inferred from faulty shorthand.
- https://github.com/raymas/enigma-cipher-machine : author implementation README commercial rotor/entry/reflector constants; downloaded main source/license to work/enigma/vendor/raymas.zip. Correctly instantiated unchanged simulator used for cross-checks; its incomplete commercial unit test is not a published successful vector.
- https://cryptocellar.org/pubs/enigvar.pdf : corrected author copy of Hamer/Sullivan/Weierud1998 Enigma Variations. Saved work/enigma/vendor/enigvar.pdf/text; independent historical distinction of settable and stepping reflector and Swiss rewirings. It does not identify HCP332.

Retained vendor SHA256 hashes in work/enigma/provenance.json. Original cryptogram source/ files unchanged. No published target solution was sought.
