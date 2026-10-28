# HCP 1556 (pc_hcp_237): a Czech love letter from Pepouš to Anna Tichá

**Status: deciphered in full (336 of 336 cipher signs, 338 letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-28.

## Origin and context

The cryptogram is record 1556 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1556), portal name pc_hcp_237, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-28 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1903-04-26, language Czech, location Europe, sender Unknown, recipient Anna Tichá, with no transcription or solution attached.

It is a picture postcard showing three carnations (dark red, red-and-yellow and pink) on long green stems. The card is scanned sideways; turned upright (90° clockwise), the main cipher text stands in sixteen rows to the right of the stems and below the flowers, and ends with the plain date **26./IV. 1903.** (Sunday, 26 April 1903). Two further cipher lines run along the long edge of the card (the bottom edge of the scan as delivered, the left edge of the upright card) and continue the letter.

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.** ("Honoured Miss Anna Tichá, teacher in Žirovnice near Počátky", South Bohemia). It carries an Austrian 5-heller stamp cancelled PRAHA, whose day and month are mostly covered by the stamp ("6" and "03" are visible), and an inverted arrival postmark ŽIROVNICE / SEROWITZ showing "27", a roman month whose visible part is V, and "03". The printer's line along the left edge reads "Farbenlichtdruck v. Martin Rommel & Co., Hofkunstanstalt, Stuttgart. 563."

