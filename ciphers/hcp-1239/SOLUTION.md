# HCP1239 — to Jolánka Tóth, June 1912: an apology and an invitation to a song soirée

**Status: complete reading of the ciphertext with disclosed residual points; the cursive signature in the stamp box is unread.** Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. The portal shows status Not solved and attaches no transcription or solution; no published solution was found. The transcription and normalization are mine; the key comes from finished sister cards, above all HCP1216.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the Jolánka family key, as tabulated in `ciphers/hcp-1216/SOLUTION.md`. The address (Szép reményű Tóth Jolánka úrleánynak, Jászárokszállás) is in clear. Points specific to this card:

- A closed figure-8 sign is a variant of k (*hetek*, *urékat*, *ki*, *kedves*).
- The d-shaped sign (short tick left, long stroke right) also has to serve as p in *megkaptam* and as h in *hetek* (row 6). The h/p sign proper is long left, short right.
- The plain cross is u, the tailed cross is z, and s + tailed cross is sz.
- The picture side has only printed text (Asszonykám adj egy kis kimenőt; four lines naming Petőfi: Szabadság, szerelem...). It has no cipher.

**Type note (2026-11-03, Claude Opus 5.5):** register type changed from `MASC` to **`MASC + Steganography`**: the stamp was lifted and five rows of cipher signs plus a cursive word were written in the stamp box, hidden under the stamp (see "Stamp-box message (2026-11-03)" below).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1239/work/decode.py
```

It checks the SHA-256 of all four images, decodes `work/ledger.txt` (one token per written sign, read by eye from enlarged crops) and prints the literal rows followed by `work/normalized.txt`.

## Literal decipherment

```
01 kedvesjolankambecses          11 moczarurekatismeg
02 soraitkoszonetel              12 hivtamaszonysagal
03 megkaptamigazansajna-         13 iseljönethacstehti
04 lomhogyenmiattam              14 jöjöneledesembiszta
05 anyitszenveddenemte           15 tovalaszatvarva
06 hetekrolakedvesjo             16 maradoköszintetisz
07 lankamjojjönela               17 telöjeistenvele
08 dalestejrecsütör              18 aviszontlatasra:
09 törtokönidefeke               19 engesztel[j][#]ljekikedvesmamajaesahjattisz (bottom edge)
10 teruhabaniseljöhet            20 teletemet (bottom right)
stamp box: csokolom | szamta | lanszor | istenve | le | [cursive signature]
```

## Hungarian (normalized)

Kedves Jolánkám! Becses sorait köszönettel megkaptam. Igazán sajnálom, hogy én miattam annyit szenved, de nem tehetek róla. Kedves Jolánkám, jöjjön el a dalestélyre csütörtökön ide. Fekete ruhában is eljöhet. Móczár urékat is meghívtam asszonysággal, is eljönnek. Ha [csak] teheti, jöjjön el, édesem. Biztató válaszát várva maradok őszinte tisztelője. Isten vele, a viszontlátásra:

Engesztelje ki kedves mamáját és apját. Tiszteletemet.

Stamp box: Csókolom számtalanszor. Isten vele. [signature unread]

## English

Dear Jolánka! I received your esteemed lines with thanks. I am truly sorry that you suffer so much because of me, but I cannot help it. Dear Jolánka, come to the song soirée here on Thursday. You may come in a black dress too. I have also invited Mr Móczár and his family, with his wife; they are coming too. If you [only] can, do come, my sweet. Awaiting your encouraging reply, I remain your sincere admirer. God be with you, until we meet again.
Make peace with your dear mother and father. My respects.
Stamp box: I kiss you countless times. God be with you. [signature unread]

## Slovak

Milá Jolánka! Vaše vzácne riadky som s vďakou dostal. Naozaj ľutujem, že kvôli mne toľko trpíte, ale nemôžem za to. Milá Jolánka, príďte vo štvrtok sem na pesničkový večierok. Môžete prísť aj v čiernych šatách. Pozval som aj pána Móczára s rodinou a s manželkou, aj oni prídu. Ak [len] môžete, príďte, drahá. V očakávaní Vašej povzbudivej odpovede zostávam Váš úprimný ctiteľ. S Bohom, dovidenia.
Uzmierte si drahú mamu a otca. Moja úcta.
V rámčeku na známku: Bozkávam Vás nespočetnekrát. S Bohom. [podpis neprečítaný]

## Uncertainties

Accents are not transcribed in the ledger and are supplied in normalization; dots are marked only where seen.

1. **Stamp-box signature.** A connected cursive word, not family signs as far as I can tell. I cannot read it and do not force it. Feri, the sender on many sister cards, is not confirmed here; the card is effectively unsigned.
2. **Row 19, the weakest point.** *engesztel* is followed by a cross, preferably the j-sign (low flat foot, as in the j two signs later, not the mid-height bar of f), then a solid blot with a hook on top, then *lje ki*. I take *-lj-* as written, the cross and blot being a false start blotted out and restarted, and read *engesztelje ki*. That deletion is an interpretation from sense, not a sign reading. The third sign is cut by the card edge and smeared: it shows an s/k-like top and is read g only from the word.
3. **Row 8, *dalestélyre*.** The first signs are blotted: a blotted short upper left stroke, a thin long pink stroke to its right, then two blotted bars. That is the d shape followed by a, so *dal* is read from the shape, but it remains partly blotted. *Pál* or *hál* (h/p) and *nál* (two strokes) are less likely on the shapes; *bál* is not supported, as no six sign is seen. Literal *estejre* needs only the writer's documented j for ly (HCP1212) to give *estélyre*; *dalestély* (song soirée) suits the note about dress.
4. **Row 13, *iseljönet*.** The last sign is a clear t-sign where *eljönnek* needs k, with one n. I normalize to *is eljönnek* ("they are coming too") from sense. The clause division and comma before it are editorial; the card has no punctuation here.
5. **Row 13, *hacstehti*.** Literal *ha cs tehti*; I normalize to *ha [csak] teheti*, supplying *ak* and *e*. The h of *tehti* is the proper h (long left, short right). The h of *hetek* in row 6 is the d-shaped sign, read h from sense.
6. **Row 14, *édesem*.** The fourth sign of *e d e ? e m* is a heavy blot over a loop, closer to the k-8 than to s; s is read from sense. *édesem* jars slightly with the otherwise formal tone but is the family's usual word.
7. **Row 5, *szenved de*.** Literal *szenvedde* divides without emendation into *szenved | de*. The second d is a pale long stroke with a short red left tick, the d shape, followed by three-bar e.
8. **Row 19, *mamaja es ahjat*.** Literal *mamája* lacks the final t of *mamáját* (writer's omission, supplied). The s of *és* is a blot taken as s, and the fused two strokes of *apját* are read as the h/p sign, p by sense. *tiszteletemet* stands alone with no verb; I give it as an elliptical closing.
9. **Other writer's spellings normalized:** *koszonetel* → köszönettel, *anyit* → annyit, *csütör | törtokön* → csütörtökön (*tör* repeated across the row break), *aszonysagal* → asszonysággal, *jöjön* → jöjjön, *bisztato* → biztató (s + z written).
10. **Date and origin.** The postmark shows 912 JUN and a place beginning JÁSZ; the rest of the place name and the day are not legible. Row 8 says Thursday but no calendar date.

## Why it is correct

- The family key, unchanged except for the disclosed k variant, turns all 20 rows and the stamp box into Hungarian, leaving only the signature and the two signs taken as deleted.
- Repeated words agree across the card: *kedves* ×3, *Jolánkám* ×2, *jöjjön/jöjön*, *isten vele* ×2, *is* ×3.
- Unforced phrases emerge across row breaks: *sajná-lom*, *te-hetek róla*, *feke-te ruhában*, *meg-hívtam*, *biszta-tó válaszát*, *tisz-telője*, *tisz-teletemet*. The writer's own hyphen in row 3 falls exactly in *sajná-lom*.
- Móczár recurs on sister cards, spelt the same way: "mondja meg Moczárnak" (HCP1295) and *hazamegy moczarhoz* (HCP1232, row 11).
- The formulas match the family: *Becses sorait köszönettel megkaptam* (HCP1212), *Isten vele*, *csókolom számtalanszor* (HCP1216). The addressee, town and 1912 date fit the card's clear text and postmark.

## Stamp-box message (2026-11-03)

Stamp-box audit, Claude Opus 5.5, 2026-11-03, on fresh crops of `work/hires/*_adr.jpg` (`work/stamp-2026-11-03/`, 2-5x, green channel where the blue printed emblem crosses the red ink). The stamp is lifted; the paper is bare inside the dashed box apart from the printed blue emblem and brown glue staining at the top. Under the stamp the sender wrote five rows in the family cipher signs and one cursive word in plain script. The signs were read again from the pixels and agree with ledger rows S1-S5 (already printed by `work/decode.py`, which still passes; nothing was changed in the script).

- Literal: `csokolom | szamta | lanszor | istenve | le | [cursive word]`
- Signs: opposed bowls + loop + section + loop + wave + loop + three strokes (cs o k o l o m); right bowl + tailed cross, two bars, three strokes, gamma, two bars (sz a m t a); wave, two bars, two strokes, right bowl + tailed cross, loop, F (l a n sz o r); dotted i, right bowl, gamma, three bars, two strokes, chevron, three bars (i s t e n v e); wave, three bars (l e).
- Hungarian: Csókolom számtalanszor. Isten vele. [signature unread]
- English: I kiss you countless times. God be with you. [signature unread]
- Slovak: Bozkávam Vás nespočetnekrát. S Bohom. [podpis neprečítaný]

Unread: only the cursive word after *le*: a looped capital like H or F, then three or four connected small letters ending in a descender. It is not forced (Feri is not confirmed). Every cipher sign in the box is read; no clause is left unread.

## Response to review 1

Verdict REVISE. All six findings are addressed. I rechecked the crops named in findings 1 to 4 myself and agree. No sign value changed; `python3 -I ciphers/hcp-1239/work/decode.py` was re-run after the fixes and all four hashes are OK, with the literal rows unchanged except the row 19 deletion marker.

1. **Row 5 (major): fixed.** On the crop the second d is a pale long stroke with a short left tick, followed by three-bar e, so the card reads *szenved, de nem tehetek róla*. `work/normalized.txt`, English, Slovak and uncertainty 7 are changed. The sentence is now present tense, with the written *de*.
2. **Row 8 (major): fixed.** Normalized to *dalestélyre* by the writer's j for ly (HCP1212, key section). The translations say song soirée and uncertainty 3 is reworded; *dal* stays disclosed as partly blotted.
3. **h/d note (minor): fixed.** The crops confirm it. Ledger row 6 first token is now `D>h`, row 13 h is plain `H`. The key note and uncertainty 5 are corrected. The letters do not change.
4. **Row 19 cross (minor): fixed.** The low flat foot matches the j-sign, so j is now the preferred value: ledger token `{J}`, printed `[j]`, in place of `{+}`, in `work/ledger.txt` and `work/decode.py`. *Engesztelje ki* is kept as the weakest point in uncertainty 2.
5. **Row 13 punctuation (minor): addressed by note.** I keep the comma because neither alternative is better Hungarian, and uncertainty 4 now says the division and comma are editorial. The letters do not change.
6. **Móczár cross-reference (minor): added, with a correction.** The phrase the review quotes, *hazamegy moczarhoz*, is on HCP1232 row 11, not on HCP1295. HCP1295 has "mondja meg Moczárnak". Both are cited under Why it is correct.

The changes are normalization and documentation only, so no second review round is needed, as the review itself states.
