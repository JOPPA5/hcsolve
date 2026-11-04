# hcp-1180 – solution (round 1)

Card: HC Portal cryptogram 1180, "cpc_--___CH_Neuchatel_", T. Schrödel collection. Swiss 5 c
"Carte-correspondance" postal card addressed (in clear) to "Monsieur Oskar Egli au Credit Mutuel à
Neuchâtel". Postmark date reads "-VI 75" (June 1875, year digits faint). The message side is
written entirely as mock algebra. Portal status: Not solved; no transcription or solution attached.
Transcription, key and decipherment: Claude Opus 5.5, 2026-11-03. No earlier work on this number.
A short web search (Klaus Schmeh's blog, which features Schrödel cards) found no published
solution of this card.

## Cipher type and key

Vowel substitution disguised as algebra (register label: **MASC**; strictly a partial substitution: only the vowels are replaced, by digits, and consonants stay plain).

- Consonants stand for themselves (plain lower-case Latin script).
- Vowels are digits: **1 = a, 2 = e, 3 = i, 4 = o, 5 = u**; umlauts are fractions: **1/1 = ä, 5/5 = ü**.
- The signs `+ - = ( ) .` and the root sign `√` (written V in the transcription) are decoration
  and carry no letter value. Words are often, but not always, separated by `=`.

Example: `(w-2r+d)2 = 3c-h = d-3r` → werde ich dir.

## Command (run from repo root)

```
python3 -I ciphers/hcp-1180/work/decode.py
```

It checks the SHA-256 of the four images (source/ and work/hires/), then decodes
`work/transcription.txt` (my sign-by-sign transcription, Claude Opus 5.5) and prints:

```
werther kampfgenosse! ich befinde mech seit einigen tagen in ettiswil sobald ich wieder in altbüron residiere werde ich dir einen brief schreiben ich melde dir hiemit vorläufig das du mir keine zietung abonieren must werde dir dann die ursache mittheilen empfange unterdessen die saumäsigsten grüsse von plüs soli
-- left margin --
ettiswil den 35 stosmonat ano tubak
```

## Plaintext (German, 1870s Swiss spelling kept; editorial punctuation)

Werther Kampfgenosse! Ich befinde mech [= mich] seit einigen Tagen in Ettiswil. Sobald ich wieder
in Altbüron residiere, werde ich dir einen Brief schreiben. Ich melde dir hiemit vorläufig, das[s]
du mir keine Zietung [= Zeitung] abonieren must; werde dir dann die Ursache mittheilen. Empfange
unterdessen die saumäsigsten Grüsse von Plüs = Soli.

Left margin: Ettiswil, den 35. Stosmonat anno Tubak.

## English

Worthy comrade-in-arms! I have been in Ettiswil for some days. As soon as I am residing in
Altbüron again I will write you a letter. For now I just let you know that you need not take out
a newspaper subscription for me; I will then tell you the reason. Meanwhile receive the most
tremendous ("saumässig", Swiss slang) greetings from Plüs = Soli.
Margin: Ettiswil, the 35th of "Stosmonat", anno Tubak (a joke date; "anno Tubak" = "in the year dot").

## Slovak

Vážený spolubojovník! Už niekoľko dní som v Ettiswile. Len čo budem opäť bývať v Altbürone, napíšem
ti list. Zatiaľ ti len oznamujem, že mi nemusíš predplácať noviny; dôvod ti potom poviem. Medzitým
prijmi tie najstrašnejšie (švajč. slang „saumässig") pozdravy od Plüs = Soli.
Okraj: Ettiswil, 35. „Stosmonat", anno Tubak (žartovný dátum, „za dávnych čias").

## Uncertainties (all disclosed)

1. **h / k**: this hand uses one looped letter for both h and k. It is read k only in Kampf, keine
   and Tubak, on word sense; elsewhere h (ich, hiemit, schreiben, mittheilen, Ursache).
2. **Writer's slips, decoded literally**: `m-2c+h` = "mech" for "mich" (the digit is clearly a
   looped 2, not 3); `(z-3.2t)(5n-g)` = "Zietung" for "Zeitung" (the same 3.2 group gives "die"
   correctly in the last line). Before it the writer struck out a first attempt `z-2?t` (not decoded).