The card belongs to a family of cipher postcards to Anna Tichá in the same hand and the same cipher, signed by "Pepouš" (a pet form of Josef), several of which are deciphered in this repository (for example HCP 1520–1527, 1533, 1535, 1537 and 1544). The key used here was transferred unchanged from those earlier cards (ciphers/hcp-1520/work/key.json); a partial key for the family was published earlier by Maxim Egorov (https://maxim-egorov.dev/research/anna-ticha-postcards/). This card was therefore read with a **known, transferred key**; it is not a new key recovery. No reading of this particular card was supplied or consulted.

![Picture side as scanned (source/picture.jpg)](../source/picture.jpg)

![Picture side turned upright: sixteen cipher rows right of the stems ending with the date 26./IV. 1903, and the two-line continuation along the left edge (work/picture-clockwise.png)](../work/picture-clockwise.png)

![Address side: Anna Tichá, teacher in Žirovnice near Počátky; PRAHA stamp cancellation at the top right, ŽIROVNICE / SEROWITZ arrival postmark at the left (source/address.jpg)](../source/address.jpg)

Other marks on the card, none of them cipher: the plain date, the address, the printed postcard headings in several languages, the printer's line, the stamp and the two postmarks, and the HCPortal watermark on both sides. Both solver and reviewer searched both sides and found no other cipher text.

## Method

The transcription is **manual**: the solver turned the scan upright, read the sixteen main rows (M01–M16) and the two edge rows (B01–B02) sign by sign from enlarged per-row crops (work/M01.png to M16.png, B01.png, B02.png), and recorded each row with its crop box in work/rows.json and each of the 336 signs with its row and index in work/positions.json. No OCR was used and the portal supplied no transcription. The difficult places (the K/Z pair, the T/D pair in M01, the two CH signs in M14, the last L of ZTRATIL where it crosses a printed flower stem) were checked against other occurrences of the same shapes on the same card (work/focused-controls.png). Several first readings were corrected on the enlargements before handover, all by rereading the shapes, never by changing the key: BEHEM (M11), KVETNA (six signs, M12), JEMUZ (M09), P. (M08), PUS (M14) and VZPOMI-NAJICI (M15–M16).

The signs are a mixture of digit-like shapes and Latin-like cursive letters, each standing for one plaintext letter, plus one special sign for the digraph CH. The family key decodes every sign of this card into connected Czech, with no unknown or unused sign.

In review the reviewer made its own upright frame and 4× crops, read all eighteen rows independently, wrote down its own shape labels and its own statement of the key, and decoded them with its own script (review/work/my_decode.py). Its reading agrees with the solver's in **all 336 positions**.

## Key

Monoalphabetic substitution; the labels are conventional names for the handwritten shapes, not exact reproductions. Note that the shape labelled `m` stands for N and `n` for M, `t` (crossed) for D and `d` (looped) for T, `c` (round) for S and `s` (angular) for C, and `b` for P and `p` for B. `y` labels the J-shaped sign (it looks like a 7 on this card), and `H` the r-shape with a small cap, which stands for the digraph CH.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | y | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | H | CH | | | | |

The family key also has a shallow v-shaped sign for F; it does not occur on this card. Letters F, G, Q, W and X do not occur in the text. Czech diacritics are not encoded: the cipher writes base letters only (Č as C, Ř as R, Í as I, and so on).

Frequency of each sign on the card (336 in all): 1:9, 2:11, 3:17, 4:29, 5:43, 6:34, y:10, 8:11, b:10, c:21, d:21, f:14, g:15, h:14, m:22, n:14, p:4, q:11, r:5, s:5, t:14, H:2.

## Plaintext

Ciphertext as transcribed, row by row (punctuation and line-end hyphens as on the card):

```text
M01 fh581 d4g, t2c4m-
M02 g3 n3y5 y5t4m6,
M03 q6 th6r1 84cd5g.
M04 m5q6m5tp6f6 nm5 n3y5
M05 6m2mg6 d6g5 f5 cf5n
M06 cht5sg2? n6n d5, 6m2cg3
M07 d384g h6t 6 d32q4n b3 d3p5
M08 m5cn4hm5! - y5 b. h4t4s4
M09 c5t4f1 d1q, y5n2q m5t6fm3
M10 q5nh586 b6m4? - c5yt5n5 c5
M11 6m2mg3 bh5th6r6, p5r5n
M12 gf5dm6? - d5c4 c5 m6
M13 th6r5 h6tg1 df5 6 d4c4s
M14 fh581H, f6cm4f1H b2c d4
M15 b3c486 df2y cd685 fqb3n4-
M16 m6y4s4 b5b32c.
B01 qdh6d48 c5 y4q m5g384g6d1 n2y 84cd5g
B02 d3p5 q6c86m1. gt5 f5q4 d3r3 6c4 bh4s4m6?
```

Literal Czech, as decoded, line for line (base letters only, no accents; the date 26./IV. 1903. is written in plain at the end of M16):

```text
M01 VRELY TIK, DUSIN-
M02 KO MOJE JEDINA,
M03 ZA DRAHY LISTEK.
M04 NEZANEDBAVA MNE MOJE
M05 ANUNKA TAKE VE SVEM
M06 SRDECKU? MAM TE, ANUSKO
M07 TOLIK RAD A TOUZIM PO TOBE
M08 NESMIRNE! - JE P. RIDICI
M09 SEDIVY TYZ, JEMUZ NEDAVNO
M10 ZEMRELA PANI? - SEJDEME SE
M11 ANUNKO PREDRAHA, BEHEM
M12 KVETNA? - TESI SE NA
M13 DRAHE RADKY TVE A TISIC
M14 VRELYCH, VASNIVYCH PUS TI
M15 POSILA TVUJ STALE VZPOMI-
M16 NAJICI PEPOUS.
B01 ZTRATIL SE JIZ NEKOLIKATY MUJ LISTEK
B02 TOBE ZASLANY. KDE VEZI TOHO ASI PRICINA?
```

Normalized Czech (diacritics, capitals, punctuation and the joining of the two split words are editorial; dík is an editorial correction of the card's TIK; p. is kept as the writer's abbreviation of pan):

**Vřelý dík, dušinko moje jediná, za drahý lístek. Nezanedbává mne moje Anunka také ve svém srdečku? Mám tě, Anuško, tolik rád a toužím po tobě nesmírně! — Je p. řídící Šedivý týž, jemuž nedávno zemřela paní? — Sejdeme se, Anunko předrahá, během května? — Těší se na drahé řádky tvé a tisíc vřelých, vášnivých pus ti posílá tvůj stále vzpomínající Pepouš.**

**Ztratil se již několikátý můj lístek tobě zaslaný. Kde vězí toho asi příčina?**

English translation: **Warm thanks, my one and only darling, for your dear card. Does my Anunka not neglect me in her little heart as well? I love you so much, Anuška, and I long for you immensely! — Is the headmaster, Mr Šedivý, the same one whose wife died recently? — Shall we meet, dearest Anunka, some time in May? — Looking forward to your dear lines, your ever-remembering Pepouš sends you a thousand warm, passionate kisses.**

**Yet another of my cards sent to you has been lost. Where might the cause of it lie?**

Slovak translation: **Vrelá vďaka, dušička moja jediná, za milý lístok. Nezanedbáva ma moja Anunka aj vo svojom srdiečku? Mám ťa, Anuška, tak rád a nesmierne po tebe túžim! — Je pán riadiaci Šedivý ten istý, ktorému nedávno zomrela manželka? — Stretneme sa, predrahá Anunka, počas mája? — Na tvoje milé riadky sa teší a tisíc vrúcnych, vášnivých bozkov ti posiela tvoj stále spomínajúci Pepouš.**

**Stratil sa už niekoľký môj lístok poslaný tebe. Kde asi väzí príčina?**

Notes on the reading:

- **TIK / dík.** The first sign of the second word in M01 is the looped d-shape (T), clearly different from the crossed t-shape (D) that opens DUSIN- in the same row; the card therefore literally reads TIK. The intended word is clearly dík ("thanks"), as in the opening Srdečný dík of other family cards. A plausible cause: this cipher gives the crossed t-shape to D and the looped d-shape to T, so the two are easily swapped, and in Czech an initial D and T differ only in voicing. Both solver and reviewer read the sign as T; the literal reading keeps TIK.
- **Šedivý.** The cipher has no capitals, so ŠEDIVY can be read as the surname Šedivý (a common Czech surname: "Is the headmaster, Mr Šedivý, the same one whose wife died recently?") or as the adjective šedivý, "grey-haired" ("Is the grey-haired headmaster the same one whose wife died recently?"). The normalized text uses the surname reading; the card does not decide between them.
- **p. řídící** is pan řídící, the usual form of address for the head teacher of a village school (řídící učitel); the question fits the recipient, herself a teacher.
- **Anunka, Anuško, Anunko** are pet forms of Anna; **dušinko** ("darling", literally "little soul") is split over M01–M02 as DUSIN-KO, and **vzpomínající** over M15–M16 as VZPOMI-NAJICI.
- **Sejdeme se … během května?** ("shall we meet during May?") fits a letter dated late April. **pus** is the genitive plural of pusa, "kiss".
- The two edge lines (B01–B02) are a postscript: the writer complains that yet another of his cards to Anna has gone missing.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1556/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of both scans and the metadata, of the record files and row crops, and of the credited reference files (the family key and controls of ciphers/hcp-1520 and the files in batches/easy-2026-10-28/); checks that the key equals the family key; decodes the manual transcription in work/rows.json with the key in work/key.json; re-encodes every literal row and checks it against the transcription; checks all 336 indexed positions in work/positions.json; checks the literal block in SOLUTION.md; and prints the eighteen literal rows with the line `VERIFY: 18 rows; 336 mapped cipher positions; CH=2; unknown=0; literal letters=338; ...`. It does not read the image; the transcription step is manual and was confirmed independently in review. SOLUTION.md names a machine-specific Python under ~/.cache/codex-runtimes; plain `python3 -I` gives the same result. Because the script verifies files outside ciphers/hcp-1556 (ciphers/hcp-1520/work/ and batches/easy-2026-10-28/), it runs only in a checkout that contains those files.

## Uncertainties

- **One writer's slip.** The card has TIK (the T-shape) where dík is meant; one sign of 336. The cipher text is otherwise consistent, but not flawless.
- **An unusual C.** The 4th sign of PRICINA (B02) has a hook at the top left and a long lower stroke curling left; it is taller and more open than the angular s-shape (C) of RIDICI, TISIC and NAJICI, and lacks the foot of the digit-1 sign (Y). It is read as C, the only reading that gives a word; PŘÍČINA ("cause") is certain from the sentence. This sign was noted by the reviewer.
- **Close calls, all checked on the scan by both solver and reviewer:** the K/Z pair (closed bowl with a top-right flick for K, a 9-like sign hooking left for Z) in KO, ZA, TYZ, JEMUZ, ZEMRELA, KVETNA, ZTRATIL, JIZ and VEZI; the D/T, S/C, B/P, M/N and I/Y pairs throughout; the two capped-r CH signs of VRELYCH and VASNIVYCH; the final L of ZTRATIL where it crosses the printed flower stem (both lobes visible).
- **Šedivý** as surname or adjective, see above.
- The accents, punctuation and word joins of the normalized Czech are editorial. The cipher encodes base letters only; the accents follow standard Czech orthography.
- The sender is known only as Pepouš (Josef); his civil identity, and that of the headmaster, are not established.
- The postmark dates are not fully legible: the PRAHA cancellation is mostly under the stamp, and on the ŽIROVNICE arrival postmark it cannot be seen whether the month is IV or V. If it is V, the card arrived a month after the written date, which would be odd but would fit the card's own complaint about lost cards. The date rests on the plain 26./IV. 1903 on the card and the portal metadata.
- The key was transferred from the earlier family cards and the published partial key, not recovered blind from this card; it decodes every sign here without change.
- No search for a prior publication of this card was made beyond the portal status (Not solved), the AI Decipherment Register (no entry for cryptograms/1556 or pc_hcp_237) and the Cipher-Atelier Anna Tichá readings (no card 237), all on 2026-10-28.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the solver's literal plaintext), made its own upright crops of the scan, read all eighteen rows itself, and decoded its own transcription with its own statement of the key; its reading agreed with the solver's in all 336 positions, with a one-to-one key covering every sign. It confirmed the literal TIK, the K/Z choices, the two CH signs and the final L of ZTRATIL, that neither side carries any other cipher text, and that no prior solution of this card had been published. Its four findings were minor and are reflected here:

- **Unusual C in PŘÍČINA.** Now named in the uncertainties; the reading C is unchanged.
- **Portable command.** The reproduction command is given with plain `python3 -I`.
- **Šedivý.** Both readings, surname and "grey-haired", are now stated.
- **Stale wording.** SOLUTION.md said that no independent review had taken place; its response to review records that this is superseded, and this report does not repeat it.

No decoded letter changed as a result of the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the transcription and decipherment were made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1556, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1556 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4728/conversions/pc_hcp_237_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4729/conversions/pc_hcp_237_adr-large.jpg (source/address.jpg).
- Family key: earlier Anna Tichá family cards in this repository, ciphers/hcp-1520/work/key.json.
- Maxim Egorov, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-28.
