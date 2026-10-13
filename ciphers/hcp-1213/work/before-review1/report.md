# HCP1213 - Easter greetings and moving into Pest

**Status: solver-complete semantic edition with localized scribal uncertainties.** Full-card independent review is pending. Work date: 2026-10-13.

## Source and method

The HC Portal record was marked Not solved when acquired. General, Description and Attachments were inspected; no attached transcription or solution was supplied. Both source images and metadata remain unchanged. See SOURCES.md for URLs and hashes. The catalog dates the postcard to 1913 and identifies Tóth Jolánka as recipient; the main footer now supplies the name Feri. This does not establish a surname or identify him with other uncertain signatures.

Hungarian graphic monoalphabetic substitution; the working key was transferred from HCP1301/1243 and applied directly to this separate card. Manual shape tokens cover 27 main rows and seven stamp rows. This was not a blind transcription: earlier readings were known. The computer decodes these tokens; it does not read pixels.

## Hungarian editorial reading

Szeretet[t] édes Jolánkám! Kívánom, hogy a legjobb egésségben találja soraim. Hogy teltek a húsvéti ünnepek? Remélem jól, jobban mint nekem. Első nap voltam Szolnokon, második napon szabad voltam, és így voltam öntözköd[ni] a szomszédoknál és Szentmihályon. Ez volt az összes húsvé[ti] öntözködé[…]. Sajnálom, édesem, hogy magát nem öntözhettem meg, de majd, édesem, ha feljön, el fogom végezni nekünk, édesem, akkor is jó lesz.

Tudatom, édesem, hogy már én is bemegyek Pest[re] lakni május elsejére. Nagyon kellemetlen volt eddig is; nagyon kellemetlen volt a ki[k]lakás, mert nagyon sokat kell gyalogolnom, ha éjjel érkeztem, és közelebb leszek legalább magához. Isten vele, édes, a boldog viszontlátásra! Imádja Feri.

Under the stamp: Számtalanszor csókolja sírig hű kedvese, [F…i?].

## English translation

My beloved, sweet Jolánka! I hope my lines find you in the best of health. How were the Easter holidays? Well, I hope, better than for me. On the first day I was in Szolnok; on the second day I was free, so I went Easter sprinkling at the neighbours’ and in Szentmihály. That was all of my Easter sprinkling [word ending unclear]. I am sorry, my darling, that I could not sprinkle you, but later, my darling, when you come up, I shall do it for us, my darling; it will still be good then.

I am letting you know, my darling, that I too am moving into Pest to live there by the first of May. It has been very unpleasant until now; living out there [source kiklakás] was very unpleasant, because I have to walk a great deal when I arrived at night, and at least I shall be closer to you. Farewell, my darling, until our happy reunion! Feri adores you.

Under the stamp: Your sweetheart, faithful until death, kisses you countless times, [F…i?].

## Uncertainties and normalization

The main message is semantically covered; the full shape ledger includes every main and stamp row. Row 11 has an uncertain suffix after öntözködé; row 8 omits an expected ni, and húsvé lacks ti. Source forms masodok, szubad, edig, nagyosokat, akor, kozeleb and kiklakás are preserved in the literal output and normalized or disclosed in this edition. Pest[re] supplies an absent case ending. The phrase nekünk, édesem is read literally rather than replaced with a guessed activity. The main footer independently reads imadja feri; the cramped stamp signature remains uncertain despite that evidence. h/p remain a graphic near-homograph. This is a solver claim, not an accepted independent review.

Accents, spaces and punctuation are editorial where not plainly present. The original period spelling egésség is retained. Easter sprinkling is supported by the repeated source öntöz-/öntözköd- forms, not an imported poem. The opening question now reads hogy teltek; the previously missing closing line reads viszontlatasra imadja feri. The literal accommodation form kiklakás is interpreted as living outside the city, in the context of moving into Pest and long walks; that interpretation is explicitly distinguished from the letters.

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


## Reproduction

From the repository root:

```sh
python3 batches/jolanka-next-five-2026-10-12/visual-ledgers/decode.py 1213
```

The command checks the original address scan SHA-256, reads work/as-seen-full-pass4.txt and prints all 34 literal rows with uncertainty markers. work/as-seen-decoded.txt stores the same output. The normalized Hungarian and English above are editorial; they are not emitted by pretending an OCR system exists. Source crops top.png, bottom.png, promise-full-pass4.png and end-0/1.png show the disputed and newly resolved positions.

## Validation and review status

All three archived source hashes pass check_readings.py. The shape decoder accounts for all regions of cipher text; the uncertain final stamp name and row-11 suffix remain visible. Repeated greetings, multiple place names, the Easter account, relocation date and final signature support the reading. No independent full-card acceptance is claimed, and no register entry or FINAL is created. Prior intermediate readings and failed hypotheses remain in work/ and NOTES.md.

## Archived source provenance

# HCP1213 sources

Captured 2026-10-12 through the rendered portal General, Description and Attachments tabs. Status: **Not solved**.

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1213

- picture.jpg: https://api.hcportal.eu/media/3699/conversions/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-108_pic-large.jpg ; SHA256 32d9c28494c868f41c7ca3886227e7d762eba855633726a979892dcb41b89c94
- address.jpg: https://api.hcportal.eu/media/3700/conversions/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-108_adr-large.jpg ; SHA256 791dd148567031c0959ab6b71b0f231538ce594cfa5de5eb957f3e1f97feb42c
