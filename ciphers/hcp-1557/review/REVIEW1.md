REVISE

# Review 1 — hcp-1557 (pc_hcp_238), reviewer Claude Opus 5.5, 2026-10-29

## Summary

The reading stands: the card is a Pepouš → Anna Tichá Easter card (8 Apr 1903) in the
shared family key, and the Czech is coherent and fits the date ("Veselé velikonoce",
svátky, neděle a pondělí). The decryption is reproducible. However, the "literal"
transcription is **not literal** in at least four places: the visible sign was
silently normalised to the sign the expected plaintext needs. All four look like
writer slips (most are the writer dropping into ordinary plaintext letters), so the
editorial text does not change, but the transcript, the literal output and the
claims in SOLUTION.md ("no assignments inferred from grammar", "VE SNE ... is the
decoded text") must be corrected and the slips disclosed.

## What I verified and how

1. Ran the SOLUTION command
   (`.../python3 ciphers/hcp-1557/work/decode.py`): exit 0, output equals
   `work/literal-cz.txt`, counts R1 71 / R2 76 / R3 75 / R4 73 = 295 units, 6 CH, one {U1}.
2. Independent decoder `review/work/mydecode.py` (own key dict, CH matched as one unit,
   {U1} passed through): `python3 -I review/work/mydecode.py work/manual-transcript.txt`
   → identical to `literal-cz.txt` (diff empty), 295 units, no unmapped symbol.
   Output saved in `review/work/my.txt`.
3. Key: identical to `ciphers/hcp-1520/work/key.json` and the other finished family
   cards (1545 uses the label `7` for J where this card uses `y` – label only; on the
   scan the J sign is the 7-like form). Every transcript symbol is covered.
4. Scan: own 3–8x LANCZOS crops of `source/picture.jpg` in `review/work/`
   (band0–2, u1*, ztravilo, za_dik, drahy8, mohl8, kontr, vesne, tisic, cmp_s_t,
   nejpr8, r2start, r2mid, r3left, r4*, …). Checked all four rows word by word
   at 3–4x; disputed signs at 6–8x. Address side not separately re-examined beyond
   the solver's description.
5. Context: date 8./IV.1903 (picture side) = Easter week 1903 (Easter Sunday 12 Apr 1903);
   "jel bych na neděli a pondělí" = Easter Sunday/Monday. Fits.

## Findings

1. **major – MOHL is visibly MORL.** R3 word `n3r8`. At 8x (`mohl8.png`) the third
   sign is the tall looped h-shaped sign, the same class as the R in DRAHY
   (`drahy8.png`: t-**h**-6-**r**-1, where tall h = R and small r = H) and in OCHURAVEL,
   POZDRAVU. The small r-shaped H sign is not there. Correct transcript: `n3h8` →
   literal MORL, editorial *mohl* (writer wrote the plaintext letter h). Not disclosed.

2. **major – VE SNE is visibly VE CNE.** R4 `f5 cm5`. `cmp_s_t.png` places the sign
   beside the final sign of TISIC (`d4c4s`, label s = C): same small looped s-shape; it
   is not the open c-shape (= S) of POSILA/PEPOUS. Correct transcript `f5 sm5` → literal
   VE CNE, editorial *ve sně* (writer wrote plaintext s). SOLUTION.md explicitly asserts
   "The literal VE SNE ... is the decoded text" – this is wrong and must be corrected.

3. **major – KONTROLORU: fourth sign is the crossed t (= D), not d (= T).** R3
   `g3mdh383h2`. In `kontr.png` / `cmp_s_t.png` the sign after m is the crossed
   t-shape matching DIK's t (=D), not the rounded ∂-shape (=T) of TISIC/STALE. Literal
   KONDROLORU, editorial *kontrolorů* (again a plaintext t). The illustration overlaps
   here, so state the confidence, but the visible shape favours t; the solver's
   overlap notes discuss g/q only.

4. **minor – NEJPRIJEMNEJI: second sign is 3 (= O), not 5 (= E).** R2 `m5ybh4y5nm5y4`.
   At 8x (`nejpr8.png`) the sign after m has the curved 3-top identical to `s3` (CO),
   unlike the flat-topped 5 later in the same word. Literal NOJPRIJEMNEJI (probable slip
   or ambiguous 3/5); disclose. The word also ends with `!`, not `.`
   (punctuation only).

5. **minor – ZTRAVILO initial.** The first sign (`ztravilo.png`) ends in an open
   descender hooking left, closer to the g (= K) of DIK than to the closed loop of the
   q (= Z) in ZA (`za_dik.png`). Neither K nor Z gives standard *strávilo*; keeping
   ZTRAVILO as literal is acceptable, but note the q/g ambiguity. The d/T second sign
   is confirmed.

6. **minor – U1 restoration is acceptable and disclosed.** `u1.png`, `u1_R.png`: a dark
   printed leaf covers one sign-width before `6`; faint humps are visible but no
   sign can be read. [N]a is the only natural Czech fit and is correctly marked as a
   restoration; literal keeps {U1}. Accepted.

7. **minor – stale/contradictory statements in SOLUTION.md.** Title and early sections
   still say "partial", "no DONE marker", "337 contributions"; the completion section
   says complete, 357 records. The report should give one current status. The claims
   "No new assignments were inferred from Czech grammar" and the hash/round-trip
   checks do not cover findings 1–4; reword.

8. **minor – sample checks that passed.** VRELY DIK ZA DRAHY LISTEK, SVATKY CO,
   PREJI SVEMU SRDECKU, NASICH (two-hump m confirmed), OCHURAVEL, KDYBYCH, ODJETI,
   JEL BYCH NA NEDELI A PONDELI, BUDU TEZ STALE, TISIC POZDRAVU A DLOUHYCH VRELYCH
   PUS POSILA, TVUJ PEPOUS, the six CH signs (tilde-capped r) all match the scan.
   PSANKO, POKUD, NESMIRNE behind the illustration are plausible but low-contrast.

## Required fixes

- Transcript/literal: MORL (`n3h8`), VE CNE (`f5 sm5`), KONDROLORU (`g3mth383h2`),
  NOJPRIJEMNEJI (`m3ybh4y5nm5y4`), or explicitly mark each as uncertain; update counts
  if anything changes (unit count unchanged at 295).
- Add the slips to the uncertainty list (writer's plaintext-letter slips at h, t, s),
  correct the VE SNE statement, unify the status text.

## Not verified

- Glyph-by-glyph confirmation inside the darkest overlap patches (NESMIRNE, PSANKO,
  POKUD) beyond plausibility; resolution of the 1024 px scan limits this.
- The 25 internal hashes were run but not independently recomputed.
- Identity of "Pepouš" beyond the family attribution.
