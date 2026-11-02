# HCP 1139 (cpc_1916-01-06_HU_Mezokovesd_HU_Szomolya_szomolya-15): Árpád's New Year letter to Margitka

Human solver: Tomáš Pavuk

**Status: deciphered in full (366 cipher signs: 364 by the key as written, 2 by word sense, in words that are certain); independent review 1 verdict ACCEPT, no decoded word changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1139 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1139), portal name cpc_1916-01-06_HU_Mezokovesd_HU_Szomolya_szomolya-15, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was **not checked** for this card, so it is not known whether it treats it. The transcription and reading here were made from the card.

It is a picture postcard with a girl's portrait, printed in Saxony. The picture side has no writing. On the address side the whole message is enciphered, including a boxed signature written sideways. Only two things are open: the place and date up the margin, Mezőkövesd 1916 I/6 (6 January 1916), and the address:

Őnagysága / Sziber Margitka / ur-leánynak / Szomolya / u. p. Bogács

That is "Her Ladyship, Miss Margitka Sziber, Szomolya, post office Bogács". The postmarks show letters but no readable date, so the date is the writer's own. The language of the message is Hungarian.

The card belongs to the Mezőkövesd correspondence, wartime cards sent to Margitka Sziber in the village of Szomolya in north-east Hungary. Several of them carry the same digit cipher (for example hcp-1174, 1178, 1179, 1148 and 1160), and the writer signs as Árpád.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is **manual**. The solver read all 22 rows sign by sign from the high-resolution scan at 2x to 6x, one row of text to one row of signs, and recorded them in work/transcription.txt. The card has no word divisions; those are the solver's.

The key was **transferred, not recovered here**. It was built on the sister cards named above, and this card needed no new value. Applied to the card, it gave Hungarian at once. No value was adjusted for this card and no word was forced. work/decode.py checks the hashes of the scans, decodes every sign with the key, and asserts each decoded word against the stated reading. To reproduce it, run from the repository root:

python3 -I ciphers/hcp-1139/work/decode.py

## Key

The system is a monoalphabetic substitution of the kind labelled MASC in the register. One letter is one digit plus an optional mark. Long and short vowels are often not separated (`0` is o and ó, `.1` is u, ú and ű).

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| `0` | o, ó | `2,` | cs | `6,` | n |
| `0,` | ö, ő | `2.` | é | `6.` | ny |
| `1` | i | `3` | d | `7` | k |
| `1.` | a | `3,` | r | `7,` | s |
| `1:` | e | `3.` | v | `7.` | sz |
| `1'` (high dot) | á | `4,` | g | `8` | m |
| `1,` | b | `4.` | gy | `8,` | t |
| `.1` (dot left) | u, ú, ű | `5` | h | `9` | p |
| `:1` (two dots left) | ü | `5,` | l | `9,` | z |
| `2` | c | `6` | j | | |

Twenty-four of these signs come from hcp-1174, 1178 and 1179. The other five (`4.`, `6`, `6.`, `2`, `.1`) come from hcp-1148 and 1160, and words on this card confirm them. For `2` (only in tubicám) and `6.` (only in aranyos) that confirmation is one word each, and `2` rests on hcp-1148 alone.

## Plaintext

Hungarian, spelling as on the card, punctuation and word division added.

Mezőkövesd 1916 I/6 (open)

Kedves Margitkám!

Hogy múlt el az új év neked, jól-e vagy rosszul? Mert nekem nagyon rosszul, egyrészt mer [= mert] nem veled tölthettem, az tán [= aztán] meg máskép [= másképp] is egy kicsit beütöt [= beütött] a krak [= krach].

Aranyos babuskám, szeressél igazán.

Boldog csak úgy lehetsz,

hogy ha engem szeretsz.

Üdvözletem küldöm, édesem, tenéked,

úgy szeressél engem, mint ahogy én téged.

Nem kérek Istentől kincset, gazdagságot,

csak téged, tubicám, s hozzád boldogságot.

Sokszor csókolva és üdvözölve téged maradok hű kedvesed

Árpád

## English translation

Mezőkövesd, 6 January 1916

