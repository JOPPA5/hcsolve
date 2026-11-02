REVISE

# Review 1 of HCP1226 (Claude Opus 5.5, reviewer, 2026-11-02)

The key, the type and the body of the message stand. The closing on the stamp box is misread: the claimed unreadable word is legible, and the "j" restored there does not exist. Row 27 has a wrong sign and its normalized text contains letters that are not on the card. These are concrete fixes, so the verdict is REVISE, not REJECT.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1226/work/decode.py` ran. All four SHA-256 hashes printed OK, and the output matches the literal block in SOLUTION.md, including the normalized text.
- **Independent decode.** `review/work/verify.py` holds my own row-by-row transcription and its own sign mapping, and diffs it against `work/ledger.txt`. The ledger was in view while I read, so this is independent in code and pixels, not blind. Ledger 724 signs, mine 724 (S3 has one more, S4 one fewer). Differences: row 27, S3, S4 only (findings 1 and 2).
- **Pixels.** I read all 28 rows, the edge run and the stamp box on my own 2.2–5x crops of `work/hires/*_adr.jpg` (`review/work/a1.png` … `h4.png`, `st.png`, `r27*.png`, `a27.png`, `r18.png`, `r3*.png`, `edge.png`). For the stamp box I wrote `ink.py` and `ink2.py`, which suppress the green print by chroma (`s34v.png`, `stink.png`, `s3i.png`, `s4i.png`).
- **Key and coverage.** The sign table agrees with HCP1216 `work/graphic-key.json`. Every sign in rows 1–28 and E1 gets a value; only the row 18 scribble lacks one. No key was fitted on this card.
- **Language and context.** Period Hungarian, formal *maga* address, family formulas (*becses sorait megkaptam, mit köszönök szépen*; *édes egyetlen reményem*), addressee and signature fit. Printed picture-side text checked on `pic.png`: as claimed. Address as claimed. Right-edge run confirmed on `edge.png`: rotated two bars then section mark, i.e. *a k*, completing *rokonin|ak*.
- **Published solution.** The solver names none, and nothing in the directory suggests one was used. The key transfer is disclosed.

## Findings

1. **major — S3 and S4 are misread; the "unreadable word" and the "j" are both wrong.** The ledger has `S3 ) E M j? O L` and `S4 H/d ? ? ? V I`, giving *édesem jol[…] viszontlátásra* and "my darling Jol[…]" in the translations. With the green print suppressed (`s34v.png`, `s3i.png`; also visible as dark dashes on `s34.png`):
   - S3 reads right bowl, three bars, **three** strokes (the third runs inside the triangle), then **two bars** at about x 2975–3005, y 425–450, then a **six** whose tall stem is what the solver took for the j stem and whose bowl lies on the triangle's right edge, then loop, wave. That is `s e m a b o l`, with no j and no foot to restore.
   - S4 reads tick + long stroke (d), the upper part of a cursive loop (o, the only partial sign), a descender with hook (g), chevron, dotted curve: `d o g v i`.
   - Together: **Isten vele, édesem, a boldog viszontlátásra**. This is the writer's own closing, word for word: HCP1251 and HCP1248 (Feri), and HCP1205 (the same formula on Jolánka's side). I read the signs first and found the sister cards afterwards, but the o of S4 is still partly supported by the word.
   - Fix: correct both ledger rows, normalized text and all three translations; drop "Jol[…]"; delete uncertainties 2 and 3; update the status line and the claim of unread signs. Mark the S4 o as partial. The solver must confirm this on its own crops.

2. **major — row 27 has a wrong sign, and the normalized text shows letters the card does not have.**
   - The sign before the last n of *elégeta_en* has **two bars**, with clear paper where a third would be (`a27.png`, `r27b.png`). It is a, not e. The ledger's E is wrong and the literal word is `elegetalan`. SOLUTION item 1 says "every sign is clear" yet carries this error.
   - The normalized line prints *modorommal meg lesznek elégedetlenek*, with -mal and -ek supplied and without square brackets, though brackets are used elsewhere (*rokon[a]inak*). Only a trailing "[editorial]" marks it, and "elégedetlen" is not what is written.
   - The division needing fewer additions should lead: *modorom meg lesz nek[ik] elégetalan [= elégtelen?]*, "my manners, for their part, will be insufficient for them". The *meg* then has its normal contrastive sense, and the privative ending is what the card shows. The negative sense fits the next sentence (what occupation she will tell them).
   - Fix: correct the ledger; print the literal word in the normalized text with any additions in brackets; state that the sense is a reading of one misspelt word, not of clear text; make the translations follow. After finding 1 this is the only soft spot on the card, so under the batch rule it can pass as a single un-understood word only if the rest of that clause is kept to what is written.

3. **minor — row 18: the scribble is most likely e, and *be* should go.** `r18.png` shows a dense blob with bar structure, the size of a three-bar sign, inked over. Read as e the run is *kimegyek eléjébe az állomáson*, one word, the normal *eléjébe megy* "go to meet". The normalized *eléje be az állomáson* and item 5's "awkward" stem from the false division. Keep the sign as `[#]` in the ledger with the value by sense, and fix the normalized text and item 5. The English is unaffected.

4. **minor — ledger marks a dot that is not on the card.** `O:d` is defined as "dot mark seen over the sign". In row 3 only the first o of *köszönök* has dots; the second and third have none (`r3o.png`). Either transcribe them as plain O or redefine the mark. The same row's *kaptam* sign is also not the shape SOLUTION item 6 implies: it is a separate tick above-left of a long stroke (`r3p.png`), the d form, not the tall+short of *szépen* in row 4. Ledger H is a value by sense there; say so.

5. **minor — literal *édes|sem* is a doubled s.** S2 ends in s and S3 begins with s, so the literal text is *édessem* at the row break. The "édesem ×5" claim and the list of normalized spellings (item 8) should say this. My crops agree with the ledger on both signs.

6. **minor — "Why it is correct" must be updated.** "Only the signs of items 2 and 5 left without a value" no longer holds after finding 1. The 724-sign total can stay, since S3 gains one sign and S4 loses one.

## What held up under attack

Rows 1–26 and 28, E1, S1, S2, S5–S7: my reading gives the same letters as the ledger. Disclosed calls I checked and accept: *sa+nos* (row 15, upright cross clearly written), *szetném*, *de* with the h-form sign, row 25 *majd*, *leírni* with the i dot (on my crop a dot is visible, so item 6's "shows no dot" may refer to the second i; the solver should state which), row 17 overwritten *hetek*-area signs, and S7 tilted cross as f. *még soká tehetem* without *nem* is real and disclosed, and "it will be a long time before I can" is a fair rendering.

## What I could not verify

- The S4 o is partial under the print and its lower loop is lost; the word sense supports it.
- The sense of row 27 (finding 2): both readings of the clause are interpretations.
- The postmark: left mark begins ÉRSEK…, the centre mark shows 17 and a second illegible group (`pm1.png`), so no year or place is proved. Disclosed in item 10.
- Accents: not transcribed in the ledger, so I did not check them sign by sign.
- Whether *micsoda foglalkozást mond majd* means her occupation or his; the English keeps this open, which is right.
