REVISE

# Review 1 of hcp-1153

Reviewer: Claude Opus 5.5, 2026-11-02. Round 1. The cipher type, the key and nearly all of the plaintext stand. One word called certain (`lám`) is misread, and that misreading is the only reason a sentence looked loose. It must be fixed before FINAL.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1153/work/decode.py`: hashes OK, 348 signs, 2 flagged, assertion passes, output equals the plaintext in SOLUTION.md. The assertion only compares the transcription with a text typed from it, so it proves consistency, not correctness.
- **Own decoder.** `review/work/my_decode.py` (run from `ciphers/hcp-1153`) holds my own typed reading of all rows, taken from my crops, and its own key table. It does not use the solver's decoder. It compares my reading with `work/transcription.txt` token by token: 348 signs, 29 distinct, all covered by the key, two differences (findings 1 and 4). All other tokens agree, and every row gives the solver's letters. With the sign read as written, `ha` comes out `hi` (disclosed, finding 3).
- **Transcription against pixels.** I read every row of the address side of `work/hires/` in my own crops (`review/work/r1a` to `r6b`, `l12a`, `l12b`, `b1a` to `b2b`, `l14a`, `l14b`, 1.7x to 2.1x), and enlarged the disputed points 4x to 10x (`lam`, `lat6`, `lat10`, `ha`, `szem`, `von`, `szamal`, `ler`).
- **Disclosed points I checked and accept.** `jutsz` (dot at the foot of the 1, `b1a`); `lányka` (raised ring, `b1b`); `ráérek`; `szemébe` (hook is the serif of a 1, two dots, no cross, `szem`); `csal` (idiom `könnyet csal a szemébe` confirms it); `Értesítlek` (no e sign, `r1a`); `leér` with `3,` at the stamp (`ler`); L15 and L16 under the printed logo and line (`l14a`, `l14b`).
- **Key.** The table agrees with hcp-1174, 1178, 1179 apart from the signs below. `4.`, `5.`, `6`, `6.`, `.1` occur with the same values on hcp-1135, 1140, 1142, 1143, 1144, 1151, 1170 (not FINAL). On this card each gives clean words.
- **Language and context.** The plaintext is natural early twentieth-century Hungarian, with the verse fitting the clear words and the violets on the picture side (`review/work/pic.png`; no writing there). Recipient, route (Mezőkövesd to Szomolya, u. p. Bogács) and signature fit the family. The address and date read as stated.
- **Published solution.** None attached on the portal; none used, as far as I can tell. The solver states the HistoCrypt article was not checked.

## Findings

1. **`lám` is `lát`: the 8 has a comma (major).** L12, tokens `5, 1. 8`. SOLUTION.md item 4 says "no further sign, certain". There is a further stroke. On `review/work/lat6.png` (5x) and `lat10.png` (10x) a stroke starts just below and right of the 8's lower loop, the normal place of this writer's comma, and runs down into the top of the `6` of `könnyet` on L13. It is two strokes, not one: the upper part is steep, there is a thick join with a sideways tick, and the 6's ascender continues at a lower angle. The next 6 on the same row (`6.`) has an ascender that stops about 20 pixels of the original scan lower relative to its bowl, which is about where this 6's ascender stops without the upper piece. So the sign is `8,` = t, a collision of a comma with the row below, the same accident the solver already accepted at `vonat` (finding 2).
   The word then gives ordinary Hungarian: `mert még ha mást lát is az ember, még az is könnyet csal a szemébe`, "for even when one sees someone else [part], even that brings a tear to one's eye". `az ember` is simply the subject of `lát`. This dissolves SOLUTION.md items 4 and 5, which are explanations of a problem that the misreading made: `lám` as a short `látom`, and `az ember` "standing for" `az ember szemébe`. Height alone would not decide this, as 6 ascenders vary on the card; the join, the change of angle and the grammar together do.
   Fix: L12 token to `8,`, `lát` in `PLAIN`, the plaintext, both translations and the uncertainties. The clause no longer needs a loose-syntax note. English, for example: "for even when one sees someone else, even that brings a tear to one's eye". Slovak: "lebo aj keď človek vidí niekoho iného, aj to mu vženie slzu do oka". Disclose it as a comma touching the row below, not as a clean sign. Crop `work/crops/x5.png` shows the same stroke; it was not a matter of resolution.

2. **`vonat`: the flag rests on a wrong reason (minor).** SOLUTION.md uncertainty 2 says the comma cannot be separated from "the ascending stroke of the row below". The sign below (L05) is a 3, and a 3 has no ascender. On `review/work/von.png` the stroke starts just below and right of the 8 and ends on the top of the 3, so nothing else can account for it: it is the 8's comma. The reading `t` is right. The `?` can go, or stay with the reason corrected. The count of flagged signs changes accordingly.

3. **`ha` (accepted, no change needed).** On `review/work/ha.png` the 1 has no dot at all. Literal `hi`; `mert még ha ... is` fixes a. Correctly disclosed.

4. **`szám(t)alanszor`: the letter lost is probably the m, not the t (minor).** L14, `7. 1. 8 1. 5,`. On `review/work/szamal.png` a stroke rises right of the 8 from the `0` of `csókol` on L15, above the top of that 0's body. A 0 has no ascender, so as in finding 2 this is most simply the comma of the 8: `8,` = t, literally `szátalanszor`, that is `szá(m)talanszor`. The solver mentions this as an alternative but transcribes `8` and prints `(t)`. The pixels here are less clean than in findings 1 and 2, because the printed `nach` and the crossed 7 lie on the same spot. Either way one letter is missing and the word is certain. Prefer `8,` and `szá(m)talanszor`, or keep the current form and state both as open; the transcription and decoder should match whichever is printed.

5. **Key table omits `9,` = z (minor).** The table in SOLUTION.md has no row for `9,`, though `decode.py` has it and the card uses it 5 times (each `az`). Add it, so that the table alone decodes the card as the brief requires.

6. **`5.` = ly: conflict with FINAL cards not disclosed (minor).** SOLUTION.md says the key values fit "without change", but FINAL hcp-1178 and 1179 file `5.` as an l variant, while `5.` = ly here. Likewise `.1` was explicitly dropped from the key of hcp-1178 in its review, and `5.`, `.1`, `6`, `6.`, `4.` stand only on cards not yet FINAL. On this card `oly` twice settles ly, and `jutsz` carries `.1` alone. State this in the key note.

7. **Unrecorded stroke after the signature (minor).** A hooked stroke stands after the last 3 of `Árpád` (`review/work/l14b.png`), of the same kind as the `)` the transcription records after `imádód`. It is not in the transcription. Record it as `)`. Reading it as a comma of the 3 would give `Árpár`, which is excluded by hcp-1174.

## What I could not verify

- The postmark. On `review/work/stamp.png` it is too faint and broken for a date or year; so the year 1916 rests on the portal filename only, as the solver says.
- The distinction of `1.` and `1'`: the dot heights vary and I did not test it sign by sign. The solver's statement that accents come from the words is fair.
- The HistoCrypt article linked by the portal (not opened).
- Whether finding 4 is a comma: see the caveat there.

## Register

Once finding 1 is fixed, no clause is left unread, so the card counts as complete. MASC is the right label.
