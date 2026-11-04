# HCP 1208 (cpc_1914-10-15_HU__HU_Budapest_jolanka-55): Feri to Jolánka Tóth, the cancelled train

Human solver: Tomáš Pavuk

**Status: deciphered in full (420 signs in 22 main rows and 5 rows round the stamp, with a few single-sign points disclosed below); independent review 1 verdict REVISE, findings addressed, last sentence corrected. Type MASC + Steganography.** Report dated 2026-11-02, stamp-box section added 2026-11-03.

## Origin and context

The cryptogram is record 1208 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1208), portal name cpc_1914-10-15_HU__HU_Budapest_jolanka-55, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was found.

The address side carries a plain address in pencil, "Önagysága / Tóth Jolánka / úrleánynak / Budapest / István út" and a number group under the collector's stamp, tentatively 5 sz. II. e. 5 a (house, floor, door). The name and town are certain; the number group is not, and it does not bear on the message. The postmark reads BUDAPEST 914 OKT 15. The whole left half of the side is filled with cipher in violet pencil, partly under the postmark and its wavy cancellation. Five more rows of cipher are written inside the stamp box, where the stamp covered them; the stamp is now lifted (see "Message under the stamp").

The picture side is a printed comic card with the caption "A szerelem hőmérője. Aztán, hogy megöleltelek lett „16" fok a meleg." ("Love's thermometer. And then, when I embraced you, the heat rose to 16 degrees.") and publisher number 34213/4. It has no handwriting.

![Address side with the cipher (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, print only (source/picture-large.jpg)](../source/picture-large.jpg)

The card belongs to the family of Hungarian cipher postcards from Feri to Jolánka Tóth, several of which are deciphered in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). The key comes from those cards; this card was read with a **known, transferred key**. It is not a new key recovery.

## Method

The transcription is manual, sign by sign, from the portal's un-converted original scan (3421 × 2176 pixels), on enlarged crops. Rows 4 to 10 could not be read on the plain scan, because the postmark and cancellation run across them. A map of blue minus green removes the black ink and leaves the violet pencil, and those rows were read on that map together with saturated colour crops.

The key was applied unchanged; every sign on the card falls into it and no new value was needed. The final transcription, `work/ledger.txt`, records signs as shape classes rather than letters, and `work/decode.py` applies the key, so the plaintext is produced mechanically. The only word-sense choices inside the key are marked in the ledger: the tall + short sign as h or p, and the 5-shape as k or g.

Two independent checks support the text. It says "holnap, azaz pénteken" (tomorrow, that is Friday), and 15 October 1914, the date of the postmark, was a Thursday. And the last sentence, read from the signs, is the family's standard formula.

To reproduce, from the repository root: `python3 -I ciphers/hcp-1208/work/decode.py`.

## Key

**Cipher type: MASC + Steganography** (updated 2026-11-03). A simple monoalphabetic substitution with invented graphic signs; part of the message is hidden in the stamp box, under the stamp. Digraphs are written with two signs (c+s, s+z, g+y). Dots or strokes over a sign give ö, ü, ű, é, á.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark or 5-shape | k (also g) | F-like, two bars | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| long stroke + tick on the left | d | two equal strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall + short stroke | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | | | | |

## Plaintext

Literal decipherment, row by row, with no word division (as on the card):

```text
01 szeretetedesjolankam        12 holnapazazpentakan
02 kivanomhogyalegjobbked      13 delutanszabadleszeke
03 vebentaleljasoraim          14 eshogyelmehtekemagá
04 sajnalomhogyeztalapot       15 hozédesemmivelmég
05 kelkuldenemmertmagais       16 nemtudomhogyhova
06 gondoljahogyvalami          17 megyünkesmikorjö
07 különösdologadtaelo         18 vűnkviszszadehale
08 magatsajnalattalkeltu       19 hetelmegyekezel
09 datnomedesemhogyavona       20 bezaromsoraim
10 tunkatlemondjakesigy        21 maradoksirighű
11 mostmarnemtudomhogy         22 kedveseferi
under the stamp: csokol / szam / talan / szor / ferid
```

**Hungarian (normalized):** Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Sajnálom, hogy ezt a lapot kell küldenem, mert maga is gondolja, hogy valami különös dolog adta elő magát. Sajnálattal kell tudatnom, édesem, hogy a vonatunkat lemondják, és így most már nem tudom, hogy holnap, azaz pénteken délután szabad leszek-e, és hogy elmehetek-e magához, édesem, mivel még nem tudom, hogy hová megyünk és mikor jövünk vissza, de ha lehet, elmegyek. Ezzel bezárom soraim, maradok sírig hű kedvese, Feri. Under the stamp: Csókol számtalanszor Ferid.

