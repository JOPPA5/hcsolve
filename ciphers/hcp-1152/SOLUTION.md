# hcp-1152 solution (round 1, corrected after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal shows Not solved and attaches no solution or transcription. No published solution of this card was found in the repo. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. The key comes from FINAL card hcp-1174 and the later cards of the family; the transcription is my own, from `work/hires/`.

## Cipher type and key

Hungarian letter to Margitka Sziber, Szomolya, from the Mezőkövesd writer (signed Sz. A.). The salutation and the first part of the letter are enciphered (118 signs in 8 written lines); the end of the sentence, the verses and the closing are in clear. Register label: MASC. A letter is one sign: a digit, alone or with a mark, and the mark is part of the sign. Word spaces are mostly kept. Key transferred, not rebuilt. Signs on this card:

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o | | `2,` | cs | | `6` | j |
| `1` | i, í | | `2.` | é | | `6,` | n |
| `1.` | a | | `3` | d | | `7` | k |
| `1:` | e | | `3,` | r | | `7,` | s |
| `1'` (high dot) | á | | `3.` | v | | `7.` | sz |
| `.1` (dot on the left) | u | | `4,` | g | | `8` | m |
| `-1` (dash on the left) | ú | | `4.` | gy | | `8,` | t |
| | | | `5` | h | | `9` | p |
| | | | `5,` | l | | | |

`.1` = u is from hcp-1168 and `-1` = ú from hcp-1170, each with thin support there. Both are confirmed here: `csak ugyan` and `úgyis`, at the expected places.

## Ciphertext as read (card lines)

    1  4x 1: 3 3. 1: 7,  8 1. 4, 1 8, 7 1' 8 !
    2  8 1  3. 1. 6,  3. 1: 5, 1: 3  5 0 4.  6, 1: 8
    3  1 3, 7.  5 1 7  8, 1. 5, 1' 6,  2, 1. 7  6, 1: 8
    4  5 1. 3, 1. 4, 7 0 5,  2, 1. 7  .1 4. 1. 6,  1 3, -
    5  6 1' 5,  7 1: 3 3. 1: 7,  7 2. 3, 5, 1: 7
    6  7. 2. 9 1: 6,  6, 1:  7 0 8 [blot] 3, 1 2, 3  1.  7. 1 -
    7  3. 1: 8 1: 8,  2. 6,  -1 4. 1 7,  1 3, 0 7
    8  8 1 6, 3 1 4,  (then clear text)

## Plaintext (Hungarian; [ ] = enciphered on the card)

The punctuation inside the cipher part is mine; the card has none there.

[Kedves Magitkám]!

[Mi van veled, hogy nem írsz? Hisz talán csak nem haragszol csak ugyan, írjál kedves, kérlek szépen, ne komorícsd a szívemet, én úgyis irok mindig] még többet ez után, mert mostanába nem érkeztem. Sz. A.

Emészt a vágy napról napra,
Mint sorvasztó-kór betegét;
Csókot hintani ajakadra,
Szívni édes leheletét.

II
Emészt a vágy... sivó, kopár,
Tikkadt mező a kebelem,
Perzsel a hő, a napsugár,
Égő vágyam: a szerelem.

III
S te szép leányka kaczagsz tán
Amig én érted epedek...
Oh, kaczagj, csak nem neked fáj
Hogyha én érted szenvedek!

mindnyájatokat csókollak.

Address: Tek. Szépreménnyü Sziber Margitka kisasszonynak, Szomolya, u. p. Bogács. Pencil note at the foot: 1915 XII 5.

## English translation

Dear Margitka! What is the matter with you, that you do not write? Surely you are not really angry, are you? Write, dear, I beg you, do not darken my heart; I will write anyway, always, and more from now on, because lately I have not had the time. Sz. A.

Longing consumes me day by day, / as a wasting disease consumes its patient; / to scatter kisses on your lips, / to breathe in your sweet breath.

II. Longing consumes me... barren, bare, / a parched field is my breast; / the heat scorches, the sunshine; / my burning longing: love.

III. And you, pretty girl, are perhaps laughing / while I pine for you... / Oh, laugh, it is not you who hurts / when I suffer for you!

I kiss you all.

## Slovak translation

Milá Margitka! Čo je s tebou, že nepíšeš? Veď sa azda naozaj nehneváš? Píš, milá, prosím ťa pekne, nezatemňuj mi srdce; ja aj tak píšem stále, a odteraz ešte viac, lebo v poslednom čase som nemal čas. Sz. A.

Túžba ma stravuje deň čo deň, / ako zhubná choroba svojho chorého; / sypať bozky na tvoje pery, / vdychovať tvoj sladký dych.

II. Túžba ma stravuje... pustá, holá, / vyprahnutá lúka je moja hruď; / páli horúčava, slnečný lúč; / moja horúca túžba: láska.

III. A ty, pekné dievča, sa azda smeješ, / kým ja za tebou prahnem... / Ó, smej sa, veď to nebolí teba, / keď ja pre teba trpím!

Bozkávam vás všetkých.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1152/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign, asserts that each decoded word matches the stated reading, and prints the full text with the address. The open text is hard-coded in the script, so the command reproduces only the decoding of the cipher signs. It reports 118 signs: 114 by the table and 4 by sense.

## Uncertainties

Cipher signs. Four signs are in `ODD` in `work/decode.py`. `Kedves`, `hisz` and `haragszol` are certain from the other letters. `komorícsd` is weaker: it is a restoration, the only word found to fit (item 4).

