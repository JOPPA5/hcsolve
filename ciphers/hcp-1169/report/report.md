# HCP 1169 (cpc_1915-12-29_HU_Mezokovesd_HU_Szomolya_szomolya-14): a New Year love letter in numbers on a Hungarian postcard

Human solver: Tomáš Pavuk

**Status: deciphered in full (271 of 271 cipher signs, 2 of them by word sense); one word of the open note is not understood; independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1169 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1169), from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), which was not consulted, so it is not known whether the article discusses this card. No published solution was found.

The picture side shows a family greeting the New Year, with the printed words "Boldog ujévet!" ("Happy New Year!"). The message side is dated in open writing 1915. XII/29, Mezőkövesd, that is 29 December 1915, during the First World War. Mezőkövesd and Szomolya lie in Borsod county in north-east Hungary. The third digit of the handwritten year is overwritten. The postmark MEZŐKÖVESD has lost its day and month, but below the wheel a 9, a 1 and a hook that fits 5 are visible, which supports the year.

The address, as written, reads: Tek. / Szépreményü / Sziber Margitka / kisasszonynak / Szomolya) Bogács- / (Borsod m[?] u. p. In standard terms this is "To the Honourable, Promising Miss Margitka Sziber, Szomolya, Borsod county, last post office Bogács". One tall crossed stroke after the m of the county abbreviation is not resolved.

The card belongs to a series from Mezőkövesd to Szomolya. Sister cards hcp-1174, 1178 and 1179 had already been read, and hcp-1174 is signed Árpád in cipher and addressed to the same young woman. This card was read from that known key, extended by four signs here. It is not a wholly new key recovery.

![Picture side with the printed greeting (source/picture-large.jpg)](../source/picture-large.jpg)

![Address and message side: digit panel at the upper left, open note below it, address at the right (source/address-large.jpg)](../source/address-large.jpg)

Everything on the left half of the address side is by the sender. The digit panel covers fifteen lines. The two words "Most pedig" stand in clear inside it, and the New Year wish below is in clear. Light grey pencil strokes over the panel are later marks and do not affect the letters.

## Method

The transcription is **manual**: the digits were read from enlarged crops of the unconverted high-resolution scan. No OCR was used and the portal supplied no transcription. The difficulty is that commas hang well below and to the right of their digit, so they can be assigned to the wrong sign. The panel was therefore re-cropped as two-line tiles, which settled, for example, `1: 5,` in "elhozta".

The starting point was the table of hcp-1174, 1178 and 1179. It already gave csókol-, kedves and Árpád. The remaining values followed from words: `4` is f (fogsz, fehér), `4.` is gy (hogy, nagyon, gyenge), `5.` is ly (oly, melyet), `6` is j (jó, majd).

The script work/decode.py checks the scan hashes, decodes the whole transcription and asserts that the result equals the stated reading letter by letter:

    python3 -I ciphers/hcp-1169/work/decode.py

## Key

Monoalphabetic substitution of Hungarian letters by digits. Each letter is one sign, a digit alone or a digit with a mark, and the mark is part of the sign. There is no word division. Vowel length is not always told apart.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| 0 | o, ó | 2. | é | 5. | ly |
| 0, | ö, ő | 3 | d | 6 | j |
| 1 | i, í | 3, | r | 6, | n |
| 1. | a | 3. | v | 7 | k |
| 1: | e | 4 | f | 7, | s |
| 1' (one high dot) | á | 4, | g | 7. | sz |
| :1 (dots left) | ü, ű, ú, u | 4. | gy | 8 | m |
| 1, | b | 5 | h | 8, | t |
| 2, | cs | 5, | l | 9 / 9, | p / z |

On this card `5.` is only ly, carried by two words; on hcp-1178 and 1179 it stands for plain l. The difference does not affect the text here, since `5.` occurs only where the word needs that sound.

## Plaintext

Hungarian, spelling as on the card. Square brackets mark enciphered text. Word divisions are the solver's, and punctuation in the cipher part too, except "!" and ")".

[Drága jó Margitkám!]

[Elhozta a jó Isten az újévet is, melyet már oly nagyon vártam, hogy mégis közelebb legyek a szabadulás ideéhez, no de majd elérkezik az is, akor esik le szívemről egy malomkő és hejébe te fogsz rajta fügni boldogan mint gyenge szívű fehér galamb a fészkében midőn tojássait költi.]

Most pedig [üdvözölve és csókolva téged) hű kedvessed Árpád]

Open note: Boldog ujévet kivánok mindnyájatoknak még a kis haragos Mariskónak is nemigen megfek[t/f]el(?) 1915. XII/29 Mezőkövesd

