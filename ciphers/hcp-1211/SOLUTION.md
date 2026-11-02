# HCP1211 — Feri to Jolánka Tóth: thanks for her lines, "the forget-me-not blooms only for me"

**Status: complete reading, corrected after review 1 (see the last section).** Solver: Claude Opus 5.5, 2026-11-02. There is no earlier work on this number. No published solution was found; the portal shows Not solved and attaches no transcription or solution. The transcription is my own, made from enlarged crops of the un-converted scan `work/hires/*_adr.jpg`. It is not blind: I knew the family key and read with word sense in mind (see Uncertainties).

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the Jolánka postcard family). The key was transferred from HCP1216 / 1212 and tested on this card; one sign form differs, see below. The picture side has no writing. The address and the note under the stamp are in plain hand.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark with dot below | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma | t |
| short + long stroke joined | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short tick | h / p | crossed diagonal | z |
| C-shape | g (this card) | dotted crossed curve | i | inverted T | j |

Joined forms: C+y = gy, two strokes+y = ny, wave+y = ly. Accents are marks over the base sign and are not consistent.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1211/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (322 tokens, one per written sign, all 17 rows) with the key, prints the literal row text, and prints the editorial `work/normalized.txt`. The computer decodes the tokens; the tokens themselves are a manual reading of the pixels.

## Literal decipherment (as printed; the h/p sign is shown as h)

```
01 édesegyetlenremé            10 rozsaésszivébenane
02 nyemsoraitköszönet          11 felejcs[is]csaknekemvirul
03 telmegkahtammelyavar        12 {blot}onszivevirágaésneher
04 vavartidöabelolmeg          13 vadjonelsohalegyen
05 érkezetédesjolánkam         14 asorbarmilymosto
06 aboldogsagtolalig           15 haazenedesjolánkámat
07 tudokválaszolai             16 elfeledninembirnám
08 széhszemébennyilik          17 sohaistenveleédesemaviszolatasraferi
09 énreszemrealeg{O}szebb
```

## Hungarian (normalized)

Édes egyetlen reményem! Sorait köszönettel megkaptam, mely a várva várt időn belől megérkezet[t]. Édes Jolánkám, a boldogságtól alig tudok válaszolni. Szép szemében nyílik én részemre a legszebb rózsa, és szívében a nefelejcs is csak nekem virul. Ön szíve virága, és ne hervadjon el soha, legyen a sor[s] bár mily mostoha, az én édes Jolánkámat elfeledni nem bírnám soha. Isten vele, édesem, a visz[ont]látásra! Feri

Under the stamp, plain hand, rotated: Csókolom a csókra való kis száját. Feri

Address, plain hand: Szépreményű Tóth Jolánka kisaszonynak [sic] sz. r. t. (abbreviation as seen), Jász-Árokszállás, Alszög

## English

My sweet only hope! I received your lines with thanks; they arrived within the long-awaited time. My sweet Jolánka, I can hardly answer for happiness. In your beautiful eyes the loveliest rose blooms for me, and in your heart even the forget-me-not blooms only for me. The flower of your heart, may it never wither, however cruel fate may be, I could never forget my sweet Jolánka. Farewell, my darling, until we meet again! Feri

Under the stamp: I kiss your little mouth, made for kissing. Feri

## Slovak

Moja sladká jediná nádej! Vaše riadky som s vďakou dostal, prišli v očakávanom čase. Sladká moja Jolánka, od šťastia sotva dokážem odpovedať. Vo Vašich krásnych očiach pre mňa kvitne najkrajšia ruža a vo Vašom srdci aj nezábudka kvitne len pre mňa. Kvet Vášho srdca, nech nikdy nezvädne, nech je osud akokoľvek krutý, svoju sladkú Jolánku by som nikdy nedokázal zabudnúť. S Bohom, drahá, dovidenia! Feri

Pod známkou: Bozkávam Vaše malé ústa stvorené na bozkávanie. Feri

## Uncertainties

