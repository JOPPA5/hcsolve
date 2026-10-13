REVISE

# Review 1 — HCP 1218 (round DONE1, partial claim)

Reviewer: claude-opus-5-5, 2026-10-14. The solver hands this over honestly as a **partial** decipherment with one unread clause (A15/A16). I read the whole card from `source/address.jpg`. Everything the solver does read is confirmed, and **the open clause can be read**: it is `csak a pénz fogyott` ("only the money ran out"). The gap came from two misclassified signs in the ledger, not from the writer. With that, the main text is complete; the verdict is REVISE so that the solver can check and adopt (or refute) the reading and then drop the "partial" label.

## What I verified and how

1. **Command.** `python3 batches/jolanka-next-five-2026-10-12/visual-ledgers/decode.py 1218` exits 0, source hash matches, prints 22 main rows, 7 stamp rows and N01.
2. **Independent reading.** 4× strips of the text column and details of A15/A16, the stamp, the annotation and the postmark (`review/work/`, made with `zoom.sh`). Read with the shape table only, then compared with the ledger. I agree with the ledger on rows A01–A14, A16–A22 and S01–S07 apart from the points listed under findings.
3. **Answers to the solver's four priority questions** are findings 1, 3, 4 and 5.
4. **The Petőfi identification.** Correct. The first stanza of *Honfidal* is "Tied vagyok, tied, hazám! / E szív, e lélek; / Kit szeretnék, ha tégedet / Nem szeretnélek?", and the seven stamp rows `tiedvagy / okesziv / elelek / kitszeret / nek?ate / gednem / szetnelek` are that stanza with `tied, hazám` dropped and `téged` for `tégedet`. The solver found the poem only after decoding the phrases and says so; it is a quotation used by the writer, not a published solution of the card. The disclosure in `SOURCES.md` and `SOLUTION.md` is adequate.
5. **Context.** The postmark shows `…SEP…`, in agreement with the portal's 9.1912. "Tegnap … vasárnap" and "első vasárnap volt" put the writing on a Monday after the first Sunday of a month; 1 September 1912 was a Sunday. Addressee `Tóth Jolánka úrleánynak, Jászárokszállás`. `Berénybe` = Jászberény, where HCP 1213 was later addressed.

## Findings

1. **major — A15 reads `csak a pénz fogyot(t)`; the "undeciphered clause" is a ledger error.** Detail `review/work/z-a15-big.png`. After `( ) = S` (`csak`) the signs are:
   - two bars — `a` (the ledger has `E`);
   - tall stroke with tick — `p` (ledger `H`, fine);
   - three bars — `e`;
   - two short strokes — `n`;
   - a diagonal cross **with a clear horizontal bar through it** — that is the crossed diagonal `z`, not the plain `x` = `u`. Compare the plain `x` of `mulat` directly above it in A14 and the crossed one in `roszu`;
   - upright cross — `f`;
   - then, in paler ink beyond the margin line: loop, `gy` group, loop, `Γ` — `o gy o t`.

   So: `…csak a pénz fogyot` + A16 `me(g) azt az egyet megjegyzem…`. In context: *"…de még ilyen rosszul nem mulattam soha, csak a pénz fogyott. Meg azt az egyet megjegyzem, hogy …"* — "…I have never enjoyed myself so little, only the money ran out. And one more thing I note, that …". The solver's segmentation `épen | u | fogy?t` put the word boundary in the wrong place and read `z` as `u`; the conjectures tested in pass 7 (`fogott meg`, `fojt meg`) all kept that wrong `u`. The final loop is `o`, which settles `{i|o?}`.

2. **minor — A16 `me`.** I also see only `/// ≡` before `azt`; `meg` with the `g` omitted (or lost at the line break) is the natural reading. It is a connective ("and also"), not the verbal particle of a verb in A15.

3. **minor — A17, the number.** Two identical digit-like signs, each a clear `3`, followed by `) X ɣ F` (`szor`): `33szor`. I confirm the reading as written. Whether "33 times" is meant literally is another matter: mock weddings and fines are a standard game at a *szüreti mulatság* (harvest ball), which would also explain why "only the money ran out". That is my interpretation and should be marked as such if used.

4. **minor — stamp S05 and S07.** S05: tall stroke + tick, then two bars, then `Γ ≡`: `{h|p} a t e`, i.e. `ha te-`; I see no third bar, so `a` rather than `e`. S07: `) X ≡ Γ // ≡ ~ ≡ S` = `szetnelek`, as the solver now has it; there is no `F` and no room for one. `sze[re]tnélek` is a justified restoration of a slip, correctly bracketed.

5. **minor — N01 is longer than the ledger.** Detail `review/work/z-n01.png` (the small cipher under `úrleánynak`). I count nine or ten signs: `) X ≡ Γ/F ≡ Γ ≡ Γ ≡ ~`, against seven in the ledger (`) Z E ? E T E L`). One `≡ Γ` group is missing from the ledger. As written the note is `sze{r|t}etetel` — `szeretettel` with a single `t`, so only the usual undoubled consonant has to be restored, not "more than a doubled t" as `SOLUTION.md` says. The signs are tiny and partly under the portal watermark; treat the count as ±1.

6. **minor — bar counts.** A03: `egésség-b≡n` looks three-barred to me (`egésségben`), where the ledger has `6 A N` and the solution cites `egésségban` as a preserved source spelling. A21: `≡ X ≡ ~` (`ezel`, i.e. `ezzel`) rather than `A Z A L`. Neither affects the meaning.

7. **minor — translation.** "because it was the first Sunday" is right but unexplained; on HCP 1301 the same writer spends his Sunday at a committee meeting, fire-brigade drill and cinema guard duty, so "first Sunday" is presumably a duty day. Worth a sentence in the report, marked as inference.

8. **minor — protocol.** `report/report.pdf` exists at `DONE1` for a claim the solver itself calls partial; it must be rebuilt. No watcher was running (the solver records that this is by the human's instruction).

## Required for the next round

- Check finding 1 against the scan. If accepted: correct A15 in the ledger (`… CS A K A H E N Z + O GY O T`), put the sentence into the Hungarian and English text, and remove the "partial" status, the pass-7 gap discussion from the claim (keep it in `NOTES.md`), and the `[…]`.
- Correct N01 and S05 in the ledger or say why not.

Because finding 1 changes the status of the whole claim from partial to complete, this needs a `DONE2`, not a direct `FINAL`.

## What I could not verify

- Accents, as on the other cards.
- N01 sign count, see finding 5.
- The day in the postmark.
- Whether a decipherment of this card exists elsewhere; I relied on the solver's searches.
