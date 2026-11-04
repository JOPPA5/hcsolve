# HCP 1250: Feri to Jolánka Tóth, "you will be my partner"

Human solver: Tomáš Pavuk

**Status: deciphered in full (570 signs, of which 2 are restorations of hidden signs); small disclosed points only. Independent review 1 verdict ACCEPT, no sign value changed.** Report dated 2026-11-01. All reading by Claude Opus 5.5; there was no earlier work on this number.

## Origin and context

The cryptogram is record 1250 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1250), portal name cpc_1913-06-16_HU__HU_Jasz Arokszalas_jolanka-38, from Tobias Schrödel's collection of cryptographic postcards (private collection). At capture on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The collection is described in the HistoCrypt paper linked from the record (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166).

The date 1913-06-16 comes only from the file name; the cancellation is only partly legible.

The picture side has print only (Cigányprímás / Lári-Fári and a verse). It has no handwriting.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address is in plain writing: Szépremény[ű] Tóth Jolánka úrleánynak, Jász Árokszállás ("To the promising young lady Jolánka Tóth, Jászárokszállás"). The end of the first word runs into a pink smear; the sister cards HCP 1252 and 1253 have the full form. All the ciphertext is on this side: 24 rows on the left half, the last of which runs along the bottom edge to the right edge, and 8 upright rows in the stamp field, where the stamp is gone and the signs stand over the printed seal.

