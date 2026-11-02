# HCP 1154 (cpc_1915-11-29_HU_Mezokovesd_HU_Szomolya_szomolya-07): a hurt reproach in digits to Margitka Sziber

Human solver: Tomáš Pavuk

**Status: all 116 cipher signs are deciphered (115 as written, 1 by word sense); independent review 1 verdict ACCEPT, cipher reading unchanged.** The only unread word on the card is one the writer himself inked out. Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1154 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1154), portal name cpc_1915-11-29_HU_Mezokovesd_HU_Szomolya_szomolya-07, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was **not checked** for this card, so it is not known whether it treats it. The reading here was made from the card. There was no earlier work on this number.

The card is a picture postcard showing a couple on a birch bench, with no writing on the picture side. It is addressed to "Tek. Szépreményű Sziber Margitka kisasszonynak, Szomolya, u. p. Bogács", to the promising young lady Margitka Sziber, in the village of Szomolya in north-east Hungary. A handwritten note at the top right gives 1915 XI/29. The postmark is Mezőkövesd, 915 NOV 2-, with the last digit of the day lost at the edge of the stamp. The card is signed Sz. A. Its message is open Hungarian. The heading and one passage are in digits, and a four-line verse and a closing greeting stand in clear under the signature.

The card belongs to the Mezőkövesd family, wartime cards of 1915 and 1916 to the same young woman. Hcp-1140 is also signed Sz. A. in clear, and hcp-1174 signs Árpád in cipher in the same correspondence, so Árpád is a likely name for the writer, though this card does not establish it.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The cipher rows were read sign by sign from enlarged crops of the un-converted high-resolution scan. No OCR was used. The key was transferred from the finished cards hcp-1174, 1178 and 1179, and no value was fitted to this card. Four signs missing from those three tables were taken from other cards of the family, and each gives a word here at once.

First readings such as `haragudnel` and `tegnep` were corrected at 5x: the 1 after the n of haragudnál has one high dot only, which makes it á, and the 1 in tegnap has one low dot only, which makes it a. The word division is the solver's, because the cipher has none.

Reproduction, from the repository root:

```text
python3 -I ciphers/hcp-1154/work/decode.py
```

It checks the hashes of the scans, decodes work/transcription.txt, asserts the stated reading and prints the card. The clear text is typed into the script, so the command reproduces only the cipher part.

## Key

Monoalphabetic substitution with no word division. A digit together with its mark is one letter. Only signs that occur on this card are listed: 24 distinct signs in 116 tokens. In this hand the 7 is always crossed, and the 5 carries a short top stroke.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| 0 | o | 3 | d | 6, | n |
| 1 | i | 3, | r | 7 | k |
| 1. | a | 3. | v | 7, | s |
| 1: | e | 4 | f | 7. | sz |
| 1' (high dot) | á | 4, | g | 8 | m |
| .1 (dot at left) | u | 4. | gy | 8, | t |
| 2. | é | 5 | h | 9 | p |
| 6 | j | 5, | l | 9, | z |

Of the 116 tokens, 110 use the table of hcp-1174, 1178 and 1179, 5 use the four signs from the wider family (`4`, `4.` twice, `.1`, `6`; all four are on the finished cards hcp-1163 and 1168), and 1 is read by sense (see below).

## Plaintext

Ciphertext by card row, with the solver's word division (`|`) and the row-end hyphens of the card. The one sign read against its written form is shown as `3.[r]`.

```text
7 1: 3 3. 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8 !
7 1: 3 3. 1: 7,
8 1. 3, 4, 1 8, 7 1' 8 | 6, 1: 8 | 5 1 7. 1: 8
5 0 4. | 6, 1: 8 | 5 1. 3, 1. 4, .1 3 6, 1' 5, | 6, 1:
1 7, | 8, 1. 4, 1. 3 | 8 1: 3.[r] 8, | 8, 1: 4, 6, 1. 9 | 2. 7. -
3, 1: | 3. 1: 8, 8, 1: 8 | 1. 7. 8, | 9 1: 3 1 4, | 1: 5, -
7, 1: | 7 2. 9 9, 1: 5, 1: 3 | 5 0 4. | 4 1' 6 | 1: 9,
6, 1: 7 1: 8
```

Hungarian. Square brackets show what is enciphered on the card; inside them, me[r]t marks the one sign not read as written.

```text
[Kedves Margitkám]!

Szerencsésen haza értem, épen a hat órát ütötte a toronyóra
mikor a piacra értem nagyon hideg volt már talán nem is igen
megyek <one deleted word> Karácsonyig, de más-különben nem is
tudnám megálni, hogy ne menjek.
[Kedves Margitkám nem hiszem hogy nem haragudnál ne is tagad
me[r]t tegnap észre vettem aszt pedig el se képzeled hogy fáj
ez nekem.] Sz. A.

Hiába jártam utánad
Reményeim mind elfogytak.
Olyan lett a szívem mint a
jégvirágos téli ablak.
Mindnyájatokat csókollak
```

