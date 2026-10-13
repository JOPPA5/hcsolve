REVISE

# Review 1 — HCP 1301 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-12. Short version: **the decipherment is correct** — I re-read the whole card sign by sign from `source/address.jpg` and get the same Hungarian text. The verdict is REVISE, not ACCEPT, because the "source-bound" transcription is not a transcription (finding 1) and in at least two rows it does not match what is written on the card (findings 2–3). None of the findings changes the meaning of the message.

## What I verified and how

1. **The documented command.** `python3 batches/postcards-five-2026-10-12/verification/decode.py 1301` runs, the SHA-256 of `source/address.jpg` matches, and the output is byte-identical to `work/diplomatic-reading.txt` (`diff` empty), 24 rows.
2. **Where the tokens come from.** Read `verification/build_editions.py`: the rows of `verified-edition.json` are produced by mapping each *plaintext letter* of a hard-coded Hungarian string to its class name. `decode.py` maps them back. See finding 1.
3. **Independent reading of the scan.** I ignored `verified-edition.json`, cut the address side into 4× upscaled strips (`review/work/crops.sh`, `review/work/strip-*.png`) plus 8–10× details (`review/work/zoom.sh`, `z-*.png`), and read every row applying only the shape table from `SOLUTION.md`. Result per row:

   | Row | My reading | vs. solver |
   |---|---|---|
   | 1 | kedvesjolánkámhogy | same |
   | 2 | teltelavasár?apja (one overwritten sign) | same, overwrite disclosed |
   | 3 | remélemjolamiengem | same |
   | 4 | iletelégjolteltmert | same |
   | 5 | nemvolegyperczsza | same |
   | 6 | b?didőmdélután3tól (2nd sign: two or three bars, unclear) | same up to a/e |
   | 7 | [blot/5]tigválasztmányiülés | same |
   | 8 | 5tól7igtűzoltógya | same |
   | 9 | **kolatéseste**½9től12ig | **differs** — finding 2 |
   | 10 | amozgószínházbanvol | same |
   | 11 | tamőrségenabólislát | same |
   | 12 | hatjajolánkámédesem | same |
   | 13 | nemmehetemlemajd | same |
   | 14 | jövővasárnapokvetlen | same |
   | 15 | lemegyekdehacsakteheti | same (h/p see finding 4) |
   | 16 | jojonfelédesemcsü | same |
   | 17 | **tö?ökön**epedőszivel (7 signs, not 8) | **differs** — finding 3 |
   | 18 | várvamaradokőszinte | same |
   | 19 | imádoj.tisztelemkedves | same (middle of `tisztelem` cramped) |
   | 20 | mamáját | same |
   | stamp | csokol / jaatá / volbó(l) / imádoja | same |

4. **Key consistency.** The distinctive signs behave as a real monoalphabetic key across all 24 rows and across the companion card HCP 1243: `6`=b, `⊥`=j, `§`=k, `F`=r, `Γ`=t, `Λ`=v, bold cross=f (`fel`, row 16; `kifejezni` on 1243), `( )`=cs (`csak`, `csü-`, `csokol`), `( X`=cz in `percz`. I found no sign that needs two different plaintext values, with the exception in finding 4.
5. **Language and context.** Natural 1912 Hungarian with period spelling (`percz`), formal address (`teheti`, `jöjjön`, `mamáját`) consistent throughout. `választmányi ülés`, `tűzoltógyakorlat`, `mozgószínház` are long, specific words that cannot be forced onto noise. The portal date 1912-06-04 was a **Tuesday**; the preceding Sunday was 2 June, so "Hogy telt el a vasárnapja?" and "csütörtökön" (Thursday 6 June) fit. The postmark shows `…JUN…`. Addressee on the card is `Tóth Jolánka`, matching `Jolánkám`.
6. **Prior solutions.** I did not find any sign in the files that a published solution was used; I did not repeat the web search (see "could not verify").

## Findings

