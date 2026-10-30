# HCP 1538 (pc_hcp_219): a Czech love letter from Pepouš to Anna Tichá

Human solver: Tomáš Pavuk

**Status: deciphered in full (503 cipher signs: 498 read, 1 partly visible, 4 restored at the edge of a printed stem or flower); independent review 1 verdict REVISE, findings addressed, reading unchanged apart from the two corrections the reviewer verified.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1538 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1538), portal name pc_hcp_219, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-28 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1903-09-22, language Czech, location Europe, sender Unknown, recipient Anna Tichá, with no transcription or solution attached.

It is a picture postcard with a printed bouquet whose tied stems run across the middle of the card. The card is scanned sideways; turned upright (90° clockwise), the main cipher text stands in eleven rows (M01–M11) across the bouquet stem, with the plain date **22./IX.1903** (Tuesday, 22 September 1903). Four more cipher rows (S01–S04) stand upside down along the upper edge of the scan, partly over a printed yellow flower, and continue the letter.

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.** ("Honoured Miss Anna Tichá, teacher in Žirovnice near Počátky", South Bohemia). It carries no cipher text.

The card belongs to a family of cipher postcards to Anna Tichá in the same hand and cipher, signed "Pepouš" (a pet form of Josef); several are deciphered in this repository (for example HCP 1520–1527, 1545 and 1556). The key was **transferred** from those cards and from the partial family key published by Maxim Egorov (https://maxim-egorov.dev/research/anna-ticha-postcards/); it was not recovered blind from this card. No reading of this card was supplied or consulted.

![Picture side as scanned (source/picture.jpg)](../source/picture.jpg)

![Picture side turned upright: rows M01–M11 run across the printed stem; S01–S04 are the inverted rows at the top of the scan (work/picture-upright.png)](../work/picture-upright.png)

![Address side (source/address.jpg)](../source/address.jpg)

## Method

The transcription is **manual** (no OCR; the portal supplies none). The first transcription and partial decipherment were made on 2026-10-28 by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol). It left ten dark "spans" where rows meet the printed stem or the yellow flower, one overinked word in M08 and one ambiguous sign in S01.

Claude Opus 5.5 completed the reading on 2026-10-29. Enlargements at the stem (work/claude/stem-a.png, below) show that **the stem was printed before the writing and the writer left it blank**: every row stops cleanly at the left edge of the stem and resumes at its right edge, and the signs on both sides are complete. So seven of the ten "spans" (M01–M05, M08, M09) hide no letters at all. In three places (M06, M07 at the stem; S01 at the flower) a sign or two at the edge is lost; these are restored from Czech grammar and marked as restorations. The overinked word in M08 reads sign by sign as `bh3r84q5d4` = PROHLÍŽETI; the ink is only heavier, not a cancellation.

![Rows M01–M04 at the printed stem, enlarged: each row ends at the left edge of the stem and resumes at its right (work/claude/stem-a.png)](../work/claude/stem-a.png)

Each sign stands for one plaintext letter (one sign for the digraph CH). The family key decodes every sign of the card; no sign is unknown.

## Key

Monoalphabetic substitution; the labels are conventional names for the handwritten shapes. Note the pairs that swap: `m` = N and `n` = M, `t` (crossed) = D and `d` (looped) = T, `c` = S and `s` = C, `b` = P and `p` = B. `y` and `7` both label the J sign; `ř` labels the CH sign.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | y / 7 | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | ř | CH | | | | |

The family's shallow v-sign (F) does not occur here. Diacritics are not encoded (Č as C, Í as I, and so on).

Frequency of each sign on the card (503 in all, restorations included): 1:10, 2:22, 3:34, 4:44, 5:60, 6:39, y:10, 7:3, 8:17, b:15, c:36, d:29, f:20, g:23, h:18, m:33, n:24, p:8, q:12, r:7, s:15, t:23, ř:1.

## Plaintext

Ciphertext as transcribed (`||` = the blank printed stem, `[..]` = restored signs, `(..)` = partly visible sign):

