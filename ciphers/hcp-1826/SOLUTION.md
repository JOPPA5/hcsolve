# hcp-1826 (pc_hcp_507) — solution

Status: complete reading, solved by Claude Opus 5.5 on 2026-10-30. No earlier work on this number and no published solution was seen; the portal attaches none (status Not solved). The orchestrator's register check found no record of this card.

## Cipher type and key

Monoalphabetic substitution (MASC) with a hand-made numeric alphabet in English. Consonants are numbered downwards, skipping vowels; vowels and w have special signs. A circle around a sign marks a capital.

| a | b | c | d | e | f | g | h | i | j | k | l | m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (crossed Z-like sign) | 19 | 18 | 17 | 2 with raised dot | 16 | 15 | 14 | 1 with raised dot | 13 | 12 | 11 | 10 |

| n | o | p | r | s | t | u | v | w | y |
|---|---|---|---|---|---|---|---|---|---|
| 9 | 0 in left bracket | 8 | 6 | 5 | 4 | 0 in right bracket | 3 | 0 with raised dot | 0 plain |

q, x and z do not occur (the sequence would give q = 7; 7 never stands alone on the card). Capitals seen: circled 19 = B, 1 = I, X = A, 4 = T, 11 = L, 18 = C. The time 1:48 is written as a plain numeral with a colon-like double dot.

The dots after 1, 2 and 0 are part of the letter, not punctuation; they also separate them from the tens numbers.

## Reading order

The message side has two blocks. The side block runs at 90 degrees, from the divider leftwards (S01-S12). It continues in the upside-down block above it, from the card centre out to the top edge (T1-T6), ending in the signature.

## Plaintext (literal, writer's spelling)

your card received was planing on going on the train that gets to B at 1:48 wednesday but if you do not want me to come then just say so as for the other visit I do not want to go now until the last of Aug. then T. can go with me and there is anothe reason. Let me knew if you want me to come wed. or would rather I would come some other time I just as soun help you what I can any way. love Carrie.

## Normalized English

Your card received. Was planning on going on the train that gets to B[loomville?] at 1:48 Wednesday, but if you do not want me to come then just say so. As for the other visit, I do not want to go now until the last of Aug.; then T. can go with me, and there is another reason. Let me know if you want me to come Wed. or would rather I would come some other time. I [would] just as soon help you what I can anyway. Love, Carrie.

## Slovak translation

Tvoju kartu som dostala. Plánovala som ísť vlakom, ktorý prichádza do B[loomville?] v stredu o 1:48, ale ak nechceš, aby som prišla, tak to jednoducho povedz. Čo sa týka tej druhej návštevy, nechcem ísť teraz, až koncom augusta; potom môže ísť so mnou T., a je tu ešte iný dôvod. Daj mi vedieť, či chceš, aby som prišla v stredu, alebo by si radšej chcela, aby som prišla inokedy. Rada by som ti pomohla, ako len budem môcť. S láskou, Carrie.

## Command (from the repo root)

    python3 -I ciphers/hcp-1826/work/decode.py

It checks the SHA-256 of the two source scans and the two originals, then decodes work/transcription.txt with the key. Result: 300 signs, 29 distinct forms, none unkeyed. Run it from the repo root; the paths are relative to it.

## Uncertainties

- Writer's spellings kept in the literal text: "planing"; "knew" (12 9 2' 0', for know); "soun" (5 [0 0] 9, for soon: the two boxes join at the foot, but the second is closed on the right, as in "you"); "anothe reason" (only one 6 between the words; the sign is shared or an r was dropped).
- End of the card, T6: the circled 18 of Carrie is cramped at the card edge. The arc over the 8 is visible but thin, so a reader could take it for a 0 beside an 8. The word and the pencil name on the picture side support the circle reading. A small dot sits above the first stroke of this sign, apart from the dot of the 2' in "love". It may be a stray or a full stop after "love"; it does not change a letter.
- End of T5: "what" (0' 14 X 4) sits in the corner, cramped against the card edge. This is a strong reading, not a certain one: the X has a top bar and a bulge and its foot runs into the final 4. The ending has the same form as "that" in S03 (4 14 X 4). No higher scan exists. See the response to review 1.
- Bracket direction is the only o/u difference. In S09 "until" and S10 "of" the box looks closed on both sides, and the box in S12 "reason" lies on the printed imprint and is faint. Those were settled by the word.
- Faded 5 in S10 "Aug.": the body looks like 6 with the separate top bar of the writer's 5. Read as 15 = g.
- B and T. are bare initials. B may be Bloomville (the address), T. is unknown. Word divisions and all punctuation except the writer's full stops are mine.
- Identity and date: the postmark is only partly legible: "JU", a third letter that may be L or N, and "191" with the last digit lost. So the card was mailed in June or July of a year 1910-1919, which agrees with the text's "until the last of Aug." as something still ahead. The 1-cent Washington stamp fits the 1910s. The sender's name in pencil on the picture side reads best as Carrie Craig; the surname is outside the cipher and stays uncertain.

## Why this is correct

Every one of the 300 signs decodes with one fixed key and no homophones beyond the capital marking; two cramped places at the end of the card ("what" in T5, the circled C of Carrie in T6) rest on the form of the sign plus the sense or the pencil name. The result is continuous, ordinary English of a family card across 18 lines. The word list covers the whole card and nothing is skipped. The key has a visible regular structure (b = 19 down to v = 3, y = 0) found from the text, not assumed, and it predicts all the consonants on the card. "Carrie" agrees with the pencil name on the picture side, and "B" fits the recipient's town, Bloomville, N.Y.

## Credit

Transcription, analysis and decipherment: Claude Opus 5.5. No earlier work on this card.

## Response to review 1

Verdict REVISE. I rechecked each finding on the reviewer's crops and on the scan.

1. T5 last word, major: fixed. I agree. On review/work/crops/with_rot.png the dot sits at the corner of the 0, no dot follows the 1, and the fourth sign has a top bar going left and is far wider than a 1. The ending matches 14 X 4 of "that" in S03. "with" in S11 shows the normal 0' 1' 4 1 4. work/transcription.txt now has `0' 14 X 4`; the literal text, normalized English, Slovak and the uncertainty bullet are changed. Rerun: 300 signs, 29 forms, no unkeyed token, as before, since the old and new words both have 4 signs. The reading is marked as strong, not certain.
2. Wording of "Why this is correct" and T6: fixed. Both cramped places are now named there, and T6 is no longer called the only such reading.
3. Stray dot at T6: fixed. I see it on review/work/crops/sig.png and it is now disclosed. No letter changes.
4. Dating evidence: fixed. Added the third postmark letter (L or N), June or July, and the agreement with "last of Aug." On review/work/crops/pencil.png I also read Carrie Craig, so the text prefers Craig and keeps it marked uncertain.

No key change and no other sign changed. The rest of the reading stands.
