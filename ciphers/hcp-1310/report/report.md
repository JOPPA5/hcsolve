# HCP 1310 (cpc_1912-07-03_HU__HU_Jasz Arokszalas_jolanka-28): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: whole message read (all 21 main rows, the 6 rows under the stamp and the line below the address; 374 signs); one word, *Darasztin*, is not identified as a place. Independent review 1 verdict REVISE; two signs and one normalized word corrected.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1310 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1310), portal name cpc_1912-07-03_HU__HU_Jasz Arokszalas_jolanka-28, part of Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, date 1912-07-03, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. This report settles the language: it is Hungarian.

The picture side is a printed song card, *Hej cigány hallod-e?* (publisher number 3077/78), with no cipher text. Everything enciphered is on the address side, in red ink: 21 rows on the left, six short rows under the stamp, and one line below the address.

The address and dateline are in plain writing: *Szép reményű Tóth Jolánka úrleánynak, Jász Árokszálás* and *Kelt Gyöngyös 1912 Júl. 1 reggel* ("Written at Gyöngyös, 1 July 1912, in the morning"). The dateline agrees with the postmarks, which show July 1 and a Jászárokszállás mark reading Jul 3. The writer signs himself Feri. He is the sender of many cards to Jolánka in this cipher, several of them finished in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301, 1305).

Other marks, none of them cipher: a small red number in the bottom right corner, perhaps 7/27 (uncertain), and a faint pencil note under the postmark. The note starts *sziv...*, has a capital J-like form and ends *...ák hoz*; *Szívem Jolánkához* ("to my heart's Jolánka") is a hypothesis and nothing depends on it.

