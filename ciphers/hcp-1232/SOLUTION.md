# HCP1232 — Feri to Jolánka Tóth: Corpus Christi, no work, waiting for her call home

**Status: complete reading, no unread word, with disclosed residual points; review 1 corrections incorporated. Claude Opus 5.5, 2026-11-02.** No earlier work exists on this number. The portal shows Not solved, with no transcription or solution attached, and the orchestrator's register check found no record. No published solution of this card was found or used.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the Jolánka postcard family. The key was transferred unchanged from HCP1216 (sign table in its SOLUTION.md; also 1212, 1213, 1217, 1218, 1243, 1301), and every value was tested again on this card. One word, "Szer" at the head of row 1, is in plain script and runs straight into the cipher.

two bars a; six b; left bowl c; tick + long stroke d; three bars e; upright cross f; open loop with descender g; tall stroke + short h/p (near-homograph); dotted crossed curve i (the dot is often absent); inverted T j; section mark k (written S-shaped or 8-shaped); wave l; three short strokes m; two short strokes n; cursive loop o (dots over it for ö); F-sign r; right bowl s; gamma t; plain cross u; chevron v; low descender y; crossed diagonal z. Joined sz and cs are not used as ligatures here: c and s are separate bowls.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1232/work/decode.py
```

It checks the SHA-256 of all four images, decodes `work/ledger.txt` (one token per written sign: 23 main rows, 5 rows in the stamp field) and prints the literal rows and `work/normalized.txt`. The ledger is a manual transcription from the pixels, not OCR. Plainly: the invented signs cannot be typed, so each ledger token is a label for a sign, and most labels are already the letter that the HCP1216 table assigns to that sign (only F, ), X, 6, + and the dotted forms are converted). The command therefore prints and checks the transcription; it does not independently apply a key to raw ciphertext, and the key work lies in reading the signs into labels, which the review repeated on its own crops. `work/zoom.py NAME x0 y0 x1 y1 Z` (coordinates in units of 1.72 original pixels) reproduces an enlarged crop into `work/crops/`.

## Literal decipherment (as printed by the command; {x} = restored or doubtful)

```
01 Szeretetedesjolankam          13 hiany{n}emtudomhogymelik
02 kivanomhogyalegjobb           14 szomb{a}tonkapomkiaköny
03 kedvebenta{l}jasoraim         15 vetde[blot]arokszalasracsagak
04 hogymulaturna{p}jan           16 kormegyekhamagaedesem
05 remele{m}jolendol             17 hivhazaarokszalasba
06 goztammittudjakcsinal         18 tiszeletetetmegkap
07 nilegalabbtelikaval           19 tammelyetköszönök
08 isazidömegmos{t}aztis         20 örülökhogyszesenfo
09 el{v}esztemamiedigszora       21 gadtaaszobaaszonyom
10 kozasomvoltajagerjo           22 ezel{b}ez{a}romsoraim
11 z{s}ihazamegymoczarhoz        23 maradokimadjaferi
12 dolgoznimernagyamuka          stamp: {c}sokolom szamta lanszor imdoja feri
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Hogy mulat Úrnapján? Remélem, jól. Én dolgoztam, mit tudjak csinálni, legalább telik avval is az időm. Meg most azt is elvesztem, ami eddig szórakozásom volt: a Jáger Józsi hazamegy Móczárhoz dolgozni, mer nagy a munkahiány. Nem tudom, melyik szombaton kapom ki a könyvet, de Árokszállásra csak akkor megyek, ha maga, édesem, hív haza Árokszállásba. Tiszteletét megkaptam, melyet köszönök. Örülök, hogy szívesen fogadta a szobaasszonyom. Ezzel bezárom soraim. Maradok imádója Feri.

In the stamp field: Csókolom számtalanszor. Imádója Feri.

Plain address: Szépreményű Tóth Jolánka úrhölgynek, Jász Árokszállás. Postmark fragments: ...PEST, and an Árokszállás postmark showing the number 24; its month and year are not readable. The picture side has only the publisher's printed poem and caption (Aranyeső), no handwriting.

## English

My beloved sweet Jolánka! I wish that my lines find you in the best of spirits. How are you enjoying yourself on Corpus Christi Day? Well, I hope. I worked, for what else could I do; at least that too passes my time. And now I lose even what has been my amusement until now: Józsi Jáger is going home to work for Móczár, because work is very scarce. I do not know on which Saturday I will get my [work] book out, but I will go to Árokszállás only if you, my sweet, call me home to Árokszállás. I have received your respects, for which I thank you. I am glad that my landlady received [it/you] gladly. With this I close my lines. I remain your admirer, Feri.
In the stamp field: I kiss you countless times. Your admirer, Feri.

