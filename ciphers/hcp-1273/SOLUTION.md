# HCP1273 — Feri to Jolánka Tóth: after the dance, and why he cannot come on Sunday

**Status: complete reading of the ciphertext, revised after review 1 (verdict REVISE; see the response at the end).** Claude Opus 5.5, 2026-11-01. One short word in the unenciphered cursive note is unread. All work on this number is by Claude Opus 5.5; the key was taken from finished sister cards (mainly HCP1216, solved by the OpenAI GPT solver and completed by Claude Opus 5.5). The portal shows status *Not solved* with no transcription or solution attached; no published solution of this card was seen (no dedicated literature search was made; the portal cites the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166, not consulted). The transcription is mine (none attached), made by eye and not blind to the family's vocabulary.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the Jolánka family key of HCP1216 etc., unchanged. No sign needed a new value.

*2026-11-03:* type is now **MASC + Steganography**: a plain-Hungarian message is written in the stamp box, where the (now lifted) stamp covered it; see "Stamp-box message (2026-11-03)".

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl (with bar) | c | three short strokes | m | gamma/corner | t |
| short + long stroke, joined | d | two short strokes | n | plain X | u |
| three bars | e | loop with hook | o | chevron | v |
| upright cross | f | tall + short stroke | h / p | joined loop + descender (cy) | gy |
| open hook with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | opposed bowls | cs | low descender | y (ny = n + y) |