3. **must**: `m-5s+t`; the sign after 5 is partly covered by the HCPortal collection stamp; read s
   ("must" = musst). The order `5` then `s` is visible, the shape of s is not fully clear.
4. **mittheilen**: `m-3t+t-h-2V3l-2n`; the e (2) is inked over / blotted but its shape remains; old
   spelling "mittheilen" (pre-1901 th).
5. **saumäsigsten**: `(s-1+5m-1/1s)(3g-s-t)-2n`; the s in `3g-s-t` resembles a 5 (which would give
   "igut", no word); read s on word sense. Spelling with one s is the writer's.
6. **Margin date**: "35" is read as digits (day 35, a joke matching "anno Tubak"); the first digit
   has an open 3 shape. **"Stosmonat"** is read sign by sign (s t o s m - o n a t) but is not a
   month name I know; it is the one word whose meaning I cannot explain (a joke month?).
   "1n+4" = "ano" (anno).
7. **Signature** "Plüs = Soli" read literally (p l ü s / s o l i); possibly the surname Plüss and a
   nickname. The final sign of Soli is a 3 (i).
8. A faint pencil mark (a "3"/"5") above the first line is in a different medium (later
   annotation?) and is not part of the text.
9. Word division is editorial; on the card many word breaks fall on "=" but e.g. Altbüron|residiere,
   befinde|mech are separated only by "-".

The address side is ordinary plain writing; the imprinted stamp leaves no stamp box to hide
anything under, and the card has no picture. No steganographic part was found.

## Why I believe it is correct

- One fixed 7-symbol key (five digits, two fractions) turns every group on the card into German,
  with no unused or unexplained sign except the struck-out attempt.
- The text is coherent and fits context: Ettiswil and Altbüron are neighbouring villages in the
  canton of Lucerne; the recipient is in Neuchâtel; Swiss forms (saumässig, Tubak, hiemit,
  "residiere") and 1870s spelling (Werther, mittheilen) match the 1875 card.
- Digits occur only where a vowel is required and never where a consonant is.

## Response to review 1

Verdict ACCEPT; all four minor findings addressed, the decoded text is unchanged.

1. **Margin direction** – agreed. On the card the margin runs from top to bottom; it stands upright
   after a 90° counter-clockwise turn (new crop work/margin_upright.png from the hires scan shows
   `2t-t+3s+w-3l = d-2n = 35' = s+t-4s+m- / 4n-1-t = 1n+4 = t+5b-1+k .` upright). The comment in
   work/transcription.txt and NOTES.md are corrected; the line order and reading are unaffected.
   The left margin is written "vertically, running top to bottom".
2. **"must" nuance** – agreed: "du mir keine Zeitung abonieren must" = "you need not take out a
   newspaper subscription for me". English changed accordingly; Slovak changed to "nemusíš mi
   predplácať noviny".
3. **"Stosmonat"** – kept flagged as the one un-understood word: read sign by sign, meaning unknown,
   perhaps a joke month in the style of the old Swiss month names (Brachmonat, Heumonat). It is not
   presented as a known word. The rest of the card reads.
4. **Type label** – MASC kept as the nearest allowed register label; the key section now says
   explicitly that only vowels are substituted (digits/fractions) while consonants stay plain inside a
   mock-algebra disguise. No steganographic part: the card has an imprinted stamp (no stamp box) and
   no picture side, and neither side shows hidden, reversed or edge writing, so "MASC +
   Steganography" does not apply.

Reproduction command re-run after the edits (`python3 -I ciphers/hcp-1180/work/decode.py`): four
hash checks OK, output identical to the plaintext above.