1. **major — the reproduction command does not decode the cipher; it round-trips the answer.** `build_editions.py` generates `verified-edition.json` from the claimed plaintext (`classes[ch]` for every plaintext letter). The command in `SOLUTION.md` therefore cannot fail and proves nothing about the card. The solver says this openly in `SOLUTION.md` and `NOTES.md`, which is to its credit, but the README asks for a command that produces the plaintext *from the source and the key*. For a graphic cipher with no machine-readable source that means a transcription recorded sign by sign as seen (shape classes, including ambiguous/overwritten ones), made without going through the plaintext. Findings 2 and 3 show the practical consequence. Also misleading: the file name `verified-edition.json`, and row windows for rows 21–24 that all point to the same rectangle.

2. **major (transcription) / minor (meaning) — row 9 is not what the card says.** Detail `review/work/z-row09.png`. The card has eleven signs before `½`: `§ ɣ ~ = Γ` + `≡́ ) ≡ ) Γ ≡`, i.e. **`kolat és este`** — no `F` (r) sign in `korlat`, and an extra accented `és` before `este`. The solver's row has ten letters `korlateste`. So the writer wrote `…tűzoltógyako(r)lat és este ½9-től…` ("… fire drill **and** in the evening from half past eight …"). The `r` is an editorial restoration and must be listed as such; the `és` is missing from both the diplomatic and the normalized text and from the translation.

3. **major (transcription) / minor (meaning) — row 17 has one sign fewer than claimed.** Detail `review/work/z-row17.png`. The word after `csü-` is `Γ ö ʃ ö § ɣ //`: seven signs. The solver's `törtökön` needs eight. The third sign is a hooked `Γ`-like form that is neither a clean `F` nor a clean `Γ` — either an r+t ligature or one of the two letters was left out. `csütörtökön` is certainly the intended word, but the diplomatic row must show what is there (e.g. `tö{rt}ökön`).

4. **minor — `h` and `p` are not reliably two different shapes.** The key table gives h = "two separate tall strokes" and p = "tall stroke with short companion". On the card, the h in `dehacsak` and `teheti` (row 15) and in `ház` (row 10) is drawn as tall stroke + short tick, the same as p in `nap` (row 14), `percz` (row 5), `epedő` (row 17); only some h's (`hatja`, `mehetem`) have the tick first. On HCP 1243 row 9, `lapot` and `lehet` stand side by side with the same form. At 1024 px I cannot separate them; they are resolved by context. This does not threaten the reading (every case is unambiguous in Hungarian), but the key should say that h/p are near-homographs instead of presenting them as distinct classes. The same applies, more mildly, to d / n (long vs short pair of strokes).

5. **minor — row 6, second sign.** `sza-bad`: the sign after `6` looks closer to three bars (`e`) than two (`a`) in my crops. `szabad` is obviously meant; list it with the other accent/bar-count uncertainties.

6. **minor — protocol.** (a) `SOLUTION.md` and `NOTES.md` were modified after `DONE1` (mtime 23:08 vs marker 23:07; the translation was switched from Slovak to English). `NOTES.md` records that a human asked for it, so I reviewed the current text, but the README says nothing changes after a marker. `batches/…/README.md` still says "Slovak translation". (b) No watcher was started (`NOTES.md` says so; there is no `.watch.log`). (c) There is no `review/`-independent record of how the shape classes were first established — `NOTES.md` jumps from "scouts failed" to "the shared alphabet now reads all twenty lines". One or two sentences on how the break-in happened (which word, which card) belong in the notes and the report.

## Required for closing

- Replace the plaintext-derived token ledger with an as-seen transcription (or state plainly in `SOLUTION.md` that no source-to-plaintext command exists and remove the word "verified"), and fix rows 9 and 17 in it.
- Add `és` to the normalized text and translation; list `gyako(r)lat` and `csütö(r)tökön` among the editorial repairs.
- Note the h/p (and d/n) near-homography in the key section.

These are corrections of the record, not of the solution. If they are made, I see no need for another review round.

## What I could not verify

- Accents. At this resolution acute / double acute / diaeresis are often indistinguishable from stray dots and from descenders of the row above; I checked letters, not accents.
- The overwritten sign in `vasárnapja` (row 2) and the blot at the start of row 7 — I can only say the solver's reading is compatible.
- The last sign of stamp row 3 (`volból`) is cramped against the frame.
- Whether a decipherment has been published elsewhere. I relied on the solver's bounded search in `SOURCES.md` and did not repeat it.
- The identity of the sender. The companion card HCP 1243 carries a plain-text signature under its stamp (see that review); the solver has not used it.
