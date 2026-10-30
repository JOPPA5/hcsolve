# hcp-1333 (pc_hcp_14) — SOLUTION (Claude Opus 5.5 as solver, 2026-10-30)

Status: complete reading of all 197 signs, with four physically obscured signs restored and disclosed below; key corrected after review 1 (see the last section), plaintext unchanged. No earlier work exists on this number. The portal attaches no solution (status Not solved) and no transcription; the transcription is mine, from the scan. No published solution was used. Extent of the search: the portal page, plus the orchestrator's check of the AI Decipherment Register on 2026-10-30. No separate web search was made for this card.

## Cipher type and key
Private Greek-looking simple substitution (register type MASC), Portuguese plaintext (the date line and the address are in clear). Word gaps and accent marks stay as in plaintext. There are 19 sign classes for 21 letters plus ç: four classes hold two letters each, and m has two forms. Sign codes are mine (`work/key.json`):

| code | glyph | letter | code | glyph | letter |
|---|---|---|---|---|---|
| U | u-shape with thin lead-in stroke | a, v | F | rho | s |
| W | w-shape, heavy first stroke, no thin lead-in | g, q | I | Lambda, two strokes meeting near the top; often a foot; height not a reliable mark | t |
| O | plain o | u | V | long stroke with small foot, often barred | l |
| X | cross | o | E | Sigma | h |
| R | hooked r-shape | e | S | large looped S | b |
| Q | head with a tick to the right, curved tail | i | s | small s | z |
| 9 | closed head, no tick, straight tail | p | Z | zeta with a tick to the right | j |
| L | tall lambda, stem or stroke running above the junction | d, r | H | theta | n |
| P | double stroke with overbar (pi) | m | T | T with overbar | c, ç |
| N | the same with a linking stroke, in "mamã", "-mente" | m | | | |

## Plaintext (Portuguese, card spelling; accents, punctuation and capitals editorial except where noted)
Atalaya, 12-6-913 (in clear)

Quinito do meu coração. Não venhas logo às cinco horas porque tenho de ir passeiar com a mamã, provavelmente para o lagar novo. Ao sol posto já devemos cá estar. Um beijo ao Luizito, saudades à Laura e Paulo e um abraço da tua Triz. Até logo amorsito.

Address (in clear): Ex.mo Sr. Joaquim Picciochi Garcia, Entroncamento.

## English
Quinito of my heart. Do not come at five o'clock later on, because I have to go for a walk with mama, probably to the new oil mill. By sunset we should be back here. A kiss to Luizito, regards to Laura and Paulo, and a hug from your Triz. See you later, little love.

## Slovensky
Quinito môjho srdca. Nechoď potom o piatej, lebo musím ísť na prechádzku s mamou, pravdepodobne k novému lisu na olej. Pri západe slnka by sme už mali byť tu. Bozk Luizitovi, pozdravy Laure a Paulovi a objatie od tvojej Triz. Do skorého videnia, láska moja.

## Command (run from the repo root)
    python3 -I ciphers/hcp-1333/work/decode.py
It checks the SHA-256 of both source scans and both hires originals, checks every token against `work/key.json`, and prints the plaintext by card line, then as running text with no accents except ç, then the sign counts. The transcription records the letter chosen for each two-letter class, so the script verifies consistency with the key but does not itself resolve U, W, L and T: that choice is mine, made from context.

