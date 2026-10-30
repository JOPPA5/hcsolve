ACCEPT

# Review 1 — HCP1545 / pc_hcp_226 (Anna Tichá family, 8 Aug 1903)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Solver work: OpenAI GPT solver (2026-10-28, main transcription and partial
reading) and Claude Opus 5.5 as solver (2026-10-29, "Completion and handover" section on U01).

## What I verified and how

1. **Solver command.** Ran
   `/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1545/work/decode.py`
   from the repo root: exit 0. All hash, crop, index and inverse-key checks passed. It reported 362 mapped units, 7 CH units and 1 unresolved region. Its 15 output lines are identical to the plaintext in SOLUTION.md and to work/plaintext.txt.
2. **Independent decoder.** I wrote `review/work/indep_decode.py`, which uses its own key table typed from the family key
   (`12345678bcdfghmnpqrst` → `YUOIEAJLPSTVKRNMBZHCD`, `ř`→CH). It checks that this table equals `ciphers/hcp-1527/work/key.json` (True) and decodes the `cipher` field of every row in work/transcription.json. Result:
   all 15 rows match the solver's per-row plaintext. That gives 362 units and 0 unmapped signs, and the output equals plaintext.txt. The key therefore covers
   the whole transcribed ciphertext. The one exception is the U01 mark, which has no key letter (finding 1).
3. **Transcription against the scan.** I rotated source/picture.jpg myself (ROTATE_270 for the body, ROTATE_180 for the margin) and made
   3–8x crops in review/work/: `r01_04.png`, `r05_08.png`, `r09_12.png`, `margin.png`, `r07_start.png` and `r08_end.png`.
   I read R01–R12 and M01–M03 sign by sign at 3x, and I looked closely at the disputed places:
   - R07 first sign: it has a long returning descender loop, which is the g/K class. It is not the compact q/Z head, and it is not the r/H form
     seen in `th6r1`. The literal reading KOLUBENKU is therefore what is written, not a forced reading. HOLOUBENKU would be an emendation, and the solver correctly does not insert it.
   - R09 `6m2mg3`: the third sign is clearly 2/U, so ANUNKO is correct. It agrees with ANUNKA on HCP1535 and HCP1533.
   - M02 `b5b32c`: PEPOUS is correct.
   - R04 `gh4q3f68` KRIZOVAL, R11 `f38m1ř řf484ř b48m5 m6 t574m6ř` and R12 `s5s4845, 6p1ř 75 n3r8 75cd5 t3`: all agree with the scan.
   - M01 and M02 agree in full, including the split `2bh4n- / m1ř`.
   - The hand separates q/Z from g/K only weakly (a "9" against a "g" with a long loop). The solver's assignments are consistent with the word context in every case, and I found no sign
     whose reading flips a word.
4. **Context.** The address side reads "Velectěná Slečna / slečna Anna Tichá / učitelka t. č. / v Pelhřimově", with "Vlastnoručně dodati!", a PRAHA
   dispatch postmark and a Pilgram/Pelhřimov stamp. The picture side carries the date 8./VIII.1903. All of this fits the content: the sender is in Prague, works on the "dějiny
   Cecilie" during the holidays ("do konce prázdnin"), and signs as Pepouš like the rest of the family. The Czech is idiomatic period Czech throughout.
   "křižoval" (crossed letters) and "tisíc upřímných pus" are formulas that recur on the other family cards.
5. **Sources and honesty.** The key is openly credited as a transfer from earlier family cards and from the published partial study by Maxim Egorov. The portal
   status was Not solved and no solution was attached. I found no use of a published solution for this card that is not disclosed.

## Findings

1. **U01 is treated as a non-letter on interpretation, not on proof (minor).** In `r08_end.png` the sign after `bh475t5` is
   one small oval with a dot inside. It matches none of the 22 key signs, so it does not fit the key, as the solver says. PŘIJEDE in the 3rd person is grammatical, and the
   writer does refer to Anna in the 3rd person on sister cards (HCP1535 "Anunka … přijede do Prahy", HCP1525 "Jak strávila dušička
   moje Silvestra?"). However, the solver's on-card evidence ("dostala" without *jsi*) is weak, and this same card also uses the 2nd person ("s tvým").
   An ad-hoc 2nd-person ending (PŘIJEDEŠ) therefore cannot be excluded, although Š is written as `c` elsewhere (PEPOUŠ = `b5b32c`), which argues against it.
   The meaning is the same either way. The report should keep the mark visible and say "unidentified mark; probably not a letter".
2. **SOLUTION.md contradicts itself about status (minor).** The first section is titled "takmer úplné čítanie" and states that it "NIE JE
   bezvýhradné úplné rozlúštenie". It also says "Nevznikol stavový marker, PDF ani zápis do registra", and the "Root source QA" section says "The result remains
   partial". The "Completion and handover" section, by contrast, claims a "complete reading". The decoder still prints "R08 U01 is unresolved" and "1–2-unit
   extent", while the completion section says the mark is a single oval. The report and register entry should use one harmonized
   statement: complete reading of all letters, with one unidentified non-key mark disclosed.
3. **The visible háček on E in KOLUBENKU is dropped (minor).** `r07_start.png` shows a clear háček over the `5` in `p5`
   (BĚ). The editorial Czech should read *koluběnku* [sic] (cf. *holoubě/holoubku*), or should at least note the háček. The solver's policy says diacritics are
   editorial, so this is a matter of completeness, not an error in decryption.
4. **"Cecilie" is left uninterpreted (minor, optional).** That is acceptable and is disclosed. A plausible period context is the
   Cecilian (church-music) movement, e.g. a society named after St Cecilia. The report could mention this as a possibility only.

## What I could not verify

- I could not identify the meaning of the dotted-oval mark (U01) definitively. I did not find the same sign on the sister scans in the time
  available.
- I did not check the quotation's closing mark or the exact punctuation pixel by pixel. They do not affect the letters.
- I did not independently re-run the register check. I rely on the orchestrator's note dated 2026-10-29.
