# HCP 1530 (pc_hcp_211): a Czech love letter from Pepouš to Anna Tichá

Human solver: Tomáš Pavuk

**Status: deciphered in full. 464 cipher signs give 470 letters; 2 signs are restored from context and 5 are faint. Independent review 1 gave REVISE. The review's findings were addressed and one letter changed (DRAHE to DRAHY).** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1530 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1530), portal name pc_hcp_211. It belongs to the HCPortal collection of cryptographic postcards, which is a private collection. On 2026-10-28 the portal listed it as **Not solved**, with these details:

- tags: Postcard, HCPortal collection
- category: Substitution
- date: 1903-11-14
- language: Czech
- location: Europe
- sender: Unknown
- recipient: Anna Tichá

No transcription or solution was attached.

The picture side shows a stag and a hind in a snowy forest. The scan is sideways. Turned upright (90° counter-clockwise), the card has nine cipher rows at the bottom. Five more rows sit in the top margin, written upside down, and they are the *beginning* of the letter. The reading order is therefore the five top rows (T01–T05), then the nine bottom rows (B01–B09); "TAKE JA" at the end of T05 runs on into "VZPOMINAM" at the start of B01. In the middle of the picture the date **14.XI.1903** is written in plain script. B07 contains one short word in ordinary handwriting, «Issajův», which is not enciphered.

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek** ("Honoured Miss Anna Tichá, teacher in Žirovnice near Počátky", South Bohemia). It carries an Austrian 5-heller stamp cancelled PRAHA and an arrival postmark ŽIROVNICE / SEROWITZ.

