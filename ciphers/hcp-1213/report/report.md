# HCP1213 - Easter greetings and moving into Pest

**Status: ACCEPT in independent review 2; final edition.** Updated 2026-10-14.

## Source and method

The HC Portal record was marked Not solved when acquired. General, Description and Attachments were inspected; no attached transcription or solution was supplied. Both source images and metadata remain unchanged. See SOURCES.md for URLs and hashes. The catalog dates the postcard to 1913 and identifies Tóth Jolánka as recipient; the main footer now supplies the name Feri. This does not establish a surname or identify him with other uncertain signatures.

Hungarian graphic monoalphabetic substitution; the working key was transferred from HCP1301/1243 and applied directly to this separate card. Manual shape tokens cover 27 main rows and seven stamp rows. This was not a blind transcription: earlier readings were known. The computer decodes these tokens; it does not read pixels.

## Hungarian editorial reading

Szeretet[t] édes Jolánkám! Kívánom, hogy a legjobb egésségben találja soraim. Hogy telt el a húsvéti ünnepek? Remélem jól, jobban mint nekem. Első nap voltam Szolnokon, második napon szabad voltam, és [víg?] voltam öntözköd[ni] a szomszédoknál és Szentmihályon. Ez volt az összes húsvé[ti] öntözködés. Azt sajnálom, édesem, hogy magát nem öntözhettem meg, de majd, édesem, ha feljön, el fogom végezni. Nekünk, édesem, akkor is jó lesz.

Tudatom, édesem, hogy már én is bemegyek Pest[re] lakni május elsejére. Nagyon kellemetlen volt eddig is; nagyon kellemetlen volt a kis lakás, mert nagyon sokat kell gyalogolnom, ha éjjel érkeztem, és közelebb leszek legalább magához. Isten vele, édes, a boldog viszontlátásra! Imádja Feri.

Under the stamp: Számtalanszor csókolja sírig hű kedvese, [F…i?].

## English translation

My beloved, sweet Jolánka! I hope my lines find you in the best of health. How were the Easter holidays? Well, I hope, better than for me. On the first day I was in Szolnok; on the second day I was free and [cheerful?]; I went Easter sprinkling at the neighbours’ and in Szentmihály. That was all of my Easter sprinkling. What I regret, my darling, is that I could not sprinkle you, but later, my darling, when you come up, I shall do it. For us, my darling, it will be just as good then.

I am letting you know, my darling, that I too am moving into Pest to live there by the first of May. It has been very unpleasant until now; the little lodging was very unpleasant, because I have to walk a great deal whenever I arrived at night, and at least I shall be closer to you. Farewell, my darling, until our happy reunion! Feri adores you.

Under the stamp: Your sweetheart, faithful until death, kisses you countless times, [F…i?].

## Uncertainties and normalization

Row 11 now includes its formerly omitted ending: öntözködés azt; the suffix gap is resolved. Row 21 ends in a small s/k-like sign, preferred s, yielding a kis lakás; the former invented kiklakás gloss is withdrawn. Row 8 has an explicit UNKNOWN token for a large symmetric caret (v or insertion mark), followed by ig. Víg (“cheerful”) is preferred but qualified; the earlier így interpretation remains an alternative if the caret is nonalphabetic and the following form is gy. Row 7 reads második and szbad, with sz[a]bad editorial. Single n/b are preferred in rows 4/5; exact duplication remains uncertain. Row 15 has a blot and dot after végezni, followed by a new sentence Nekünk, édesem… . Other source forms edig, nagyosokat, akor and kozeleb remain. Pest[re] supplies a case ending. The main signature is Feri; the abbreviated stamp signature [F…i?] remains uncertain. Accents and h/p near-homographs remain qualified. Review 2 accepted the corrected decipherment; these localized uncertainties remain open.

Accents, spaces and punctuation are editorial where not plainly present. The original period spelling egésség is retained. Easter sprinkling is supported by the repeated source öntöz-/öntözköd- forms, not an imported poem. The opening question reads hogy telt el. The closing line reads viszontlatasra imadja feri. The accommodation phrase is now a kis lakás, with a disclosed s/k ambiguity in its final small sign; no invented compound is translated.

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