Dear Margitka of mine!

How did the New Year go for you, well or badly? For me very badly: first, because I could not spend it with you, and then in other ways too the crash has struck a bit.

My lovely little darling, love me truly.

You can only be happy

if you love me.

I send you my greeting, my sweet,

love me as I love you.

I ask of God no treasure, no riches,

only you, my little dove, and with you happiness.

Kissing and greeting you many times, I remain your faithful sweetheart

Árpád

## Slovak translation

Mezőkövesd, 6. januára 1916

Moja drahá Margitka!

Ako ti prešiel Nový rok, dobre alebo zle? Mne veľmi zle: po prvé preto, že som ho nemohol stráviť s tebou, a potom aj inak ma trochu postihol krach.

Moja milá bábika, miluj ma naozaj.

Šťastná môžeš byť len tak,

ak miluješ mňa.

Posielam ti svoj pozdrav, moja sladká,

miluj ma tak, ako ja teba.

Nežiadam od Boha poklad ani bohatstvo,

len teba, moja hrdlička, a k tebe šťastie.

Mnohokrát ťa bozkávam a pozdravujem, zostávam tvoj verný milý

Árpád

## What remains uncertain

**Signs resting on word sense (2 of 366).**

- téged in "mint ahogy én téged" (line 15): the first sign is a plain 8 with no comma, so the key gives méged. The rhyme with tenéked and the same word at two other places fix téged. It is taken as a dropped comma.
- First rosszul (line 3): under the 7 stands an ink blot with a thin tail, and the pixels do not separate `7.` (sz) from `7,` (s). The same word has a clear `7, 7.` in line 4, and rossul would only be a spelling variant.

**Other close calls.** None of them changes a word.

- tubicám: the third sign is crossed by a stroke from the line above. It has the single stem of a 1 and not the bars of this writer's 7, so it is `1,` = b. tusicám is no word the solver knows.
- hozzád: the dot on the 1 is large and stands at mid to upper height, so it is read as `1'` (á).
- tölthettem and üdvözölve: the ö is a 0 with the comma touching it, written tight. It is counted as plain `0,`.
- hű is written with `.1`. It is the only ű on the card, so no separate sign is attested here.
- ha (line 11) lies in a blue blot, but stem and dot are visible.
- A stray dot stands before the first hogy. The word is hogy either way.
- krak is taken as the loanword krach, spelled by ear, in "beüt a krach" (a crash or disaster strikes). The signs are clear, but this meaning comes from memory and was not checked in a dictionary. What the crash was, money or the war, the card does not say.
- Curved lines separate the sections, and a frame encloses the last two lines. A `>`-shaped stroke before maradok is unexplained. These marks were not treated as cipher.
- Whether the verses are a known popular rhyme was not searched.

## Why the solution is believed correct

A key taken from other cards gives continuous Hungarian across the whole card. The verses rhyme with no help from the solver (lehetsz / szeretsz, tenéked / téged, gazdagságot / boldogságot), and the four long lines are all regular 6+6 syllables. The boxed signature decodes to Árpád, the salutation to Kedves Margitkám, and the closing formula hű kedvesed matches hcp-1148. A New Year letter fits 6 January.

## Review and what changed

An independent reviewer, a separate Claude Opus 5.5 agent, ran the command, decoded the transcription with its own script and table, and compared all 22 rows with its own crops of the high-resolution scan. It found no wrong letter and no forced word, tried to refute the reading and could not. Its verdict was ACCEPT, with five minor findings:

1. A blot in the first rosszul had been counted as a clean sign. It is now declared as resting on sense.
2. Two signs had been called 9-shaped. On the close-ups they are a 0 with a comma touching it, so they now count as plain `0,`. With finding 1, the count moved from 363 clean and 3 by sense to 364 and 2.
3. The English now says the crash "has struck a bit", for egy kicsit.
4. The provenance of `2` and `6.` is now stated, as above.
5. The address is now given as written, ur-leánynak.

The decoded text did not change. The reviewer could not verify the postmark date, what the crash referred to, or the meaning of the `>` stroke and the left dot in hogy. It also did not open the HistoCrypt article.
