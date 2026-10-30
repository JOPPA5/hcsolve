# hcp-1332 (pc_hcp_13) — solution, Claude Opus 5.5, 2026-10-30

Status: complete reading, small residual points listed below; corrected after review 1 (see the last section). No published solution was found or used; the portal attaches none and the orchestrator's register check of 2026-10-30 lists none. No web search for this card beyond that. No earlier work exists on this number.

## Cipher and key

Portuguese lovers' postcard (Atalaya to Coimbra, 12-12-1912) in a simple monoalphabetic substitution with an invented, Greek-looking cursive alphabet. Word gaps, punctuation and accent marks stay as in plaintext. Cipher type for the register: MASC. Portal language "Unknown" should read Portuguese.

| plain | sign | id | plain | sign | id |
|---|---|---|---|---|---|
| a, v | μ-like, two humps | M | m | Π with bar | P |
| b | big looped δ | D | n | θ | H |
| c, ç | T with bar | T | o | × | X |
| d | λ, right stem runs up past the junction | L | p | 9 with straight tail | 9 |
| e | β, often open, Γ/n-like | B | q, g | ω-like, heavy first stroke | U |
| f | α | F | r | λ/k, left stroke runs through, leg from the middle | R |
| h | Σ | S | s | ρ, closed head | C |
| i | ϙ, curved tail | Q | t | short Λ, no ascender | A |
| j | ζ | Z | u | o | O |
| l | ν | V | z | small ς | 5 |

k, w, x, y do not occur. Sign transcription: `work/transcription.txt` (389 signs: 18 main lines, a vertical margin text, two lines on the picture side).

## Command (from the repo root)

    python3 -I ciphers/hcp-1332/work/decipher.py

It checks the SHA-256 of the four images, decodes the transcription line by line, and checks that the reading text has exactly the decoded letters. That last check only guards against typing slips between the two texts; it says nothing about the agreement of the transcription with the scan.

## Plaintext (original spelling; punctuation and a few accents the writer left out, such as até, sós, dês, lightly normalised)

Meu Quinito. Há hoje por cá uma grande telha. E sabes porquê? Porque a Laura já hontem foi á quinta, e para a semana já pode ir ao bonito.! Esta noite só sonhei com o Luizito. Vamos hoje a Torres, e com a paternidade. Que dês para lá alguma coisa? O nosso sobrinhito quando for mais velho ha de ser como esse menino. E muito chic o teu bilhete. Qualquer dia lá iremos. Adeus amorsito até Sabbado!! Abraça-te com todo o amor a sós, sempre só tua Triz. E hoje não te mando um beijo!!

Picture side, top left: A minha cabeça está melhor.

Not enciphered: "Atalaya, 12-12-912", the address (Ill.mo Ex.mo Sr. Dr. Joaquim Picciochi Garcia, R. da Ilha n.º 8, Coimbra), and on the picture "O sonho continua... Dela..." in block letters, which may be a later owner's addition.

## English

My Quinito. There is a great fuss/mood around here today. And do you know why? Because Laura already went to the quinta (farm) yesterday, and next week she can already go to the pretty one(?). Last night I dreamed only of Luizito. We are going to Torres today, with the parents. That you should give something over there? Our little nephew, when he is older, will be like that boy. Your note is very chic. One of these days we will go there. Goodbye, little love, until Saturday!! She embraces you with all her love, in private, always yours alone, Triz. And today I am not sending you a kiss!!
Picture side: My head is better.

## Slovensky

Môj Quinito. Dnes je tu veľká nálada/rozruch. A vieš prečo? Lebo Laura bola už včera na quinte (statku) a budúci týždeň už môže ísť k peknému(?). Dnes v noci sa mi snívalo len o Luizitovi. Dnes ideme do Torres, s rodičmi. Že by si tam niečo dal? Náš synovček, keď bude starší, bude ako ten chlapec. Veľmi šik je tvoj lístok. Niektorý deň tam pôjdeme. Zbohom, láska moja, do soboty!! Objíma ťa so všetkou láskou, v súkromí, navždy len tvoja Triz. A dnes ti nepošlem bozk!!
Strana s obrázkom: Moja hlava je na tom lepšie.

