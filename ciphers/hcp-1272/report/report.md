# HCP 1272 (jolanka-17): Feri to Jolánka Tóth, thanks for a card and greetings to cousin Ilonka

Human solver: Tomáš Pavuk

**Status: partial. All enciphered text is read, with one weak phrase; about one line of a separate unenciphered note under the stamp stays unread. Independent review 1 verdict REVISE, findings addressed, no letter of the decipherment changed. No register entry is submitted.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1272 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1272), portal name cpc_1912-04-30_HU__HU_Jasz Arokszalas_jolanka-17, from Tobias Schrödel's collection of cryptographic postcards. When captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was found.

It is a tinted photographic greeting card of a young couple, with a printed Hungarian verse and the caption *Akiknek a szívük fáj*. The picture side has no handwriting. Everything written is on the address side, in red ink. The address is plain: **Szépreményű Tóth Jolánka úr leánynak, Jász Árokszállás** ("To the promising Miss Jolánka Tóth, Jászárokszállás"). The postmark legibly shows ÁPR 30; the year 1912 comes from the portal's file name and was not confirmed on the postmark.

The card belongs to the family of cipher postcards addressed to Jolánka Tóth, signed Feri on this card. Other family cards are deciphered in this repository (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). This card has no earlier work of its own. The key was worked out on those sister cards, whose earlier passes were by the OpenAI GPT solver and Claude Opus 5.5.

