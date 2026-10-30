# HCP1212 - A letter, love verse and dinner

**Status: main text deciphered with disclosed source spelling variants; small address annotation unresolved.** This is a working edition, not an independently accepted complete-card solution. Work date: 2026-10-13.

## Source and method

The HC Portal card dated 17 February 1912 was marked Not solved when acquired. All three portal tabs and both sides were inspected; no attached transcription or solution was provided. Tóth Jolánka is the addressee. The cipher sign-off spells Feri. The scans and metadata remain unchanged; SOURCES.md records their origin and hashes.

The Hungarian text uses graphic monoalphabetic substitution. The key was transferred from HCP1301/1243 and compared directly with this card. The main ledger is manually entered from visible shapes after earlier hypotheses were known; it is not blind OCR. Colour threshold views help separate neighbouring red strokes but add no source resolution. The original scan remains the authority.

## Hungarian editorial reading

Édes Jolánkám! Becses sorait köszönettel megkaptam, melyek örömemre szolgáltak, és az alat[t]i sorokban válaszolok.

Kivel bizonyítsam,
hogy téged szeretlek?
Tanúm, ki [alkoté → alkotá?] a nagy
mindenséget.
Hogy csak érted élek,
s érted szenvedek,
és [mindenemnél?] a földön
jobban szeretlek.

A vacsora elég kedélyes volt, és hogy mit ad vissza, azt nem értem. Isten vele.

Bottom sign-off: A viszontlátásra, szeretettel, Feri.

Small address-side cipher annotation: […].

## English translation

My sweet Jolánka! I have received your valued lines with thanks; they gave me joy, and I reply in the lines below.

Whom shall I call upon to prove
that I love you?
My witness is he who [created?] the great
universe.
That I live only for you,
and suffer for you,
and love you more
than [everything I have?] on earth.

The dinner was quite pleasant, and I do not understand what you are giving back. Farewell.

Bottom sign-off: Until we meet again, with love, Feri.

Small cipher annotation beside the address: […].

## What changed and what remains uncertain

All 17 main rows, including the verse, dinner statement and Feri sign-off, now have an intelligible reading. Source kivel is retained rather than changed to mivel: the next line calls the creator as witness. Alkoté and mindenemél remain disclosed source spelling variants; the suggested normalizations are qualified. The dinner phrase is ad vissza, resolved by distinguishing two bars from a neighbouring corner stroke and separating the two right bowls after i. The small address annotation remains unresolved; szeretettel and tisztelettel are only competing formula hypotheses, not established text. No complete-card completion marker or register entry is created.

The literal row-15 sequence after mit is A D V I ) ) Z A, decoding ad vissza. The earlier edv{?}ze resulted from including the preceding corner's top stroke when counting horizontal bars, and failing to separate two bowls. dinner-word-pass5.png makes this correction inspectable. The card does not explain what is being returned, so no object is invented in the translation.

The verse's source kivel literally asks “with whom/by whom”; the English renders its witness construction. The unaccented tanum and the following ki alkoté a nagy mindenséget support the creator-as-witness reading. The source mindenemél is normalized tentatively to mindenemnél; the added n is not a seen glyph. The bottom source szeretel is normalized to szeretettel. Other editorial spacing, punctuation and accents are not claimed as separate encoded characters. Original period spelling is retained where useful.

The tiny annotation beside kisasszonynak has overlapping and cramped strokes. Its middle resembles zeletetel. Neither a full szeretettel nor a full tisztelettel can yet be demonstrated sign by sign. The ordinary cursive stamp note is separate from the main encrypted text and is not presented as a decoded cipher. Searches for the apparent verse found no matching published text; no candidate poem supplied missing letters.

## Working key


At this scan resolution h/p are near-homographs and sometimes require linguistic context; d/n can also differ only by stroke length. The shape names below describe tendencies, not a guaranteed visual classifier. This qualification follows the independent HCP1301 review that arrived during this batch.

| Named graphic class | Letter |
|---|---|
| two-bars | a |
| six | b |
| left-bowl | c |
| joined-two-strokes | d |
| three-bars | e |
| cross | f |
| open-loop-descender | g |
| two-tall-strokes | h |
| dotted-crossed-curve | i |
| inverted-T | j |
| section-mark | k |
| wave | l |
| three-short-strokes | m |
| two-short-strokes | n |
| cursive-loop | o |
| tall-short-stroke | p |
| F | r |
| right-bowl | s |
| gamma | t |
| x | u |
| chevron | v |
| low-descender | y |
| crossed-diagonal | z |
| two-bars:acute | á |
| three-bars:acute | é |
| dotted-crossed-curve:acute | í |
| cursive-loop:acute | ó |
| cursive-loop:diaeresis | ö |
| cursive-loop:double-acute | ő |
| x:acute | ú |
| x:diaeresis | ü |
| x:double-acute | ű |


## Reproduction and evidence boundary

Run from the repository root:

```sh
python3 batches/jolanka-next-five-2026-10-12/visual-ledgers/decode.py 1212
```

The command checks the address scan hash and decodes all 17 main rows, including the footer, from work/as-seen-main-pass4.txt. The current ledger name preserves its creation pass; row 15 was corrected in pass 5, and the previous version is archived separately. work/as-seen-decoded.txt stores the result. The command does not decode the tiny annotation and does not turn pixels into letters automatically. The normalized reading and translation are editorial layers above the literal output.

## Review status

No independent full-card acceptance is claimed. All three original source hashes were verified. The small annotation keeps this card short of a complete-card decipherment; no DONE or FINAL marker and no register entry are created. Prior hypotheses and failed readings are retained in work/ and NOTES.md.
