# HCP1277 — Feri to Jolánka Tóth: the meeting is off, he has been sent on a long journey

**Status: whole message read, no opaque word left; the closing under the stamp is physically damaged (disclosed below). Corrected after review 1 (REVISE).** Written 2026-11-01 by Claude Opus 5.5.

Credit: all work on this number (transcription, key transfer, decipherment) is by Claude Opus 5.5; the key comes from the finished Jolánka-family cards (HCP1216, 1212, 1213, 1217, 1218, 1243, 1301). No external plaintext was used: the portal shows status *Not solved* with no attached transcription or solution; no published solution of this card was found.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (register label MASC), same key as HCP1216 unchanged. Accents are marks over the base sign.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c (not used here alone) | three short strokes | m | gamma/corner | t |
| long stroke + joined tick | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | stroke + right tick (h/p near-homograph) | h / p | low descender | y |
| small 5-shaped hook | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | y-shaped sign (loop + descender) | y | opposed bowls | cs |

Dots over o/u give ö/ü. On this card *gy* is always two separate signs, the 5-shaped hook g and then the y-shaped sign, all 14 instances checked (`work/crops2/gy0.png`, `gy1.png`, `gy2.png`). The same y-shaped sign stands alone in *enyhebbek* (row 14).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1277/work/decode_opus.py
```

It checks the SHA-256 of all four image files, decodes the manual sign ledger `work/ledger-opus.txt` (one token per written sign: 668 tokens in 29 rows plus 43 in 7 rows under the stamp; the first-round ledger is kept as `work/ledger-opus.round1.txt`) and prints the literal rows, then the normalized text `work/normalized-opus.txt`. The ledger is a manual transcription from enlarged crops of `work/hires/*_adr.jpg` (`work/crops/`).

## Literal decipherment

```
01 szeretetedesjolankamkivanom     16 semmintegyenlörelemon
02 hogyalegjobegesegbentalaljasora 17 daniaviszontlatasrol
03 immintirtamisedesemhogyaköz     18 mitnagyonsajnalokede
04 bejöttakadajokmiatnemelvez      19 semugyvartamaztazidöt
05 hetükaviszontlatasörömeit       20 hogybiztosanmegtudtam
06 debizunkazistenbeneslegyen      21 hogyleszeszabadomvagy
07 türelemmelalegközelebbi         22 semgondolhatjaedesemmij
08 alkalmatkeresnfogomhogy         23 erzesfogotelmikormegtud
09 viszontlathassambarnehe         24 tutamhogyegyhoszuutra
10 zenmegymostmarvisza             25 küldtekeseb{v/b}elkeresztül
11 kerültemaregiutazasi            26 huztakmindenszamitaso
12 mederbeestemviszaesara          27 matmostbezaromsoraim
13 kelvarnommegaforgalom           28 maradokszeretetokedveseferi
14 egykicsitenyhebbeknemlesz       29 soraitvaromirjonedesmiujsag
15 nekmostnincsmashatraede
under stamp: edesem | csokolo | lomsza | mtalan | szorsze | ret{?}{?}ed | s[...]er{?}
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb egészségben találja soraim. Mint írtam is, édesem, hogy a közbejött akadályok miatt nem élvezhetjük a viszontlátás örömeit, de bízunk az Istenben, és legyen türelemmel. A legközelebbi alkalmat keresni fogom, hogy viszontláthassam. Bár nehezen megy, most már visszakerültem, a régi utazási mederbe estem vissza, és arra kell várnom, míg a forgalom egy kicsit enyhébbek nem lesznek. Most nincs más hátra, édesem, mint egyelőre lemondani a viszontlátásról, amit nagyon sajnálok, édesem. Úgy vártam azt az időt, hogy biztosan megtudjam, hogy lesz-e szabadom vagy sem. Gondolhatja, édesem, mily érzés fogott el, mikor megtudtam, hogy egy hosszú útra küldtek, és evvel keresztülhúztak minden számításomat. Most bezárom soraim, maradok szerető kedvese Feri. Sorait várom, írjon, édes, mi újság.

Under the stamp: Édesem, csókolom számtalanszor. Szeret[...] ked[...] [...]

## English

My beloved sweet Jolánka! I wish that my lines find you in the best of health. As I also wrote, my sweet, because of the obstacles that came up we cannot enjoy the joys of meeting again, but we trust in God, and do be patient. I will look for the next opportunity to see you again. Though it goes hard, I am now back; I have fallen back into my old travelling routine, and I must wait for this, until the traffic gets a little lighter. There is nothing left now, my sweet, but to give up our meeting for the time being, which I greatly regret, my sweet. I so waited for the time when I would know for certain whether I would have time off or not. You can imagine, my sweet, what feeling came over me when I learned that they were sending me on a long journey, and with that they crossed out all my plans. Now I close my lines; I remain your loving sweetheart, Feri. I await your lines; write, sweet one, what is new.

Under the stamp: My sweet, I kiss you countless times. Lov[ing] sw[eetheart…]

## Slovak

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky našli v najlepšom zdraví. Ako som aj písal, drahá, pre prekážky, ktoré nastali, si nemôžeme vychutnať radosti zo stretnutia, ale dôverujeme v Boha, a majte trpezlivosť. Budem hľadať najbližšiu príležitosť, aby som Vás znova videl. Hoci to ide ťažko, teraz som už späť, znova som upadol do starého cestovného koryta, a na to musím čakať, kým doprava trochu nepoľaví. Teraz nezostáva nič iné, drahá, ako sa zatiaľ vzdať stretnutia, čo veľmi ľutujem, drahá. Tak som čakal na ten čas, aby som isto vedel, či budem mať voľno, alebo nie. Môžete si predstaviť, drahá, aký pocit ma pochytil, keď som sa dozvedel, že ma posielajú na dlhú cestu, a tým prečiarkli všetky moje plány. Teraz končím svoje riadky, ostávam Váš milujúci milý, Feri. Čakám na Vaše riadky, napíšte, sladká, čo je nové.

Pod známkou: Drahá, bozkávam Vás nespočetnekrát. Milu[júci] mi[lý…]

## Uncertainties

1. **Row 12 *és arra*, resolved by word division.** The letters are unchanged from round 1 (e, s, a, r, a) and were first misread as one word `esara`. The e has its own acute stroke, clearly separate from the sign above it (`work/crops2/r12acc.png`). *ara* → *arra* is a normalization, in line with the writer's frequent single consonants, and *arra* is the antecedent of the *míg* clause. The reading therefore rests on the pixels for the letters and on word sense for the division.
2. **Row 25 *és evvel*: one sign rests on word sense.** e s | e b, then a chevron and a small closed b-bowl written on top of each other, then e l (`review/work/z25b.png`). I transcribe the sign as `{v/b}`: the writer changed his mind between b and v, so the written form is *ebvel*/*ebbel* corrected in one direction or the other, and I cannot tell which stroke came last. *evvel* (= *ezzel*) is a normalization from sense.
3. **Under the stamp** the closing is damaged by tear, stain and very faded (orange-brown) ink, recovered in part from the blue channel (`work/crops/st3b.png`). Read: *édesem csókolo|lom szá|mtalan|szor sze|ret…*. In *csókolo* the k is the g-like hook, read as k from sense. Row S6: after *ret* a blotted sign (ö likely) and a stained k-position sign, then faint *e d*. Row S7: a hook (s or part of v), then signs lost under the tear (a ring-shaped mark there is postmark or stain, not ciphertext), then faint *e r* and a last sign that looks more like a right hook than a dotted i, so the first-round literal `eri` is withdrawn in favour of `er{?}`. The formula is evidently *szerető kedvese Feri*, as in row 28, but that is **not** a reading and is not printed in the plaintext. The ledger's `S6 # #` and `S7 [ … #` mark this.
4. **Calls resting on word sense (near-homographs):** every h/p sign on this card is read h from word sense (*hogy, nehezen, enyhebbek, hátra, hosszú, keresztülhúztak …*); no p occurs in the text. d/h at the head of row 6 *de* (tall stroke + tick); row 19 *időt*: the sign is d (joined, two strokes), which could be taken as n; the literal alternative *inöt* is no word. Row 11 *utazási*: the sign before *i* is a loop-like s with curl joined to the i, close to o; *utazaoi* is no word. Row 29 *ujsag*: the same curled s, and a final g shaped more like S (k); *mi újság* is the only reading. Row 23 *mikor*: i has only a dash above it. Row 1 *kívánom*: the i dot is at the card edge and is not secure; the letter is o-like otherwise.
5. **Blots:** row 7 *közelebbi*, the ö is overwritten by a blot, dots visible; row 14 *lesz*, s blotted before z; row 15 *nincs* and row 18 *nagyon*, the first n is a heavy overwritten hash-like sign; row 29 *írjon*, the j is blotted and z-like (read j from sense; *irzon* is no word). Row 24 begins `tutam` with a dark but plain cross, u (the two dots beneath it belong to the ü of *küldtek* in row 25): a dittography across the row break, *megtud|tutam*, normalized *megtudtam*.
6. **Writer's spellings normalized:** *szeretet* → szeretett, *legjob* → legjobb, *egeseg-* → egészség-, *miat* → miatt, *elvezhetük* → élvezhetjük, *akadajok* → akadályok, *mij* → mily (ly written j, consistently), *keresn* → keresni (i omitted), *visza* → vissza, *ara* → arra, *eb{v/b}el* → evvel, *kel* → kell, *meg* → míg (dialect; the *míg … nem* construction fixes the sense), *egyenlöre* → egyelőre, *fogot* → fogott, *hoszu* → hosszú, *megtudtam* in row 20 rendered as a purpose clause (*megtudjam*), *szeretetö* → szerető (extra *te*). *enyhébbek … lesznek* is printed as written: a plural with the singular *forgalom*, the writer's agreement. *szabadom* is printed as written and probably means "my leave, my time off". Accents (á, é, í, ó, ú) are mostly invisible and are supplied. Row-breaking words: *sora|im, köz|bejött, élvez|hetjük, nehe|zen, ede|sem* (×2), *lemon|dani, mij|érzés, megtud|tutam, számitáso|mat, lesz|nek*.
7. **Date.** The portal's file name says 1914-03-01. The round postmark shows the digits **91** upright (`work/crops2/year.png`, with the foot serif of the 1 at the bottom); a third digit lies under the green pen stroke and is not legible (`work/crops2/year3.png`). So it shows a year 91x and does not settle 1914 against a later year. The boxed mark reads ÚJPEST. Day and month are not legible. The circumstances of "being sent on a long journey" (a railwayman? military?) are not established. The sender is signed Feri (as on HCP1216); identity with that Feri is likely from the key and addressee, not proven.
8. **Address side**, plain writing, not cipher: *Szépreményű / Tóth Jolánka / úrleánynak / Jász Árokszállás* ("To the hopeful young lady Jolánka Tóth, Jászárokszállás"); the first line lies over the postmark and is clearly legible on enlargement (`review/work/word.png`).

