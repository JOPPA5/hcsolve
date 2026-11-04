# HCP 1245: Feri to Jolánka Tóth, safe arrival and letters moved to the evening (March 1912)

Human solver: Tomáš Pavuk

**Status: deciphered except one blotted word in row 16; the rest of the card reads. Independent review 1 verdict REVISE (one clause corrected), review 2 verdict ACCEPT.** Report dated 2026-11-01. All work on this number is by Claude Opus 5.5; the key comes from earlier work on the family (see Method).

## Origin and context

The cryptogram is record 1245 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1245), portal name cpc_1912-03-20_HU__HU_Jasz Arokszalas_jolanka-11, part of Tobias Schrödel's collection of cryptographic postcards (T. Schrödel Collection, private collection). When captured on 2026-11-01 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The solver met no published solution of this card.

It is a Hungarian picture postcard. The address side carries seventeen rows of cipher in red ink, written beside the plain address **Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás** ("To the hopeful young lady Jolánka Tóth, Jászárokszállás"). In the box for the stamp, under the stamp (now lifted; a small green corner of it remains), the sender hid a message in plain hand: Csókol számtalanszor hű kedvesed Feri ("Kisses you countless times your faithful sweetheart Feri"). Every letter of it reads; it was written to be covered when the stamp was stuck on. The postmarks show GYÖNGYÖS 912 MÁR and a second impression MÁR 20, which agrees with the date 1912-03-20 in the portal's file name.

The card belongs to the family of Jolánka postcards, sent by Feri to Jolánka Tóth in Jászárokszállás around 1912 and written in one shared cipher. Another card of the same period (HCP 1271) has Feri moving to work at Gyöngyöspüspöki, near Gyöngyös, which fits the postmark and the opening news of a safe arrival.

The picture side has no handwriting. It has a printed verse:

> Sorrentói ábránd. Irtam ezt a levelemet / estefelé hétkor, / Sorrentó előtt a nap leszáll. / Remélem, hogy e pár sor irásom / Te édes, egészségben, / jo kedvben talál!

"Sorrento reverie. I wrote this letter of mine toward evening at seven, as the sun sets before Sorrento. I hope these few lines of my writing find you, my sweet, in good health and good spirits." (Spelling as printed.)

![Address side with the seventeen cipher rows, the plain address and the stamp box (source/address-large.jpg)](../source/address-large.jpg)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![The printed verse, turned to reading position (work/verse.png)](../work/verse.png)

## Method

The key was **transferred, not recovered**: it is the Jolánka family key, unchanged, as set out in the reviewed family cards (HCP 1216 and others, whose earlier passes were by an OpenAI GPT solver and Claude Opus 5.5). The transcription is **manual**: each of the 17 rows was read sign by sign on enlarged crops of the high-resolution address side and recorded in a ledger with one token per written sign (274 tokens, of which two are blots hiding part of a word). A short script checks the hashes of the image files and decodes the ledger; it is `work/decode.py`.

The key gives Hungarian on all 17 rows, and no sign outside the blots lacks a value. Repeated words decode identically (bolond three times, édes three times, hogy twice). The writer drops into plain Latin letters inside the cipher three times: a t ending row 1, dél in row 6 and az in row 8.

## Key

Cipher type: **MASC + Steganography** (updated 2026-11-03). Monoalphabetic substitution of Hungarian with invented graphic signs, plus a plain-text message hidden under the stamp. The labels below are descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S shape) | k | F shape | r |
| six | b | wave | l | bowl with descender | s |
| long + short stroke | d | three short strokes | m | gamma | t |
| three bars | e | two short strokes | n | cross with stem | u (X) / z (diagonal with stem) |
| open loop with descender | g | cursive loop | o | chevron | v |
| long + short stroke | h / p | dotted crossed curve | i | low descender | y (in gy, ny) |
| inverted T | j | opposed bowls | cs | joined loop + descender | gy |

sz is written bowl + z. Accents are strokes or dots over the base sign. The signs for d, h and p are near-homographs, and n and d differ only in stroke length, so those calls rest on the word; this is the known weakness of this family's key.

## Plaintext

Literal decipherment, row by row. `<...>` marks plain Latin letters on the card, `[?]` a sign lost under a blot, `[n?]` an uncertain sign:

