REVISE

# hcp-1178 review, round 1 (reviewer: Claude Opus 5.5, 2026-11-01)

The solution gets the 13-sign transcription, the cipher type and 12 of the 13 values right. One letter of the plaintext is wrong: the line reads **csókollak téged** ("I kiss you"), not `csókoljak téged`. Open-text errors also need fixing. No new key is needed.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1178/work/decode.py` from the repo root. Hashes OK; output `csokoljaktéged`, matching the claim. The script asserts that string and hardcodes the sister controls, so it shows self-consistency only.
- Read the 13 signs on my own 5x crops of the hires scan (`review/work/d1.png`, `d2.png`, `d3.png`, 8x `mark.png`). I get the same sequence: `2, 0 7 0 5, 5. 1. 7 8, 2. 4, 1: 3`. The marks are clear: the first 5 has a true comma with tail, the second a round dot.
- Independent decode (`review/work/mydecode.py`), using values only from hcp-1174's sign table. That table has no `5.`. Output: `csokol[5.]aktéged`. With l: `csokollaktéged`; with j: `csokoljaktéged`.
- Key coverage: all 13 signs map. There is no enciphered text elsewhere on the card; the picture side carries no writing.
- Sister passages checked on pixels: hcp-1174 foot (`review/work/c74.png`, `foot74b.png`, `llek74.png`), hcp-1179 bottom rows (`r79a.png`, `r79b.png`).
- Open text sampled against crops: `ang`, `anyu`, `fuj`, `fuj2`, `vers`, `top1`, `top2`, `note1`, `note2`, `sigz`, `addr2`, plus the `_b` blue-channel versions in `review/work/`.
- No published solution seems to have been used; portal capture shows none attached.

## Findings

1. **major: `5.` = j is wrong; `5.` is l. The plaintext is `csókollak téged`.**
   - hcp-1179 bottom row has `1. 5. 1: 4, 7. 1: 1,` = `a legszeb(b)`. The dot after the 5 is clear (`r79b.png`), in undamaged writing and a secure word. `ajegszeb` is nonsense. SOLUTION uncertainty 2 calls this a "damaged passage ... that does not settle it"; the blot on that card is elsewhere, and this does settle it. The hcp-1179 solver already lists `5.` as l.
   - The writer does double consonants, against the argument from `akor`: this same card spells `Üdvözöllek` in clear, and hcp-1174 enciphers `5, 5, 1: 7` (-llek) and `5, 5, 1. 7` (-llak).
   - `csókollak` is the expected formula, as on hcp-1174. A bare subjunctive `csókoljak téged` would be odd without `hadd` or `hogy`.
   - Fix the key table, `decode.py` (including its assertion), plaintext, English and Slovak: "I kiss you", „bozkávam ťa“. Note that `5.` and `5,` are variants of l, and that `5.` is not attested as j anywhere in this family.

2. **major: the claim that hcp-1174 has `5.` in the same word is false.** SOLUTION uncertainty 2 and the `1174 foot` control in `decode.py` give `2, 0 7 0 5, 5. 1. 7`. On the scan the second 5 of hcp-1174 has a small faint hooked comma before the `1.` (`c74.png`); the hcp-1174 solver also reads `5, 5,`. The control was shaped to agree with the wrong reading. Correct it.

3. **major: verse line 6 is probably misread.** `Hol a fájó fuvalmas szél` does not fit the pixels. Under the strokes the last part shows several descenders close together and reads best as `fujja a szél` (`fuj2.png`), which `fuvalmas` with its single descender cannot give. The word before it is less sure: it may end in -t (`fákat`, `fáját`?). A line such as `Hol a fákat fújja a szél` ("where the wind blows the trees") would keep the eight syllables and the rhyme levél/szél, but that exact word is my suggestion, not a reading. `fájó` is not flagged as uncertain at all. Re-read the line and fix the translations.

4. **minor: `ver[s]cskét` is wrong.** The word is split across lines 5 and 6. The second part is plainly `secskét` (`vers.png`), so the card has `ver-secskét` = `versecskét`. No letter is missing and no bracket is needed.

5. **minor: `Angyukádal` is unexplained.** The translations treat "Angyuka" as a name without comment. Under the strokes the word could be `Anyukádal` (= anyukáddal, "with your mother"); `Angyuka` could also be a kin term from `ángy`. I could not separate g+y from y alone: a descender from the line above interferes (`anyu.png`). Disclose both readings. The note "single l assumed" is also confused: the point is single d for -dd-.

6. **minor: signature.** `Sz. K.` is given as fact, but the capital can also be read A (`sigz.png`). hcp-1179 discusses the same ambiguity, and hcp-1174 is signed Árpád, which favours `Sz. A.`. Disclose it and compare.

7. **minor: top margin line.** It can be pushed further than the solver did, though not closed. The blue channel suggests `Vasárnap k?m?g?ek egy ... vonatnál`, possibly `kimegyek` ("I go out"); the word after `egy` remains unread (`top1.png`, `top2.png`). This is open text outside the cipher, so it does not make the decipherment partial. The solver's disclosure of the gap is honest.

8. **minor: support is overstated.** "Eleven of the 13 values come from other cards ... unforced" sits beside a key outlined partly from this same card (`téged` on 1178 used in deriving values), and `.1` = u on hcp-1175 conflicts with that directory's own transcription (`3 1. 5,`, which also notes a possible `3.` + `1`). The latter does not touch this card, but it should not be cited as a clean control.

## Could not verify

- The second word of verse line 6 and the middle of the top margin, under the brown strokes.
- Postmark date; the stamps are illegible beyond fragments.
- The whole of hcp-1175 and the key derivation order on the sister cards, none of which are FINAL or reviewed.

## Register

Type MASC is right. After findings 1 to 4 are fixed, the enciphered line is fully read and an entry would be justified.
