# HCP1218 — Sunday and a masons’ dance

**Status: partial decipherment, submitted for first independent review. Updated 2026-10-14.** The stamp quotation has been identified; one main-text clause remains undeciphered. DONE1 is a handoff of this qualified claim, not a solved/FINAL designation.

## Source and method

The [HC Portal record](https://crypto.hcportal.eu/dashboard/cryptograms/1218), named jolanka106 and dated September 1912, was visibly **Not solved** when captured on 2026-10-12. The postcard is addressed to Tóth Jolánka. General, Description and Attachments were read, and both sides are preserved unchanged in `source/`. See `SOURCES.md` for the URLs and hashes. The portal was rechecked on 2026-10-14 and still displayed Not solved. Its address viewer exposed the same 1024 × 657 image.

The cipher is a Hungarian graphic monoalphabetic substitution. The alphabet was transferred from HCP1301/HCP1243 and tested against this card. The transcription is manual, with prior plaintext hypotheses known; it is neither blind transcription nor OCR. A complete spatial ledger now covers 22 main rows, seven stamp rows and the address annotation. That coverage does not mean every word has been deciphered.

The editorial text supplies spacing, punctuation and most accents. Brackets indicate significant restored letters or unresolved readings. Ordinary source spelling is retained where useful, including egésségban and tánczolni. All literal row output is in `work/as-seen-decoded.txt`; it takes precedence over editorial normalization for exact character claims.

## Hungarian editorial reading

Kedves édes Jolánkám! Kívánom, hogy a legjob[b] kedvében és egésségban találja soraim. Édesem, hogy mulatott tegnap? Remélem, [m]int rendesen, most is jól telt el a vasárnap. Ami engem il[l]et, én el voltam foglalva, mert első vasárnap volt, este pedig a kőműves mulatság volt, és pedig szüreti, de még ilyen ro[s]szu[l] nem mulattam soha, csak ép[p]en […] azt az egyet megjegyzem, hogy [33?]-szor nősültem meg négy leán[n]yal. Tánczolni egyáltalán nem tánczoltam. Mikor megy Berénybe? Az[z]al bezárom soraim, sorait várva.

Small annotation by the address: szeretettel? (editorial restoration; literal sze{r|t?}etel).

Under the stamp, source-assisted editorial reading:

Tiéd vagyok, e szív, e lélek; kit szeretnék, [ha?] téged nem sze[re]tnélek?

## English translation

My dear, sweet Jolánka! I hope my lines find you in the best of spirits and in good health. My darling, how did you enjoy yourself yesterday? I hope that, as usual, Sunday went well again. As for me, I was busy, because it was the first Sunday; in the evening there was a masons’ dance, specifically a harvest dance, but I have never enjoyed myself so little, just […] I will just mention that I “married” [33?] times with four girls. I did not dance at all. When are you going to Berény? With that I close my lines, awaiting yours.

Small annotation by the address: [with love?].

Under the stamp, source-assisted translation:

I am yours, this heart, this soul; whom would I love [if] I did not love you?

## Identification of the stamp verse

On 2026-10-14 a search for the already-decoded phrases found Sándor Petőfi’s **Honfidal**, written in Debrecen in January–February 1844. The [published text](https://www.magyarirok.hu/petofi-sandor/h/honfidal) opens:

Tied vagyok, tied, hazám! / E szív, e lélek; / Kit szeretnék, ha tégedet / Nem szeretnélek?

This is an external literary source used during decipherment, not an independently obtained complete plaintext or a previously published solution of this postcard. The card appears to adapt the patriotic stanza for a personal addressee. It omits tied, hazám and has téged rather than tégedet. Those words must not be restored to the card merely because they occur in the poem.

The previous interpretation és [s]zívelelek was a word-boundary error. The unchanged letters in S02–S03, okesziv / elelek, divide exactly as the end of vagyok followed by e szív, e lélek. No extra s or e is needed. This resolves that passage directly, while the literary parallel identifies its likely source.

For S05, ha is the source-assisted preferred reading, but h/p and a/e remain explicitly uncertain in the ledger. Two main red bars and a small lower red mark are visible. For S07, the former F T token sequence did not match the enlarged scan: the visible middle forms are T N, giving szetnelek. The editorial restoration sze[re]tnélek explains the intended conditional verb, but the two supplied letters are not visible. Possible copying or enciphering error remains an interpretation.

## Remaining uncertainty

The main text remains partial at A15–A16: after csake{h|p}en the current visual ledger reads ufogy{i|o?}t / me. The earlier unqualified úgy was not supported by a separately transcribed gy at that position and has been withdrawn. The letter sequence is not yet a coherent phrase. A17 has two digit-like signs, provisionally 33. N01 literally gives sze{r|t?}etel; szeretettel requires more than a doubled t and remains an editorial restoration. For the stamp, the opening Tiéd vagyok, e szív, e lélek now follows the unchanged S01–S03 letters exactly (accents and word boundaries editorial). S05 is h/p plus a/e-shaped bars; ha is strongly supported by the published poetic parallel but not established by pixels alone. S07 reads szetnelek on renewed inspection: the middle shapes are a corner and two short strokes. The editorial sze[re]tnélek supplies re; the omitted signs are not visible. The adaptation and possible writing error must not be replaced by an unqualified copy of the published stanza. First independent review is requested for this explicitly partial decipherment. No complete-solution claim, FINAL or register entry.

The main clause was retested as fogott meg, fogyott and fojt meg. None accounts securely for the observed signs and line break; none has been promoted into the translation. Repeating an enlarged or colour-thresholded view adds no source detail.

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



## Reproduction and evidence boundary

Run from the repository root:

```sh
python3 batches/jolanka-next-five-2026-10-12/visual-ledgers/decode.py 1218
```

This checks the archived address image hash and decodes the manually observed shape tokens into literal row text. It preserves uncertain tokens and does not silently supply letters from the poem. It does not itself read pixels or independently prove the manual transcription. The ledger is `work/as-seen.txt`, its coverage and limitations are in `work/as-seen-provenance.json`, and the earlier excerpt ledger is retained unchanged in `work/as-seen-excerpts.txt`.

`python3 batches/jolanka-next-five-2026-10-12/check_readings.py 1218` checks all three archived source hashes and prints the editorial claim. That second command is an integrity check, not cryptanalysis. Earlier readings are retained in the numbered JSON snapshots, including `reading-before-pass6.json`.

## Seventh-pass check, 2026-10-14

The disputed A15 shapes were compared at the same scale with f in foglalva (A09) and gy in hogy (A17). The cross and joined descending pair support the current f and gy classifications; they do not support silently changing the fragment to fogott meg. The last loop remains i/o-ambiguous. See `work/gap-comparison-pass7.png`.

`work/compare-gap.py` regenerates those source crops and records ten manually proposed conjectures in `work/gap-candidates-pass7.json`. It measures ordinary letter edit distance only, ignoring accents and spaces. The proposed úgy fogott meg needs five letter edits from either current literal alternative; no candidate was accepted. Edit distance is neither a language probability nor a decipherment proof. A possible writing error or a remaining transcription error cannot yet be distinguished.

The portal still displayed Not solved. Its full image viewer exposed the same 1024 × 657 address image and no higher-resolution download control. Focused searches for the card label did not locate a relevant published transcription. The linked collection article's abstract was accessible, but its PDF could not be retrieved; that failure does not show that the article lacks relevant evidence. No additional plaintext has been claimed in this pass.

## First-review handoff and acceptance boundary

This solver edition is ready for independent inspection, but its decipherment is explicitly partial. Repeated reinspection by the same solver has not resolved A15/A16. Rather than silently repair that phrase, the handoff preserves the literal candidates, source crops and failed conjectures. A DONE1 marker requests review of the claim as stated; it must not be interpreted as complete recovery of the message. No register entry or FINAL is appropriate on the present evidence.

Please read all 22 main rows, seven stamp rows and the annotation from the archived scan before comparing with the ledger. Priority questions:

1. A15/A16: is the current ufogy{i|o?}t / me segmentation correct? Check both the overflow beyond the vertical margin and the beginning of the next row. Are any signs omitted, joined, overwritten or misclassified? Context alone has not yielded an acceptable reading.
2. S05: inspect the long-stroke group and horizontal bars without substituting the expected ha from Honfidal. S07: check the corner and two-stroke group behind szetnelek, and whether the proposed missing re is justified.
3. N01: test literal sze{r|t?}etel against the editorial szeretettel. The extra letters are not claimed to be visible.
4. A17: test the two apparent digits 33 independently. The “married four girls” anecdote is a literal interpretation, not evidence that the digit reading must be correct.

Earlier key acceptance on other cards does not independently confirm this card’s glyph transcription. A reviewer’s reading may correct the solver’s ledger, as happened on 1213 and 1217. Until the remaining substantive fragment is resolved, this report must remain labelled partial even if the shared substitution key is accepted.
