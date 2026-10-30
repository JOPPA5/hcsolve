REVISE

# Review 1 — HCP 1530 (pc_hcp_211), reviewer Claude Opus 5.5, 2026-10-29

The reading is correct: a Czech love letter from Pepouš to Anna Tichá, enciphered with the known
Anna Tichá / Pepouš family substitution key. All four dark spans can be read from the pixels, mostly
or fully, and the solver's completion (LISTEK / NYNEJSI / JEDINEMU / URADE) is right. But the
deliverable is internally inconsistent. The single command required by the README still prints
`[U1]…[U4]` and the wrong letter DRAHE. The header still says PARTIAL. The completion lives only in
an appended prose section. These are concrete fixes, so the verdict is REVISE, not ACCEPT.

## What I verified and how

1. **Solver command.** `python3 ciphers/hcp-1530/work/decode.py` runs cleanly. All hashes pass and
   it prints 445 units / 451 letters. The output equals the "Literal Czech base plaintext" block,
   placeholders included. It does **not** produce the plaintext claimed in the
   "Completion and handover" section.
2. **Own crops** (review/work/crops.py, run with -I on source/picture.jpg). I rotated the image
   90° CCW, cropped the top margin box and turned it 180°, then made 5–8x enlargements:
   topx2.png, T01x3.png, U1x5.png, U1x7.png, VRELYx7.png, U2x5.png, U3x5.png, U4x5.png,
   U4x8.png, U4x8c.png (autocontrast), bottom.png, B02x2.png, B02qg.png, B07rx3.png and
   B07zdrzel.png.
3. **Independent decoder** (review/work/mydecode.py). I typed my own transcription of all 14 rows
   from those crops, applying the family key (7-shaped sign = J, labelled `y` by the solver).
   Output:
   ```
   VRELY DIK SRDECKO MOJE ZLATE, ZA DRAHY L[IS]TEK
   JAK DARI SE NYNI S HLAVICKOU? JA JSEM, BOHUDIK,
   BOLEST SVE HLAVY JIZ PREMOHL, KTERE MNE NYNI
   PRISLO VELICE NEVHOD. U NAS JIZ BLIZI SE DOBA
   VANOCNI A S NI ROZMNOZENI PRACE. TAKE JA
   VZPOMINAM NA LONSKY ROK VTETO DOBE,
   KDY MOJE SRDECKO ZDE DLELO NA ZKOUSKACH.
   SKODA. A TY HEZOUNKE CHVILKY VZDY TAK
   RYCHLE PRCHAJI. JAK TRAVI ANUSKA NYNEJSI
   DLOUHE VECERY? MUJ ZIVOT JE NARAMNE JEDNO-
   TVARNY. VCERA CHTEL JSEM NAVSTIVITI VECER
   KONCERT „Issajův" V RUDOLFINE, ZDRZEL JSEM
   SE VSAK PRILIS DLOUHO V URADE. TISIC VRELYCH
   PUS POSILA PEPOUS SVEMU JEDINEMU SRDECKU.
   ```
   (My script has a typing slip in row B07, "KONCTERT"; the image reads g3ms5hd = KONCERT.)
   This matches the solver's positive reading everywhere except DRAHY, and it agrees with the
   completion section.
4. **Key coverage.** Every legible sign on the card maps through the 23-entry family key. No
   unassigned symbol remains. The single v/F rests on the documented card199 transfer and on
   RUDOLFINE, and it is disclosed as such.
5. **Language and context.** The text is natural Czech of c. 1900 (bohudík, navštíviti, srdéčko,
   hezounké, dlelo). It fits the family: Pepouš writing to Anna Tichá, a teacher in Žirovnice;
   the Rudolfinum concert hall in Prague; Christmas approaching on a card dated 14.XI.1903.
   Earlier GPT solver work and the published partial family key (Egorov / Cipher-Atelier) are
   credited in SOLUTION.md and SOURCES.md.

