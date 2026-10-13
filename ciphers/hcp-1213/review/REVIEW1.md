REVISE

# Review 1 — HCP 1213 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-14. **The card is deciphered in substance**: Easter greetings, Szolnok, Easter sprinkling at the neighbours' and in Szentmihály, moving into Pest by 1 May, the signature `Feri`. I read the whole card from `source/address.jpg` and agree with the solver on the great majority of the roughly 600 signs. The ledger is a real shape transcription. It is, however, incomplete in row 11 (four signs missing, which resolves the solver's own "unclear suffix"), and several of the oddities the solver reports as "source forms" are in my reading ledger errors, one of them probably hiding an ordinary Hungarian phrase behind a non-word (`kiklakás`). Hence REVISE.

This scan is the hardest of the series (27 rows of small green writing at 1024 px), so my confidence per sign is lower than on HCP 1301/1217; I mark below what I am sure of and what is a second opinion.

## What I verified and how

1. **The documented command.** `python3 batches/jolanka-next-five-2026-10-12/visual-ledgers/decode.py 1213` exits 0, source hash matches, output identical to `work/as-seen-decoded.txt` (27 + 7 rows).
2. **Provenance of the ledger.** As for HCP 1217: `work/as-seen-full-pass4.txt` is only read, never generated, by the batch scripts.
3. **Independent reading.** Nine 4× strips of the text column, plus details of rows 3, 7–8, 11, 21–22, the last rows, the stamp field and the postmark (`review/work/s-*.png`, `z-*.png`, made with `zoom.sh`). Rows where I agree with the ledger sign for sign (apart from accents): 1, 2, 6, 9, 10, 12, 13, 14, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27 and stamp rows S1, S2, S4, S5. Differences are the findings below.
4. **Key consistency.** Same alphabet as the other Jolánka cards. Distinctive signs check out: upright cross = f in `feljön`, `fogom`, `Feri`; `6 6` = bb in `legjobb`, `legalább`; `( )` = cs in `csókolja`.
5. **Context.** The address side is not Jászárokszállás this time: `Tekintetes Pernyés Mihály úr levelével, Szépreményű Tóth Jolánka úrleánynak, Jász-Berény, Sárkány u. 22 sz.` — the card went to Jolánka care of a Pernyés Mihály in Jászberény. The postmark is illegible beyond `91…`, so the portal's bare "1913" cannot be refined from the card; the text itself fixes it to shortly after Easter and before 1 May. `Szentmihály` (Rákosszentmihály) and Pest are consistent with the sender's location on HCP 1217.

## Findings

1. **major — row 11 is four signs longer than the ledger, and they are the "unclear suffix".** Strip `review/work/s-03-y210.png`, first complete row. After `…ő // Γ ő X S ő //` (`öntözköd`) the card continues `≡́ ) = X Γ`, running up to and across the red margin line: **`…öntözködés azt`**. The ledger stops at `E:acute UNKNOWN`. With the next row this gives *"Ez volt az összes húsvé(ti) öntözködés. Azt sajnálom, édesem, hogy magát nem öntözhettem meg"* — "That was all the Easter sprinkling. What I regret, my darling, is that I could not sprinkle you." The uncertainty paragraph about `öntözködé[…]` should be replaced by this reading, and `SOLUTION.md`'s claim that the ledger "includes every main row" is not true for this row.

2. **major (meaning) — `kiklakás` (rows 21–22) is not a Hungarian word and I do not think it is on the card.** Detail `review/work/z-row21-22.png`. Row 21 ends `= S i` + one small s-shaped sign written across the margin line. That last sign is visibly smaller and simpler than the two `k` signs (`S` with hook) elsewhere in the same row; it is at least as compatible with the right bowl (`s`). Then row 22 begins `~ = S = )` (`lakas`). **`a kis lakás`** — "the little lodging was very unpleasant, because I have to walk a great deal when I arrive at night" — is plain Hungarian and needs no gloss. The solver's translation "living out there [source kiklakás]" rests on an invented compound. If the solver keeps `k`, it should at least present `kis` as the alternative and stop translating a non-word.

3. **major (transcription) — row 3 ends `telt el`, not `teltek`.** Detail `review/work/z-row03-end.png`: `Γ ≡ ~ Γ ≡ ~`, the last sign being a wave across the margin line, not the k sign. "Hogy telt el a húsvéti ünnepek?" is the same formula as "Hogy telt el a vasárnapja?" on HCP 1301. `NOTES.md` presents `teltek` as a resolved reading of pass 4.

4. **major (transcription) — row 8 has an unrecorded sign.** Detail `review/work/z-row07-08.png`: `≡ )` + a large symmetric caret + `i g Λ ɣ ~ Γ = ///`. The ledger has `E:acute ) I GY V…` and skips the caret. It is larger and differently built from the hooked chevron used for `v` in the same row, so it may be an insertion mark, but as letters the row reads `és víg voltam` ("and I was merry") at least as well as `és így voltam`. Either way the sign must be in the ledger with a flag.

5. **minor — several "preserved source forms" look like ledger errors.**
   - Row 7 `masodok`: the vowel sign after `//` carries a dot, i.e. it is `i` — `második`, as expected.
   - Row 7 `szubad`: I see only one crossed sign between the right bowl and `6` (`) X 6 = //`), i.e. `szbad` with the `a` omitted, not `z` + `u`.
   - Row 4 `ünnepek` and row 5 `jobban`: I see one `//` and one `6` respectively, where the ledger has two. (Doubtful at this resolution; the meaning is not affected.)
   These matter because `SOLUTION.md` lists such forms as evidence of faithful transcription.

6. **minor — row 15, sentence division.** There is a blot and a dot after `végezni`. "…el fogom végezni. Nekünk, édesem, akkor is jó lesz" ("…I will do it. For us, my darling, it will be just as good then") parses more naturally than the solver's "I shall do it for us".

7. **minor — stamp rows S3, S6, S7.** S3 (`kolja`) is heavily inked and I can only say it is compatible. S6 ends in a blot after `vese`; S7 is an upright cross plus one small dotted sign — `F` and `i`, plausibly an abbreviated `Feri`, as the solver cautiously says. No objection to the `[F…i?]` treatment.

8. **minor — context not used.** The c/o address in Jászberény (`Pernyés Mihály`, `Sárkány u. 22`) is not mentioned in `SOLUTION.md`; the report should give it, since the solver states the recipient only from the catalogue.

9. **minor — protocol.** `report/report.pdf` exists already at `DONE1`. No watcher was running.

## Required for closing

- Complete row 11 in the ledger and replace the "uncertain suffix" passage by `öntözködés. Azt sajnálom…`.
- Re-examine the last sign of row 21 and either adopt `kis lakás` or give it as an explicit alternative; remove the gloss of `kiklakás` from the translation.
- Correct row 3 (`telt el`), record the caret in row 8, and recheck the row 7 forms.

The first two change the edited text, so I would like to see the corrected `SOLUTION.md` once more (`DONE2`); it should be a short round.

## What I could not verify

- Accents throughout.
- Rows 20 and 21 middle (`edig is nagyon`): cramped, I can neither confirm nor contradict the ledger sign for sign.
- The date: postmark illegible.
- Whether a decipherment exists elsewhere — I relied on the solver's bounded search; `SOURCES.md` for this card does not itself record a prior-solution search (the 1301/1243 files do).
