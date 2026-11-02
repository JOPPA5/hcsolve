# hcp-1169 solution (round 1, corrected after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal attaches no solution or transcription. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. I started from the key of FINAL sister cards hcp-1174, 1178 and 1179 and extended it on this card. No transcription existed: mine is `work/transcription.txt`, read from enlarged crops of the hires address side.

## Cipher type and key

Register label: MASC. Hungarian, monoalphabetic digit cipher. Each letter is one sign, a digit alone or a digit with a mark; the mark is part of the sign. No word division. The whole message is enciphered except the two words `Most pedig`; a New Year wish below it is in clear.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2.` | é | | `5.` | ly |
| `0,` | ö, ő | | `3` | d | | `6` | j |
| `1` | i, í | | `3,` | r | | `6,` | n |
| `1.` | a | | `3.` | v | | `7` | k |
| `1:` | e | | `4` | f | | `7,` | s |
| `1'` (one high dot) | á | | `4,` | g | | `7.` | sz |
| `:1` (dots left) | ü, ű, ú, u | | `4.` | gy | | `8` | m |
| `1,` | b | | `5` | h | | `8,` | t |
| `2,` | cs | | `5,` | l | | `9` / `9,` | p / z |

New against the sister tables: `4` f, `4.` gy, `5.` ly, `6` j. They were fixed here by `fogsz`, `fehér`; `hogy`, `nagyon`, `gyenge`; `oly`, `melyet`; `jó`, `majd`. hcp-1178 has `5.` for plain l in `csókollak`, while here it is only ly; that is a difference, not a conflict I can resolve from this card.

271 cipher signs, 269 by the table, 2 by sense.

## Plaintext (Hungarian; [ ] = enciphered; spelling as on the card)

[Drága jó Margitkám!]

[Elhozta a jó Isten az újévet is, melyet már oly nagyon vártam, hogy mégis közelebb legyek a szabadulás ideéhez, no de majd elérkezik az is, akor esik le szívemről egy malomkő és hejébe te fogsz rajta fügni boldogan mint gyenge szívű fehér galamb a fészkében midőn tojássait költi.]

Most pedig [üdvözölve és csókolva téged) hű kedvessed Árpád]

Open note: Boldog ujévet kivánok mindnyájatoknak még a kis haragos Mariskónak is nemigen megfek[t/f]el(?) 1915. XII/29 Mezőkövesd

Address, as written: Tek. / Szépreményü / Sziber Margitka / kisasszonynak / Szomolya) Bogács- / (Borsod m[?] u. p. The stroke after `m` is one tall crossed stroke with a long descender and is not resolved; `u. p.` is `utolsó posta`, last post office, the form hcp-1174 also has. Postmark MEZŐKÖVESD. Picture side, printed: Boldog ujévet! (no accent on the u)

Non-standard spellings, normal form: `ideéhez` = idejéhez, `akor` = akkor, `hejébe` = helyébe, `fügni` = függni, `tojássait` = tojásait, `kedvessed` = kedvesed. Punctuation in the cipher part is mine, except `!` and `)`.

## English translation

Dear good Margitka! The good Lord has brought the New Year too, which I have so longed for, so that I may yet be closer to the time of my release. Well, that too will come; then a millstone will fall from my heart, and in its place you will hang on it, happy as a gentle-hearted white dove in its nest when it hatches its eggs.

And now, greeting and kissing you) your faithful sweetheart Árpád

I wish a happy New Year to all of you, even to little cross Mariska, [nemigen megfek[t/f]el: "not much" plus a word not understood]. 29 December 1915, Mezőkövesd.

## Slovak translation

Drahá dobrá Margitka! Dobrý Boh priniesol aj Nový rok, na ktorý som tak veľmi čakal, aby som bol predsa bližšie k času svojho oslobodenia. Nuž ale príde aj to; vtedy mi spadne zo srdca mlynský kameň a na jeho miesto budeš na ňom visieť ty, šťastná ako nežná biela holubica v hniezde, keď sedí na vajíčkach.

A teraz ťa pozdravujem a bozkávam) tvoj verný milý Árpád

