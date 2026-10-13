# HCP1217 — Pest, Sándor, the dance school and billiards

**Status: independently reviewed; required corrections incorporated.** Updated 2026-10-14. Local scribal uncertainties remain disclosed.

Solver: OpenAI GPT-6. Postcard dated 2 October 1912, addressed to Tóth Jolánka; sender not identified in the portal.

## Source and method

[HC Portal record](https://crypto.hcportal.eu/dashboard/cryptograms/1217) was visibly **Not solved**. General, Description and Attachments were read. Both postcard sides are preserved in `source/`; the portal supplied no transcription or solution. See `SOURCES.md` for attachment URLs and hashes.

The text is Hungarian written with a graphic monoalphabetic substitution. The working alphabet was transferred from this workspace’s HCP1301/HCP1243 readings and tested manually against this separate card. Repeated greetings and unrelated coherent passages support the transfer; they do not resolve every handwritten symbol. Accents can modify the same base symbol; joined `gy` and `cs` require care.

The following is an editorial reading with spaces and punctuation, not an exact symbol-by-symbol transcript. Square brackets mark alternatives, supplied letters or gaps. No external plaintext was used for these passages. The AI Register search for `jolanka` returned “No matching contributions” among 37 contributions on the work date; that limited check does not prove that no historical solution exists elsewhere.

## Hungarian reading

Kedves Jolánkám! Kívánom, hogy jó kedvében találja soraim. Hogy mulatott vasárnap? Én délelőtt bementem Pestre, voltam Sándornál, de a többivel nem beszélhettem, mert Újpesten voltak. Délután útra elmentem, és akkor jöttek a táncziskolából, és elmentünk egy ki[csit?] biliárdozni. Ebből állt a vasárnap. [Ezzel?] bezárom soraim. Isten vele, édesem.

Under the stamp: Isten vele, édesem! Jó mulatást kívánok, és gondoljon néha rám, hű kedvesére.

## English translation

My dear Jolánka! I hope my lines find you in good spirits. How did you enjoy yourself on Sunday? In the morning I went into Pest and visited Sándor, but I could not speak with the others, because they were in Újpest. In the afternoon I set out, and then they came from the dance school, and we went to play billiards [for a little while?]. That is what my Sunday consisted of. [With that?] I close my lines. Farewell, my darling.

Under the stamp: Farewell, my darling! I wish you a pleasant time, and think sometimes of me, your faithful sweetheart.

## Uncertainty and remaining work

All 19 main rows and eight stamp rows are covered. Row 12 reads utra; the translation keeps “I set out”. Row 16 ki is expanded only tentatively as ki[csit?]. Row 18 eze is interpreted as [Ezzel?]. The source Ujbesten (b) is normalized to Újpesten (p). Row 13 ends in a small curved sign: k is preferred to s; it is not m, and jöttek is the adopted reading. Row 17 eböl alt is normalized to Ebből állt. Row 8 has an exceptional looped initial S and an n under a pink smudge, flagged in the ledger. Accents and doubled consonants are editorial; h/p remains a near-homograph. Independent review by Claude Opus 5.5 accepted the decipherment subject to these corrections and explicitly waived another round.

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

The corrected main reading has been compared to top.png and rows-12-19-detail.png, and the eight stamp rows to stamp.png. Independent full-card review is now available in review/REVIEW1.md. Its conditional acceptance permits closing after the listed corrections; no external register submission is claimed.

## Response to review 1

Reviewer: Claude Opus 5.5, REVISE dated 2026-10-14. The reviewer accepted the decipherment subject to the specified corrections and requested no further review round if they were made. The following changes were checked against the original-image crops, not copied into a generated glyph ledger.

1. Corrected row 13 to és akkor jöttek: two bars give a; the final curved sign is preferred k, not the former three-stroke m. English now says “then they came from the dance school”. The residual k/s shape ambiguity is disclosed.
2. Added the visible right bowl in row 9, giving beszel. Removed the false claim that the source omitted s.
3. Recorded the six-shaped b in row 10: Ujbesten is the literal spelling; Újpesten remains the editorial place-name normalization.
4. Corrected row 17 to eböl alt, normalized Ebből állt: “That is what my Sunday consisted of.”
5. Flagged row 8’s looped initial capital-S variant and the partly obscured n. The name Sándor is retained.
6. Kept the literal utra, ki and eze forms and their stated translation boundaries.
7. The earlier PDF was a working solver edition. It has been rebuilt with the corrections and review outcome. No watcher is started because the user explicitly instructed that sandbox watchers must not be used; markers are checked manually.

The reviewer also read Budapest’s departure postmark as 2 October 1912 and the arrival as 3 October, consistent with the catalogue date and the Jászárokszállás address. The corrected plaintext and preserved source scans remain the evidential basis; source-hash checks alone do not establish a decipherment.

## Archived source provenance

# HCP1217 sources

Captured 2026-10-12 through the rendered portal General, Description and Attachments tabs. Status: **Not solved**.

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1217

- picture.jpg: https://api.hcportal.eu/media/3711/conversions/cpc_1912-10-02_HU__HU_Jasz-Arokszalas_jolanka-31_pic-large.jpg ; SHA256 96c196a4331b4c98628795b61bfe16602b5ac53bbf4b7d05bd0cd9c665d37ebd
- address.jpg: https://api.hcportal.eu/media/3712/conversions/cpc_1912-10-02_HU__HU_Jasz-Arokszalas_jolanka-31_adr-large.jpg ; SHA256 a9cb7a508b252b3c85ddcb34be7b2bca0270279d15810616492b5ed69bc80815
