REVISE

# Review 1 of HCP1239, Claude Opus 5.5, 2026-11-02

The decipherment stands: the Jolánka key turns the card into coherent Hungarian and I found no wrong letter that changes the message outside the points below. Two normalizations should change, and one of them alters the meaning of a sentence. The literal ledger already supports both fixes. The sign notes on h/d also need correcting. No new sign reading is needed for any of this.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1239/work/decode.py`: all four SHA-256 values OK; 20 rows plus stamp rows printed, identical to the literal block in SOLUTION.md.
- **Independent decode.** `review/work/indep_decode.py` (run from the cipher directory) holds my own sign-by-sign keying of rows 1 to 20 from my own crops (`review/work/crop.py`, `crop3.py`, `crop4.py`; output in `review/work/crops2/`), with the sign table taken from ciphers/hcp-1216/SOLUTION.md. It compares row by row with the solver's output. 16 of 20 rows are identical letter for letter. The other four:
  - Rows 3 and 6: I key the d-shaped sign where the solver writes p and h; the word decides, see finding 3.
  - Row 14: my sign is left unresolved (`?`), the solver has s from sense. Disclosed.
  - Row 19: unresolved signs at the three places the solver discloses; my one letter difference is the cross, keyed j, see finding 4.
- **Pixels, every row.** All rows were read on the enlarged crops of the hires scan, including rows 19 and 20 across the whole bottom edge, and the stamp box. Rows 5, 6, 8, 11, 13, 14 and 19 were enlarged further.
- **Key coverage.** Every written sign is accounted for except the disclosed deleted signs in row 19 and the cursive word in the stamp box. No sign was skipped.
- **Picture side.** Print only (Asszonykám adj egy kis kimenőt; Szabadság, szerelem... Petőfi). No cipher, as claimed.
- **Context.** Addressee and town in clear agree. Postmark shows 912 JUN and a JÁSZ place name, as claimed. No day legible to me either. Móczár recurs as a surname on sister card HCP1295, which supports the reading of row 11 (not cited by the solver). Portal capture shows no attached solution; no published solution appears to have been used.
- **Language.** Period Hungarian with the writer's known habits (dropped double letters; j for ly, stated in ciphers/hcp-1212/SOLUTION.md). Not words forced onto noise: long unforced phrases (*Becses sorait köszönettel megkaptam*, *Fekete ruhában is eljöhet*, *Biztató válaszát várva maradok őszinte tisztelője*).

## Findings

1. **major. Row 5 is mis-normalized: the card reads *szenved, de nem tehetek róla*.** The ledger's literal *szenvedde nem te-hetek* divides without any emendation into *szenved | de | nem tehetek róla*. On the crop (`crops2/r5.png`) the first d is a clean short-left, long-right sign. The second is a pale long stroke whose short left tick is red, again the d shape, followed by three-bar e. There is no reason to read t there. SOLUTION.md (uncertainty 7) offers *szenvedde/szenvedte* and normalizes to *szenvedett, nem tehetek róla*, which changes the tense and drops the written word *de*. Correct text: *Igazán sajnálom, hogy én miattam annyit szenved, de nem tehetek róla.* English: "...that you suffer so much because of me, but I cannot help it." Fix the normalized file, the English and the Slovak, and rewrite uncertainty 7.

2. **major. Row 8 *estejre* is *estélyre*, not *estéjére*.** Literal *dalestejre* needs only the writer's documented j for ly (HCP1212: "ly not used – the writer writes j") to give *dalestélyre*, from *dalestély*, a song soirée. That is a real compound, and *estély* suits the following sentence about dress. *Estéjére* needs an inserted syllable and is awkward Hungarian. Normalize to *jöjjön el a dalestélyre csütörtökön ide*, "come to the song soirée here on Thursday". The first signs do show the d shape: a blotted short upper left stroke, a thin long pink stroke to its right, then two blotted bars (`crops2/r8.png`). So *dal* remains partly blotted and should stay disclosed, but the case for it is stronger than the solver states, and uncertainty 3 should be reworded.

3. **minor. The h/d statement in the key section is wrong in one place.** SOLUTION.md and the ledger say the h of *tehti* in row 13 is the d-shaped sign (token `D>h`). On `crops2/h13.png` it is the proper h: long pink stroke on the left, short red stroke on the right. The token should be plain `H`. Conversely the first sign of *hetek* in row 6 (`crops2/r6.png`), token `H`, is d-shaped: short blotted upper left, long stroke right. So the d-shape-for-h case is row 6, not row 13. The letter is unchanged in both places and rests on sense in row 6; please correct the ledger tokens, the key note and uncertainty 5.

4. **minor. Row 19, the cross.** On `crops2/r19b.png` the cross has a low, flat foot, the same form as the j-sign two signs later, not the mid-height bar of the f in *fekete*. Literal *engesztel j [blot] l j e* is therefore a natural false start, with *-lj-* written and then restarted after the blot. The solver's reading is right and disclosed; state j as the preferred value, not "f, or j". *Engesztelje ki* still depends on the deletion and on a third sign read g from sense; on my crop that sign is s/k-like. Keep it marked as the weakest point. The two signs after *es* (the s of *és* and the fused h) also rest on sense, as disclosed.

5. **minor. Row 13.** *Asszonysággal, is eljönnek* is punctuated oddly in the normalized text. The t-for-k in *eljönet* and the *ha cs tehti* expansion are disclosed and I have no better reading. Consider *...asszonysággal. Is eljönnek* or a note that the punctuation is editorial. No change to the letters.

6. **minor. Add the HCP1295 cross-reference** for Móczár to the reasons for correctness (Jáger Józsi "hazamegy Móczárhoz" on that card; the writer spells it Moczar there as here).

## Not verified

- The stamp-box cursive word (it begins with a looped capital resembling H or F; I cannot read it either). It is a single word, alone, so by the run's rule it does not block completeness.
- Row 14, fourth sign of *édesem*: overwritten blot; I can confirm neither s nor k-8. Sense only, as disclosed.
- Accents throughout, and the postmark day and full place name.
- The historical identity of the sender or of Móczár. I did not search for a dalestély in Jászárokszállás in June 1912.
- I keyed the transcription after having read the solver's plaintext, so my pass is a check, not a blind reading.

## Verdict

REVISE. Fix findings 1 and 2 in the normalized text and all three translations, and correct the notes in 3 and 4. These are normalization and documentation changes, not a new reading, so no second review round is needed if nothing else changes.
