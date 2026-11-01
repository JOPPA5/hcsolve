# HCP 1273: Feri to Jolánka Tóth, after the dance

Human solver: Tomáš Pavuk

**Status: the cipher text is read in full (477 signs in 22 rows). Independent review 1 gave the verdict REVISE; four signs and two word divisions were corrected, and solver and reviewer readings now agree on all 477 signs. One word in the unenciphered note over the stamp stays unread.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1273 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1273), portal name *cpc_1912-05-04_HU__HU_Jasz Arokszalas_jolanka-18*, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The date 1912-05-04 comes from the portal's file name; the postmark on the card shows MAJ and a day that looks like 4, but the year cannot be read.

It is a Hungarian romantic picture postcard: a young woman sits with lilac while a young man with a bouquet appears in a vision behind her. The printed captions read *Sirassatok engem orgonavirágok…* ("Weep for me, lilac blossoms…") and *Kis falumat nem látom én soha többé / Búcsút mondok, búcsút veszek / Mindörökké* ("I shall never see my little village again / I say farewell, I take my leave / for evermore"). The picture side has no cipher.

The address side is written in red ink. The right half carries the plain address *Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás* ("To the promising young lady Jolánka Tóth, Jászárokszállás"). The cipher fills the left half and runs on along the whole bottom edge, beneath the address. A short note in ordinary cursive is written over the stamp.

