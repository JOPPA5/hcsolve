# HCP 1244 (cpc_1912-04-10_HU__HU_Jasz Arokszalas_jolanka-16): Feri to Jolánka Tóth, safe arrival and Easter sprinkling

Human solver: Tomáš Pavuk

**Status: the whole enciphered text is read (17 rows plus one word below the address). One sign keeps two possible values, and one word of a separate plain note stays unread. Independent review 1 verdict REVISE; all findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1244 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1244), part of Tobias Schrödel's cryptographic postcards collection (private collection; see https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When captured on 2026-11-01 the portal listed it as **Not solved**, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The date 1912-04-10 comes from the portal's file name.

The address side carries the plain address **Szépreményű Tóth Jolánka kisasszonynak, Jászárokszállás**, the red cipher text in rows, one enciphered word below the address, and a plain note in the stamp box. The stamp itself is gone. Turned 180°, the postmark shows `91…`, then APR, then 10 or 16. The month fits the file date, but the last digit of the year is not legible. The picture side is a printed verse headed *Szerenád. Ábránd.*, number 2317, and is not cipher.

The card belongs to the family of Hungarian cipher postcards to Jolánka Tóth, several of which are deciphered in this repository. Sister cards connect the writer with Gyöngyös (HCP 1271), and give the name Holes Ferenc (HCP 1268, 1309). Easter 1912 fell on 7 April by calculation, so the question about sprinkling on Easter Monday suits the date. Reading *kiöntözte* as that custom is an interpretation.

