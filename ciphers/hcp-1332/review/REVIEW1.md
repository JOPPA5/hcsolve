REVISE

# Review 1 of hcp-1332 (pc_hcp_13) — Claude Opus 5.5 as reviewer, 2026-10-30

The cipher type, the key and nearly the whole reading stand. Two places on the card were misread, and in both the true signs give better sense than the solver's text: signs are missing from the transcription, so the claim "no unread sign" is false. The picture-side line says "A minha cabeça", not "Ha cabeça"; "á torre" is "a Torres". Both are concrete fixes, so this is REVISE, not REJECT.

## What I verified and how

- `python3 -I ciphers/hcp-1332/work/decipher.py`: hashes pass, "384 cipher signs decoded", "reading text equals decoded letters: yes". Output matches the claimed plaintext, but this only compares the transcription with the solver's own text. It cannot detect signs missing from the transcription.
- `review/work/decode.py` (mine, own table, no import from the solver): same text from the same transcription; with my two corrections, 389 signs. No sign falls outside the key.
- Pixels: `review/work/crop.py` on the `work/hires/` originals. All 18 main lines at 3x (`r1a`–`r6b`). Margin, rotated, 5x (`margin_c`). Picture side, rotated, 6x (`p1a`, `p1b`, `pside`). Disputed words at 5–7x (`z_torre`, `z_des`, `z_a8`, `z_pater`, `z_pode`, `z_va`, `z_bilhete`, `z_blot`, `z_onos`, `z_velho`). All in `review/work/`.
- Margin: the five vertical lines read n-a-o / t-e / m-a-n / d-o u-m / b-e-i-j-o!!, as transcribed. The sign the solver calls Π in "man-" has two stems and an overbar: m is right.
- Language: continuous Portuguese of 1912, with period spelling. Sound.
- Sister card hcp-1333 (same addressee, still in review, grep only): it has no "Torres", "bonito" or "minha". Its solver also has one sign standing for a and v, which agrees with uncertainty 7 here; that is not independent proof.
- Published solutions: none on the portal capture; none cited. I ran no separate web search.

## Findings

1. **major — Picture-side line: four signs are missing, and "Ha" is wrong.** `P1` is transcribed `SM TMDBTM`. The line on the card (`review/work/p1b.png`, `p1a.png`) reads μ Π ϙ θ Σ μ, then T μ δ β T μ. That is `M PQHSM TMDBTM`, "a minha cabeca". The four signs M P Q H are plainly there at the left end of the line, faint but legible, and the solver seems to have started reading at the Σ. The line says **"A minha cabeça está melhor"** (my head is better). This removes the "Ha" oddity in uncertainty 2, which treated a transcription gap as a writer's slip. It also makes "All 384 signs… no leftovers and no unread sign" false. The first sign is the weakest of the four, but with "minha" following, "a" is secure. Fix: `work/transcription.txt`, READING, plaintext, English and Slovak; delete uncertainty 2; correct the count.

2. **major — A7: a sign is missing; "torres", not "torre".** `A7` is transcribed `M AXRRB,`. After the β there is a further sign with a closed triangular head, before the comma (`review/work/z_torre.png`). It is the ρ of s, the same form as in "esse". The word is `AXRRBC`, "torres". The sign before it, M, has no accent, while this writer does mark á ("foi á", line A4), so the solver's "á torre" adds an accent that is not on the card. The natural reading is **"Vamos hoje a Torres"**, a place name, not "to the tower". From general knowledge, not checked here: Torres Novas lies close to Atalaia in Santarém district, which would suit the card's "Atalaya"; Torres Vedras is possible too. Whichever it is, the fix to the text stands. Fix: transcription, READING, plaintext, both translations, and a note on the place.

3. **minor — A8: "despara" is better divided "des para".** The third sign has a tall stem running past the junction, the same form as d in "pode" (`z_des.png`, `z_pode.png`), so d is firm and uncertainty 4's "L or A is not fully sure" can go. Word gaps on this card are irregular, and there is a visible gap between ρ and 9. "des para" gives real words with no change to any sign: "Que dês para lá alguma coisa?" (that you give/send something there?). This is my suggestion, not proved, but it is better than a non-word plus a translation "Will something go off over there?" that nothing supports. Solver: adopt it or justify "despara".

4. **minor — Translation of "já hontem".** "já" is "already", not "only": "Laura already went to the quinta yesterday". English and Slovak ("len včera") should change. "Telha" and "a paternidade" are properly flagged as interpretive.

5. **minor — "v" (sign W) is an assignment by sense, not a separate sign.** At 5–7x "va-" and "velho" use the same two-hump sign as a (`z_va.png`, `z_velho.png`). Uncertainty 7 discloses this, but the table still lists W as a sign and the "Why this is correct" section calls the table one-to-one with "two merged letter pairs". There are three merged pairs: q/g, c/ç, a/v. The same applies to the `assert` in `decipher.py`, which holds only because W is a separate label. Better to transcribe M and let the decoder choose, or say plainly that W is chosen by context.

6. **minor — The check in `decipher.py` is weak.** "reading text equals decoded letters" is circular with respect to the scan. `SOLUTION.md` should not offer it as evidence of coverage.

## Checked and upheld

The rest of the sign-by-sign reading held on the crops, including "por-/quê", "porque a Laura", "foi á quinta", "pode ir ao bonito" (r firm, sense still open and disclosed), "sobrinhito", "chic o teu bilhete", "Adeus amorsito até Sabbado", "tua Triz". "paternidade": the d signs are short there and sense chose them, as uncertainty 5 says. A17 blotted sign: a closed head under a blot, a correction or double stroke; s is reasonable and disclosed. Pet name Quinito for Joaquim fits the address. The clear text matches the card.

## Could not verify

- The sense of "ir ao bonito", "uma grande telha" and "a paternidade", and who Laura, Luizito and Triz are.
- Which Torres is meant, and which Atalaia the card came from; I did not read the postmark.
- Whether "O sonho continua... Dela..." on the picture is a later addition.
- The faint first sign of the P1 line on its pixels alone.

## Register

Once findings 1 and 2 are fixed the solution is fit for a register entry; re-review is not needed unless the solver changes more than these points.
