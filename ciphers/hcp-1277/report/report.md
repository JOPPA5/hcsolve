# HCP 1277 (cpc_1914-03-01_HU__HU_Jasz Arokszalas_jolanka-48): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered; all 29 main rows read with no opaque word, and the short closing under the stamp is read as far as the damage allows. Independent review 1 verdict REVISE; all findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1277 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1277), portal name cpc_1914-03-01_HU__HU_Jasz Arokszalas_jolanka-48, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a tinted photograph of a couple about to dance, with the printed caption Édes párom szállj velem… ("Sweet partner, glide with me…") and a four-line printed verse about a waltz. It carries no cipher.

The whole message is on the address side, in green ink and invented signs: 29 rows on the left half of the card and seven short rows hidden under the stamp, where the stamp has been torn or soaked away. The address is plain writing: Szépreményű / Tóth Jolánka / úrleánynak / Jász Árokszállás ("To the hopeful young lady Jolánka Tóth, Jászárokszállás"). The boxed postmark reads ÚJPEST. The round postmark shows the digits 91 and a third digit under the pen, so it neither confirms nor contradicts the date 1914-03-01 in the portal's file name.

The card belongs to the family of cipher cards to Jolánka Tóth, of which HCP 1216, 1212, 1213, 1217, 1218, 1243 and 1301 are finished in this repository. It is signed Feri, as HCP 1216 is. That he is the same Feri is likely from the key and the addressee, not proven.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the plain address and the postmarks (source/address-large.jpg)](../source/address-large.jpg)

## Method

The key was transferred unchanged from the finished sister card HCP 1216; this is a known family key, not a new key recovery. The work was the transcription. The solver read every row from enlargements of the un-converted original scan, including the blue channel for the faded ink under the stamp, and recorded a sign ledger with one token per written sign: 668 tokens in the main text and 43 under the stamp. A short script decodes the ledger. No OCR was used and no plaintext of this card was available from any source.

The writer spells by ear, often drops a doubled consonant and rarely shows an acute accent. The literal decipherment keeps this; the normalized text supplies accents and standard spelling, and every such change is listed below.

The two hardest places were solved by word division, not by changing letters. The strings `esara` and `esebvel` looked like unknown words in the first round. Review showed that each begins with the word és ("and"): és arra in row 12 and és evvel in row 25.

![Row 12: the free-standing acute above the e of és; the row above has a different sign (work/crops2/r12acc.png)](../work/crops2/r12acc.png)

![Row 25: b, then a chevron and a small b-bowl written on top of each other, between e and e (review/work/z25b.png)](../review/work/z25b.png)

![Round postmark, turned so that the digits stand upright: 9, 1, and a third digit under the green pen (work/crops2/year.png)](../work/crops2/year.png)

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs. The labels are conventional names for the handwritten shapes.

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

Dots over o and u give ö and ü. Acute accents are small strokes over the base sign. On this card gy is two signs, g and then the y-shaped sign, in all 14 instances. Left bowl c does not occur alone here, only in cs.

## Plaintext

Literal decipherment, row by row (`{v/b}` = overwritten sign, `{?}` = unreadable sign, `[...]` = lost; S rows are under the stamp):

