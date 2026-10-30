# HCP1570 / pc_hcp_251: Pepouš to Anna Tichá, 27 December 1902 (v2, after review 1)

**Status: deciphered in full.** All 523 cipher signs are mapped: 521 to the unchanged Anna Tichá family key (6 of them its CH sign) and 2 to the family's k-shaped **G** sign (already attested on hcp-1541, hcp-1553 and hcp-1554). That gives 529 plaintext letters, with no unknown sign. Version 2 applies the four transcription corrections from review 1, which I confirmed on the scan. The v1 record, in which one sign was left as an opaque `{U1}`, is kept unchanged in `work/v1/`.

Credit: the source capture, the row framework, the v1 transcription and the first reading were made by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) together with its root process. The v1 completion (handover DONE1) and this v2 revision are by Claude Opus 5.5. The family key comes from earlier family cards in this repository (`ciphers/hcp-1520/work/key.json`) and from Maxim Egorov's published partial study (https://maxim-egorov.dev/research/anna-ticha-postcards/). No reading of this card was supplied or consulted.

## Sources and scope

Portal record https://crypto.hcportal.eu/dashboard/cryptograms/1570, name **pc_hcp_251**. The portal shows status Not solved, Czech, Substitution, date 1902-12-27, sender unknown, recipient Anna Tichá, private collection. No transcription or solution was attached. The two sides are `source/picture.jpg` and `source/address.jpg` (see `SOURCES.md`).

The picture side (1024×674) is read after a **90° counter-clockwise rotation** (674×1024). It holds 15 cipher rows in the upper block. The words **Veselé vánoce!** next to R03 and the date **27/XII 1902** after R15 are written in plain and are not part of the cipher. The address side is in plain: Anna Tichá, učitelka t.č. v Pelhřimově, with the note *Vlastnoručně dodati!* ("to be delivered into her own hands"). No other cipher text appears on either side.

## Key

Monoalphabetic substitution, base letters only, with one digraph sign. The labels are names for the handwritten shapes.

| Label | Plain | Label | Plain | Label | Plain | Label | Plain |
|---|---|---|---|---|---|---|---|
| 1 | y | 2 | u | 3 | o | 4 | i |
| 5 | e | 6 | a | 8 | l | q | z |
| g | k | f | v | h | r | t | d |
| r | h | c | s | s | c | n | m |
| m | n | p | b | b | p | d | t |
| y | j | H | ch | **G** | **g** | | |

