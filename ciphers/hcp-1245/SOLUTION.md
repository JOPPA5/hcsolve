# HCP1245: Feri to Jolánka Tóth, safe arrival, letters moved from noon to evening, and a joking love note (Gyöngyös, March 1912)

**Status: read in full except one blotted word in row 16.** Claude Opus 5.5, 2026-11-01. Revised after review 1 (row 7 corrected, rows 6 to 9 reread); review 2 verdict ACCEPT, with its minor findings addressed below.

Credit: all work on this number is by Claude Opus 5.5 (the source capture by the orchestrator, the reading here). The key is transferred from the reviewed Jolánka family cards (HCP1216 and others), whose earlier passes were by the OpenAI GPT solver and Claude Opus 5.5. The portal shows status *Not solved* and attaches no transcription or solution; I met no published solution of this card.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the Jolánka postcard family key, unchanged (full legend in `ciphers/hcp-1216/SOLUTION.md`).

2026-11-03 type note: the stamp was lifted and the stamp box carries a hidden plain-Hungarian message written under it, so the card is typed **MASC + Steganography** (register label). See *Stamp-box message (2026-11-03)* below.

Signs used here:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S shape) | k | F shape | r |
| six | b | wave | l | bowl with descender | s |
| long + short stroke | d | three short strokes | m | gamma | t |
| three bars | e | two short strokes | n | cross with stem | u (X) / z (diagonal with stem) |
| open loop with descender | g | cursive loop | o | chevron | v |
| long + short stroke | h / p | dotted crossed curve | i | low descender | y (in gy, ny) |
| inverted T | j | opposed bowls | cs | joined loop + descender | gy |

*sz* is written bowl + z. Accents are strokes or dots over the base sign.

The writer breaks into plain Latin letters inside the cipher in three places: the *t* ending row 1, *dél* in row 6, *az* in row 8. The stamp box and the address are plain hand. The picture side has no handwriting, only a printed verse (read in full on `work/verse.png`, a rotated crop of the hires picture side):

> *Sorrentói ábránd.* Irtam ezt a levelemet / estefelé hétkor, / Sorrentó előtt a nap leszáll. / Remélem, hogy e pár sor irásom / Te édes, egészségben, / jo kedvben talál!

"Sorrento reverie. I wrote this letter of mine toward evening at seven, as the sun sets before Sorrento. I hope these few lines of my writing find you, my sweet, in good health and good spirits." (Spelling as printed.) The card's message plays on this: see *Why it is correct*.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1245/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (one token per written sign, a manual transcription from the pixels) with the key, and prints the literal rows and `work/normalized.txt`.

## Literal decipherment

```
01 edesszerelmem<t>u         10 aszerelmesmindbolond
02 datomhogyszerencse        11 mondjaazokosak
03 senmegerkeztemedes        12 ugylatszikmerenmig
04 jolankamsajnalat          13 elekcsakbolondmaradok
05 talkeltudatnihogy         14 bolondjaketszehszemednek
06 alevelei<dél>ről          15 edeskinybabushateleszel
07 estereleszekkeny          16 [?][n?]e[?]yemszivemeltem
08 telenatteni<az>ira        17 nemleszborus
09 sat
```

(The `h` in *szeh* of row 14 is the h/p sign, p here.)

## Hungarian (normalized)

Édes szerelmem! Tudatom, hogy szerencsésen megérkeztem. Édes Jolánkám, sajnálattal kel[l] tudatni, hogy a levelei délről estére leszek kénytelen át[t]enni az írását. A szerelmes mind bolond, mondjá[k] az okosak. Úgy látszik, mer[t] én, míg élek, csak bolond maradok, bolondja [a] két szép szemednek. Édes ki[csi]ny babus, ha te leszel [? one blotted word: *reményem*? *nejem*? *enyém*? *menyem*?], szívem, éltem nem lesz borús.

Stamp box, plain hand: Csókol számtalanszor hű kedvesed Feri.

