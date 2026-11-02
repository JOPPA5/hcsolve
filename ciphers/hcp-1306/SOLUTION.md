# HCP1306: Feri to Jolánka Tóth, a refused quarrel by postcard (PARTIAL)

**Status: PARTIAL after the revision of 2026-11-02. Almost the whole card now reads; one clause at the end of row 26 (*hát e bizatam el a ho*, printed as hate bizatamelaho) stays unread, so the card is not handed to review (no DONE1) and gets no register entry.** Claude Opus 5.5, 2026-10-30 and 2026-11-02. No earlier work on this number exists; the portal shows Not solved with no attached solution. No external plaintext was used.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented signs: the Jolánka postcard family, same key as finished cards hcp-1216, 1212, 1213, 1217, 1218, 1243, 1301. See the table in `ciphers/hcp-1216/SOLUTION.md` and the token legend at the head of `work/ledger.txt`. Variants on this card: k is an S-shaped section mark, usually with a base curl, g a flagged hook with no curl; a single stroke is a reduced d or h; dots of i often absent.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1306/work/decode.py
```

Checks the SHA-256 of the four images, decodes `work/ledger.txt` (about 640 signs, a manual reading, not OCR and not blind to the family key), prints the literal letters row by row, then the normalized text.

## Literal decipherment

Printed by the command (ledger revised 2026-11-02). {a|b} = shape between two classes.

```
01 szeretetedesjolankam              14 kormegyekmertmeg
02 mosthedigvalaszolok               15 akorsemhettemmokor
03 sorairairaojöromel                16 biztosnakondotam
04 ir{n|/}ekh{a|e}tlah{o|i}{t|r}isegysze   17 arakeremedesemhaigazan
05 re{h|d}enekehamarabkime           18 szerethagyjonfelaval
06 rülazirnivalommint                19 atolakodovetejtar
07 meganekedesemhamagamon            20 salm{i|o}tremelesmegistette
08 domtcsakszovala{k|g}armeg         21 esnemmeltattavalaszra
09 mon/aniamiojne/ezen               22 soraitamiabözsitileti
10 megymertnagyrabszol               23 igazansajnalomhogyenn{y|i}i
11 gavagyoknemrendel                 24 rejutovajobaratsagezt
12 kezemmagamfelettob                25 nemgondoltamamialitaszkilahjatiletiszeretnem
13 betnemiromhogymo                  26 latniesszeretnemenelinteznhatebizatamelaho
R1 /ezelbezaromsoraimmaradoko{k|6}   (inner right edge, reading upward)
R2 szeretikedveseferi                (outer right edge, reading upward)
S1-S7 ldo{g|?} / iszont / atasig / udvozli / szere / toked / veseferi   (stamp area)
```

## Hungarian (normalized; square brackets mark supplied letters or the unread clause)

Szeretett édes Jolánkám! Most pedig válaszolok soraira. Oly örömmel írnék hat lapot is egyszerre, de neke[m] hamarabb kimerül az írnivalóm, mint magának, édesem, ha magam mondom. Csak szóval akar[om] megmondani, ami oly nehezen megy, mert nagy rabszolga vagyok, nem rendelkezem magam felett. Többet nem írom, hogy mikor megyek, mert még akkor se m[e]hettem, mikor biztosna[k] [g]ondo[l]tam. Arra kérem, édesem, ha igazán szeret, hagyjon fel avval a tolakodó vetélytársal, mit remélek, és meg is tette, és nem méltatta válaszra sorait. Ami a Bözsit illeti, igazán sajnálom, hogy ennyire jut[ott] a jóbarátság, ezt nem gondoltam. Ami a Litaszki(?) lapját illeti, szeretném látni, és szeretném én elintézni, [hát e bizatam el a ho: UNREAD] szereti kedvese Feri. Ezzel bezárom soraim, maradok. Bo(?)ldo[g] viszont[l]átásig üdvözli szerető kedvese Feri.

## English

My beloved sweet Jolánka! Now then I answer your lines. With such joy would I write even six cards at once, but my matter for writing runs out sooner than yours, darling, if I say so myself. Only by word of mouth do I want to say what comes so hard, because I am a great slave, I have no command over myself. I will no longer write when I am going, because even then I could not go, when I thought it certain. I ask you, darling, if you truly love me, give up that intrusive rival, as I hope, and you have indeed done so, and did not deem his lines worth an answer. As for Bözsi, I am truly sorry that the good friendship has come to this; I did not expect that. As for Litaszki's(?) card, I would like to see it and I would like to settle it myself, [unread clause] loves you, your sweetheart Feri. With this I close my lines, I remain. Until a happy(?) reunion, greetings from your loving sweetheart Feri.

## Slovak

Moja milovaná sladká Jolánka! Nuž teda odpovedám na Vaše riadky. S takou radosťou by som napísal aj šesť lístkov naraz, ale mne sa skôr minie, čo písať, než Vám, drahá, ak to môžem sám povedať. Len ústne chcem povedať to, čo ide tak ťažko, lebo som veľký otrok, nerozhodujem sám o sebe. Viac nepíšem, kedy idem, lebo ani vtedy som nemohol ísť, keď som to pokladal za isté. Prosím Vás, drahá, ak ma naozaj ľúbite, skoncujte s tým dotieravým sokom, v čo dúfam, a aj ste to urobili a neuznali ste jeho riadky za hodné odpovede. Čo sa týka Bözsi, naozaj ľutujem, že dobré priateľstvo došlo až sem; to som si nemyslel. Čo sa týka lístka Litaszkiho(?), chcel by som ho vidieť a chcel by som to sám vybaviť, [neprečítaná veta] Vás ľúbi Váš milý Feri. Týmto končím svoje riadky, zostávam. Do šťastného(?) videnia, pozdravuje Váš milujúci milý Feri.

## Uncertainties

1. **Row 26 tail, the reason the card stays partial.** Signs are clear: h a t e b i z a t a m e l a h o, then the card corner, then *szereti kedvese Feri* on the outer edge. Sentence not resolved. Candidates not adopted: *hát ezt bízza rám* would fit the sense very well but needs r where the sign is a plain gamma t with no middle bar, plus a lost zt and a double z, and leaves *el a ho*; *ahogy szereti* needs gy, and the corner is intact with no room for it; *bízatom el*, *eladó* give no sentence. The word before, *elintézn*, lacks its final i if *hát* starts the clause.
2. **Row 4** rests partly on sense. *írnék*: first sign under the postmark, the n shows only one stroke beside postmark letters, é from a separate tick in clear paper above the sign. *hat*: the third bar of a would-be e lies on the machine-cancel wave. *lapot*: the sign read t lies on the wave, which covers where the middle bar of r would be, and the o has a tail like i. Literally a reader could see *hetlapiris*; *hat lapot is egyszerre* is the only sentence found and it fits the following *de*.
3. **Row 5** *de*: the d has its tick to the right, the shape of h/p on this card. The hand reduces d and h to one stroke elsewhere (rows 9), so the call is word sense. *neke[m]*: no m is written; the area is clear of hiding, so this is the writer's omission.
4. **Row 15** *se m[e]hettem*: written s e m h e t t e m; no e between m and h. Writer's omission, or *sem [me]hettem*. The h was misread as n before; first stroke long, second short.
5. **Row 16** *biztosna[k] [g]ondo[l]tam*: one S-shaped sign serves for k and g; l not written. Same habit of dropped letters as *akar[om]* and *elintézn*.
6. **Row 25** *Litaszki*: clear letters, taken as a surname; not identified. *lapját*: h = p, written lahjat. Could be a common word I do not know; alone.
7. **Row 24** *jutova* for *jutott a*: the sign is a chevron v, not t; word sense.
8. **Rows 19-20** *vetélytársal* has j for ly and single l for ll; *mit*: the vowel is between o and i, no certain dot. The subject of *meg is tette* is taken as the addressee (maga-form).
9. **R1** starts with a stray single stroke, not explained. *maradok*: the d is short + long stroke, the o partly over a stain. Then o and a small curl: taken with stamp row S1 *ldo(g)* as *boldog* split across the line, which requires the curl (b, or k) and o in reversed order at the cramped corner. This is a conjecture, marked (?) in the text. The last sign of S1 keeps only a lower stroke; g is a restoration.
10. **Row 3:** the letters are s o r a i r a i r a: *ira* is written twice. Taken as a slip (dittography) and left out of the normalized text; *oly* is written oj, the family habit.
11. **Rows 7-8** *ha magam mondom* followed by a stray t: sense call kept from the first pass.
12. **Reading order** of edge rows and stamp block is inferred. *viszont[l]átásig*: no l visible between the two stamp rows.

## Why the readable parts are believed

The unchanged family key gives long runs of idiomatic Hungarian that could not arise by chance (*nagy rabszolga vagyok, nem rendelkezem magam felett; nem méltatta válaszra; ami a Bözsit illeti, igazán sajnálom*). The address, Budapest cancel and signature Feri fit the family. *Illeti* decodes identically in rows 22 and 25, *kedvese Feri* in R2 and S7, and *mokor* with the same spelling in rows 13-14 and 15.

## Revision 2026-11-02

Claude Opus 5.5, second attempt ordered by the human. Before: rows 3-5, 15, 25 (noun), 26 tail, R1 tail, S1 unread and rows 19-20 unclear. New crops in `work/rev2/` from the original in `work/hires/` (`work/rev2crop.py`): the red channel nearly removes the green-grey paper and shows ink through postmarks, the blue channel clears the stamp stain. All rows were re-read; the old ledger is kept as `work/ledger-2026-10-30.txt`.

Changed:

- **Sign classes.** Separated K (S with base curl) from G (flagged hook), D (left tick) from H (right tick). Red channel shows the extra bars of "e" in rows 3 and 4 and the "r" middle bar in row 4 can be postmark wave.
- **Rows 3-5 resolved:** *soraira. Oly örömmel írnék hat lapot is egyszerre, de neke[m] hamarabb...* (see 2, 3 above).
- **Row 15 resolved:** n was h, s was k: *se m[e]hettem, mikor*.
- **Rows 18-20 resolved:** *avval a tolakodó vetélytársal, mit remélek*. First sign of row 20 is s, *mot* is *mit*.
- **Row 21:** final sign is a, *válaszra*.
- **Row 25:** *lapját illeti*, with *Litaszki* left as a name.
- **R1:** h a r a h i was m a r a d: *soraim, maradok*. **S1:** l h n was l d o, giving the tentative *boldog viszontlátásig*.
- **Row 26:** last sign is o, not i; still unread.

Not achieved: the clause in row 26. By the completeness rule the card stays partial; no DONE1, no register entry. The sister cards hcp-1212, 1213, 1216, 1217, 1218, 1243, 1301 were searched for the closing formulae and for *biz-* words; nothing resolves the clause.
