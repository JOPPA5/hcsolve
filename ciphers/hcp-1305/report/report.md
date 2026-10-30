# HCP 1305 (cpc_1912--_HU__HU_Jasz Arokszalas_jolanka-98): Fery to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: the whole card is read and every sign has a value; one word (*tustkantek*) is transcribed but not understood. Independent review 1 verdict REVISE; its findings are addressed here.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1305 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1305), portal name cpc_1912--_HU__HU_Jasz Arokszalas_jolanka-98, part of Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a hand-tinted photograph of a couple, the woman holding flowers. Its only added marks are pink ink splashes at the upper left, which are not text. The whole message is on the address side, in red ink: 19 rows across the left half of the card, one word running up the right edge, and six short rows written over the place of the stamp. Plain Latin script is used for the address and for two insertions inside the cipher text, "Koth. Leg." and "20 án".

The card is addressed to Miss Jolánka Tóth at Jászárokszállás (Hungary). The file name on the portal says 1912, but the postmark is too blurred to confirm a date, so the date is not established. The writer signs *Fery*. The card belongs to the family of Jolánka cards in this repository (for example HCP 1216, 1217 and 1218), from which the key was taken.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: cipher rows at the left and bottom, the edge row at the lower right, and the block over the stamp at the upper right (source/address-large.jpg)](../source/address-large.jpg)

## Method

The card was read with a **known, transferred key**. This is not a new key recovery. The transcription is manual: Claude Opus 5.5 read every sign from enlarged crops of the high-resolution address scan and recorded it in a sign ledger, with no OCR. A short script then checks the hashes of the scans and decodes the ledger. The family key decoded the card without change, into Hungarian, with no sign left over and no new value.

In review a separate Claude Opus 5.5 agent made its own crops, transcribed all the signs itself, and decoded them with the family key file rather than the solver's script. The two readings differed in one sign of 345. That sign was corrected, and the two readings now agree in all 345.

## Key

Simple monoalphabetic substitution with invented graphic signs, the Jolánka family key (the sign names are conventional descriptions):

| Sign | Plain | Sign | Plain |
|---|---|---|---|
| two bars | a | section mark | k |
| six | b | wave | l |
| left bowl | c | three strokes | m |
| short stroke, then tall | d | two strokes | n |
| three bars | e | cursive loop | o |
| upright cross | f | F-like sign | r |
| open loop with descender | g | right bowl | s |
| tall stroke, then short | h or p | gamma | t |
| dotted crossed curve | i | plain cross | u |
| inverted T | j | chevron | v |
| low descender | y | crossed diagonal with tail | z |

Dots over o and u give ö and ü, and a tick over a vowel gives an acute accent, though accents are often absent. On this card *gy* and *ny* are written as two signs. The h and p signs cannot be told apart here, so each choice between them rests on word sense.

## Plaintext

Literal decipherment, row by row. `{a|e}` marks a vowel left open, and square brackets mark plain Latin script on the card.

```text
01 cszeretetedesjo
02 lankamkivanomhogy
03 alegjobkedveben
04 talaljasoraimhogy
05 mulatharasztin
06 esmiujsagmagok
07 feléamam{a|e}haza
08 jöttemartudatom
09 édesemhogy[Koth.Leg.]egy-
10 letimulatság[20án]
11 leszamielégrocz
12 korlemivelakor
13 akarjolánkahest
14 remigydazénre-
15 menyeimtustkantek
16 meginthétfonéj
17 jelvoltegykis
18 tüzünkismostmastnemírhatokmint
19 hogyirjonmagaisistenveleaviszont
20 l{a|e}tasra
s1 üdvöz
s2 lome
s3 tavol
s4 bol
s5 hüked
s6 vesefery
```

Normalized Hungarian (word division, accents and bracketed repairs are editorial):

**Szeretet[t] édes Jolánkám! Kívánom, hogy a legjob[b] kedvében találja soraim. Hogy mulat Harasztin? És mi újság magok felé, a mama haza jött-e már? Tudatom, édesem, hogy Kath. Leg. egyleti mulatság 20-án lesz, ami elég ros[s]zkor le[sz?], mivel ak[k]or akar Jolánka Pestre, mi így d[e] az én reményeim [tustkantek] megint. Hétfőn éjjel volt egy kis tüzünk is. Most mást nem írhatok, mint hogy írjon maga is. Isten vele, a viszontlátásra.**

**Under the stamp: Üdvözlöm e távolból. Hű kedvese, Fery.**

Address, in plain script: Szépreményű Tóth Jolánka úrleánynak, Jász Árokszál[l]ás.

English translation: **My beloved sweet Jolánka! I wish that my lines may find you in the best of spirits. How are you enjoying yourself at Haraszti? And what is new over your way, has mother come home yet? I let you know, my sweet, that the Catholic Young Men's Association ball will be on the 20th, which is rather badly timed, since Jolánka means [to go] to Pest then, so my hopes [word not understood; sense unknown, perhaps something like "came to nothing"] again. On Monday night we had a small fire as well. I cannot write anything else now, except that you should write too. God be with you, until we meet again.**

**Under the stamp: I greet you from this distance. Your faithful sweetheart, Fery.**

Address: To the promising Miss Jolánka Tóth, Jászárokszállás.

