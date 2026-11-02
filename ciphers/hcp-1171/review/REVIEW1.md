ACCEPT

# Review 1 of hcp-1171

Reviewer: Claude Opus 5.5, 2026-11-02. Round 1, from DONE1. The solver's files and source/ were not changed. My scripts and crops are in review/work/.

## Result

The reading stands. The card is open Hungarian, later struck through in brown, with only the salutation and the signature enciphered: 20 signs, giving Kedves Margitkám and Árpád. I could not refute it. All findings below are minor. Finding 1 is a real transcription slip in the address and should be fixed. The others are editorial.

## What I verified and how

1. Command. `python3 -I ciphers/hcp-1171/work/decode.py` runs and all 4 SHA-256 hashes match both the script and SOURCES.md (also recomputed with shasum). Output agrees with the plaintext in SOLUTION.md apart from the added commas and line joins, which the solution discloses. The open text is hard-coded in the script, as the solution also says.
2. Independent decryption. `review/work/own_decode.py` (run from review/work) parses the key tables of FINAL cards hcp-1174 and hcp-1178 rather than using the solver's table, and decodes tokens I typed from my own crops `top.png` and `sig.png`. Output: `kedves margitkám`, `árpád`, 20 signs, no key conflict between the two cards. All 13 distinct signs are in the sister keys, and the key was not fitted to this card.
3. Cipher signs against the hires scan, sign by sign (`top.png`, `sig.png`): `7 1: 3 3. 1: 7,` / `8 1. 3, 4, 1 8, 7 1' 8 !` and `( 1' 3, 9 1' 3 )`. All confirmed. The `4,` has a brown strike-out through its lower stem, but the hook to the right is visible. No ciphertext lies elsewhere on either side; the picture side carries no writing.
4. Open text, on red-channel crops of every row (`l1`...`l6`, plus zooms `z_*`, `y_*`, `x_*`). All rows read as claimed, including the checked points `mind` (minims m-i-n-d, i dot visible, `y_a.png`), `kettőnket` (`x_a.png`; nothing follows it before the margin rule), `jól`, `ilyen`, `no de`, `ujságot`, `irhatok`, `Más`, `téged`, `legtisztáb` with single b and a hyphen below (`y_tad.png`, `z_lt.png`), and the quatrain.
5. `csókollak` (`w_col.png`, `w_rb.png`, my own R minus B separation). Solver's caution is right: -k-o-l-l-a-k is clear, and the c-s-ó region shows three letters of the right widths under the print, with the hooked foot of an s. The heavy slanted stroke beneath it is the ascender of the l of `szivvel` on the next row, not part of this word, so it does not argue against the reading. The verb is well supported by sense and hcp-1174 but its opening is not independently legible. It is disclosed as the least sure word.
6. Language and context. Period Hungarian with normal informal spellings, a real rhyme, and a coherent situation (late visit, apology, walk home on frozen ground in late November). Recipient, town and route match the Mezőkövesd series. hcp-1179 does open with `Kedves Margitkám!` in clear and hcp-1174 is signed Árpád in cipher, as claimed. The postmark gives 915 NOV 2?, with a trace of a second digit consistent with the portal's 22.
7. Honesty. The key's transfer from hcp-1174 is stated. The unchecked HistoCrypt article is stated. No published solution appears to have been used.
8. Verbless clause `csak mégis mind a kettőnket / hogy ...`. All words are read and the gap is the writer's, so it is not an unread clause. The translations mark the supplied verb. This is one defect in a clause that is otherwise understood, not a partial reading.

## Findings

1. **minor, address word miscopied.** SOLUTION.md and decode.py give `Szépreményű`. On the card (`x_nny.png`, `z_szep.png`) there are four clear minims after é, then y, then u: `Szépreménnyu` as far as the strokes go, with no dots or accent over the last letter on clean paper. Sister cards hcp-1140 and 1152 record `Szépreménnyü`, so the doubled spelling is a known habit. Fix: give the word as written, and note the normal form.
2. **minor, bracket convention collides.** The plaintext legend says `[ ]` means enciphered on the card, but `legtisztáb[b]` uses the same brackets for an editorial letter. Fix: write `legtisztáb` and give the normal spelling in the existing note, or use another mark.
3. **minor, translation notes point at nothing.** English "the purest heart [word implied, see below]" and Slovak "[slovo sa rozumie, pozri nižšie]" refer to an implied word, but no word is implied: `legtisztább szivvel` is complete, and Uncertainties 2 only treats the b. Fix: delete both notes.
4. **minor, the `a` of `mind a` is under-described.** Uncertainty 3 says only that a brown stroke crosses it. On `x_a2.png` the sign is a blotted, heavier shape than the clean `a` of `a legtisztáb`, and a descender from the row above runs into it. It may be overwritten. `mind a kettőnket` is the only idiomatic reading and I accept it, but it rests on word sense and should say so.
5. **minor, `(A)`.** Uncertainty 6 says a thin stroke stands just before it. That stroke is simply the opening parenthesis of `(A)` (`z_A.png`), so nothing extra is there. The note should also cite that hcp-1179 is signed Sz. A., which supports A as his initial; solver only says "likely".
6. **minor, postmark town.** SOLUTION.md gives the postmark as `Mezőkövesd`, but only M is legible on this strike (decode.py itself says so). The town is inferred from the series. State it as such in SOLUTION.md.
7. **minor, needless doubt.** The solution says the dots of `1'` in the signature stand less high than in the top line. On `top.png` and `sig.png` they stand at about the same height in the upper part of the digit. The Arpad alternative can be dropped. It would not change the name either way.

## What I could not verify

- The opening c-s-ó of `csókollak` as letters independent of sense. Solver and I agree on the limits here.
- The second digit of the postmark day; it lies on the stamp and is only faint.
- Whether the HistoCrypt article discusses this card; neither of us checked it. The portal lists it as the source.
- Who struck the text through, and when.

## Register note

The card meets the completeness rule: every word of the card is read, and the one thin word stands alone. Type label MASC is the live register label used on the sister cards.
