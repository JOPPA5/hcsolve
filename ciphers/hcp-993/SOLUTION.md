# hcp-993 – Solution (round 1, with response to review 1)

Card: HC Portal cryptogram 993, `cpc_1903-02-04_DE_Munchen_DE_Eschersheim_kellermann-01`
(T. Schrödel collection). Picture postcard "München – Wittelsbachbrunnen", Verlag Wagner & Weil,
München, No. 503. Dated by the writer "München d. 4. Febr. 03"; Eschersheim arrival postmark
"-4.2.03 6-7 V." (the München cancellation over the stamp is only partly legible, see Uncertainty 8).
Addressed "Fräulein Margarethe Kellermann / p. Adr. Herrn A. Weyhe / Hochwohlgeboren /
Eschersheim b/Frankfurt a/Main / Frankfurterstr. 49". Signed "Erich". Language: German.

All work in this directory is by Claude Opus 5.5 (2026-11-03). There is no earlier work on this number.
The portal page has status "Not solved" and no attached transcription or solution; I made the
transcription myself from the high-resolution scan (work/hires/). See "Published solutions" below.

## Cipher type and key

Simple monoalphabetic substitution (MASC) with digits and a few invented signs, one sign per letter.
The message is written on the picture side, card turned 90°; one sentence in plain German Kurrent
script is embedded in it (line 2–3), plus a plain date line. The last two cipher lines ("und Küssen /
Dein Erich") and two rows of dots are written upside down in the right half of the picture side.

| sign | letter | | sign | letter |
|---|---|---|---|---|
| 0 | o | | arch with a dot under it | i |
| 1 | l | | C-shaped hook with blob (like a reversed 6) | r |
| 2 | n | | reversed c | c |
| 3 | m | | capital I with serifs | z |
| 4 | e | | u-shaped cup | u |
| 5 | s | | pointed v | d |
| 6 | b | | oval crossed by long vertical (φ) | a |
| 7 | t | | + | f |
| 8 | h | | + with two bars (≠) | k |
| 9 | g | | z-like stroke joined to 0 (ligature) | w |
| | | | 0 with bar above (ō) | v |
| | | | U with two dots | ü |
| | | | 0 with two dots | ö |

Not attested on the card: j, p, q, x, y. ß is written as s/ss. The numeral "18" is written in plain
digits inside a box, to mark it as a number, not cipher.

## Command (run from the repo root)

```
python3 -I ciphers/hcp-993/work/decode.py
```

It verifies the SHA-256 of the four source images, then decodes `work/transcription.txt` (one token per
sign; restorations and the writer's slips are marked there) and prints the plaintext line by line.

## Plaintext (German; spelling normalised, line breaks of the card removed)

> München d. 4. Febr. 03
>
> Mein herzinniggeliebtes Herzens....! [Deinen lieben Brief habe ich erhalten. Bin kerngesund.] Werde
> von Tag zu Tag ungeduldiger, Dich bald wieder in die Arme schließen zu können. Nun sind es noch 18
> Tage bis dahin. Bin nur froh, dass mir diesmal kein Feldwebel einen Strich durch die Rechnung machen
> kann. Lieb! Dein E. wird Dich ganz und gar aufessen, wenn er kommt. Doch nun lebe recht wohl und
> grüße alle Lieben recht herzlich. Dich aber umarmt mit innigsten Grüßen und Küssen Dein Erich
> ........

The bracketed sentence is written in plain Kurrent, not enciphered. Decoder output as on the card:

```
L1   mein herzinniggeliebtes herzens....!
L2   Deinen lieben Brief habe ich erhalten. Bin kern=
L3   gesund. werde von tag zu tag ungeduld-
L4   iger dich bald wieder, in die arme schlie
L5   sen zu können. nun sind es noch 18 tage bis
L6   dahin. bin nur froh dass mir diesmal kein
L7   feldwebel einen strich durch die rechnung ma-
L8   chen kann. lieb! dein e wird dich ganz und
L9   gar aufessen wenn er kommt. doch nun lebe
L10  recht wohl. und grüsse alle lieben recht herz=
L11  lich. dich aber umarmt mit innigsten, grüssen.
L12  und küssen          (upside down)
L13  dein erich          (upside down)
L14  (.... ....)         (upside down, two rows of dots)
```

## English translation

Munich, 4 Feb. 1903. My most dearly beloved darling (lit. "heart's ....")! [I have received your dear
letter. I am in the pink of health.] I am growing more impatient from day to day to hold you in my arms
again soon. Now there are still 18 days until then. I am just glad that this time no sergeant can spoil
my plans (lit. "draw a line through the reckoning"). Dear! Your E. will eat you up completely when he
comes. But now farewell, and give my warmest regards to all your loved ones. And you are embraced, with
most heartfelt greetings and kisses, by your Erich ........

## Slovak translation

Mníchov 4. febr. 1903. Moja najvrúcnejšie milovaná srdiečko....! [Tvoj milý list som dostal. Som
zdravý ako repa.] Zo dňa na deň som netrpezlivejší, že ťa čoskoro znova zovriem v náručí. Teraz to
ešte potrvá 18 dní. Som len rád, že mi tentoraz žiadny šikovateľ nepreškrtne plány. Milá! Tvoj E. ťa
celú zje, keď príde. Ale teraz sa maj veľmi pekne a srdečne pozdravuj všetkých svojich drahých. Teba
však objíma s najvrúcnejšími pozdravmi a bozkami Tvoj Erich ........

## Uncertainties (all disclosed)

1. Ink smear (a vertical wiped band across the left part of the text). Signs restored there:
   - "Feldwebel" (L7): the sign between the 2nd and 3rd e is smeared; the e's and final l are visible;
     restored as 6 = b (only letter that makes a word). Context (a soldier on leave) supports it.
   - "aufessen" (L9): "auf" (φ U +) and "sen" (5 4 2) are clear; the smear hides about two signs
     (spacing measured: about three sign-advances between + and 5). Restored as "es". This is a
     two-sign restoration; the alternative "auffressen" would need four hidden signs and fits the
     spacing worse. The meaning ("eat you up") is the same either way.
   - "wohl" (L10): w-ligature and a faint 0 visible, one sign smeared, then 1; restored h.
   - "kann" (L8): ≠, φ and two 2-signs are visible through the smear, faintly.
   - "bis" (L5): the last sign at the card edge is partly smeared (a 5 with its top bar is visible).
   - "bin" (L6) first sign and "recht" (L10) first word are faint but readable.
2. Writer's slips:
   - "ungeduld-iger" (L3–L4): the card has U 2 9 4 V U 1 – then "iger": the second d is not written
     (supplied, marked <V> in the transcription).
   - "dahin" (L6): the third sign is 6-like (closed lower loop, heavy ink-filled upper part); it may
     be a 6 (b, giving "dabin") or an 8 with a blotted upper loop. Read as h (8) on word sense; the
     reading is the same either way.
   - "schliesen" with a single s for ß; normalised to "schließen". The final "grüssen" (L11) does
     carry umlaut dots above the U (corrected after review 1); normalised to "Grüßen".
3. The w-sign is a ligature of a z-like stroke and an 0; I treat it as one sign (it occurs in werde,
   wieder, wird, wenn, wohl). Reading it as two signs gives no words.
4. "r" (hook) vs "b" (6): the two signs are similar; the r-hook has an open bowl and a blob foot, the 6
   a closed bowl. In "bin" (L6) and "nur/mir" the call partly rests on word sense.
5. Plain Kurrent sentence: "Bin kern=gesund" – the word "kern" is a dense Kurrent scrawl; k is clear
   (tall loop), the humps after it are read as e-r-n on word sense ("kerngesund" is idiomatic).
   Date line "Febr." could be "Fbr."; the postmark confirms February.
6. "Herzens....!" ends in dots on the card – the endearment is left unfinished on purpose (the noun is
   not written). "Lieb!" stands alone as written. "Dein E." is a single 4 (e) – the writer's initial.
7. Steganography check: the picture side holds the whole message; nothing hidden was found in the
   picture or margins. On the address side the stamp is still affixed, so nothing under it can be
   checked from the scans; no writing is visible around it. The two rows of dots at the end are
   plain dots (kisses/sign-off), not a code as far as can be seen.
8. Postmarks: the Eschersheim arrival mark reads clearly "-4.2.03 6-7 V." (4 Feb 1903, 6-7 a.m.).
   The München cancellation is struck over the stamp and only partly legible: "MUENCHEN", "03", a
   "3" and stacked month letters that are unclear (they look like DEZ; FEB cannot be confirmed).
   It does not confirm the date. A morning arrival on 4 Feb implies posting in München on 3 Feb,
   although the writer dated the card "d. 4." (written late on the 3rd, or misdated).

## Why I believe it is correct

- Every cipher sign on the card (about 330 signs) decodes with one fixed table of 23 signs to
  grammatical, idiomatic German of 1903 with consistent spelling; no sign has two values.
- The plaintext matches the card's context: written in München, to a young woman (Fräulein) staying
  with a family in Eschersheim; the writer is a soldier ("Feldwebel", leave in 18 days); signed Erich.
- The embedded plain Kurrent sentence ("Deinen lieben Brief habe ich erhalten. Bin kerngesund.")
  joins seamlessly with the enciphered text on both sides.
- Long words with repeated letters fix the key independently: herzinniggeliebtes, Herzens, Rechnung,
  ungeduldiger, innigsten.

## Published solutions

None found. The portal attaches only a link to T. Schrödel, "Cryptographic postcards" (HistoCrypt 2021);
its abstract page gives no decipherment of this card (the full PDF was not checked).

## Register type

MASC (digit/symbol substitution). No register entry is written in this round (README: only after the
review).

## Response to review 1

Review 1 (Claude Opus 5.5, verdict ACCEPT) had four minor findings. All are accepted and fixed; the
plaintext is unchanged apart from the umlaut on the last word of L11 and one full stop.

1. **Umlaut dots on the final "Grüßen" – fixed.** I re-checked the crop (review/work/z_grussen.png,
   also work/crops/z_grussen.png): two dots stand clearly above the U of 9 hook U 5 5 4 2. The
   transcription now has `Uuml` there; the "ink running dry" remark is removed from Uncertainty 2.
2. **Postmarks – fixed.** The card header now quotes the Eschersheim arrival "-4.2.03 6-7 V." only and
   gives the full address including "p. Adr." and "Hochwohlgeboren". The München cancellation is
   described as partly legible (new Uncertainty 8; review/work/stamp.png shows "MUENCHEN", "03", a "3"
   and unclear month letters) and is no longer claimed to confirm the date. The posting-day
   discrepancy (arrival early on 4 Feb, written date "d. 4.") is stated.
3. **"dahin" – fixed wording.** Uncertainty 2 now says the third sign is 6-like and possibly an 8 with
   a blotted upper loop (review/work/z_dahin.png); the reading h on word sense stays. The marker
   {6=8} in the transcription is kept, as the more cautious notation.
4. **Full stop after "wohl" – fixed.** Added to L10 of work/transcription.txt.

Re-run after the fixes: `python3 -I ciphers/hcp-993/work/decode.py` prints "source hashes OK" and the
output shown above (L10 "recht wohl. und grüsse ...", L11 "... innigsten, grüssen."). The reviewer's
independent decoder (review/work/verify.py, run read-only on the corrected transcription) gives the same
lines and the same counts: 337 signs read on the card, 6 restored, 1 supplied, 1 emended.

Steganography check repeated in the light of the observation (from the human's colleague) that hidden
messages under the stamp are common on another postcard series: on this card the stamp is still
affixed, the scans show no writing at its edges, and no hidden text is visible elsewhere. The type stays
MASC; it cannot be excluded that something lies under the stamp.

Register type: MASC.
