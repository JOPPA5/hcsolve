# HCP 1251 (cpc_1914-04-12_HU__HU_Jasz Arokszalas_jolanka-52): Feri to Jolánka Tóth, Easter Sunday 1914

Human solver: Tomáš Pavuk

**Status: complete reading, with signs under the postmark and in the washed-out stamp box restored and marked. Independent review 1 verdict REVISE; all nine findings addressed, and the sense of the letter did not change.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1251 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1251), portal name cpc_1914-04-12_HU__HU_Jasz Arokszalas_jolanka-52, from Tobias Schrödel's collection of cryptographic postcards (private collection; related publication: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card turned up.

It is a picture postcard. The picture side has only a printed verse (Csendes álmok éjjelén…) and no cipher. The address side is in plain writing: **Szép reményű Tóth Jolánka úrleánynak, Jászárokszállás** ("To the fair and promising Miss Jolánka Tóth, Jászárokszállás"; a Hungarian town in the Jász region). It is cancelled BUDAPEST 914 APR 12, and 12 April 1914 was Easter Sunday.

The cipher is all on the address side: 25 rows in the left half, rows 26–28 across the full width along the bottom edge, and seven rows in the stamp box, uncovered when the stamp was soaked off.

The card belongs to the family of cipher postcards to Jolánka Tóth, many of them from a suitor named Feri, deciphered in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243, 1263, 1272, 1301).

![Address side with the cipher, the cancellation and the stamp box (source/address-large.jpg)](../source/address-large.jpg)

