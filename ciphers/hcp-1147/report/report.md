# HCP 1147 (cpc_1916-04-20_HU_Mezokovesd_HU_Szomolya_szomolya-29): an Easter letter and three verses in a digit cipher

Human solver: Tomáš Pavuk

**Status: deciphered in full (475 of 475 cipher signs: 469 by the key as written, 6 by word sense); independent review 1 verdict ACCEPT, three minor findings addressed, no change to the Hungarian reading.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1147 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1147), portal name cpc_1916-04-20_HU_Mezokovesd_HU_Szomolya_szomolya-29, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, main category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). The reviewer read its abstract page, which speaks of a collection of more than 400 encrypted postcards and does not mention this card or its people. The full text was not read. The reading here was made from the card.

It is a picture postcard showing a couple with lilacs; the picture side carries no writing. It was sent from Mezőkövesd to Szomolya in north-east Hungary, by a writer who signs Árpád. The only open text is the address, "Őnagysága. / Rózsa Reményü / Sziber Margitka / Kisasszonynak / Szomolya / u.p. (Bogács)", and the date "(Mezőkövesd, 1916. IV/20.)" in the top margin. The postmarks show APR 20, with the year not legible, so the year rests on the writer's note. Easter Sunday 1916 fell on 23 April, three days after the card, which fits a message about Easter leave.

The card belongs to a correspondence from Árpád to Margitka Sziber. Hcp-1174, 1178 and 1179 are finished cards of the same group, on which only parts of the message are enciphered. On this card the whole message is in cipher.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, sign by sign, from the un-converted high-resolution scan enlarged 3 to 8 times. No OCR was used. Colour, red-channel and blue-minus-red crops were used where the ink crosses the printed table of the card (N1 to N3) or the postmark (L2 to L6).

The key started from the finished sister cards. The salutation `2. 3 1: 7, 8 1. 3, 4, 1 8, 7 1' 8 !` is letter for letter the "Édes Margitkám!" of hcp-1174, and the table carried over gave "ha pista húsvétra kap szabadságot" at once. Five signs are new, each found from a word that it alone completes: `6` j, `6.` ny, `8.` ty, `4.` gy and `·1` u. The value `4` = f, tentative on hcp-1175, is confirmed here by falu and fér.

The decoding can be reproduced from the repository root with `python3 -I ciphers/hcp-1147/work/decode.py`. It checks the hashes of the scans, decodes the transcription sign by sign, stops on any mismatch with the stated reading and prints the text. Address and date are hard-coded, as they are open text.

## Key

Monoalphabetic substitution (MASC). Each letter is one sign: a digit alone, or a digit with a mark, and the mark is part of the sign. A stroke, dot or colon after the digit is the mark; a dot or colon left of 1 also counts. Latin `a` and `az` are written openly among the signs in a few places. Vowel length of o, i, u, ö and ü is not marked.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o, ó | `2,` | cs | `6` | j |
| `0,` | ö, ő | `2.` | é | `6,` | n |
| `1` | i, í | `3` | d | `6.` | ny |
| `1.` | a | `3,` | r | `7` | k |
| `1:` | e | `3.` | v | `7,` | s |
| `1'` (high dot) | á | `4` | f | `7.` | sz |
| `1,` | b | `4,` | g | `8` | m |
| `·1` (dot left) | u, ú | `4.` | gy | `8,` | t |
| `:1` (colon left) | ü, ű | `5` | h | `8.` | ty |
| `9` | p | `5,` | l | `9,` | z |

## Plaintext

All of this is cipher. Capitals and punctuation are editorial. The card has few word gaps, so word breaks and the order of the boxes (letter, bird verse, compass verse, village verse, closing) follow sense and layout.

```text
Édes Margitkám!

Ha Pista húsvétra kap szabadságot, légy szíves írd meg neki,
hogy hacsak lehet, nálatok töltse el a húsvétot, mert nagyon
szeretnék vele találkozni, hátha többet nem beszélhetek vele.
Most egyéb újságot nem írok, majd szóval többet.

Hozzád repül a távolból
kis angyalom, a madárka,
oda száll az ablakomra,
csőrében egy képes kártya.

Északon és délen
képed itt van vélem,
keleten, nyugaton
te vagy gondolatom.

Kicsi házban, falu végén,
hogy ha laknám veled én,
azt mondanám: ottan lakom
a világ közepén.

Most többet nem tudok írni, mert nem fér. Sok csókkal és
öleléssel maradok hozzád mindig hű imádód (Árpád)
```

