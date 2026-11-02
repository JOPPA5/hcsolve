ACCEPT

# Review 1 of hcp-1168 (reviewer: Claude Opus 5.5, 2026-11-02)

The reading stands. I tried to break it sign by sign and could not. No sign value, word or clause needs to change. Six minor findings remain, mostly about how the evidence is described. The first three should be fixed before the report is written.

## What I verified and how

- **Solution command.** `python3 -I ciphers/hcp-1168/work/decode.py` exits 0. All 4 hashes are OK, with 365 signs, 359 by table and 6 by sense. The output matches the plaintext in SOLUTION.md.
- **Printed body.** The body the script prints is a hard-coded string, not generated text. I checked it separately: with spaces and punctuation removed, it equals the `READ` table that the decoder asserts against (283 letters, identical).
- **Independent decoder.** `review/work/own_decode.py` shares no code with `work/decode.py`. It uses the hcp-1174 table plus the new values, kept apart, and outputs one line per row. It gives the same letters, and with the 6 tagged signs taken at face value it gives `koronáBol`, `UdvPzPlve`, `CSokolva`, `Kirig`, which is exactly what the solver reports. It found 31 distinct signs and 365 tokens, and every token is covered.
- **New-value counts.** They match SOLUTION.md: `6.` 5, `6` 6, `2` 5, `4.` 4, `.1` 3 (one of them tagged).
- **Transcription against the scan.** I read every cipher row, including the signature and the two verse words, on my own 2x crops of `work/hires/*_adr.jpg` (`review/work/b_*.png`, `last_*.png`). There is no disagreement with `work/transcription.txt`. I spot-checked the solver's corrected places: jobban, fizetik, fizettem, krájcár against krajcár, and the `3,` in krajcárral. All are as now transcribed.
- **Enlarged checks, 4x to 8x** (`z_*.png`, `cmp_*.png`):
  - `koronából`: the body is a serifed 1 with a clear comma, not a crossed 7. The hairline is not a crossbar. The reading is good, and this tag is, if anything, over-cautious.
  - `sírig`: a plain crossed 7 with no comma; the stamp lies near it but hides nothing. Disclosed correctly.
  - `csókolva`: blotted body, tail of a 2, clear comma. Disclosed correctly. The dot over the `5,` is there, as stated.
  - `.1`: a single left dot in hozzájutni and in Anyukád. In `üdvözölve` there is a lower dot and a thick blob at the end of the serif, which may be the upper dot of `:1`, so `ü` has more support than the solver claims.
  - `szerető`, first sign: this is the most doubtful sign not tagged. Its top is a closed loop, so it resembles a 4 (the solver's notes record that it first read it as `4.`). On `cmp_sz.png` it matches the crossed 7 of `sokszor`: the bar runs well past the stem to the right, while no `4.` on the card does this. `7.` stands on the pixels.
  - `elszavalja`, `Saját kis versembe zárni`, `Szeretném én`, `Hogy mikor ajkad`: readable as stated. The stroke over `elszavalja` is the detached comma of the line above.
  - Picture side (`pic_note.png`) and address side read as stated.
- **Language and context.** The text is natural, informal Hungarian of the period with plausible spellings. Kreuzer and crown fit 1916. Recipient, town, signature and the salutation agree with hcp-1174. The arithmetic (9 = 8 + 1) is real and comes from the signs. No word looks forced; the text is long enough (365 signs, 31 values) that a monoalphabetic fit like this one cannot arise by chance.
- **Disclosure.** All 6 sense-read signs are tagged and listed, and they add up. Published-solution status is stated honestly. Nothing suggests outside material was used.

## Findings

1. **Broken cross-reference (minor).** The plaintext, the English and the Slovak all say "see point 3" for `keves`. Point 3 of the numbered Uncertainties is `csókolva`; `keves` is an unnumbered bullet. A reader of the report would be sent to the wrong place. Fix: number it or name it.

2. **e/é statement is wrong, and it bears on `keves` (minor).** SOLUTION says long and short vowels are not separated "except a/á". The table also separates e/é: `2.` is é and `1:` is e, and é is written with `2.` in `Édes`, `és` and `még`. So `kevés` would need a spelling slip, not just a normal reading of the signs, because `7 1: 3. 1: 7,` has `1:` as its second vowel. That levels the two options: `kedves` drops a d and `kevés` swaps a vowel sign. Together with the sense, this favours `kedves`, or at least takes away the claim that `kevés` is the unforced reading. Fix: correct the sentence and restate the comparison. The reading stays open.

3. **`olan` may be an artefact of the table (minor).** The dotted row of the alphabet gives digraphs: `4,` g / `4.` gy, `6,` n / `6.` ny, `7,` s / `7.` sz. By that pattern `5,` l / `5.` belongs to ly. Then `0 5. 1. 6,` is simply `olyan`, as written. `5.` = l is taken from hcp-1178/1179 (`a legszeb`, `csókollak`), so the writer also uses it for plain l and this is not proved. It is the only `5.` on this card. Fix: mention the alternative beside `olan`, and do not call it "parallel" to `inyen` without this caveat. `inyen` remains a real oddity, since `6.` there is clear.

4. **`üdvözölve`: "written like plain 9" overstates (minor).** On `cmp_oe.png` the plain 9 of `pár` has a tail that flows straight out of the ring. The two signs in `üdvözölve` have a separate squared head at the start of the tail, with a notch against the ring. That is `0,` with its comma touching. The table value `0,` = ö is therefore probably written as such, the p-versus-ö conflict is weaker than stated, and the "9-for-ö habit" should not be used as supporting evidence under "Why I believe it is correct". The tags may stay. The reading is unchanged.

5. **"Seven values are new" conflicts with the rest (minor).** The table bolds five (`2`, `6`, `6.`, `4.`, `.1`), the key paragraph and NOTES.md list the same five as new with `4` confirmed. Fix: state one number.

6. **`adóságomat`: the dot is not clearly a "high dot" (minor).** On `z_adosa.png` the dot sits lower than the usual `1'` (about 35% down the sign against about 23% elsewhere). The hyphen lies at the foot of the sign, where the lower dot of `1:` would be. `1:` cannot be fully excluded on the pixels; `á` is confirmed by the word. SOLUTION asserts this from the sign alone. Fix: say it rests partly on sense (tagging it would make 7 sense-read signs).

## What I could not verify

- The HistoCrypt article linked from the portal: not checked by the solver or by me, so whether it treats this card is unknown.
- The postmark year. I read `91?` with a last digit that looks like 5 or 6, then `JAN`. It does not settle 1916, as SOLUTION says. The written dates give 1916.
- A printed source of the verse: not searched.
- Punctuation of the money passage: none is enciphered, so the clause division is interpretation, as disclosed. The note on the picture side seems to use commas (`1916, I 30,`) where the solution prints dots; this is trivial.