**English:** My beloved sweet Jolánka! I wish that my lines may find you in the best of moods. I am sorry to have to send this card, since you too will think that something unusual has come up. I must tell you with regret, my darling, that they are cancelling our train, and so I now do not know whether I shall be free tomorrow, that is Friday afternoon, and whether I can go to you, my darling, because I do not yet know where we are going and when we are coming back; but if it is possible, I will go. With this I close my lines; I remain, faithful unto the grave, your sweetheart, Feri. Under the stamp: Your Feri kisses you countless times.

**Slovak:** Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Mrzí ma, že musím poslať tento lístok, lebo aj Vy si pomyslíte, že sa stalo niečo zvláštne. S ľútosťou Vám musím oznámiť, drahá, že náš vlak rušia, a tak teraz neviem, či budem zajtra, teda v piatok popoludní voľný a či budem môcť prísť k Vám, drahá, lebo ešte neviem, kam pôjdeme a kedy sa vrátime; ale ak to bude možné, prídem. Týmto končím svoje riadky a zostávam až do hrobu verný Váš milý, Feri. Pod známkou: Bozkáva Vás nespočetnekrát Váš Feri.

## Message under the stamp

Added 2026-11-03 after a stamp-box audit. The five rows earlier described as "round the stamp" lie inside the dotted frame of the stamp box. The postmark circle stops at the frame, so the stamp was on the card when it was cancelled and these rows were hidden under it. The stamp has since been lifted; a green triangular patch of residue with a round hole remains, and three of the rows run across it. The rows are in the cipher signs, read with the same key: "csokol / szam / talan / szor / ferid", that is **Csókol számtalanszor Ferid** ("Your Feri kisses you countless times"; Slovak "Bozkáva Vás nespočetnekrát Váš Feri"). Nothing in the box is left unread. This hidden placing is why the card is typed MASC + Steganography.

![The stamp box at 2x, with the cipher rows under the lifted stamp (work/stamp-2026-11-03/stamp_box_2x.jpg)](../work/stamp-2026-11-03/stamp_box_2x.jpg)

## Uncertainties

The writer's spelling is kept in the literal text; word division, accents and spelling in the normalized text are editorial. His slips include "talelja" (találja), "pentakan" (pénteken), "kel" (kell), "ezel" (ezzel) and "elmehtek" (elmehetek).

- **Rows 4 to 10** lie under the postmark and cancellation. All visible strokes fit the words given, but "ezt a lapot", "maga is", "a vona-" and "lemondjak" rest partly on word sense. The d of "dolog" in row 7 rests on word sense alone.
- **Row 10 "lemondjak"** has no accent visible. I read "lemondják" (they cancel). A first person "lemondjak" (that I should give up our train) is grammatically possible and would change only that clause.
- **"Our train"** is not explained by the card. HCP 1228 has Feri in railway clothes, which may be the background, but that is a hint and not evidence.
- **Row 20**: the r of "bezarom" has a faint low arm; gamma t is the alternative and gives no word.
- **Row 21 "sirig"**: the fourth letter is a heavy overwritten blot, read i partly on sense. The final sign is a 5-shape read g.
- **g and k, h and p** are near-homographs in this hand. The choices rest on word sense and are explicit in the ledger.
- **Stamp row S3** starts with a sign close to a chevron, read t because v gives no word.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) cropped the scan itself, wrote its own transcription in sign classes, and decoded it with the family table. It confirmed the key, the type, and rows 1 to 18, including the rows under the postmark. Its verdict was REVISE. Changes made:

- **The closing sentence was misread and is corrected.** Row 20 was first read "banatom" and row 21 "szretok" ("Ezzel bánatos soraimmal maradok szerető [s] hű kedvese"). The signs give "bezarom" and "sirig", the family's formula. Row 19 has "hetel", so no slip there.
- **Row 7**: the d of "dolog" is now disclosed as resting on word sense.
- **The decoder** was only printing a ledger written in letters. The ledger now holds sign classes and the script applies the key.
- **Accents** seen at the ends of rows 14 and 15 are now recorded.

The reviewer also questioned the first reading "még hoz[zád]" at the ends of rows 14 and 15. On rechecking that place the solver found a sign that both had missed. Row 14 runs on across the printed divider of the card, past the g, with two bars and an acute (á); and the bars before the g are two, not three. Row 14 ends "magá" and joins row 15 "hoz": **magához**, "to you". The sense of the clause stays the same, no letter has to be supplied, and the formal address holds. The reviewer has not seen this last correction. The right edge of all other rows was searched for signs past the divider, and there are none.

![End of rows 13 to 15: "magá" across the divider, with the acute above the last two bars, and "még" below it (work/row14-15-end.jpg)](../work/row14-15-end.jpg)