![Picture side, printed song card with no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: 21 cipher rows at the left, the stamp block at the top right, the plain red address and dateline (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is manual. No OCR was used and the portal supplied none. Every sign was read by eye on enlarged crops of the un-converted original scan and recorded as one token in a ledger; a short script decodes the ledger.

The card was read with a **known, transferred key**; this is not a new key recovery. The key comes from the finished Jolánka cards, chiefly HCP 1216. That key was first transferred by the OpenAI GPT solver and completed by Claude Opus 5.5. On this card, the reading, ledger and interpretation are by Claude Opus 5.5; no earlier work on this number exists. The key applied without change and no sign fell outside it.

The first attempt misread the chevron as d, which blocked the first row. Once d was recognised as short + tall stroke, h as tall + short, and the chevron as v, the opening *kedves egyetlen reményem* appeared and the remaining rows followed. Rotating the stamp block by 180 degrees was also tried and was wrong: the block is upright.

## Key

Simple monoalphabetic substitution with invented graphic signs, written continuously. The names are conventional labels for handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S, 8, 5 forms) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma | t |
| short stroke left + tall right | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke left + short right | h (near-homograph of p; no p occurs here) | hooked descender | y |
| open loop with descender | g | crossed curve, usually dotted | i | crossed diagonal with tail | z |
| that loop + hooked descender | gy | inverted T | j | | |

Marks over a sign are accents: double dots give ö and ű. Acutes are not transcribed in the ledger.

## Plaintext

Literal decipherment, row by row, as written (the writer's slips are kept):

```text
01 kedvesegyetlenre      12 ennemtalakoztam
02 menyemtudatomhogy     13 meolyaneberekel
03 szerencsesenmegerkez  14 sehalaistennekezel
04 temazutbantalalkoz    15 bezaromsoraim
05 tamegykocsivalame     16 mertmarkevesaid
06 lyiketmegtamad        17 jomulataskivanok
07 takahogyvisznek       18 darasztinistenve
08 felölbejotekarok      19 edesematavolbol
09 szalasbanmegrais      20 imadokadvasseferi
10 lovödöztekdene        21 tiszteleakedvasmamat
11 kiisvoltfegyvere

Under the stamp: csokja / idra / szom / jazok / hükadve / sedferi
Below the address: szeretetel
```

Normalized Hungarian (word division, most accents and the bracketed letters are editorial):

**Kedves egyetlen reményem! Tudatom, hogy szerencsésen megérkeztem. Az útban találkoztam egy kocsival, amelyiket megtámadtak, ahogy Visznek felől bejöttek Árokszállásban, még rá is lövö[l]döztek, de neki is volt fegyvere. Én nem találkoztam mé[g] olyan e[m]berekkel se, hála Istennek. Ezzel bezárom soraim, mert már kevés a[z] id[ő]. Jó mulatás[t] kívánok Darasztin[?]. Isten ve[l]ed, édesem, a távolból imádó kedvese Feri. Tisztele[m] a kedves mamát.**

**Under the stamp:** Csókjaidra szomjazok. Hű kedvesed Feri.

**Below the address:** szeretettel.

English translation: **My dear only hope! I inform you that I have arrived safely. On the way I met a carriage that had been attacked: as they came in from the direction of Visznek at Árokszállás, they even fired at him, but he had a weapon too. Thank God, I have not yet met such people myself. With this I close my lines, for time is now short. I wish you a good time at Darasztin[?]. God be with you, my sweet; from afar, your adoring sweetheart Feri. I respect the dear mother.**

Under the stamp: I thirst for your kisses. Your faithful sweetheart Feri. Below the address: with love.

Slovak translation: **Moja drahá, jediná nádej! Oznamujem, že som šťastne dorazil. Na ceste som stretol koč, ktorý prepadli: keď prichádzali od Visznek v Árokszállási, ešte aj naň strieľali, ale aj on mal zbraň. Ja som sa, chvalabohu, s takými ľuďmi ešte nestretol. Tým končím svoje riadky, lebo už je málo času. Želám dobrú zábavu v Daraszti[?]. S Bohom, moja milá; z diaľky ťa zbožňujúci milý Feri. Úctivo pozdravujem drahú mamu.**

Pod známkou: Túžim po tvojich bozkoch. Tvoj verný milý Feri. Pod adresou: s láskou.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1310/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 of both source scans and both un-converted originals, decodes the manual ledger `work/ledger.txt` with the key, and prints the literal rows and the normalized text. It does not read the image: the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **Row 18, *Darasztin*.** Every sign is read, but the word is not identified. It has a parallel on HCP 1305, row 5, `mulatharasztin` (*Hogy mulat ...?*, "how are you amusing yourself ...?"): the same eight letters after the first sign, in the same *mulat-* context. It is probably one place or jocular name. The first signs differ: d here, h/p on HCP 1305. These are the same two strokes in opposite order, so one card may contain a slip. *Darasztin* / *Harasztin* ("at Haraszt[i]") is a hypothesis; such a place could not be confirmed.
- **Word-sense calls.** These signs are decided by the word, not by shape alone:
  - the h of *hű* (stamp row 5), where only one thick stroke is visible;
  - the t of *volt* (row 11), with a doubled stroke that leans towards r;
  - the t of *távolból* (row 19), crossed by the following a;
  - the sixth sign of *szeretetel*, blotted and closer to r;
  - the d of *kedvesed* (stamp row 6), with a faded right stroke.
- **Row 7, third sign.** A 5-like section mark, read k on shape: *megtámadtak, ahogy*. The alternative s gives *megtámadta, s ahogy* and the same story.
- **Writer's spellings.** He drops letters and sometimes writes two bars for three. Normalized: *jotek* to jöttek, *talakoztam* to találkoztam, *lovödöztek* to lövöldöztek, *a id* to az idő, *mulatas* to mulatást, *tiszteleakedvas* to tisztelem a kedves, *kadvasse* to kedvese, *szalasban* to Árokszállásban (the card has *szálás* in the plain address too). *Isten ve|edesem* rests on word sense: the writer lost `l` and one `ed`. The dropped m of *tisztelem* is an interpretation, not a hidden sign; a pink blot in row 21 lies under a sign that is still a wave.
- **The formal *kedvese*** in row 20 sits beside informal *veled* and *kedvesed*; it is kept as written.
- **The events** are the writer's report and could not be checked. "Him" comes from *neki*, which has no gender in Hungarian. Visznek is a village near Gyöngyös and Jászárokszállás; its exact position relative to the two towns was not checked against a map.
- **The corner mark** and the middle of the pencil note remain uncertain.
- **Prior work.** No published solution was found or used: the portal shows Not solved with nothing attached, and the orchestrator found no record for this target in the AI Decipherment Register on 2026-10-30.

## Why the reading is believed correct

The unchanged family key turns every sign into Hungarian. The sense runs across row breaks (*megérkez|tem*, *ame|lyiket*, *ne|ki*), and the stamp rows join into *csókjaidra szomjazok*. Repeated words decode identically: *találkoz-* in rows 4 and 12, *Feri* twice, *kedve-* three times. The stock phrases *egyetlen reményem* and *a távolból* match sister cards, and the places fit the dateline and the address.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, wrote its own sign-by-sign reading of the 21 main rows (332 signs) in its own notation with the key rebuilt from HCP 1216, and read all rows, the stamp block and the address line on its own crops. Its reading differed from the solver's at exactly two signs and it could not refute the message. It confirmed that the stamp block is upright. The solver checked each finding on the crops and accepted all of them:

- **Row 13 (major).** The sign before the final l has three bars, so it is e, not a. The row reads `meolyaneberekel`. This was a misreading that had been explained as a spelling habit; the note was removed.
- **Row 18 (major).** The ninth sign is n, not h, because the short stroke stands low, unlike this card's h. The solver's claim that no sister card helps was false, and the HCP 1305 parallel is now recorded. The word was previously left untranslated; it now appears as a marked hypothesis.
- **Row 9 (minor).** A clear acute gives *még rá is*, not *meg rá is*.
- **Disclosure (minor).** The h of *hű* and the t of *volt* are now listed as word-sense calls.
- **Pencil note and status wording (minor).** Updated, and "between" for Visznek softened to "near".

The story and the key did not change.

## Sources

- HC Portal record 1310, all three tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1310 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3990/conversions/cpc_1912-07-03_HU__HU_Jasz-Arokszalas_jolanka-28_pic-large.jpg and the original at https://api.hcportal.eu/media/3990/cpc_1912-07-03_HU__HU_Jasz-Arokszalas_jolanka-28_pic.jpg
- Address side: https://api.hcportal.eu/media/3991/conversions/cpc_1912-07-03_HU__HU_Jasz-Arokszalas_jolanka-28_adr-large.jpg and the original at https://api.hcportal.eu/media/3991/cpc_1912-07-03_HU__HU_Jasz-Arokszalas_jolanka-28_adr.jpg
- Family key and parallels: ciphers/hcp-1216 and ciphers/hcp-1305 in this repository.
