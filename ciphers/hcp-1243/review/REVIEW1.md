REVISE

# Review 1 — HCP 1243 (requested by the human before any DONE marker)

Reviewer: claude-opus-5-5, 2026-10-12. **Protocol note:** this directory has no `DONE1`, so by the README it is still the solver's turn. The human asked for a review of the current `SOLUTION.md` directly, so I wrote this file but did **not** create `REVIEWED1`. If the solver later creates `DONE1`, this review should be treated as already delivered for that state of the files.

Short version: **the reading of the main cryptogram is correct.** I re-read all rows from `source/address.jpg` and get the same text. The open points are the same kind as on HCP 1301 (the transcription is derived from the plaintext), one inserted letter, an unchecked date, and the plain-text note under the stamp, which is more legible than the solver says and appears to contain a signature.

## What I verified and how

1. **The documented command.** `python3 batches/postcards-five-2026-10-12/verification/decode.py 1243` runs, the image hash matches, output is byte-identical to `work/diplomatic-reading.txt` (18 rows).
2. **Where the tokens come from.** As for 1301: `verification/build_editions.py` builds `verified-edition.json` from the hard-coded plaintext. Finding 1.
3. **Independent reading of the scan** (4× strips and 6–7× details in `review/work/`, made with `crops.sh` / `zoom.sh`), using only the shape table from `../hcp-1301/SOLUTION.md`:

   | Row | My reading | vs. solver |
   |---|---|---|
   | 1 | szeretettédesjolán | same |
   | 2 | kámtudatomhogysze | same |
   | 3 | rencsésenmegérkez | same |
   | 4 | tem.mindjartazutba | same (there is a full stop after `tem`) |
   | 5 | találkoztamavval | same |
   | 6 | azegyénnelkinekazt | same |
   | 7 | alapotadtamdeőazt | same |
   | 8 | alí[overwritten F/Γ]jahogyőbedob | same, disclosed |
   | 9 | taaztalapotlehet | same |
   | 10 | hogymégmegkapja | same |
   | 11 | lehet[blot]hogynem. | same |
   | 12 | egyparszóvalkifejezni | same |
   | 13 | hiddelbabam,nemlehet | same |
   | 14 | hogyvagyaszivemheznőve | same |
   | 15 | shogyme(nn)yireszeretlek. | same; the n-strokes are run together |
   | 16 | [blot]**stevele**atávolból | **differs** — finding 2 |
   | 17 | ezentulügyeljeabéjegmelett? | same; last sign unclear |
   | 18 | szamr? | same up to the last sign (two or three bars) |

4. **Key consistency.** Same alphabet as HCP 1301, sign for sign; the rare signs agree across the two cards (bold cross = f in `kifejezni` here and `fel` there; `6` = b in `babám`, `bedobta`; `( )` = cs in `szerencsésen`). The z / u pair (crossed X vs plain x) is cleanly distinct in `az utba`, row 4.
5. **Language and context.** Coherent, idiomatic Hungarian; the verse is a regular four-line rhyme (`lehet` / `szeretlek` is an assonance typical of album verse). Addressee on the card is `Tóth Jolánka`. A red `20` is indeed written in the top right corner beside the stamp field, which fits the closing instruction about "the number beside the stamp".

## Findings

1. **major — the reproduction command round-trips the answer** (identical to finding 1 of the HCP 1301 review). Disclosed by the solver, but it means no step in the repo goes from the card to the text. The ledger should be an as-seen sign transcription. The braces/brackets `{t|r}` and `[i]` are carried as `literal:` tokens, which only works because the ledger was written from the plaintext.

2. **major (transcription) / minor (meaning) — row 16: there is no `n` in `Isten`.** Detail `review/work/z-row16.png`: after the blot the signs are `) Γ ≡ Λ ≡ ~ ≡` = `s t e v e l e`; nothing stands between `≡` and `Λ`. The solver's diplomatic row has `istenvele`. `Isten vele` is certainly meant, but the `n` is a restoration (and the initial `i` is under an ink blot). Both must be listed with the other repairs; `SOLUTION.md` currently claims the diplomatic output "preserves" what the scan supports.

3. **major — the under-stamp note is more legible than stated, and it is signed.** `SOLUTION.md` says only `Isten önnel` is secure and leaves the rest "unresolved". In `review/work/z-stamp.png` I read, in ordinary cursive: `Isten ön- / nel cso- / kolom / számtalan- / szor / szeretet- / tel De…` — "God be with you, I kiss you countless times, with love, De…". The last word is a short name beginning `De` (`Dezső`? `Deri`? — I cannot settle it at this resolution). This is not cipher, but it is the **sender's signature**, and the portal lists the sender as Unknown. It matters for the context section of the report for both cards. The lines `csókolom` and `számtalanszor` run across the printed stamp-field emblem and are the weakest part of my reading; treat it as a second opinion to be checked, not as established.

4. **minor — the date was taken from the portal and not checked against the card.** The postmark (`review/work/z-postmark.png`) reads `…ÁROKSZÁ… 912 ?EB 27`. The only Hungarian month abbreviation ending in `EB` is `FEB`, so the postmark appears to be **27 February 1912**, not 17 May 1912 as in the portal metadata and in `SOLUTION.md`. The first letter of the month and the first digit of the day are weak, so I do not claim this is certain — but the solution should report what the postmark shows and flag the discrepancy rather than repeat the metadata.

5. **minor — h/p near-homographs** (same as finding 4 on HCP 1301). Row 9 has `lapot` and `lehet` next to each other with p and h drawn as the same "tall stroke + tick". Both are fixed by context; the key description should admit it.

6. **minor — the last two rows are less secure than the text suggests.** The final sign of row 17 looks like the loop (`o`) at least as much as dotted `i`; the last sign of row 18 may have three bars (`e`). `bélyeg melletti számra` is the natural reading and I have no better one, but `[i]` alone understates it. Also `ügyelje` has no final `n` on the card, and `alí?ja` has one `l` — both already disclosed.

7. **minor — state.** `NOTES.md`/`SOLUTION.md` describe this as a full reading "with localized qualifications" but no `DONE1` exists, while HCP 1301 has one. Either hand it over properly or label it partial; right now it is neither.

## Assessment

The main message is solved; I would not expect its meaning to change. Before a `DONE1` I would want: an as-seen transcription with row 16 corrected, the postmark date addressed, and the under-stamp note either transcribed (with the signature) or explicitly scoped out with its legible part quoted.

## What I could not verify

- Accents (same limitation as on 1301: 1024 px scan).
- The overwritten sign in row 8 — both `F` and `Γ` strokes are present; I cannot say which was written last.
- The signature under the stamp and the two middle lines of that note.
- The first letter of the month in the postmark.
- Whether a decipherment was published elsewhere; I relied on the solver's search in `SOURCES.md`.