Dots/ticks over o and u give ö/ü. Other accents are not transcribed.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1273/work/decode.py
```

It checks the SHA-256 of both source scans and both hi-res originals, decodes the manual sign ledger `work/ledger.txt` (22 rows) and prints the literal letters, then the normalized text `work/normalized.txt`.

## Literal decipherment (as printed by the command; h = the h/p sign)

```
01 kedvesjolankambecses             12 hazamentemedesjolan
02 soraitmegkahtamegyerre           13 kamsajnalattalkeltu
03 fogadjaköszönetemetamu           14 datnihvasarnahleszaz
04 latsagbancsakmulattam            15 egyletbevalasztmanyi
05 mertmuszajvoltmert               16 ülesesemiatnemmehetekle
06 akitelfogadtamaval               17 avasarnahimulatastmeg
07 muszajvolttanczolni              18 irtamkedvesjolankamami
08 desokszorelgondoltam             19 averseitiletiazokegesz
09 haitletvolnaazencsil             20 aszivemighathaönszivbölir
10 lagomenyemvolnaatancz            21 jaamiboldogsagunkörökefogtartaniistenveleedesem
11 teremmaregyorakor                22 aviszontlatasrajövövasarnah
```

Rows 21–22 run on across the bottom edge of the whole card, under the address.

## Hungarian (normalized)

Kedves Jolánkám! Becses sorait megkaptam, [í]gy erre fogadja köszönetemet. A mulatságban csak mulattam, mert muszáj volt, mert akit elfogadtam, avval muszáj volt táncolni, de sokszor elgondoltam, ha itt lett volna az én csillagom, enyém volna a táncterem. Már egy órakor hazamentem.
Édes Jolánkám, sajnálattal kell tudatni, h[ogy] vasárnap lesz az egyletbe[n?] választmányi ülése, s e miatt nem mehetek le. A vasárnapi mulatást megírtam, kedves Jolánkám. Ami a verseit illeti, azok egész a szívemig hat, ha ön szívből írja, a mi boldogságunk örökké fog tartani. Isten vele, édesem, a viszontlátásra jövő vasárnap.

Unenciphered, in plain cursive in the stamp box, under the lifted stamp: Csókolom számtalanszor. Sírig hű szere[…]je [one word only partly read], Feri. (Corrected 2026-11-03; the earlier "[unread word] ke[dve]se(?)" is withdrawn.)

## English

Dear Jolánka! I have received your esteemed lines, so please accept my thanks for them. At the party I only enjoyed myself because I had to: whoever I had accepted as a partner, I had to dance with. But I often thought to myself: if my star had been here, the dance hall would have been mine. I went home already at one o'clock.
Sweet Jolánka, I regret to have to tell you that on Sunday there is a committee meeting in the association, and because of that I cannot come down. I have written about Sunday's party, dear Jolánka. As for your verses, they reach right to my heart; if you write them from the heart, our happiness will last forever. God be with you, my darling; until we meet next Sunday.

Under the stamp: I kiss you countless times. Faithful until the grave, your [one word only partly read: szere…je], Feri.

## Slovenčina

Milá Jolánka! Vaše vzácne riadky som dostal, prijmite preto moju vďaku. Na zábave som sa zabával len preto, že som musel: koho som prijal, s tým som musel tancovať. Ale často som si pomyslel: keby tu bola moja hviezda, tanečná sála by bola moja. Už o jednej hodine som išiel domov.
Sladká Jolánka, s ľútosťou Vám musím oznámiť, že v nedeľu bude v spolku zasadnutie výboru, a preto nemôžem prísť dolu. O nedeľnej zábave som už písal, milá Jolánka. Čo sa týka Vašich veršov, tie mi siahajú až k srdcu; ak ich píšete zo srdca, naše šťastie bude trvať navždy. S Bohom, drahá moja, dovidenia budúcu nedeľu.

Pod známkou: Bozkávam nespočetnekrát. Až do hrobu verný Váš [slovo prečítané len čiastočne: szere…je], Feri.

## Uncertainties

Signs under ink or overwriting:

1. **Row 2, the sign before `gy`**: an overwritten, unclear vertical sign with bars (ledger: e), then a paler, retraced gy. Literally *egy*; I normalize to *[í]gy*, which rests on sense only. It does not affect the clause's meaning much. *t* in *sorait* is also overwritten, with thin strokes showing beside it (earlier sign covered).
2. **Row 2 last sign**: the final e of *erre* is three bars with extra verticals forming a lattice (a flourish or a correction); taken as e from the word.
3. **Row 8 first sign**: a heavily retraced d, read from *de*; **restoration by sense**.
4. **Row 15 after `v`**: a thin top bar and a solid blot, so a and e cannot be told apart. *a* is a **restoration** from *választmányi*.
5. **Row 15 `be`**: three bars, read literally. I adopt, as a proposal, *egyletbe(n)*, dialect -be for -ben ("in the association"), which needs no omitted letter. Alternatives stay open: *az egylet bel-választmányi ülése* ("the association's inner-committee meeting") needs an omitted l; *bál-választmányi* ("ball committee") would suit the dance context but needs a wrong vowel and an omitted l. "Committee meeting" is secure under all three.
6. **Row 16**: a pink blot covers the e of *nem* (**restoration**, only one word fits). The two strokes of the n stand beside the blot; I read them as n, not a second t, so *miat* has one t. Literal *ülesese* is divided *ülése, s e [miatt]* ("meeting, and because of this"); no sign is deleted. All three e and both s are clean. (Round 1 treated it as a dittography; that was unnecessary.) The ü sign is a blotted X with dots above it.
7. **Row 21 end**: the final m of *édesem* is three strokes bent sideways at the card's edge; a pink mark touches them. Word sense supports m. In *vele* the last e lies under the grey collector's stamp but its bars are visible.
8. **a/e after gamma**: the arm of t sits over the following bars and can look like a third bar (*mulattam, tartani, tanczolni, fogadtam, irtam, mulatast*). I count only the bars below the arm, and the words confirm a. Row 4 *csak* has two bars linked by a diagonal pen stroke. Round 1 also miscounted four clean signs elsewhere, each toward an expected word (see the response to findings 1 to 4 and 6), so after review I rechecked the a/e bar counts of all 22 rows on enlarged crops; no further sign changed.
9. **Row 18**: the j of *Jolánkám* has a stem slightly crossing its base and could be taken for f; j from the name. **Row 21**: `bo(l)dog`, the l is a tiny stroke attached to the o.
10. **h/p, by word sense**: `megkahtam`→p, `vasarnah`→p (three times), `h` in row 14 and the rest →h. Row 14 has a lone h, read as the common abbreviation h. = *hogy*.
11. **d/n, by word sense**: row 8 *gondoltam*, rows 1/12/18 d of *kedves/édes* are long-stroke d; all other pairs are short n.

Writer's spelling, normalized: *mer* → mert (row 5, also on HCP1216), *aval* → avval, *let* → lett, *it* → itt, *miat* → miatt, *keltu|datni* → kell tudatni, *ileti* → illeti, *öröke* → örökké, *tancz-* is old spelling. Line breaks *csil|lagom*, *tancz|terem*, *mu|latsagban*, *Jolan|kam*, *tu|datni* fall mid-word.

Also uncertain:

12. **Cursive note over the stamp (plain text, not ciphertext)**: *csokolom / szamtalan / szor sirig / hű …* is clear. The word after *hű* looks like "pene", the next line like "ketse"; the postage print and a hole interfere. I read the ending as a form of *kedvese* only by analogy with HCP1216 ("sírig hű kedvese Feri"), and do not claim it. *2026-11-03: superseded; see "Stamp-box message (2026-11-03)": the two lines read szere / tetje, one word, not kedvese.* The signature begins *Fer*, then runs into a stain; *Feri* is a reading supported by the sister cards.
13. **Address (plain)**: Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás. Parts lie under the cancel and the collector's stamp. Postmark shows MAJ; the year comes from the portal file name (1912-05-04), not checked on the cancel.
14. The picture side has only printed captions (Sirassatok engem orgonavirágok…; Kis falumat nem látom én soha többé / Búcsút mondok, búcsút veszek / Mindörökké), no cipher.

## Why it is correct

- The key comes unchanged from finished cards; every sign of all 22 rows gets a value and the output is continuous Hungarian with no gap.
- The words break naturally and repeat identically: *Jolánkám* ×3, *vasárnap* ×3 (two plus *vasárnapi*), *muszáj volt* ×2, *mert* ×2, *volna* ×2.
- Long, unlikely strings arise unaided: *köszönetemet*, *választmányi*, *boldogságunk*, *viszontlátásra*, *sajnálattal*.
- The content fits the family: formal *ön* address, signature Feri, Jolánka Tóth of Jászárokszállás; *csókolom számtalanszor, sírig hű* matches HCP1216's closing.

## Response to review 1

Each sign below was reread by me on the reviewer's enlargements (review/work/crops/) and the row crops. Fixed in `work/ledger.txt`, `work/normalized.txt` and this file; `python3 -I ciphers/hcp-1273/work/decode.py` rerun: all four hashes OK, output identical to the literal and normalized text above, 477 tokens.

1. **Fixed.** Row 10 has one group of three strokes between the o and the three-bar e (`r10m`), so *csillagom, enyém volna a táncterem*. "Mennyem" and its spelling note are gone.
2. **Fixed.** Row 11: the sign after mm is two hooked bars, clearly fewer than the three of the following e (`r11mar`), so *már egy órakor hazamentem*. The emendation mer[t] and the non-sequitur are gone. One sentence now ends at *táncterem*.
3. **Fixed.** Row 8: the sign after r has three clear bars (`r8e`), so *sokszor elgondoltam*; "[al]" and the *sokszorral* speculation are removed.
4. **Fixed.** Row 6 last word is `aval` (two clean bars, `r6end`); ledger, literal text and spelling note changed.
5. **Adopted.** *ülése, s e miatt* deletes no sign, and I confirm the letters on `r16b`. *egyletbe(n)* is adopted as a proposal only, with the bel-/bál- alternatives kept (uncertainty 5).
6. **Addressed.** Uncertainty 8 now records that the errors were not limited to signs after gamma. I rechecked a/e bar counts across all 22 rows on the crops; no further change. Signs that remain under ink stay listed as restorations.
7. **Fixed.** English and Slovak regenerated; *akit elfogadtam* now "koho som prijal", English "whoever I had accepted as a partner". "Why it is correct" stays true unchanged: its counts (*mert* ×2, *volna* ×2) do not depend on the corrected signs.
8. **Fixed.** Key table has its own row for the low-descender y, as on HCP1216; ny is n + y here (rows 10, 15).

Also corrected on my own check of the picture side, which the reviewer left open: the caption reads *Sirassatok*, not "Szirassatok" (uncertainty 14). It carries printed text only, no cipher.

## Stamp-box message (2026-11-03)

Audit by Claude Opus 5.5 on the hi-res address scan (`work/hires/…_adr.jpg`), crops in `work/stamp-2026-11-03/` (`box_context_1x.png`, `box_2x.png`, `line4_4x.png`, `line5_4x.png`, `line5_left_6x.png`; `word4_sep_5x.png` and `line5_sep_4x.png` separate the red ink from the pink printed emblem).

**State of the box:** the stamp has been lifted. The dotted stamp frame is empty except for gum stains and two small green fragments of the stamp paper (left edge and bottom of the frame), and the second postmark's ring breaks off at the frame, because the cancel struck the stamp that is gone. The writing therefore lay under the stamp. It is in plain Hungarian cursive in the same red ink, not in the cipher signs. A pale pink printed emblem (wreath with R) lies under the writing and is not part of the message.

**Literal reading, line by line:** `csokolom` / `szamtalan` / `szor sirig` / `hű szere` / `tetje` / `Feri`.

- Lines 1 to 3 and *hű* are clear.
- Line 4 after *hű*: s, z (crossed, as in *szor*), e, r (an n-like hump, the same r as in *szor*), e. Round 1 read "pene"; on the ink-separated crop the first sign is the writer's small s, not p.
- Line 5: t (bar across a stem), e, a second crossed t-like sign, j (dot above, loop below; a hole touches the loop), e. Round 1 read "ketse"; the first sign has no k loop and the fourth has a dot and a descender, so j.
- Signature: F, e, r (n-like), i; the end runs into a stain. *Feri* as on the sister cards.

Lines 4 and 5 join as one word, literally *szeretetje*. That is not a normal Hungarian form. The nearest family word is *szeretője* ("his lover/sweetheart"), but it needs ő where I see e plus a crossed sign, so I do not adopt it. *kedvese* does not fit the strokes and is withdrawn.

**Normalized Hungarian:** Csókolom számtalanszor. Sírig hű szere[…]je(?), Feri.
**English:** I kiss you countless times. Faithful until the grave, your [word starting szere-, ending -je, not read], Feri.
**Slovak:** Bozkávam nespočetnekrát. Až do hrobu verný Váš [slovo začínajúce szere-, končiace -je, neprečítané], Feri.

**Unread:** the one noun after *hű*. Its letters are read (szere|tetje) but they make no word I can confirm; *szeretője* is only a candidate. Everything else in the box is read.

The reproduction script `work/decode.py` covers the ciphertext ledger only. The stamp text is plain cursive and is read by eye; the script was not changed.
