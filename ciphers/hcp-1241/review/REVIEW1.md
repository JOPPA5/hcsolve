ACCEPT

# Review 1 of HCP1241 (Jolánka family, Feri to Tóth Jolánka)

Reviewer: Claude Opus 5.5, 2026-11-02. The verdict is ACCEPT: the reading stands and only minor points remain. They can be fixed in the response without a new round.

## What I verified and how

1. **Solution command.** `python3 -I ciphers/hcp-1241/work/decode.py` ran. All four SHA-256 checks print OK. Its 20 literal rows match the block in SOLUTION.md.
2. **Independent decode.** I read the whole card from my own crops (`review/work/crop.py`, `review/work/crops/`, 2x to 5x, plus `blot.py` for the green channel). I wrote the signs under neutral names in `review/work/my_signs.txt`. `review/work/my_decode.py` then decodes them with the key rebuilt from `ciphers/hcp-1216/work/graphic-key.json`, not from the solver's decoder.
   - Result: 20 rows, 299 signs, 0 rows differ from the solver. The two doubtful signs are excluded from the comparison, and the h/p sign is compared as one class.
   - This transcription is not blind, because I had read SOLUTION.md first.
3. **Key coverage.** All 297 identifiable signs fall in the HCP1216 classes. No new sign value is needed; only row 18's first sign and row 20's third sign remain open. A plain monoalphabetic key gives continuous Hungarian, so forced reading is not a credible explanation.
4. **Pixels, every row.** Rows 1 to 20 were checked sign by sign, including the row-crossing ones. I also enlarged the signs that decide words:
   - The d signs (short stroke to the left of a long one) in fordulok, édes, gondol and both in Dudás are real. The n in gondol and talán has two equal strokes beside them.
   - Row 12 k has looped forms but only k fits, in teszek/ezek.
5. **Restorations, each on the pixels.**
   - Row 20 second sign, i: confirmed. There is a clear dot above, and the blot has a light spot where the loop of the i sign would be. The plain cross + in fejét (same row) has no dot and no loop. The solver's call stands.
   - Row 20 third sign, [s]: a real restoration and disclosed as one; see finding 2.
   - Row 18 first sign, {b?}: disclosed as doubtful; see finding 3.
   - Stamp panel: "ke[d]vese" is smeared as stated. Only "Fe" of the signature is visible; the rest is under the pink blot, as stated.
6. **Language and context.** The text is ordinary period Hungarian with the informal spellings of this family (semi, nagyóbb). Dudás is a real surname. Feri, Tóth Jolánka, Jászárokszállás and "Isten vele" all fit HCP1216. Translations were checked and are faithful in both languages.
7. **Plain parts.** "tiszteltetem a kedves" and "mamáját" are on the card as stated, and the panel reads as stated. The picture side carries only the printed texts, as stated, with no handwriting.
8. **Sources.** The portal metadata matches SOURCES.md. No other SOLUTION.md in the repo mentions Dudás.

## Findings

1. **Minor: a written point is missing from the ledger.** Row 17 has a clear point just after the p of vasárnap (`review/work/crops/dots16.png`). It looks the same as the point after reményem in row 16, which the ledger does record. It supports the solver's sentence break there and also supports the split into "távol|bo…" as a new sentence. Add `.` after P in row 17.
2. **Minor: the row 20 blot has an undisclosed alternative.** SOLUTION says only s gives "Juliska", which is true but circular. The blot has a light interior (`review/work/crops/blot_g.png`), so it is not simply a solid stroke. Its outer shape is a crescent bulging to the lower right, which suits a bled right bowl, and it is about as wide as an opposed-bowl cs. So cs, giving a diminutive like "Julicska", cannot be excluded on the pixels. I have no attestation for that form and it does not change the sense, since the person is a Julia either way. Keep [s] and add the alternative to uncertainty 1. "Juliska" should be presented as the likeliest form.
3. **Minor: row 18 first sign rests on sense.** The sign is a thin diagonal with a flag at the top and a loop at the base (`review/work/crops/r18a.png`). The four sixes on this card have a curved stem and no flag. So b is a context call, and SOLUTION says so. I found no better reading. "Távolbó[l]" should stay marked as doubtful in the report too. The sentence still reads if the sign is left open.
4. **Minor: note 5 misstates "tört[én]t".** The literal t o r t e t contains the e, so only the n is missing, plus the ö dots and the é accent. The notation should be "tört e[n]t" or the note reworded.
5. **Minor: the key table does not fit this hand exactly.** The d sign is described as "joined", but here the two strokes are separate and parallel. What separates d from h/p is the order: short then long for d, long then short for h/p. Add this to the table, because the d calls depend on it.
6. **Minor: small plain-text restorations are not disclosed.** The final t of mamáját lies in a pink blot. The final n of "szamtalan" also runs into a blot. "hű" and "reményű" are written with two dots, like ü, and are normalized to ű. List these beside uncertainty 6.
7. **Minor: the decoder is close to an identity map.** Ledger tokens are named by their plaintext letters, so `decode.py` proves little by itself. SOLUTION does say the ledger is a manual transcription, and the reading is backed by my neutral-name pass. No change is required, but the report should not present the command as independent proof.

## What I could not verify

- **Postmark day.** Both postmarks show 12 MÁJ and a day beginning with 1, but I cannot read the second digit with confidence. The solver's caution is right. 12 May 1912, the date in the file name, was a Sunday, which is compatible with "vasárnap" but proves nothing.
- **Published solutions.** I did not open the portal's linked HistoCrypt article. The "no published solution" claim rests on the solver's and orchestrator's checks.
- **The name.** I could not confirm Dudás Juliska as a real person, or the -bó form as this writer's dialect.
- **Context.** What had to be destroyed and why is unknown, as SOLUTION says.