![Address side, with the cipher rows, the address and the stamp box (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: a printed verse, no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

This is a **known-key reading**, not a new key recovery. The key of the finished card HCP 1216 was applied unchanged. All reading on this number is by Claude Opus 5.5; there is no earlier work on this card, though the family key was partly established earlier by the OpenAI GPT solver.

The transcription is manual, sign by sign, from enlarged crops of the un-converted original scan. It is stored as a token ledger (work/ledger-opus.txt) and decoded by a script. A first reading of row 4 as "a vo-" gave nothing; that sign is a deep wave (l), which gives *alo|mason*. Reading *kiöntöztek* in row 7 failed because the card has no k there.

## Key

Simple monoalphabetic substitution with invented graphic signs. Word division is not marked. The sign names are conventional labels for handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma | t |
| short + long stroke | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| open loop with descender | g | tall + short stroke | h / p | low descender | y |
| dotted crossed curve | i | joined loop + descender | gy | long crossed diagonal | z |
| inverted T | j | | | | |

Dots and ticks over a sign are accents, written only here and there. f does not occur. The h/p sign is a near-homograph, so that choice rests on word sense. Row 17 has a d+j ligature.

## Plaintext

Literal decipherment as printed by the reproduction command. `h` is the h/p sign, `[s]` is a blotted s, and `{j|t}` is the two-valued sign discussed below.

```text
01 kedvesjolánkam
02 tudatomhogysze
03 rencsésenmegerkez
04 tünkagyöngyösialo
05 masonvártrankahaés
06 anymédesjolankam
07 kiöntözteemárma
08 gáténamesterurla
09 nyaitolannyivi
10 zethogybörigeláz
11 tamistenvelaviszont
12 latásradesokáleszaz
13 elegleszkibirni
14 adossoh’semmarad{j|t},
15 acsok[s]ohasemart.
16 hacsókotkahbabám
17 csakaddvisszamindjart
A1 szeretettel
```

Normalized Hungarian (word division, accents and punctuation are editorial):

**Kedves Jolánkám! Tudatom, hogy szerencsésen megérkeztünk. A gyöngyösi állomáson várt ránk apa és any[á]m. Édes Jolánkám, kiöntözte-e már magát? Én a mester úr lányaitól annyi vizet, hogy bőrig eláztam. Isten vel[e] a viszontlátásra. De soká lesz az, elég lesz kibírni. Adós soh'sem maradj, a csók soha sem árt. Ha csókot kap, babám, csak add vissza mindjárt.**

Below the address, enciphered: **Szeretettel.**

Plain hand, in the stamp box: Csókolom a távolból az e… …tel Fe[?]ri. Holes Ferencz.

English translation: **Dear Jolánka of mine! I let you know that we arrived safely. At Gyöngyös station father and my mother were waiting for us. Sweet Jolánka of mine, has anyone sprinkled you yet? As for me, from the master's daughters [I got] so much water that I was soaked to the skin. God be with you, until we meet again. But that will be a long time; it will be hard enough to bear. Never stay in debt, a kiss never does harm. If you get a kiss, my baby, just give it back at once.**

Below the address: **With love.** Stamp box: I kiss you from afar … [one word unread] … Feri. Holes Ferencz.

Slovak translation: **Milá moja Jolánka! Oznamujem Vám, že sme šťastne docestovali. Na stanici v Gyöngyösi nás čakal otec a moja mama. Sladká moja Jolánka, už Vás niekto polial? Ja [som dostal] od dcér pána majstra toľko vody, že som zmokol do nitky. S Bohom, dovidenia. Ale to bude dlho, bude ťažké to vydržať. Nikdy nezostávaj dlžný, bozk nikdy neuškodí. Ak dostanete bozk, zlatko, hneď ho vráť.**

Pod adresou: **S láskou.** V rámčeku známky: Bozkávam Vás z diaľky … [jedno slovo neprečítané] … Feri. Holes Ferencz.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1244/work/decode_opus.py
```

The script checks the SHA-256 hashes of the two source scans and the two hi-res originals, decodes the ledger with the key, and prints the literal rows and the normalized text. It does not read the images; the transcription step is manual.

## Uncertainties

- **Row 14, last sign: *maradj* chosen, *maradt* not excluded.** The sign has both a gamma top (t) and a base bar running through the foot of its stem, the construction of the d+j ligature in row 17 (j). No other t on the card has a base bar. Both features are pen strokes; the top bar runs into a wet smear, but the green and blue channels show a firm core inside it. I read j because a base bar has no place in a t, because the imperative gives the clause a subject and matches *add vissza*, and because the tick after the sign works as a comma. Rows 14–17 are laid out as a four-line verse rhyming on lines 2 and 4, so the rhyme of *maradt* with *árt* is no argument for t. Stroke order cannot be shown from the scan, and only the original card could settle it. If the sign is t, the clause reads "a debtor he never stayed". The jesting sense of the verse is the same either way.

![Row 14, the end of maradj: the third stem has a top bar running into the smear and a base bar through its foot (review/work/crops/r14end.png)](../review/work/crops/r14end.png)

![Row 17, the d+j ligature of mindjárt, for comparison (review/work/crops/r17end.png)](../review/work/crops/r17end.png)

- **h/p by word sense.** *apa* (row 5) and *kap* (row 16) read the sign as p; *hogy*, *soha* and *ha* read it as h.
- **Restorations.** The first letter of *soha* in row 15 is filled by a blot, though its outline fits s and no other letter gives a word. The t of *-tól* in row 9 is largely under a blot. *any[á]m* in row 6 lacks the á on the card.
- **Writer's forms.** *alo|mason* is normalized *állomáson*. *vela* has two firm bars, so it is a, not e: I keep it as the article and drop the e (*vel[e] a*). The alternative is that it stands for the e of *vele*. *sohsem* is colloquial, and the high arc in it may be an apostrophe.
- **No verb in rows 9–10.** *Én … annyi vizet* has no verb such as *kaptam*; it is not supplied in the Hungarian.
- **Person in rows 16–17.** *kap* is third person or formal, *add* is informal. *Ha csókot kap babám* can also mean "if my baby gets a kiss". *kiöntözte* is singular, literally "has he sprinkled you".
- **Marks.** A tick after row 14 and a round dot after row 15 are read as a comma and a full stop. Other punctuation is editorial, and accents on the card are unreliable.
- **Stamp box (plain, not cipher).** One word, begun with *e-* and running to *-tel*, is not read. The t and á of *távolból* are in a tear and rest on the same formula on HCP 1278. *Feri* is likely, not certain. *Ferencz* fades under the postmark and is read with the help of sister cards.
- **Date.** The year's last digit and the ring text of the postmark are not legible; 1912 rests on the file name.
- Pencil marks at the top right corner (about "17") look like a later dealer or collector mark and are not read.

## Why the reading is believed

All rows decode with the HCP 1216 key unchanged. The opening formula matches HCP 1278 almost word for word, yet rests on signs read here. Gyöngyös and the name Holes agree with sister cards, and the word below the address decodes to *szeretettel* with no other support. The reviewer's own sign-by-sign reading gave no letter difference in 281 signs, though it was not blind.

## Review summary

The review was made by a separate Claude Opus 5.5 session. It re-ran the command, decoded its own transcription with its own script, and inspected all rows and the restorations at enlargement. Verdict: **REVISE**; the key, row text and sense stood.

What changed because of it:

- The last sign of row 14 was recorded as a plain t. It is now recorded as a sign with both features, and the normalized reading changed from *maradt* to *maradj*, with the English and Slovak.
- Marks in rows 14–15 were added to the ledger, and the full stop after row 14 became a comma.
- *vele* became *vel[e] a*, keeping the letter on the card, and *úrlányaitól* became *úr lányaitól*.
- The translations were tightened ("has anyone sprinkled you"; the switch of person is disclosed and kept in the Slovak).
- Descriptions of two signs and of the postmark were corrected.

The reviewer could not settle the row 14 sign, the postmark year or the stamp-box word. None of these is settled now.