1. `Kedves`, first sign: an odd closed form with a crossbar, like a 4 with a bar or a retouched sign. It is not a clean `7` and not a clean `4`. Read as k by sense only (`4` = f would give `fedves`); the same word is written cleanly in line 5.
2. `hisz`: crossed 7 with no dot seen; the table gives `hik`. Sense wants `7.`.
3. `haragszol`: same case; the table gives `haragkol`. hcp-1174 has the same missing dot in `szerető`. Since the word division `hisz talán` rests on this reading, note that the signs alone give `hik talán`.
4. `komorícsd`, sign o: **a restoration.** A solid ink blot of about the size of a digit stands where the `0` should be, and the 8 before it is also heavily inked. The blot may be a correction. `komorít` (to make gloomy) is the one word I found to fit `komo?rícsd` and `a szívemet`; cs for ts is a phonetic spelling of the imperative `komorítsd`, and the sign `2,` is clean.

Other points of the text:

- `Magitkám`: the card really has no `3,`. This is the writer's slip for `Margitkám`, printed as written; the address has Margitka.
- `írjál` is split across a line end, with a hyphen at the margin (`1 3,` / `6 1' 5,`). The `6` has no comma and the `1'` has one high dot, so it is not `írnel`.
- `irok`, `csak ugyan`, `ez után`: spelled as on the card; the normal forms are `írok`, `csakugyan`, `ezután`.
- `mostanába nem érkeztem`: `nem érkeztem` taken as "I had no time", the usual sense of `ráér/érkezik` in this period and region. The translation of this phrase is an interpretation; the words are clear.
- `sorvasztó`: the script is cramped at sz, and the line is partly crossed by a stroke from the card's writing above; the word is read with sense support.
- `hintani`: the letter after t looks like a, and I print it as written; the normal form is `hinteni`. No dot is visible on the final i. The line `Csókot hintani ajakadra` is one syllable long as read (9 against 8 in the other lines), and `hinteni` would be too. The metre expects the short `hintni`, but the pixels show the longer form, so the reading stays.
- `leheletét`: an accent shows only on the last e; the line is heavily overwritten at `-helet-`. `betegét`/`leheletét` rhyme. The form is third person ("its/her breath"), while `ajakadra` in the line before is second person ("your lips"). Both translations print "your sweet breath", which normalises this; the shift may be forced by the rhyme.
- Line 4: the marks after `1` in `haragszol` (second sign) and `ugyan` (third sign) are elongated ticks, not round dots, and strictly could be taken for `1,` = b on hcp-1168. I read them as `1.` by judgement and sense (`hbragszol`, `ugybn` are not words); they stay among the 114 table reads.
- `Tikkadt`: the capital looks like a barred T or F. `Tikkadt` (parched) is taken from sense, with `mező`. `Fikkadt` is not a word.
- `sivó`: as written; compare `sivár` (barren). `sivó` is an old form.
- `mindnyájatokat`: the closing line runs along the bottom edge and is pale, and the accent on á is not certain. The same word stands on hcp-1157 and 1170; hcp-1169 has the same stem in another case, `mindnyájatoknak`.
- The `II`, `III` are stanza numbers, written small over the line ends. There is no `I`.
- The postmark on the stamps is not fully legible; I read only a day that may be 5. The date comes from the pencil note, `1915 XII 5`, whose hand I did not compare with the writer's. It agrees with the portal's file name.
- Whether the poem is printed elsewhere was not checked.

## Why I believe it is correct

- One fixed key from other cards decodes 114 of the 118 signs as written into running Hungarian. The other 4 are disclosed above. Three sit in words fixed by the surrounding signs; the fourth, in `komorícsd`, is a restoration from sense and shape. No value was created for this card.
- The enciphered sentence runs straight into the clear text: `én úgyis irok mindig` + `még többet ez után`.
- `.1` = u and `-1` = ú, each previously weakly attested, land on `ugyan` and `úgyis`.
- Complaint at silence, and a plea to write, fits the correspondence and the open verses on longing.
- Heading and signature Sz. A. agree with the sister cards hcp-1175, 1176, 1179.

## Response to review 1

Verdict REVISE. All six findings are addressed. The cipher reading is unchanged: no sign, value or decoded word changed. One open-text word changed.

1. `keblem` (major): fixed. I enlarged the crop (`review/work/keb.png`) and it shows k-e-b-e-l-e-m. The plaintext here and the verse in `work/decode.py` now print `kebelem`. The stanza then has 8 syllables per line and a full rhyme with `szerelem`. The translations do not change.
2. `hintani` and the metre: disclosed in Uncertainties. The crop (`review/work/hint.png`) still shows hint-a-n- with no dot on the final i, so I keep the reading as written and report the extra syllable.
3. "The words are certain": reworded in Uncertainties and in "Why I believe it is correct". `komorícsd` is now excepted.
4. Two `1.` marks: seen in `review/work/a3.png`, where the mark in `haragszol` is an elongated tick; one line added to Uncertainties. The count of 114 stays.
5. `leheletét`: the shift from third person to "your" in the translations is disclosed in Uncertainties. The translations themselves stay, with that note.
6. Citation: corrected. A check of the SOLUTION.md files shows `mindnyájatokat` on hcp-1157 and 1170, and `mindnyájatoknak` on hcp-1169.

Re-run after the fix: `python3 -I ciphers/hcp-1152/work/decode.py` gives hashes OK, 118 signs, 114 by table, 4 by sense, and prints `Tikkadt mező a kebelem,`.

The review's unverified points stand and go into the report as open: the postmark, the HistoCrypt article, a printed source of the poem, the sense of `nem érkeztem`, and `sivó`.
