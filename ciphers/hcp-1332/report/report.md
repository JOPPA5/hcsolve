# HCP 1332 (pc_hcp_13): a Portuguese lovers' postcard in an invented Greek-looking alphabet, 1912

Human solver: Tomáš Pavuk

**Status: deciphered in full (389 of 389 cipher signs); independent review 1 verdict REVISE, all findings addressed.** A few phrases are read with certainty as letters but stay uncertain in sense. Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1332 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1332), portal name pc_hcp_13, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1912-12-12, language Unknown, location Europe, sender Unknown, recipient Joaquin Picciochi Garcia, with no transcription or solution attached. This work shows the language is Portuguese. No published solution was found or used; there was no web search for this card beyond the register check.

The picture side is a tinted photographic postcard of a curly-haired girl and a boy in a sailor suit, with two chicks and pussy willow, numbered 2244. Two cipher lines stand at its top left, turned sideways. The block-letter words "O sonho continua... Dela..." on the picture are in plain writing and may be a later owner's addition.

The address side has a plain heading "Atalaya, 12-12-912", a Portuguese 10-réis stamp overprinted REPUBLICA, and the plain address: Ill.mo Ex.mo Sr. Dr. Joaquim Picciochi Garcia, R. da Ilha n.º 8, Coimbra. Eighteen cipher lines fill the left half, and a short text continues vertically in the top margin, to the right of them.

