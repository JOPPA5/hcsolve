ACCEPT

# Review 1 of hcp-1164 (reviewer: Claude Opus 5.5, 2026-11-02)

The reading stands. I tried to refute it on the pixels, the key and the language and found nothing that changes a word of the plaintext. Only minor points remain.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1164/work/decode.py` ran clean: hashes of the 4 scans OK, 556 cipher signs, 31 distinct, no unused key sign. Its output agrees with the plaintext in SOLUTION.md word for word (only line breaks and editorial punctuation differ, as the solver says).
2. **Independent decoder.** `review/work/mydecode.py` builds the table per digit and mark from scratch and ignores the solver's "reading" column. It gives the same text, also 556 signs and 31 distinct. Every sign in the transcription has a table value. The commonest signs are `1:` e (57) and `1.` a (53), as expected for Hungarian.
3. **Transcription against the scans.** I made my own crops from `work/hires/` (`review/work/crops/`, made by `rc.py`, `ps.py`) and read the whole card, not a sample, against `work/transcription.txt`: top block (r1 to r4), verses 1 to 3 (v1, v2, v3), closing (cl, ked), margin and dashed box (m1a, m1b, box), corner box (corner), picture side with red channel and contrast (ps0 to ps3). I found no sign that differs from the transcription, apart from the blotted signs below, which the solver lists.
4. **Each disclosed point on the pixels.**
   - `bajod` (m1a): first sign is a tapered blot with a clear comma. It is not legible alone, but no other sign gives a word and `valami bajod` is idiomatic. Reading by sense, disclosed.
   - `mert` (m1a): last sign is a blot on the frame line, with a comma. Same status.
   - `kedvesed` (ked): third sign is a closed heavy 3 and could pass for 8 alone. The word decides it. Disclosed.
   - `babus` (ps3): I too see one dot, with the comma of the preceding `1,` where the lower dot would lie. Disclosed.
   - `nincs e` (m1b): both dots of `1:` are visible against the green print. The long comma of `2,` is there, reaching toward the row below.
   - `rózsák` (st7): the 7 has no comma. The mark below is a drawn star sitting on the arrow line, separated from the 7. Confirmed, and the verse reads with it.
   - `it` (r2): one `8,`. Confirmed.
   - Margin order: inner row, then outer row, then box. Only this order gives a sentence. Dashes of a shared frame are visible (m1a, box).
   - Corner box: `1 3, 6 1' 5,` is visible; the 6 has no comma, so j, not n. Confirmed.
   - Ornament under verse 1 (orn2): a laurel-like branch, not crossed-out writing. Confirmed.
   - Date: four strokes between an over-line and an under-line (date2), so IIII. Confirmed.
5. **Language.** The text is natural Hungarian of the period and has no forced words. All three verses count 8/7/8/7 syllables by my own count. Rhymes hold (jelenthet/szentet, Margitka/hajnalra; igazán/rám is near). The clear letters mixed into verse 3 (`M betű`, `jelenthe`+`t`, `szente`+`t`, `így?`) could not have been forced by the key. I checked the English and Slovak translations against the Hungarian; they are faithful.
6. **Context.** Addressee, address and signature Árpád match hcp-1174. The postmark shows APR and a day 1; the year is not legible, as the solver says. 1 April 1916 was a Saturday, which suits a card saying he can hardly come up on Sunday (the solver does not use this). The picture of a couple fits `páros élet`.
7. **Key independence.** hcp-1165 and hcp-1169 (separate solving, reviewed) file `4.` gy, `6` j, `6.` ny, and hcp-1169 also `5.` ly, from other words. That supports the new values here.
8. **Disclosure.** SOURCES.md and SOLUTION.md agree: no portal solution, HistoCrypt article not checked, key origin credited. The solver's transcription is declared as its own.

## Findings

1. **minor: `5.` is filed differently on the sister cards, and the note understates it.** SOLUTION.md gives `5.` = ly and says only that it "may bear on" `hcp-1178`/`1179`. Those cards file `5.` as l (`a legszeb`, `csókollak`), with hcp-1178 stating that the mark on 5 distinguishes no letter. The ly value is sound here: the dot is visible in `milyen` (ps0), `olyankor` (ps0) and `oly` (m1a), and no l reading gives those words. The solution should state the conflict: the writer uses `5.` for ly here, while it stands for l on those two cards.
2. **minor: `9.` = zs rests on one occurrence.** `Each new sign recurs or fits the pattern` is accurate but general. `9.` occurs once (`rózsák`) and `8.` only twice, in the same word. They should be named as thinly attested. The reading is not in doubt, since the word and the digraph pattern both support it.
3. **minor: small details of the date line.** `work/transcription.txt` and the plaintext give `1916. IIII/1`. In date and date2 I see no separate slash after IIII: the diagonal to the right belongs to the frame and the flag of the 1, and the dot after 1916 may be the head of the under-line. This has no effect on the date; give the form as seen or say that the punctuation is editorial.

## Could not verify

- Whether the HistoCrypt article linked from the portal discusses this card. I did not check it, nor did the solver, who says so.
- Whether the verses are borrowed from a printed source. Nothing on the card says so; neither the solver nor I searched.
- The blotted signs in `bajod` and `mert`, and the lower dot in `babus`, cannot be read from the ink alone (the scans go no further). They rest on word sense, as disclosed.
- The postmark year.

No whole clause is unread, so the card counts as complete and is eligible for a register entry with type MASC. Findings 1 to 3 need a short response in SOLUTION.md and no new review round.
