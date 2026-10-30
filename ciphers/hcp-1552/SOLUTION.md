# HCP1552 / pc_hcp_233 — complete reading (Pepouš to Anna Tichá, 30 May 1903)

Status: **complete reading, revised after review 1 (REVISE).** All 14 cipher rows are read: **410 cipher units → 413 base letters, including 3 single-unit CH signs; no unknown span remains.** The overinked word in row 7, formerly the unresolved span U1, is read from the pixels as NAVRATU (see Uncertainties).

The picture side uses the known Anna Tichá family monoalphabetic substitution. This is **known-key transfer**, not independent key discovery. The picture-side date reads **30./V. 1903.** The ordinary address reads "Velectěná Slečna / slečna Anna Tichá / učitelka t. č. v / Pelhřimově.", with "Vlastnoručně dodati". Printed stationery, stamp, postmarks and the modern watermark are not ciphertext; the address side has no ciphertext.

Credits: the transcription, records and decoder were made by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) on 2026-10-28, which left the row-7 span open. Claude Opus 5.5 read that span, handed the card to review (2026-10-29), and made the corrections after review 1.

## Sources and prior knowledge

See `SOURCES.md`. Portal status was Not solved, with no attached transcription or solution. The canonical family key `ciphers/hcp-1520/work/key.json`, the published partial family key `batches/easy-2026-10-28/published-anna-ticha-key.txt` and the [public Anna Tichá research by Maxim Egorov](https://maxim-egorov.dev/research/anna-ticha-postcards/) were available **before** this transcription. No plaintext of this card was supplied or consulted. The AI Decipherment Register had no record for this card (orchestrator check, 2026-10-29).

## Key

| Cipher label | Plain | Cipher label | Plain |
|---|---|---|---|
| 1 | y | 2 | u |
| 3 | o | 4 | i |
| 5 | e | 6 | a |
| 8 | l | b | p |
| c | s | d (round, looped) | t |
| f (tall looped) | v | F (shallow v; unused here) | f |
| g | k | h | r |
| m (two humps) | n | n (one hump) | m |
| p | b | q | z |
| r | h | s | c |
| t (tall crossed) | d | y (the 7-shaped J sign) | j |
| H (r with a small cap/tilde) | ch | | |

Labels are names for glyph shapes. The family key files of other cards (e.g. `ciphers/hcp-1545/work/key.json`) write the J sign as `7` and the CH sign as `ř`; here they are `y` and `H`; the values are identical. 22 classes occur on this card. Diacritics are not encoded.

## Reproduction

From the repository root:

```bash
python3 -I ciphers/hcp-1552/work/decode.py
```

The read-only script checks the hashes of the originals, of the credited reference files and of the six record files; checks that `work/key.json` equals the family key (plus the unused F); rebuilds the per-glyph inventory from `work/transcription.txt`; checks literal equality with `work/literal.txt`; re-encodes the whole literal with the inverse key (greedy CH); and prints the literal. Expected summary: `14 rows; 410 recognized cipher units; 413 recognized base letters; 3 CH units; 0 unknown spans`. It runs only in a checkout that also contains `ciphers/hcp-1520/work/` and `batches/easy-2026-10-28/`.

Output (literal, base letters, source line breaks):

```text
tisicery tik, dusinko moje predraha, za listek
dnesni. vzpominam neustale s touzebnosti a
preji si vrele, aby se anunka uklidnila a mezi
svymi drahymi hodne vesele svatky zazila. tesim
se velice na slibeny listek z pelhrimova.
dopis s podobenkami zaslu ihned po svatcich
po tvem navratu. kdy hodlas se dati vypodob-
niti s karlusou? - pac
a tisic vrelych, uprimnych
pus posila ti vecne
tvuj pepous.
mel jsem vybrany jiny listek, napsal
jsem vsak omylem na nej zirovnickou tvoji
adresu. zaslu ti jej do zirovnice?
```

## Editorial Czech reading

Accents, capitals and punctuation are editorial; VYPODOB-/NITI is joined. "dík" is an editorial correction of the written TIK.

> Tisícerý dík [psáno TIK], dušinko moje předrahá, za lístek dnešní. Vzpomínám neustále s toužebností a přeji si vřele, aby se Anunka uklidnila a mezi svými drahými hodně veselé svátky zažila. Těším se velice na slíbený lístek z Pelhřimova. Dopis s podobenkami zašlu ihned po svátcích po tvém návratu. Kdy hodláš se dáti vypodobniti s Karlušou? – Pac a tisíc vřelých, upřímných pus posílá ti věčně tvůj Pepouš.
>
> Měl jsem vybraný jiný lístek, napsal jsem však omylem na něj žirovnickou tvoji adresu. Zašlu ti jej do Žirovnice?

## English translation

> A thousand thanks, my dearest darling, for today's card. I think of you constantly and with longing, and I warmly wish that Anunka would calm down and spend a very merry holiday among her dear ones. I am very much looking forward to the promised card from Pelhřimov. I will send the letter with the photographs right after the holidays, after your return. When do you intend to have your picture taken with Karluša? – A paw, and a thousand warm, sincere kisses your Pepouš sends you for ever.
>
> I had chosen a different card, but by mistake I wrote your Žirovnice address on it. Shall I send it to you in Žirovnice?

## Slovak translation

> Tisícoraká vďaka, dušička moja predrahá, za dnešný lístok. Neustále s túžbou spomínam a vrúcne si želám, aby sa Anunka upokojila a medzi svojimi drahými prežila veľmi veselé sviatky. Veľmi sa teším na sľúbený lístok z Pelhřimova. List s podobizňami pošlem hneď po sviatkoch, po tvojom návrate. Kedy sa mieniš dať odfotografovať s Karlušou? – Labku a tisíc vrúcnych, úprimných bozkov ti naveky posiela tvoj Pepouš.
>
> Mal som vybraný iný lístok, ale omylom som naň napísal tvoju žirovnickú adresu. Mám ti ho poslať do Žirovnice?

## Uncertainties

- **NAVRATU (row 7, formerly U1).** After `m6` (NA) the signs `f h 6 d 2` and a full stop are read at 9–10x (`work/overink-wide.png`, `review/work/U1_x10.png`). The `h` and the second `6` are retraced in heavier ink; this is read as retracing, not cancellation. An earlier word under the retraced ink cannot be excluded from a 1024×674 scan, but nothing suggests one. The earlier solver kept this span open; it was closed on 2026-10-29 and accepted by the reviewer.
- **TIK (row 1).** The second word is written with the round d (= T), the same as in the first word and in DATI, not the crossed t (= D) of DUSINKO/DOPIS. The card literally reads TIK; "dík" is an editorial correction, as on sister card hcp-1556.
- **SLIBENY (row 5).** The fifth sign is read as `5` (E) on review: it has the top bar and lower bowl of the writer's 5 and lacks the tall left loop of his 6. This is at the resolution limit; the alternative `6` would give SLIBANY, a non-standard form.
- **Stem crossings, bottom rows.** JINY and OMYLEM cross printed flower stems; the reading adds no letters behind stems.
- **Pac** is read as the affectionate "paw" (a hand-giving greeting), a common Czech closing of the period; **Karluša** is a person not otherwise identified; **Anunka** is the pet name of Anna used across the family, here apparently in the third person.
- Accents, capitals and the joining of VYPODOB-/NITI are editorial.

## Why it is believed correct

Every one of the 410 cipher units is decoded with the unchanged family key, with no unmapped sign, and gives continuous, grammatical Czech of 1903 that fits the card: written in Prague on Saturday 30 May 1903, the eve of Whit Sunday (31 May), hence "svátky"; addressed to Anna Tichá, teacher in Pelhřimov; mentions Žirovnice, her home town on other family cards; signed Pepouš, as the whole family. An independent reviewer decoded the transcription with its own key table and read all rows against the scan.

## History (superseded)

The first solver (OpenAI GPT, 2026-10-28) recorded 405 units / 408 letters and left the row-7 overink as an unknown-length span U1, excluding the candidate VRATU from the literal because the segmentation was not secure. Claude Opus 5.5 read the span on 2026-10-29 and handed the card to review as complete; that completion was first recorded only in an appended section, which review 1 flagged (finding 4). The present file replaces the partial-state text.

## Response to review 1

Verdict REVISE. All six findings addressed; the reading changed by two letters (I→U, A→E) and the U1 span is now in the records.

1. **ANINKA → ANUNKA (major) — fixed.** At 6x (`review/work/row3_aninka.png`) the third sign of `6m?mg6` is the same `2` (U) that begins the next word `2g84tm486`, not the `4` (I). Transcription now `6m2mg6`; literal, Czech, English and Slovak say Anunka. Unit count unchanged.
2. **SLIBANY → SLIBENY (minor/major) — fixed.** At 8x (`review/work/r5_slibany_x8.png`) the sign after `p` has the top bar and lower bowl of this writer's `5` and lacks the tall left loop of `6` (compare `6` in the row below in the same crop). Transcription now `c84p5m1` = SLIBENY; literal and editorial text now agree. The residual doubt is disclosed under Uncertainties.
3. **Completion not in the reproducible record (major) — fixed.** `⟦U1⟧` replaced by `fh6d2` in `work/transcription.txt`; `work/inventory.json` rebuilt (row 7 now 35 units; the U1 entry moved to `resolved_spans` with length 5); `work/literal.txt` regenerated; `work/decode.py` no longer handles an unknown span and asserts that every symbol is mapped; record hashes in `work/audit-sha256.json` updated. Re-run: `python3 -I ciphers/hcp-1552/work/decode.py` exits 0 and prints `14 rows; 410 recognized cipher units; 413 recognized base letters; 3 CH units; 0 unknown spans`; its literal equals the block above, and the reviewer's own `review/work/mydecode.py` on the new transcription gives the same text (up to a trailing newline).
4. **SOLUTION.md contradicted itself (major) — fixed.** The file is rewritten: the header states the complete claim, the old partial-state caution is kept only as a short history.
5. **Translation errors (minor) — fixed.** One Czech, one Slovak (and one English) version remain, all with Anunka and návratu; Slovak uses "mieniš" and "podobizňami".
6. **Label convention (minor) — fixed.** The key table now says `y` = the 7-shaped J sign and `H` = the CH sign written `ř` in other family key files.
