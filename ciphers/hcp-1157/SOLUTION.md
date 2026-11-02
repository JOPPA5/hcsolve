# hcp-1157 solution (round 1, corrected after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal attaches no solution or transcription and shows status Not solved. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. All transcription here is mine, from work/hires/ (no attached transcription exists).

## Cipher type and key

Register label: MASC. The card is open Hungarian; only the two-line salutation is enciphered, in the Mezőkövesd digit-plus-mark monoalphabetic key (one letter = one digit with its mark). The key comes from FINAL sister card hcp-1174 and was not reconstructed here.

Signs on this card (24 signs, 15 distinct, `1.` occurring once and `1'` three times):

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| `1` | i | `2.` | é | `6,` | n |
| `1.` | a | `3` | d | `7` | k |
| `1:` | e | `3,` | r | `7,` | s |
| `1'` | á | `3.` | v | `8` | m |
| `4,` | g | `4.` | gy (new) | `8,` | t |

Ciphertext as read:

    7 1: 3 3. 1: 7,   8 1. 3, 4, 1 8, 7 1' 8 /
    2. 7,   1' 6, 4. 1 7 1' 8 /

The `/` at each line end is a single slanted stroke with no dot (the line 1 stroke has a small hook at the top). I take it as punctuation, an exclamation stroke; it is not a `1`, having no flag, and `margitkámi` is no word. The plaintext prints it as `!`.

`4.` = gy is the only value not on the hcp-1174 table. It has one occurrence here, but it is not new to the family: FINAL sister hcp-1165 fixes it from `5 0 4.` hogy and `6 1. 4. 0 6,` nagyon. The sign here is visibly different from the `4,` of Margitkám (a low dot, no hook), and `ángyika` is a word the correspondence uses (`ángyikával` on hcp-1144, `angyikát` on hcp-1165).

## Plaintext (Hungarian; [ ] = enciphered on the card; line breaks simplified, spelling and word division as written; line-end hyphenated words are joined)

[Kedves Margitkám! És ángyikám!]

Édes anyám már elment csütörtökön Róza itt maradt nem tudom medig lesz itt. En a régi kvártélyon háltam pénteken este demajd az életembe került még most is nagyon rosszul vagyok a dolog úgy történt hogy a szoba nagyon hideg volt és vittem szenet és fát magam voltam egyik inassem hált ott felvoltam 12 óráig mert rendezgettem egyet mást aztán betüzeltem a kályhába jól meg raktam szénnel a cső egyhelyen lyukas én lefeküdtem és egyóra múlva felébredtem borzasztó hányinger fogot elő aligbírtam felkelni már nem volt erőm az ajtót nagy nehezen kinyitottam és ki szaladtam az udvarra ) a szén gáz akart megölni

Sz. A.

mindnyájatokat csókollak.

Normal spelling would give meddig, fogott, Én, kiszaladtam, szén-gáz; `demajd` = de majd, `inassem` = inas sem, `felvoltam` = fel voltam, `aligbírtam` = alig bírtam, `meg raktam` = megraktam, `egyóra` = egy óra.

Address: Tek. / Szépreményü / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács. Postmark MEZŐKÖVESD 915 DEC 3, N, C. The picture side (couple at a fence) has no writing.

## English translation

Dear Margitka of mine! And my ángyika (sister-in-law or aunt by marriage)! [cipher ends]

My dear mother already left on Thursday; Róza stayed here, I don't know how long she will be here. I slept at the old lodgings on Friday evening, but it nearly cost me my life, I am still very unwell. It happened like this: the room was very cold and I carried in coal and wood. I was alone, neither of the apprentices slept there. I was up until 12 because I was tidying one thing and another, then I lit the stove and loaded it well with coal. The pipe has a hole in one place. I lay down and an hour later I woke up; a terrible nausea seized me, I could hardly get up, I had no strength left, with great difficulty I opened the door and ran out into the yard. ) The coal gas tried to kill me.

Sz. A.

I kiss you all.

## Slovak translation

Drahá moja Margitka! A moja ángyika (švagriná alebo teta)! [koniec šifry]

Moja drahá matka už odišla vo štvrtok; Róza tu ostala, neviem, dokedy tu bude. V piatok večer som spal v starom podnájme, ale takmer ma to stálo život, ešte aj teraz mi je veľmi zle. Stalo sa to takto: izba bola veľmi studená a nanosil som uhlie a drevo. Bol som sám, ani jeden z učňov tam nespal. Bol som hore do 12, lebo som upratoval všeličo, potom som zakúril do pece a dobre som ju naložil uhlím. Rúra je na jednom mieste deravá. Ľahol som si a o hodinu som sa zobudil; prepadla ma strašná nevoľnosť, sotva som vládal vstať, už som nemal síl, s veľkými ťažkosťami som otvoril dvere a vybehol som na dvor. ) Uhoľný plyn ma chcel zabiť.

Sz. A.

Bozkávam vás všetkých.

## Command

From the repo root:

    python3 -I ciphers/hcp-1157/work/decode.py