All three archived source hashes pass check_readings.py. The corrected shape ledger now includes the previously missed row-11 ending and row-8 caret; the final stamp name and caret remain uncertain. Repeated greetings, multiple place names, the Easter account, relocation date and final signature support the reading. Review 2 accepted the corrected full-card decipherment. A local register entry accompanies this final edition; no external submission is claimed. Prior intermediate readings and failed hypotheses remain in work/ and NOTES.md.

## Response to review 1

Reviewer: Claude Opus 5.5, REVISE dated 2026-10-14. The reviewer finds the card deciphered in substance, but requests a short second round after corrections. No FINAL or register entry is created.

1. Completed row 11 from the source strip: E:acute ) A Z T replaces the old truncated E:acute UNKNOWN ending. It reads öntözködés. Azt sajnálom… . The former suffix uncertainty and overstatement of complete transcription are withdrawn.
2. Re-examined row 21: its last small sign is simpler than the two preceding k signs. Adopted right bowl s, hence a kis lakás (“the little lodging”); k remains a local alternative. Removed the invented kiklakás gloss.
3. Corrected row 3’s final wave from K to L: telt el, not teltek.
4. Added the visible large caret in row 8 as UNKNOWN, followed by I G. Preferred víg is qualified in both languages. An insertion mark plus the earlier így reading cannot be excluded; the shape is no longer omitted.
5. Corrected második (dotted I) and szbad (one crossed sign after s, not two). Rechecked rows 4/5 and preferred single N and 6, while retaining uncertainty over doubling. Removed masodok and szubad from claimed source forms.
6. Recorded the blot and dot after végezni and separated Nekünk, édesem, akkor is jó lesz into a new sentence. English now distinguishes “I shall do it” and “For us ...”.
7. Retained the qualified stamp signature [F…i?]; the main Feri does not prove every obscured stamp stroke.
8. Added the visible address context: Tóth Jolánka, care of Pernyés Mihály, Jász-Berény, Sárkány u. 22. The postmark does not securely refine the catalogue’s 1913; the message places it after Easter and before 1 May. Rákosszentmihály is a plausible identification of Szentmihály, not an expanded word on the card.
9. The existing PDF was a working solver edition and is rebuilt for the second round. The user’s explicit no-watcher instruction overrides the repository watcher default; markers are handled manually.

Earlier claims and the exact reviewed ledger are archived in work/before-review1/. The bounded prior-solution search is recorded in SOURCES.md; its negative result is not proof of novelty.

## Response to review 2

Claude Opus 5.5 returned ACCEPT on 2026-10-14 after verifying the revised ledger and report. All nine findings of review 1 were addressed.

1. The readings kis lakás and [víg?] originated with the reviewer. The solver compared them with the same source crops and adopted them with the stated qualifications; this is not a second independent witness. The lower-resolution s/k and caret ambiguities remain.
2. Changed the English wording to “whenever I arrived at night”. The tense mixture reflects the source; no claim about additional journeys is inferred.
3. Re-examined the archived HCP1243 address-side stamp note without editing that finalized card. Its short cursive signature is compatible with Feri, including a possible capital F, but this cross-card suggestion does not establish the name or the writer’s identity. The present card’s cipher signature Feri remains the direct evidence.

The English report is rebuilt with this acceptance and the remaining qualifications. The local register entry uses solver TODO because no personal name was supplied. No external register submission, commit or push was performed.

## Archived source provenance

# HCP1213 sources

Captured 2026-10-12 through the rendered portal General, Description and Attachments tabs. Status: **Not solved**.

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1213

- picture.jpg: https://api.hcportal.eu/media/3699/conversions/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-108_pic-large.jpg ; SHA256 32d9c28494c868f41c7ca3886227e7d762eba855633726a979892dcb41b89c94
- address.jpg: https://api.hcportal.eu/media/3700/conversions/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-108_adr-large.jpg ; SHA256 791dd148567031c0959ab6b71b0f231538ce594cfa5de5eb957f3e1f97feb42c

Prior-solution search boundary: on the initial batch work date, 2026-10-12, the rendered AI Register search for jolanka returned no matching contributions among 37 entries. This was a name-only search, not an exhaustive proof of novelty. No published plaintext was used for HCP1213.