## Findings

1. **[major] The command does not produce the claimed plaintext; the record is stale.**
   work/transcription.json and decode.py still contain U1–U4 as unknowns, with "candidate only"
   notes (U1 even says PSANKO), and still record DRAHE. The README requires "a single command that
   produces the full plaintext". Fix: transcribe the span signs into transcription.json (U1
   `8 [4c] d 5 g`, U2 `m 1 m 5 7 c 4`, U3 `t 4 m 5`, U4 `t 5`), mark the restored signs in the
   output, update counts and hashes, and rerun.
2. **[major] DRAHE should be DRAHY.** In U1x7.png / U1x5.png the last sign of `th6r?` is a
   vertical stroke with a foot. It is identical to the `1` (Y) closing `fh581` (VRELY,
   VRELYx7.png) and clearly unlike the open `5` of the same row. So the sign is `1`, the word is
   DRAHÝ, and it agrees grammatically with masculine LÍSTEK. The solver flagged this in the
   completion section but left it wrong in the record, in the literal plaintext and in the
   command output.
3. **[major] SOLUTION.md contradicts itself.** The title line says "PARTIAL", and the body has
   "four dark source spans retained", "coverage … unknown", the earlier Slovak translation with
   placeholders, "No solved register entry is appropriate". The completion section then says
   "complete reading". The solver needs one consolidated status, plaintext, editorial text and
   translation. The Slovak translation must be updated to "za drahý lístek … nynější … v úřade …
   jedinému".
4. **[minor] Degree of restoration in U1 must be stated.** On the pixels: `8` (L) is probable,
   the next one or two signs are lost in the dark paint, and `d 5 g` (TEK) is visible before
   the closing bracket. So LISTEK = L + [IS restored from context, the width fits two signs] +
   TEK. The completion table lists visible `8`…`5 g` but does not say plainly that I and S are
   restored rather than seen. U2 (`m1m57c4`) is fully legible in U2x5.png and needs no hedging.
   In U3 the `7 5 t 4 m 5 n 2` signs are all discernible in U3x5.png, with t and 4 faint. In U4
   the `2 h 6 t 5` signs are visible in U4x8c.png; `t` and `5` are faint but have the right
   shapes. These three can be stated as read, with "faint" noted where it applies.
5. **[minor] q/Z and g/K are near-identical in this hand.** In B02qg.png, the first sign of `qt5`
   (ZDE) and both signs of `qg…` (ZKOUSKACH) look alike. The same holds in B07zdrzel.png
   (`qthq58`). The readings ZDE / ZDRZEL / ZKOUSKACH are certainly right, and the solver's own
   notes record an early KDE / KDYZEL misreading. However, telling Z from K at those positions
   relies partly on Czech, not only on shape. Disclose this.
6. **[minor] NEVHOD is not anomalous.** "přišlo … nevhod" is a standard Czech adverbial usage, so
   the remarks calling it "unusual" (Czech section and Slovak bracket) should go. KTERÉ, read as
   "which (thing)", is also acceptable as written.
7. **[minor] Issajův = Ysaÿe is context only.** This identification is fine as a labelled
   suggestion. I could not confirm a Ysaÿe concert at the Rudolfinum on 13 Nov 1903. Keep it
   flagged as unverified, or cite a source.

## What I could not verify

- Whether Ysaÿe (or another "Issaj") played at the Rudolfinum on 13.XI.1903.
- The exact number of signs hidden in the U1 dark patch. Two (IS) fits the width but cannot be
  counted.
- The card199 reference photo, which I did not re-inspect. I accepted the v/F transfer on the
  documented comparison and the unambiguous RUDOLFINE.
- The register: I relied on the orchestrator's 2026-10-29 check that the target is absent.

Recommendation: once findings 1–3 are fixed and 4–5 are disclosed, the reading can be finalised
as complete, with "LI[S]TEK"-type restoration noted for U1.
