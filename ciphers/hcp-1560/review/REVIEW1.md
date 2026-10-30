REVISE

# Review 1 — hcp-1560 (pc_hcp_241), Pepouš to Anna Tichá, 17 March 1903

Reviewer: Claude Opus 5.5, 2026-10-29. Own scripts and crops are in `review/work/`.

## What I verified and how

1. **The solver's command.**
   `/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1560/work/decode.py`
   **Fails** at once:
   `AssertionError: ('../SOLUTION.md', 'canonical record changed')`. The
   "Completion and handover" section was added to SOLUTION.md after
   `record-sha256.json` was frozen. The command prints no plaintext at all (finding 1).
2. **My own decryption** (`review/work/mydecode.py`). It applies the family key
   from `ciphers/hcp-1520/work/key.json` directly to `work/transcription.txt`. Its output
   (`review/work/mine.txt`) is byte-identical to `work/literal.txt`. Every
   cipher label in the transcription is in the key, so no glyph is left unmapped. The key
   is the family key unchanged: the 22 classes in use are the hcp-1520 labels, and v/F is unused.
   The decoding is therefore consistent with the transcription. The problems are in the
   transcription itself.
3. **Source check.** I rotated `source/picture.jpg` with ROTATE_270 (674×1024) and made
   crops enlarged 3–10× (`review/work/upright.png`, `U1/U2/U3*.png`, `R08b`, `R09b`, `R10b`,
   `R10lis`, `R01dik`, `band0–5`). I compared all rows at 2× with the transcription and
   compared the disputed signs sign by sign.

## Findings

1. **major — The documented command does not run, and it would not produce the claimed plaintext.**
   Once SOLUTION.md was edited, the decoder's SHA guard on its own record files fails.
   Even with the guard passing, it decodes `transcription.txt`, which still contains
   `⟦U1⟧ ⟦U2⟧ ⟦U3⟧`. It also asserts 509 units, so it cannot output the completed reading
   (MUSELA / JE / A) that the Completion section claims. README step 4 requires a single
   command that produces the full plaintext. Fix: put the restorations (marked as
   restorations) and the corrections below into the transcription, and regenerate or drop the
   self-hash manifest so that editing SOLUTION.md does not break the command.

2. **major — BICH ×3 and BIL are misreadings. The source has the 1/Y sign: BYCH, BYL.**
   In R08 `p1ř p18`, R09 `p1ř` and R10 `p1ř`, the sign after `p` is the flagged
   numeral-1 form. That is the same sign as in `f1r3f5d4` (VYHOVETI, same row R08) and in
   `d4c4s5h1` (TISICERY, R01). It is not the open-topped "ч"-like 4 seen in
   `d4c4s5`, `bh4f4m28` (PRIVINUL, R09) or `f6cm4f5` (VASNIVE, R10), which sit beside it
   on the same rows (`review/work/R08b.png`, `R09b.png`, `R10b.png`, `R01dik.png`). The
   solver says the I/Y controls "support retaining BICH/BIL literally". The pixels show the
   opposite. Four labels `4`→`1` need correcting. The "editorial I→Y repairs" for these
   words then disappear: the source spells them correctly.

3. **major — LISOVAL is a misreading. The word is `b2c3f68` = PUSOVAL ("pusoval",
   colloquial "kissed").** R10, before `, 6q p1`: the first sign has the tall
   ascender loop of `b` (P), not the closed double loop of `8` (L). Compare it with the
   `8` at the end of the same word. The second sign is the looped `2` (U), as in `6m2mg6`,
   not `4` (`review/work/R10lis.png`, 6×). This gives "tak dlouho bych tě vášnivě
   pusoval", which fits the card's own "tisíc dlouhých pus". The Completion section turns
   literal LISOVAL into "líbal [sic]", and the earlier sections into "lisoval / tisol".
   Both are unsupported glosses on a wrong transcription and should be removed.

4. **minor — U1/U2/U3: the restorations are supported by pixels. U3 is undersold, and
   the files are inconsistent about all three.**
   - U1 (R03): `q5 n2c586` is plainly legible through the light grey overprint
     (`U1.png`). **MUSELA** is read, not guessed. Agreed.
   - U2 (R06): a single smudged sign after `7`/J. At 10× its flagged top matches `5`
     (`U2z.png`). **JE** is acceptable as a damaged reading.
   - U3 (R10): under the dark smudge between `c3p5` and `d6g` there is a single sign with an
     upright stroke curling into a lower loop, consistent with `6` = A (`U3.png`,
     `U3z.png`). The Completion section calls A "restored from context … weakest point".
     It is a damaged but visible sign. Label it that way, as a damaged reading.
   - The upper sections of SOLUTION.md still call all three "opaque", with "length
     unasserted" and "no letter assigned", and `uncertainties.json` has `unit_count:
     null`. This contradicts the Completion section. Make them consistent.

5. **minor — SOLUTION.md contradicts itself.** The heading and early sections say
   "partial … not an accepted or complete decipherment" and give the counts 509/516. The
   last section says "complete reading". The Slovak translation still follows the old
   reading ("azda musela", "tisol", BICH). After fixes 1–4, rewrite these as one
   consistent current claim with updated counts, and give the translation of the corrected
   text.

6. **minor — Attribution.** Earlier work is credited to "root"/"solver team" without
   naming the model. Per the run brief, the earlier transcription is GPT (Astra/Sol) work
   and the completion is Claude Opus 5.5. Say so explicitly. The family key / Egorov partial
   study credit is present and adequate. No target-specific published solution appears to
   have been used.

## Corrected reading (for the solver to verify, not adopt blindly)

… že musela ulehnouti … Chřipka je zákeřná nemoc … Kéž **bych byl**, zlato moje, u
tebe! Přivinul **bych** tě takto vřele k sobě a tak dlouho **bych** tě vášnivě
**pusoval**, až by Anunka řekla, že již je úplně zdráva …

The rest of the transcription agrees with the source in my row-by-row 2× comparison. Spot
checks at 3–5×: R01, R08 (KEZ, VYHOVETI), R09 (PRIVINUL, TAKTO), R10 (VASNIVE), and the
signature rows R13–R15 (DLOUHYCH, PUS, POSILA, VECNE TVUJ, PEPOUS). The language is natural
Czech of c. 1903. The names (Anunka = Anna Tichá, Pepouš) and the place (Žirovnice u
Počátek, teacher) fit the family. The date 17.III.1903 is plain text on the card.

## What I could not verify

- The q/g distinction at every occurrence. The family key has no G, so a g/q swap would
  show up as Z/K. I checked KEZ, ZANETU and ZAKERNA visually only at 2–5×.
- Small accent-like marks: I did not test whether they are encoded.
- The exact postmark dates and the address alteration (not cipher content).