Non-standard spellings, with the normal form: ideéhez = idejéhez, akor = akkor, hejébe = helyébe, fügni = függni, tojássait = tojásait, kedvessed = kedvesed.

## Translation

**English.** Dear good Margitka! The good Lord has brought the New Year too, which I have so longed for, so that I may yet be closer to the time of my release. Well, that too will come; then a millstone will fall from my heart, and in its place you will hang on it, happy as a gentle-hearted white dove in its nest when it hatches its eggs.

And now, greeting and kissing you) your faithful sweetheart Árpád

I wish a happy New Year to all of you, even to little cross Mariska, [nemigen megfek[t/f]el: "not much" plus a word not understood]. 29 December 1915, Mezőkövesd.

**Slovak.** Drahá dobrá Margitka! Dobrý Boh priniesol aj Nový rok, na ktorý som tak veľmi čakal, aby som bol predsa bližšie k času svojho oslobodenia. Nuž ale príde aj to; vtedy mi spadne zo srdca mlynský kameň a na jeho miesto budeš na ňom visieť ty, šťastná ako nežná biela holubica v hniezde, keď sedí na vajíčkach.

A teraz ťa pozdravujem a bozkávam) tvoj verný milý Árpád

Želám šťastný Nový rok vám všetkým, aj malej nahnevanej Mariške, [nemigen megfek[t/f]el: „nie veľmi" a neporozumené slovo]. 29. decembra 1915, Mezőkövesd.

The word "szabadulás" fits a writer waiting for release, but the card does not say from what, and the translation leaves that open.

## Uncertainties

Cipher signs:

- **esik**: the 1 has a tiny dot beside it, where the á dot sits. Literally this gives "esák", which is not a word. Read as i by sense; "esik le szívemről egy malomkő" is idiomatic.
- **szívű**: the mark under the 7 is in shape a short comma, unlike the round dots of `7.` elsewhere. Literally this gives "sívű". The sz is a correction by word sense.
- **á against e**: `1'` and `1:` are close. In Drága, már, vártam, tojássait, Árpád and Margitkám á was chosen because the word requires it. In galamb a stain beside the first vowel is ignored.
- **One-dot :1**: szabadulás and újévet show one left dot, the other words two. It is treated as a variant of the same sign.
- **Árpád**: the final 3 has a long stroke to the right, about three times a normal comma, taken as a flourish. As a comma it would give r. The name matches hcp-1174.
- **téged)**: a bracket-like stroke and a short stroke beside it are treated as punctuation. They are darker than the neighbouring digits. "téger" is not a word.
- Hyphens at line ends also follow complete words; they are line fillers.

Open text:

- **megfek[t/f]el**: the one word not understood. The letters are m-e-g-f-e-k, a long crossed stroke, e-l. The stroke drops below the line like an f, so "megfekfel" is at least as good a reading as "megfektel". "megfektél" ("you lay down, fell ill") is a guess that rests on the t, and its link to the sentence is unclear. The sentence before it is complete and "nemigen" reads.
- **Most pedig**: the d is looped and could at first sight be "ol"; read by sense.
- **Mariskónak**: there is a second small vowel body under an arch after the o, perhaps a correction. The name is certain.
- **mindnyájatoknak**: the j stands at the margin and "atoknak" is partly overwritten.
- **Address**: the stroke after the m of the county abbreviation is unresolved.

## Review

An independent reviewer, a separate Claude Opus 5.5 agent, tried to refute the solution. It re-read all 271 signs on the high-resolution scan before comparing, wrote its own decoder with the key typed afresh, and got the same letters. It found no digit or mark that differs from the transcription, apart from the shape call on szívű. Its verdict was **ACCEPT**, with eight minor findings on disclosure and the open text. All were accepted:

1. The address was misread as "(Borsod megy.)"; it now follows the card, with u. p. and the unresolved stroke.
2. The printed greeting has no accent: "Boldog ujévet!".
3. The mark in szívű is stated as a short comma, with sz as a correction.
4. The plaintext now prints megfek[t/f]el, not a preferred t.
5. Two vowel bodies in Mariskónak are recorded.
6. One-dot `:1` is recorded for újévet too.
7. The visible figures of the postmark are recorded.
8. `5.` is stated as carried by two words, not several.

No decoded letter changed. The reviewer ruled that megfek[t/f]el is a single un-understood word, not an unread clause, a judgement call since the short clause has no other content word. It could not verify the HistoCrypt article, the sense of that word, the address stroke or the postmark day and month.