The card belongs to a family of postcards to Jolánka Tóth in the same cipher, several of which are solved in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). This card was read with that **known, transferred key**; it is not a new key recovery. No published solution of this card was seen, but no dedicated literature search was made, and the HistoCrypt paper cited on the portal (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166) was not consulted.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: cipher at the left and along the bottom edge, address at the right, cursive note over the stamp (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is manual, made from enlarged crops of the high-resolution address scan, and is not blind: the solver knew the family's vocabulary. Each written sign is one token in a sign ledger of 22 rows, and a script checks the hashes of the scans, decodes the ledger and prints the text. Word division, accents and spelling in the normalized text are editorial.

The key from HCP 1216 applied unchanged. No sign needed a new value, and all 22 rows yield continuous Hungarian. Long, unlikely words arise unaided (*köszönetemet, választmányi, boldogságunk, viszontlátásra, sajnálattal*), and words repeat identically (*Jolánkám* three times, *vasárnap* three times, *muszáj volt* twice).

In review a separate agent read all rows independently on its own crops and compared its reading with the ledger by script; see "Review" below.

## Key

Simple monoalphabetic substitution with invented graphic signs. The names below describe the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl with bar | c | three short strokes | m | gamma or corner | t |
| short + long stroke, joined | d | two short strokes | n | plain X | u |
| three bars | e | loop with hook | o | chevron | v |
| upright cross | f | tall + short stroke | h / p | joined loop + descender | gy |
| open hook with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | opposed bowls | cs | low descender | y (ny = n + y) |

Dots or ticks over o and u give ö and ü. Other accents are not written or cannot be seen at this resolution, so all acute accents below are editorial. The h/p sign is a near-homograph: h or p is chosen by word sense.

## Plaintext

Literal decipherment by written row (h stands for the h/p sign):

```text
01 kedvesjolankambecses
02 soraitmegkahtamegyerre
03 fogadjaköszönetemetamu
04 latsagbancsakmulattam
05 mertmuszajvoltmert
06 akitelfogadtamaval
07 muszajvolttanczolni
08 desokszorelgondoltam
09 haitletvolnaazencsil
10 lagomenyemvolnaatancz
11 teremmaregyorakor
12 hazamentemedesjolan
13 kamsajnalattalkeltu
14 datnihvasarnahleszaz
15 egyletbevalasztmanyi
16 ülesesemiatnemmehetekle
17 avasarnahimulatastmeg
18 irtamkedvesjolankamami
19 averseitiletiazokegesz
20 aszivemighathaönszivbölir
21 jaamiboldogsagunkörökefogtartaniistenveleedesem
22 aviszontlatasrajövövasarnah
```

**Hungarian (normalized).** Kedves Jolánkám! Becses sorait megkaptam, [í]gy erre fogadja köszönetemet. A mulatságban csak mulattam, mert muszáj volt, mert akit elfogadtam, avval muszáj volt táncolni, de sokszor elgondoltam, ha itt lett volna az én csillagom, enyém volna a táncterem. Már egy órakor hazamentem.

Édes Jolánkám, sajnálattal kell tudatni, h[ogy] vasárnap lesz az egyletbe[n?] választmányi ülése, s e miatt nem mehetek le. A vasárnapi mulatást megírtam, kedves Jolánkám. Ami a verseit illeti, azok egész a szívemig hat, ha ön szívből írja, a mi boldogságunk örökké fog tartani. Isten vele, édesem, a viszontlátásra jövő vasárnap.

Unenciphered, over the stamp: Csókolom számtalanszor. Sírig hű [unread word] ke[dve]se(?), Feri.

**English.** Dear Jolánka! I have received your esteemed lines, so please accept my thanks for them. At the party I only enjoyed myself because I had to: whoever I had accepted as a partner, I had to dance with. But I often thought to myself: if my star had been here, the dance hall would have been mine. I went home already at one o'clock.

Sweet Jolánka, I regret to have to tell you that on Sunday there is a committee meeting in the association, and because of that I cannot come down. I have written about Sunday's party, dear Jolánka. As for your verses, they reach right to my heart; if you write them from the heart, our happiness will last forever. God be with you, my darling; until we meet next Sunday.

Over the stamp: I kiss you countless times. Faithful until the grave, [unread word] your sweetheart(?), Feri.

**Slovensky.** Milá Jolánka! Vaše vzácne riadky som dostal, prijmite preto moju vďaku. Na zábave som sa zabával len preto, že som musel: koho som prijal, s tým som musel tancovať. Ale často som si pomyslel: keby tu bola moja hviezda, tanečná sála by bola moja. Už o jednej hodine som išiel domov.

Sladká Jolánka, s ľútosťou Vám musím oznámiť, že v nedeľu bude v spolku zasadnutie výboru, a preto nemôžem prísť dolu. O nedeľnej zábave som už písal, milá Jolánka. Čo sa týka Vašich veršov, tie mi siahajú až k srdcu; ak ich píšete zo srdca, naše šťastie bude trvať navždy. S Bohom, drahá moja, dovidenia budúcu nedeľu.

Nad známkou: Bozkávam nespočetnekrát. Až do hrobu verný [neprečítané slovo] Váš milý(?), Feri.

The writer's spelling is normalized: *mer* to *mert*, *aval* to *avval*, *let* to *lett*, *it* to *itt*, *miat* to *miatt*, *keltudatni* to *kell tudatni*, *ileti* to *illeti*, *öröke* to *örökké*. *Tancz-* is old spelling.

## What remains uncertain

- **Row 2, the sign before gy**: overwritten and unclear, literally e. *[Í]gy* ("so") is chosen by sense only; *egy* is the literal alternative. The final e of *erre* has extra strokes forming a lattice and is taken from the word.
- **Restorations by sense**: the heavily retraced d in row 8 (*de*); the vowel after v in row 15, where a thin bar and a blot leave a and e undecided (*választmányi*); the e of *nem* in row 16 under a pink blot, with bars visible through it; the last e of *vele* in row 21 under the collector's stamp, also with bars visible; the m of *édesem* at the card's edge.
- **Row 15, *be***: *egyletbe(n)* ("in the association", dialect -be for -ben) is a proposal. Alternatives are *az egylet bel-választmányi ülése* ("inner-committee meeting", needing an omitted l) and *bál-választmányi* ("ball committee", needing a wrong vowel and an omitted l). "Committee meeting" holds under all three.
- **Calls that rest on word sense**: p for the h/p sign in *megkaptam* and *vasárnap*; a lone h in row 14, read as the common abbreviation of *hogy*; d against n in *gondoltam, kedves, édes*; j in row 18 of *Jolánkám*, which could be taken for f; the tiny l of *boldogságunk*.
- **Cursive note over the stamp** (plain text, not cipher): *csokolom / szamtalan / szor sirig / hű* is clear. The next words look like "pene" and "ketse". Print and a hole interfere; *kedvese* is read only by analogy with HCP 1216, and neither solver nor reviewer could read the word before it. *Feri* is supported by the sister cards.
- **Date**: the year rests on the portal's file name, not on the postmark.
- **Published solutions**: no search of the literature was made, as stated above.

## Review and what changed

The review was made by a separate Claude Opus 5.5 agent, which reran the reproduction command, read all rows independently and compared the result by script: 474 tokens agreed and four differed. Its verdict was REVISE. The solver rechecked each finding on the scan and accepted all of them:

1. Row 10 has one m, not two, so the word is *enyém*, not "mennyem": "the dance hall would have been mine", not "my heaven".
2. Row 11 is *már*, not "mer[t]": the sign has two bars, not three, which removes an emendation and a non-sequitur ("for I went home at one o'clock").
3. Row 8 is *sokszor elgondoltam*, not "sokszor[al] gondoltam".
4. Row 6 ends literally *aval*, not *avel*.
5. *Ülésese* needs no deletion: it divides as *ülése, s e [miatt]*. *Egyletbe(n)* was adopted as a proposal.
6. The errors above were bar miscounts in clean signs, each leaning toward an expected word, so the a/e counts of all 22 rows were rechecked; nothing further changed.
7. The translations were regenerated, and *akit elfogadtam* made closer.
8. The key table gained the low-descender y, used for ny.

![Row 10: g, o, one group of three strokes (m), e, n, y: "...gom enyem" (review/work/crops/r10m.png)](../review/work/crops/r10m.png)

![Row 11: the two hooked bars of a, then r and the three bars of e: "mar e..." (review/work/crops/r11mar.png)](../review/work/crops/r11mar.png)

After the changes the two independent readings agree on all 477 tokens, and the reproduction command prints the text above. The reviewer did not check the picture side; the solver did, and corrected the caption spelling. The reviewer's comparison does not replace a fully blind second transcription of the disclosed doubtful signs, which remain as listed.

To reproduce, run from the repository root: `python3 -I ciphers/hcp-1273/work/decode.py`
