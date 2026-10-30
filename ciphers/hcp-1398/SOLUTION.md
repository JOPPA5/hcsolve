# HCP 1398 / pc_hcp_79 — Caesar −1 English love note, signed "Loo"

**Status: complete reading (51 of 51 cipher letters), review 1 verdict REVISE, findings addressed below.**
History: the manual transcription and the Caesar −1 reading were made by the OpenAI GPT solver
(GPT-6 Astra) on 2026-10-26, which left the signature initial open (M/N). Claude Opus 5.5, acting as
solver, resolved the signature on 2026-10-29 (DONE1) and made the post-review corrections.

## Origin

The portal record (General, Description and Attachments tabs, read 2026-10-26) shows status Not solved,
date unknown, recipient "W. Abboú", no attached transcription or solution. The address side, turned 90°
counter-clockwise, reads "Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon", with a halfpenny
Edward VII stamp (so 1902–1910) and a postmark "…MBORNE … 10 PM" (perhaps Wimborne; not securely read).
The cipher message stands on the address side under the plain heading "Thursday" (plus overwritten
initial-like marks and a word read as "Today"; none is cipher). The picture side is a printed scene with no
handwriting. The recipient and style match the same couple's Caesar −1 cards to W. Abbott in this repo
(hcp-1388, 1395, 1397); that link is supported but not proven.

## Key

Caesar shift: each cipher letter is one place after its plaintext letter (decrypt = shift −1).

```text
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Ciphertext (manual transcription, work/transcription.json)

```text
Nz. pxo. efbstu Cpz.
J. pomz. ibwf uijt
wjfx Jo. nz bmcvn
Zpvs. hjsm
Mpp
```

## Plaintext

```text
MY. OWN. DEARST BOY.
I. ONLY. HAVE THIS
VIEW IN. MY ALBUM
YOUR. GIRL
LOO
```

Reading: “My own dear[e]st boy, I only have this view in my album. Your girl, Loo.”
The card literally writes DEARST (`efbstu`, six letters); the E is an editorial restoration of a writer's
slip. Dots after words are the writer's and are kept.

Slovak: „Môj vlastný najdrahší chlapec, mám v albume len tento pohľad. Tvoje dievča, Loo.“

## Reproduce

```sh
python3 -I ciphers/hcp-1398/work/decode.py
```

Checks the source hashes, decodes the manual transcription with Caesar −1, prints the five literal rows,
a normalized line with DEAR[E]ST, and `51 cipher letters, all decoded with one key (Caesar -1); 0 alternatives.`
No OCR; the transcription step is manual.

## Uncertainties

- DEARST is what the card says; whether it is a slip or a skipped letter cannot be told from the ink.
- Signature initial: read as a copybook capital M (lead-in curl, three downstrokes joined by two arches),
  confirmed independently by the reviewer; `Mpp` → LOO. "Loo" as a pet form of Louie/Louisa is conjecture.
- Plain heading marks (overwritten initials, "Today"), the postmark town and date are not securely read;
  no date is recovered.
- Sender identity unknown.

## Why it is correct

One fixed shift decodes all 51 letters into idiomatic Edwardian English with no substitutions, skipped
groups or alternatives; the content fits a picture postcard, and the recipient and cipher match sister cards.
No published solution was found or used (portal: Not solved, nothing attached).

## Response to review 1

Verdict REVISE. All four findings accepted and fixed; the reading is not substantially changed.

1. **major — `efbsftu` vs `efbstu`.** Agreed. On review/work/dearest_thr.png and work/message.png the group
   is e, one looped f (doubled strokes, one descender), b, s, crossed t, u — six letters, and nothing between
   s and t descends as this writer's f always does. work/transcription.json now has `efbstu`; the decoder
   prints DEARST literally and DEAR[E]ST in the normalized line, with the restoration disclosed here and in
   the report. Letter count corrected: 50 + signature M = 51 (the earlier "51 + 1" included the phantom f).
2. **minor — command did not print LOO.** Fixed: the signature is frozen as `Mpp` in transcription.json
   and decode.py prints LOO with 0 alternatives. Re-run output:
   `signature: LOO` / `51 cipher letters, all decoded with one key (Caesar -1); 0 alternatives.`
3. **minor — self-contradictory SOLUTION.md.** Fixed: the stale "Partial, no DONE1" header, the [L/M]OO
   plaintext and the "Remaining limit" section were replaced by the current claim above.
4. **minor — context.** Added the address (Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon), the Edward VII
   halfpenny stamp (1902–1910) and the uncertain "…MBORNE 10 PM" postmark; the link to the 1907–08 couple
   and "Loo" = Louie/Louisa are stated as supported/conjectural only.
