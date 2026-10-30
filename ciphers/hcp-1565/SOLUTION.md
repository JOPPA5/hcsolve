# HCP 1565 / pc_hcp_246: solution (revised after review 1)

**Status: complete reading.** Nine physical rows. 395 cipher signs (including one CH sign), giving 396 letters. No unread spans remain. One drawn heart after PEPOU is not a cipher sign. All 22 key classes occur. Review 1 (verdict REVISE) is addressed below.

Credit and history:
- The first partial reading was made by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), with 381 units and six postmark spans left opaque.
- On 2026-10-29 Claude Opus 5.5 read the postmark spans as the solver.
- Review 1 was done by a separate Claude Opus 5.5 agent. It corrected four signs, and the corrections were verified on the scan and adopted here.
- The key is the published Anna Tichá family key, transferred unchanged from ciphers/hcp-1520/work/key.json. That key is credited to Maxim Egorov / Cipher-Atelier's partial study (https://maxim-egorov.dev/research/anna-ticha-postcards/) and to the earlier family cards. This is a known-key transfer, not key discovery.
- The portal (status Not solved) attaches no transcription or solution for this card.

## Cipher and key

Monoalphabetic substitution of the Anna Tichá / Pepouš family, plus one marked sign for CH. Diacritics are not encoded.

| Class |1|2|3|4|5|6|8|q|g|f|h|t|r|c|s|n|m|p|b|d|y|H|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Literal |y|u|o|i|e|a|l|z|k|v|r|d|h|s|c|m|n|b|p|t|j|ch|

## Source layout

- **Picture side** (`source/picture.jpg`). Four bottom rows, H01–H04, are in the original orientation. Five margin rows, M01–M05, are read after a 90° counter-clockwise rotation. A postmark is overprinted on the starts of the margin rows.
- **Plain date.** The handwritten date reads 19./II.1903, which agrees with the portal date 1903-02-19.
- **Address side.** "Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek".

Transcription (`work/transcription.txt`; ♡ = drawn heart, not a cipher sign):

```text
H01 fh581 b6s 6 b2c2 q6 th6r5 h3qd3n485 bc6mg3 df3y5, y5r3q 3pc6r nm5 f584s5 3p86q48.
H02 cg3t6, q5 d5 m5n3r2 q6 m5 f6cm4f5 qb2c3f6d4? 3tb3f4n t3b4c5n t85 n3qm3cd4 s3 m5y-
H03 th4f5: n6n y4d4 bh4cd4 d1t5m t3 cd6f4d58cg5r3 f5m5sg2 f r3d582 n3m3b382. 3p5tf6n
H04 c m5g384g6 s85m1 f1p3h2, gd5h4 nm5 t2dg84f5 qf32. t32f6n fc6g, q5 c5 f5m5sg2 f1rm2.
M01 b3c486n 6n3hg6, 6p1 ct5848 n5 6m2ms5,
M02 q5 y4 n6n f6cm4f5 h6t 6 6p1 b48m5
M03 q685f68 gf5d4mg2 m6c4 p86q4s4 86cg1.
M04 d4c4s. b3qth6f2 6 t832r1H b2c b3c486
M05 f5sm5 df2y b5b32♡.
```

Literal Czech (base letters, as decoded):

<!-- literal-start -->
```text
H01 vrely pac a pusu za drahe roztomile psanko tvoje, jehoz obsah mne velice oblazil.
H02 skoda, ze te nemohu za ne vasnive zpusovati? odpovim dopisem dle moznosti co nej-
H03 drive: mam jiti pristi tyden do stavitelskeho venecku v hotelu monopolu. obedvam
H04 s nekolika cleny vyboru, kteri mne dutklive zvou. douvam vsak, ze se venecku vyhnu.
M01 posilam amorka, aby sdelil me anunce,
M02 ze ji mam vasnive rad a aby pilne
M03 zaleval kvetinku nasi blazici lasky.
M04 tisic. pozdravu a dlouhych pus posila
M05 vecne tvuj pepou♡.
```
<!-- literal-end -->

Editorial Czech (accents, capitals and punctuation added; H02–H03 joined; [Doufám] is an editorial correction of literal DOUVAM):

> Vřelý pac a pusu za drahé roztomilé psánko Tvoje, jehož obsah mne velice oblažil. Škoda, že Tě nemohu za ně vášnivě zpusovati! Odpovím dopisem dle možnosti co nejdříve: mám jíti příští týden do stavitelského věnečku v hotelu Monopolu. Obědvám s několika členy výboru, kteří mne důtklivě zvou. [Doufám] však, že se věnečku vyhnu.
>
> Posílám amorka, aby sdělil mé Anunce, že ji mám vášnivě rád a aby pilně zaléval květinku naší blažící lásky. Tisíc pozdravů a dlouhých pus posílá věčně Tvůj Pepou[š]♡.

English:

> A warm handshake and a kiss for your dear, sweet little letter, whose contents delighted me greatly. What a pity I cannot smother you with kisses for it! I will answer by letter as soon as possible. Next week I am supposed to go to the builders' dance (stavitelský věneček) at the Hotel Monopol. I am having lunch with several members of the committee, who are urging me to come. But I hope I will avoid the dance.
>
> I am sending a little Cupid to tell my Anunka that I love her passionately, and to diligently water the little flower of our blissful love. A thousand greetings and long kisses, forever your Pepouš ♡.

