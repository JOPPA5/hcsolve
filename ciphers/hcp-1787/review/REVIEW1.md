REVISE

# Review 1 of hcp-1787 (pc_hcp_468)

Reviewer: Claude Opus 5.5, 2026-10-30. I tried to refute the reading. The key and the overall reading stand. Several readings need correcting from the pixels, and two of them remove disclosed exceptions or change the meaning.

## What I verified and how

- `python3 -I ciphers/hcp-1787/work/decode.py` ran with exit 0: hashes ok, misfits 0, 8 disclosed exceptions.
- Its last line is the `reading` column of `work/transcription.txt` copied out, not decoded output. The real decoded output is the literal block. It differs from the SOLUTION plaintext only in editing (`ktetice`/`k tetice`, `na říká`/`naříká`, `[?]talvrtá`/`[?čtvrtá]`, and added punctuation).
- I retranscribed all 133 words from my own crops of the hi-res originals and decoded them with my own script: `python3 -I ciphers/hcp-1787/review/work/decode_review.py`. Its test is stricter than the solver's: a reading may add only an unwritten a/á.
- With my corrections it reports 6 misfits, all genuine and all covered below or in SOLUTION.md: `hejtman` (no e), `jsme`, `to`, `vidět`, `děláme`, and `že` (x with no dash).
- Crops are in `review/work/`: every row at 2-2.5x, and contested signs at 3.5-10x. I checked every disclosed item and sampled ordinary rows. Ordinary rows agreed with the transcription sign by sign, apart from the points below.
- Key: one small key covers the whole text and the same sign values hold on both sides. Heavy stroke = a is real: in the transcription, 56 heavy marks sit against 67 a/á, and the bold `na`, `za`, `tak`, `dá` are plain to see. Exceptions are few.
- Language: natural Czech of the period, with colloquial forms (`bolejí`, `neděle` = weeks). Coherent subject. No published solution seen; the portal attaches none.
- Sequence check: "přišli na tři neděle" followed by "až bude čtvrtá neděle" makes sense together, which modestly supports item 3 of the solver's uncertainties.

## Findings

1. **major: "Vodrant" is "Vodranty", and exception 8 goes away.** Crops `y4.jpg`, `v1.jpg`. A thin diagonal stroke runs through the v (slash = o), the heavy stroke is on the 4, not on the 1, and a clear mid dot follows the last 1, before the closing quote. The transcription should be `v/14_21.`. Literal: vo-d-ra-n-ty, which is exactly the place name. Fix the transcription, plaintext, all translations, and delete the exception. The solver's stated reason (a heavy 1 that "should" be o) was a misreading. This also strengthens the card: the name now decodes mechanically.

2. **major: "na dráhy domov" is "na drahý domov".** Signs `14_8.` are d-ra-h-y, and the dot is ý as everywhere else. "Vzpomínám si na vás, milovaná Mařenko, a na drahý domov" = "and of my dear home". The solver's "roads home" (and "cesty domov") is a forced sense, and item 12's "could be a slip for a singular" falls with it. Fix all three language versions.

3. **major: "a až bude" adds a word that is not written.** Crop `r3b.jpg`. The card has `a` + x with caron: the same a + ž as `ax^` (až) in row A11, only spaced wider. The solver's transcription splits them and reads "a" and "až", which needs a second a that no sign supplies. The solver's check passes only because it is a subsequence test (finding 9). Read "až bude [?] neděle" unless a real reason for two words is shown. That also makes the clause less "unfinished" than item 3 says.

4. **major: "Vrozděř" has a final dot that the transcription lacks.** Crop `z2.jpg`. A mid dot follows the caron 4, at vowel height and before the word gap, so the literal is vrozděři (`v4/x1-^4^.`). This looks like a locative. "V ...ři jste také nebyla ještě letos?" = "In/At ...ř you have not been this year either?" reads better than the isolated "Vrozděř." The place is unidentified and I do not claim it. Correct the literal, and offer the split `v R-` as a hypothesis, with "Rozděř" unverified. Note also that "Ponávlink" adds an á with no heavy stroke visible (`6/2v0.29` is po-n-v-li-n-k). Present it as literal "Ponvlink" with the a marked as guessed.

5. **minor: "vidět" is followed by a question mark.** Crops `z6.jpg`, `y1.jpg`. The small sign after 1, with its tick below, has the same form as the writer's `?` after the two other questions. It is missing from the transcription. "zdali bychom se mohli vidět?" Add it.

