# HCP 1548 / pc_hcp_229: complete reading (Czech postcard to Anna Tichá, 6.VII.1903)

**Status (current, 2026-10-29, after review 1):** complete reading. All 296 base cipher units are decoded with the fixed Anna Tichá family key, with no unmapped sign. Two units (R02 positions 18–19, `5 2` → E U in NEUSTALE) lie under the printed green stem. They are recorded as a **restoration**: the U is clearly visible and the E is only partly visible. The key was transferred from earlier family cards, not discovered on this card.

Credit: OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol collaboration, 2026-10-28) did the source capture, the manual transcription, the key transfer and the partial reading, leaving one stem-covered span. Claude Opus 5.5 restored that span as solver on 2026-10-29. A separate Claude Opus 5.5 agent reviewed the work (review 1, REVISE). This file was then rewritten into one current statement. The superseded partial-state text is summarised under *History* at the end.

## Source

- **Card:** a Czech picture postcard addressed to *Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek*.
- **Date:** the ordinary date on the picture side is **6.VII.1903**, matching the portal date 1903-07-06.
- **Portal:** read on 2026-10-28 (General, Description and Attachments). Status *Not solved*, private collection, no transcription or solution attached. See `SOURCES.md` and `source/metadata.md`.
- **Cipher text:** nine handwritten rows on the picture side. The address side, the printed matter, the stamp and the postmarks carry no cipher.

## Type and key