The cipher passage in normal spelling: Kedves Margitkám, nem hiszem, hogy nem haragudnál, ne is tagadd, mert tegnap észrevettem, azt pedig el se képzeled, hogy fáj ez nekem.

English:

```text
[Dear Margitka]!

I got home safely; the tower clock was just striking six when
I reached the marketplace. It was very cold already. Perhaps I
will hardly go <deleted word> until Christmas, but otherwise I
could not keep from going.
[Dear Margitka, I do not believe you would not be angry, do not
even deny it, because I noticed it yesterday, and you cannot
even imagine how this hurts me.] Sz. A.

In vain I went after you,
all my hopes have run out.
My heart has become like
a frost-flowered winter window.
I kiss you all.
```

Slovak:

```text
[Milá Margitka]!

Šťastne som došiel domov, vežové hodiny práve odbíjali šiestu,
keď som prišiel na námestie. Bola už veľká zima. Možno ani veľmi
nepôjdem <škrtnuté slovo> do Vianoc, ale inak by som ani nevydržal
nejsť.
[Milá Margitka, neverím, že by si sa nehnevala, ani to nepopieraj,
lebo včera som si to všimol, a ani si nevieš predstaviť, ako ma to
bolí.] Sz. A.

Márne som za tebou chodil,
všetky moje nádeje sa minuli.
Moje srdce je ako
zimné okno s ľadovými kvetmi.
Bozkávam vás všetkých.
```

## What remains uncertain

**Cipher signs.**

- `mert`: the third sign is written `3.`, a short slanted dot of the same form as in `kedves`, and every comma in this hand has a long tail. By the key the card has `mevt`. This is taken as a writer's slip for mert, by word sense only. It is the one sign not read as written.

![The signs 3. 8, of mert, followed by 8, 1: 4, 6 of tegnap: the mark after the 3 is a short dot, the commas on the 8s have long tails (review/work/crops/z_3b.png)](../review/work/crops/z_3b.png)

- The four signs from the wider family are not on hcp-1174, 1178 or 1179. Here each stands in a sure word: `4.` in hogy (twice), `.1` in haragudnál, `4` and `6` in fáj. `6` occurs once and shows no comma, and `fáj ez nekem` depends on that.
- `ne is tagad` rests on the solver's word division. The alternative `nél ne` fails, because the high dot gives á.

**Writer's spellings, kept as written.** `tagad` for tagadd, `aszt` for azt (`7.` is clearly written, not `9,`), `megálni` for megállni, `épen`, and row-end hyphens in `ész-re`, `el-se` (el se is two words) and `más-különben` (one word).

**Open text.**

- One word after `megyek` was inked over by the writer. A tall opening stroke with a small hook above it, an accent near the end and a small closed end loop survive. It is unread, and the sentence reads without it.

![The deleted word (review/work/crops/del.png)](../review/work/crops/del.png)

- `már` stands without punctuation in `nagyon hideg volt már talán nem is igen megyek`. It can end the first clause (it was already very cold) or open the second (now perhaps I will hardly go). The translations take the first, and the sense changes little.
- `Mindnyájatokat`: the letters look like `nyoisat` here, and the word is read by sense, with no rival. `talán` has this writer's a, which looks like `oi`.
- A long stroke stands directly under `téli`. It looks like the writer's underline; the word is secure.
- A small mark after `csókollak` at the card's edge has no letter value claimed.

**Context.** The last digit of the postmark day is lost, so the day 29 rests on the handwritten note alone. That note is blue on the scan, close to the ink, and its medium cannot be told. Whether Sz. A. signs only the cipher passage or the whole card is open, since the signature stands at the end of the last cipher row above a ruled line and the verse follows below it. Who Sz. A. is does not follow from this card.

## Why the solution is believed correct

A key from other cards, with nothing fitted here, decodes 115 of 116 signs as written into a continuous, grammatical Hungarian passage that follows on from the open text. `Kedves Margitkám` appears twice as the same sign strings. The sense fits: he got home, he may not come until Christmas, then he accuses her of being angry, and the verse in clear has the same hurt tone. Enciphering only the painful personal passage suits the habit of the family, which hides tender words on an open card.

## Review and what changed

An independent reviewer, a separate Claude Opus 5.5 agent, ran the command, read the heading and all seven cipher rows itself from the high-resolution scan before comparing, and decoded them with its own script. Its reading agreed token for token: 116 signs, 24 distinct. It checked the disputed signs enlarged, the key against the sister cards, the clear text, the address and the translations. Its verdict was ACCEPT, with five minor findings:

1. The "very short comma" argument for `mert` did not hold. The sign is a dot, the card has `mevt`, and it is now called a slip and marked me[r]t.
2. `más különben` is now given as one word split at a row end.
3. The stroke under `téli` is now disclosed.
4. `már` had been dropped in the English. It is now kept in both translations, in the same place, with the ambiguity stated.
5. The description of the deleted word now names the end loop and the hook.

The solver also dropped the word pencil for the date note, after the reviewer saw that it is blue on the scan, and brought the status of the sister cards up to date. No sign and no decoded letter changed.
