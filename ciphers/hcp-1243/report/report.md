# HCP1243 — full main-message reading, with marked handwriting uncertainties

## Claim
Hungarian monoalphabetic graphic substitution, using the same alphabet as HCP1301. The complete main text is now read, including the lower love verse and final instruction. One overwritten letter and the cramped last line remain paleographically uncertain; normalized spellings must not be confused with additional visible cipher signs. Independent review confirms the main-message reading; qualifications below incorporate its findings.

The source is the archived postcard address side, dated 17 May 1912 in portal metadata (the scan instead appears to show 27 February 1912), addressed to Tóth Jolánka. The publication audit found no exact solution in its bounded search. The earlier 174-cell statistical scout was incomplete and is superseded by this manual source comparison.

## Key

The h/p shapes are near-homographs at this resolution and sometimes require context; d/n can differ mainly in stroke length. The named classes describe tendencies, not a deterministic image classifier.
See `work/graphic-key.json`. The shape-token legend is reproduced below. Two versus three horizontal bars distinguish a/e; long joined strokes d, separate long strokes h and short strokes n must not be merged. Vowel accents remain above the graphic signs. Cursive joined gy is two letters.

| Plain | Graphic class | Plain | Graphic class |
|---|---|---|---|
| a | two horizontal bars | b | 6-like |
| c | left bowl | d | two joined long strokes |
| e | three horizontal bars | f | cross |
| g | open loop with descending stroke | h | two separate tall strokes |
| i | crossed curved stroke, normally dotted | j | inverted T |
| k | section-sign-like curve | l | wave |
| m | three short strokes | n | two short strokes |
| o | cursive loop | p | tall stroke with short companion |
| r | F-like | s | right bowl |
| t | gamma-like corner | u | x-like cross |
| v | chevron | y | low descending curve |
| z | crossed diagonal | | |

## Hungarian plaintext, normalized
Brackets identify a disputed reading or editorial grammatical supplementation. Other doubled consonants and accents are normalized; the command below displays the saved manual reading and its editorial flags.

> Szeretett édes Jolánkám! Tudatom, hogy szerencsésen megérkeztem. Mindjárt az útba[n] találkoztam avval az egyénnel, kinek azt a lapot adtam, de ő azt állí[t]ja, hogy ő bedobta azt a lapot. Lehet, hogy még megkapja, lehet, hogy nem.
>
> Egy pár szóval kifejezni,\
> hidd el, babám, nem lehet,\
> hogy vagy a szívemhez nőve,\
> s hogy mennyire szeretlek.
>
> Isten vele a távolból. Ezentúl ügyelje[n] a bélyeg melletti számra.

The last sentence is the writer's irregular Hungarian as far as it can be read, not silently repaired to a polished sentence. Its sense is to pay attention to the number beside the stamp; a red `20` is visible above/right of the stamp area. The verse reading `hidd el` resolves the previously confusing sequence of cursive strokes.

## English translation
My beloved, dear Jolánka! I am writing to let you know that I arrived safely. On the way I met the person to whom I had given that postcard, but he claims that he posted it. Perhaps you will still receive it; perhaps not.

A few words cannot express — believe me, my darling — how close you have grown to my heart and how much I love you.

Farewell from afar. From now on, pay attention to the number beside the stamp.

## Reproduction from an as-seen graphical transcription

```sh
python3 batches/jolanka-next-five-2026-10-12/visual-ledgers/decode.py 1243
```

The command checks the original address-side scan hash, reads the manually observed graphical tokens in `work/as-seen.txt`, and applies the explicit shape key. It prints all 18 main-message rows, preserving the blot, overwritten F/corner, merged short strokes and ambiguous final marks. The legend and provenance are in `work/as-seen-provenance.json`. This is manual transcription followed by deterministic decoding, not OCR. The earlier plaintext and review were already known, so this is not a blind independent transcription.

The former `manual-edition.json` is retained as an older editorial serialization and is not the input of this command. The new ledger is directly entered shape tokens, not generated from a plaintext string. H/p ambiguities remain in the output; grammatical and spelling repairs are confined to the normalized text. The independent correctness evidence is Claude Opus 5.5's sign-by-sign reading in `review/REVIEW1.md`.

