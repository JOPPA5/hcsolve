# HCP 1285 (cpc_1912-01-14_HU__HU_Jasz Arokszalas_jolanka-02): a love card to Jolánka Tóth, January 1912

Human solver: Tomáš Pavuk

**Status: every written sign is read and the main message is complete; the last eight signs (the closing) are read letter by letter, but their expansion is conjecture. Independent review 1 verdict ACCEPT; no sign value changed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1285 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1285), portal name cpc_1912-01-14_HU__HU_Jasz Arokszalas_jolanka-02, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date 1912-01-14, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side shows an embracing couple with falling leaves and a printed four-line verse that begins Hulló falevél ("Falling leaf") and ends Szerelemről boldogságról ("of love, of happiness"). It carries no cipher.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address side is partly in plain writing: Szépremény[ű?] Tóth Jolánka kisasszonynak szeretettel, Jász-Árokszállás ("to Miss Jolánka Tóth, of fair promise, with love"), then a heavily struck-out start and al szög, probably the town quarter Alszög. Szépremény lies across the postmark and is followed by a pink smear; sister cards have Szépreményű, so its end may have been wiped. The postmark reads JÁSZÁROKSZÁLLÁS 912 JAN 14, which agrees with the portal date. A second postmark is only partly legible.

The message fills the left part of the address side in red invented signs. To read it, turn the card 90° clockwise: there are eleven rows, the last one short and squeezed into the corner. Three more rows stand in the stamp box, in the upright position of the card.

![Address side as captured, upright: the cipher rows at the left run sideways, three rows stand in the stamp box (review/work/upright.png)](../review/work/upright.png)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth at Jászárokszállás, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1294, 1301). Sister cards are signed Feri in plain writing; this one has no sender name. It was read with a **known, transferred key**, not by a new key recovery.

## Method

There was no earlier work on this number. The family key was taken unchanged from the legend of HCP 1216, whose earlier work was done by an OpenAI GPT solver and completed by Claude Opus 5.5.

- **Solving (2026-10-30), Claude Opus 5.5:** the hires address scan was rotated and every row read on enlarged crops, one token per written sign, in a sign ledger (`work/ledger.txt`). The ledger is manual, not OCR, and not blind: the key was known and word sense helped. No published solution was found or used.
- **Review (2026-10-30), a separate Claude Opus 5.5 agent:** re-ran the command, wrote its own transcription and key dictionary and compared them with the ledger (0 of 14 rows differ, 219 letters), and looked at every row on contact sheets and at the contested places at 3–6×. This check was not blind either, since the reviewer had read the ledger first.

The ledger holds 219 letters, two small inserted n's and two blots. The inserted n's are two small strokes which the writer seems to have added for a forgotten letter.

## Key

Hungarian simple monoalphabetic substitution with invented signs. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma | t |
| long + short stroke (short at left) | d | two short strokes; joined tail with two arches after a loop | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall + tick at upper right | h | low descender | y |
| open loop | g | tall + tick at lower right | p | crossed diagonal with hook | z |
| dotted crossed curve | i | inverted T | j | joined loop + descender | gy |

Dots over o and u give ö and ü. A left and a right bowl side by side give cs. On this card the tick position separates h from p: high in hogy, látható; low in kaptam, képen.

## Plaintext

Literal decipherment, row by row. `^n` is an n written small above the row, `{blot}` a solid blot with no value claimed. Row breaks are the writer's and fall inside words.

```text
01 kedvesédesjola^nkamb.sora      07 szontlatasrviszo^ntkiva
02 itmegkaptamme{blot}lynekna     08 nokilyenboldogsagot
03 gyonörülök.éskeremazis         09 kivanokminteképenlatha
04 renrhogyezrozsasokaig          10 toistenveleédesemhon
05 ny{blot}iljonszamomra.amien    11 esf
06 gemilletaligvaromavi           box: cso / kol / iahf
```

Normalized Hungarian (accents and punctuation editorial):

**Kedves édes Jolánkám! B[ecses] sorait megkaptam, melynek nagyon örülök, és kérem az Istent, hogy ez rózsa sokáig nyíljon számomra. Ami engem illet, alig várom a viszontlátást. Viszont kívánok ilyen boldogságot [kívánok], mint e képen látható. Isten vele, édesem. Hőn(?) és f[orrón](?) [stamp box:] csókolja, h f(?) or 14(?)**

English translation: **Dear sweet Jolánka! I have received your esteemed lines, which make me very glad, and I pray to God that this rose may bloom for me for a long time. As for me, I can hardly wait to see you again. In return I wish you such happiness as can be seen on this picture. God be with you, my darling. Ardently(?) and [hotly](?) [stamp box:] kisses you, h f(?) or 14(?)**

