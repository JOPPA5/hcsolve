# hcp-1178 solution

Solver: Claude Opus 5.5, 2026-11-01. No earlier work on this number. No published solution found; none attached on the portal.

## Cipher and key

The card is an open Hungarian letter and verse in copying pencil. Only one boxed line is enciphered, 13 signs:

`2, 0 7 0 5, 5. 1. 7 8, 2. 4, 1: 3`

The writer's note beneath it says numbers stand for letters (see below). Type: monoalphabetic substitution (MASC). A letter is a digit plus the mark after it (none, `.`, `,`, `:`), so a comma or colon is part of the sign and not punctuation. Hungarian digraphs have one sign.

Key for the 11 distinct signs of this card (10 letters, since two signs share l):

| sign | letter | sign | letter |
|---|---|---|---|
| 0 | o/ó | 3 | d |
| 1. | a | 4, | g |
| 1: | e | 5, and 5. | l |
| 2, | cs | 7 | k |
| 2. | é | 8, | t |

The two forms of l are variants: `5.` is l in `a legszeb(b)` on hcp-1179 and is not attested as j anywhere in this family. The fuller family key is in hcp-1174/SOLUTION.md (and hcp-1179/SOLUTION.md); both of those are reviewed but not FINAL at the time of writing.

How the key came out: hcp-1174 begins with a 13-sign salutation that fits `Édes Margitkám`, and `téged`, `Mondd, hogy` appear there in clear. On those values the end of this card gives `téged`. This card's own `téged` was part of the work, so it is not an independent test of those values. The independent support is on the sisters: `ölelhetlek én`, `csókollak`, `a legszeb(b)`.

## Plaintext

Enciphered line: **csókollak téged** (signs give `csokollaktéged`; the writer does not mark ó).

English: "I kiss you". Slovak: „bozkávam ťa“.

Open text (not enciphered), struck through later in brown ink; read through the strokes:

```
[top margin] Vasárnap k[i]m[e]g[y]ek(?) egy [...] vonatnál.
Kedves Margitkám!
Üdvözöllek, Angyukádal
és a kis Mariskával
együtt üdvözlésedre
ezt a pársoros ver-
secskét írom!
Tavasszal is hull a
levél,  Hol a f[...] fujja(?) a szél,
A szivet is bánat tépi,
Hogyha zord csalódás
éri. (2,0705,5.1.78,2.4,1:3
ha tudod olvasd(?) el a szám betűt is)   Sz. A.(?) Mezőkövesd
```

English: "Dear Margitka of mine! I greet you, together with your ángyuka (aunt or sister-in-law by marriage; or: your mummy) and little Mariska, and to greet you I write this little verse of a few lines! Leaves fall in spring too, where the wind blows [one word unread]; the heart too is torn by sorrow when harsh disappointment strikes it. (I kiss you; if you can, read the number-letters as well) Sz. A.(?), Mezőkövesd." Margin: "On Sunday I (perhaps) go out ... a ... at the train."

Slovak: „Drahá moja Margitka! Pozdravujem ťa spolu s tvojou ángyukou (teta či švagriná, príbuzná cez manželstvo; alebo: mamičkou) a malou Mariškou a na pozdrav ti píšem tento veršík na pár riadkov! Aj na jar padá lístie, kde fúka vietor [jedno slovo neprečítané]; aj srdce trhá žiaľ, keď ho postihne kruté sklamanie. (bozkávam ťa; ak vieš, prečítaj aj číselné písmená) Sz. A.(?), Mezőkövesd.“ Okraj: „V nedeľu (azda) vyjdem ... jeden ... pri vlaku.“

Address: Tek. Szegedy Jánosné úrasszonynak, Szomolya, u. p. Bogács. A later brown pen retraced parts and tried dates (1848, 1918, 1920); this is not part of the message.

## Command

From the repo root: `python3 -I ciphers/hcp-1178/work/decode.py`
Checks source hashes, decodes `work/transcription.txt`, asserts the result, prints sister-card controls. The controls are hardcoded sign strings, so they show agreement of the key, not an independent proof.

## Uncertainties

Cipher line: none in the signs; all 13 are clear.

