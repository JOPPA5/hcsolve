ACCEPT

# Review 1 of hcp-1159 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands. I tried to break it sign by sign and could not. Only small descriptive points remain, and none changes the text. The card qualifies as complete under the run's rule: one missing letter (`lá(n)gol`) and one abandoned blot, with everything else reading.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1159/work/decode.py` ran clean: 4 hashes OK, 125 signs, 23 distinct, 1 blotted sign undecoded. Its output equals the plaintext in SOLUTION.md. The word division and the `(n)` are the solver's, as disclosed; the open text is hard-coded, also as disclosed.
2. **Independent transcription and decode.** Before comparing, I transcribed all rows from my own crops of the hires address side (`review/work/crop.py`, `review/work/crops/`, 2x, with contrast; 4-5x at disputed spots) and decoded them with my own script, `review/work/mydecode.py`, in card rows with no word division:
   ```
   édesmargitkám / veddtölemeképes / lapot / svéletisztaszivemet / értedlágolértedégaz
   migasirelnemtemet / távolbanavágyamnekem / hateisitt[?]volnálve / lem
   ```
   125 signs, 23 distinct, sign for sign the same as the solver's ROWS, including row breaks `lapot` and `ve-lem`.
3. **Key.** The values agree with the family tables. `4.` = gy and `1,` = b are not in the hcp-1174 table but stand on several sister tables (hcp-1163, 1164, 1166, 1168, 1169), and here they give the clean words `vágyam` and `Távolban`. The 23-sign table covers the whole ciphertext. No sign needs a substitute value.
4. **Disputed signs on the pixels.**
   - `lágol` (`z_lagol.png`): `5, 1' 4, 0 5,`. There is a clear gap with nothing between `1'` and `4,`. The n is truly absent, so the solver is right not to transcribe one.
   - `az` (`z_end4.png`): closed head, one long straight stem, no lower loop, comma below; compare the two-loop 8s in `z_end3.png`. This is `9,`. The `1.` dot sits against the printed centre line and is a real dot, not a line artefact.
   - `szívemet` end (`z_end3.png`): `1:`, both dots present, one on the line; ends in `8,`.
   - Blot after `itt` (`z_blot.png`): a smeared, overwritten body with a clear comma. An `8,` is plausible but not provable. Leaving it undecoded is correct, and `itt` is complete without it.
   - Close readings of `1'` against `1:` in `lágol`, `Távolban`, `vágyam` and `volnál`: the single high dot is real in each, and in `nem temet`, `nekem` both dots are present.
5. **Heading.** The 13 signs are the same as the heading sequence in the hcp-1174 decode.
6. **Language and verse.** All lines are 7-8 syllable verse in period Hungarian, with exact rhyme `szívemet` / `temet` and `nekem` / `velem`. The word splits `s véle tiszta`, `ha te` and `ég az` are the only sensible ones. Nothing looks forced. `lángol` with `ég` is natural in the album-verse register. The topic fits the picture of a couple with roses.
7. **Open text and address.** Checked on `p1.png` and `foot.png`: `Kérlek írd meg, hogy megkaptad-e a levelet, mert küldtem benne a számbetűket is`; `Mindnyájatokat csókollak. Sz. Á.`; `írjál`; `Tek.`, `Rózsa reményű`, `Sziber Margitka kisasszonynak`, `Szomolya`, `u. p. Bogács`, `Borsod m.` All agree. The accent stroke over the A of the signature is really there. The `a` before `levelet` does look deformed by the tail of the g above, as disclosed.
8. **Picture side and postmark.** The picture side is the couple with roses and carries no writing. The postmark is illegible for a date (`post.png`): I see only ME..., one heavy digit, and a final D. The solver's statement holds.
9. **Honesty.** The portal has no solution attached. The unchecked HistoCrypt article is disclosed. The key's source is stated. Every uncertainty I found was already listed.

## Findings

1. **minor - location of the stray line is misdescribed (SOLUTION uncertainty 6).** The solver places it "between the 4th and 5th cipher rows, over `3. 0 5,` and the end of the row above". On the hires scan it runs from about x 480 to 910 at y about 1300, over `5, 1, 1.` of the `Távolban` row and under `1: 5,` of the `el` row, and it does not reach `3. 0`. On the card's physical rows that is between the 5th and 6th rows, because `lapot` stands alone. It crosses no sign and has no effect on the reading. Correct the description in the report.
2. **minor - wording of `lá(n)gol` (uncertainty 1).** The text says this is "not a restoration of something hidden". The n is nevertheless an editorial supply, resting on sense alone. Call it an emendation in the report so a reader does not take the printed `lángol` for what the card says.
3. **minor - address epithet untranslated.** The English and Slovak sections translate the body but not the address. `Rózsareményű` ("rose-hoped", a mock-honorific) is the one unusual word on the card and deserves a gloss in the report, with the note that it is written in two parts.
4. **minor - Sz. Á. versus Sz. A.** The stroke is clear here, as the solver says. The inconsistency with sister cards that print `Sz. A.` should stay disclosed in the report; I did not re-examine those cards. hcp-1174 is signed `Árpád`, which would fit `Á.`, but nothing on this card names him, so this is only a hypothesis.

## What I could not verify

- The date: the portal name's 1915-11 is not confirmed by the postmark.
- Whether the HistoCrypt article discusses this card (not checked by the solver or by me).
- What the blotted sign was, and what the stray line means, if anything.
- Whether the verse has a printed source. I recognise the type but did not trace a source.
- The Slovak `poslal` assumes a male writer. That fits the family's signature but is not shown on this card.
