# HCP1225 — Feri to Jolánka Tóth: a bad dream and a worried love letter

**Status: PARTIAL. The whole cipher text (18 rows plus one line beside the address) is read; the plain-hand note on the stamp place is not fully read: its first two words are unread.** By the project's rule for unenciphered notes this card therefore gets no DONE marker and no register entry. Written 2026-11-02 by Claude Opus 5.5. No earlier work on this number; the portal shows Not solved with no transcription or solution attached, and no published solution was found. The key comes from finished sister cards (hcp-1216 and its family).

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (register label: MASC), the Jolánka family key, transferred unchanged from hcp-1216 (`ciphers/hcp-1216/SOLUTION.md`, `work/graphic-key.json`). Accents sit over the base sign. Observations specific to this card:

- j = cross with a LOW bar (inverted-T type: *éjjel*, *jutottam*, *Jolánkám*, *baj*); f = cross with a HIGH bar (*földtekén*). This separates them cleanly here.
- g = open loop with a straight descender (*boldogság*, *gondolsz*); gy = joined "cy" (*hogy*, *egyetlen*). The writer uses gy also in *megy-láttalak* and *agyódom*.
- h/p = tall stroke + short stroke; h in *hogy*, p in *csupa* and *pá*, both by word sense.
- d = two long joined strokes (no d/n doubt on this card: all d are visibly long).
- sz = right bowl + crossed z, written as two signs; cs = opposed bowls.
- The bars under the corner t can merge visually with its top stroke, so t+a and t+e must be counted bar by bar.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1225/work/decode.py
```

It checks the SHA-256 of all four scans, decodes the manual sign ledger `work/ledger.txt` and prints the literal rows and `work/normalized.txt`. The ledger is a human-style transcription from the pixels (not OCR). Crops: `work/crop*.py`, `work/crops/`.

## Literal decipherment (as printed)

```
01 édesegyetlenremenyem        10 amiotamegylattalak
02 kivanomhogyiokedve          11 édesem,
03 bentáliasoraim.az           12 csup{a}meröboldog{s}ág
04 éjjelnagyoaroszviszony-     13 azéletem.
05 bajutotamönelalmomba        14 irdmegedesgondolsz-e
06 nagyonagyodom,nemetör       15 ram?ugymintén,
07 {r}ént{v}alamibajönne       16 nemleszboldogabbn{a}lam
08 édesjolánkámtudes           17 aföldtekén,istenvele
09 sonhogylétetelől            18 aviszontlatásrapáédes
N1 {s}zeretetel  (line beside the address, under "leánynak")
```

## Hungarian (normalized)

Édes egyetlen reményem! Kívánom, hogy jó kedvében találja soraim. Az éjjel nagyon rossz viszonyba jutottam önnel álmomba[n]. Nagyon aggódom, nem-e történt valami baj önne[l], édes Jolánkám. Tudasson hogylétéről. Amióta megláttalak, édesem, csupa merő boldogság az életem. Írd meg, édes, gondolsz-e rám? Úgy, mint én, nem lesz boldogabb nálam a földtekén. Isten vele, a viszontlátásra, pá, édes.

Beside the address: szeretet[t]el.

Plain hand on the stamp place (not cipher, NOT fully read): [two words unread] csókolja számtalanszor Feri.

## English

My sweet only hope! I wish that my lines may find you in good spirits. Last night I got on very bad terms with you in my dream. I am very worried: has something not happened to you, my sweet Jolánka? Let me know how you are. Since I first saw you, my sweet, my life has been nothing but sheer happiness. Write to me, sweet, do you think of me? As [you do, and] as I do, no one on earth will be happier than I. God be with you, until we meet again, bye, sweet.

Beside the address: with love.

Stamp place: [two words unread] kisses you countless times, Feri.

## Slovak

Moja sladká jediná nádej! Želám si, aby Vás moje riadky našli v dobrej nálade. V noci som sa s Vami vo sne dostal do veľmi zlého vzťahu. Veľmi sa bojím, či sa Vám niečo nestalo, moja sladká Jolánka. Dajte mi vedieť, ako sa máte. Odkedy som Ťa uvidel, drahá, je môj život samé čisté šťastie. Napíš mi, sladká, myslíš na mňa? Tak ako ja, nebude nikto na svete šťastnejší odo mňa. S Bohom, dovidenia, pá, sladká.

Pri adrese: s láskou.

Na mieste známky: [dve neprečítané slová] bozkáva Vás nespočetnekrát, Feri.

## Uncertainties

**Blocking point: stamp-place note.** Six plain-hand lines in ink bled by the soaked-off stamp: (1) a solid blot, then roughly *a n/m a* + a letter with a long descender + *i t*; (2) a word of about six letters with one i-dot, ending in *-as/-os*, crossed by that descender; (3–6) *cso-kol / ja szám / talan / szor Feri*. Candidates such as *Sanyit*, *[M]argit*, *[An]nyit* for line 1 all fit the outlines and none is established; line 2 has no reading. Contrast stretching (`work/crop4.py`, `crops/st_enh.png`) did not help. These are two words, not one, so the reading is reported as partial. "21" above the note is written by the same pen; its meaning is unknown (a number, not a word).

Points in the cipher text (all small; none changes the sense):

1. Row 2/3 *iokedve|ben*, *tália*: the dotted sign (i) stands where j is expected, *jó*, *találja*. Elsewhere the writer has true j. Read as the writer's i for j, by word sense. *tália* also drops *-al-* (normalized *találja*).
2. Row 3 *soraim*: the i has no dot of its own in its place; two dots stand above it, under the k of row 2 (*k* of that row has also a dot on the first occurrence, so they may belong to the k). The shape alone fits i better than o; the choice is shape plus word sense.
3. Row 4 *nagyoa*: two bars (a) clearly stand where n is expected before *rossz*. Normalized *nagyon*, as a slip; the a is on the card. *roszviszony-|ba* has a line-end hyphen on the card.
4. Rows 5/6: *álmomba|nagyon*: one n at the line break serves as the n of *nagyon*; *álmomba[n]* is supplied (colloquial -ba would also stand). *jutotam, önel* normalize single consonants.
5. Row 6 *agyodom* = *aggódom*; *nem-e* is an editorial hyphen.
6. Row 7 first sign (`{r}`): an overdrawn F, where *történt* needs t after row 6 *tör|*. Literal *törrént* or a corrected t; the word is not in doubt. Row 7 `{v}`: a heavily overdrawn chevron; *valami* by sense. *önne* has no l on the card.
7. Rows 8/9 *tudes|son*: the bars are three (e), normalized *tudasson*. *létetelől*: normalized as *hogylétéről* (or *hogyléte felől*): the signs are l é t e t e l ő l, all clear; the word is a misspelling and either normalization gives the same sense.
8. Row 10 *megylattalak*: gy is written for g.
9. Row 12 `{a}` in *csupa*: top bar overdrawn into a blot, lower bar visible; `{s}` of *boldogság*: fully overdrawn blot with an s-like outline; both by word sense. The p is h/p sign (*csuha* no word).
10. Row 15 small m in *rám*, squeezed before a real question mark. The pink smear beneath is ink offset, not a sign.
11. Row 16 `{a}` of *nálam*: a blot over the sign with a hole in it; the a is a restoration by word sense (*n?lam*), with the n also overdrawn. A loose dot in row 16 after *ne* has no value.
12. N1: small cramped signs under the grey portal stamp; first sign not a clean s; the r, e, t, l are clear. *szeretetel* is this family's spelling (hcp-1212, 1218).
13. Accents are transcribed only where seen. The writer's switch between *ön* and *te* forms is on the card.
14. Address, plain hand: first line above the postmark looks like *Szépreményű* (final letters run onto the ring, not fully legible; the formula is on hcp-1212), then Tóth Jolánka, úrleánynak s. k. (*ur leanynak s.k.*), Jász-Árokszállás. Postmark: FEB legible; the rest of the date not verified; portal file name says 1912-02-29. The printed picture text (*Sorrentói ábránd*) is not cipher.

## Why it is correct

- The family key, unchanged, turns every sign of all 18 rows and N1 into Hungarian; no sign lacks a value. The only deviations are ordinary misspellings of a writer known for them, and overdrawn signs flagged above.
- The text is coherent, with a concrete argument: a dream of quarrel, worry, request for news, love declaration, close.
- Family fit: *Isten vele*, *viszontlátásra*, *csókolja számtalanszor*, *Feri*, *szeretet[t]el*, *Jolánkám*, *egyetlen reményem*, *ön* address, addressee and place.
- Repeated words decode identically: *hogy* ×3, *édes* ×5, *boldog-* ×2, *nem* ×3.