The first 22 entries are byte-identical to `ciphers/hcp-1520/work/key.json`. **G** is the family's k-shaped sign: an ascender with a loop and a kicked leg. It is distinct from the looped-descender `g` (K) and from h/R. It occurs twice on this card: R08 SVAGROVA and R11 KOLEGY. On other family cards it stands in SVAGRA (hcp-1541), TELEGRAMY (hcp-1553) and TELEGRAM (hcp-1554).

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1570/work/decode.py
```

The command uses only the standard library and writes no files. It checks the hashes of the sources and records (`work/sha256.json`). It checks that the key is the family key plus G, then decodes `work/transcription.txt`, checks the row boxes, `positions.csv`, `inventory.json` and this file's literal block, and re-encodes the whole plaintext through the inverse key (CH before C). It prints the 15 rows and a CHECKED line. `work/rebuild_v2.py` documents how the v2 records were derived from v1 (four sign corrections).

## Literal Czech base text

```text
tisicery dik, anicko moje predraha, za hezounky
listek. mel bych vsak opravdu prijeti s metlou na
tebe, ponevadz si sve zdravi tak
dlouhym bdenim kazis. to nesmis vice, drahousku,
delati. kdyz je churava, nepise mi tak dlouho a
ja se tak rmoutim o sve srdecko. jak dari se ti
na svatcich? letos nestravil jsem stedry vecer
u bratrance. svagrova je churava a, ackoliv
jsem mel jeste tri pozvani, nesel jsem nikam,
nybrz stravili jsme vecer ten jeste s dvema
kolegy v hostinci, kam chodim na obed a na
veceri. vzpomela jsi sobe doma tez v skutku na
pepouse, ktery na tebe stale vzpomina? tisic pus
a vrelych pozdravu od tveho na odpoved nesmirne se
tesiciho pepouse.
```

## Editorial Czech

Accents, capitals and punctuation are editorial. *v skutku* is joined to *vskutku*. One spelling is repaired openly: the card has VZPOMELA, and the editorial text gives *vzpomněla* with the N added.

> Tisícerý dík, Aničko moje předrahá, za hezounký lístek. Měl bych však opravdu přijeti s metlou na tebe, poněvadž si své zdraví tak dlouhým bděním kazíš. To nesmíš více, drahoušku, dělati. Když je churavá, nepíše mi tak dlouho a já se tak rmoutím o své srdéčko. Jak daří se ti na svátcích? Letos nestrávil jsem Štědrý večer u bratrance. Švagrová je churavá a, ačkoliv jsem měl ještě tři pozvání, nešel jsem nikam, nýbrž strávili jsme večer ten ještě s dvěma kolegy v hostinci, kam chodím na oběd a na večeři. [Vzpomněla; doslova VZPOMELA] jsi sobě doma též vskutku na Pepouše, který na tebe stále vzpomíná? Tisíc pus a vřelých pozdravů od tvého na odpověď nesmírně se těšícího Pepouše.

## English translation

> A thousand thanks, my dearest Anička, for the lovely little card. I really ought to come at you with a broom, since you are ruining your health by staying up so long. You must not do that any more, darling. When she is ill, she does not write to me for so long, and I worry so about my little sweetheart. How are you getting on over the holidays? This year I did not spend Christmas Eve at my cousin's. My sister-in-law is ill and, although I still had three invitations, I went nowhere; instead we spent that evening with two colleagues in the inn where I go for lunch and supper. Did you really think of Pepouš at home, who thinks of you all the time? A thousand kisses and warm greetings from your Pepouš, who looks forward immensely to your reply.

## Slovak translation

> Tisícorá vďaka, Anička moja predrahá, za krásnučký lístok. Mal by som však naozaj prísť na teba s metlou, pretože si svoje zdravie takým dlhým bdením kazíš. To už nesmieš, drahúšik, robiť. Keď je chorá, tak dlho mi nepíše a ja sa tak trápim o svoje srdiečko. Ako sa ti darí počas sviatkov? Tento rok som nestrávil Štedrý večer u bratranca. Švagriná je chorá a hoci som mal ešte tri pozvania, nešiel som nikam, ale ten večer sme ešte strávili s dvoma kolegami v hostinci, kam chodím na obed a na večeru. Spomenula si si doma naozaj aj na Pepouša, ktorý na teba stále spomína? Tisíc bozkov a vrúcnych pozdravov od tvojho Pepouša, ktorý sa nesmierne teší na odpoveď.

## Uncertainties

- **R11 KOLEGY.** The sign after G is read as `1` (Y). It matches `1` in TISICERY and NYBRZ, but its foot is faint over the printed background. `4` (I) would give the variant spelling *kolegi*. The meaning is the same either way.
- **VZPOMELA (R12).** n/M is followed directly by 5/E, so the writer left out N. The editorial text adds it.
- **Writer corrections (not changes to the reading).** In R04 DLOUHYM, the `1` (Y) is written over another stroke. In R10 STRAVILI, the `8` (L) is darker and appears to have been retraced.
- **Interpretation.** *Když je churavá* is literally third person ("when she is ill"); it is kept as written, although it may refer playfully to Anička herself. *s metlou* ("with a broom") is read literally from the signs.
- The key was transferred from the family, not recovered blind. Every sign on this card fits it without change, apart from the family's rare G sign.
- Pepouš (a pet form of Josef) is not identified further.

## Why I believe it is correct

All 523 signs decode into continuous, grammatical Czech of the period, with a single dropped letter (VZPOMELA). The content fits the date and the card: a Christmas card dated 27 December, with *Veselé vánoce!* in plain, describes Christmas Eve (*Štědrý večer*) and the holidays. The salutation, the pet names and the closing match the other Pepouš cards. A separate Claude Opus 5.5 reviewer made an independent re-reading. After the four corrections, the reviewer's transcription is identical, sign for sign, to `work/transcription.txt`.

## Response to review 1

Verdict REVISE. I re-read every disputed place myself on 3x crops of the rows (`work/R08.png` to `work/R11.png`, further enlarged) and on the reviewer's panels. I accept all seven findings, and all of them are fixed in v2. The reproduction command was re-run and passes.

1. **R08 SVAKROVA → SVAGROVA (fixed).** The 4th sign of `cf6?h3f6` is plainly the k-shaped sign: an ascender with a loop and a kicked leg. It is not the looped-descender `g` of ACKOLIV in the same row. It is now transcribed `G` = g. The editorial "K→G" note is removed. Class counts: g 21→20, G 2.
2. **R09 TVE → TRI (fixed).** At high zoom the word reads `d h 4`: a short humped h/R without a descender, then the crossbar `4`. It is not the tall looped f/V and `5` of R14 TVEHO. The sentence now reads *ačkoliv jsem měl ještě tři pozvání*, "although I still had three invitations". The editorial Czech and both translations have been corrected. The v1 claim that root panels "confirmed" TVE was wrong.
3. **R10 JSEM → JSME (fixed).** R10 shows `y c n 5`, against `y c 5 n` (JSEM) in R09. *strávili jsme* is therefore regular Czech. The editorial removal of the final I of STRAVILI is dropped, and STRAVILI is no longer listed as an anomaly.
4. **R11 U1 + I → G + Y (fixed, residual uncertainty disclosed).** The sign after G has the lead-in and closed foot of `1`, like `1` in `m1phq` (NYBRZ) in R10. It lacks the open arm and flat bar of this hand's `4`. Read as Y: KOLEGY. Because the foot is faint, the alternative *kolegi* is listed under uncertainties. The v1 claim that the final I was "the writer's own spelling" is withdrawn.
5. **G argument (fixed).** G now rests on visual evidence: the same sign appears in R08 SVAGROVA and on hcp-1541, 1553 and 1554. It does not rest on word fit. The v1 statements "none of the family cards has a G sign" and "the sign occurs only here" were wrong and are withdrawn. G is now a key entry (`work/key.json`), and the command prints the complete plaintext without `{U1}`.
6. **Overwritten signs (disclosed).** R04 DLOUHYM (`1` written over another stroke) and R10 STRAVILI (`8` retraced) are now listed as writer corrections under uncertainties and in `work/transcription.json` (`notes_v2`). The reading is unchanged.
7. **Stale text (fixed).** This file now describes one current state. The partial-candidate and "root QA" wording is gone, and the v1 history is preserved in `work/v1/`. NOTES.md has a readable v2 entry.

Changes to the reading: three words in R08 to R11 (svagrová, tři, jsme) and the completion of kolegy. The rest of the letter, the key and the sign count (523) are unchanged.