![Picture side, with the two cipher lines at the top left (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side, with the main cipher text, the vertical margin text and the plain address (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is manual, made from enlarged crops (4–7×) of the un-converted originals; no OCR was used. Each sign was given a Latin capital or digit as a label. The key was found from the text itself, as no sister card had one:

- The doubled sign in the word of the pattern S-a-b-b-a-d-o, followed by "!!", gave a, b, d, o.
- Short recurring words gave de and do, which split the look-alike signs for d and t.
- "quê", "por", "hoje" and "sempre" then gave most of the remaining alphabet, and the Portuguese text ran on from there.

Word gaps, punctuation and accent marks stand in plain form on the card; they helped a good deal. The opening word turned out to be Quinito, the usual pet form of Joaquim, the addressee. His name played no part in setting the key.

The script `work/decipher.py` checks the hashes of the images, decodes the transcription by the key and compares the result with the reading text. That comparison catches typing slips only. It says nothing about whether the transcription matches the card; that rests on reading the scan, done by solver and reviewer separately.

## Key

Monoalphabetic substitution with invented, Greek-looking cursive signs. Labels are conventional.

| Plain | Sign | Label | Plain | Sign | Label |
|---|---|---|---|---|---|
| a, v | μ-like, two humps | M | m | Π with bar | P |
| b | big looped δ | D | n | θ | H |
| c, ç | T with bar | T | o | × | X |
| d | λ, right stem runs up past the junction | L | p | 9 with straight tail | 9 |
| e | β, often open | B | q, g | ω-like | U |
| f | α | F | r | λ/k, left stroke runs through | R |
| h | Σ | S | s | ρ, closed head | C |
| i | ϙ, curved tail | Q | t | short Λ, no ascender | A |
| j | ζ | Z | u | o | O |
| l | ν | V | z | small ς | 5 |

Three signs each cover two letters: a/v, q/g and c/ç. The letters k, w, x and y do not occur.

## Plaintext

Transcription as read from the card, line by line (^ = accent mark over the preceding sign, ~ = tilde):

```text
A1 PBO UOQHQAX. SM SXZB 9XR TM^
A2 OPM URMHLB ABVSM. BCMDB C9XR-
A3 UOB^? 9XR UOB MVMORM ZM^ SXHABP
A4 FXQM^ UOQHAM, B9MRM MCBPMHM
A5 ZM^ 9XLB QRMX DXHQAX.! BCAMHXQ-
A6 AB CX^ CXHSBQ TXP XVOQ5QAX. MM-
A7 PXC SXZB M AXRRBC, BTXPM
A8 9MABRHQLMLB. UOB LBC 9MRM
A9 VM^ MVUOPM TXQCM? XHXC-
A10 CX CXDRQHSQAX UOMHLX FXR
A11 PMQC MBVSX SM LB CBR
A12 TXPX BCCB PBHQHX. BPOQ-
A13 AX TSQT X ABO DQVSBAB
A14 UOMVUOBR LQM VM^ QRBPXC.
A15 MLBOC MPXRCQAX MAB-
A16 CMDDMLX!! MDRMTM-AB
A17 TXP AXLX X MPXR MCXC
A18 CBP9RB CX^ AOM ARQ5. BSXZB
M  HM~X AB PMH-LX OP DBQZX!!
P1 M PQHSM TMDBTM
P2 BCAM^ PBVSXR.
```

Portuguese text (original spelling; punctuation and a few unwritten accents lightly normalised):

> Meu Quinito. Há hoje por cá uma grande telha. E sabes porquê? Porque a Laura já hontem foi á quinta, e para a semana já pode ir ao bonito.! Esta noite só sonhei com o Luizito. Vamos hoje a Torres, e com a paternidade. Que dês para lá alguma coisa? O nosso sobrinhito quando for mais velho ha de ser como esse menino. E muito chic o teu bilhete. Qualquer dia lá iremos. Adeus amorsito até Sabbado!! Abraça-te com todo o amor a sós, sempre só tua Triz. E hoje não te mando um beijo!!
>
> Picture side: A minha cabeça está melhor.

English:

> My Quinito. There is a great fuss/mood around here today. And do you know why? Because Laura already went to the quinta (farm) yesterday, and next week she can already go to the pretty one(?). Last night I dreamed only of Luizito. We are going to Torres today, with the parents. That you should give something over there? Our little nephew, when he is older, will be like that boy. Your note is very chic. One of these days we will go there. Goodbye, little love, until Saturday!! She embraces you with all her love, in private, always yours alone, Triz. And today I am not sending you a kiss!!
>
> Picture side: My head is better.

Slovak:

> Môj Quinito. Dnes je tu veľká nálada/rozruch. A vieš prečo? Lebo Laura bola už včera na quinte (statku) a budúci týždeň už môže ísť k peknému(?). Dnes v noci sa mi snívalo len o Luizitovi. Dnes ideme do Torres, s rodičmi. Že by si tam niečo dal? Náš synovček, keď bude starší, bude ako ten chlapec. Veľmi šik je tvoj lístok. Niektorý deň tam pôjdeme. Zbohom, láska moja, do soboty!! Objíma ťa so všetkou láskou, v súkromí, navždy len tvoja Triz. A dnes ti nepošlem bozk!!
>
> Strana s obrázkom: Moja hlava je na tom lepšie.

"Esse menino" may well point at the boy on the picture, and the card's playful close ("today I am not sending you a kiss", written in the margin) suits a lovers' exchange. That is an impression, not a finding.

## Uncertainties

- **Sense, not letters:** "uma grande telha" (read as a whim or mood), "ir ao bonito" (a place, a person or an idiom?) and "a paternidade" (read humorously as "the parents") are interpretive.
- **"dês para":** the signs are firm. The word division and the unwritten accent are a reading, and the sentence's meaning is a guess.
- **"Torres":** read as a place name. Torres Novas lies near Atalaia in Santarém district, and Torres Vedras is also possible; this is general knowledge, not checked. Which Atalaia the card came from is also open; the postmark was not read.
- **"Abraça-te":** literally third person; it may be meant as "I embrace you".
- **Shapes:** d, t and r are close look-alikes. In a few cramped places (pode, paternidade) the shape is not decisive and sense chose. The first sign of the picture-side line is faint; "minha" after it secures "a". The last sign of A17 is blotted and read as s ("a sós"). The first sign of "mando" in the margin is read as m.
- **People:** Laura, Luizito and Triz are unidentified. Triz may be short for Beatriz; that is a guess.

## Review and what changed

A separate Claude Opus 5.5 agent reviewed the solution, read all lines on its own 3–7× crops and decoded with its own script. Verdict: REVISE. It upheld the cipher type, the key and nearly the whole reading, and had six findings, all accepted:

1. The picture-side line lacked four faint signs. "Ha cabeça" became **"A minha cabeça"**.
2. A7 lacked a final sign. "á torre" became **"a Torres"**.
3. "despara" was divided as **"dês para"**.
4. "já hontem" means "already yesterday", not "only yesterday".
5. v has no sign of its own, so the separate label W was dropped and v is now chosen by context.
6. The script's text comparison is no longer offered as evidence of coverage.

The sign count rose from 384 to 389. The earlier claim that no sign was left unread was false and has been withdrawn.

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1332/work/decipher.py
```
