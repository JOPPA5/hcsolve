ACCEPT

# Review 1 – HCP 1081 (reviewer: Claude Opus 5.5, 2026-10-30)

## What I verified and how

1. **Single command.** `python3 -I ciphers/hcp-1081/work/decipher.py` from the repo root: source SHA-256 4/4 OK, output exactly as quoted in SOLUTION.md ("am very busy please / excuse and would / write if had time / your with / all love / Jack + x").
2. **Independent decoder.** `review/work/my_decode.py` holds my own transcription of the six body rows (typed from my crops, not copied from the script) and decodes by reversing word order and the letters of each word. Same result: *am very busy please excuse and would write if had time your with all love Jack*. My transcription is identical to `work/transcription.txt` (checked programmatically: True).
3. **Transcription against the scan.** `review/work/crop.py` (PIL: grey, autocontrast, contrast x2, rotate 38°, enlarge x2 and x5) on `source/address.jpg`; crops `body.png`, `big.png`, `r1a.png`, `r1b.png`, `w2.png`, `w3.png`, `r2.png`, `r3.png`, `r4.png`, `r5.png`, `r6.png`. Checked every row sign by sign:
   - B1 `esaelp` – e, peaked s, o-like a, e, l, long-descender p: fits. `ma` – blotted m + a: fits.
   - B1 words 2/3 (the solver's new reading). Word 2 as written: y, peaked s, u, then a closing bowl with a tall rising stroke on the **right**. Word 3: y, r-hump, e, looped v. A b written mirror-wise has its ascender on the right – exactly what is seen, and the same mirroring is seen on every d (finding 1). So `ysub` / `yrev` is supported by the letter forms, not only by context; the alternative order ("am busy very") is not favoured by the pixels.
   - B2 `dluow dna esucxe` – fits; x as two opposed arcs is visible.
   - B3 `emit dah fi etirw`, B5 `evol lla`, B6 `kcaJ` (k like N, J with looped descender) + separate cross: fit.
   - B4 `htiw ruoy` – h like "lt", fits; `ruoy` see finding 2.
   - Plain header "Dear M / Just a card / thanking you / for letter" agrees with the scan.
4. **Coverage.** Every body letter is in the transcription; one rule (reverse each row) applies to all six rows; nothing left over, no restorations claimed or needed.
5. **Language/context.** Idiomatic Edwardian postcard English continuing the plain header; postmark "...ON-THE-SOL[ENT]" JY 8 11 and addressee Miss M. Jallett, Fareham agree with metadata and the greeting "Dear M".
6. **Sources.** `work/schrodel-2021.txt` contains no Fareham/Solent/Jallett/1911; portal had no solution attached. Prior GPT partial work is credited.

## Findings

1. **minor** – SOLUTION.md says the letters "are normal English cursive, not mirrored glyphs". That is not quite right: every `d` (`dluow`, `dna`, `dah`) is written as a mirrored d (looks like b, ascender on the left), and the final b of `ysub` is mirrored (ascender on the right, looks like d). This partial glyph mirroring should be stated; it is also the best visual evidence for the B1 `ysub`/`yrev` order and should be cited under Uncertainty 1.
2. **minor** – B4 `ruoy`: after the y descender the stroke rises into a small u-like tail; I agree no separate s is visible (an s would sit at the start, `sruoy`, and the first letter is a single r-hump). The disclosure ("your", not "yours") is adequate; keep it.
3. **minor** – Type label: the card is line-wise reversed writing with partly mirrored letter forms; for the register entry use something like "Reversed writing" (category Transposition on the portal), not "Mirror writing" alone.

## What I could not verify

- Only the 1024 px portal scan exists; the blotted m of `ma` and the loose y-words rest on that resolution.
- The writer's identity (Jack) and the recipient beyond the address cannot be checked externally.
- No exhaustive search for a published solution beyond the Schrödel 2021 paper and the portal page.