![Picture side with the printed verse, no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The key was transferred from the sister cards, mainly HCP 1216 (whose key work was started by OpenAI GPT and completed by Claude Opus 5.5); it was not recovered blind from this card. The transcription is **manual**: Claude Opus 5.5 read the un-converted original scan sign by sign on enlarged crops, and the reading was not blind to the family's vocabulary. Rows slope upward to the right by up to about 45 pixels, so the first per-row crops mixed neighbouring rows; continuous tiles fixed the row order.

The first anchors were köszönöm szépen édesem and kellemesebb és boldogabb lesz, then húsvéti ünnepeket. The long-legged peak was then identified as v (levelére, kívánok). Two early dead ends were resolved by re-dividing the words: olon kátolde is Ilonkától / de most, and the opaque stamp row tenve is [Is]ten ve|le.

The result is 770 signs recorded in `work/ledger.txt`, one character per written sign. The ledger is written directly in plaintext letters. The repository's reproduction command (below) therefore validates and prints this transcription; it does not apply a key to shape data.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs. Labels are descriptions of the handwritten shapes.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| two bars | a | three bars | e | six | b |
| opposed bowls | cs | stroke + tick, or crossing "4" | d | upright or tilted cross | f |
| hooked S with descender | g | tall stroke + tick at upper right | h or p | crossed loop, dot | i |
| inverted T | j | section-mark S | k | wave or chevron | l |
| three short strokes | m | two short strokes | n | cursive loop | o |
| F-like | r | right bowl | s | gamma | t |
| plain cross | u | peak with long left leg | v | low loop with descender | y |
| crossed diagonal with long arm | z | | | | |

Variants on this card: l is sometimes a plain chevron without its hook (lapot, levelére); g has a large S form (boldo|gok, row 22) and a large double-looped form (drágám, row 16); k once appears as a closed 8 (megkaptam); i is often written without its dot and then looks like o; gy is written as g + y; accents on ö, ü, ő and ó are marks added to the base sign. The h/p sign is one sign for two letters, and each case is resolved by the word.

## Plaintext

Literal decipherment. `h` stands for the h/p sign, `[ ]` for a restored sign, `{ }` for a doubtful one.

```text
01 szeretetedesjolankambe
02 csessoraitmegkahtammelyet
03 köszönömszehenedesem
04 enküldtemmaganakegylahot
05 multlevelerejaszberenybe
06 m[a]jdmegfogjakahniilon
07 katoldemostsietekvala
08 szolnijelensorairaminde
09 ne[k]elotkivanokkellemhusv{o}
10 tiünneheketremelemajöhu[s]vet
11 kelemesebesboldogableszmint
12 amostaniigazavanedesemhogy
13 aszülőnekmindentsz[a]badcsak
14 nemillikestudomhogyaz
15 atervehogyszetvalasszonben
16 nünketugyedragamaznemfog
17 nekisikerülnimertnincsaza
18 hatalomamielvaszonegymas
19 tolcsakahalaldeezthagyjuk
20 utoljaraedesembarmijen
21 szegenyekleszünkisdeboldo
22 gokesnekemnemkelsemmimas
23 nemad[o]msemenyivagyon
24 ermagatmertavagyonazel
25 fogydemagaedesmegmarad
26 kösznömmaganakedesemhogyanyiraönfelaldozódere
27 melemhogyerrenemleszszükségemmertmindigfogokanyi[t]
28 keresnihogyszenyenegycsaladoteltartsakcsakez

Stamp box:
S1 [is]tenve
S2 {e}ledese[m]
S3 aboldog
S4 viszont
S5 latasra
S6 imado[ja]
S7 fer[i]
```

Normalized Hungarian (word division, accents and spelling are editorial):

**Szeretett édes Jolánkám! Becses sorait megkaptam, melyet köszönöm szépen, édesem. Én küldtem magának egy lapot múlt levelére Jászberénybe, majd meg fogja kapni Ilonkától. De most sietek válaszolni jelen soraira. Mindenek előt[t] kívánok kellem[es] húsvéti ünnepeket. Remélem, a jö[vő] húsvét kellemesebb és boldogabb lesz, mint a mostani. Igaza van, édesem, hogy a szülőnek mindent szabad, csak nem illik, és tudom, hogy az a terve, hogy szétválasszon bennünket. Ugye, drágám, az nem fog neki sikerülni, mert nincs az a hatalom, ami elválasszon egymástól, csak a halál. De ezt hagyjuk utoljára. Édesem, bármilyen szegények leszünk is, de boldogok, és nekem nem kell semmi más. Nem adom semennyi vagyonér[t] magát, mert a vagyon az elfogy, de maga, édes[em], megmarad. Köszönöm magának, édesem, hogy annyira önfeláldozó, de remélem, hogy erre nem lesz szükségem, mert mindig fogok annyit keresni, hogy sze[ré]nyen egy családot eltartsak. Csak ez.**

**Isten vele, édesem, a boldog viszontlátásra! Imádó[ja] Feri.**

English translation:

**My beloved sweet Jolánka! I have received your esteemed lines, for which I thank you very much, my sweet. I sent you a card to Jászberény in reply to your last letter; you will get it from Ilonka. But now I hasten to answer your present lines. First of all I wish you a pleasant Easter. I hope next Easter will be more pleasant and happier than this one. You are right, my sweet, that a parent may do anything, it is just not proper, and I know that the plan is to part us. Surely, my darling, that will not succeed, because there is no power that could part us from each other, except death. But let us leave this for last. My sweet, however poor we may be, we shall still be happy, and I need nothing else. I would not give you up for any amount of wealth, because wealth runs out, but you, my sweet, remain. I thank you, my sweet, for being so self-sacrificing, but I hope I shall not need that, because I shall always earn enough to keep a family modestly. That is all.**

**God be with you, my sweet, until our happy reunion! Your adorer, Feri.**

Slovak translation:

**Moja milovaná, sladká Jolánka! Vaše vážené riadky som dostal, za čo veľmi pekne ďakujem, zlatko. Poslal som Vám do Jászberénya lístok ako odpoveď na Váš minulý list; dostanete ho od Ilonky. Ale teraz sa ponáhľam odpovedať na Vaše terajšie riadky. Predovšetkým Vám želám príjemnú Veľkú noc. Dúfam, že budúca Veľká noc bude príjemnejšia a šťastnejšia ako táto. Máte pravdu, zlatko, že rodič môže všetko, len sa to nepatrí, a viem, že plánom je rozdeliť nás. Však, drahá, to sa nepodarí, lebo niet takej moci, ktorá by nás od seba rozdelila, len smrť. Ale to nechajme nakoniec. Zlatko, nech budeme akokoľvek chudobní, predsa budeme šťastní a ja nepotrebujem nič iné. Nedám Vás za žiadne bohatstvo, lebo bohatstvo sa minie, ale Vy, zlatko, zostanete. Ďakujem Vám, zlatko, že ste taká obetavá, ale dúfam, že to nebude potrebné, lebo vždy zarobím toľko, aby som skromne uživil rodinu. Len toľko.**

**S Bohom, zlatko, do šťastného zhľadania! Váš ctiteľ, Feri.**

Notes on the reading:

- **The writer's spelling.** The normalization supplies long accents, which are mostly unmarked, and corrects szeretet (szeretett), előt (előtt), kellem (kellemes), kelemeseb, boldogab, elvászon (elválasszon), kel (kell), bármijen (bármilyen), semenyi, vagyonér (vagyonért), kösznöm (köszönöm), anyira, anyit.
- **Jászberény.** The word can attach to küldtem or to levelére. The translations attach it to küldtem (the card went to Jászberény), which suits "you will get it from Ilonka". The Hungarian allows both.
- **Ilonka** is named as the addressee's cousin on the sister card HCP 1272.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1251/work/decode.py
```

The script checks the SHA-256 of both source images and both originals, reads `work/ledger.txt`, checks that every character is a sign class listed in `work/key.json`, prints the 28 rows and the stamp box, reports 770 signs, and prints the normalized text. It does not read the image and it applies no key: the transcription step is manual, and it was checked in review as described below.

## Uncertainties

**Readings that rest on word sense**

- **Two bars against three (a/e).** The third bar is often missing or lost. Word sense decides at least de (row 7), sietek, igaza, a vagyon (row 24, crossed by a water run), de maga, magának (row 26) and the first vowel of szét (row 15), which is two bars on the card. bármijen (row 20) is two bars and a small dot below.
- **Rows 2, 7 and 15, F against gamma.** kaptam has a heavy sign close to r; sietek has a gamma touched by cancel specks; terve begins with an F-like form with a small foot. All three are read t from sense.
- **The h/p sign** is resolved by the word: kaptam, szépen, lapot, kapni, ünnepeket are p; húsvét, hogy, hatalom, halál, hagyjuk are h.
- **Dropped dot on i** (Ilonka, mostani, nem illik, annyira, sietek): i against o is decided by sense.
- **Row 10.** In ünnepeket the fourth of four strokes carries a horizontal top bar, so nn rests on sense. In jö the accent is a dot plus a longer tick and may be ő; a jő húsvét would need no omitted -vő.
- **Row 28, sze[ré]nyen.** The signs are clearly s z e n y e n. Szerényen ("modestly") assumes ré was omitted; szegényen ("poorly") fits equally well and differs little in sense.

**Restorations (signs hidden or only traces seen)**

- Row 6 m[a]jd: under the cancel ring; green traces of two bars show.
- Row 9 ne[k]e-: under the ring; traces only, shape not visible.
- Row 9 end húsv{o}: a loop with a long arm where é is expected; húsvéti from sense, possibly a mis-stroke.
- Row 10 hu[s]vet: under the postmark; a right bowl shows, so a weak reading supported by sense.
- Row 13 sz[a]bad: a correction with two overwritten blocks (z with bars struck over it, then a box of strokes). Which strokes are the intended a cannot be determined; the word is safe from sense and the following six = b.
- Row 23 nemad[o]m: the o is a smeared blot; nem adom is the only sense found and fits the next clause exactly.
- Row 25 édes[em]: the literal édes could stand as written; the restoration is optional.
- Row 27 anyi[t]: cut by the card's edge; stem and start of the top bar show.
- **Stamp box.** The ink is washed out. [is] in S1 lies under a stamp fragment and is restored from the family's formula Isten vele (HCP 1216, 1217). In S2 the l is blurred and a final m would lie at the torn edge. The normalized vele, édesem is compressed: S1 ends `ve`, S2 reads `{e} l e d e s e [m]`, so {e} is dropped as a stray and one e serves both vele and édesem. S3 boldog after the b and S5 ra are faint. In S6 -ja is not visible, and in S7 the i of feri is lost.
- Ink spills near önfeláldozó (row 26) and in remélem (row 27) are treated as no sign.

**Other limits.** The key was transferred, not recovered from this card. The writer is known only as Feri; his and Ilonka's civil identities are not established. The search for prior publication went no further than the portal page and the AI Decipherment Register, which had no record of this card on 2026-11-01.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, read all 28 rows and the stamp box on its own 2–4× crops of the original, and decoded its own sign-class transcription of rows 1, 4, 5, 12, 15, 18, 20, 26 (first part) and 28 with HCP 1216's key rather than this card's. Rows 1, 5, 12, 18 and 28 agreed exactly; the other rows produced the differences below. It judged the text natural early-20th-century Hungarian. It confirmed the restorations in rows 6, 9, 23, 24 and 27 and the signs of row 28, and found no sign of a published solution being used.

What changed:

- **Row 4.** The handed-in reading lapo[t] be was wrong. A gamma stands after the o and runs under the postmark (separated by colour on the crop below), and the supposed b e are not on the card. It now reads lapot, which is plain grammatical Hungarian.
- **Row 26.** An invented second k had produced ked[v]esem. The card has one k, so magának, édesem; the translations now say "my sweet" and "zlatko".
- **Rows 15 and 20.** Two "writer's spellings" were vowel choices against the pixels. Both are now a, and the false spelling notes are gone.
- **Key.** The claim that the g sign also stands for final k was withdrawn: those finals are ordinary k.
- **Disclosure.** The row 13 correction, the stamp compression, the nn, jö/jő, hu[s]vet and édes[em] points and the plain statement about the reproduction command were added, and the repeated-word counts were corrected.

One change came from the solver afterwards: the translations now attach Jászberénybe to küldtem. No letter changed for that.

These fixes altered four rows of the ledger (rows 4, 15, 20 and 26) and did not change the sense of the letter, so no second round was run. The reviewer could not verify the signs hidden under the stamp remnant ([is], final m of S2, -ja, i of S7), the k of row 9, or the intended letter in the row 13 correction.

![Row 4 end, green cipher ink separated from black postmark ink: h/p stroke, o, then the gamma t (review/work/c/l4m.png)](../review/work/c/l4m.png)

## Sources

- HC Portal record 1251, General, Description and Attachments tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1251 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/3814/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_adr.jpg (original) and its conversion (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/3813/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_pic.jpg (original) and its conversion (source/picture-large.jpg).
- Family key: ciphers/hcp-1216 in this repository, with sister cards HCP 1212, 1213, 1217, 1218, 1243, 1263, 1272, 1301.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-01.
