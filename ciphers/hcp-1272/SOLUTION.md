# HCP1272 — Feri to Jolánka Tóth: thanks for a card, greetings to cousin Ilonka

**Status: PARTIAL for the card as a whole. All ciphertext is read, with one weak phrase (item 2); about one line of the separate unenciphered note under the stamp stays unread (item 8), so no register entry is written (see Response to review 1).** Claude Opus 5.5, 2026-11-01.

Credit: new work by Claude Opus 5.5 on the key already established on the finished Jolánka cards (HCP1216 and sisters, whose earlier passes were by the OpenAI GPT solver and Claude Opus 5.5). No earlier work exists on this number. The portal shows *Not solved* with no transcription or solution; no published solution of this card was met.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka family, key taken from HCP1216, unchanged). Accents are marks over the base sign.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three strokes | m | gamma | t |
| short + long stroke | d | two strokes | n | plain cross | u |
| three bars | e | loop | o | chevron | v |
| open loop with descender | g | tall + short stroke | h / p | low descender | y |
| dotted crossed curve | i | inverted T | j | tailed cross | z |
| opposed bowls | cs | right bowl + tailed cross | sz | | |

Stroke calls here: d has the short stroke first, h/p the tall stroke first, n two equal strokes. h versus p is decided by word sense (*hogy, ha, lapját, lapon*).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1272/work/decode.py
```

It checks the SHA-256 of the four scans, decodes `work/ledger.txt` (a manual sign-by-sign transcription, 17 rows plus one line below the address) and prints `work/normalized.txt`.

## Literal decipherment

```
01 kedvesjolankam[lev]        10 erkezikkedvesem
02 [la]pjátmelyetna           11 hogymulatotjász
03 gyónköszönökiga            12 berénybeadjaátkö
04 zanörömmelvet=             13 szönetemetilonkauno
05 temtudomasulhogy           14 kanővernekbarismeret
06 szerencsésenmeg            15 lenvagyokeloteésad
07 érkezet.demégnagyobb       16 jaátüdvözletemet.magam
08 örömmemreszolgal           17 részérö{lm}asilaponistenvelesoraitvárva[Feri]
09 haszerencsevisza           below the address: szeretetel
```

## Hungarian (normalized)

Kedves Jolánkám! Levlapját, melyet nagyon köszönök. Igazán örömmel vettem tudomásul, hogy szerencsésen megérkezett, de még nagyobb örömömre szolgál, ha szerencsé[sen] visszaérkezik, kedvesem. Hogy mulatott Jászberénybe[n]? Adja át köszönetemet Ilonka unokanővérnek, bár ismeretlen vagyok előtte, és adja át üdvözletemet. Magam részérő[l] más[ik] lapon. Isten vele! Sorait várva, Feri.

Below the address, in cipher: Szeretettel.

Under the stamp, in plain hand: Isten vele, édes kis angyalkám, csókolom számtalanszor a mag(?)… [one line unread] hű kedvese(?) F.

## English

Dear Jolánka! Your postcard, for which many thanks. I was truly glad to learn that you arrived safely, but it will please me even more if you get back safely, my dear. How did you enjoy yourself in Jászberény? Please give my thanks to your cousin Ilonka, though I am a stranger to her, and pass on my greetings. For my own part, on another card. Farewell! Awaiting your lines, Feri.
Below the address: With love.
Under the stamp: Farewell, sweet little angel, I kiss you countless times … [one line unread] faithful sweetheart(?) F.

## Slovak

Milá Jolánka! Váš lístok, za ktorý veľmi ďakujem. Naozaj s radosťou som vzal na vedomie, že ste šťastne docestovali, ale ešte väčšou radosťou mi bude, ak sa šťastne vrátite, drahá. Ako ste sa zabávali v Jászberényi? Odovzdajte moju vďaku sesternici Ilonke, hoci ma nepozná, a odovzdajte jej môj pozdrav. Ja sám na inom lístku. S Bohom! Očakávajúc Vaše riadky, Feri.
Pod adresou: S láskou.
Pod známkou: S Bohom, sladký anjelik môj, bozkávam Vás nespočetnekrát … [jeden riadok neprečítaný] verný milý(?) F.

## Uncertainties

1. **Rows 1–2 `lev | la`** are ordinary cursive, not cipher; the rest of the word (`pját`) is enciphered. The cursive at the end of row 1 is a loop l followed by a small joined form, read *lev* only because *levlap* ("postcard") fits; the e and v are not clearly separate letters. Row 2 *la* is clear.
2. **Row 17 `{lm}asilapon`, the weakest point of the cipher text.** After *részérö* comes a cursive sign with three arches and a closing tail. Two descriptions fit: (a) the writer's ordinary cursive *m* (the same form as in his plain *Szépreményű*; compare his slips into cursive in *lev|la* and *Feri*), so that the l of *részéről* is not written at all: *részérő[l] más[ik] lapon*; (b) l and m run together. I now prefer (a), so the normalized text marks the l as supplied. The token `{lm}` in the ledger is kept only as a label for the sign. The plaintext is the same either way. The h/p sign is p by sense, and the k of *másik* is absent. The sense ("my own greetings on another card") is my interpretation, the sentence has no verb, and *lahon* (with the h value) is no word. It is one uncertain phrase, not an unread clause.
3. **Row 4 end**: after *ve* the sign is a gamma with an extended top bar and a second, lower bar. Two descriptions fit: a gamma (t) with an overlapping double hyphen, or one F-shaped sign (r). No other row break on this card has a hyphen, so the hyphen explanation has no support on the card. The value t rests on word sense only (*vet|tem*, continued in row 5): *vetrtem* and a letter a both give no word. The ledger's `T =` records that decision, not a clear shape.
4. **Row 5** `tem` has a cramped three-stroke m crowded against the next t; it is corrected or squeezed, but legible.
5. **Row 11**: the á of *Jász* is a blotted two-bar sign written over another shape, with an accent above. Read á by the word; Jászberény is near the addressee's Jászárokszállás.
6. **Row 12 `berénybe`**: *-be* is written where *-ben* is standard, and this is not a misread n.
7. Writer spellings normalized: *érkezet* → megérkezett, *örömmemre* → örömömre (three strokes twice, then e between), *szerencse* → szerencsé[sen] (ending missing; bare *szerencse* gives no grammar), *visza* → vissza, *mulatot* → mulatott, *elote* → előtte (no dots seen on o), *szeretetel* → szeretettel. Accents not visible are supplied.
8. **Plain-hand note under the stamp** is not cipher, is smeared by the stamp's removal, and is only partly read. *Isten vele / édes kis / angyalkám / csókolom / számtalan/szor* are secure. After them *a mag…* with a long descender at the line end is itself unsure. Then comes a line of which I see only two or three letters (r/s + o?), a point, and a word of about a dozen joined letters beginning t-e/ü-m/n, which is about a clause in all. Then *hű*, a last word, and a capital F. The last word's letters are not legible; *kedvese(?)* rests only on the parallel in HCP1216's stamp note (*csókolom számtalanszor sírig hű kedvese feri*), not on the pixels. That parallel may suggest a "faithful unto…" phrase, but the unread line is not written in from it. Local background subtraction on the green channel (work/note_crop.py, work/crops/note_local.png) separates the strokes better but gives no reading. The only other text on the card is the printed verse on the picture side, which is not part of the message.
9. **Row 2 `melyet`**: the sign between *e* and the descender is a wave followed by a further n-like arch with a short stem, not a plain one-hump wave. The ledger's `L` records the word-sense decision. *melyet* is certain as a word; the extra stroke is unexplained.
10. **Opening punctuation is editorial.** *Levlapját, melyet nagyon köszönök* is printed as a verbless fragment. The accusative may instead be the object of *vettem*: "Your card, for which many thanks, I truly received with joy, and noted that…". The sense barely changes; the English and Slovak follow the punctuation printed here.

## Why it is correct

- The key is unchanged from the family, and every enciphered sign in the 17 rows and the address line gets a value. Items 2, 3 and 9 are the places where the shape alone does not fix the sign and word sense does.
- The result is continuous, ordinary Hungarian, and word breaks across rows work (*na|gyon, iga|zán, vet|tem, meg|érkezet, visza|erkezik, Jász|berénybe, kö|szönetemet, uno|kanővérnek, ismeret|len, ad|ja*).
- Repeated words decode identically (*hogy, adja át, -etemet, kedves-, szerencs-*).
- Context fits the family: the Feri signature, the formal address, *Sorait várva*, *Isten vele*, and Jászberény next to the Jászárokszállás address.

## Response to review 1

Review verdict: REVISE. The reading of the ciphertext is unchanged; no letter of the ledger changed. I re-ran `python3 -I ciphers/hcp-1272/work/decode.py` after the edits: all four hashes print OK and the output carries the edited normalized text.

1. **Stamp note (major): accepted.** I rechecked the crops and made a new one (work/note_crop.py, work/crops/note_local.png). The line stays unread, so item 8 now states what is visible, marks *a mag…* as unsure, and says *kedvese(?)* rests on the HCP1216 parallel alone. No reading is written in from that parallel. On the question left open: the run's rule says a card with a whole unread clause is partial and gets no entry, and it does not exempt plain text, so I apply it to the card as a whole. Status is PARTIAL, and no register-entry.txt is written. The ciphertext alone is complete, so a human may overrule this.
2. **Row 17 token (minor): accepted.** On crop `hump` the sign has three arches and a tail, like the writer's cursive m. Item 2 now gives both descriptions and prefers the unwritten l; the normalized text prints *részérő[l]*. The token name stays, and the ledger comment is corrected.
3. **Row 2 sign (minor): accepted.** Crop `ly` shows the extra arch. Disclosed as item 9, and the claim that only one sign needs a special reading is withdrawn. The "unlike the one-hump wave l" argument is removed from item 2.
4. **Row 4 end (minor): accepted.** Crop `r4e` shows a single long top bar and a lower bar, which can be one F-shape. Item 3 now says t rests on word sense.
5. **Opening normalization (minor): accepted.** Noted as item 10; punctuation left as printed, since either option gives nearly the same sense.
6. **Row 17 sense (minor): no change possible.** I found no better parse. It stays disclosed in item 2 as one uncertain phrase.