## Slovak

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Ako sa zabávate na Božie telo? Dúfam, že dobre. Ja som pracoval, čo iné mám robiť, aspoň aj tým mi ubieha čas. A teraz strácam aj to, čo bolo doteraz mojou zábavou: Józsi Jáger ide domov pracovať k Móczárovi, lebo je veľký nedostatok práce. Neviem, ktorú sobotu dostanem knižku, ale do Árokszállásu pôjdem len vtedy, ak ma Vy, moja drahá, zavoláte domov do Árokszállásu. Vaše pozdravy som dostal, za čo ďakujem. Teším sa, že [to/Vás] moja bytná prijala ochotne. Týmto končím svoje riadky. Zostávam Váš ctiteľ Feri.
V poli známky: Bozkávam Vás nespočetnekrát. Váš ctiteľ Feri.

## Uncertainties

No word remains unread. The closing sentence of row 22, unresolved at handover, was settled in review (see Response to review 1).

Restored or doubtful signs, none affecting the sense (items 1 and 2 are the two row-22 calls):

1. **Row 22 `ezel{b}ez{a}rom`**: the sign before e is heavily overinked. It has the hollow foot of the six and a thin lead-in stroke; b rests on word sense (*bezárom*). The a after z is a thin top bar with a faint lower bar in a pink smear; also word sense.
2. **Row 22 first sign**: three strokes (e), the upper two nearly touching at the right, so literal `ezel` for *ezzel*, the spelling known from sister cards. See the reply to finding 1 for the difference from the review.
3. **Row 3 {l}**: the rising stroke of the sign before j lies under the postmark; only part of it shows. `talja` = találja (writer omitted lá).
4. **Row 4 {p}**: two pink smeared strokes between *urna* and *jan*. The smear hides the sign's form; the two strokes match the tall + short sign and p alone makes *Úrnapján*.
5. **Row 8 {t}**: after *mos* stands a gamma with a pool of ink below the bar, which looks partly like r. Read t from word sense (*most*).
6. **Row 11 {s}**: the sign after z in *Józsi* is heavily overinked and looks overwritten, with loops at top and bottom. s is from word sense, supported by nothing else; the name could be another Józ-form. The following i has no visible dot.
7. **Row 13 {n}**: the first stroke of *nem* is covered by a blot, and one stroke follows it. n from word sense.
8. **Row 14**: where the descender of the o of row 13 (*tudom*) crosses the row, brown ink touches the p of *kapom*. It could be a false start. The word is read k a p o m.
9. **Row 15 blot and the a after it**: after *de* comes a large blot with no readable sign, then two bars crossed by a stem. It is read as a: the only word that fits with the following *rokszalasra* is *Árokszállásra*, and row 17 confirms the place-name. The blot may hide a false start or a J of *Jászárokszállás*; the sign might instead be a corrected letter.
10. **Row 15 `csagak`**: the sign in the place of the k of *csak* has the form of g. Normalized *csak akkor*, with *kk* written across the row break as k + k.
11. **Row 20 `szesen`**: all signs are clear. Normalized *szívesen*, assuming the writer dropped *ív*; *szépen* (nicely) is the alternative, and neither fits without a spelling error, so this is an interpretation. The sense of the clause is the same. The object of *fogadta* is not stated.
12. **Stamp row S2**: the t of *számta* is a tall stroke with a small bump rather than a clean gamma, followed by bars with an extra arc above them that may be the foot of the row above. *Számtalanszor* fixes the reading.
13. **Stamp row S3** ends with a single short bar, read as a dash with no letter value and left out of the ledger. **S1–S5**: dots, marks before *Feri* (two small marks) are treated as punctuation.

Word-sense calls and writer's spellings:

