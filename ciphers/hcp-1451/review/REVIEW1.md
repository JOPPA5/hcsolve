ACCEPT

# Review 1 – HCP 1451 (pc_hcp_132), Atbash "True and always loving"

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Round 1 (marker DONE1).

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1451/work/decode.py` (from repo root): source hashes OK, output
   `Gifv -> True / Zmw -> And / Zodzbh -> Always / Olermt -> Loving`, "19 cipher letters decoded". Matches SOLUTION.md exactly.
2. **Independent decoder.** `review/work/atbash_check.py` (own arithmetic Atbash, own diplomatic transcription `Gifv / Jmw / Jodjbh / Olermt`):
   - literal, J kept as J: `True Qnd Qlwqys Loving`
   - J-shaped glyphs read as Z: `True And Always Loving`
   - 25-letter (I/J merged) Atbash as a control: `TRUE ROD RMWRYS MPVIOG` – nonsense, so the standard 26-letter Atbash is the rule.
   The key is a single fixed rule and covers all 19 letters; nothing is left undeciphered.
3. **Transcription against the scan.** Own LANCZOS crops of `source/address.jpg` in `review/work/` (all.png 4x; line1.png, line2.png 6x; line3.png, line4.png 5x; line1_z.png 8x; line4_mid.png 9x). Sign by sign:
   - Line 1 `Gifv`: copperplate G, dotted i, long-descender f, v with hook. Confirmed.
   - Line 2 (the completion): three letters, not four – a J-shaped capital, an m (three downstrokes, two arches), and a looped w. I see no fourth letter; the earlier GPT four-letter G?NV readings are not supported. Confirmed `?mw` → `And` when the capital stands for Z.
   - Line 3: J-shaped capital, o, d, **dotted j**, b, h. With J-glyph = Z this is `Zodzbh` → Always.
   - Line 4 (the completion): O, l, e, then a pointed-shoulder r (no closed top hook like the line-1 v), m, crossed t. Confirmed `Olermt` → Loving; the earlier OLEVMT/LOVENG reading is correctly rejected on the pixels.
   - Below: dash, ditto-like tick, dash – no letters. Picture side: print only (checked the image in source/).
4. **Language and context.** "True and always loving" is a natural Edwardian English closing phrase; English postcard posted St Albans 8 Feb 1906 to Miss L. Schuller, Berkhamsted. Fits. No names/dates in the plaintext to check.
5. **Sources/credit.** Portal status "Not solved", no attached solution; I found no indication a published solution was used. Earlier GPT work (Atbash identification, TRUE, ALWAYS) is credited in SOLUTION.md.

## Findings

1. **minor – transcription is normalised, not diplomatic.** All three cipher-Z positions are written with a J/j glyph: the two capitals (lines 2, 3) are J-shaped, and the line-3 lowercase is a clearly dotted j (the dot is a distinct ink point at 5x, not a smudge). `work/transcription.json` records them as `Z`/`z`. SOLUTION.md discloses the ambiguity, but the transcription file should give the literal glyphs (`Jmw`, `Jodjbh`) with the interpretation J-glyph = Z stated as an interpretation, or at least a `diplomatic` field next to the normalised one.
2. **minor – "writer's slip" understates the pattern.** SOLUTION.md uncertainty 2 calls the dotted j a possible slip at one spot. Because *every* Z of the ciphertext (3/3) is written in a J/j form, it looks systematic (the writer wrote Z as J, or used a J-like z form and dotted it once), not a single slip. The report should say so; the reading is unaffected.
3. **minor – line 2 letter count.** The report should briefly note why the earlier 4-letter reading was abandoned (the "n" of G?NV is the second arch of m), so a reader of the PDF can follow the correction without opening work/.

No blocker or major findings.

## What I could not verify

- The writer's intent for the J/j glyphs (systematic Z→J substitution vs. a J-like z allograph) cannot be decided from one card; it does not change the plaintext.
- Sender identity: not on the card.
- I did not re-open the live portal page; I relied on source/metadata.md and SOURCES.md for status and attachments.