```text
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

(The `h` in szeh of row 14 is the h/p sign, p here.)

### Hungarian (normalized)

Édes szerelmem! Tudatom, hogy szerencsésen megérkeztem. Édes Jolánkám, sajnálattal kel[l] tudatni, hogy a levelei délről estére leszek kénytelen át[t]enni az írását. A szerelmes mind bolond, mondjá[k] az okosak. Úgy látszik, mer[t] én, míg élek, csak bolond maradok, bolondja [a] két szép szemednek. Édes ki[csi]ny babus, ha te leszel [? one blotted word: reményem? nejem? enyém? menyem?], szívem, éltem nem lesz borús.

Word division, accents and bracketed letters are editorial. The cipher runs without spaces, and the writer drops letters.

### English

My sweet love! I let you know that I have arrived safely. Sweet Jolánka, I must regretfully tell you that I shall be forced to move the writing of the letters from noon to evening. Lovers are all fools, say the wise. It seems so, for as long as I live I shall stay nothing but a fool, a fool for your two lovely eyes. Sweet little babe, if you become [? one blotted word, perhaps my hope / my wife / mine / my bride], my heart, my life will not be gloomy.

Stamp box: Kisses you countless times your faithful sweetheart Feri.

### Slovak

Moja sladká láska! Oznamujem, že som šťastne prišiel. Sladká Jolánka, s poľutovaním musím oznámiť, že budem nútený presunúť písanie listov z poludnia na večer. Zaľúbení sú všetci blázni, hovoria múdri. Zdá sa, lebo ja, kým budem žiť, zostanem len bláznom, bláznom do tvojich dvoch krásnych očí. Sladká maličká bábika, ak budeš [? jedno zamazané slovo, snáď mojou nádejou / mojou ženou / moja / mojou nevestou], srdce moje, môj život nebude smutný.

V rámiku na známku: Bozkáva ťa nespočetnekrát tvoj verný milý Feri.

## Why the reading is believed

- Long strings arise without forcing, for example szerencsésen megérkeztem, délről estére leszek kénytelen, a szerelmes mind bolond, míg élek csak bolond maradok.
- The signature, the recipient, the date and the Gyöngyös postmark all fit the family.
- Phrases recur on sister cards: estére (HCP 1276), sajnálattal kell tudatni (HCP 1273).
- The printed verse supports rows 6 to 9 independently of the cipher. The printed lover writes his letter estefelé hétkor, "toward evening at seven", and Feri, on that very card, says his letter-writing moves to the evening.

## What remains uncertain

- **Row 16, the one unread word.** A heavy blot covers the start of the row and a second blot sits over a sign joined to a clear y. Visible: the left blot, a long and a short stroke, three bars, the second blot with y, three bars, two strokes, a thick stroke with a tail. The candidates are by sense only, and none is claimed or accounts for every mark: reményem "my hope" (the reviewer's suggestion and Feri's standing term for her, egyetlen reményem, though the left blot is tight for its letters and the visible strokes are unequal); nejem "my wife"; enyém "mine"; menyem (literally "my daughter-in-law", in older usage "bride"). A faint grey pencil hook near the blot is a different medium and is not interpreted.
- **Rows 6 to 9.** All signs are read and the sense is direct, but the grammar is loose: a levelei ... az írását is a double object. levelei is formally "his/her/your (polite) letters", or a dropped-ending levelei[m] "my letters", while the rest of the card uses familiar te; the translation says "the letters". The plain word dél could be taken as ending in b on shape alone, and rests on the pairing délről estére. A detached dot above the v of levelei is unexplained. The i of írását is tangled with the y tail above it. Why the writing moves is not stated.
- **Row 5 tudatni.** The n has a smear or correction across it; the word is by sense and has a sister parallel.
- **Row 15 kiny.** The signs k, i, ny are clear; the normalization ki[csi]ny "little" is by sense.
- **Near-homographs.** The p of szép and the d or h of mondja, mind, szemednek, hogy, ha rest on the word.
- **Plain text.** The stamp box is smeared by the stamp's printed circle, so hű kedvesed is read through it. The last address line under the stamp and portal mark, and the day on the Gyöngyös strike, were not read sign by sign by the reviewer.
- **Address form.** The card uses te, while the family usually has Ön. This is noted, not explained, though the printed Te édes on this card may have prompted it.

## Review and what changed

Two rounds of independent review were carried out by a separate Claude Opus 5.5 agent, which made its own crops, its own sign ledger and its own decoder.

**Review 1, verdict REVISE.** The main finding was a misread sign in row 7: the solver had read bowl + z and an emended eszére, but the sign is a bowl with a heavily inked gamma. That gives estére, and the clause délről estére ... áttenni replaced the earlier reading. The reviewer also required the whole printed verse to be read, the statement that the loop "settles" dél to be withdrawn, and the grammar of levelei to be disclosed. All were done, and since one clause changed the card went back for a second round.

**Review 2, verdict ACCEPT.** With accents off and d/h merged, the reviewer's ledger matched 16 of 17 rows; the only difference is the open row 16 sign. Rows 6 to 9 were confirmed sign by sign (the reviewer's ledger came from round 1, so this check was not blind). Minor findings, all addressed with no change to the reading: an editorial [a] before két is now marked; reményem was added first among the row 16 candidates; the uncertain row 16 sign is now marked in the ledger; the dot in row 6 is disclosed; a loose Slovak line was tightened.

The reviewer did not search for published solutions outside the repository, and could not prove any candidate for the row 16 word.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1245/work/decode.py
```

This verifies the SHA-256 of the four image files, decodes `work/ledger.txt` and prints the literal rows and the normalized text.