![Address side: 24 cipher rows at the left, 8 rows in the stamp field, plain address at the right (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the family of cipher postcards to Jolánka Tóth, several of which are finished in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243, 1252, 1301). The same address and signature recur. The sender signs as Feri, and on this card as her imádója ("adorer"); his full identity is not established.

## Method

This card was read with a **known, transferred key**, not a new key recovery. The key and sign classes come unchanged from HCP 1216. No plaintext of this card was available beforehand.

The transcription is manual, not OCR. The rows were cropped from the un-converted original scan of the address side, enlarged and enhanced (a green-channel image separates the ink from the orange seal), and read sign by sign into a ledger of 570 tokens, one per written sign (work/ledger.txt). A script decodes the ledger with the key; it does not read pixels. Rows slope upward to the right, and rows 4/5 and 12/13 were confused at first until the crops were aligned by x position. That correction also removed false readings (mohol nép in row 5, mester in row 17).

To reproduce, from the repository root:

```sh
python3 -I ciphers/hcp-1250/work/decode.py
```

It checks the SHA-256 of the four scans, decodes the ledger, and prints the literal rows and the normalized text.

## Key

**Cipher type: MASC + Steganography** (updated 2026-11-03). Simple monoalphabetic substitution with invented graphic signs; the labels are conventional names for handwritten shapes. The steganography is the stamp box: 8 rows of the message (Szép kedvesem, gondoljon néha rám. Viszo[n]tlátásra. Feri.) were written where the stamp would cover them. The stamp is now lifted. A new check of the stamp box on 2026-11-03 found only cipher signs there and agreed with the reading below.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark S or 8 | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| long stroke + tick | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short tick | h / p | y-sign | y |
| open loop | g | dotted crossed curve | i | tailed cross | z |
| inverted T | j | | | | |

Dots over o and u give ö and ü. On this card gy is two signs (open loop + y-sign), sz is s + z, and ly is written with j. The tall-and-short sign serves both h and p; they cannot be separated on the pixels, so that choice rests on word sense. Long-vowel accents are written only now and then: clear ticks stand over bars in row 12 (hatnánk), row 15 (enyém), row 22 and stamp row 4 (né-). Other accents are supplied in normalization.

## Plaintext

Literal decipherment, row by row. `[l]` and `[a]` are restorations; `{e/i}` is an overwritten vowel.

```text
01 edesegyetlenremenyemki         13 idömindenhetegyeszten
02 vanomhogyalegjobbegesseg       14 döesadigtartm{e/i}gaztnem
03 bentalaljasoraimmisajnos       15 mondhatomhogyenyem
04 ritkanvanmostanabajomu         16 vagyörökreesnemvalaszt
05 latastkivanoholnapdejolmu      17 elegymesto[l]semidesaj
06 latgondoljonraismertnel        18 nosmegsokaleszdebez
07 külöznömkelajomulatast         19 unkazistenbenzttertom
08 maganelkülnemtudokmulat        20 mintazenekmondjahogy
09 sagotszereznicsakazfajmert     21 megerjükmeaztazidöt
10 nincsegykicsitkozelebhozam     22 babamteleszelaparom
11 hogygyakrabbantalkoz           23 amitenaligaligvarom
12 hatnanknekemojhoszuaz          24 istenveleedescsokoljaimadojaferi
```

Stamp field: `szepkad vesem gondol jonne h[a]ram viszot latasra feri`

**Hungarian (normalized; word division, accents and punctuation are editorial, square brackets mark letters not on the card):**

Édes egyetlen reményem! Kívánom, hogy a legjobb egésségben találja soraim. Mi sajnos ritkán van mostanába[n]. Jó mulatást kívánó[k] holnap; de jól mulat, gondoljon rá[m] is, mert nélkülöznöm kel[l] a jó mulatást maga nélkül. Nem tudok mulatságot szerezni, csak az fáj, mert nincs egy kicsit közelebb hozzám, hogy gyakrabban találkozhatnánk. Nekem oly hosszú az idő, minden hét egy esztendő, és addig tart, míg azt nem mondhatom, hogy enyém vagy örökre, és nem választ el egymástól semmi, de sajnos még soká lesz, de bízunk az Istenben, [a]zt tartom, mint az ének mondja, hogy megérjük mé[g] azt az időt, babám, te leszel a párom, amit én alig, alig várom. Isten vele, édes. Csókolja imádója, Feri.

Stamp field: Szép kedvesem, gondoljon néha rám. Viszo[n]tlátásra. Feri.

**English:**

My sweet only hope! I wish that my lines find you in the best of health. Which, unfortunately, is rare lately. I wish you a good time tomorrow; but when you are having a good time, think of me too, because I must do without a good time, without you. I cannot find any amusement; only this hurts, that you are not a little closer to me, so that we could meet more often. For me the time is so long, every week a year, and it will last until I can say that you are mine forever and nothing separates us from each other. But unfortunately that will be long yet; but we trust in God, I hold, as the song says, that we shall yet live to see that time, my darling, when you will be my partner, which I can hardly, hardly wait for. Farewell, sweet one. Your adorer Feri kisses you.

Stamp field: My beautiful darling, think of me sometimes. Until we meet again. Feri.

**Slovak:**

Moja sladká jediná nádej! Želám si, aby Vás moje riadky našli v najlepšom zdraví. Čo je, žiaľ, teraz zriedkavé. Želám Vám zajtra dobrú zábavu; ale keď sa budete dobre zabávať, myslite aj na mňa, lebo ja sa musím zaobísť bez dobrej zábavy, bez Vás. Neviem si nájsť zábavu, bolí ma len to, že nie ste trochu bližšie ku mne, aby sme sa mohli stretávať častejšie. Mne je čas taký dlhý, každý týždeň je ako rok, a potrvá to dovtedy, kým nebudem môcť povedať, že si navždy moja a že nás od seba nič neoddelí. Ale žiaľ, to bude ešte dlho trvať; no dúfame v Boha, ja si myslím, ako hovorí pieseň, že sa ešte dožijeme toho času, moja milá, keď budeš mojou družkou, čoho sa sotva, sotva dočkám. S Bohom, drahá. Bozkáva Vás Váš ctiteľ Feri.

Pole známky: Moja krásna drahá, myslite na mňa niekedy. Dovidenia. Feri.

## Uncertainties

Restorations of hidden signs (two):

- **Row 17, the l of egymástól.** The sign lies under a heavy ink blot with about three legs joined at the top. The pixels cannot choose between a wave and three strokes; the l rests on the word (nem választ el egymástól semmi).
- **Stamp row 5, the a of ha.** It falls on the printed seal and shows only as faint pink bars. Restored from néha rám.

Calls that rest on word sense:

- **h/p:** p in holnap, párom, szép; h elsewhere. Before the p of párom (row 22) stands a separate wedge-shaped blob, a blot or a cancelled sign, unexplained and not counted as a sign.
- **Row 14 vowel of míg:** three bars with a long crossing stroke, apparently a correction. Addig tart, míg… requires "until".
- **d/n:** in mondhatom, mondja, gondoljon, minden the d has a short first stroke, close to n. The word settles each.
- **Row 18–19 `bez|unk`:** three bars (e) after the b, normalized bízunk. No other word fits …az Istenben.
- **Row 19, the s of Istenben:** hollow, abraded top; it reads as a right bowl only with some allowance.
- **Row 24 imádója:** the i looks more like a dotted loop. **Row 23 amit:** the t is rounded and hooked.
- **Row 2 and row 7:** the m of kívánom and nélkülöznöm has one short extra stroke, which no word uses.
- **Stamp row 1, the vowel after k:** smudged. It is tokenized as a but cannot be told from e, so kadvesem may be a writer's error or just a smudged kedvesem. The word stands either way.

Editorial readings:

- **Row 6 `rais`:** normalized rá[m] is ("of me too"), taking the m as one more dropped letter, because mert then keeps its usual sense and the stamp field has gondoljon néha rám. The literal rá is ("of this too, that…") is the alternative. The signs are the same.
- **Row 5 `kivano`:** kívánó[k]; kívánom with the m dropped gives the same sense.
- **Rows 3–4, "Mi sajnos ritkán van mostanába[n]"** can attach to the health wish or stand alone. The sentence division there is editorial, though a short oblique stroke before jó in row 4 is probably a comma and supports a break. De jól mulat as "but when you are having a good time" is an interpretation.
- **Letters not on the card:** [a]zt (row 19), mé[g] (row 21), viszo[n]t (stamp), kel[l], mostanába[n] (colloquial -ba for -ban is also possible).
- **Writer's spellings normalized:** közeleb, hozam (hozzám), talkozhatnank (találkozhatnánk, ál omitted across rows 11–12), ojhoszu (oly hosszú), adig, mest- (mást-), semi, tertom (tartom), enek.
- The letter mixes formal address (találja, gondoljon) with te leszel a párom inside the reported song line. It is kept as written. The song is not identified.
- The Hungarian judgement is an AI's, not a native speaker's.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, read all 24 main rows and all 8 stamp rows from its own crops into its own transcription, decoded that with its own key table written from the HCP 1216 sign list, and compared it with the ledger: 570 signs, no row differing, after treating h/p as one sign and leaving the three unreadable signs as unknown. That reading was made after seeing the ledger, so it was a check against the pixels and not a blind reading. It found eight minor findings and no blockers. All were accepted:

- **Row 6:** the normalized text changed from rá is to rá[m] is, with English and Slovak changed to match; the old reading stays as the alternative.
- **Row 4:** mostanában now shows its missing n in brackets, and the oblique stroke is disclosed.
- **Row 17:** the claim that only a wave fits the blot was withdrawn.
- **Stamp row 1:** the vowel after k is now marked uncertain, not a sure writer's error.
- **Row 22 and row 19:** the wedge before the p and the damaged s are now disclosed.
- **Accents:** the statement was softened and the clear ticks are named.
- **Translations:** "with us" and "u nás" were removed, and the Slovak of alig várom was corrected.

No sign value and no ledger token changed.

## Sources

- HC Portal record 1250, General, Description and Attachments tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1250 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3810/conversions/cpc_1913-06-16_HU__HU_Jasz-Arokszalas_jolanka-38_pic-large.jpg, original in work/hires/.
- Address side: https://api.hcportal.eu/media/3811/conversions/cpc_1913-06-16_HU__HU_Jasz-Arokszalas_jolanka-38_adr-large.jpg, original in work/hires/.
- Family key: ciphers/hcp-1216 in this repository.
- No published solution of this card was found.
