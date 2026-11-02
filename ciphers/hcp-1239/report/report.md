# HCP 1239 (cpc_1912-06-_HU__HU_Jasz Arokszalas_jolanka-105): an apology and an invitation to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: all 20 rows and the five cipher rows in the stamp box read as Hungarian; one cursive word in the stamp box is unread and row 19 has one interpreted deletion. Independent review 1 verdict REVISE; its findings are addressed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1239 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1239), portal name cpc_1912-06-_HU__HU_Jasz Arokszalas_jolanka-105, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution was found or used.

The address is in clear, in red ink: **Szép reményű Tóth Jolánka úrleánynak, Jászárokszállás** ("To the young lady of fair promise, Jolánka Tóth, Jászárokszállás"). The postmark shows 912 JUN and a place name beginning JÁSZ; the day and the rest of the name are not legible. The message fills the left half of the address side in invented signs, 18 rows, with two further rows along the bottom edge and five short rows in the stamp box.

The picture side has only printed text (Asszonykám adj egy kis kimenőt, and four lines naming Petőfi: Szabadság, szerelem...). It has no cipher.

![Address side with the cipher text, the clear address and the stamp box (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, printed text only (source/picture-large.jpg)](../source/picture-large.jpg)

The card belongs to the Jolánka family of postcards, addressed to Jolánka Tóth in the same cipher; several are signed Feri. This card is effectively unsigned, so Feri is likely but not confirmed as its writer.

## Method

The key was **transferred** from finished sister cards, above all HCP 1216; this is not a new key recovery. The solver read the address side sign by sign from enlarged crops of the un-converted original scan and recorded one token per written sign in work/ledger.txt. The script work/decode.py checks the SHA-256 of the four images, decodes the ledger, and prints the literal rows and the normalized text:

```text
python3 -I ciphers/hcp-1239/work/decode.py
```

In review, the reviewer read every row on its own crops and keyed its own transcription. Sixteen of 20 rows agreed letter for letter, and the other four differed only at signs already disclosed or at the h/p/d call settled by the word. The reviewer had seen the solver's plaintext first, so this was a check, not a blind reading.

## Key

Simple monoalphabetic substitution with invented graphic signs; the Hungarian plaintext is written with digraphs spelled sign by sign (cs, gy, sz). The full table is in the HCP 1216 report. Points specific to this card:

- A closed figure-8 sign is a variant of k (hetek, urékat, ki, kedves).
- The d-shaped sign (short left, long right) also serves as p in megkaptam and as h in hetek (row 6). The proper h/p sign is long left, short right. These two calls rest on the word.
- The plain cross is u, the tailed cross is z, and s + tailed cross is sz.
- The writer uses j for ly, as stated on HCP 1212.

## Plaintext

Literal decipherment, row by row ([j] [#] are signs taken as deleted):

```text
01 kedvesjolankambecses
02 soraitkoszonetel
03 megkaptamigazansajna-
04 lomhogyenmiattam
05 anyitszenveddenemte
06 hetekrolakedvesjo
07 lankamjojjönela
08 dalestejrecsütör
09 törtokönidefeke
10 teruhabaniseljöhet
11 moczarurekatismeg
12 hivtamaszonysagal
13 iseljönethacstehti
14 jöjöneledesembiszta
15 tovalaszatvarva
16 maradoköszintetisz
17 telöjeistenvele
18 aviszontlatasra:
19 engesztel[j][#]ljekikedvesmamajaesahjattisz
20 teletemet
S1 csokolom
S2 szamta
S3 lanszor
S4 istenve
S5 le
```

**Hungarian (normalized):**

Kedves Jolánkám! Becses sorait köszönettel megkaptam. Igazán sajnálom, hogy én miattam annyit szenved, de nem tehetek róla. Kedves Jolánkám, jöjjön el a dalestélyre csütörtökön ide. Fekete ruhában is eljöhet. Móczár urékat is meghívtam asszonysággal, is eljönnek. Ha [csak] teheti, jöjjön el, édesem. Biztató válaszát várva maradok őszinte tisztelője. Isten vele, a viszontlátásra:

Engesztelje ki kedves mamáját és apját. Tiszteletemet.

Stamp box: Csókolom számtalanszor. Isten vele. [cursive signature, unread]

**English:**

Dear Jolánka! I received your esteemed lines with thanks. I am truly sorry that you suffer so much because of me, but I cannot help it. Dear Jolánka, come to the song soirée here on Thursday. You may come in a black dress too. I have also invited Mr Móczár and his family, with his wife; they are coming too. If you [only] can, do come, my sweet. Awaiting your encouraging reply, I remain your sincere admirer. God be with you, until we meet again.

Make peace with your dear mother and father. My respects.

Stamp box: I kiss you countless times. God be with you. [signature unread]

**Slovak:**

Milá Jolánka! Vaše vzácne riadky som s vďakou dostal. Naozaj ľutujem, že kvôli mne toľko trpíte, ale nemôžem za to. Milá Jolánka, príďte vo štvrtok sem na pesničkový večierok. Môžete prísť aj v čiernych šatách. Pozval som aj pána Móczára s rodinou a s manželkou, aj oni prídu. Ak [len] môžete, príďte, drahá. V očakávaní Vašej povzbudivej odpovede zostávam Váš úprimný ctiteľ. S Bohom, dovidenia.

Uzmierte si drahú mamu a otca. Moja úcta.

V rámčeku na známku: Bozkávam Vás nespočetnekrát. S Bohom. [podpis neprečítaný]

## What remains uncertain

Accents are not transcribed sign by sign; they are supplied in normalization.

- **Stamp-box signature.** One connected cursive word, starting with a looped capital. Neither solver nor reviewer can read it, and it is not forced. It stands alone, so it does not leave a clause unread.
- **Row 19, the weakest point.** After engesztel come a low-footed cross (the j-sign) and a solid blot, then lje ki. They are taken as a false start, blotted and restarted. That deletion is an interpretation. The third sign, cut by the card edge, shows an s/k-like top and is read g only from the word engesztelje. The s of és and the fused p of apját also rest on sense.
- **Row 8, dal.** The opening d + a is blotted; the d shape is visible but the word is partly read from sense.
- **Row 13.** Literal iseljönet ends in a clear t-sign where eljönnek needs k, and ha cs tehti is expanded to ha [csak] teheti. The comma before is eljönnek is editorial.
- **Row 14, édesem.** The fourth sign is an overwritten blot, read s from sense.
- **Date and identity.** Thursday is named with no calendar date. Neither the sender nor Móczár has been identified historically, and no record of the soirée was searched for.

Writer's spellings normalized: koszonetel to köszönettel, anyit to annyit, csütör | törtokön to csütörtökön, aszonysagal to asszonysággal, jöjön to jöjjön, bisztato to biztató, mamaja to mamáját.

## Why the reading is believed correct

The unchanged family key, with the disclosed k variant, gives Hungarian across all rows. Repeated words agree (kedves three times, Jolánkám twice, isten vele twice). Phrases run unforced over row breaks (sajná-lom, with the writer's own hyphen; te-hetek róla; feke-te ruhában; tisz-teletemet). The formulas match the family (Becses sorait köszönettel megkaptam on HCP 1212). Móczár recurs on sister cards HCP 1295 and HCP 1232.

## Review and what changed

The independent reviewer, a separate Claude Opus 5.5 agent, returned REVISE: the decipherment stands, with two normalizations to change and notes to correct.

- **Row 5:** szenvedett, nem tehetek became szenved, de nem tehetek. The literal signs divide without emendation, and the tense and the written word de are now kept.
- **Row 8:** dal estéjére became dalestélyre, by the writer's j for ly, so "song evening" became "song soirée".
- **h/d notes:** the d-shaped h is in row 6 (hetek), not row 13 (tehti). The ledger was corrected; the letters did not change.
- **Row 19:** the cross is now stated as the j-sign, a false start.
- **Row 13:** the punctuation is marked as editorial.
- **Móczár:** the cross-reference was added. The solver located the review's quoted phrase on HCP 1232 rather than HCP 1295, and cites both.

No sign value changed, so no second round was needed.