## Uncertainties

1. "Abraça-te" could mean "she embraces you" or be meant as "I embrace you"; the letters are firm, the English and Slovak follow the literal third person.
2. "A minha cabeça" (picture side): the first sign of the line is faint; with "minha" following, "a" is secure. "Torres" is read as a place name; which Torres (Torres Novas lies near Atalaia in Santarém district, Torres Vedras is possible; general knowledge, not checked) and which Atalaia are open.
3. "ir ao bonito": letters firm, sense unclear (a place, a person or an idiom). The sign in "ir" was checked at high zoom against other r and d signs and is r.
4. "dês para": the signs are firm (d by its stem, as in "pode"); the word division is a reading, helped by a visible gap between ρ and 9 on the card, and the accent on "dês" is not written. The translation of the sentence is a guess. "telha" and "a paternidade" are read as slang/humour: "uma grande telha" (a whim, a mood), "a paternidade" (the parents); those translations are interpretive.
5. d (L) and t (A) and r (R) are close look-alikes and were separated by shape; in a few cramped places (pode, paternidade) the shape is not decisive and sense chose.
6. "mando": the first sign in the margin has a thick, converging stem, read as Π (m); as T the word would be "cando/canto", which makes poor sense. The word has a hyphen, written man-do across a margin line.
7. v is not a separate sign: in "vamos" and "velho" the sign is the same two-hump M as a. v is assigned by context ("amos", "aelho" are not words); the decoder does this by a rule, as it does for q/g.
8. U stands for both q and g. T stands for c and ç. With a/v that makes three merged pairs.
9. Line A17, last sign is blotted; read as s ("a sós"), a closed ρ head under the blot.
10. "Triz" may be short for Beatriz; that is a guess. Quinito is a usual pet form of Joaquim, matching the addressee.

## Why this is correct

- All 389 signs on my corrected transcription decode by one table of 21 signs (three merged letter pairs, as disclosed); the reviewer read all lines at 3–7x and, after the corrections below, found no further unread sign.
- The text is continuous Portuguese of the period with old spellings (hontem, Sabbado), and runs across hyphenated line ends: por-/quê, noi-/te, va-/mos, nos-/so, mui-/to, até-/Sabbado.
- Accent marks fall where Portuguese has them: quê, já, cá, lá, só, não, está.
- The first words give the addressee's own pet name, which was not used to set the key: Quinito for Joaquim Picciochi Garcia.
- The sister card hcp-1333 (same addressee) opens with a word of the same pattern as "Quinito"; that was only glanced at, not decoded.

## Response to review 1

All six findings accepted; I rechecked each on the reviewer's crops (`review/work/`). The reproduction command was re-run after the changes: 389 signs, all in the key, reading text equal.

1. **Fixed.** On `p1b.png` the line clearly begins with the four signs μ Π ϙ θ before Σ μ. `P1` is now `M PQHSM TMDBTM`, "A minha cabeça". The old claim "no unread sign" was false, and the uncertainty about "Ha" is gone (uncertainty 2 replaced).
2. **Fixed.** `z_torre.png` shows the closed ρ after the β. `A7` is now `AXRRBC`, "a Torres"; no accent is on the M, so none is printed. Place-name note added to uncertainty 2.
3. **Adopted.** `A8` is now `LBC 9MRM`, "dês para"; d is firm on `z_des.png`. No sign changed; the sentence meaning stays a guess, and the unwritten accent is disclosed (the writer also omits it in até and sós).
4. **Fixed.** "já hontem" is now "already yesterday" / "už včera".
5. **Fixed.** `z_va.png` confirms the same sign for a and v. W removed: transcription now has M in both places, the key table shows a, v under M, `decipher.py` picks v by a context rule, and "Why this is correct" names three merged pairs.
6. **Fixed.** The check is relabelled as an integrity check in `decipher.py` output and above; it is no longer offered as evidence of coverage.

The "chic" item under "old spellings" was also dropped: it is a loan word, not an old spelling. No reading other than the points above changed.