6. **minor: "středu" hook is on the dash.** Crop `v2.jpg`. The hook sits over the dash as in `neděle`, so the signs are `51-^1:`, literally stědu, with ě. The key entry "1 with caron: tř in středu" is then unnecessary; delete it and note simply that ř is omitted. Item 12 needs the same change.

7. **minor: "přijeďte" has its i, and the ring is not "ď + a".** Crop `r4.jpg`. A mid mark follows the caron 4 (`64^.z-`), so item 12's "no i after ř" is wrong. The mark on 1 is the same ring as in Maďar, not a caron. The ring therefore means ď alone. In Maďar the a is simply unmarked, so "a ring on 1 gives ď + a" should go.

8. **minor: address and postmarks are not used, and the date claim is too weak.** Crops `r6.jpg`, `r7.jpg`, `v5.jpg`. SOLUTION.md never gives the clear address. It reads "Známé slečně sl. Mařence Pařezové, Dobřeň, p.p. Suhdol". The second postmark reads SUKDOL (Suchdol) with a year 06 that is clear at 3x. Dobřeň is a part of Suchdol in the Kutná Hora district, about 2 km from Suchdol (web search this session; https://en.wikipedia.org/wiki/Suchdol_(Kutn%C3%A1_Hora_District)). That puts the addressee near Čáslav and fits "podíval domů". Record the address and the year 1906 from the postmark, with day and month still unread. Do not confuse this Dobřeň with the one in the Mělník district. This also bears on sister card hcp-1786 (Kutná Hora) as a hypothesis only.

9. **minor: the check in decode.py is too weak.** It accepts a word if the literal is a subsequence of the reading, so any inserted letters pass (finding 3 slipped through this way). The reading printed at the end is the typed column, not derived. Tighten the test so that only unwritten a/á may be added, and say in SOLUTION.md what the command does and does not produce. It should also print the literal as the primary output.

10. **minor: SOLUTION.md and the transcription disagree, and smaller points.**
    - Item 5 cites `91-1.c-:`, but the file has `91-1.c-`. The pixels show dash then `?`; the "two dots" are not separate from the question mark as far as I can see (crop `p2.jpg`), so the "unexplained" dots can probably go.
    - "přišli": crop `z4.jpg` shows one small mark or a very tight vertical pair after 0, unlike the wide horizontal pair in `parku` and `mohli`. Read as i, this word need not be an exception; "mohli" stays one.
    - A dot after `jednoho` (`z3b.jpg`) is not in the transcription; probably punctuation.
    - `marše`: no caron on 5 is visible and this is not listed in item 12.
    - "to" `1/-`: the dash at line end is more likely a line-end mark than a sign; the crossing X of the watermark falls on this sign, so the sign itself is less sure than stated.

11. **minor: status wording.** "Whole message read" overstates. Three words are unread and two more are unidentified. Say "message read except for ...", and carry that into the report.

## Findings on the three unread words (no fix, for the record)

- `?9`: the blot is H-shaped, like the solver's joined 1 + 4 in "tři", not like 6 + 0 with dots (`r1.jpg`). "pluk" has no support from the pixels; the solver rightly leaves it unread, but "[?regiment]" should be removed from the translations or marked as sense only.
- `?-6-`: the first sign under the specks looks most like 2, which would give "nebe", but this is not secure and no sense follows (`r3.jpg`). Stays unread.
- `?1_0v41_`: a heavily scribbled sign, a heavy 1, a tall oval partly under the watermark, v, 4, heavy 1 (`r2.jpg`, `r2b.jpg`). "čtvrtá" stays a sense guess, reasonably disclosed. The oval is not clearly 0 and could be c.

## Disclosure

The solver disclosed "nedovolil" (crossed 8 is really there, so the sense call is fair), the heavy-stroke exceptions, and the guesses. No undisclosed use of a published solution. The restorations are labelled, apart from findings 3 and 4 above.

## What I could not verify

- Day and month of either postmark. "May" rests on the text only.
- "Ponvlink" and "Vrozděři" as places.
- The three unread words.
- The Vodranty source pages in SOURCES.md were not re-fetched. The name itself agrees with what I know of Čáslav.
- Whether the sender of hcp-1786 is the same person. I read only that card's SOLUTION.md.

## Disposition

REVISE. Correct findings 1 to 4 in the transcription and all three language versions, then address 5 to 11. A new review round is not needed for these corrections alone unless the reading of the unread words changes.
