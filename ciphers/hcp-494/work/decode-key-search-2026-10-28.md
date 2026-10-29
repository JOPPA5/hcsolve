# DECODE key search: public coverage and access limits

Date: 2026-10-28. Research helper: `danish_witness`; parent solver: `root`.

## Result

The public DECODE catalogue exposes a much broader image inventory for HStAM 4 d 1236 than the eight images previously observed in the official Arcinsys delivery. This establishes an additional collection to inspect, not a new decipherment of HCP 494. The public thumbnails are sufficient to identify two existing keys by page layout, but not to read new key values reliably.

The most useful crosswalk is **HCP key 266, existing page 25 → DECODE R4706, gallery P2**. R4706 includes five gallery images, three further text pages and a cover among them. After this identification, the parent solver independently inspected HCP key 266 and observed **four publicly accessible larger pages, 25–28**. The `key_266` helper is handling that independent HCP copy. No new key values from those pages are claimed in this note.

## Public catalogue coverage

Starting point: [DECODE records](https://de-crypt.org/decrypt-web/RecordsList). Searches used the ordinary public search form with `cmd=search`, the indicated `search` string, and an empty `searchtype`.

| Search | Observed results relevant to this investigation |
| --- | --- |
| `1234` | Four Marburg records: R4687, R4688, R4690, R4691; 16 gallery thumbnails total. |
| `1236` | 51 results overall; 46 Marburg records named `Hstam_4_d_nr_1236_01` through `_46`; 124 gallery thumbnails total. The five other results were excluded from this image survey. |
| `Lincker` | The public result page says “No records found”. This does not establish that the collection contains no Lincker material. |
| `Celle` | Three displayed records: R3907 and R3905 in the British State Papers, and R1141 in Modena. None is a Marburg result. No detailed examination of those unrelated manuscripts was undertaken. |

All 50 relevant record pages and their **140 literal public thumbnail URLs** were saved. All nine contact sheets covering the 140 thumbnails were visually inspected for page layout and obvious key-family features. Download size is 2,165,494 bytes. The images are approximately 200 pixels wide; enlarging them does not restore missing writing detail. No full-resolution DECODE manuscripts were obtained.

The 46 Marburg 1236 catalogue entries display a start year of **1715**. For example, R4706 and R4707 additionally describe the material as from the second half of Landgrave Karl's reign. The four 1234 entries display the broad range **1600–1699**, with additional information describing them as likely mid-seventeenth-century material. These are catalogue dates and descriptions, not independently established dates for every manuscript page. No specific 1660s date was found in the surveyed 1236 metadata.

Gallery image counts sometimes exceed the metadata's “No. of Pages”: R4706 has five gallery images but four pages in the metadata; R4719 has three gallery images but two pages in the metadata. This note counts actual gallery image references, including covers.

## Verified visual crosswalks

| Existing local witness | DECODE record and image | Evidence and limit |
| --- | --- | --- |
| `source/key266-0025.jpg` | [R4706, Hstam_4_d_nr_1236_14](https://de-crypt.org/decrypt-web/RecordsView/4706), [P2 thumbnail](https://de-crypt.org/decrypt-custom/filesrv/?file=TH_IMG_R4706_I27646_P2.jpg) | Matching whole-page geometry, alphabet table, null-number lines, two-column word list and folds. This is a visual identification of the same manuscript page, not a pixel-identity claim. |
| `source/key255-0013.jpg` | [R4691, Hstam_4_d_nr_1234_04](https://de-crypt.org/decrypt-web/RecordsView/4691), [P3 thumbnail](https://de-crypt.org/decrypt-custom/filesrv/?file=TH_IMG_R4691_I27592_P3.jpg) | Matching table, syllable signs, lists and page geometry. This is the known key 255, not a newly discovered matching key. |
| `source/full/key255-0016.jpg` | [R4691](https://de-crypt.org/decrypt-web/RecordsView/4691), gallery P4 | Matching known cover/docket. The existing larger scan contains the Lincker 1666 / Celle 1676 inscription; those words were not newly deciphered from the tiny DECODE thumbnail. |

Comparison image: `decode-key-search-2026-10-28/key255-key266-crosswalk.jpg`. It compares existing local scans with enlarged public thumbnails. Enlargement is for layout comparison only.

R4706 gallery image names are `TH_IMG_R4706_I27646_P1.jpg` through `P5.jpg`. P2 is the existing HCP 266 page 25; P1, P3 and P4 are additional text pages; P5 is a cover/docket. The page ordering in DECODE should not be assumed to equal HCP page numbering without a crosswalk.

Other layouts screened include ordinary alphabet and word-list keys, multi-page nomenclators, and matrix tables. R4707 is an adjacent eight-image record with a visually related presentation. None of these thumbnail surveys establishes that its alphabet, syllable signs or numeral values match HCP 494. No candidate plaintext was inferred from unreadable entries.

## Access boundary

The record pages explicitly show **“Access mode: Authentication required”**. The parent solver made an ordinary browser click on a thumbnail at [R4719](https://de-crypt.org/decrypt-web/RecordsView/4719). Its full-image display reported **“Insufficient permissions to so see the full image”** (wording reported by the parent from the rendered UI).

After that observation, only the literal thumbnail `src` URLs already public in the record pages were downloaded. No full-image URL variants were requested, no login was performed, and no terms were accepted. No attempt was made to bypass that restriction. The parent has asked the user whether an authorized DECODE account is available; no account availability is established by this helper's evidence.

The independent [HCP key 266 page](https://crypto.hcportal.eu/dashboard/cipher-keys/266) is a separate public source. The parent observed its General, Description and Attachments and reports four larger images, pages 25–28. Following that source is the current lawful route to readable versions of the known key's additional pages. It does not change the DECODE permission result.

## Saved evidence and reproducibility

All files are under `work/decode-key-search-2026-10-28/`:

- `queries.json`, `search-*.html`, `1236-record-index.json`: search evidence and result inventory.
- `R*.html`: all 50 relevant public record pages.
- `record-gallery-index.json`: record names, URLs, gallery files, counts and observed access labels.
- `thumbnail-manifest.json`: each literal public URL, local path, byte count and SHA-256.
- `ordered-thumbnails.json`: contact-sheet order. A filename ending `_P.jpg` represents an unnumbered gallery image, not a manuscript page numbered zero.
- `thumbnails/`: the 140 public thumbnails.
- `sheets/001-016.jpg` through `sheets/129-140.jpg`: all nine visually screened sheets.
- `key255-key266-crosswalk.jpg` and `crosswalk.json`: page-identification evidence and its limits.

No files in `source/`, no shared solution or notes, and no state markers were changed by this subtask. HCP 494 remains unsolved by this investigation: the advance is a verified crosswalk and access to a broader key inventory, with the readable HCP 266 follow-up delegated to the other helper.