![Address side: the cipher text at left and along the bottom, the plain address, one cipher line under the address, and the note under the removed stamp (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: printed verse and caption only (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

This is a **known-key reading**, not a new key recovery. Claude Opus 5.5 transcribed the card by hand, sign by sign, from enlarged crops of the unconverted original scan: 17 rows plus one line under the address. It decoded them with the HCP 1216 key, unchanged. No OCR was used. Every sign falls in a known class of the family and no new sign is needed. The letter f does not occur in the cipher, as *Feri* is written in ordinary cursive.

Stroke order mattered. The short-then-long stroke is d, the tall-then-short stroke is h or p, and two equal strokes are n. Sorting these gave *tudomásul*, *kedvesem* and *adja*; treating them all as n gave nonsense. The choice between h and p is made by word sense (*hogy, ha, lapját, lapon*).

To reproduce, run from the repository root:

```text
python3 -I ciphers/hcp-1272/work/decode.py
```

It checks the hashes of the four scans, decodes the ledger work/ledger.txt and prints the literal and normalized text.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs. Accents are marks over the base sign. The labels below describe the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three strokes | m | gamma | t |
| short + long stroke | d | two strokes | n | plain cross | u |
| three bars | e | loop | o | chevron | v |
| open loop with descender | g | tall + short stroke | h / p | low descender | y |
| dotted crossed curve | i | inverted T | j | tailed cross | z |
| opposed bowls | cs | right bowl + tailed cross | sz | | |

## Plaintext

Literal decipherment. Square brackets mark ordinary cursive, not cipher; {lm} is the label for the sign in uncertainty 1.

```text
01 kedvesjolankam[lev]        10 erkezikkedvesem
02 [la]pjátmelyetna           11 hogymulatotjász
03 gyónköszönökiga            12 berénybeadjaátkö
04 zanörömmelvet=             13 szönetemetilonkauno
05 temtudomasulhogy           14 kanővernekbarismeret
06 szerencsésenmeg            15 lenvagyokeloteésad
07 érkezet.demégnagyobb       16 jaátüdvözletemet.magam
08 örömmemreszolgal
09 haszerencsevisza
17 részérö{lm}asilaponistenvelesoraitvárva[Feri]
below the address: szeretetel
```

Hungarian, normalized (word division, accents, spelling and punctuation are editorial):

Kedves Jolánkám! Levlapját, melyet nagyon köszönök. Igazán örömmel vettem tudomásul, hogy szerencsésen megérkezett, de még nagyobb örömömre szolgál, ha szerencsé[sen] visszaérkezik, kedvesem. Hogy mulatott Jászberénybe[n]? Adja át köszönetemet Ilonka unokanővérnek, bár ismeretlen vagyok előtte, és adja át üdvözletemet. Magam részérő[l] más[ik] lapon. Isten vele! Sorait várva, Feri.

Below the address, in cipher: Szeretettel.

Under the stamp, in plain hand: Isten vele, édes kis angyalkám, csókolom számtalanszor a mag(?)… [one line unread] hű kedvese(?) F.

**English.** Dear Jolánka! Your postcard, for which many thanks. I was truly glad to learn that you arrived safely, but it will please me even more if you get back safely, my dear. How did you enjoy yourself in Jászberény? Please give my thanks to your cousin Ilonka, though I am a stranger to her, and pass on my greetings. For my own part, on another card. Farewell! Awaiting your lines, Feri.

Below the address: With love.

Under the stamp: Farewell, sweet little angel, I kiss you countless times … [one line unread] faithful sweetheart(?) F.

**Slovak.** Milá Jolánka! Váš lístok, za ktorý veľmi ďakujem. Naozaj s radosťou som vzal na vedomie, že ste šťastne docestovali, ale ešte väčšou radosťou mi bude, ak sa šťastne vrátite, drahá. Ako ste sa zabávali v Jászberényi? Odovzdajte moju vďaku sesternici Ilonke, hoci ma nepozná, a odovzdajte jej môj pozdrav. Ja sám na inom lístku. S Bohom! Očakávajúc Vaše riadky, Feri.

Pod adresou: S láskou.

Pod známkou: S Bohom, sladký anjelik môj, bozkávam Vás nespočetnekrát … [jeden riadok neprečítaný] verný milý(?) F.

## What remains uncertain

- **Note under the stamp, the reason this card is partial.** It is not cipher, and it is smeared by the removal of the stamp. *Isten vele, édes kis angyalkám, csókolom számtalanszor* is secure. *a mag…* is unsure. The next line shows only two or three letters, a point, and a joined word of about a dozen letters, which amounts to about a clause. The last word is not legible; *kedvese(?)* rests only on the parallel note on HCP 1216, *csókolom számtalanszor sírig hű kedvese feri*. The unread line was not filled in from that parallel.
- **Row 17, *részérő[l] más[ik] lapon*, the weakest cipher phrase.** The cursive sign after *részérö* has three arches and a tail. It is probably the writer's plain cursive m with the l not written, or else l and m run together. The plaintext is the same either way. The k of *másik* is also missing, the phrase has no verb, and its meaning is an interpretation. The neighbouring signs are clear.
- **Row 4 end.** The sign can be a gamma with a double hyphen or one F-shaped r. The value t rests on word sense (*vet|tem*).
- **Row 2 *melyet*.** The sign read as l has an extra arch that stays unexplained; the word itself is certain.
- **Rows 1–2 *lev|la*** are cursive, not cipher, and *lev* is read by the sense of *levlap*, "postcard".
- **Row 11.** The á of *Jász* is blotted and read by the word.
- **Opening punctuation** is editorial. *Levlapját* may instead be the object of *vettem*: "Your card … I received with joy".
- **Writer's spellings** were normalized: *érkezet, örömmemre, szerencse* (ending missing), *visza, mulatot, elote, szeretetel*, and *-be* for *-ben* in *Jászberénybe*. Accents not visible are supplied.
- **The year** is known only from the portal's file name.

![The note under the stamp, green channel with the background subtracted: the lines from "szor a mag…" to the F (work/crops/note_local.png)](../work/crops/note_local.png)

## Review and what changed

An independent Claude Opus 5.5 reviewer ran the command, wrote its own decoder and transcription of all 18 rows with the key taken directly from HCP 1216, and found agreement on all 306 signs on base letters. Its transcription was not blind, as it had read the solver's text first. It checked the disputed places on crops and tried to find another reading, and did not refute the solution. Its verdict was **REVISE**, with six findings:

- Major: the stamp note leaves about a clause unread, and the consequence for completeness was not stated. **Fixed:** the note's status is now spelled out, and the card is recorded as partial with no register entry. The ciphertext alone is complete, so a human may decide otherwise.
- Minor: the row 17 sign was described too confidently. **Fixed:** both descriptions are given and the l is printed as supplied.
- Minor: the extra stroke in row 2 was undisclosed. **Fixed:** disclosed.
- Minor: the F-shaped alternative at row 4 end was not stated. **Fixed:** stated, and t is said to rest on word sense.
- Minor: the opening punctuation was an unflagged choice. **Fixed:** flagged.
- Minor: row 17 stays weak in sense. **Unchanged:** no better parse exists, and it stays disclosed.

No letter of the decipherment changed. Only the normalized text (*részérő[l]*), the description of the uncertain signs and the status changed. The reviewer could not read the unread line either, could not confirm the year from the postmark, did not compare accents sign by sign, and relied on the review of HCP 1216 for the key beyond its fit here.
