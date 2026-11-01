REVISE

# hcp-1174 review, round 1 (reviewer: Claude Opus 5.5, 2026-11-01)

The cipher reading stands. Every enciphered word is correct, and I could not refute the key. Concrete fixes are needed in how the open (struck-through) text is presented: the line `vági által` is printed as if read, and the two pixel-level points below should be shown as written. The solution stays complete only if the fix in finding 1 shows that the problem is confined to one phrase. No new key is needed.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1174/work/decode.py`: hashes OK, 89 signs, full text printed. The output matches SOLUTION.md except for the points in finding 3. All the open text is hard-coded in the script, and the assertions compare the transcription with the solver's own readings, so this shows self-consistency only.
- Independent decode: `review/work/mydecode.py`, with my own sign-by-sign transcription from 2x to 5x crops of the hires address side (`review/work/r_*.png`, `z_*.png`, `y_*.png`) and no ODD table. I get 89 signs and 23 distinct signs, the same counts as the solver. Literal output:
  `édesmargitkám / ölelhetlekén / sziveméled / szeretem / szimtalanszorüdvpzpllek / csokollak / keretökedvesed / árpád`
  So 84 of the 89 signs decode by the table alone. The other five are the disclosed ones: `sz[i→á]mtalanszor`, `üdv[p→ö]z[p→ö]llek`, `[k→sz]erető`. The fifth is the blotted r of `szerető`, which I also transcribe as `3,` and which decodes only on that reading.
- Sign checks by eye, each on crops:
  - Salutation: the `1'` high dot of `Margitkám` is clear. The stroke after the final 8 looks like a comma (`8,` would give -kát), but `y_acc.png` shows it sits over the `é` of `ígérete-` on the line below, so I take it as that accent. `-kám` stands.
  - `Ha ...`: all commas are present.
  - `szívem éled`: the comma under the 5 is there (the 1179 notes quote this sign without it).
  - `szeretem` (`y_mondd4.png`): `1: 8, 1: 8` is clear.
  - `5, 5,` in `csókollak` (`y_ll.png`): both are commas. The second is faint, and it is not a dot.
  - `:1` for ü: two dots to the left are clear.
  - `Árpád` (`y_end.png`): `1' 3, 9 1' 3` is clear, including the closing bracket.
- The four disclosed odd signs are as described. Sense makes all of them safe:
  - The `9` in Árpád stays p; no other reading fits.
  - In `üdvözöllek` the sequence is `9 9, 9̇`. The middle sign has a separate comma (z). The outer two are 9-shaped with a joined tail and the third has a dot above, as stated. Comma tails joined to the body also occur at `8,` in `számtalanszor`, which supports the "joined `0,`" explanation.
  - The first sign of `szerető` differs from the plain `7` of `kedvesed` (an extra foot or lobe at lower right, no free dot). That fits a dot absorbed into the sign. The sense call is honest.
- Key structure: the signs group sensibly by digit (a base digit plus a mark). There are no contradictions across positions, and the table is compatible with `work/key.json` on hcp-1179 (`5`/`5,` differ only because that card's table merges them as l).
- Open text, read from red-channel crops with the brown ink suppressed (`q_*.png`, `p_*.png`). I confirm `Bocsáss meg, hogy ígéretemet nem teljesítettem, vagyis nem mehettem fel, de semmi tekintetben sem tehettem`, the `jövő ... felmegyek, az idő nem` sequence, `és majd pótolni fogom a multat is`, `Halkan keblemet`, `Messzi csendülj röpke kis dal`, `felett`, `Hol virág terem`, `látszik`.
- Date and address: heading `Mezőkövesd, 916. II/15`; postmark FEB 15 with a damaged year that fits 916. The address reads as claimed. Signature `Árpád` is also compatible with the open `Árpád` read on hcp-1177 (same Mezőkövesd/Szomolya circle) and with `Sz. A.` on 1175, 1176 and 1179.
- Language: real Hungarian of the period, with a Latinate `differál` and `multat`. A suitor's message on an open card fits.
- No sign of a published solution used.

## Findings

1. **major: `vági által` is printed as a reading in the main plaintext, but it is neither supported by the pixels nor Hungarian.** On `review/work/p_lagy2.png` the second word begins with a round o-like letter and reads `oltal` / `oltál`, not an evident `által`. `vági` is not a word, and `által` cannot govern the accusative `keblemet`, so the line as printed has no verb. The disclosure under Uncertainties is honest, and the translation already brackets the phrase, but the plaintext block (and the script output) shows it as settled text. Fix: print the letters as seen with a marker, e.g. `Lágy tavaszdal [vagi oltal ?] / Halkan keblemet`, and state that the verb of this sentence is unread. I propose no reading of my own. This is plain text, not cipher, and it is one phrase, so it does not make the card partial as long as it is labelled. If the solver cannot narrow it, say that the two words are unresolved and do not call any part of them certain.
2. **minor: write `differál` as it stands.** On `q_l2.png` I see a single f (`diferál`/`difevál`). The plaintext should give the spelling on the card, with the normalised form in a note. The same applies to `tavaszdal`, where the crops show the disclosed `tavaszo-`-like form: keep the note.
3. **minor: command output differs from SOLUTION.md.** The script prints `[csókollak szerető kedvesed Árpád]` with no parentheses, while the SOLUTION has `[csókollak] ([szerető kedvesed]) [Árpád]`. The card has both brackets (`y_end.png`). It also omits the address given in the plaintext section. Align them.
4. **minor: "Every one of the 89 cipher letters gives Hungarian, using one fixed key" and "Twenty-three signs give all 89" overclaim.** The fixed key gives `szimtalanszor`, `üdvpzpllek`, `kerető` literally. State that 84 signs decode by the table and 5 are read by sense. The Uncertainties section already has the facts, and the claim under "Why I believe it is correct" should match.
5. **minor: wrong detail on the sister-card evidence.** SOLUTION quotes hcp-1178 as `... 5, 5, 1. 7 ...`, but that card's own transcription and its review have `5, 5.` there (this card has `5, 5,`). The signature on sisters is `Sz. A.`, not `Sz. Á.`, and the accent is not attested. Correct both, and add the open `Árpád` of hcp-1177 as the stronger corroboration.
6. **minor: `II.` marks.** The card has an unpunctuated `II` before `Ha` and a second `II` at `Csengj`. Only the first is in the plaintext, with a full stop that is not on the card. Show both, or say why not. Their meaning is unexplained, so say so.
7. **minor: published-solution statement.** "No published solution seen" sits beside "the HistoCrypt article ... was not consulted". State plainly in SOURCES.md and in the report that the portal's linked article was not checked for this card.

## What I could not verify

- The exact words under the densest strike-outs. `mehettem`, `A jövő` (the first sign looks like a 6), the end of `vasárnapi`, `tér`, and `házig` (pixels also allow `hóvig`) match the solver's disclosed doubts. I read them no better.
- The Hungarian printed source of the poem, if one exists; it could settle finding 1. I did not search for it.
- The HistoCrypt article linked from the portal; I did not read it either.
- The middle digit of the postmark year: the damaged sign fits 6 but is not clear.

## Register

The card is eligible after the findings are addressed, with type MASC, provided finding 1 is marked as a single unresolved open-text phrase.