```text
M01 d4c4s5h1 t4g q6 th6r1 || 84cd5g tm5cm4! d6g5
M02 nm5 c5 6m4sg3 n6 || 75t4m6, f584s5 cd1cg6
M03 b3 d3p5. t3f385m5 n5 || c5, th6r32cg2, p6d4 m5n2-
M04 c4s, fqt4d f4c, q5 y5m || d5p5 6 bh3 fqt1 n6n h6t.
M05 q627686 yc4 n3y4 t2c4 || s5832 6 m5m4 d6n y4q
M06 n4cd6 bh3 m4g3r3 y4m5r[3] || t3f385m32 cf3y4 cdh6f4n
M07 6c4 s5832 f5 cb385sm[3c]||(d)4 b6m6 t5g6m6, c gd5-
M08 h1n p2t5n5 bh3r84q5d4 || b6n5dm4 gm4r2 t5g6m-
M09 cg32, y6g yc5n c4 || d3 y4q q6n832f68 bh4
M10 s5s48cg5n g3ms5hd5. t5m, gt1 3ty5t2 t3c2t
M11 m5f4n, n1c84n fc6g, q5 p2t f5 sdfhd5g f5s5h m5p
S01 f b6d5g h6m3. q685q4 m[6] || d3n, gt1 p2t2 c 2sd5n
S02 gf6hd68m4n r3d3f. d4c4s 2bh4nm1ř b2c d4 b3c486
S03 f5sm5 df27 b5b32c, gd5h1 c5 m6 c84p5m5 bc6mg3
S04 m5cn4hm5 d5c4.
```

Literal Czech, as decoded (base letters only):

```text
M01 tisicery dik za drahy listek dnesni! take
M02 mne se anicko ma jedina, velice styska
M03 po tobe. dovolene me se, drahousku, bati nemu-
M04 sic, vzdit vis, ze jen tebe a pro vzdy mam rad.
M05 zaujala jsi moji dusi celou a neni tam jiz
M06 mista pro nikoho jineh[o] dovolenou svoji stravim
M07 asi celou ve spolecn[os](t)i pana dekana, s kte-
M08 rym budeme prohlizeti pametni knihu dekan-
M09 skou, jak jsem si to jiz zamlouval pri
M10 cecilskem koncerte. den, kdy odjedu dosud
M11 nevim, myslim vsak, ze bud ve ctvrtek vecer neb
S01 v patek rano. zalezi n[a] tom, kdy budu s uctem
S02 kvartalnim hotov. tisic uprimnych pus ti posila
S03 vecne tvuj pepous, ktery se na slibene psanko
S04 nesmirne tesi.
```

Normalized Czech (accents, capitals, punctuation and word joins are editorial):

**Tisícerý dík za drahý lístek dnešní! Také mně se, Aničko má jediná, velice stýská po tobě. Dovolené mé se, drahoušku, báti nemusíš, vždyť víš, že jen tebe a pro vždy mám rád. Zaujala jsi moji duši celou a není tam již místa pro nikoho jiného. Dovolenou svoji strávím asi celou ve společnosti pana děkana, s kterým budeme prohlížeti pamětní knihu děkanskou, jak jsem si to již zamlouval při cecilském koncertě. Den, kdy odjedu, dosud nevím, myslím však, že buď ve čtvrtek večer neb v pátek ráno. Záleží na tom, kdy budu s účtem kvartálním hotov. Tisíc upřímných pus ti posílá věčně tvůj Pepouš, který se na slíbené psánko nesmírně těší.**

English translation: **A thousand thanks for your dear card today! I too miss you very much, my only Anička. You need not fear my holiday, darling; you know that I love only you, and for ever. You have taken my whole soul and there is no room left in it for anyone else. I shall probably spend my whole holiday in the company of the dean, with whom we are to look through the deanery's memorial book, as I already arranged at the Cecilian concert. I do not yet know the day I leave, but I think either Thursday evening or Friday morning. It depends on when I finish the quarterly accounts. A thousand sincere kisses are sent to you by your ever-faithful Pepouš, who is immensely looking forward to the promised little letter.**

Slovak translation: **Tisícoraká vďaka za drahý dnešný lístok! Aj mne sa, Anička moja jediná, veľmi cnie za tebou. Mojej dovolenky sa, miláčik, báť nemusíš, veď vieš, že len teba a navždy mám rád. Zaujala si celú moju dušu a nie je tam už miesto pre nikoho iného. Dovolenku strávim asi celú v spoločnosti pána dekana, s ktorým budeme prezerať dekanskú pamätnú knihu, ako som si to už dohodol pri cecilskom koncerte. Deň odchodu ešte neviem, myslím však, že buď vo štvrtok večer, alebo v piatok ráno. Záleží na tom, kedy budem hotový so štvrťročným účtom. Tisíc úprimných bozkov ti posiela naveky tvoj Pepouš, ktorý sa nesmierne teší na sľúbený list.**

