REVISE

# Review 1 — HCP 1217 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-14. **The card is deciphered**: the key transfers from HCP 1301/1243 and my own sign-by-sign reading of `source/address.jpg` gives the same letter, the same topics and the same stamp message. The shape ledger is now a real transcription (not generated from plaintext), which is a clear improvement over round 1 of HCP 1301. It still disagrees with the card in four rows, and one of those changes the meaning of a sentence (finding 1). Hence REVISE.

## What I verified and how

1. **The documented command.** `python3 batches/jolanka-next-five-2026-10-12/visual-ledgers/decode.py 1217` exits 0, the SHA-256 of `source/address.jpg` matches the manifest, output is identical to `work/as-seen-decoded.txt` (19 + 8 rows).
2. **Provenance of the ledger.** `decode.py` only maps tokens of `work/as-seen.txt` to letters; no script in the batch directory writes that file from a plaintext string (`grep` for `as-seen`/`tokens` in `batches/jolanka-next-five-2026-10-12/*.py`: nothing). I accept the solver's statement that it was typed from the image.
3. **Independent reading.** 4× strips of the whole text column and details of rows 8–13, 17, the last row, the stamp and the postmarks (`review/work/`, made with `crops.sh` / `zoom.sh`). I read each row with the shape table only and then compared with the ledger:

   | Row | My reading | vs. ledger |
   |---|---|---|
   | 1–7 | kedvesjolankam / kivanomhogyjo / kedvebentalalja / soraimhogymu / latotvasarnap / endelelőtbemen / tempestrevoltam | same |
   | 8 | [large looped S]a[pink smudge]dornaldeatob | same letters; see finding 5 |
   | 9 | bivelnembe**s**zel | **differs** — finding 2 |
   | 10 | hettemmertuj**b**esten | **differs** — finding 3 |
   | 11 | volt[blot]akdelut?n | same |
   | 12 | utraelmentem | same |
   | 13 | es**a**kkorjotte**k** | **differs** — finding 1 |
   | 14 | atancziskolabol | same |
   | 15 | eselmentünkegy | same |
   | 16 | kibiliardozni | same |
   | 17 | **e**bö**l alt**avasar | **differs** — finding 4 |
   | 18 | napezebezarom | same |
   | 19 | soraimistenveleédesem | same |
   | S1–S8 | istenvele / édesemjo / mulatast / kivanok / esgondol / jonne{h|p}a / ram{h|p}űked / vesere | same |

4. **Context.** The Budapest postmark reads `912 OKT 2`, the Árokszállás arrival mark `…OCT 3`: the portal date 1912-10-02 is confirmed by the card. 2 October 1912 was a Wednesday, so "vasárnap" is 29 September. Sender in Pest / Újpest, addressee `Tóth Jolánka úrleánynak, Jászárokszállás` — consistent with HCP 1301 and 1243. `táncziskola` with `cz` is period spelling.
5. **Language.** Ordinary colloquial Hungarian of the period, same formulae as the other cards of the series (`Kívánom, hogy … találja soraim`, `Isten vele, édesem`). Not forced.

## Findings

1. **major — row 13 says "then they came", not "then I came".** Detail `review/work/z-row13.png`. The row is `≡ ) = S S ɣ F ⊥ ɣ Γ Γ ≡` + a final small S-shaped sign at the margin. (a) The third sign has two bars: `akkor`, not `ekkor`. (b) The final sign is a curved sign of the same family as the two `k`s earlier in the row; it is certainly not the three short strokes of `m` that the ledger records. The row therefore reads **`és akkor jöttek`**. This repairs the one sentence of the solver's translation that does not make sense ("In the afternoon I set out, and then I came from the dance school, and we went to play billiards"): the writer says that in the afternoon he went again/out, **and then they** — the friends he had missed in the morning because they were in Újpest — **came from the dance school, and we went** to play billiards. The first-person plural `elmentünk` in row 15 needs exactly this subject.

2. **major (transcription) — row 9 has the `s`.** `review/work/z-row08-10.png`: `6 ≡ ) X ≡ ~` = `beszel`. The ledger has `6 E Z E L` and `SOLUTION.md` builds an uncertainty note on it ("Row 9 has `bezel`, interpreted as `beszél`"). The card is simply correct here; the note should go.

3. **major (transcription) — row 10 has `6` (b), not the h/p sign.** Same detail image: `X ⊥ 6 ≡ ) Γ ≡ //` = `ujbesten`. The ledger has `H`, decoded `uj{h|p}esten`. `Újpesten` is of course meant (compare `Pestre` in row 7, written with the normal p sign), but what is on the card is a b — a slip of the writer. It must be recorded as seen and listed among the normalizations, not silently turned into the expected sign.

4. **minor (meaning nearly unchanged) — row 17 reads `ebből állt`, not `abból lett`.** `review/work/z-row17.png`: first sign three bars; after the first wave come two bars (with a mark above), a wave, then `Γ`: `≡ 6 ő ~ = ~ Γ` = `eböl alt`. "Ebből állt a vasárnap" ("that is what my Sunday consisted of") is also the more idiomatic sentence. The ledger's `A 6 O L L E T` has the bar counts the other way round.

5. **minor — row 8, `Sándornál`.** The first sign is a large looped S-form, unlike the plain right bowl used for `s` everywhere else on the card (possibly a deliberate capital), and the `n` lies under a pink smudge/erasure. The ledger records an ordinary `)` and `N` with no flag. The name itself is not in doubt.

6. **minor — remaining wording.** `utra elmentem` (row 12) is what is written; the translation "I set out" is acceptable, but with finding 1 the sentence should be re-read as a whole. `ki biliárdozni` (row 16) and `eze` (row 18) are correctly reported as seen.

7. **minor — protocol.** `report/report.pdf` already exists at `DONE1`; it must be rebuilt after these corrections anyway. No watcher was running for this directory.

## Required for closing

Correct the four ledger rows (9, 10, 13, 17), the Hungarian text and the English translation accordingly (`…és akkor jöttek a táncziskolából…`, `Ebből állt a vasárnap`), drop the `bezel` note, add `Ujbesten` → `Újpesten` to the normalizations. No further review round is needed from my side if this is done; the decipherment itself is accepted.

## What I could not verify

- Accents (1024 px scan).
- The exact last sign of row 13: I am sure it is not `m`; between `k` and a small `s` I prefer `k` on shape and on grammar.
- Whether a decipherment exists elsewhere — I relied on the solver's bounded search.