```text
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

Normalized Hungarian:

Szeretett édes Jolánkám! Kívánom, hogy a legjobb egészségben találja soraim. Mint írtam is, édesem, hogy a közbejött akadályok miatt nem élvezhetjük a viszontlátás örömeit, de bízunk az Istenben, és legyen türelemmel. A legközelebbi alkalmat keresni fogom, hogy viszontláthassam. Bár nehezen megy, most már visszakerültem, a régi utazási mederbe estem vissza, és arra kell várnom, míg a forgalom egy kicsit enyhébbek nem lesznek. Most nincs más hátra, édesem, mint egyelőre lemondani a viszontlátásról, amit nagyon sajnálok, édesem. Úgy vártam azt az időt, hogy biztosan megtudjam, hogy lesz-e szabadom vagy sem. Gondolhatja, édesem, mily érzés fogott el, mikor megtudtam, hogy egy hosszú útra küldtek, és evvel keresztülhúztak minden számításomat. Most bezárom soraim, maradok szerető kedvese Feri. Sorait várom, írjon, édes, mi újság.

Under the stamp: Édesem, csókolom számtalanszor. Szeret[...] ked[...] [...]

English:

My beloved sweet Jolánka! I wish that my lines find you in the best of health. As I also wrote, my sweet, because of the obstacles that came up we cannot enjoy the joys of meeting again, but we trust in God, and do be patient. I will look for the next opportunity to see you again. Though it goes hard, I am now back; I have fallen back into my old travelling routine, and I must wait for this, until the traffic gets a little lighter. There is nothing left now, my sweet, but to give up our meeting for the time being, which I greatly regret, my sweet. I so waited for the time when I would know for certain whether I would have time off or not. You can imagine, my sweet, what feeling came over me when I learned that they were sending me on a long journey, and with that they crossed out all my plans. Now I close my lines; I remain your loving sweetheart, Feri. I await your lines; write, sweet one, what is new.

Under the stamp: My sweet, I kiss you countless times. Lov[ing] sw[eetheart…]

Slovak:

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky našli v najlepšom zdraví. Ako som aj písal, drahá, pre prekážky, ktoré nastali, si nemôžeme vychutnať radosti zo stretnutia, ale dôverujeme v Boha, a majte trpezlivosť. Budem hľadať najbližšiu príležitosť, aby som Vás znova videl. Hoci to ide ťažko, teraz som už späť, znova som upadol do starého cestovného koryta, a na to musím čakať, kým doprava trochu nepoľaví. Teraz nezostáva nič iné, drahá, ako sa zatiaľ vzdať stretnutia, čo veľmi ľutujem, drahá. Tak som čakal na ten čas, aby som isto vedel, či budem mať voľno, alebo nie. Môžete si predstaviť, drahá, aký pocit ma pochytil, keď som sa dozvedel, že ma posielajú na dlhú cestu, a tým prečiarkli všetky moje plány. Teraz končím svoje riadky, ostávam Váš milujúci milý, Feri. Čakám na Vaše riadky, napíšte, sladká, čo je nové.

Pod známkou: Drahá, bozkávam Vás nespočetnekrát. Milu[júci] mi[lý…]

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1277/work/decode_opus.py
```

The command checks the SHA-256 of the four image files, decodes the ledger `work/ledger-opus.txt` and prints the literal rows and the normalized text.

## Uncertainties