Monoalphabetic substitution of base Czech letters (no diacritics). One extra sign, `ř` (an r with a separate bar or cap), stands for the digraph CH. The key is the family key, byte-identical to `ciphers/hcp-1545/work/key.json`. It was first published as a partial study by Maxim Egorov (<https://maxim-egorov.dev/research/anna-ticha-postcards/>) and is used on the earlier family cards in this repository.

|Shape|1|2|3|4|5|6|7|8|b|c|d|f|g|h|m|n|p|q|r|s|t|ř|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Plain|Y|U|O|I|E|A|J|L|P|S|T|V|K|R|N|M|B|Z|H|C|D|CH|

Inventory on this card (296 units): 1:9 2:8 3:23 4:19 5:27 6:31 7:7 8:13 b:8 c:25 d:18 f:17 g:7 h:12 m:20 n:14 p:5 q:10 r:9 s:4 t:9 ř:1.

## Ciphertext (work/ciphertext.txt)

```text
d4c4s5h1 t4g q6 3p6 th6r5 84cdg1 6 q6 fqb3-
n4mg2. 76 fqb3n4m68 m52cd685. 74q c5 n5
cht5sg3 m5rm5f6? - 3 c86fm3cd4 7c5n d5md3-
gh6d5 m5n58 qt5 q6tm5 m6fcd5f1. p18 7c5n
c5 t4f6d m6 bh2f3t 4 m6 f86cdm4 c86fm3cd
m6 cd6h3n5cdcg5n m6n5cd4. fc3p3d2 p18 7c5n
m6 bh3n3s4 ph6dh6 3m3r3 qm6n5r3 n5r3 g3n4c6h5
q 74r86f1. d4c4s fh581r b3qth6f2 6 t832r1r f6cm4-
f1ř b2c b3c486 df27 b.
```

In R02, the `52` after `m` is the restored stem-covered pair.

## Literal plaintext (work/literal.txt)

```text
TISICERY DIK ZA OBA DRAHE LISTKY A ZA VZPO-
MINKU. JA VZPOMINAL NEUSTALE. JIZ SE ME
SRDECKO NEHNEVA? - O SLAVNOSTI JSEM TENTO-
KRATE NEMEL ZDE ZADNE NAVSTEVY. BYL JSEM
SE DIVAT NA PRUVOD I NA VLASTNI SLAVNOST
NA STAROMESTSKEM NAMESTI. VSOBOTU BYL JSEM
NA PROMOCI BRATRA ONOHO ZNAMEHO MEHO KOMISARE
Z JIHLAVY. TISIC VRELYH POZDRAVU A DLOUHYH VASNI-
VYCH PUS POSILA TVUJ P.
```

The ordinary date 6.VII.1903 follows in plain writing.

## Editorial Czech

Accents, word division and the CH in *vřelých, dlouhých* are editorial. The card has VRELYH and DLOUHYH.

> Tisícerý dík za oba drahé lístky a za vzpomínku. Já vzpomínal neustále. Již se mé srdéčko nehněvá? – O slavnosti jsem tentokráte neměl zde žádné návštěvy. Byl jsem se dívat na průvod i na vlastní slavnost na Staroměstském náměstí. V sobotu byl jsem na promoci bratra onoho známého mého komisaře z Jihlavy. Tisíc vřelých pozdravů a dlouhých vášnivých pus posílá tvůj P[epouš?].

The signature on the card is only **P.** The expansion *P[epouš?]* is a family inference: other cards to Anna Tichá in the same hand and cipher are signed *Pepouš* in full (e.g. hcp-1556). It is not read on this card.

## English translation

> A thousand thanks for both dear cards and for remembering me. I have been thinking of you constantly. Is my little heart no longer angry? – This time I had no visitors here for the celebration. I went to watch the procession and the celebration itself on Old Town Square. On Saturday I was at the graduation of the brother of that commissioner from Jihlava whom I know. A thousand warm greetings and long passionate kisses are sent by your P.

## Slovak translation

> Tisícoraká vďaka za oba drahé lístky a za spomienku. Ja som spomínal neustále. Už sa moje srdiečko nehnevá? – Počas slávnosti som tentoraz nemal žiadne návštevy. Bol som sa pozrieť na sprievod aj na samotnú slávnosť na Staromestskom námestí. V sobotu som bol na promócii brata toho môjho známeho komisára z Jihlavy. Tisíc vrúcnych pozdravov a dlhých vášnivých bozkov posiela tvoj P.

## Reproduction

From the repository root:

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1548/work/decode.py
```

Plain `python3 -I` also works, because the script uses only the standard library. The script:

- checks the hashes of the originals, the record files and the reference files;
- decodes `work/transcription.json` with `work/key.json`;
- checks every indexed position in `work/positions.csv`;
- checks that `work/literal.txt` and `work/ciphertext.txt` match exactly;
- re-encodes each plaintext row with the fixed key and compares it with the ciphertext row;
- asserts 296 units, exactly one CH, and exactly the two restored units R02/18–19.

It prints the literal plaintext above and the line "296 base cipher units, all mapped by the fixed key -> 297 base letters; no unmapped sign". `work/build-record.py` (needs PIL) regenerates the record files and row crops. It was re-run on 2026-10-29 for the restoration.

## Uncertainties

1. **NEUSTALE (R02/18–19), a restoration.** The pair sits under the printed green stem. After `m` there is room for exactly one small sign. It is dark, with a hooked top, consistent with a small `5` (E) as in R03/R04 `m5`, and only partly visible. Next comes a clearly visible `2` (U), then `cd685`. *Neustále* ("constantly") is the natural Czech word. The crops are `work/claude/neustale.png` and the reviewer's `review/work/r02_stem_red.png`.
2. **VRELYH, DLOUHYH (R08).** The two final r's have no CH bar, unlike the barred `ř` in R09 `f1ř` (VYCH). This is a writer's omission. The literal keeps H, and the editorial text reads *vřelých, dlouhých*.
3. **Stem crossings.** R01 DRAHE, R03 SLAVNOSTI and R04 NAVSTEVY cross the stem. Their strokes remain readable, and the reviewer confirmed them.
4. **Signature.** The final underlined `b` gives P. The sender's identity (Pepouš?), the brother and the commissioner from Jihlava are not established. The celebration on Old Town Square on 6 July fits the Jan Hus commemoration, but this is context only and is not used as evidence.
5. **Editorial details.** Accents, *mé* for ME, and VSOBOTU written as one word (= *v sobotu*) are editorial.
6. **Image resolution.** The portal image is 1024×674. The restoration in uncertainty 1 is read at the limit of this resolution.

## Why the reading is correct

A fixed family key, unchanged, turns all nine rows into continuous idiomatic Czech of the period. The content (thanks for cards, *srdéčko*, a visit to Prague, kisses, signature P) matches the family. The reviewer read the transcription independently against the scan and decoded it with its own script, with identical output.

## Response to review 1

Review 1 (Claude Opus 5.5) gave the verdict REVISE. It confirmed the decipherment, the transcription and the NEUSTALE restoration. The findings concerned the consistency of the records.

1. **major – the reproduction command and records did not give the claimed plaintext.**
   - **Fixed.** `work/build-record.py` now records R02 as `m52cd685`. The two units carry `"restored": true` in `work/transcription.json`, and the former `unknown_spans` entry is replaced by a `restorations` entry describing the evidence.
   - I re-ran `build-record.py`, which regenerated `transcription.json`, `positions.csv` (now 296 indexed positions; R02/18 = 5/E, R02/19 = 2/U), `ciphertext.txt`, `literal.txt` and `record-sha256.json`.
   - `work/decode.py` no longer accepts unknown spans. It asserts 296 units and exactly the two restored units, and prints NEUSTALE.
   - I re-ran the command on 2026-10-29. It passes all checks and prints the literal plaintext above.
2. **major – SOLUTION.md contradicted itself.**
   - **Fixed.** This file is now one current statement: one literal plaintext, one Czech version, one English version and one Slovak version.
   - The partial-state text is no longer presented as current. It is summarised under *History*.
   - I added a dated entry to NOTES.md that supersedes the earlier "partial" lines there.
3. **minor – the sender name was expanded.**
   - **Fixed.** The Czech now ends *P[epouš?]*, with a note that the expansion is a family inference and not a reading. The English and Slovak versions have P only.
4. **minor – VRELYH/DLOUHYH.**
   - **Agreed.** Uncertainty 2 now states this plainly as a writer's omission, read editorially as *vřelých, dlouhých*.
5. **minor – the E is partly visible.**
   - **Agreed and corrected.** I had written that the E was only inferred. I looked again at `review/work/r02_stem_red.png`: between `m` and the visible `2` there is a small dark sign with a hooked top, consistent with `5`. Uncertainty 1 now says the E is partly visible. It is still listed as a restoration.

The reading is unchanged by the review. Only the records and wording changed.

## History (superseded)

- **2026-10-28, OpenAI GPT.** Source capture, manual transcription, family-key decoding and the record/guard scripts. The handover was a *substantial partial reading*: 294 mapped units plus one stem-covered span of unknown length, U1, in R02 (N⟦U1⟧STALE).
  - At that point the final b/P and the R09 CH were labelled tentative. A preliminary K/Z mislabel (JIK → JIZ) had been corrected using `work/q-g-controls.png`.
- **2026-10-29, Claude Opus 5.5 (solver).** Read U1 from the enlarged crop `work/claude/neustale.png` as one hidden sign plus a visible `2`, giving NEUSTALE. Handed over as DONE1.
- **2026-10-29, review 1.** REVISE. The records were brought into line, as described above.