14. h/p: *hogy, hiány, hív, haza, -hoz* are h; *Úrnapján, kapom, megkaptam* are p, by word sense only. d/n and the short d in *fogadta* (tick + long stroke, row 21) were checked on enlarged crops; *fogadta* was first misread as *fogan-* and corrected by the tick.
15. Normalizations: *szeretet edes* → szeretett édes (one t lost); *remele{m}* → remélem (third stroke of m lies under the postmark ring, see item 17); *aval is* → avval is; *meg most* kept (could be *még most*); *edig* → eddig; *mer* → mert (spoken form); *muka hiany* → munkahiány (*muka* is also a real colloquial word for toil); *melik* → melyik; *köny|vet* → könyvet (dots written over the o); *tiszeletetet* → tiszteletét (a t lost, and the writer also repeated et); *aszonyom* → asszonyom; *imadja* in row 23 and *imdoja* in the stamp → imádója; *Moczar* kept as a surname, taken as Móczár with assumed accent. Accents are mostly not visible and are supplied.
16. *a könyvet* (row 14–15) is taken as a work or service book; the card does not say which book. Józsi Jáger and Móczár are not identified. Year unknown: the Árokszállás postmark clearly shows 24, not claimed as the day, and its month and year are not readable (the portal's file name also has --24). Úrnap (Corpus Christi) places it in late May or June. The Feri of this card is not proved to be the Feri of HCP1216, though the signature and key match.
17. **Row 5 third stroke of m**: stands where the postmark ring crosses the row; seen as a purple overlap (red under black) at stroke height and spacing.
18. **Row 14, sign after b of *szombaton***: thin top bar, heavy blob, thin bottom bar; closer in form to e, read a from word sense.
19. **Row 9, v of *elvesztem***: chevron with an extra crossing stroke at the left, possibly a correction; v from word sense.
20. **Stamp S1, first sign**: left bowl with an inner curl, like a six; c from word sense (*csókolom*).

## Why it is correct

- The HCP1216 key, unchanged, turns every sign of all 23 rows and the stamp into Hungarian, apart from one blot and the restored, overinked or damaged signs listed above; nothing was fitted to this card.
- Long stretches decode without any choice: *legjobb kedvében*, *mit tudjak csinálni*, *szórakozásom volt*, *Árokszállásra … Árokszállásba* (the name appears twice, and it is the plain-text address), *köszönök*, *örülök hogy*, *szobaasszonyom*, *Maradok … Feri*.
- The text is coherent colloquial Hungarian with the formal *maga* address and the family's closing formulas, and the stamp-field text repeats the signature.
- Row 22 is the family's standard closing, *Ezzel bezárom soraim*, as decoded independently on hcp-1235, 1249 and others. This reading came from review 1, not from the handover.

## Response to review 1

Verdict REVISE. Every finding checked on the hires scan; all fixed except one detail of finding 1. Reproduction re-run after the changes: all four hashes OK.

1. **Row 22 z, not v: fixed, with one correction to the finding.** On `review/work/crops/cmp.png` and my own `work/crops/row22.png` the disputed sign is a long diagonal crossed by a descending stroke, the same shape as the z above it, and unlike the plain chevron of row 7. The word is *bezárom*; the closing is the family formula and "soraim" is right as written. Ledger, normalized text and both translations are changed, and my "unresolved" item and "I await my lines" are gone. **I disagree on one detail:** the review says the first sign of the row shows two bars (a), so `azel`. `work/crops/row21-22-left.png` shows three strokes, top and middle nearly joined at the right, then a separate lower one; the two-bar a at the left of row 21 sits directly above for comparison. It is e, and the literal is `ezel`, exactly the sister cards' form. My handover also had a here, so this corrects my own ledger too. Credit: z/*bezárom* came from the review.
2. **munkahiány: fixed** in English and Slovak (lack of work). `muka` omitting n remains disclosed.
3. **Row 5 m: fixed.** On `r05.png` the purple overlap has stroke height and spacing. Ledger {M}, normalization note changed, disclosed as item 17.
4. **Row 14 ö: fixed.** Two dark dots stand over the sign on `r14k.png`. Ledger O:, literal `köny`.
5. **Undisclosed damaged signs: fixed.** All three seen on `r14.png`, `r09.png`, `stamp.png`; now marked {a}, {v}, {c} in the ledger and listed as items 18 to 20. The "Why it is correct" line covers them.
6. **Postmark: fixed.** 24 is clear on `pm120.png`; reported without claiming it is the day.
7. **fogadta gloss: fixed.** [it/you] and [to/Vás]; *szépen* added to item on row 20.
8. **tiszeletetet: fixed** in the normalization item.
9. **Reproduction: fixed.** Row 11 and row 22 tokens now use the stated `)` and `6` labels, and the Reproduction section and ledger header say plainly that the ledger is a labelled transcription, not ciphertext run through a key.
10. **Status and evidence: fixed.** Title line and "Why it is correct" updated, with the origin of the reading stated.

The cipher type, key and sense of the card are unchanged apart from the closing sentence, which the review settled and which reads as a fixed formula.