**English:** Sweet Margitka! If Pista gets leave for Easter, please write to him that, if it is at all possible, he should spend Easter at your place, because I would very much like to meet him; who knows, I may never speak with him again. I am not writing any other news now; more by word of mouth later.

To you from afar, my little angel, flies / the bird; / there it alights on my window, / in its beak a picture card.

North and south / your image is here with me; / east and west / you are my thought.

In a little house at the end of the village, / if I lived with you, / I would say: there I live, / at the centre of the world.

I cannot write more now, because it will not fit. With many kisses and embraces I remain ever your faithful adorer (Árpád)

**Slovak:** Moja sladká Margitka! Ak Pišta dostane na Veľkú noc dovolenku, buď taká dobrá a napíš mu, aby, ak je to len možné, strávil Veľkú noc u vás, lebo by som sa s ním veľmi rád stretol; ktovie, či sa s ním ešte niekedy porozprávam. Teraz inú novinu nepíšem, viac potom ústne.

K tebe z diaľky, môj anjelik, letí / vtáčik; / tam sadá na moje okno, / v zobáku obrázková pohľadnica.

Na severe i na juhu / tvoj obraz je tu so mnou; / na východe, na západe / ty si mojou myšlienkou.

V malom domčeku na konci dediny, / keby som býval s tebou, / povedal by som: tam bývam, / v strede sveta.

Viac teraz nemôžem písať, lebo sa to nezmestí. S mnohými bozkami a objatiami zostávam navždy tvoj verný ctiteľ (Árpád)

## Uncertainties

Six signs are not taken at face value:

1. **egyéb (L7).** The 1 stands on the printed divider, with a round dot at its foot and a dash high to the right, read as a widely spaced colon, `1:` = e. The word is then literally "egyeb" for egyéb, a slip or short spelling.
2. **most (L7).** The final 8 has no comma, so literally it is m. The same word in the closing has `8,`.
3. **nagyon (L4).** The first 6 has no comma, so literally it is j. The stroke nearby belongs to the 8 of "mert".
4. **többet (L8).** The ö looks like a plain 9, read as `0,` with the comma joined on, as hcp-1174 has in üdvözöllek. The word has plain `0,` twice elsewhere on this card.
5. **mondanám (N3).** The sign is abraded and partly under the printed word "Import". What is left does not fix the digit. `3` = d rests only on the word, the one word that fits.
6. **légy (L2).** An ink blot covers the place of the dot of `4.`.

Other points:

- **ablakomra (M3).** The 8 is heavily blotted, but both loops are closed, so it is m and not d. The reading is what the card says, yet the verse has the bird fly to the addressee, so "ablakodra" (your window) would make better sense. The blot may be a correction or a slip; the scan cannot show ink order.
- "kis angyalom" is taken as a vocative to Margitka; apposition to the bird is possible.
- `6.` (nyugaton) and `8.` (kártya) occur once each on this card and rest on those words. Sister cards, not all of them finished, read `6.`, `8.`, `4.` and `·1` the same way, which is support, not proof.
- The 7 of közepén (N4) is abraded but still a 7. A stroke in újság (L8), taken as the comma of `7,`, runs into the line below.
- Pista is not identified. "Szabadságot kap" suggests military leave, and "hátha többet nem beszélhetek vele" reads as wartime worry, but that is interpretation; the card does not say so.
- The verses may be quoted or popular. They were not traced to a printed source.

The whole key reads one continuous message, and no clause is left unread.

## Review

An independent reviewer (a separate Claude Opus 5.5 agent) read every row from its own crops, before comparing, and decoded the literal reading with a separately written key. Of 479 tokens, 5 differed from the solver's transcription, and all 5 were points the solver had disclosed. Decoded without sense corrections, the card gives the claimed text apart from jagyon, mosm, egyeb, tpbbet and the illegible spot in mondanám. The reviewer also confirmed the Easter date, the rhymes, the agreement with hcp-1174, and that nothing suggested an undisclosed source.

Verdict **ACCEPT**, with three minor findings:

1. The blotted 8 of ablakomra and its awkward sense were not disclosed. Both are now listed.
2. The tally was slightly overstated: the hidden dot of légy was counted as read by the table, the abraded 7 of közepén was not mentioned, and "each recurs" was not true of `6.` and `8.`. The count is now 469 + 6 and all three are stated.
3. "kis angyalom" was translated as apposition. It is now a vocative, in English and Slovak, with the other reading noted.

No letter of the Hungarian changed.
