# HCP1217 — Pest, Sándor, the dance school and billiards

**Status: solver-complete with localized scribal uncertainties.** This card has not had an independent full-text review. Work date: 2026-10-12.

Solver: OpenAI GPT-6. Postcard dated 2 October 1912, addressed to Tóth Jolánka; sender not identified in the portal.

## Source and method

[HC Portal record](https://crypto.hcportal.eu/dashboard/cryptograms/1217) was visibly **Not solved**. General, Description and Attachments were read. Both postcard sides are preserved in `source/`; the portal supplied no transcription or solution. See `SOURCES.md` for attachment URLs and hashes.

The text is Hungarian written with a graphic monoalphabetic substitution. The working alphabet was transferred from this workspace’s HCP1301/HCP1243 readings and tested manually against this separate card. Repeated greetings and unrelated coherent passages support the transfer; they do not resolve every handwritten symbol. Accents can modify the same base symbol; joined `gy` and `cs` require care.

The following is an editorial reading with spaces and punctuation, not an exact symbol-by-symbol transcript. Square brackets mark alternatives, supplied letters or gaps. No external plaintext was used for these passages. The AI Register search for `jolanka` returned “No matching contributions” among 37 contributions on the work date; that limited check does not prove that no historical solution exists elsewhere.

## Hungarian reading

Kedves Jolánkám! Kívánom, hogy jó kedvében találja soraim. Hogy mulatott vasárnap? Én délelőtt bementem Pestre, voltam Sándornál, de a többivel nem be[s]zélhettem, mert Újpesten voltak. Délután útra elmentem, és ekkor jöttem a táncziskolából, és elmentünk egy ki[csit?] biliárdozni. Abból lett a vasárnap. [Ezzel?] bezárom soraim. Isten vele, édesem.

Under the stamp: Isten vele, édesem! Jó mulatást kívánok, és gondoljon néha rám, hű kedvesére.

## English translation

My dear Jolánka! I hope my lines find you in good spirits. How did you enjoy yourself on Sunday? In the morning I went into Pest and visited Sándor, but I could not speak with the others, because they were in Újpest. In the afternoon I set out, and then I came from the dance school, and we went to play billiards [for a little while?]. That was my Sunday. [With that?] I close my lines. Farewell, my darling.

Under the stamp: Farewell, my darling! I wish you a pleasant time, and think sometimes of me, your faithful sweetheart.

## Uncertainty and remaining work

The whole main message and all eight stamp lines have a reading. Direct shape transcription resolves row 12 as `utra`, not the previous conjecture `újra` (“again”). Row 16 visibly has `ki` before `biliardozni`; `[csit?]` is an editorial suggestion, not missing image data magically recovered. Row 18 visibly reads approximately `eze`, with the intended closing connector inferred as `ezzel`. Row 9 has `bezel`, interpreted as `beszél`; doubled consonants and many accents are normalized. H/p remains a visual near-homograph. This is a complete semantic solver claim with local scribal uncertainty; only the shared key, not this particular card, has independent review.

## Working key

At this scan resolution h/p are near-homographs and sometimes require linguistic context; d/n can also differ only by stroke length. The shape names below describe tendencies, not a guaranteed visual classifier. This qualification follows the independent HCP1301 review that arrived during this batch.

| Named graphic class | Letter |
|---|---|
| two-bars | a |
| six | b |
| left-bowl | c |
| joined-two-strokes | d |
| three-bars | e |
| cross | f |
| open-loop-descender | g |
| two-tall-strokes | h |
| dotted-crossed-curve | i |
| inverted-T | j |
| section-mark | k |
| wave | l |
| three-short-strokes | m |
| two-short-strokes | n |
| cursive-loop | o |
| tall-short-stroke | p |
| F | r |
| right-bowl | s |
| gamma | t |
| x | u |
| chevron | v |
| low-descender | y |
| crossed-diagonal | z |
| two-bars:acute | á |
| three-bars:acute | é |
| dotted-crossed-curve:acute | í |
| cursive-loop:acute | ó |
| cursive-loop:diaeresis | ö |
| cursive-loop:double-acute | ő |
| x:acute | ú |
| x:diaeresis | ü |
| x:double-acute | ű |

## Reproduction from a manual graphical transcription

```sh
python3 batches/jolanka-next-five-2026-10-12/visual-ledgers/decode.py 1217
```

This checks the original scan hash and decodes `work/as-seen.txt`, a shape-token transcription manually made from the scan and its crops. It is not OCR and is not blind: the previous reading was known. Unlike the prior editorial serializer, no plaintext-to-token program creates this ledger. Near-homographs remain `{h|p}` in the output; spelling expansions belong only to the normalized reading. `as-seen-provenance.json` contains the shape legend. All 19 main rows and eight stamp rows are included.

The corrected main reading has been compared to top.png and rows-12-19-detail.png, and the eight stamp rows to stamp.png. The user waived repeated review of the already validated shared key. No independent full-card review, FINAL or register submission is claimed here.

## Archived source provenance

# HCP1217 sources

Captured 2026-10-12 through the rendered portal General, Description and Attachments tabs. Status: **Not solved**.

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1217

- picture.jpg: https://api.hcportal.eu/media/3711/conversions/cpc_1912-10-02_HU__HU_Jasz-Arokszalas_jolanka-31_pic-large.jpg ; SHA256 96c196a4331b4c98628795b61bfe16602b5ac53bbf4b7d05bd0cd9c665d37ebd
- address.jpg: https://api.hcportal.eu/media/3712/conversions/cpc_1912-10-02_HU__HU_Jasz-Arokszalas_jolanka-31_adr-large.jpg ; SHA256 a9cb7a508b252b3c85ddcb34be7b2bca0270279d15810616492b5ed69bc80815