## Remaining uncertainty and scope
- Row 8 has an overwritten F/gamma-like form: `alí{t|r}ja`. Context supports `állítja` (claims), but the t/r ambiguity remains explicitly in the diplomatic output.
- `utba`, `alítja`, `béjeg`, `melett{i|o?}` and the missing n in `ügyelje[n]` are not silently converted into perfect source spelling. The final sign may instead be o; normalization of `béjeg` to `bélyeg` is lexical, not a newly observed glyph.
- The ordinary cursive note is scoped separately from the cipher. On reinspection, the reviewer’s provisional reading is plausible: `Isten ön- / nel cso- / kolom / számtalan- / szor / szeretet- / tel De…`. English: “God be with you; I kiss you countless times; with love, De…”. Ink across the printed emblem weakens the middle words; the signature remains unresolved. Do not identify the sender as Dezső or Deri from this scan alone.
- The printed picture-side verse is ordinary Hungarian, not ciphertext.
- The main cryptogram is solved with the localized qualifications above. The ordinary cursive signature remains unresolved and is explicitly outside the encrypted-message claim. The existing REVISE findings have been addressed; no second independent review or external register submission is claimed.

## Verification gain
The earlier `leve... tőlem` hypothesis was wrong. The actual row is `lehet hogy nem`, following `lehet hogy még megkapja`. `ládát` was also wrong: the same p sign used in the companion card yields `lapot`. Shared alphabet agreement across both cards and coherent complete continuations provide substantially stronger evidence than the earlier opening-only language score.

## Response to review 1
1. **As-seen transcription:** completed as `work/as-seen.txt`. The independent shape-to-letter decoder now consumes that ledger directly. There is no plaintext-to-token generation in this path, and the provenance explicitly discloses that previous readings were known.
2. **Row 16:** the source ledger contains a blot followed by `) T E V E L E`, decoding to `{blot}stevele`. Initial i and missing n are editorial repairs in normalized `Isten vele` and are not invented source signs.
3. **Stamp note:** re-examined; the legible provisional passage and English translation are quoted above. The exact signature is unresolved and is scoped out, as the reviewer allowed. No sender name is attributed from it.
4. **Postmark:** the apparent 27 February 1912 reading and conflicting portal 17 May 1912 date are both disclosed. Source metadata remains immutable.
5. **Key:** h/p near-homography is carried explicitly into the new decoder output. d/n stroke-length ambiguity is documented.
6. **Ending:** row 17 ends with `END-I/O`, row 18 with `BARS2/3`, rather than forcing the intended wording into the ledger. The merged n-cluster in row 15 is also flagged. Accents remain less certain than base letters.
7. **State:** the review-requested documentary work is complete. Closure relies on the existing independent confirmation of the main message and the addressed REVISE findings, under README step 5; the reviewer files are untouched. The user's instruction avoids another review of the same confirmed key.

Solver: OpenAI GPT-6. Independent reviewer: Claude Opus 5.5, review 1 dated 2026-10-12.

## Archived source provenance

# Sources for HCP 1243

Captured 2026-10-12. Status observed: Not solved. All three portal tabs inspected.

- metadata.md: rendered General, Description and Attachments at https://crypto.hcportal.eu/dashboard/cryptograms/1243
- picture.jpg: https://api.hcportal.eu/media/3789/conversions/cpc_1912-05-17_HU__HU_Jasz-Arokszalas_jolanka-22_pic-large.jpg (downloaded through image viewer, unchanged) SHA256 5efe093aaa70675818816e273537fba79446e31753f9d60716abd1898dcbde57
- address.jpg: https://api.hcportal.eu/media/3790/conversions/cpc_1912-05-17_HU__HU_Jasz-Arokszalas_jolanka-22_adr-large.jpg (downloaded through image viewer, unchanged) SHA256 f716e782be6ee3140dc27debfa7db88831693343f88bf1e2397acaedf61b691c

## Prior-solution audit
AI Register https://ai.hcportal.eu/register/ searched on 2026-10-12 by identifiers 1243, 1301, 917, 975, 1000 and names jolanka, fritzsalmen, heidelberg, Jessze: 0 matching contributions for each. Exact-name web searches returned no exact solution. Absence from searched sources does not establish global absence.
