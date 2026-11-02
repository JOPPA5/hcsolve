# hcp-1167 solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The transcription is my own, made from `work/hires/`. The portal lists the card as Not solved with no solution attached. I did not check the HistoCrypt article the portal links, so I cannot say whether it discusses this card. No published solution turned up.

## Card

Picture postcard (a couple embracing, no writing on the picture side), Mezőkövesd, 1916. III/11., to Sziber Margitka at Szomolya. The left side is almost entirely cipher: 18 lines of figures. Below them are two lines of open greeting and the open place and date. Same correspondence as hcp-1174, 1165 and 1178.

## Cipher type and key

Register label: MASC. A digit-plus-mark monoalphabetic cipher, starting from the key of hcp-1174, 1179 and 1165. The mark belongs to the sign, so `3` is d, `3,` is r and `3.` is v. Marks to the left of a 1 are part of the sign too. The card has visible and fairly regular gaps, but they do not settle every boundary, so the final word division is mine.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2.` | é | | `6` | j |
| `0,` | ö, ő | | `3` | d | | `6,` | n |
| `1` | i, í | | `3,` | r | | `6.` | ny |
| `1.` | a | | `3.` | v | | `7` | k |
| `1:` | e | | `4` | f | | `7,` | s |
| `1'` (high dot) | á | | `4,` | g | | `7.` | sz |
| `1,` | b | | `4.` | gy | | `8` | m |
| `:1` (dots left) | ü | | `5` | h | | `8,` | t |
| `.1` (dot left) | u, ú, ű | | `5,` | l | | `9` | p |
| `2,` | cs | | `5.` | ly (see uncertainty 5) | | `9,` | z |

The ciphertext is in `work/transcription.txt`, line by line as on the card.

## Plaintext (Hungarian)

Everything from Édes to the signature is enciphered. The spelling of the card is kept, with accents added where the cipher does not mark them.

Édes Margitkám! Értesítelek hogy Rózától most kaptam egy lapot melyben azt írja hogy írt nektek egy levelet már három hete és választ még nem kapot rá nem tudja mi oka lehet. Most pedig értesítlek édesem hogy ha csak lehet minden bizonyal fel megyek. Most többet nem írok majd szóval többet már úgyis régen nem beszélgettünk. Soraimat bezárva adig is maradok üdvözölve és számtalanszor csókolva hűséges kedvesed és imádód a sírig (Árpád)

Open text: Sokszor csókolom ángyikát is / és [a?] kis Mariskát is. / Mezőkövesd, 1916. III/11.

Address: Őnagysága / Rózsa reményű / Sziber Margitka / kisasszonynak / Szomolya / Borsod m. u. p. Bogács

Normal spelling of three forms: kapot = kapott, bizonyal = bizonnyal, adig = addig.

## English translation

Sweet Margitka! I let you know that I have just received a card from Róza, in which she writes that she wrote you all a letter three weeks ago and has still had no reply to it; she does not know what the reason can be. And now I let you know, my sweet, that if at all possible I will certainly come up. I will not write more now, more by word of mouth; we have not talked for a long time anyway. Closing my lines, until then I remain, greeting you and kissing you countless times, your faithful sweetheart and your adorer to the grave (Árpád)

Open: Many kisses to ángyika too, and to little Mariska too. Mezőkövesd, 11 March 1916.

`ángyika` is a kin word (sister-in-law or aunt); the exact relation is not established.

## Slovak translation

Moja sladká Margitka! Oznamujem ti, že som práve dostal od Rózy pohľadnicu, v ktorej píše, že vám napísala list už pred tromi týždňami a ešte na to nedostala odpoveď; nevie, čo môže byť príčinou. A teraz ti oznamujem, moja zlatá, že ak to len bude možné, určite prídem hore. Teraz už viac nepíšem, viac potom ústne; aj tak sme sa už dlho nerozprávali. Končiac svoje riadky, zatiaľ ostávam, pozdravujúc ťa a nespočetnekrát bozkávajúc, tvoj verný milý a tvoj ctiteľ až do hrobu (Árpád)

