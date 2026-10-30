REVISE

# Review 2 — HCP 1528 (pc_hcp_209), Anna Tichá / Pepouš family

Reviewer: Claude Opus 5.5, 2026-10-30. Round 2 (marker DONE2).

All nine findings of review 1 have been fixed, and rows R12–R14 and R16 now match the
scan. But a fresh sign-by-sign re-read of the whole card found one more transcription
error, in R07. The record has the word `bh4c83` (PRISLO). The card shows `p183` (BYLO).
This error came from the original GPT record (`work/v1/transcription.json`). It was carried
into round 2, and I missed it in review 1 too. My statement in review 1 that "R01–R11
match my reading" was wrong for this word. The fix is a single, unambiguous word, and the
rest of the reading stands, so the verdict is REVISE, not REJECT.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1528/work/decode.py` exits 0. All hashes
   pass, and it prints 18 rows: 564 signs, 572 letters, gaps Q1/H1/H2. Its output is
   identical to the claimed plaintext in SOLUTION.md and to `work/plaintext.txt`.
2. **Key.** `work/key.json` is identical to the family key in
   `ciphers/hcp-1545/work/key.json`. It is a 22-sign bijection, and the CH sign is the
   only digraph. Every transcribed sign is covered by the key, with no new assignments.
3. **Independent decoder.** `review/work/review2_decode.py` uses a key typed in by hand
   and my round-2 transcription, re-read from fresh crops in `review/work/r2/`. Its output
   is in `review/work/review2_decode_output.txt`: **562 signs, 570 letters**. It differs
   from the solver only in R07, word 3.
4. **Fresh crops** (3–6x, LANCZOS, all in `review/work/r2/`):
   - `a_r01_03`, `b_r04_06`: sample rows R01–R06
   - `c_r07_09`, `k_r07a`, `n_r07b`, `o_r08a`: R07–R09
   - `g_r06mid`, `l_r06tree`: the H1 blot
   - `h_r09end`: H2
   - `d_r10_12`, `e_r13_15`, `f_r16_18`: R10–R18
   - `i_r02end`: Q1
   - `j_r05I`, `m_r05I`: the R05 "I"
5. **Review-1 corrections confirmed on the pixels:**
   - R12 `n4 fc6g q5 cf4m 3b5d d6g3f1` (MI VSAK ZE SVIN OPET TAKOVY)
   - R13 `84cd5g, 76g3 b3c85tm5, gd5h1 nm5` (LISTEK, JAKO POSLEDNE, KTERY MNE)
   - R14 `q6hn32d48. cht5sm1 b3qth6f6` (ZARMOUTIL. SRDECNY POZDRAVA). The final sign of
     the first word is the 8/L loop.
   - R16 `df27` (TVUJ), with the z-like 2/U.
   - R10 PROSIM ends in `n`/M.
   - R15, R17 and R18 are as recorded.

## Findings

1. **major — R07, word 3: the card has BYLO, not PRISLO.** The record has
   `m6 řf484 bh4c83, b383q483 cf32 h2sg2`. Crops `k_r07a.png` and `n_r07b.png` (and the
   solver's own `work/claude/r2/r06_08.png`) clearly show **four** signs after `řf484`:
   `p183`. They are the long-stemmed p/B, then 1, 8 and 3. This is the same word as `p183`
   (BYLO) after the blot in R06 (`l_r06tree.png`). There is no room for a six-sign `bh4c83`.
   The `h`/R and `c`/S that PRISLO needs are not there. The row reads
   `m6 řf484 p183, b383q483 cf32 h2sg2` = NA CHVILI BYLO, POLOZILO SVOU RUCKU.

   What must change:
   - `transcription.json` (R07 units 30 → 28), `positions.csv`, `plaintext.txt`, the
     hashes and the decoder output. The totals become 562 signs and 570 letters.
   - The base plaintext, the accented Czech and both translations.
   - The claim that "our base text is identical to the reviewer's" must go.

   The literal sentence is now "aby mne [H1] bylo mé srdéčko aspoň na chvíli bylo, položilo
   svou ručku na hlavu". The writer repeats *bylo*. It is colloquial and imperfect, but it
   is coherent: "that my sweetheart had been with me, at least for a moment, had laid her
   hand on my head". Do not repair it to "přišlo". The translations should render "been
   (with me)", not "come". Whether the H1 blot hides a short word (for instance a preposition
   such as "u") stays an open question. Keep H1 as a gap.
2. **minor — R07 POLOZILO, sign 2.** The second sign of `b?839483` is blotted by ink or
   engraving (`n_r07b.png`). It looks like a smudged 3/O, and the reading POLOZILO is safe in
   context. But it is a sign read from context, so add it to the uncertainty table as
   probable.
3. **minor — Provenance of the round-2 transcription.** The round-2 record is
   character-for-character the reviewer's round-1 transcription (apart from the gap
   notation and the `?` on the R05 "I"). SOLUTION.md discloses that it agrees with the
   reviewer. It does not say that rows the solver did not re-read (R01–R11 apart from
   R02 end, R09 and R10–R11) were taken over from the earlier records without fresh
   verification. That is how the R07 error survived two rounds. State which rows were
   re-checked on the pixels in round 2 and which were inherited, and re-check R07 after
   the fix.

## Confirmed as correct

- The key is the family key. No published plaintext of pc_hcp_209 is used, and the prior
  generic key of M. Egorov / Cipher-Atelier is credited.
- R01–R06 and R08–R18 agree with my fresh reading sign by sign. The disclosed
  uncertainties (Q1 KRK?, H1 blot, H2 BAV…, HEZKY, the R05 "I") are labelled correctly and
  are not forced. JO and SLECNA JANKOVA are kept literal, as they should be.
- The context fits. Trhové Sviny and slečna Janková appear on the address side, the card
  is dated 5./XII.1903 and is signed Pepouš. The language is real colloquial Czech of the
  period.
- The GPT and Claude contributions are credited accurately in "Credits and history".

## Could not verify

- I did not re-open the live portal or Egorov's page. I relied on SOURCES.md and the
  orchestrator's register check.
- Ink under the foliage (H1, the end of R09) cannot be read on this 1024 px scan.
- Diacritics are not transcribed. The accents are editorial.
