ACCEPT

# Review 1 of hcp-1156 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands. I tried to break it sign by sign and could not. Only minor points remain: one wrong count, one overstated claim, and two sign forms that are read by word sense without saying so in SOLUTION.md. They are worth fixing before the report is written, and they do not change a single word of the plaintext.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1156/work/decode.py` runs: "source hashes OK (4 files)", "ciphertext signs: 151, distinct 25". Its output matches the plaintext in SOLUTION.md word for word. Note that the script's assertion compares two strings the solver typed, so it proves self-consistency only; SOLUTION.md says the open text is hard-coded.
2. **Independent decode.** `review/work/decode_review.py`: I retyped all the signs from my own crops, with no copying from `decode.py`, and took the key from the sister tables (hcp-1174, 1179) plus the three values under test (`4`, `4.`, `6`). Result: 151 signs, 25 distinct plus the blotted sign, and it gives the same text line by line: kedves igazszivü margitkám / irhatsz akarmit ne félj / ügyse (lássa) meg senki ha / betüvel nem akkor irjal / ?amokkal bizhatsz bennem / testvér én ügy bizok / benned mint a jo istenkében / hü kedvesed árpád. My sign counts agree with the solver's total.
3. **Transcription against pixels.** Every cipher sign was checked on `work/hires/` crops at 2x (`review/work/crops.py`: h1, h2, c1a to c9b), and every doubtful sign at 3 to 5x (`review/work/crops2.py`, z_*.png). All commas, dots and colons are as transcribed, including the absence of a comma on the three `6` = j signs (`félj`, `irjál`, `jó`), which is what separates j from n.
4. **Restoration and doubtful signs.**
   - Blot, first sign of `számokkal` (z_blot.png): crossbar, stem and a round dot at lower right survive, consistent with `7.`. Disclosed correctly as a restoration. It is a single sign, and `?amokkal` admits no other sensible word beside the clear "betüvel".
   - `7,` of `senki` (z_senki.png): the hook touches the crossbar and makes a small closed triangle, so it resembles a closed 4. The bar runs through the stem to the right as in the other 7s, and `g-enki` is no word. See finding 3.
   - `:1` of `úgyse` and `úgy` (z_L2start.png, z_L5us.png): see finding 2.
   - `1'` of `Margitkám` (z_marg.png): bar right of the stem, as the solver says. `Árpád` (z_arpad.png), written over the printed stamp box: `1'`, `3,` (comma faint, visible), `9` with no comma, `1'`, `3`, in parentheses.
5. **Open text.** I read every line on `review/work/o0..o8, o_date` (full width of the hires scan, unenlarged) and found no disagreement: Szerencsésen haza érkeztem ... Most már; Sokszor csókollak maradok; Mezőkövesd, 1915, XII/28. `ertt` (written with a doubled t), `utól`, `othol`, `berámáz-tattam` are as the solver reports. The capitals N and L of `Nagy Lojzi` are as described, and the name fits. No unread word or clause: the card counts as complete by the run's rule.
6. **Key coverage and consistency.** Every sign decodes. No sign has two values and no letter is forced. `1,` = b is attested on hcp-1179. `4` = f, `4.` = gy, `6` = j are this card's own and do not clash with the family table (no earlier value exists for them).
7. **Language and context.** Natural, informal Hungarian of the period: "úgyse lássa meg senki" runs across the clear word `lássa`, which is a strong check: the cipher on both sides of a clear verb has to give úgyse before it and its verbal prefix meg after it, and it does. "Ha betüvel nem, akkor irjál számokkal" is a sensible statement inside a digit block. Names, recipient, town, date and signature match the Mezőkövesd family; the file name of the scan gives 1915-12-28 independently, and the postmark shows DEC 28.
8. **Sources.** Portal shows no solution and no transcription. SOLUTION.md states that the HistoCrypt article was not checked for this card. No sign of a published solution being used. Picture side: no handwriting, only the printed trefoil, as stated.

## Findings

1. **minor: wrong count and overstated evidence for the new values.** Uncertainty 6 says `:1 4.` is read "`úgy` twice and `úgyse` once" and that `4.` is "fixed by those three words". The card has `4.` twice only: `úgyse` (block line 2) and `úgy` (line 5). My count: `4.` 2, `4` 1, `6` 3. The clear `úgy` in the open text is not cipher evidence. The section "Why I believe it is correct" likewise says the three values are fixed "each by several clean words"; that holds for `6` only, since `4` rests on `félj` alone (plus the sister hint) and `4.` on two words. The values are still sound, because the words leave no alternative, but the text should state the true counts.
2. **minor: undisclosed form of `:1` in both `gy` words.** At 4 to 5x neither of the two signs has the two separate dots seen in `igazszívű`, `betüvel` and `hű`. On z_L5us.png the mark is a single slanted bar left of and parallel to the stem; on z_L2start.png it is a heavy parallel stroke joined to the stem at the top. It reads as the colon dragged into a line, and the sign is certainly not a plain `1`, so `:1` is right; but this is a reading helped by word sense and should be listed with the other sign forms in Uncertainties. It also bears on finding 1, since `úgy` is what fixes `4.`.
3. **minor: `senki` not in Uncertainties.** NOTES.md records that the sign looked like `4,` at low enlargement, but SOLUTION.md is silent. Add one line: the closed-looking 7 with comma, settled by the bar through the stem and by the word.
4. **minor: bracket placement in the translations.** The English keeps "see it" outside the brackets to mirror `lássa`, and the Slovak does the same with "neuvidí", although that one word renders clear `lássa` together with enciphered `meg`. The brackets in the translations are therefore only approximate. Say so in one phrase, or mark the clear word in the Hungarian only.
5. **minor: "sister" for testvér.** Disclosed and handled well; I would keep a note in the report that "brother/sister" is a plain turn of address here, because the card is otherwise a love letter.

## What I could not verify

- The identity of Nagy Lojzi, Róza and Árpád: no outside evidence.
- The year on the postmark, which is hidden by the stamp; 1915 rests on the written date and the scan's file name.
- The HistoCrypt article for this card: not opened by me either.
- The Hungarian judgement is my own reading; no native speaker checked it. Colloquial forms (`bizok`, `othol`, `ért utól`) look right for the period and the writer.
