# hcp-1174 solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-01. No earlier work on this number. The portal attaches no solution. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses this card.

## Cipher type and key

The card is Hungarian plain text with key words replaced by a digit cipher (register label: MASC). Each letter is one sign: a digit, or a digit with a mark. The comma is part of the sign, so `3` is d and `3,` is r. There are no word divisions. Parentheses on the card are punctuation.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2,` | cs | | `5,` | l |
| `0,` | ö, ő | | `2.` | é | | `6,` | n |
| `1` | i, í | | `3` | d | | `7` | k |
| `1.` | a | | `3,` | r | | `7,` | s |
| `1:` | e | | `3.` | v | | `7.` | sz |
| `1'` (high dot) | á | | `4,` | g | | `8` | m |
| `:1` (dots to the left) | ü | | `5` | h | | `8,` | t |
| `9` | p | | `9,` | z | | | |

Only signs attested on this card are listed. The card has 89 cipher letters written with 23 distinct signs. Of the 89, 84 decode by this table as written; 5 are read by sense (see Uncertainties).

Key recovery: `téged` and `Mondd, hogy` in clear, Heine's rhyme scheme, and the repeated `5, 5, 1. 7` / `5, 5, 1: 7` endings (-llak / -llek) gave the first letters. The comma then turned out to separate pairs that first looked like one digit for two letters (d/r, k/s, m/t, h/l).

## Plaintext (Hungarian; [ ] = enciphered on the card)

Mezőkövesd, 916. II/15.

[Édes Margitkám]!

Bocsáss meg, hogy ígéretemet nem teljesítettem, vagyis nem mehettem fel, de semmi tekintetben sem tehettem. A jövő vasárnapi bátran felmegyek, az idő nem diferál [= differál], hogy milyen lesz az mindegy, és majd pótolni fogom a multat is.

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

[számtalanszor üdvözöllek] és [csókollak] ([szerető kedvesed]) [Árpád]

Address: Őnsg. / Szépreményű Sziber Margitka kisasszonynak / Szomolya / u. p. Bogács. Postmark Mezőkövesd, FEB 15; the year is damaged and fits 916.

`[vagi oltál ?]` gives the letters as seen. The two words are unresolved, and the verb of that sentence is unread. The two `II` marks stand on the card without a full stop; their meaning is unexplained.

## English translation

Sweet Margitka! Forgive me for not keeping my promise, that is, I could not come up, but I could do nothing about it at all. Next Sunday I will boldly come up; the weather makes no difference, whatever it is like, and I will also make up for the past.

II If I can embrace you, / my face brightens, my heart revives.

Soft spring song [two words unread, with the verb] softly my breast; / ring far away, little flying song, / over the space. // II Ring on and on, to that house / where flowers grow, / and if a rose is seen there, / say that I love her.

Countless times I greet you and kiss you (your loving sweetheart) Árpád

## Slovak translation

Moja sladká Margitka! Odpusť mi, že som nesplnil svoj sľub, teda že som nemohol prísť hore, ale nijako som si nemohol pomôcť. Budúcu nedeľu smelo prídem, na počasí nezáleží, nech bude akékoľvek, a minulosť si tiež vynahradím.

II Keď ťa môžem objať, / tvár sa mi rozjasní, srdce ožije.

Jemná jarná pieseň [dve neprečítané slová so slovesom] ticho moju hruď; / zaznej do diaľky, letmá pesnička, / ponad priestor. // II Zvoň ďalej a ďalej, až k tomu domu, / kde rastú kvety, / a ak tam uvidíš ružu, / povedz, že ju milujem.

Nespočetnekrát ťa pozdravujem a bozkávam (tvoj milujúci milý) Árpád

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1174/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign, asserts that each decoded word matches the stated reading, and prints the full text with the address. The open text is hard-coded in the script, so the command reproduces only the decoding of the cipher signs. It reports how many signs decode by the table and how many are read by sense (84 and 5).

## Uncertainties

Cipher signs. Five signs at four points are in `ODD` in `work/decode.py`. The fixed table alone gives `szimtalanszor`, `üdvpzpllek` and `kerető`. Each word is certain as a word, but these signs are not clean:

1. `számtalanszor`: the second sign is a plain `1` on the card, with no high dot seen. Key gives i, sense needs á.
2. `üdvözöllek` (two signs): both ö signs are 9-shaped, not `0,`; the second of them has a dot above. I take them as a joined `0,`. This rests on word sense, since `9` alone is p.
3. `szerető`: no separate dot is visible under the crossed 7, so the sign is read as `7.` by sense.
4. `szerető`: the r sign is blotted. The comma is clear, the body is taken as 3 by sense.

Struck-through plain text. Later brown strike-outs cover all of it. I read it with the brown ink suppressed (`work/ink.py`). The poem is read from the card but fitted to Heine, so these are the weak points:

- `[vagi oltál ?]` is unresolved. Both words stay unread and no part of them is certain. On `work/crops/l_vagi5.png`, `l_altal5.png` and `l_red.png` the first word shows v, two round letters, a looped descender and a dotted i; the second opens with a round o-like letter and ends in -tál or -tal. `oltál` and `által` both remain possible for the shape; `oltal` is an o-word as seen. `vagi` is not a Hungarian word. `keblemet` is accusative, so this line must hold the verb of the sentence, and that verb is unread. It is one phrase of open text, not cipher, and the rest of the stanza reads.
- `tavaszodal`: the card appears to have this form, printed with the normal `tavaszdal` beside it.
- `diferál`: one f on the card, for normal `differál`.
- Published Hungarian source: not found. Antal Radó's translation `Tavaszi dal` (LiederNet, text 114147) was compared by keyword only and has none of the distinctive words of this text, so it is a different version.
- `Át a tér felett` could be `Át az éter felett`; the accent seems to sit on the visible `tér`.
- `házig` is read mainly by sense (Heine: "bis an das Haus"); the pixels could suggest `hóvig`.
- `Hol`: the final l is under an overstrike.
- `II`: one in the left margin before `Ha`, one above the start of `Csengj`. They could number stanzas or parts, but that is unproven.
- `mehettem` is overwritten by a strike-out; `A jövő`: the first sign looks like a 6 or A; `vasárnapi` is as written, the last letter unclear (sense wants `vasárnap`).

The word `Őnsg.` in the address is an abbreviated title read as written; it is not part of the message.

## Why I believe it is correct

- One fixed key decodes 84 of the 89 cipher signs as written into Hungarian. The other 5 are disclosed above and all sit in words that the surrounding signs fix.
- Words fit the clear text exactly: `Ha ölelhetlek én, téged`, and `éled` rhymes with `téged`.
- `szeretem` rhymes with `terem` and completes Heine's "Leise zieht durch mein Gemüt" ("sag, ich lass sie grüßen"), here turned into a love line.
- The same key decodes `2, 0 7 0 5, 5. 1. 7 8, 2. 4, 1: 3` on sister card hcp-1178 as `csókollak téged` (that card has `5, 5.` where this one has `5, 5,`). That sequence was not used to build the key beyond `csókollak`.
- `Árpád` agrees with the open signature read as `Árpád` on hcp-1177 from the same Mezőkövesd/Szomolya circle, though that signature is that card's least sure word. It is also compatible with the signature `Sz. A.` on hcp-1175 and 1176 (no accent attested there). It was found from the digits, not from those cards.
- Enciphering only the tender words is consistent with a suitor writing on an open postcard to a young woman.

## Response to review 1

Verdict REVISE. The key, the cipher reading and all 89 signs are unchanged. All seven findings are addressed.

1. **Major, `vági által`: fixed.** I re-read the phrase at 5x on the hires scan, in colour and in the red channel (`work/lagy.py`, `work/crops/l_vagi5.png`, `l_altal5.png`, `l_red.png`). I agree with the review: it does not show `vági által`. It is now printed as `[vagi oltál ?]` in SOLUTION.md and in the script output, and the verb is stated as unread. The translations mark it the same way. I could not narrow it: the second word's shape allows `oltál`, and an `á` in `által` cannot be excluded, but no reading is claimed. A search for the printed Hungarian source did not find it. Radó's `Tavaszi dal` is a different version (keyword check on LiederNet text 114147). The problem is confined to these two words of open text, and the rest of the stanza reads.
2. **Minor, `differál`: fixed.** The plaintext gives `diferál`, with the normal form beside it. `tavaszodal` is treated the same way, and the notes are kept.
3. **Minor, command output: fixed.** The script now prints `[csókollak] ([szerető kedvesed]) [Árpád]` and the address. I re-ran it: hashes OK, 89 signs, and the output matches this file. The one difference is the `[= ...]` normal forms, which appear only here.
4. **Minor, overclaim: fixed.** The key note and the evidence section now say 84 signs by the table and 5 by sense, and the script prints those counts.
5. **Minor, sister evidence: fixed.** hcp-1178 is quoted with `5, 5.` as on its own transcription, and the signature is `Sz. A.`. The open `Árpád` of hcp-1177 is added, with the note that it is that card's least sure word. So I treat it as support, not as proof.
6. **Minor, `II` marks: fixed.** Both are shown without a full stop, confirmed on `work/crops/ii_over.png`: one in the margin before `Ha`, one above `Csengj`. Their meaning is stated as unexplained. I also corrected my own note on `Hol`, since the `II` stands a line higher and the l is under an overstrike.
7. **Minor, published solution: fixed.** The header here, SOURCES.md and the report say that the portal's linked article was not checked for this card.

One small correction of mine: the postmark year is now given as damaged, in line with what the review could not verify.