Notes on the reading:

- **NEMU-SIC (M03–M04)** is the writer's spelling of *nemusíš* ("you need not"); the same habit appears on a sister card as TESIC for *těšíš*. **VZDIT** (`fqt4d`, with I, not Y) is normalised to *vždyť*. **pus** is the genitive plural of *pusa* ("kiss").
- **Dovolené mé se … báti nemusíš** ("you need not fear my holiday"): Pepouš reassures Anna about a holiday he will spend with the dean, looking through the deanery's memorial book (*pamětní kniha*), arranged at a Cecilian (church-music) concert.
- **Thursday evening or Friday morning** fits a card written on Tuesday 22 September 1903; the **quarterly accounts** (*účet kvartální*) fit the end of the third quarter.

## Reproduction

From the repository root:

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1538/work/decode_final.py
```

(plain `python3 -I` works the same; the script uses only the standard library). It checks the SHA-256 of both scans, decodes the manual transcription `work/transcript-final.txt` with the key `work/key.json`, stops on any unmapped glyph, counts read, partly visible and restored signs separately, compares the output with the saved `work/decoded-final.txt`, and prints the fifteen literal rows above under the line `COMPLETE literal reading: 498 signs read, 1 partly visible, 4 restored; 503 cipher signs total; no unmapped glyphs.` The transcription itself is manual; the script does not read the image.

## Uncertainties

- **Three restorations.** JINEH[O] (M06), SPOLEČN[OS]TI (M07) and N[A] TOM (S01) lie at the edge of the stem or the yellow flower. The four restored signs are not read; they rest on edge traces and grammar. The Czech in each case (*jiného*, *ve společnosti*, *záleží na tom*) is not in doubt.
- **Partly visible signs.** In M07 only the ascender of `d` (T) shows right of the stem. In S01 the sign before the flower has the m-form (N); *na tom* rests on that form and on context together.
- **Close calls checked on the scan:** M03 `n5` = MÉ (one-hump n, as in `n6` MÁ, unlike the two-hump m of `t3f385m5`); M08 `r84` under heavier ink; the raised `s` that ends NEMUSIC in M04.
- Only the scan exists, so it cannot be checked whether any letter lies physically under the stem in M06, M07 or S01.
- The accents and punctuation of the normalized Czech are editorial. The sender is known only as Pepouš; the dean and the concert are not identified.
- The key is transferred from the family, not recovered blind from this card; it decodes every sign here without change.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent (Anthropic), round 1, verdict **REVISE**. The reviewer ran the solver's command, decoded the transcription with its own script and the family key from another card (all signs mapped), and checked the stem, the restorations and many ordinary rows on its own 4–8× crops. It confirmed that the stem was printed first and hides nothing in seven rows, and it confirmed MÉ in M03 and PROHLÍŽETI in M08. Its findings and what changed:

1. **major — the reproducible record still showed the old partial state.** A new final transcription and decoder replace it (work/transcript-final.txt, work/decode_final.py); restorations are kept in brackets and counted separately; SOLUTION.md's header and uncertainties now match the complete reading. The round-1 files are kept as history.
2. **major — a sign missing in M04.** A raised `s` before the comma was added: NEMU-SIC (*nemusíš*). The total is now 503 signs.
3. **minor — word division in M07.** The record now separates *ve | společnosti*.
4. **minor — wording of the restorations.** The uncertainties now say that *na tom* rests on form and context, and that the M07 `d` is only partly visible.
5. **minor — VZDIT.** Kept literal; *vždyť* is stated as a normalisation.

The reading itself did not change, apart from the two corrections the reviewer verified on the scan (MÉ and the added S of NEMUSIC).

## Credits

Initial transcription and partial decipherment: OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol), 2026-10-28. Completion of the reading, response to review and this report: Claude Opus 5.5 (Anthropic), 2026-10-29. Independent review: a separate Claude Opus 5.5 agent. Family key: earlier Anna Tichá cards in this repository and the published partial study by Maxim Egorov.

## Sources

- HC Portal record 1538, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1538 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4674/conversions/pc_hcp_219_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4675/conversions/pc_hcp_219_adr-large.jpg (source/address.jpg).
- Maxim Egorov, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
