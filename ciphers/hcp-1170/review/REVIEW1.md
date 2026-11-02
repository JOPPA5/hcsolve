REVISE

# Review 1, hcp-1170 (reviewer: Claude Opus 5.5, 2026-11-02)

The decipherment stands. The cipher passage is correct sign for sign and the card reads in full. Two open-text words need correcting or relabelling, and two small statements need fixing. None of this changes the sense of the card.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1170/work/decode.py` passes all four SHA-256 checks and prints 81 signs, 25 distinct, with its internal assertion satisfied. The bracketed cipher text in SOLUTION.md matches the raw decode.
- **Independent decode.** `review/work/verify.py` holds six rows keyed from my own enlargements (`review/work/r1a` to `r6b`, 3x), not copied from `work/transcription.txt`. It gives the same letters: drága margitkám / üdvözöllek és / téged és mindnyá- / -tokat mi ujság van / ot és hogy vagytok rosz / üdö van e ot. 81 signs, 25 distinct. The only difference is the name I give the sign the solver writes `-1` (finding 3).
- **Transcription against pixels.** All 81 signs were read one by one on the enlargements, with no disagreement. I checked in particular:
  - every `1'` shows one high dot (drága, Margitkám, mindnyá-, újság);
  - the plain 5 in `hogy` against `5,` in `üdvözöllek`;
  - `6,` in `van` and in the first `n` of `mindnyá-` against bare 6 in `-ja-` and `-jság`;
  - `6.`: the heavy, retraced 6 with a short dash low at its right, as the solver describes;
  - the brown speck under the 3 of `üdő`: brown, unlike the violet-blue ink, so correctly not read as a dot.
- **Key coverage.** Every sign decodes. No sign is unassigned. Long and short vowels fall together as on the sisters, except a/á and e/é.
- **Sister claims.**
  - `csókollak téged` on hcp-1178, `üdvözöllek` on hcp-1174, `legszeb` on hcp-1179 and `diferál` on hcp-1174 all confirmed.
  - The hcp-1175 statement `4.` = l is in its NOTES.md; that card has no SOLUTION.md.
  - The new values `6`, `6.`, `4.` also appear on unfinished sister cards (hcp-1144, 1147, 1141), and `üdő` and `rosz` recur on hcp-1142 and 1160. These cards are not FINAL, so they are support only. The solver's values were not contradicted.
- **Open text.** All 14 open lines were read on red-channel strips with stretched contrast (`review/work/L07` to `L20`, `strip.py`), and the date line, address and postmark on colour crops. Everything agrees with the solver's reading except finding 1 and finding 2.
- **`írd`.** The solver's doubt (note 6) can be narrowed. The same detached bowl-plus-stem d stands in `anyukád`, `Kövesdre` and `Mezőkövesd` on this card (`L08`, `zdate`), which also read `ol` at first sight. `írd` is simply this writer's d, and the strict `írol` is not a real alternative.
- **Language and context.** Period Hungarian with this correspondence's spellings. Mezőkövesd to Szomolya, December 1915, date and postmark year agree. English and Slovak translations checked against the Hungarian and are faithful.
- **Honesty.** No published solution used, and the unread HistoCrypt article is disclosed. Uncertainties are disclosed apart from findings 1 and 2.
- **Picture side.** Printed portrait, no writing, one short blue stroke and a brown stain. Nothing hidden there.

## Findings

1. **major: `le jön` is an emendation; the letters say `jöm`.** `review/work/zjon2.png` shows three downstrokes after the ö, then an exit stroke. The `jön` of line 7 (`zjon1.png`) has two downstrokes and an exit stroke, and the final m of `mondom` (`zmondom.png`) has three. So this word is written like an m. The solver's "the hump count is not perfect" understates this. I still agree with `jön` on sense: the writer is in Kövesd, so he cannot "come down" there, and the mother is the subject of the sentence before. **Fix:** state in Uncertainties that the pixels give `jöm` and that `jön` rests on word sense alone, and mark it in the plaintext (for example `jön [card: jöm]`). Carry that into the report. The translation depends on this choice.

2. **minor: `Semmi` is written `Semi`.** `review/work/zsem.png` shows S, e, three downstrokes, then i with its dot: one m. `Semmi` would need six downstrokes. This fits the writer's single consonants (`rosz`, `ot`), and SOLUTION.md says the spellings are the writer's, so the plaintext should print `Semi` and list it with the other spellings. Also add it to the open text in `work/decode.py`.

3. **minor: `-1` is labelled too narrowly and as a separate sign.** The card has a thick lobe left of the stem (`z4u.png`). Sister cards have a dot left of the 1, `.1` = u, ú (hcp-1137, 1143, 1147; hcp-1140 already notes the parallel). The cipher does not otherwise mark vowel length on i, o, ö, ü. So the sign is most simply u/ú, and the only reason to write ú is standard spelling of `újság`. **Fix:** give the value as u, ú, and say it is probably the same sign as `.1`. Whether the accent is written in the open `ujság` near the end of the card is unclear, so that spelling should not be used as evidence.

4. **minor: the postmark is clearer than stated.** `review/work/zpm.png` shows 13 plainly; the 3 stands on the stamp and is legible. Uncertainty 10 says it "may not be a 3". State the conflict as it is: postmark DEC 13, written date XII/14. The written 14 is also clear, so the cause is unknown (a misdated card or an unchanged postmark date). The portal's file-name date simply repeats the written date and is not independent evidence.

## What I could not verify

- The HistoCrypt article linked from the portal was not consulted.
- The sender's identity. The card is unsigned, and the link to the Árpád of hcp-1174 rests on hand and context only.
- Whether `maradtam` is complete as a closing. The word reads, cramped under a strike-out, and nothing follows it. I accept it as a lone word.
- `mindnyá-jatokat`, first letter of the second line: too heavily overwritten to confirm the j from the pixels. It is fixed by the fragment and the cipher passage, as the solver says.

## Register

The whole card reads, so after the fixes it qualifies as complete. No clause is unread. The MASC label is correct.
