# HCP1296 — plain-text postcard to Jolánka Tóth: NO CIPHER FOUND

**Status: partial by category, not by legibility. The whole card is read, but nothing on it is enciphered, so there is no decipherment, key or cipher type to claim. No DONE marker and no register entry are proposed.** Written 2026-10-30 by Claude Opus 5.5, from enlarged crops of the originals in `work/hires/`. There is no earlier work on this number. The portal shows Not solved and attaches no transcription or solution. No published solution was found or used.

## Cipher type and key

None. The portal files the card under Substitution, but the message, the signature, the stamp-box greeting and the address are all ordinary Hungarian cursive in red ink. The Jolánka family's graphic signs (HCP1216 key) do not occur anywhere on it. An equalized image of the picture side (`work/crops/pic_eq.png`) shows only the printed verse and caption, with no handwriting. Only the portal's filing and the series name (`jolanka-25`) connect it to the cipher cards.

Not tested: a hidden second layer such as an acrostic or marked letters. Nothing on the card suggests one. The two ink densities look like pen refills.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1296/work/show_plain.py
```

It checks the SHA-256 of all four images and prints the manual transcription `work/transcription.txt`. Nothing is computed, because there is no key.

## Hungarian (normalized)

Mélyen tisztelt Jolánka kisasszony! Becses sorait megkaptam, melynek nagyon örülök. Ne haragudjon, hogy ily soká válaszolok, de nem írhattam hamarabb, de ezután pontosabb leszek. Mi újság Árokszállásban? De szeretném már meglátogatni! Itt nincs semmi újság, csak az, hogy meleg van. Meleg van-e Jolánkáék felé? Tisztelem a kedves szüleit és a kedves barátnéit, is meg testvéreit.

Up the divider: Tisztelője [H?]al[o/e]s Ferenc.
In the stamp box: Üdvözlem távolból.
Address: Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás.

Printed on the picture side (not written by the sender): caption "Akiknek a szívük fáj" and a four-line verse beginning with it.

## English

Deeply respected Miss Jolánka! I have received your esteemed lines, which made me very glad. Do not be angry that I am answering so late, but I could not write sooner; from now on I will be more punctual. What news in Árokszállás? How I would like to visit it now! There is nothing new here, only that it is hot. Is it hot over your way, Jolánka? My respects to your dear parents and your dear girlfriends, and also to your brothers and sisters.
Your admirer, [H?]al[o/e]s Ferenc. Greetings from afar.
To the promising young lady Jolánka Tóth, Jászárokszállás.

## Slovak

Hlboko vážená slečna Jolánka! Váš vzácny list som dostal a veľmi ma potešil. Nehnevajte sa, že odpovedám tak neskoro, ale nemohol som napísať skôr; odteraz budem presnejší. Čo je nové v Árokszállási? Ako rád by som ho už navštívil! Tu nie je nič nové, len to, že je teplo. Je teplo aj u vás, Jolánka? Pozdravujem Vašich milých rodičov a Vaše milé priateľky, aj Vašich súrodencov.
Váš ctiteľ [H?]al[o/e]s Ferenc. Pozdravujem Vás z diaľky.
Nádejnej slečne Jolánke Tóthovej, Jászárokszállás.

## Uncertainties

1. **Signature surname:** the first letter is probably H but K is not excluded, and the vowel after l is o or e. It is reported literally. Ferenc is the formal form of Feri, the sender of the cipher cards, but nothing here proves they are the same man. The hand was not compared with his, and his cipher cards use another script.
2. **`ninos`-like word (row 13):** it looks like n-i-n-o-s with a mark above, and is read as *nincs* from context.
3. **`Tiszteem` (row 17):** no clear l is visible, and the word is normalized to *Tisztelem*.
4. **`nejeit` (rows 17–18):** *barát-nejeit* is normalized to *barátnéit*. The second-last vowel is uncertain.
5. **Word sense in the stamp box:** the box is overwritten and sits on a grey circular impression. *üdvöz-lem távol-ból* rests partly on sense: the first row looks like `uolizü`, the third has a v that resembles n, and this hand's d looks like `ol` and its b like `li`, as in `ole` = *de* and `hamarali` = *hamarabb*.
6. **`ismeg`:** this is written as one word and read as *is meg* ("and also").
7. **Writer's spellings normalized:** *kisaszony, soka, irhatam, hamarab, pontosab, it, semi, Arokszálás, Jolankaek*.
8. **Date:** 1912-06-11 is the portal's date. The right postmark shows `91` with the following digits lost, and the left one is JÁSZÁROKSZÁLLÁS with an unclear date, so the card does not independently confirm the day or year.

## Why this is believed correct

Every row reads directly as coherent period Hungarian without any substitution, and the address gives the same family details as HCP1305 (*Szépreményű Tóth Jolánka úrleánynak*). The formal tone fits a polite acquaintance, unlike the *édes Jolánkám* love letters of the cipher cards.