Address, plain hand: Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás.

## English

My sweet love! I let you know that I have arrived safely. Sweet Jolánka, I must regretfully tell you that I shall be forced to move the writing of the letters from noon to evening. Lovers are all fools, say the wise. It seems so, for as long as I live I shall stay nothing but a fool, a fool for your two lovely eyes. Sweet little babe, if you become [? one blotted word, perhaps my hope / my wife / mine / my bride], my heart, my life will not be gloomy.

Stamp box: Kisses you countless times your faithful sweetheart Feri.

## Slovak

Moja sladká láska! Oznamujem, že som šťastne prišiel. Sladká Jolánka, s poľutovaním musím oznámiť, že budem nútený presunúť písanie listov z poludnia na večer. Zaľúbení sú všetci blázni, hovoria múdri. Zdá sa, lebo ja, kým budem žiť, zostanem len bláznom, bláznom do tvojich dvoch krásnych očí. Sladká maličká bábika, ak budeš [? jedno zamazané slovo, snáď mojou nádejou / mojou ženou / moja / mojou nevestou], srdce moje, môj život nebude smutný.

V rámiku na známku: Bozkáva ťa nespočetnekrát tvoj verný milý Feri.

## Uncertainties

1. **Row 16 opening, the one unread word.** A heavy ink blot covers the start of the row. Visible: a wide blot, then a long and a short stroke (uncertain: n, the h/p/d sign, or the end of an m; `[n?]` in the ledger), three bars, a second blot with a small counter joined to a clear y descender, three bars, two strokes, then a thick stroke with a tail. I give the word as `[?][n?]e[?]yem`. Candidates, all by sense: *reményem* ("my hope", the reviewer's suggestion, listed first: r, e under the left blot, m as the visible strokes plus a third under the blot, e, ny under the second blot, e, m; Feri's standing term for her is *egyetlen reményem* across this family; weak points: the left blot is tight for r + e + one stroke of m, and the visible strokes are long and short, not two equal m strokes); *nejem* ("my wife", the blot's flat base being the inverted T j, with a stray y); *menyem* (the reviewer's suggestion: blot plus two strokes = m, three bars = e, second blot with y = ny, then e, m; literally "my daughter-in-law", in older usage "bride"; it fits the stroke order but the sense is uncertain); *enyém* ("mine", with ny under the blot; the family has *enyémnek mondhatom*, HCP1292, but the visible order n-like strokes, e, y fits it badly). None accounts for every mark. This is **not** a restoration; I claim no reading, and the normalized text leaves the word open. A faint grey pencil hook lies on and under the left blot (`review/work/b4.png`); it is a different medium, not a cipher sign, and I do not interpret it. The last stroke group is taken as m; its tail makes a d shape possible (literal *…end*, no word).
2. **Rows 6 to 9.** Every sign is read and the sense is direct: *délről estére ... áttenni* "to move from noon to evening". What remains loose is the grammar and one form:
   - *a levelei ... az írását* is a double object, as if *a levelek írását* had been started and the sentence recast.
   - *levelei* formally means "his/her/your (Ön) letters", while the rest of the card uses *te*. I translate "the letters": nothing shows that hers are meant, and the sense does not need it.
   - Row 7 sign 3 is a bowl joined at the top to a heavily inked gamma (t). It was first misread as bowl + z.
   - *dél* is plain Latin. On shape alone its last letter could be b (tall loop, then a low curl back to the stem, unlike the rising tail of the l's in the stamp box). *dél* rests on the sense *délről estére*, with the two strokes over the next o giving *ő*.
   - A detached dot stands above the left arm of the v of *levelei* (row 6, `review/work/r2/r6a.png`). It is unexplained, possibly a displaced accent, and does not change the word.
   - *levelei* could also be *levelei[m]* "my letters", given the writer's dropped endings; "the letters" stays safe either way.
   - The i of *írását* (row 8) is tangled with the descender of the y of *kény* above, so its loop may belong to that y. The crossing stroke is its own.
   - Why the writing moves is not stated on the card. New working hours are a guess (HCP1271 has the change of workshop).
3. **Row 5 *tudatni*:** the n has two short horizontal strokes across it, a smear or a correction. *tudatni* is by sense and matches *sajnálattal kell tudatni* in HCP1273.
4. **Row 15 *kiny*:** signs k i ny are clear, though a blot touches the foot of the i. Normalized *ki[csi]ny* by sense ("little"); *kis* would need an s that is not there.
5. **Word-sense calls on near-homographs:** p in *szép* (row 14, h/p sign); d in *mondja, mind, szemednek* and the d/h of *hogy, ha*. Stroke length is not decisive on these, and d/n calls rest on the word.
6. **Blotted but legible:** u of *úgy* (row 12), b of *bolondja* (row 14), m of *mondja* (row 11), h of *hogy* (row 2), third bar of e in *édes* (row 15). Their shapes remain visible.
7. **Writer's spellings normalized:** *kel* → kell, *atteni* → áttenni, *mondjá* → mondják, *mer* → mert (the same habit as HCP1216); *[a]* before *két* (row 14) is an editorial addition, the card has *bolondja ket*. Accents are partly visible (several acutes on é and á are clear) and are not ledgered; they are supplied in normalization. Row 9's *sat* completes *ira-sat* = *írását* across the row break.
8. **Stamp box:** smeared by the stamp's printed circle; *hű ked / vesed* is read through it. The d's look like *ol*.
9. **Date:** the portal filename gives 1912-03-20; the postmarks show GYÖNGYÖS 912 MÁR and a second MÁR 20 impression, consistent. The day on the Gyöngyös strike is covered by the stamp edge.

## Why it is correct

- The family key was transferred unchanged and gives Hungarian on all 17 rows; apart from the blot no sign lacks a value.
- Long strings arise unforced: *szerencsésen megérkeztem*, *sajnálattal kel tudatni*, *délről estére leszek kénytelen*, *a szerelmes mind bolond*, *míg élek csak bolond maradok*, *bolondja két szép szemednek*, *nem lesz borús*.
- Repeated words decode identically (*bolond* ×3, *édes* ×3, *hogy* ×2, *szerelm-* ×2, *tudat-* ×2).
- It fits the context: the card is posted at Gyöngyös in March 1912, and HCP1271 (same period) has Feri moving to work at Gyöngyöspüspöki. The signature *Feri* and the recipient match the family. *estére* occurs in the family (HCP1276), and *sajnálattal ... tudatni* has family parallels (HCP1273, HCP1274).
- The picture side supports rows 6 to 9 independently of the cipher: the printed lover wrote his letter *estefelé hétkor* ("toward evening at seven"), and Feri, on that very card, announces that his letter-writing moves to the evening. This also fits the playful tone. The *te* address (*szemednek, leszel, kedvesed*) differs from the usual *Ön* of the family; I note it and do not explain it, though the printed *Te édes* on this card may have prompted it.

## Response to review 1

Verdict REVISE. I rechecked each finding on the crops named below and accept all five.

1. **Row 7 sign (major): fixed.** On `review/work/cmp_st.png` and `sign_row7.png` the sign is a bowl plus a thick stem with a flat bar running right from its head, the heavy gamma of *látszik* (row 12). No arm crosses left of the stem as in every sz group. My *eszére* / *ezér[t]* was wrong, and its emendation is gone. `work/ledger.txt` row 7 now has T; `work/normalized.txt`, the literal row, the Hungarian, the English, the Slovak and uncertainty 2 are redone. The invented "[come?]" and "your letters" are gone.
2. **Printed verse (major): fixed.** I read the whole verse, opening words included, on my own crop `work/verse.png`; it is quoted above and used in *Why it is correct*.
3. **Status and `levelei` (minor): fixed.** The status line no longer calls the clause partly inferred. Uncertainty 2 states the double object and the *levelei* / *te* mismatch, and the translations say "the letters".
4. **"The looped l settles it" (minor): fixed.** On `review/work/b1.png` the letter is indeed nearer a b than the stamp-box l's. *dél* now rests on the sense, as uncertainty 2 says.
5. **Row 16 candidate (minor): fixed.** *menyem* is listed with *nejem* and *enyém*, unclaimed. The normalized text and translations now leave the word open instead of showing two readings as if they were the only ones. I also added the pencil mark, which neither pass had noted.

Reproduction rerun after the fix (`python3 -I ciphers/hcp-1245/work/decode.py`): all four hash checks OK, row 7 prints `estereleszekkeny`, and the normalized text prints the new clause.

The reading of one whole clause changed, so, as the reviewer recommended, this goes back as round 2 for a check of rows 6 to 9 rather than to FINAL.

## Response to review 2

Verdict ACCEPT. I rechecked findings 1 to 3 on the reviewer's crops and accept all of them. None changes the reading, so this goes to FINAL.

1. **Unmarked *a* in the normalized text: fixed.** `review/work/r2/r14.png` shows inverted T, two bars, section mark: one a only. The normalized text now has *bolondja [a] két*, in this file and in `work/normalized.txt`, and uncertainty 7 lists the addition. *Why it is correct* quotes the string as written, without the a.
2. **Row 16 candidate: fixed.** *reményem* now heads the candidates in uncertainty 1, in the normalized text and in both translations, credited to the reviewer with its weak points, and unclaimed. On `review/work/r2/r16a.png` the visible strokes are indeed a long and a short one, so "two strokes (n...)" said too much. `work/ledger.txt` row 16 sign 2 is now `[n?]`, `work/decode.py` accepts that token, and the literal row prints `[?][n?]e[?]yemszivemeltem`.
3. **Detached mark in row 6: fixed.** The dot is clear on `review/work/r2/r6a.png`, above the left arm of the v. Uncertainty 2 now discloses it as unexplained.
4. **Slovak: fixed.** Now *Zaľúbení sú všetci blázni*, matching the English.
5. **Plain *dél*: no action,** as the reviewer says; the disclosure stands. I added the *levelei[m]* possibility the reviewer raised to uncertainty 2.

Reproduction rerun after the fixes (`python3 -I ciphers/hcp-1245/work/decode.py`): all four hash checks OK, row 16 and the normalized text print as above, and all other rows are unchanged.

## Stamp-box message (2026-11-03)

Audit by Claude Opus 5.5 on the hires address side (`work/hires/..._adr.jpg`), crops in `work/stamp-2026-11-03/` (`stamp_box_2x.png`, and `stamp_lines2-5_redmask_3x.png`, a red-minus-green mask at 3x that removes the blue printed circle).

- **State:** the stamp is lifted. Only a small green corner fragment of it remains at the lower right of the box; the blue circle in the middle is part of the card's printed stamp field (publisher's mark), not a postmark. The writing lies in the box where the stamp covered it, so it was hidden when the card was posted.
- **Script:** plain Hungarian in Latin cursive, red ink, same hand and ink as the cipher. No cipher signs in the box.
- **Literal reading, six lines:** csokol / szamta / lanszor / hü ked / vesed / feri
- **Normalized Hungarian:** Csókol számtalanszor hű kedvesed Feri.
- **English:** Kisses you countless times your faithful sweetheart Feri.
- **Slovak:** Bozkáva ťa nesčíselnekrát tvoj verný milý Feri.
- **Unread:** nothing. Accents on *csókol*, *számtalanszor* are not written (normalized only); *hü* is written with two dots for *ű*. The letters of lines 3 and 4 cross the printed circle but every letter reads on the red mask. This is the same text already given above; the audit confirms it and adds the hidden-under-stamp status. The reproduction script covers the cipher rows only; the stamp text is read by eye.