Otvorený text: Mnohokrát bozkávam aj ángyiku a aj malú Marišku. Mezőkövesd, 11. marca 1916.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1167/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription.txt` and prints the text line by line, marking each sign read by sense. It reports 345 cipher signs: 341 by the table, 4 by sense.

## Uncertainties

Cipher signs read by sense. These four are not what the sign gives as written:

1. `lehet` in `mi oka lehet` (line 7): the first sign is a plain `5` with no comma, so the table gives `hehet`.
2. `hogy` (line 9): the last sign is a plain `4` with no dot, so the table gives `hof`. The same word has `4.` twice elsewhere on the card.
3. `lehet` in `ha csak lehet` (line 9): the last sign is a plain `8` with no comma, so the table gives `lehem`. No comma is visible; the end of the line is clean paper.
4. `szóval` (line 12): the third sign is a plain `3` with no dot, so the table gives `szodal`.

All four are a mark left off the right digit in a very common word. In `lehet` the card's own second occurrence shows the writer missing a mark in that word.

5. `5.` = ly rests on one word, `melyben`. On hcp-1178 and 1179 `5.` is l, so the same sign may simply be l with `melben` as a spelling; the word is the same either way. `5,` is the normal l on this card.
6. `.1` occurs three times: in `tudja` (u), `úgyis` (ú) and `hűséges` (ű). Vowel length in the last two is by word sense, since the cipher shows no length here. The dot left of the 1 in `úgyis` is firm and separate (corrected in review 1).
7. Word division and punctuation in the plaintext are mine. `majd szóval többet` is taken as "more by word of mouth", and the sentence breaks around it are my reading. The card has a clear gap between `fel` and `megyek` (line 10); taking them as the one word `felmegyek` is grammar, not a fact about the writing. The plaintext keeps the card's gap.
8. `imádod` is printed `imádód` ("your adorer"), since `0` covers o and ó and the word follows `kedvesed és`. `imádod` ("you adore") would not fit that closing.

9. `megyek` (line 10): the last vowel is `1:`. Its lower dot is clean, but the upper dot touches the start of the following 7. `1:` is right: the alternative `1.` would give `megyak`.
10. Fused commas: the `6,` in `számtalanszor` (line 16) and the `6,` of `nem` on line 13 have the comma run into the tail of the 6 instead of written apart. This is the writer's habit. I read `6,`; the plain 6 has no such tail (`majd`, `tudja`).

Open text:

11. `[a?]` in `és [a?] kis Mariskát is`: the short word before `kis` is badly formed, a top stroke with an l-like tail, printed over by a green `1440`-like number. It is not a clean `a`. I take it as `a` by sense, with hcp-1178 `és a kis Mariskával` as the parallel. The k of `kis` is blotted, and the word is read from its shape and from the parallel.
12. `Mariskát`: the mark above is the accent of á, not an extra i.

Not read: I did not use the postmark. The date comes from the writer's own `1916. III/11.`, which agrees with the portal's file name.

## Why I believe it is correct

- A key taken from other cards, with only the signs this card needs, gives 341 of 345 signs as written, and these form connected, ordinary Hungarian prose with no forced words.
- The text is a practical message with a clear plot (Róza's unanswered letter, a promised visit), not a set of phrases.
- The closing formula and the signature `Árpád` are found from the digits and agree with hcp-1174 and hcp-1165. The open greeting to ángyika and Mariska agrees with hcp-1165 and 1178.
- `4.`, `6`, `6.`, `1,` and `4` all give the same values here as on hcp-1165.

## Response to review 1

Verdict REVISE. All seven findings are addressed. One sign and one word change; the rest of the reading stands. Re-ran `python3 -I ciphers/hcp-1167/work/decode.py`: hashes OK, 345 signs, 341 by the table, 4 by sense, and line 12 now ends `már ugyis`.

1. major, fixed. I looked at `review/work/z_iy.png` and agree: a firm dot stands left of the 1, the same form as `.1` elsewhere. `work/transcription.txt` line 12 now has `.1 4. 1 7,`, and the plaintext has `úgyis` for `így is`. The English is now "anyway". The Slovak `aj tak` already fits. hcp-1152 (FINAL) has the same `.1` in `úgyis`.
2. minor, fixed. Uncertainty 6 now says three occurrences. The counts stay at 345 and 341.
3. minor, fixed. New uncertainty 9. `z_megy.png` shows the upper dot touching the 7, and `1:` stands.
4. minor, fixed. Uncertainty 7, the key section and the header of `work/transcription.txt` are reworded: there is a gap at `fel | megyek`, and the one-word reading is grammar.
5. minor, fixed. New uncertainty 10 on the fused commas.
6. minor, no change needed. `[a?]` stays disclosed as a reading by parallel, not as a clean sign. It is one word alone and the rest of the clause reads. It stands as uncertainty 11.
7. minor, resolved since the review. hcp-1165 now has its FINAL marker, so the citations of it stand; hcp-1174 and 1178 are FINAL too.

Items the reviewer could not verify remain open: the postmark date strip, whether the HistoCrypt article discusses this card, the exact kin sense of `ángyika`, and who Róza is.
