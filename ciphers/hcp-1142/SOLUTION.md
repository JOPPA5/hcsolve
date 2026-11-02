# hcp-1142 solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal shows Not solved and attaches no solution or transcription. The transcription is my own, read from `work/hires/` at 2-5x. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. The key comes from the Mezőkövesd family cards (FINAL hcp-1174, 1178, 1179); see below for the signs taken from cards still in review.

## Cipher type and key

Hungarian text, all enciphered with a digit cipher except the two closing lines (register label: MASC). Each letter is one sign: a digit, or a digit with a mark. A comma, dot or colon is part of the sign. The word divisions in the transcription are mine.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2` | c | | `5.` | ly (l on FINAL cards) |
| `0,` | ö, ő | | `2,` | cs | | `6` | j |
| `1` | i, í | | `2.` | é | | `6,` | n |
| `1.` | a | | `3` | d | | `6.` | ny |
| `1:` | e | | `3,` | r | | `7` | k |
| `1'` (high dot) | á | | `3.` | v | | `7,` | s |
| `:1` (dots left) | ü | | `4` | f | | `7.` | sz |
| `1,` | b | | `4,` | g | | `8` | m |
| `9` | p | | `4.` | gy | | `8,` | t |
| `9,` | z | | `5` | h | | `8.` | ty |
| | | | `5,` | l | | | |

The card has 210 cipher signs, 30 distinct. All are in the table. Two signs carry an odd stroke and rest partly on sense (uncertainties 1 and 2).

Source of the values: the signs of the FINAL cards decode most of the card at once. Not on those tables, or tentative there: `2` = c, `4` = f, `4.` = gy, `6` = j, `6.` = ny, `8.` = ty. I got them from this card's own words (`piciny`, `felmegyek`, `nagyon`, `jó`, `kártyán`). The same values stand on sister cards hcp-1147, 1149, 1151, 1161 and 1170, which agree. The dot after g, n, t gives the palatal gy, ny, ty. hcp-1179 prints `8.` as t? in its text; `kártyán` here favours ty.

`5.` is a separate case and conflicts with the FINAL cards. hcp-1178 and 1179 give `5.` = l firmly (`a legszeb`, `csókollak`), and hcp-1149, 1166 and 1168 also use l. This card gives ly in my print, but it cannot separate the two: `amelynek` and `hely` are the normal spellings of what the writer could equally have spelled `amelnek` and `hel` (`melnek` stands on hcp-1160). The words are the same either way. So `5.` is l or ly, and a palatal rule is not proved for this sign.

## Plaintext (Hungarian; line breaks of verse are mine, punctuation and capitals mine)

Enciphered:

Kedves Margitkám!

A lapodat megkaptam, amelynek nagyon megörültem. Vasárnap ha jó üdő lesz, felmegyek.

Aszt mondja szívemnek mindenik verése:
Te vagy a világnak legszebb teremtése.

E kártyán piciny hely van, nem sokat írhatok.
Üdvözöllek, s aki voltam tenéked, az maradok.

Open text at the foot:

Számtalanszor csókollak mindanyájatokat (?),   (Sz. A.)

The foot word is printed as the card shows it, with its doubt; it is a form of `mindnyájatokat` (all of you). See uncertainty 3.

Address: Tek. / Szépreményü / Sziber Margitka / kisasszonynak / (Szomolya.) / u. p. Bogács / (Borsod m.)

Spellings as on the card: `aszt` (azt), `üdő` (idő, dialect form, as on hcp-1160, 1170), `mindenik` (each one), `tenéked` (neked, older form). The key does not separate o/ó, ö/ő, i/í, so `jó`, `üdő`, `szívemnek`, `írhatok` carry accents I supply. `vol-` / `tam` breaks over a line with a hyphen stroke on the card.

The horizontal rules above and below the Aszt mondja couplet set the verse off. Both pairs rhyme in the cipher: verése / teremtése, írhatok / maradok.

## English translation

Dear Margitka of mine! I received your card, which made me very glad. On Sunday, if the weather is good, I will come up.

Each of its beats says this to my heart:
You are the most beautiful creation in the world.

There is little room on this card, I cannot write much.
I greet you, and what I have been to you, that I will remain.

Countless times I kiss you all [`mindanyájatokat` (?), a form of `mindnyájatokat`]. (Sz. A.)

Address: To the Honourable, the promising Miss Margitka Sziber, (Szomolya), post office Bogács (Borsod county).

## Slovak translation

Drahá moja Margitka! Tvoj lístok som dostal a veľmi ma potešil. V nedeľu, ak bude pekné počasie, prídem hore.

Každý jeho úder hovorí môjmu srdcu:
Ty si najkrajšie stvorenie sveta.

Na tomto lístku je málo miesta, veľa napísať nemôžem.
Pozdravujem ťa, a čím som ti bol, tým ostanem.

Nespočetnekrát vás všetkých bozkávam [`mindanyájatokat` (?), tvar slova `mindnyájatokat`]. (Sz. A.)