1. **Row 12 és arra, resolved by word division.** The letters are unchanged from round 1 (e, s, a, r, a) and were first misread as one word `esara`. The e has its own acute stroke, clearly separate from the sign above it (figure above). ara → arra is a normalization, in line with the writer's frequent single consonants, and arra is the antecedent of the míg clause. The reading therefore rests on the pixels for the letters and on word sense for the division.
2. **Row 25 és evvel: one sign rests on word sense.** e s | e b, then a chevron and a small closed b-bowl written on top of each other, then e l (figure above). I transcribe the sign as `{v/b}`: the writer changed his mind between b and v, so the written form is ebvel/ebbel corrected in one direction or the other, and I cannot tell which stroke came last. evvel (= ezzel) is a normalization from sense.
3. **Under the stamp** the closing is damaged by tear, stain and very faded (orange-brown) ink, recovered in part from the blue channel. Read: édesem csókolo|lom szá|mtalan|szor sze|ret…. In csókolo the k is the g-like hook, read as k from sense. Row S6: after ret a blotted sign (ö likely) and a stained k-position sign, then faint e d. Row S7: a hook (s or part of v), then signs lost under the tear (a ring-shaped mark there is postmark or stain, not ciphertext), then faint e r and a last sign that looks more like a right hook than a dotted i, so the first-round literal `eri` is withdrawn in favour of `er{?}`. The formula is evidently szerető kedvese Feri, as in row 28, but that is **not** a reading and is not printed in the plaintext. The ledger's `S6 # #` and `S7 [ … #` mark this.
4. **Calls resting on word sense (near-homographs):** every h/p sign on this card is read h from word sense (hogy, nehezen, enyhebbek, hátra, hosszú, keresztülhúztak …); no p occurs in the text. d/h at the head of row 6 de (tall stroke + tick); row 19 időt: the sign is d (joined, two strokes), which could be taken as n; the literal alternative inöt is no word. Row 11 utazási: the sign before i is a loop-like s with curl joined to the i, close to o; utazaoi is no word. Row 29 ujsag: the same curled s, and a final g shaped more like S (k); mi újság is the only reading. Row 23 mikor: i has only a dash above it. Row 1 kívánom: the i dot is at the card edge and is not secure; the letter is o-like otherwise.
5. **Blots:** row 7 közelebbi, the ö is overwritten by a blot, dots visible; row 14 lesz, s blotted before z; row 15 nincs and row 18 nagyon, the first n is a heavy overwritten hash-like sign; row 29 írjon, the j is blotted and z-like (read j from sense; irzon is no word). Row 24 begins `tutam` with a dark but plain cross, u (the two dots beneath it belong to the ü of küldtek in row 25): a dittography across the row break, megtud|tutam, normalized megtudtam.
6. **Writer's spellings normalized:** szeretet → szeretett, legjob → legjobb, egeseg- → egészség-, miat → miatt, elvezhetük → élvezhetjük, akadajok → akadályok, mij → mily (ly written j, consistently), keresn → keresni (i omitted), visza → vissza, ara → arra, eb{v/b}el → evvel, kel → kell, meg → míg (dialect; the míg … nem construction fixes the sense), egyenlöre → egyelőre, fogot → fogott, hoszu → hosszú, megtudtam in row 20 rendered as a purpose clause (megtudjam), szeretetö → szerető (extra te). enyhébbek … lesznek is printed as written: a plural with the singular forgalom, the writer's agreement. szabadom is printed as written and probably means "my leave, my time off". Accents (á, é, í, ó, ú) are mostly invisible and are supplied. Row-breaking words: sora|im, köz|bejött, élvez|hetjük, nehe|zen, ede|sem (×2), lemon|dani, mij|érzés, megtud|tutam, számitáso|mat, lesz|nek.
7. **Date.** The portal's file name says 1914-03-01. The round postmark shows the digits **91** upright (figure above, with the foot serif of the 1 at the bottom); a third digit lies under the green pen stroke and is not legible. So it shows a year 91x and does not settle 1914 against a later year. The boxed mark reads ÚJPEST. Day and month are not legible. The circumstances of "being sent on a long journey" (a railwayman? military?) are not established. The sender is signed Feri (as on HCP1216); identity with that Feri is likely from the key and addressee, not proven.
8. **Address side**, plain writing, not cipher: Szépreményű / Tóth Jolánka / úrleánynak / Jász Árokszállás ("To the hopeful young lady Jolánka Tóth, Jászárokszállás"); the first line lies over the postmark and is clearly legible on enlargement.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **REVISE**. It ran the command, decoded the ledger with its own table, read all rows sign by sign from its own crops, and confirmed the key, the language and the context. It found no sign of an outside plaintext. Its findings and what changed:

- **Word division (major).** `esara` and `esebvel` are és arra and és evvel. Accepted after checking the pixels; the two "not understood" words are gone, and the blotted sign is recorded as an overwrite.
- **Row 10 (major).** The card has már, not mer; the claimed spelling mer was withdrawn.
- **Rows 24–25 (major).** The two dots belong to the ü of küldtek, and the blotted sign in row 24 is a plain u, giving the dittography megtud|tutam.
- **gy (minor).** Two signs, not one; ledger and key table corrected, plaintext unchanged.
- **Counts and editorial marks (minor).** hogy occurs 6 times; enyhébbek nem lesznek and szabadom are now printed as written.
- **Word-sense calls (minor).** The k of csókolo and the last sign of the stamp rows are disclosed; that last sign is now unread.
- **Comma in most már visszakerültem, a régi utazási mederbe estem vissza.** Disputed and kept: mederbe goes with estem vissza.
- **Address side and date (minor).** Szépreményű and ÚJPEST are recorded. The reviewer's year 916 is disputed: the legible digits are 91 upright, "16" comes from viewing them upside down, and the third digit lies under the pen.

Apart from these points the reading is the one handed over in round 1.

## Credits

- **Claude Opus 5.5, 2026-11-01:** transcription, transfer of the family key, decipherment, response to review and this report.
- **Claude Opus 5.5, separate reviewer agent:** independent review.

## Sources

- HC Portal record 1277, General, Description and Attachments tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1277 (source/metadata.md).
- Scans of both sides from the portal (source/picture-large.jpg, source/address-large.jpg, and the originals in work/hires/); URLs and hashes are in SOURCES.md.
- Family key: ciphers/hcp-1216 (Jolánka family, also HCP 1212, 1213, 1217, 1218, 1243, 1301).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-01.