Slovak translation: **Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky našli v tej najlepšej nálade. Ako sa zabávate v Haraszti? A čo je nové u Vás, vrátila sa už mama domov? Oznamujem Vám, drahá, že zábava Katolíckeho spolku mládencov bude 20., čo je dosť nevhodne, lebo vtedy chce Jolánka [ísť] do Pešti, takže moje nádeje [slovo nepochopené; zmysel neznámy, možno niečo ako „vyšli navnivoč"] zase. V pondelok v noci sme mali aj malý požiar. Teraz nemôžem napísať nič iné, len aby ste napísali aj Vy. S Bohom, dovidenia.**

**Pod známkou: Pozdravujem Vás z tejto diaľky. Váš verný milý, Fery.**

Adresa: Nádejnej slečne Jolánke Tóthovej, Jászárokszállás.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1305/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the two portal scans and the two high-resolution originals, decodes the manual sign ledger work/ledger.txt and prints the literal rows, then prints the normalized text from work/normalized.txt. It does not read the image: the transcription step is manual and was checked independently in review.

## Uncertainties

- **`tustkantek` (row 15) is not understood.** All ten signs are clear: t u s t k a n t e k. Its sense is unknown. The sentence would fit something like *füstbe mentek* ("went up in smoke") or *tönkrementek* ("were ruined"), but each needs several signs changed, so these are guesses at the sense only. Whether *megint* ("again") closes this sentence or opens the next is also open.
- **Haraszti (row 5).** The letters are `harasztin`. Taking this as the place name Haraszti with a locative ending rests on word sense, and which Haraszti is meant cannot be shown. Sister card HCP 1310, row 18, has `darasztin` in a similar context, with d as its first sign, so this is probably one recurring name.
- **Pest (row 13)** is p by word sense on the h/p sign, since *hest* is no word. The sentence has no verb, and *Jolánka* in the third person may be a polite usage for the addressee or another person of that name.
- **Bare signs.** The `le` in row 12 is taken as an unfinished *lesz*, and the `d` in row 14 as *de* with its e elided. Both are guesses.
- **Row 1, first sign.** The card has an extra left bowl before *sz*. With the right bowl it looks like the family's opposed-bowls sign for *cs*, written by mistake, or it is a false start. Row 11 has *rocz* where *rossz* is meant; the writer seems to confuse the two bowls.
- **Open vowels.** In row 7 the vowel after the second m has two or three bars (*mama* by sense). In the bottom-right corner the edge row crosses the end of row 18. The t of *mint* can be seen there, but three strokes remain for the vowel of *l_tásra*, so it may be literally e, a slip for á. *látásra* is by word sense.
- **Other marks.** In row 18 the a of *hatok* is struck over, and small extra ticks on two m signs are read as pen slips. In the stamp block a smear covers part of the second row, and the first ü is blotted.
- **Normalization.** Missing dots and accents are supplied. *Koth.* in plain script is taken as *Kath.* and expanded as Katholikus Legényegylet, which the cipher text *egyleti* continues directly.
- **Date and persons.** The date is not established, and Fery's civil identity is unknown.
- **Key.** The key was transferred from the family cards, not recovered blind from this card. The reading used expected family formulas, and the word-sense calls above are stated so that they can be tested. No search for a prior publication was made beyond the portal status and the AI Decipherment Register (no record for this card, checked on 2026-10-30).

The reasons for confidence are these: the unchanged key turns the whole card into Hungarian; the opening and closing match the family formulas (for example *Kívánom, hogy a legjob[b] kedvében … találja soraim* on HCP 1218); long unforced words come out (*tudatom*, *egyleti mulatság*, *reményeim*, *viszontlátásra*, *távolból*); the cipher word *egyleti* joins the independent plain-script "Leg."; and two transcriptions agree sign for sign.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. It ran the command, read every row independently from its own crops, and confirmed the key, the cipher type and the overall reading. Its findings and what changed:

- **Row 17, first sign (major).** It is j, not f. The sign is an inverted T like the j signs, not a cross like the f signs, as shown below. The solver's *éjfél* ("midnight", which also needed a supplied ending) became *éjjel*, across the row break: "On Monday night we also had a small fire".
- **Row 5 (major).** The solver had changed h to p to get an awkward *parasztin* ("among the peasants"). The literal letters are kept and read as the place name *Harasztin*. The review said no other family card has this name; the sister parallel on HCP 1310 was added in response.
- **`tustkantek` (minor).** The translations no longer say "probably".
- **Corner (minor).** The t of *mint* is no longer queried. The vowel `{a|e}` stays open, since the crossing strokes do not settle it.
- **Row 1, hyphens, status line (minor).** The *cs* possibility is noted, the two hyphens on the card are now in the ledger and output, and the status text was updated.

![Row 17, first sign, compared with others (left to right, from review/work/crops/z_jf_compare.png): the sign in row 17, j of row 8, j of row 13, j of row 3, f of row 7, f of row 16](../review/work/crops/z_jf_compare.png)

The transcription, decipherment and translation of this card, and its closing steps, were done by Claude Opus 5.5. The family key comes from earlier cards, whose work is by the OpenAI GPT solver and Claude Opus 5.5.

## Sources

- HC Portal record 1305, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1305 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3975/conversions/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_pic-large.jpg, and the original https://api.hcportal.eu/media/3975/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_pic.jpg
- Address side: https://api.hcportal.eu/media/3976/conversions/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr-large.jpg, and the original https://api.hcportal.eu/media/3976/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr.jpg
- Family key: ciphers/hcp-1216/SOLUTION.md and ciphers/hcp-1216/work/graphic-key.json in this repository.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