Adresa: Veľactenej, nádejnej slečne Margitke Sziberovej, (Szomolya), pošta Bogács (župa Borsod).

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1142/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription.txt` by the key, asserts that each decoded line matches the stated reading, and prints the open lines and the address. The open lines are hard-coded in the script, so only the cipher is reproduced.

## Uncertainties

1. Last sign of `maradok` (end of the last cipher line): a 7 with a wedge below it (`work/crops/L14end.png`). The graphic evidence is open. The right arm of the wedge runs in the direction of this writer's commas and stands at the foot of the 7, where a comma stands, which would give `7,` = s. A second arm from the left makes a V, which a comma does not have. `maradok` stands on sense alone: `marados` is no word here. The rhyme with `írhatok` points the same way, but that is the same argument and not extra evidence.
2. `8.` in `kártyán`: the dot has a long tail running under the next sign (`work/crops/ty.png`). I take it as a dot; a plain `8` (m) gives no word, and no comma is present for `8,`. The word fixes it, so this rests partly on sense.
3. `mindanyájatokat` (?) (open text, second line of the foot, bottom edge): the one unsure word of the card. `mind` and `-tokat` are clear. After `mind` the strokes are a clear `a`, `n` and a descender letter, so the card is not spelled `mindny...`. Then come an a-like letter with a blotted right side, an open c-like letter under an acute, a second descender with a tick above and to the right, an o/a-like letter, and a short i/u stroke before `-tokat` (`work/crops/word1.png`, `word2.png`, `word-mid.png`). I cannot match every stroke, and there are one or two strokes more than `mindanyájatokat` needs. The sense `all of you` is secure for three reasons: `-tokat` is the second-person plural accusative ending, `csókollak` needs a second-person object, and the phrase stands on sister cards (`Számtalanszor csókollak mindnyájatokat` on hcp-1172, which has no marker yet; `Mindnyájatokat csókollak` on FINAL hcp-1152, 1154, 1157). It is one word, and the rest of the card reads.
4. `Sz. A.`: signature in a loop (`work/crops/sig.png`), same form as on hcp-1175, 1176, 1178. The A is the likely capital; hcp-1178 discussed K as an alternative. Family cards sign the name Árpád in cipher.
5. The couplet may be a quotation or a popular verse. I looked for no source. `mindenik verése` is read as "each of its beats", with the heart as the implied owner; "szívemnek" could also be the possessor ("each beat of my heart says this").
6. Date: not established. The card has no written date. The purple round stamp shows `BORSOD`, `KÖ…` and the year 1906. Inverted letters on its lower arc look like `...GYE`, so it may be a county seal (`BORSOD VÁRMEGYE ...`), and that would make 1906 a seal year and not a posting date. The portal filename `cpc_1906--` may come from it. The grey postmark is covered by the stamp; no place or date can be made out. The family's dated cards are 1915-16. So I give no date.
7. The stamp's text between `BORSOD` and the year is not fully legible and adds nothing.
8. The picture side has only a printed tinted photograph and publisher's marks; no writing.

## Why I believe it is correct

- 210 signs decode with one fixed key to continuous, grammatical Hungarian, with no gap and no unread sign.
- The verse lines rhyme. verése / teremtése is independent support, since no key value or reading came from it. írhatok / maradok is weaker support, since `maradok` itself rests on sense (uncertainty 1), though no key value was set from it.
- The text fits the correspondence: the same recipient, address and closing signature; the same hand; `aszt` and `üdő` are the writer's spellings on sister cards; `felmegyek` and a Sunday visit match hcp-1174.
- The opening `Kedves Margitkám`, `megkaptam`, `lapodat` use only FINAL-card values and read at once.
- No letter comes from a sister card's words. The open foot word is the one word supported by them, and it is disclosed.

## Response to review 1 (verdict REVISE)

1. Foot word: fixed. I reread it on the review crops and on a new enhanced crop (`work/crops/word-mid.png`, `work/crop5.py`). The reviewer is right: `a`, `n`, descender after `mind`. The plaintext, both translations' notes and `work/decode.py` now print `mindanyájatokat (?)`, glossed as a form of `mindnyájatokat`. Uncertainty 3 is rewritten, and it says that the strokes are one or two more than this form needs. It stays one word with a secure sense, so the card remains complete.
2. `5.` = ly: fixed. The key section now states the conflict with hcp-1178, 1179 (and 1149, 1166, 1168), says that `amelynek` / `amelnek` and `hely` / `hel` are the same words, and drops `5.` from the palatal pattern. The table marks it. The print stays `amelynek`, `hely`, with no change to the words.
3. Independence claims: fixed. Only verése / teremtése now counts as independent support. The sister-card status is corrected from current markers: hcp-1152, 1154, 1157, 1160, 1161, 1170 are FINAL, hcp-1147, 1149, 1151 are REVIEWED1, and hcp-1172 has no marker.
4. Last sign of `maradok`: agreed. Uncertainty 1 no longer leans towards a flourish; it says that the wedge is open and that the word stands on sense.
5. Date and seal: the seal note is added to uncertainty 6. Still no date.

The transcription and key values did not change. `python3 -I ciphers/hcp-1142/work/decode.py` was rerun after the edits: hashes OK, 210 signs, 30 distinct, lines match.