The card belongs to a family of cipher postcards to Anna Tichá. They are written in the same hand, use the same cipher and are signed "Pepouš", a pet form of Josef. Several are deciphered in this repository, for example HCP 1520–1527 and 1537–1556. The key was taken over from those cards. Maxim Egorov (Cipher-Atelier) had already published a partial key for the family (https://maxim-egorov.dev/research/anna-ticha-postcards/). This card was therefore read with a **known, transferred key**, not a key recovered from scratch. No earlier reading of this particular card was found or consulted.

![Picture side as scanned (source/picture.jpg)](../source/picture.jpg)

![Picture side turned upright: five upside-down rows in the top margin, the plain date 14.XI.1903 in the middle and nine rows at the bottom (work/upright.png)](../work/upright.png)

![Top margin cropped and turned 180°, rows T01–T05 (work/top-upright.png)](../work/top-upright.png)

![Address side: Anna Tichá, teacher in Žirovnice near Počátky (source/address.jpg)](../source/address.jpg)

## Method

The transcription was made **by hand**. The scan was turned upright and the top margin was cropped and turned again. Each of the 14 rows was then read sign by sign from enlarged crops; no OCR was used. Four places lie under dark paint in the picture: the end of T01, the end of B04, the end of B08 and the middle of a word in B09. These were enlarged five to eight times and read sign by sign. Every sign carries a certainty mark (clear, faint, probable, or restored from context). The record is in work/v2/transcription-v2.json.

The signs are a mixture of digit-like shapes and Latin-like cursive letters. Each sign stands for one plaintext letter, and one special sign stands for the digraph CH. The family key turns every sign on the card into connected Czech. No sign is left without a value.

The work was done in two stages. An OpenAI GPT solver (GPT-6 Astra) made the first transcription. It left the four dark places open as unknown spans and assigned the one F sign by comparing it with an already published card (card 199 / HCP 1518). Claude Opus 5.5 then read the four dark places and handed the solution to review. After the review it corrected the record and wrote this report. A separate Claude Opus 5.5 reviewer made its own crops, typed its own transcription of all 14 rows and decoded it with its own script. Its reading agrees with the final text letter for letter.

## Key

The cipher is a monoalphabetic substitution. The labels below are conventional names for the handwritten shapes. Several of them are traps:

- the shape labelled `m` stands for N, and `n` stands for M;
- the crossed `t` stands for D, and the looped `d` stands for T;
- the round `c` stands for S, and the angular `s` stands for C;
- `b` stands for P, and `p` stands for B;
- `y` labels the J sign, which looks like a 7 on this card;
- `ř` labels the special CH sign;
- `v` is a shallow open v-shape for F, unlike the tall looped `f` (V).

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 8 | L | q | Z |
| g | K | f | V | h | R | t | D |
| r | H | c | S | s | C | n | M |
| m | N | p | B | b | P | d | T |
| y | J | ř | CH | v | F | | |

Czech diacritics are not encoded: the cipher writes base letters only (Ř as R, Í as I, and so on). G, Q, W and X do not occur on this card. F occurs once, in RUDOLFINE.

## Plaintext

Ciphertext as transcribed, row by row. Punctuation is as on the card; «Issajův» is ordinary script.

```text
T01 fh581 t4g cht5sg3 n3y5 q86d5, q6 th6r1 84cd5g
T02 y6g t6h4 c5 m1m4 c r86f4sg32? y6 yc5n, p3r2t4g,
T03 p385cd cf5 r86f1 y4q bh5n3r8, gd5h5 nm5 m1m4
T04 bh4c83 f584s5 m5fr3t. 2 m6c y4q p84q4 c5 t3p6
T05 f6m3sm4 6 c m4 h3qnm3q5m4 bh6s5. d6g5 y6
B01 fqb3n4m6n m6 83mcg1 h3g fd5d3 t3p5,
B02 gt1 n3y5 cht5sg3 qt5 t8583 m6 qg32cg6ř.
B03 cg3t6. 6 d1 r5q32mg5 řf48g1 fqt1 d6g
B04 h1ř85 bhř6y4. y6g dh6f4 6m2cg6 m1m5yc4
B05 t832r5 f5s5h1? n2y q4f3d y5 m6h6nm5 y5tm3-
B06 df6hm1. fs5h6 řd58 yc5n m6fcd4f4d4 f5s5h
B07 g3ms5hd «Issajův» f h2t38v4m5, qthq58 yc5n
B08 c5 fc6g bh484c t832r3 f 2h6t5. d4c4s fh581ř
B09 b2c b3c486 b5b32c cf5n2 y5t4m5n2 cht5sg2.
```

Literal Czech as decoded. Restored letters are in brackets.

```text
T01 VRELY DIK SRDECKO MOJE ZLATE, ZA DRAHY L[IS]TEK
T02 JAK DARI SE NYNI S HLAVICKOU? JA JSEM, BOHUDIK,
T03 BOLEST SVE HLAVY JIZ PREMOHL, KTERE MNE NYNI
T04 PRISLO VELICE NEVHOD. U NAS JIZ BLIZI SE DOBA
T05 VANOCNI A S NI ROZMNOZENI PRACE. TAKE JA
B01 VZPOMINAM NA LONSKY ROK VTETO DOBE,
B02 KDY MOJE SRDECKO ZDE DLELO NA ZKOUSKACH.
B03 SKODA. A TY HEZOUNKE CHVILKY VZDY TAK
B04 RYCHLE PRCHAJI. JAK TRAVI ANUSKA NYNEJSI
B05 DLOUHE VECERY? MUJ ZIVOT JE NARAMNE JEDNO-
B06 TVARNY. VCERA CHTEL JSEM NAVSTIVITI VECER
B07 KONCERT «Issajův» V RUDOLFINE, ZDRZEL JSEM
B08 SE VSAK PRILIS DLOUHO V URADE. TISIC VRELYCH
B09 PUS POSILA PEPOUS SVEMU JEDINEMU SRDECKU.
```

Normalized Czech. Diacritics, capitals, punctuation and the split of VTETO into "v této" are editorial.

**Vřelý dík, srdéčko moje zlaté, za drahý lístek. Jak daří se nyní s hlavičkou? Já jsem, bohudík, bolest své hlavy již přemohl, které mně nyní přišlo velice nevhod. U nás již blíží se doba vánoční a s ní rozmnožení práce. Také já vzpomínám na loňský rok v této době, kdy moje srdéčko zde dlelo na zkouškách. Škoda. A ty hezounké chvilky vždy tak rychle prchají. Jak tráví Anuška nynější dlouhé večery? Můj život je náramně jednotvárný. Včera chtěl jsem navštíviti večer koncert „Issajův“ v Rudolfině, zdržel jsem se však příliš dlouho v úřadě. Tisíc vřelých pus posílá Pepouš svému jedinému srdéčku.**

English translation: **Warm thanks, my golden darling, for your dear card. How is your poor head now? Thank God, I have got over my headache, which came at a very bad moment. Here the Christmas season is already drawing near, and with it more work. I too remember last year at this time, when my darling was here for her examinations. What a pity. And those lovely moments always pass so quickly. How does Anuška spend these long evenings? My life is terribly monotonous. Yesterday I wanted to go to the "Issajův" concert in the Rudolfinum in the evening, but I stayed too long at the office. A thousand warm kisses from Pepouš to his only darling.**

Slovak translation: **Vrelá vďaka, moje zlaté srdiečko, za milý lístok. Ako sa teraz darí hlavičke? Ja som, chvalabohu, bolesť hlavy už premohol, ktorá mi teraz prišla veľmi nevhod. U nás sa už blíži vianočný čas a s ním pribúda práce. Aj ja spomínam na minulý rok v tomto čase, keď tu moje srdiečko pobývalo na skúškach. Škoda. A tie pekné chvíľky vždy tak rýchlo ubiehajú. Ako trávi Anuška terajšie dlhé večery? Môj život je nesmierne jednotvárny. Včera som chcel večer navštíviť koncert „Issajův“ v Rudolfine, zdržal som sa však príliš dlho v úrade. Tisíc vrúcnych bozkov posiela Pepouš svojmu jedinému srdiečku.**

Notes on the reading:

- **Context.** The letter fits a card written in mid-November: Christmas is drawing near and the evenings are long. "Zde" ("here") and the Rudolfinum, the concert hall in Prague, agree with the PRAHA cancellation, so the writer was in Prague. Anna, a teacher, had been in Prague a year earlier "na zkouškách", probably for teacher examinations.
- **Rudolfině** is the Czech locative of Rudolfinum. **«Issajův»** is written in ordinary script, not in cipher, and the handwriting is hard to read. It may refer to the violinist Eugène Ysaÿe, but this is only a suggestion: no source was found for a Ysaÿe concert at the Rudolfinum on 13 November 1903.
- **které mně nyní přišlo velice nevhod** ("which came at a very bad time for me") is ordinary Czech. **pus** is the genitive plural of pusa, "kiss". **srdéčko** and **hezounké** are affectionate diminutives. JEDNO-TVARNY is split across B05–B06.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1530/work/decode.py
```

The script uses only the Python standard library and writes no files. It does the following:

1. checks the SHA-256 hashes of both scans and the metadata;
2. checks that the key (work/key.json) is one-to-one with 23 entries;
3. decodes the manual transcription in work/v2/transcription-v2.json and checks every sign by mapping it back through the inverse key;
4. prints the 14 literal rows above, with restored letters in brackets;
5. ends with `464 cipher units (6 CH) -> 470 letters; 457 clear, 5 faint/probable, 2 restored from context` and a list of the faint signs.

The script does not read the image itself, so the transcription step stays manual. The reviewer confirmed it independently. The first, partial decoder is kept as work/decode-v1-partial.py.

## Uncertainties

- **LÍSTEK (T01).** After the L, one or two signs are lost under dark paint. They are restored as I and S because the word must be lístek and the width fits two signs. The exact number of hidden signs cannot be counted. The L is probable; the closing TEK is clearly visible.
- **Faint signs.** In JEDINEMU (B09) the D and I are faint, and in ÚŘADĚ (B08) the D and E are faint. All four have the right shapes.
- **Z and K.** In this hand Z (`q`) and K (`g`) look nearly the same in ZDE, ZDRŽEL and ZKOUŠKÁCH, so at those places the choice rests partly on Czech word forms as well as shape. The first solver at first misread ZDE as KDE and ZDRŽEL as KDYZEL, then corrected both.
- **F.** The single shallow v-shaped F in RUDOLFINĚ was assigned by comparison with the same sign on the published card 199 / HCP 1518. The word Rudolfině confirms it.
- **«Issajův».** This plain-script word is read tentatively, and the performer is not identified, see above.
- **Postmark.** The arrival postmark ŽIROVNICE seems to read 15 / V / 03, which does not fit the written date of 14.XI.1903. Its month may be worn or partly struck. The dating rests on the written date and on the letter's own content.
- **Editorial choices.** The accents, punctuation and word divisions of the normalized Czech are editorial.
- **Persons.** The sender is known only as Pepouš (Josef). His civil identity is not established.
- **Key.** The key was transferred from the family cards and the published partial key, not recovered from this card. It decodes every sign here without any change.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **REVISE**. The reviewer:

- ran the decoder;
- made its own crops at 5–8× enlargement;
- typed its own transcription of all 14 rows;
- decoded it with its own script.

It confirmed the reading and the completion of the four dark places, found no sign without a value in the key, and found the Czech natural and in keeping with the period and the family of cards. Its findings and what changed:

1. **The command did not produce the claimed plaintext.** The old record still held the four dark places as unknowns. Fixed: a new record transcribes them sign by sign, and the rewritten decoder prints the complete text.
2. **DRAHE should be DRAHY.** The last sign of the word has the foot of the Y sign. Corrected; this is the only letter that changed. "Drahý lístek" also agrees in gender.
3. **SOLUTION.md contradicted itself** (it still said PARTIAL). Fixed: it now opens with one consolidated status and text, and the old sections are marked as superseded history.
4. **How much is restored had to be stated.** Done: the I and S of LÍSTEK are marked as restored and the faint signs are listed.
5. **Z and K look alike.** Now disclosed, see the uncertainties.
6. **NEVHOD is ordinary Czech.** Agreed; the earlier remark calling it unusual was withdrawn.
7. **The Ysaÿe identification is unverified.** It is kept only as a labelled suggestion.

Credits: the first transcription and the F assignment were made by OpenAI GPT (GPT-6 Astra). Claude Opus 5.5 read the dark places, made the post-review corrections and wrote this report. The independent review was done by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1530, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1530 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4650/conversions/pc_hcp_211_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4651/conversions/pc_hcp_211_adr-large.jpg (source/address.jpg).
- Family key: earlier Anna Tichá cards in this repository (ciphers/hcp-1520, ciphers/hcp-1545/work/key.json).
- F reference: card 199 / HCP 1518 photograph, https://api.hcportal.eu/media/4614/pc_hcp_199_pic.JPG
- Maxim Egorov, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29 by the orchestrator: no entry for this card.
