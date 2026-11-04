# hcp-1132 (cpc_--_HU_Debrecen_HU__) - solution, round 1

Status: **complete reading**, with the disclosed residual points listed below. Solver: Claude Opus 5.5
(claude-opus-5-5), 2026-11-03. The orchestrator captured the portal page and the scans on 2026-11-03. All
segmentation, transcription, key identification and decoding are new work done in this round. No earlier
solver worked on this number.

No published solution was found or used. The portal status is "Not solved", and the portal attaches no
transcription or solution. A web search for the addressee and card found nothing. The orchestrator's check of
the AI Decipherment Register (2026-11-03) found no record.

## Card and context

- Hungarian picture postcard "Libapásztorleány / Gänsemädchen / Goose-herd Maid", Hafa, Budapest (photo
  Debreczeny József), no. 173. T. Schrödel collection.
- Stamp: 6 fillér "Debreceni Collegium 1538-1938 / Egyetem", Magyar Kir. Posta (1938 issue), cancelled
  DEBRECEN. The date of the postmark is not legible. The card was therefore posted in 1938 or later.
- Address, in plain cursive Hungarian: "Tek. Sődy Sándor / fodrász m. urnak / H. / Csapó utca 97. szám". This means
  "To Mr. Sándor Sődy, master hairdresser, local [Helyben = Debrecen], Csapó Street no. 97". Csapó utca is a
  street in Debrecen. A pencil "200" (a dealer's price?) is also on the card.
- Plain note, written upside down at the top: "Vigyázz a kis libákra !!!", meaning "Watch out for the little
  geese!!!". This is a joke on the goose-girl picture: "kis liba" (little goose) is also slang for a silly young girl.
- The picture side has no handwriting; it was checked with contrast enhancement. I could not see under the stamp.

## Cipher type and key

**International Morse code written with pen dots and dashes** (no secret key). The register type label is `MASC/Morse`.

- The message fills the left half of the address side in **21 vertical columns**. Turn the card 90° anticlockwise
  (the printed "Copyright Hafa ..." line then stands upside down along the top of the field; corrected wording, see Response to review 1). The columns then become lines. The **right-most column is read first**, each
  from top to bottom. The writer then ran out of room and wrote a short **line along the bottom edge**, read left to right.
- A dot is a short, round, dark blob. A dash is a stroke 30-110 px long in the 3468 px scan. Letter breaks are
  only larger gaps (about 45-120 px, against 12-40 px inside a letter). No word breaks are marked, and words run on
  across columns.
- The letters are standard International Morse plus the usual Hungarian extensions **É `..-..`, Á `.--.-`, Ö `---.`**.
  Hungarian digraphs are sent letter by letter (SZ = S+Z, CS = C+S, GY = G+Y, NY = N+Y). Ó is sent as plain O.
- Punctuation is written in the reading orientation. A short stroke beside a column is a **comma**. A stroke with a dot
  is **"!"** (in C2, C4 and C21). One section of C10 is **struck through** by the writer.

## Transcription

`work/transcription.txt` holds all 21 columns plus the bottom line, transcribed from enlarged crops of
`work/hires/cpc_--_HU_Debrecen_HU___adr.jpg` (strip and zoom crops in `work/crops/`, made by `work/zoom.py`,
`work/zoom2.py`, `work/pair.py`, `work/strips2.py`). The mark list is `work/comps.json` (`work/components.py`).
Column assignment was checked by eye, because the columns on the left lean by up to 100 px.

## Command (run from the repo root)

```
python3 -I ciphers/hcp-1132/work/decode.py
```

It checks the SHA-256 of both `source/` images and both `work/hires/` originals. Then it decodes every column and prints:

```
C1   ÉDES JO KIS          C12  BA, MAJD RÖ
C2   URAM! KEDVES         C13  VIDESEN ELMON
C3   SORAID MEG           C14  DOM, SOKAT,
C4   KAPTAM! BO           C15  GONDOLVA
C5   CSÁS MEG É           C16  RÁD, SZÁM
C6   DESEM HOGY           C17  TALANSZOR
C7   ÉN NEM VÁLA          C18  CSOKOL KI
C8   SZOLTAM SO           C19  S FELESÉGED
C9   RAIDRA DE SOK        C20  ANYA ESTE VÁ
C10  SOK MINDEN, [struck out]   C21  RLAK!! TÁNCO
C11  ÉRT MOSTANÁ          BL   LUNK
```

## Plaintext (Hungarian)

As written (column breaks joined, punctuation as on the card):

> ÉDES JO KIS URAM! KEDVES SORAID MEGKAPTAM! BOCSÁS MEG ÉDESEM HOGY ÉN NEM VÁLASZOLTAM SORAIDRA DE SOK
> SOK MINDEN, [struck out] ÉRT MOSTANÁBA, MAJD RÖVIDESEN ELMONDOM, SOKAT, GONDOLVA RÁD, SZÁMTALANSZOR
> CSOKOL KIS FELESÉGED ANYA ESTE VÁRLAK!! TÁNCOLUNK

Normalised: "Édes jó kis uram! Kedves soraid[at] megkaptam! Bocsás[s] meg, édesem, hogy én nem válaszoltam
soraidra, de sok-sok minden ért mostanába[n], majd rövidesen elmondom. Sokat gondolva rád, számtalanszor csókol
kis feleséged, Anya. Este várlak!! Táncolunk."

Plain-text parts: "Vigyázz a kis libákra !!!" (upside down) and the address (see above). At the bottom centre of
the Morse field, three plain question marks "? ? ?" (x 990-1150, y 2040-2105) are written upright in the normal
card orientation. They belong to no column and are not Morse; probably a teasing "can you read it?".

## English translation

"My sweet, good little husband! I have received your dear lines! Forgive me, darling, for not answering your
lines, but lots and lots of things have happened to me lately; I'll tell you about it soon. Thinking of you a lot,
your little wife, Anya ("Mum"), kisses you countless times. I'll be waiting for you this evening!! We'll dance."
Plain note: "Watch out for the little geese!!!"

## Slovak translation

„Môj sladký, dobrý malý mužíček! Tvoje milé riadky som dostala! Odpusť mi, zlatko, že som ti na tvoje riadky
neodpovedala, ale v poslednom čase sa mi stalo veľa, veľa vecí; čoskoro ti to porozprávam. S myšlienkami na teba
ťa nespočetnekrát bozkáva tvoja malá manželka, Anya („mamka“). Večer ťa čakám!! Budeme tancovať.“
Poznámka: „Pozor na malé husky!!!“

## Uncertainties (all disclosed)

1. **Letter boundaries are not marked**, only by gap size. That size overlaps in places, and the split was chosen by
   word sense in these spots:
   - É in C1 (internal gap 38 px).
   - The Y of HOGY in C6 (internal gap 52 px).
   - **ANYA** in C20 (`.- -. -.-- .-`). The gap of 48 px inside `-.--` would otherwise give the non-word "ANNMA".
2. **C13, end of ELMON-**: the N is a single heavy black stroke at the bottom edge (y 2019-2110). It has a thick upper part and a
   thickened foot, joined by a thin neck, and is read as dash + dot run together. This rests on the word ELMONDOM.
3. **Bottom line, final K (`-.-`)**: the last dash is the horizontal foot of an L-shaped stroke. The vertical arm of
   the same stroke is the last dash of C11's Á (MOSTANÁBA). One continuous piece of ink is therefore used by two
   letters. Without it, C11 would end in P and the bottom line in N, and neither gives a word.
4. **Struck-through section** in C10 (y 1810-2040): a long line drawn through about five marks. It is the writer's
   own deletion and is not read. A small hooked stroke just before it is taken as a comma.
5. **"!!" in C21**: two dots plus three short strokes between C20 and C21 (y 985-1052). By the construction of the "!" in C2 and C4
   (stroke on the column line, dot to its left), they are read as "!!" after VÁRLAK. The third stroke has no dot of its own. If placed after
   ANYA instead, the meaning does not change.
6. Spellings as written: BOCSÁS (standard bocsáss), SORAID MEGKAPTAM (standard soraidat), MOSTANÁBA (colloquial
   or eastern-dialect form of mostanában), JO / CSOKOL for jó / csókol (Morse without Ó). Commas after ELMONDOM and
   SOKAT are the writer's, and the normalised text keeps only the sense.
7. "ANYA" ("Mum") is read as the wife's signature or pet name; a personal name cannot be excluded. The sender is not named
   anywhere else.
8. Not checked: what is under the stamp (no image), and the postmark date.

## Why I believe it is correct

- Every mark in all 21 columns and in the bottom line is used. Each group is a valid Morse letter, and the whole decodes
  into continuous, grammatical, colloquial Hungarian with no gaps apart from the writer's own deletion.
- The text fits the address: a wife writes to her husband ("uram", "kis feleséged"), a hairdresser in Debrecen. The plain joke about
  the "little geese" matches the picture. The Hungarian Morse letters É, Á and Ö occur where the words need them.
- The punctuation has its own consistent logic: strokes beside the column are commas, and stroke + dot is "!".

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave the verdict **ACCEPT** with five minor findings. Response by the
solver (Claude Opus 5.5), 2026-11-03:

1. **Shared L-stroke (MOSTANÁBA / TÁNCOLUNK).** Agreed. It stays listed as uncertainty 3, and the report states that it
   is an inference from word sense, made because one continuous stroke is used by two letters. No change to the reading.
2. **Heavy stroke at the end of C13 (ELMON|DOM).** Agreed. Uncertainty 2 is kept, and the report says that no separate
   dot can be seen and that N rests on the word ELMONDOM.
3. **Three exclamation marks in the plain note.** Fixed. I made my own crop of the hires scan, turned upright
   (`work/crops/note_upright.png`, x 1450-2250, y 0-260, rotated 180°). It clearly shows three "!" after "libákra". The
   note is now "Vigyázz a kis libákra !!!" everywhere in this file, in NOTES.md and in the report, with the translations to match.
4. **Morse letter splits chosen by word sense** (É in C1, Y in HOGY, ANYA in C20). Agreed. They stay listed under uncertainty 1.
5. **Type label.** It stays `MASC/Morse`. The report states that Morse is a public code with no secret key. On the user's
   question about steganography under the stamp (raised for the Árokszállás Jolánka series): this card is not from that
   series. The stamp lies flat, and no ink shows at its edges in the scan, but there is no image without the stamp. A hidden
   message there therefore cannot be ruled out. It stays a stated limitation, and `MASC + Steganography` is not used,
   because nothing on this card shows hidden writing.

A further correction from my own re-check: the orientation note said that after turning the card 90° anticlockwise the
"Copyright Hafa ..." line "reads normally". That was wrong. In the reading orientation it stands upside down along the top
(see `work/crops/morse_reading.png`). The direction of the turn and the reading order were right and are unchanged.

The reproduction command `python3 -I ciphers/hcp-1132/work/decode.py` was re-run after these edits. All four hash checks
print OK, and the output is unchanged (21 columns + BL). No decoded letter changed.