## Uncertainties
1. Two-letter classes. U = a/v, W = g/q, L = d/r and T = c/ç are one shape to my eye, or nearly so: 69 of the 197 signs sit in such a class (U 38, L 19, T 7, W 5). Each use was chosen by the word it makes; T is harmless, as c and ç are one letter in the writer's system. For L, the division in sister card hcp-1332 seems to hold here too (see Response, finding 3), but not in every example, so I keep one class.
2. L and I are not cleanly separated. I is normally a Lambda with no ascender, but several I (tua, ate, amorsito) come close to L, and the r of "amorsito" is short. L against I was settled by sense in those places. The 10 I signs therefore also lean partly on sense, on top of the 69 in uncertainty 1.
3. Restorations, signs physically obscured, marked `!` in the transcription. Card line 8, first sign (U, "Ao"): blotted and overprinted by the publisher's "W."; only the heavy shape shows. Card line 14, second and third signs (X, W of "logo"): under the printed "Serie Nr. 22-12". An ink-colour separation shows the blue-grey ink but not clean shapes; a ring fits o and strokes fit W. "logo" is supported by the same word in line 2 and by the sense of "Até logo", and it is a restoration. Card line 6, first sign (9): under the printed "&": the head is hidden, the straight tail is visible; p is required by "provavelmente".
4. "Serie" also touches the first sign of line 14; V (long stroke) is visible.
5. N in "mamã" and "-mente" looks like P with a stroke linking its two stems (it reads as an H under a bar). I take it as a linked form of m; that is an explanation from shape and sense, not proof.
6. 9 in "pas-" has a mark above it; meaning unknown, possibly accidental. Marks over U in "coração" (line 1) and "mamã" fit a tilde; the mark over "à" and "já" fits an accent. The card does not mark every accent ("não").
7. In line 12 the first sign of "e Paulo" has a taller form than usual R, read as a variant. The last sign of that line (U of "abra-") is crossed by the printed rule.
8. "Triz" is read as a name, a usual short form of Beatriz; that expansion is my inference. "Luizito", "Laura", "Paulo" are unverified persons. "lagar novo" may be a place name. Line 13 has a hyphen between "ate" and "logo", two words, as the card breaks it.
9. Word gaps in my edition are editorial: the card's spacing is irregular, for example "por-/que" and "pa-/ra".

## Why this is correct
- Every sign is used and the same signs recur for the same letters; the text is continuous, idiomatic Portuguese of the period with no gaps, including the old spellings "passeiar" and the informal "amorsito".
- It emerged from independent anchors: "saudades", "às cinco horas", "tenho de ir", "ao sol posto", "provavelmente", "abraço".
- It fits the card: someone at Atalaia, apparently a young woman living with her mother, writing to Joaquim, called "Quinito", at nearby Entroncamento, and the date in June.
- Sister card hcp-1332 (same recipient, same hand and script) opens with the same "Quinito", and "hoje por cá" reads there with the same key; it ends with the same "tua Triz". I read only those parts of 1332 as a check; it is not solved here.

## Response to review 1
Verdict REVISE. All six findings addressed; no letter of the plaintext changed. Comparison sheets are in `work/resp/` (made by `work/resp/sheet.py`, 4-6x from the hires scan). `python3 -I ciphers/hcp-1333/work/decode.py` re-run after the changes: hashes OK, 197 signs, same text apart from ç now printed.

1. Fixed. The review is right. `work/resp/u.png` shows q (Quinito, que) and g (logo, lagar) with a heavy first stroke and no thin lead-in; a and v have the thin lead-in. The 2 tokens moved from U to W, key and table changed: W = g, q; U = a, v.
2. Fixed, and the split holds. I looked at all 16 Q signs (`work/resp/Q2.png`). The 10 i (Quinito twice, cinco, ir, seiar, beijo, Luizito twice, Triz, amorsito) all have a tick running off to the right and a curved tail. The 6 p (por, pas, pro, pa, posto, Paulo) have a closed head without the tick and a straighter tail; the head of "pro" is under the printed "&", so there the tail alone speaks. My earlier claim that the difference fails at "Quinito" was wrong: I had tested open against closed, the wrong feature. New sign 9 = p; Q = i. This also agrees with hcp-1332. No reading changes.
3. Fixed by disclosure. I withdraw "75 of 197"; the count is now 69 (U 38, L 19, T 7, W 5), and `decode.py` prints it. Uncertainties 1 and 2 state the L/I overlap, and the table no longer says "short slanted stroke". On d/r (`work/resp/dr.png`): in the 6 d the stem seems to run smoothly into the ascender with the left stroke as a side branch, and in most r the left stroke runs straight through with the leg as the branch, which is the hcp-1332 division. Some r (abra, Triz, Laura) are too heavy or cramped to decide, so I do not split the class. I agree with the review on the amorsito r being short, but it does overshoot the junction (`work/resp/dr.png`), so I keep it in L, not I (`work/resp/t.png`).
4. Fixed. Y and Z compared at 6x (`work/resp/jj.png`): "já" and "beijo" have the same zeta with a tick to the right. One sign; Y dropped, Z = j. Same as hcp-1332.
5. Fixed. key.json now has T = c, ç and the 2 tokens read T.ç (coração, abraço).
6. Fixed. The status paragraph now states the extent of the search. Also the review says the line 6 sign is marked `!`; it was not, and now it is, so four signs carry the mark.
