# HCP 1174 (cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18): a suitor's digit cipher on a Hungarian postcard

Human solver: Tomáš Pavuk

**Status: all 89 cipher signs are deciphered (84 by the key as written, 5 by word sense); independent review 1 verdict REVISE, findings addressed, cipher reading unchanged.** Two words of the open text remain unread. Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1174 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1174), portal name cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-01 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was **not checked** for this card, so it is not known whether it treats it. The whole reading here was made from the card.

The card was sent in wartime, from Mezőkövesd to the village of Szomolya in north-east Hungary. It is headed *Mezőkövesd, 916. II/15*. The postmark shows FEB 15; its year is damaged but fits 1916. It is addressed to *Őnsg. Szépreményű Sziber Margitka kisasszonynak, Szomolya, u. p. Bogács*, "To the promising young lady Margitka Sziber". *Őnsg.* is an abbreviated title, read as written.

The message is open Hungarian with the tender words replaced by digits. A later hand struck the open text through in brown ink. The writer apologises for not coming as promised, announces a visit, and copies a love verse. The verse is a Hungarian version of Heine's "Leise zieht durch mein Gemüt", in which the closing request to greet the rose has become *say that I love her*. The printed source of this Hungarian wording was not found. Antal Radó's translation *Tavaszi dal* (LiederNet text 114147) was compared by keyword only, and it is a different version.

The card belongs to a group in one correspondence. Hcp-1175, 1178 and 1179 also carry digit passages. A note on hcp-1178 dares the reader to read the "number-letters". Hcp-1177, in clear, is signed with a name read as Árpád.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, from the un-converted high-resolution scan enlarged 2 to 5 times. No OCR was used. To see the open text under the brown strike-outs, the red channel was clipped so that the brown ink drops out and the blue writing stays.

No key existed, so it was recovered from the card. The starting points were the open words around the digits (`Ha ... téged`, `Mondd, hogy ...`), the rhymes (`éled` with `téged`, `szeretem` with `terem`) and the repeated endings `5, 5, 1. 7` and `5, 5, 1: 7`, which are -llak and -llek. A straight digit alphabet failed, and so did treating the comma as a word divider. The step that worked was to treat a digit and its mark as one sign. The comma then separated pairs that had looked like one digit for two letters: `3` d and `3,` r, `7` k and `7,` s, `8` m and `8,` t, `5` h and `5,` l.

The decoding can be reproduced from the repository root with `python3 -I ciphers/hcp-1174/work/decode.py`. It checks the scan hashes, decodes every sign and asserts that it matches the stated word. The open text is hard-coded there, so the command tests the cipher part only.

## Key

Monoalphabetic substitution (MASC), with one sign per letter, or per digraph for cs and sz. There are no word divisions. Only the 23 signs attested on this card are listed.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o, ó | `2,` | cs | `5,` | l |
| `0,` | ö, ő | `2.` | é | `6,` | n |
| `1` | i, í | `3` | d | `7` | k |
| `1.` | a | `3,` | r | `7,` | s |
| `1:` | e | `3.` | v | `7.` | sz |
| `1'` (high dot) | á | `4,` | g | `8` | m |
| `:1` (dots at left) | ü | `5` | h | `8,` | t |
| `9` | p | `9,` | z | | |

## Plaintext

Square brackets show the enciphered parts. `[vagi oltál ?]` gives unresolved letters as seen, and `[= ...]` gives the normal spelling. Parentheses are on the card.

```text
Mezőkövesd, 916. II/15.

[Édes Margitkám]!

Bocsáss meg, hogy ígéretemet nem teljesítettem, vagyis
nem mehettem fel, de semmi tekintetben sem tehettem.
A jövő vasárnapi bátran felmegyek, az idő nem diferál
[= differál], hogy milyen lesz az mindegy, és majd
pótolni fogom a multat is.

II Ha [ölelhetlek én], téged,
Arcom derül, [szívem éled].

Lágy tavaszodal [= tavaszdal] [vagi oltál ?]
Halkan keblemet
Messzi csendülj röpke kis dal
Át a tér felett.

II Csengj ki váltig ama házig
Hol virág terem
És ha ott egy rózsa látszik
Mondd, hogy [szeretem]

[számtalanszor üdvözöllek] és [csókollak]
([szerető kedvesed]) [Árpád]
```

**English:** Sweet Margitka! Forgive me for not keeping my promise, that is, I could not come up, but I could do nothing about it at all. Next Sunday I will boldly come up; the weather makes no difference, whatever it is like, and I will also make up for the past.