1. **Rows 4 and 7, two bars read as n.** Row 4 literally gives *idő a belől*, row 7 *válaszola* + i. Both are normalized with n (*időn belől*, *válaszolni*). The two bars are clear on the card, so these two n are emendations by word sense: I take them as the same slip, horizontal two-bar for vertical two-stroke. *belől* is the writer's form of *belül*. The last sign of row 7 has its dot, above and to the right, with a separate full stop after it.
2. **Row 12, first sign.** An ink blot stands at the left edge, in the first-sign position, then a plain cursive o + n. The o is on the card; only its two dots are supplied, and they are absent, not hidden. I read *Ön*, and the open question is whether the blot covers a letter before *on*. Neither solver nor reviewer can settle that from the pixels. This is the weakest point, one uncertain word in a card that otherwise reads. The sentence *Ön szíve virága* is also loose; "[You are] the flower of the heart" is possible, and *szívem* ("my heart") is not what the signs give.
3. **The g sign.** Family tables list "left bowl = c" and "open loop with descender = g". On this card a large C-shape serves as g in *meg*, *boldogság*, *alig*, *legszebb*, *virága* and in joined gy, and c occurs only inside cs. On HCP1216 the g of *hogy* is a smaller angular form, plausibly the same sign written differently. The value rests on word sense across those words, and I did not do a sign-by-sign comparison with the sister cards.
4. **Over-inked signs.** Row 9 has a filled ring between *leg* and *szebb*, left out as a false start or correction. Row 6 the g of *-ság-* is a filled blob joined to the t, row 6 last g is filled, row 11 the n of *nekem* is merged by a blot, row 16 the f of *elfeledni* is a star-shaped blot under the printed "Série 2285", row 7 the u of *tudok* and row 17 the z of *viszo-* are over-inked. All are read by shape plus word sense. Row 12 *virága* has a blot on the á.
5. **h/p by word sense**: *megkaptam*, *szép* (p); *hervadjon*, *soha*, *mostoha* (h). **d/n** were told apart by the joined short + long form against two equal strokes; d in row 13 *hervadjon* and row 16 *elfeledni* also rests on word sense. **u/z:** on this card u and z are hard to tell apart by shape (a crossing diagonal with a tail in both). The two u tokens, *tudok* and *virul*, rest on word sense.
6. **Row 3:** a separate short bar stands above the m of *meg*, not read as a letter. Row 17 row-end: the last sign of *Feri* is thick and its dot sits to the upper right.
7. **Writer's spellings:** *érkezet* (a dot follows it; one t), *sor* for *sors* (*sor* can itself mean lot, so the bracket is optional), *viszolátásra* (nt omitted), and accents mostly absent. Row 11 has the word *is* in plain Latin letters in the middle of the cipher.
8. **Plain text.** Under the stamp the second line is cramped; *csókra va-ló* is read from the cursive and the a of *csókra* looks like o. In the address the writer has *kisaszonynak* with one s, and the abbreviation after it is *sz. r. t.* followed by dots; it is reported literally and not expanded (a sister card, HCP1225, has *s. k.* at that place). *Alszög* is read from the cursive and taken as a part of Jászárokszállás, not verified.
9. **Date and sender.** The portal file name gives 1912-02-10. The first mark shows ...ÁROKSZÁ..., the year remains 912, a month beginning with F, and the day 10, consistent with that date. A second mark begins GYÖN…, possibly Gyöngyös, which remains a guess. Neither mark is fully legible. The sender signs Feri, as on the family cards; no further identification is claimed.

## Why it is correct

The family key gives connected Hungarian across all 17 rows without any per-row change. The reading contains long specific sequences that no noise would give: *köszönettel megkaptam*, *várva várt*, *boldogságtól alig tudok*, *legszebb rózsa*, *nefelejcs*, *ne hervadjon el soha*, *bár mily mostoha*, *elfeledni nem bírnám*, *Isten vele*, and the name *Jolánkám* twice with the same signs. Words run across row breaks correctly (*remé-nyem*, *köszönet-tel*, *vár-va*, *ne-felejcs*, *her-vadjon*, *mosto-ha*). The sender and recipient match the family; the rose and forget-me-not imagery fits Feri's verses on the sister cards.

## Response to review 1

Verdict REVISE. All seven findings were checked on the reviewer's crops and accepted. No key value and no word of the sense changed; the corrections remove one false word and fix one sign. After them, `python3 -I ciphers/hcp-1211/work/decode.py` prints four OK lines and 322 signs, and its rows match the literal block above.

1. **Inserted *ha* (major): fixed.** Row 14 ends *mosto* plus a hyphen stroke, and row 15 begins *ha az én*. The only *ha* is the end of *mosto-ha*. It is gone from `work/normalized.txt` and the Hungarian block, old uncertainty 3 is deleted, and "since" / "lebo" are dropped from the translations. The sentence now reads cleanly and rhymes: *bár mily mostoha, az én édes Jolánkámat elfeledni nem bírnám soha.*
2. **Row 15 token (minor): fixed.** Only two bars stand between the m and the t, so the token is `=`, not `E`. One addition of mine: the comma-shaped mark over the bars after the k in this word (`review/work/z_row15end.jpg`) is an acute, so that token is now `='`. Row 15 prints *haazenedesjolánkámat*, and the normalization no longer changes any letter of the name.
3. **Row 7 last sign (minor): fixed.** The dot is there, above and to the right, so the token `I_` is now `I` (removed from `decode.py` and the ledger legend) and uncertainty 1 is corrected. No other token used it.
4. **Row 12 (minor): fixed in wording.** *[Ö]n* becomes *Ön*, and uncertainty 2 says that the o is present, its dots are supplied, and the open question is a possible letter under the blot. That question stays open.
5. **Address (minor): fixed.** The address now reads *kisaszonynak* [sic] *sz. r. t.*, confirmed on `review/work/addr.jpg`. It stays unexpanded.
6. **u against z (minor): added** to the word-sense calls, uncertainty 5.
7. **Date note (minor): added** to uncertainty 9, with what `review/work/z_pm.jpg` shows.