Želám šťastný Nový rok vám všetkým, aj malej nahnevanej Mariške, [nemigen megfek[t/f]el: „nie veľmi" a neporozumené slovo]. 29. decembra 1915, Mezőkövesd.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1169/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign of `work/transcription.txt`, asserts that the result equals the stated reading letter by letter, prints the counts and the full text. The word divisions in the transcription are mine; the accented, punctuated text and the open parts are hard-coded in the script.

## Uncertainties

Cipher signs:

1. `esik`: the 1 has a tiny dot beside it (`work/crops/r3d.png`). Taken literally as `1'` it gives `esák`; I read a plain 1 by sense. The phrase `esik le szívemről egy malomkő` is idiomatic.
2. `szívű` (row beginning `6, 1 1, 0 5,`, last sign; `review/work/crops/sz7.jpg`): the mark under the 7 has a head and a short tail. In shape it is a short comma, unlike the round dots of `7.` in `szívemről` and `fészkében`. The literal reading is `7,` = `sívű`. `sz` is a correction by word sense, a slip of the writer or a shortened mark.
3. `á` and `e`: `1'` and `1:` are close. Some `1'` have a faint speck low down (for example in `Drága`), and a few `1:` have a dash on top. In `Drága`, `már`, `vártam`, `tojássait`, `Árpád`, `Margitkám` I chose á because the word requires it. In `galamb` the first vowel shows a faint brown top mark beside a large low dot (`work/crops/r5b.png`); I take it as `1.` with a stain, giving a.
4. `szabadulás`: `:1` has one left dot, standing next to the 3. One-dot `:1` is a real variant, since `újévet` shows it too (`review/work/crops/uj.jpg`), while `fügni`, `-vű`, `hű`, `üdvözölve` show two. The alternative split `3.` + `1` would give `szabaviás`-like nonsense. The `á` dot is partly behind the printed red divider.
5. `Árpád`: the final 3 has a long tail to the right, which I take as a closing flourish, not a comma (`3,` would give r). The name agrees with hcp-1174.
6. `téged)`: a bracket-like stroke with a short stroke beside it. I treat it as punctuation; the short stroke could be a comma of the 3 (`téger`), which is not a word.
7. The doubled s in `tojássait` and `kedvessed` is on the card. In `kedvessed` it falls at a line break. Other spellings under Plaintext are as written and are not corrected in the decoding.
8. The hyphens at line ends also stand after complete words (`szabadulás`, `le`, `és`); they are line fillers.

Open text:

- `Most pedig`: the d is looped and could at first sight be `ol`; `Most pedig` is by sense and fits what follows.
- `megfek[t/f]el` (`review/work/crops/megf.jpg`): the letters are m-e-g-f-e-k, then a long crossed stroke, then e-l, with no visible accent. The crossed stroke goes below the line like the first f, while the t of `atoknak` stands on the line, so `megfekfel` is at least as good a letter reading as `megfektel`. I cannot settle the meaning. `megfektél` ("you lay down, fell ill"), a dialect past form, is a guess that rests on the t, and I do not know how it connects with `Mariskónak is`. Reading j for the k (`megfejtel`) is out: the letter has an ascender and no descender. This is the one un-understood word on the card. It is left untranslated; the reviewer should decide whether this leaves a clause unread.
- `Mariskónak`: after the k there is an o and then a second small vowel body under an arch, before `nak` (`review/work/crops/kona.jpg`), written `kóo`-like, perhaps a correction or doubled vowel. The name is certain.
- `mindnyájatoknak`: the j stands at the margin with a hyphen and `atoknak` is partly overwritten at its t/o.
- Year: `1915` has an overwritten third digit. The portal file name gives 1915-12-29, and a New Year card fits. The day and month of the postmark are lost, but below the wheel `9 1` and a hook that fits 5 are visible (`review/work/crops/stamp.jpg`), which supports the year.
- Light grey pencil strokes over the digit panel are later marks. A ruled line separates the cipher body from the closing, another crosses the open note. Neither affects the letters.

`Mezőkövesd` is written over a slip at its start (the z over another letter); the place is certain.

## Why I believe it is correct

- One fixed table turns all but 2 of 271 signs into continuous, grammatical, idiomatic Hungarian, without forcing word divisions: a single sentence of over 45 words holding the idiom `esik le szívemről egy malomkő` and the extended dove simile.
- Key values taken from hcp-1174 and 1179 (for example `2, 0 7 0 5,` = csókol-, `7 1: 3 3. 1: 7,` = kedves, `1' 3, 9 1' 3` = Árpád) work here unchanged. Árpád and the addressee match that correspondence.
- Of the four new values, `4`, `4.` and `6` are each carried by several independent words; `5.` by two (`melyet`, `oly`).
- `újévet`, `Boldog ujévet` in clear on the same card, the printed `Boldog ujévet!` and the date 29 December all agree. `szabadulás` fits a writer waiting for release, though the card does not say from what, and the translation `release` leaves that open.

## Response to review 1

Verdict ACCEPT, eight minor findings. I rechecked each against the reviewer's crops. No decoded letter changed; `work/decode.py` was re-run and passes (271 signs, 2 by sense).

1. Address: fixed. `borsod.jpg` and `addr.jpg` show `Borsod m`, a tall crossed stroke, then `u p.`, and `Szomolya)` with a bracket. `Szépreményü` has a two-dot ü. The address in this file and in `decode.py` now follows the card.
2. Printed greeting: fixed to `Boldog ujévet!`.
3. `szívű`: agreed and fixed. `sz7.jpg` shows a short comma form, so the uncertainty now says literal `sívű`, `sz` by correction. The `~` token is kept and its comment changed. The citation now points to that crop.
4. `megfektel`: agreed and fixed. Plaintext now prints `megfek[t/f]el`; the note states that `megfektél` rests on the t and that j for k is excluded.
5. `Mariskónak`: agreed and fixed. `kona.jpg` shows two vowel bodies; noted as written.
6. One-dot `:1`: agreed and fixed. `uj.jpg` shows it; uncertainty 4 lists `újévet`.
7. Postmark: agreed and added. The lower arc shows `9 1` and a hook that fits 5; day and month stay unread.
8. `5.`: agreed and fixed; the reasons section now says two words.

The reviewer's rulings stand: `megfek[t/f]el` is the one un-understood word and the card counts as complete with it marked; `esik`, `Árpád` and `téged)` stay as sense calls. The HistoCrypt article remains unchecked.