1. `5.` = l rests on the secure `a legszeb(b)` on hcp-1179 and on the expected formula; this card alone could not separate l from j. The mark on 5 does not distinguish a letter in this family, which is unusual for the cipher.
2. `2,` = cs occurs only in this word in the cards used here (also hcp-1174). `?okollak téged` points to `csókollak`.
3. `0` stands for ó here; the writer does not mark the long vowel.
4. Short ciphertext: 13 signs alone cannot prove a key; the reading depends on the sister-card key.

Open text (none of this affects the cipher):

5. Verse line 6, the word after `Hol a`: begins with f and has one descender in the middle (`work/crops/L6a_v.png`), but is not read. `fájót` and `fákat` are guesses only. `fuvalmas` of DONE1 is withdrawn. `fujja` is a fair reading, the double descender being the deciding feature, but is under heavy strokes.
6. Top margin: `Vasárnap` and `vonatnál` are firm, `egy` fair, `kimegyek` a suggestion; the word between `egy` and `vonatnál` stays unread (`work/crops/T1_v.png`, `T2_v.png`).
7. `Angyukádal`: the pixels do not separate g+y from y alone. I prefer `Angyukádal` = angyukáddal, from `ángy` (a female relative by marriage), because the addressee is Szegedy Jánosné and sister card hcp-1175 opens `Kedves Ángyika!` to her (from that directory's notes, not reviewed). It fits a greeting to Margitka "together with your ángyuka". `Anyukádal` ("with your mummy") stays possible. Either way -dal has single d for -ddal, as in `akor` on hcp-1175.
8. Signature: `Sz. A.` or `Sz. K.`. The capital is ambiguous on this card; hcp-1174 is signed Árpád, and that favours A.
9. `olvasd` could be `olvasod`; `ha tudod` is faint at its start.
10. The card is undated; the stamps' postmark is illegible apart from fragments.

## Why this is correct

All 13 signs were read on the hires scan at 4x and independently by the reviewer at 5x, with the same result (`work/crops/dig1.png`, `dig2.png`). Every sign maps with a value attested elsewhere in the family. The text is a normal Hungarian phrase. The same word `csókollak` closes hcp-1174 from the same writer to the same Margitka, and the writer's own note announces number-letters. The word `téged` comes out on a key whose sister-card passages read as Hungarian, though this card contributed to that key.

Limits: only 13 signs here, so the case rests on the family key, not on this line alone.

## Response to review 1

1. **`5.` = j wrong (major): fixed.** I looked at the hcp-1179 foot (`review/work/r79b.png`): the dot after 5 is clear in `1. 5. 1: 4, 7. 1: 1,`, which only reads as `a legszeb`. My "damaged passage" remark was wrong, and so was the `akor` argument, since this card spells `Üdvözöllek` in clear. Key, `decode.py`, assertion, plaintext and both translations now give `csókollak téged`. The sign reading itself is unchanged; on `work/crops/dig1.png` the first 5 has the comma and the second the dot.
2. **hcp-1174 "same sign" claim false (major): fixed.** On `review/work/c74.png` a small faint hooked comma follows the second 5. I had shaped the control on my misreading. The control is now `5, 5,`, and the claim is removed.
3. **Verse line 6 misread (major): fixed as far as the pixels allow.** New violet-minus-red crops (`work/crop7.py`, `work/crops/L6a_v.png`, `L6b_v.png`) plus the reviewer's `fuj.png`, `fuj2.png` confirm several close descenders before `a szél`, so `fuvalmas` is withdrawn in favour of `fujja`. The word before it stays unread and is bracketed. I do not adopt `fákat` or `fájó`. Translations are updated.
4. **`ver[s]cskét` (minor): fixed.** The second line plainly has `secskét`; now `ver-secskét`, with no bracket.
5. **`Angyukádal` (minor): fixed.** The pixels do not settle g on `review/work/anyu_b.png`. Both readings are disclosed (uncertainty 7), and the sense `ángy` is preferred because hcp-1175 addresses the same recipient as `Ángyika`. The confused "single l" note is replaced by the single-d point.
6. **Signature (minor): fixed.** Now `Sz. A.(?)`, with K disclosed (uncertainty 8).
7. **Top margin (minor): addressed.** `kimegyek` is now given as a suggestion only, and the remaining gap is stated.
8. **Overstated support (minor): fixed.** The "eleven of 13, unforced" claim is gone, and the role of this card's `téged` in the key is stated. The hcp-1175 passages, including `.1` = u, are dropped from the key and the controls because that card has no reviewed solution. The key table is reduced to this card's signs.
