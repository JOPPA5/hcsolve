REVISE

# Review 1 – hcp-1548 (pc_hcp_229), Czech postcard to Anna Tichá, 6.VII.1903

Reviewer: Claude Opus 5.5, 2026-10-29. Review round 1 (marker DONE1).

## Summary

The decipherment is correct. The fixed Anna Tichá family key, applied to a transcription I checked against the scan, gives coherent Czech of the period across all nine rows. The 2026-10-29 restoration of U1 as `5 2` → NEUSTALE matches the pixels and is disclosed. The deliverable still contradicts itself, though. The single reproduction command, `work/literal.txt`, `work/ciphertext.txt` and the first half of SOLUTION.md all still describe a *partial* reading with an unknown-length span ⟦U1⟧. Only the appended "Completion and handover" section claims a complete reading. These records need to be brought into line before FINAL. That is a concrete fix, not a change to the reading, so the verdict is REVISE.

## What I verified and how

1. **Solver command.** I ran `…/python3 -I ciphers/hcp-1548/work/decode.py` from the repo root. It passes all its hash and inverse checks, but its output still contains `VZPOMINAL N⟦U1⟧STALE`, "294 mapped base cipher units" and "Total cipher length UNKNOWN". It does **not** produce the plaintext that the completion section claims (NEUSTALE).
2. **Key.** `work/key.json` is byte-for-byte the family key in `ciphers/hcp-1545/work/key.json` (22 signs including ř = CH). No card-specific aliases are used.
3. **Independent decryption.** `review/work/indep_decode.py` takes the hcp-1545 key and `work/ciphertext.txt`, with `{U1}` replaced by the claimed `52`. Output:
   `TISICERY DIK ZA OBA DRAHE LISTKY A ZA VZPO- / MINKU. JA VZPOMINAL NEUSTALE. JIZ SE ME / SRDECKO NEHNEVA? … TVUJ P.`
   It has 296 units and no unmapped sign. It is identical to the claimed completed reading. Every ciphertext sign is covered by the key.
4. **Transcription against the scan.**
   - I read all nine rows on the enlarged `work/text.png` and on my own crop `review/work/r08_r09.png` (3x from `work/upright.png`). The glyph strings agree with `work/ciphertext.txt` row by row.
   - I checked these spots specifically:
     - R01 `th6r5` DRAHE at the stem
     - R03 `c86fm3cd4` SLAVNOSTI
     - R04 `m6fcd5f1` NAVSTEVY
     - R07 `pk6dh6` BRATRA
     - R08 `fh581r` and `t832r1r`, where the final r has no bar or caron (correctly kept as H)
     - R09 `f1ř`, where a distinct bar sits over the r (correctly CH)
     - the underlined `b.` before the date 6.VII.1903
5. **U1 restoration (R02).**
   - My own crops are `review/work/r02_stem.png` (6x), `review/work/r02_stem_c.png` (contrast) and `review/work/r02_stem_red.png` (8x, red channel, which suppresses the green stem).
   - After `m` there is a small dark sign with a short hooked top, then a clearly visible `2`, then `cd685`.
   - The gap holds exactly one sign. The small sign fits a small `5` (compare `m5` in R03/R04) and does not fit any other key sign well.
   - So the U is read from the pixels and the E is partly visible and consistent. The result, *neustále*, is the natural Czech word.
   - The restoration is disclosed in the completion section as "restoration of one hidden sign". I accept it.
6. **Language and context.** The Czech is idiomatic for 1903, with the usual cipher-postcard simplifications (no accents, VSOBOTU written together). The contents fit the family: thanks for postcards, *srdéčko*, kisses, signature P. On the date: Staroměstské náměstí on 6 July (the Hus commemoration) is plausible context, and the solver correctly does not use it as evidence. Jihlava is near the recipient's region (Žirovnice u Počátek).
7. **Prior publication.**
   - I fetched the Cipher-Atelier `anna-ticha` directory listing and `card-229.md` (HTTP 404), and read its `readings.md`. Card 229 / HCP 1548 does not appear, and none of the strings "neustále", "Staroměstském", "komisaře z Jihlavy" or "promoci" occur.
   - The portal status recorded in SOURCES.md is Not solved. The family key is credited (Egorov study, earlier cards).
   - 1548 is not in `register-exclusions.json`.

## Findings

1. **major – the reproduction command and records do not give the claimed plaintext.**
   - `work/decode.py`, `work/literal.txt`, `work/ciphertext.txt`, `work/positions.csv` and `work/transcription.json` still encode U1 as an unknown-length span. The command prints `N⟦U1⟧STALE` and "Total cipher length UNKNOWN".
   - The README requires a single command that produces the full plaintext.
   - **Fix:**
     - Put `5 2` into the R02 transcription/ciphertext, flagged as a restoration (e.g. a token kind `restored`).
     - Update the counts to 296 units.
     - Regenerate the literal and the hashes, so the command prints NEUSTALE.
2. **major – SOLUTION.md contradicts itself.**
   - The heading and early sections still say "substantial partial reading", "not a complete exact plaintext", "No state marker … is produced", "No grammatical completion is supplied". The literal block and the editorial Czech and Slovak blocks still show ⟦U1⟧.
   - The appended section says "complete reading". NOTES.md has the same split.
   - **Fix:** Rewrite the top of SOLUTION.md as one current statement, with the old partial state kept as history only. Give one literal plaintext, one Czech version and one Slovak version.
3. **minor – the sender name is expanded without support on this card.**
   - The completion's editorial Czech ends "tvůj P[epouš]". The earlier text says "the sender's identity is not established".
   - The P signature fits the Pepouš family cards (e.g. hcp-1556 signs "pepous" in full), but this card only has P.
   - **Fix:** Keep `P[epouš?]` with a note that the expansion comes from the family. Do not present it as read. The completion's Slovak version already leaves it as plain "P".
4. **minor – VRELYH/DLOUHYH.**
   - These are correctly kept literally. My crop confirms there is no CH bar on the two R08 terminal r's, against a clear bar in R09 `f1ř`.
   - The report should state this plainly as a writer's omission, read editorially as *vřelých, dlouhých*. This is already essentially done.
5. **minor – the restored E is only partly visible.**
   - The completion says the E is the only sign that fits. My red-channel crop shows a small dark sign consistent with `5`, so the E is partly attested, not purely inferred.
   - The report may say so, while still listing it as a restoration.

## What I could not verify

- The original postcard at higher resolution than the 1024x674 portal image. The stem-covered sign in R02 is read at the limit of this resolution.
- Whether anything was ever published about this card outside the AI register, the HC portal and the Cipher-Atelier repository.
- The identities of the sender, the brother and the commissioner, and the exact event on Staroměstské náměstí.