II If I can embrace you, / my face brightens, my heart revives.

Soft spring song [two words unread, with the verb] softly my breast; / ring far away, little flying song, / over the space. // II Ring on and on, to that house / where flowers grow, / and if a rose is seen there, / say that I love her.

Countless times I greet you and kiss you (your loving sweetheart) Árpád

**Slovak:** Moja sladká Margitka! Odpusť mi, že som nesplnil svoj sľub, teda že som nemohol prísť hore, ale nijako som si nemohol pomôcť. Budúcu nedeľu smelo prídem, na počasí nezáleží, nech bude akékoľvek, a minulosť si tiež vynahradím.

II Keď ťa môžem objať, / tvár sa mi rozjasní, srdce ožije.

Jemná jarná pieseň [dve neprečítané slová so slovesom] ticho moju hruď; / zaznej do diaľky, letmá pesnička, / ponad priestor. // II Zvoň ďalej a ďalej, až k tomu domu, / kde rastú kvety, / a ak tam uvidíš ružu, / povedz, že ju milujem.

Nespočetnekrát ťa pozdravujem a bozkávam (tvoj milujúci milý) Árpád

## What remains uncertain

**Cipher signs.** The fixed table alone gives `szimtalanszor`, `üdvpzpllek` and `kerető`. Five signs are therefore read by sense, although each word is certain as a word:

- `számtalanszor`: the second sign is a plain `1`, with no high dot seen. The key gives i, and sense needs á.
- `üdvözöllek` (two signs): both ö signs are 9-shaped, not `0,`, and the second has a dot above. They are taken as a `0,` with the comma joined to the body. `9` alone would be p.
- `szerető` (two signs): the first sign shows no separate dot and is read as `7.`, with the dot apparently absorbed. The r is blotted: its comma is clear, and the body is taken as 3.

**Open text under the strike-outs.** This is plain text, not cipher.

- `[vagi oltál ?]`: both words are unresolved. `vagi` is not a Hungarian word. `keblemet` is accusative, so this line must hold the verb of the sentence, and that verb is unread. The problem is confined to this phrase, and the rest of the stanza reads.

![The unresolved phrase, red channel, 3x (work/crops/l_red.png)](../work/crops/l_red.png)

- `tavaszodal` appears for `tavaszdal`, and `diferál` has one f for `differál`.
- `Át a tér felett` could be `Át az éter felett`.
- `házig` is read mainly by sense, from Heine's "bis an das Haus"; the pixels also allow `hóvig`.
- `mehettem` lies under a strike-out, and in `A jövő` the first sign looks like a 6. The end of `vasárnapi` is unclear, and sense wants `vasárnap`. The l of `Hol` lies under an overstrike.
- The two `II` marks (in the margin before `Ha`, above `Csengj`) are unexplained.
- The signature `Sz. A.` on sister cards carries no attested accent, and the open `Árpád` of hcp-1177 is that card's least sure word. They support the name but do not prove it. The digits themselves give it clearly.

## Why the solution is believed correct

One fixed key decodes 84 of 89 signs as written into Hungarian, and the other 5 sit in words fixed by the signs around them. The decoded words complete the open text exactly: `Ha ölelhetlek én, téged`, with `éled` rhyming with `téged` and `szeretem` with `terem`. The same key gives `csókollak téged` on hcp-1178, beyond what was used to build it there. Enciphering only the tender words suits a suitor writing on an open postcard.

## Review and what changed

An independent reviewer, a separate Claude Opus 5.5 agent, ran the command, made its own sign-by-sign transcription from its own crops and decoded it with its own script and no table of exceptions. It got the same 89 signs and 23 distinct signs, and it confirmed all the enciphered words. It tried to refute the key and could not. Its verdict was REVISE, with one major and six minor findings, all on presentation and open text:

1. `vági által` had been printed as a reading. It is now `[vagi oltál ?]`, with the verb stated as unread (major).
2. `differál` is now given as written, `diferál`.
3. The command output now matches this text, including the parentheses and the address.
4. "Every one of the 89 letters" was an overclaim. It now reads 84 by the table and 5 by sense.
5. Details of the sister-card evidence were corrected, and the open `Árpád` of hcp-1177 was added.
6. Both `II` marks are now shown, with their meaning given as unexplained.
7. It is now stated that the portal's linked article was not checked.

The key and the deciphered words did not change. The reviewer could not settle the words under the densest strike-outs, or the middle digit of the postmark year.