Slovak translation: **Milá sladká Jolánka! Vaše vážené riadky som dostal a veľmi sa z nich teším a prosím Boha, aby táto ruža dlho kvitla pre mňa. Čo sa mňa týka, sotva sa môžem dočkať nášho stretnutia. Na oplátku Vám želám také šťastie, aké vidno na tomto obrázku. S Bohom, drahá moja. Vrúcne(?) a [horúco](?) [rámček pre známku:] bozkáva Vás, h f(?) alebo 14(?)**

Notes on the reading:

- Ami engem illet ("as for me"), Becses sorait ("your esteemed lines"), Isten vele ("God be with you") and csókolja ("kisses you") are formulas of the family; formal third-person address is usual there too.
- Mint e képen látható ("as can be seen on this picture") points to the couple on the picture side, and the printed verse speaks of happiness: a check that does not depend on the cipher.
- Rózsa ("rose") stands without an article and may be a figure for the love or for Jolánka; the card does not say.
- Viszont may equally mean "however" in row 7.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1285/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of both source scans and both hires originals, decodes the manual sign ledger `work/ledger.txt` and prints the literal rows and `work/normalized.txt`. It does not read the image; the transcription step is manual.

## Uncertainties

- **The closing (rows 10–11 and the last box row): the main open point.** The letters are `hon esf` and `ia h f`. Hőn és f[orrón] csókolja ("ardently and hotly kisses you"), running from row 11 into the box, is a conjecture that supplies the verb rows 10–11 lack; it is not a reading. The o of `hon` has extra strokes and a blob: a correction or perhaps a double accent, which would favour hőn. Its tail has two arches like n, while the box tail after o has one wave like l, so `hol` is unlikely.
- **h f or 14.** The last two box signs read as h and f, but they also look like the digits 14, and the card is postmarked on the 14th. The stamp ring and ink bleed prevent a decision (see the crop below). No abbreviation dots stand there. A signature "h. F." (faithful Feri) is therefore only one option, and the card may have no signature at all.

![Stamp box enlarged: cso / kol / ia, then the two signs read h f, or the digits 14 (review/work/z_box.png)](../review/work/z_box.png)

- **Three r-shaped signs where t is needed.** Row 3–4 `is|renr` is read Istent and row 7 `viszontlátásr` is read viszontlátást. All three signs are ordinary F in form; a slip of the pen is a hypothesis about the writer. Istent is not in doubt. Row 7 may instead be the formula viszontlátásr[a] with a dropped a, though várom a viszontlátást is better grammar.
- **Inserted n.** Small double strokes stand at the head of the k of Jolánkám and just above the heavy t of the second viszont. Both are read as a missed n added afterwards. The second could be várnom in row 6, which makes worse sense.
- **Blots.** Rows 2 (me█lynek) and 5 (ny█íljon) have solid blots with no value claimed. In row 1 the a of Jolánkám has a square blot directly under its two bars, possibly a third bar (e); a rests on word sense. Blotted letters in rows 3, 7 and 8 are overwritten but their shape is seen, and word sense helped.
- **Row 10, first sign** (t of látható) is a heavily bled gamma with a spur, which may be bleed or the same r/t slip.
- **Repeated kívánok.** It is written in rows 7–8 and again in row 9; the normalization brackets the second.
- **`b.` in row 1** is written with a dot and expanded to b[ecses] as on HCP 1212 and 1294; the expansion is editorial.
- **z and i are close shapes**, and z is called by word sense in az, ez, rózsa. Row 10 Isten has no dot on its i. `ia` in the box stands for -ja.
- **Sender.** No name stands on the card. Feri comes only from the family and is not asserted here.
- No search for a prior publication of this card was made beyond the portal status (Not solved) and the AI Decipherment Register (no entry on 2026-10-30).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. It ran the command, compared its own transcription with the ledger with no difference in 14 rows, checked the pixels, and confirmed that the family key covers every sign and the text is idiomatic. It noted that this agreement was not blind. Its six findings were all minor and led to these changes:

- **Row 1:** the blot under the a is disclosed, and the position of the inserted n corrected.
- **Row 10:** the feathered first sign is disclosed.
- **Key:** the joined n is listed, and the claim that the row 10 and box tails are the same shape is withdrawn.
- **Closing:** the reading 14 is named as a rival to h f, dots are removed from the normalization, and rows 10–11 are joined to the box as one conjectural clause.
- **Row 7:** viszontlátásr[a] is listed as an alternative, and "gamma with an added bar" is no longer stated as seen.
- **Wording:** the row break látha|tó, the citations for b[ecses] and the possibly wiped end of Szépremény.

No sign value changed. The reviewer could not verify the expansion of the closing, the values of the blots, the second postmark or the sender.

## Sources

- HC Portal record 1285, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1285 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3915/conversions/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/3915/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_pic.jpg.
- Address side: https://api.hcportal.eu/media/3916/conversions/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/3916/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_adr.jpg.
- Family key: ciphers/hcp-1216 and its sister cards in this repository.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