It checks the SHA-256 of all four scans, decodes the 24 signs, asserts each word and prints the card. The open text is hard-coded, so the command reproduces only the decoding of the cipher.

## Uncertainties

Cipher:

- `4.` = gy occurs once here; its value comes from FINAL hcp-1165 and from the word, as stated above.
- `ángyikám`, first sign: I read `1'` (á). In line 2 the dots of the first and the last `1` stand at the same height (measured by the reviewer: rows 184 to 203 and 187 to 205 on the hires scan), so the writer made one sign twice, and the last is á in the same word ending as `Margitkám`. Residual doubt: both dots are lower on the stem than the `1'` of line 1 (rows 77 to 98), so the reading rests on the match and the context, not on the dot alone. The reading `angyikám` would be the same word with a dropped accent, as `angyikát` on hcp-1165 shows, so the sense does not depend on it.
- `ángyika`: I translate it as a kin word, a woman related by marriage, sister-in-law or aunt. It stands in clear in the correspondence (`ángyikával`, hcp-1144), hcp-1165 greets `angyikát`, and hcp-1175 opens `Kedves Ángyika!` to Szegedi Jánosné (from that directory's notes; that card is not finished). `mindnyájatokat` (you all) also points to more than one person in Szomolya. The exact relation, and who the ángyika of this card is, are not given here. A personal name cannot be excluded, and "my little angel" is dropped as main reading.
- The second `7` of line 1 has a looped top, unlike the other 7s, but it has the cross bar, and k is what Margitkám needs. No other 7-like sign is in the family key.

Open text (all read from the pixels):

- `hányinger`: the h is partly under the printed `Serie Nr. 2963`, and could be taken for k at a glance; `kányinger` is not a word.
- `hált` (second one): printed publisher marks overlap the a; `hült` is excluded by sense, and an accent stroke stands above it.
- `már` runs under the printed FOTOTAGLIO box, and `ki` (before `szaladtam`) is blotted; both are legible enough but are the weakest open words.
- `) a szén gáz akart megölni`: there is a closing parenthesis with no opening one. Its role is unexplained. `ölni` is written under `meg-` at the corner.
- Order of the bottom lines: `mindnyájatokat csókollak.` and `Sz. A.` stand on the address side; I print them last, but the writer may have put them there before running out of room.
- `Sz. A.` is taken as written. Sister hcp-1174 signs in cipher `Árpád`. That identification is not proven by this card.
- Postmark day: reads 3 with a stray mark before it; a 13 cannot be fully excluded (portal filename says 12-03). 3 December 1915 was itself a Friday, so "pénteken este" would be a week earlier, or the day is 13 (a Monday), which would suit "still very unwell" better. This is not resolved and does not touch the text.

## Why I believe it is correct

- All 24 signs decode by one table, 23 of them on values fixed independently by hcp-1174 (one of the 23, the looped `7`, is a variant form), and `4.` on a value fixed independently by hcp-1165.
- `Kedves Margitkám!` is the opening used in clear on sister hcp-1178, and the recipient's name is on the address of this card.
- The open text is a continuous, coherent account of carbon monoxide poisoning from a coal stove with a holed flue pipe. It is sequential (cold room, coal, stove, sleep, nausea, weakness, door, yard, cause). Nothing in it is forced.
- The signature `Sz. A.` and the plural kiss match hcp-1175, 1176 and 1178 from the same writer. No Margitka word is enciphered except the salutation here, which fits the family's habit of enciphering only tender words.

## Response to review 1

Verdict REVISE. Re-read at 3x from work/hires (`work/crops/report_cipher.png`, `review/work/z_ang.png`).

1. **`ángyikám` (major): fixed.** I agree. The two dots of line 2 stand level, so they are one sign. My earlier remark that this was "only the accent" was wrong in effect, because it left the little-angel sense as an equal option. Sign table note, ciphertext, `work/decode.py`, plaintext, English, Slovak and uncertainties now read `1'` and `ángyikám`, translated as a kin word. hcp-1144 is cited. Line 2 `1.` no longer occurs. The identity of the ángyika and the exact relation are stated as unknown, and the residual doubt from the lower dot is stated.
2. **`4.` = gy (minor): fixed.** The text now cites hcp-1165, which has since become FINAL, so it needs no caveat about being under revision.
3. **Word division (minor): fixed.** Plaintext and `decode.py` now keep the card's division: `demajd`, `inassem`, `meg raktam`, `egyóra`, and `En`, which has no accent on the card (`work/crops/report_en1.png`). Normal forms are listed under the plaintext. Hyphens at line ends are joined in SOLUTION.md; decode.py keeps `bor-zasztó` broken as a row, and the note above covers it.
4. **End strokes (minor): fixed.** The ciphertext now shows `/`, explained as a single slanted stroke read as punctuation.
5. **Looped `7` (minor): fixed.** The script output and the "why correct" section now note the one variant form.

Disagreement: none. The reading was not substantially changed: one accent in the cipher, its gloss, and word division. Re-run: `python3 -I ciphers/hcp-1157/work/decode.py` prints hashes OK, 24 signs, `kedves margitkám és ángyikám`.