Slovak:

> Vrelé podanie ruky a bozk za Tvoj drahý, milý lístoček, ktorého obsah ma veľmi potešil. Škoda, že Ťa zaň nemôžem vášnivo vybozkávať! Odpoviem listom podľa možnosti čo najskôr: budúci týždeň mám ísť na staviteľský venček v hoteli Monopol. Obedujem s niekoľkými členmi výboru, ktorí ma naliehavo pozývajú. Dúfam však, že sa venčeku vyhnem.
>
> Posielam amorka, aby oznámil mojej Anunke, že ju mám vášnivo rád, a aby usilovne polieval kvetinku našej blaživej lásky. Tisíc pozdravov a dlhých bozkov posiela navždy Tvoj Pepouš ♡.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1565/work/decode.py
```

The script uses only the standard library and writes nothing. It performs these checks:
- the source hashes;
- that the key is byte-identical to ciphers/hcp-1520/work/key.json;
- it decodes `work/transcription.txt` and re-encodes every row with the inverse key;
- it checks the result against `work/transcription.json`, `work/literal-czech.txt`, `work/glyph-index.csv` and the literal block above.

It prints the nine literal rows and a PASS line. The corrected records were written by `work/apply-review1.py`.

## Uncertainties

- **DOUVAM / doufám (H04).** The 4th sign of `t32f6n` is read as f (V), giving DOUVAM. A small stroke at x-height might be an F crossbar or a ligature, and this cannot be decided at the scan's resolution. "Doufám" in the editorial text is an editorial correction.
- **POSILAM (M01).** The first sign is a tall b-form under heavy postmark dots, and the c is partly blackened by a stamp dot. The shapes fit, but the word relies partly on context.
- **The heart after PEPOU (M05).** It is a drawn heart, not a cipher sign, and it is not counted. Whether it replaces the final Š or is pure decoration cannot be decided. The editorial "Pepouš" follows the signature on the sister cards.
- **ZPUSOVATI** is a colloquial verb from *pusa* ("kiss"), "to cover with kisses". It is not a standard dictionary form, but it is clearly legible.
- **Unconfirmed historical details.** The Hotel Monopol and the stavitelský věneček are not identified historically. The town is not named on the card.
- **Accents.** The accents and punctuation of the editorial text are editorial.

## Why it is believed correct

- The unchanged family key decodes all 395 signs into fluent, grammatical Czech of about 1903, with no leftover sign.
- The text is a love letter to "Anunka" (Anna Tichá) signed Pepou(š), consistent with the family and the address.
- The reviewer independently re-read every row on enlargements and decoded with an independently typed key. Its reading is identical to the one given here.

## Response to review 1

1. **Command failed and did not give the full plaintext (major): fixed.**
   - The old `decode.py` hash-pinned SOLUTION.md and NOTES.md through `work/manifest.json`, so every later edit broke it. It also still carried `<UNK>` spans.
   - `work/apply-review1.py` now writes the completed, corrected transcription into `work/transcription.json`, `transcription.txt`, `literal-czech.txt` and `glyph-index.csv`.
   - `decode.py` was rewritten. It no longer hashes the editable record files (only the source scans and the key identity). It decodes the full transcription, with the inverse-key, record and literal-block checks.
   - Re-run result: PASS, 9 rows, 395 signs, 0 unknown. The old `work/manifest.json` is superseded and no longer used.
2. **H01 `t4g` DIK → `b6s` PAC (major): fixed.** On review/work/h01_dik6x.png I see the same three signs:
   - a b with a bowl, matching the first sign of b2c2;
   - a 6;
   - the small s-class sign.

   "Vřelý pac a pusu" is the common Czech formula. The earlier "dík" was supplied from context.
3. **H02 ZLUSOVATI → `qb2c3f6d4` ZPUSOVATI (major): fixed.** On h02_zpus7x.png the 2nd sign has an ascender and a bowl (b = P), under the watermark band. The invented editorial "zlíbati" is removed.
4. **M03 `g f5d4mg5` → `gf5d4mg2` KVĚTINKU (major): fixed.**
   - On m03_kvetink.png the final sign is the 2 (U) form, not the 5.
   - There is no word space after g.
5. **M03 BLAZISI → `p86q4s4` BLAZICI (major): fixed.** On m03_blaz6x.png the 6th sign is the small s-class sign, unlike the round c of m6c4 just before it. The c/s alternative is closed.
6. **U01–U06 (minor): adopted.**
   - U02–U05 are confirmed.
   - U01 (POSILAM) is now disclosed as partly context-supported.
   - The U06 heart is recorded as a non-cipher mark (♡) and is not counted as a unit. The editorial Š is marked as editorial.
7. **DOUVAM (minor): adopted.** The literal stays DOUVAM. "[Doufám]" is flagged as an editorial correction, and the possible F-crossbar is disclosed.
8. **Self-contradictory SOLUTION.md (minor): fixed.** This file was rewritten with one status, one literal, one editorial text, English and Slovak translations, current counts (395 signs / 396 letters / 0 unknown) and one uncertainty list. The superseded partial text is summarized under "Credit and history".
9. **Watcher 401 (minor, no content effect): noted.** Nothing to change.