## Why it is correct

- The HCP1216 key, unchanged, turns all 29 rows into continuous Hungarian with no new sign classes; no word remains opaque.
- Long non-trivial strings fall out without forcing: *közbejött akadályok miatt, viszontlátás örömeit, bízunk az Istenben, legközelebbi alkalmat, keresztülhúztak minden számításomat, gondolhatja édesem mily érzés fogott el*.
- Repeated words decode identically: *hogy* ×6, *édesem* ×5 (one of them under the stamp), *viszontlát-* ×3, *visza* ×2.
- The content fits the family: formal *Ön* address, love-letter formulas, a thwarted meeting, the sender's constant travel (Vámosgyörk passage on HCP1216).

## Response to review 1

Verdict REVISE. Reproduction re-run after the changes: `python3 -I ciphers/hcp-1277/work/decode_opus.py` prints four OK hashes and the listing above.

1. **Word division, accepted and tested on the pixels.** Row 12: *és arra*; the acute over the e stands free of the row above (`work/crops2/r12acc.png`), and the sentence reads. Row 25: *és evvel*; the sign is a chevron and a small bowl superimposed (`review/work/z25b.png`). The ledger now records it as `V/6`, literal `{v/b}`. Normalized text, the three translations and uncertainties 1–2 are rewritten; the break before *Vissza* is gone.
2. **Fixed.** Row 10 is `M A F`, *már*: two bars with an acute (`review/work/z10.png`). The false claim of a spelling *mer* is removed.
3. **Fixed.** Row 25 `K X:d L`, the dots belong to this X; row 24 `T X T A M`, literal `tutam` (`review/work/z24.png`). Uncertainty 5 is rewritten.
4. **Fixed.** I inspected all 14 instances (`work/crops2/gy0.png`, `gy1.png`, `gy2.png`, montage scripts `work/gy_montage.py`, `work/gy_montage2.py`): the two signs are separate each time. The ledger now has G Y, and the key row reads y. The plaintext is unchanged; main-text tokens go from 654 to 668.
5. **Fixed.** *hogy* ×6, and *édesem* ×5 is stated as including the one under the stamp.
6. **Two parts fixed, one part disputed.** The text now has *enyhébbek nem lesznek* and *szabadom*, with notes. I keep the comma in *most már visszakerültem, a régi utazási mederbe estem vissza*: with *estem vissza* now part of the sentence, *mederbe* belongs to that verb (the review's own finding 1 makes this the case), and making it one clause with *visszakerültem* would strand *estem vissza*.
7. **Fixed.** The g-like k of *csókolo* and the last sign of S7 are in uncertainty 3; the ledger's last S7 sign is now `#`.
8. **Partly disputed.** *Szépreményű* is recorded (uncertainty 8), and ÚJPEST is recorded. I do not accept `916`. The two legible digits read **91** with the 1 upright; "16" comes from viewing them upside down (`review/work/pm180.png`). The third digit is under the pen (`work/crops2/year.png`, `year3.png`). There is therefore no stated conflict with the portal's 1914, only an unconfirmed year 91x (uncertainty 7).
