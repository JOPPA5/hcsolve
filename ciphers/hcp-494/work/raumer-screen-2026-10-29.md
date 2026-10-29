# Raumer family file: bounded primary-image screening, 2026-10-29

This follows `enclosure-context-2026-10-28.md`. The independently read phrase in HCP494 is **“der Anhaltische Secretarius Raumer … die beylage Lit. B.”** The new file is a concrete archival lead, not an expanded cipher key or an identification of that enclosure.

## Material and coverage

Official reference: **Landesarchiv Sachsen-Anhalt, Z 44, A 9a IIa Nr. 62**, filmsignatur 5914; [catalogue](https://recherche.landesarchiv.sachsen-anhalt.de/Query/detail.aspx?ID=502883), [public METS delivery](https://recherche.landesarchiv.sachsen-anhalt.de/xslt/index.aspx?xml=Z_44__A_9a_IIa_Nr_62-producer.xml).

The manifest lists 111 scans. All **107 available thumbnail layouts** were inspected in numbered contact sheets, followed by **28 complete DEFAULT scans** selected for dates, signatures or chronological boundaries. MAX scans 2 and 18 were inspected to clarify the cover and a 1673 closing. Selected DEFAULT pages: 2, 9, 12, 13, 15–20, 22, 24, 28, 32, 36, 41, 51, 63, 67, 74, 78, 83, 87, 93, 98, 103, 107, 109. A helper independently screened the last eleven of these; its exact readings and caveats are in `raumer-screen-2026-10-29/later-date-triage.md` and JSON.

Scans **5, 6, 8, 11** failed with HTTP500 in THUMBS, DEFAULT and MAX. Their individually listed PDFs were then fetched once each: all four are valid PDFs, but their manuscript pages are placeholders stating **“Digitalisat nicht verfügbar”**. No manuscript was recovered; see `raumer-screen-2026-10-29/pdf-gap/manifest.json`. Consequently, this is not a visual review of all 111 scans.

## Actual dated material near the target period

Two distinct texts visibly have year **1673**:

- **15 right–17 left:** a French letter whose opening reads *Berlin le [19?] Juin 1673*. Day uncertain; the closing appears signed Raumer, but the initials are not expanded here.
- **17 right–18 left:** a heavily revised German draft, with salutation to a Freiherr / Herr Baron. MAX closing establishes **1673**; the tentative month is *Januarij*, the stacked day pair is unresolved, and place is unestablished (possibly *Regenspurg*). The earlier quick *Nov* reading is withdrawn. The subscription is a formula/abbreviation rather than a securely identified Raumer autograph.

Neither was positively identified as the enclosure B mentioned in the Hamburg letter of 4/14 May 1672. The date on 18 left belongs to the preceding draft, **not** the new letter on 18 right; the latter ends on 19 with year1685. This distinction prevents a false chronological association across a scanned spread.

Other early checks: 12 left is a Georg Raumer closing from Dessau, year1665; 13 is Dessau 21 April1675; 19 gives1685; 22 gives1686. Selected later dates fall mainly in1690–1693. Later exceptions: page107 has probable heading1676; page109 is Heidelberg1667 with signature **Ephraim Jonathan Raumer**. All uncertain day/month readings remain explicit in JSON. In particular, the first day-pair guess15/25 on page36 was withdrawn on crop review; the crop suggests18/28 but is retained as tentative.

## Two catalogue discrepancies clarified from the cover

MAX scan2, a later archival cover, explicitly lists Friedrich Gottfried von Raumer **1673/86**, and Ephraim Jonathan Raumer **1667**. This supports interpreting catalogue strings1673–1786 and1607 as transcription errors. The cover itself still calls the former **Gottfried**, so it does not settle his identity against biographical sources using **Gottlieb**. The cover is archival metadata written on the file, not a contemporary dating authority for every enclosed document.

## Result and limits

The lead yielded new primary correspondence and bounded chronological evidence, but **no new confirmed HCP494 plaintext, numerical code value, full nomenclator or enclosure B**. No obvious cipher-key/table layout was found in the available thumbnails. That does not exclude short cipher insertions: thumbnails are too small for that claim, and bodies were not exhaustively transcribed. Likewise, failure to positively recognize Hamburg, Lincker or Vultejus in selected scans is not a name-absence result.

A1673 letter can discuss1672 events; its date alone cannot disqualify a relationship. Conversely, being in a Raumer family file does not establish that its author is the secretary named by Lincker. The four unavailable early scans leave a real gap. No key mapping is inferred from any of this context.

## Reproducibility

`raumer_screen_2026_10_29.py` retrieves only exact URLs listed by the public METS, records hashes/errors and assembles contact sheets. `raumer-screen-2026-10-29/early_date_crops.py` reproduces the inspection crops with original pixels and nearest-neighbor integer enlargement. `raumer-screen-2026-10-29/summarize_screen.py` verifies all downloaded image hashes and all431 pre-existing source hashes, then writes `raumer-screen-2026-10-29.json`. Readings are manual observations, not OCR results or algorithmically proved dates.

All work is confined to these uniquely named `work/` artifacts. Source, current solution, notes, decoders and markers were not modified.
