# HCP1275 — Feri to Jolánka Tóth: a farewell after she cooled towards him

**Status: PARTIAL (revised 2026-11-02). All of the card's roughly 721 signs are transcribed and decoded, but one whole clause (rows 2–4) is not understood, and one further isolated word (row 24 `eden`) is not understood. Row 12 is now read. Review 1 verdict REVISE; findings addressed. No register entry is made for this card.** Written 2026-11-01 by Claude Opus 5.5. No earlier work exists on this number. The key comes from the finished Jolánka-family cards (HCP1216, 1212, 1301 and others; their earlier work is credited on those cards to the OpenAI GPT solver and Claude Opus 5.5). The portal shows *Not solved* and attaches no transcription or solution; no published solution of this card was found or used. The ledger is my own manual transcription from `work/hires/*_adr.jpg`; the portal attaches none.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (register label: MASC), same key as the Tóth Jolánka family. Text on the address side: 27 rows, the end of row 27 running up the right edge, and 6 short rows written under the stamp (the stamp has been lifted; its frame and torn remains are still there). The picture side has printed text only. Only the first letter, M, is an ordinary Latin capital.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | S-shaped section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left + right bowl | cs | three short strokes | m | gamma/corner | t |
| short stroke then long stroke | d | two short strokes | n | bold plain cross | u (two dots: ü) |
| three bars | e | cursive loop | o (dots: ö, ő) | chevron | v |
| upright cross + | f | long stroke then short stroke | h / p | low loop with descender | y |
| lightning-shaped sign | g | dotted crossed curve | i | crossed diagonal with flag | z |
| inverted T | j | large joined loop + y | gy (rows 2, 26; elsewhere g + y) | | |

The only difference from HCP1301's description is that the g here is an angular lightning shape rather than an "open loop"; its value is fixed by about 20 occurrences of *hogy*, *egy*, *meg*, *legyen*.

Key transferred, not reconstructed. Every value was confirmed on this card by words that recur or read clean.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1275/work/decode_opus.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger-opus.txt` (one token per written sign) and prints the literal rows and `work/normalized-opus.txt`.

## Literal decipherment (as printed by the command)

```
01 mejentiszteltjolanka              15 saalelkiismerethogyaz
02 kisaszonyönaztmondta{n}agy         16 szivemöszetörtlehethogy
03 körhogynemhalgatah{?l}ely          17 azistenmajdojanjohogy
04 karamikormegszeretelvolt          18 megvaltafajdalmeimtol
05 irantameznemlehetoka              19 majdakorenisbodogleszek.
06 elhidegülesinekirantam            20 eztavasutasnekalanyarol
07 masokotnemtalelhatok              21 amitirnemtudoksemitirni
08 minthogyakadtegyma                22 mertnemtudommirölvan
09 sikakigazdagabescsinosabb         23 szo.fenyke{p}itaztsoheki
10 legenyakinekszerencseje           24 nemadomkezböleden,ugyatöbbi{g}{t}ergyakotsemlegelabb
11 voltmagatelhoditani               25 ezeketlethatomesmegleszorökitveemlekeber{z}ivem
12 nemalokutja{b}alegyan              26 beotleszorökreazenyemeltehetamitakarnekemmindegy
13 boldoojanbodoghogy                27 ha{t}üzbeteszivagyviszakildííslegalabbnemzaverjabold
14 eszebesejusakhogynebant           E1 ogsagat (up the right edge)
under the stamp: sir{i?}[g] | hüima | dojaes | volt | kedves | se{f}eri
```

## Hungarian (normalized)

Mélyen tisztelt Jolánka kisasszony! Ön azt mondta, [olvasatlan tagmondat: a nagy kör(?), hogy nem hallgat a h?ely(?), kár(?),] amikor még szeretet(?) volt irántam. Ez nem lehet oka elhidegülésének irántam; mást nem találhatok, mint hogy akadt egy másik, aki gazdagabb és csinosabb legény, akinek szerencséje volt magát elhódítani. Nem állok útjába, legyen boldog, olyan boldog, hogy eszébe se jussak, hogy ne bántsa a lelkiismeret, hogy az [én] szívem összetört. Lehet, hogy az Isten majd olyan jó, hogy megvált a fájdalmaimtól, majd akkor én is boldog leszek. Ezt a vasutasnak a lányáról, amit ír, nem tudok semmit írni, mert nem tudom, miről van szó. Fényképét azt soha ki nem adom kezből, eden(?), úgy a többi tárgyakat sem; legalább ezeket láthatom, és meg lesz örökítve emlékbe, szívembe ott lesz örökre az enyém. Eltehet, amit akar, nekem mindegy, ha tűzbe teszi vagy visszaküldi is, legalább nem zavarja boldogságát.

Under the stamp: Sírig hű imádója és volt kedvese, Feri.

## English

Deeply respected Miss Jolánka! You said [unread clause: literally perhaps "the great kör(?), that does not listen to the h?ely(?), a pity(?)"], when there was still love(?) for me. That cannot be the reason for your cooling towards me; I can find no other than that there is another, a richer and more handsome young man, who had the luck to win you. I will not stand in your way; may you be happy, so happy that I do not even come to your mind, that your conscience does not trouble you that my heart is broken. Perhaps God will be so good as to deliver me from my pains; then I too shall be happy. About the railwayman's daughter whom you write of, I can write nothing, because I do not know what it is about. Your photograph I will never let out of my hand, [eden?], nor the other things; at least I can look at these, and it will be immortalized in memory; in my heart, there it will be mine forever. You may put away what you want, it is all the same to me, even if you put it in the fire or send it back; at least it does not disturb your happiness.

Under the stamp: Your adorer, faithful unto the grave, and former sweetheart, Feri.

## Slovak

Hlboko vážená slečna Jolánka! Povedali ste, [neprečítaná veta: doslova azda „veľký kör(?), že nepočúva h?ely(?), škoda(?)“], keď ešte bola(?) láska ku mne. To nemôže byť príčinou Vášho ochladnutia voči mne; nemôžem nájsť inú, než že sa našiel iný, bohatší a krajší mládenec, ktorý mal šťastie Vás získať. Nebudem Vám stáť v ceste, buďte šťastná, taká šťastná, aby som Vám ani na um neprišiel, aby Vás netrápilo svedomie, že moje srdce je zlomené. Možno bude Boh taký dobrý, že ma vyslobodí z mojich bolestí, potom budem šťastný aj ja. O tej dcére železničiara, o ktorej píšete, nemôžem napísať nič, lebo neviem, o čo ide. Vašu fotografiu nikdy nedám z ruky, [eden?], ani ostatné veci; aspoň sa na ne môžem pozerať, a bude zvečnená v pamäti; v mojom srdci, tam bude navždy moja. Môžete si odložiť, čo chcete, mne je to jedno, aj keď to dáte do ohňa alebo pošlete späť; aspoň to neruší Vaše šťastie.

Pod známkou: Váš do hrobu verný ctiteľ a bývalý milý, Feri.

## Uncertainties

**Not understood: one whole clause and one further isolated word (the second earlier gap, row 12, is resolved; see Revision 2026-11-02). The letters are read, apart from the marked signs; the sense is not. Because the clause in item 1 is whole, the card counts as partial.**

1. **Rows 2–4, clause after *Ön azt mondta*.** It contains row 3 `h{?l}ely`: h sign, then a long wave sign crossed by the black postmark (best match wave l, not certain), e, l, y. No word established. The next sentence (*Ez nem lehet oka…*) answers exactly this clause, so the surrounding argument does not supply its content.
2. **Row 12**: resolved, *nem állok útjába* (see Revision 2026-11-02).
3. **Row 24 `eden`** after *kezböl*: e d e n and a comma, all clear. Could be a noun of address; not established. It does not affect the surrounding sentence. The last sign's left stroke is a little longer than its right; I keep n, h/p would give no word either.

The count of 721 is approximate: at rows 24 (`{g}{t}`), 25 (`R {z}`) and 27 (`{t} U:`) the tokens are context decisions, not clean sign readings (items 5–7).

**Weakest passage, rows 2–4.** *Ön azt mondta* is sure and *amikor még … volt irántam* is sure. Between them: `a {n} a gy` has a heavily blotted sign, a smear with a tail, not recognisably n; *a nagy* is context only. A blotted h (*hagy*) is no more excluded than n. `kör`: the second sign is an o-shape with one clear dot (ö, ó possible, so *kör* or *kor*). `karam` is divided *kár, amikor* on sense. Row 4 `megszeretelvolt` is also open: *még szeretet volt* is one choice, *meg szerettél volt* is not excluded by the signs. Whether `kar` at the start of row 4 is *kár* ("a pity") or belongs to the word before the row break (`h{?l}ely|kar`, the writer swaps a and e constantly) is unsettled; no such word was found. The translation here is only a literal stab.

**Sign calls that rest on word sense or are restorations:**

4. Row 12 `{b}`: a faded tall sign in a water stain, then two bars. Revised from `{d}`: the shape is compatible with the six, but it rests partly on word sense (*útjába*).
5. Row 24 `{g}{t}`: after *többi* a small raised squiggle like g (treated as stray), then a tall stroke with a short falling tick, closest to t: *tergyakot* = *tárgyakat*. Sense-based; the shape is not the usual gamma.
6. Row 25 `{z}`: at the end of `emlekeber` (F clear) comes an overwritten composite with crossing strokes, probably not two signs, then *ivem*. Read as z of *[sz]ivem*; the F may be a false start. Normalized *emlékbe, szívembe* (with *be* from row 26). The second word's first s is not visible as a separate sign.
7. Row 27 `{t}ü`: after *ha* a single wide arch running into the bottom card edge, with two dots and a faint downstroke at its right. This is not a separate t and ü on the pixels; *tűzbe* ("into the fire") comes from context, not from a sign reading; an arc with dots also resembles ö, which gives no word. The rest of the clause (*beteszi vagy visszakildóís*) supports it.
8. Row 13 `boldo ojan`: the sign after *bold* looks like o, not g; a g is expected (*boldog olyan*), so either g is omitted or the sign is a malformed g.
9. h/p and d/n: the h/p sign is separated from d by stroke order (long+short = h/p, short+long = d). *fenykep-* and *h* words are decided by word sense. d and n calls are by this stroke difference; rows 8 *akadt*, 9 *gazdagab* rest on it.
10. Stamp row 1: `sir`, then a sign at the stamp tear (best match i), then the g of *sírig* is under the stamp residue: **restoration of one letter**, hidden sign; the formula *sírig hű* recurs in the family (HCP1216). Below row S6 there are traces at the torn edge that look like remains of the printed stamp, not ink of this message; I could not exclude a further sign there.
11. Row 22: over the o of *tudom* a second blurred curl; read as a single o.
12. Row 23 `{p}` (*fénykép-*): the only p on the card, same sign as h, decided by word sense.
13. Stamp row 6 `{f}`: the third sign of `seferi` is blotted and slanted; the value f comes from the expected name Feri, not from a clean shape.

**Writer's spellings normalized (signs are clear, normalization is editorial):** ly written j (*mejen, ojan*); frequent single for double consonants (*kisaszony, halgata, akor, öszetört, semit, viszakildó, csinosab* in *gazdagab*); e and a repeatedly interchanged (*irantam* is fine but *talelhatok, lethatom, legyan, zaverja, fajdalmeim, tergyakot*, row 24 *legelabb*); *masokot* = mást/másokat, *szeretelvolt* = szeretet volt (l for t), *bodog* = boldog (twice), *soheki* = soha ki, *kezböl* = kezemből, *viszakildíís*: two ticked i signs, normalized *visszaküldi is*; *ezt a vasutasnek* is kept as *ezt a vasutasnak* ("this railwayman's" / "the railwayman's"). *jusak* is read as *jussak* (1st person, "may I not come to your mind"). *az szívem* keeps a missing *én*.

Accents are mostly unmarked; only those seen are in the ledger, others are supplied in normalization. Row-end word breaks (*ma|sik*, *bold|ogságát*, *kedves|se*) are normal.

## Why it is correct

- The family key, unchanged, turns the card's roughly 721 signs into Hungarian; no key change or new value was needed.
- Long unforced passages that no chance mapping gives: *elhidegülésének irántam*, *gazdagabb és csinosabb legény*, *szerencséje volt magát elhódítani*, *ne bántsa a lelkiismeret*, *az Isten … megvált a fájdalmaimtól*, *örökre az enyém*, *eltehet, amit akar, nekem mindegy*, *legalább nem zavarja boldogságát*.
- Coherent narrative with formal *Ön* address, a shift from the family's *édes Jolánkám* to the cold *Mélyen tisztelt … kisasszony*, and the addressee and signature fit the family: to Tóth Jolánka, Jászárokszállás; signed Feri with the *sírig hű* formula, hidden under the stamp as on HCP1216.
- The sentence continues across the corner up the right edge exactly as HCP1216 does (*boldog|ságát*).

## Date

Not on the card in cipher. The portal file name gives 1913-08-13; the cancellation at the stamp shows only 913 legibly, with the rest of the date unreadable, so the day and month rest on the file name.

## Response to review 1

Verdict REVISE. All nine findings accepted. No letter value changed; the reading of the understood text changed in rows 20–21 and 25 only.

1. **Rows 2–4, partial: accepted.** I re-read the blot and rows 2–4 on the reviewer's crops `n1.png` and `r14b.png`. The blot is not a recognisable n. I tested the lead `h{?l}ely|kar` as one word, and a blotted h (*hagy*), and neither gives a word. The clause stays unread. The status line, the uncertainties and all three translations now say partial, and no register entry is written.
2. **Rows 20–21: fixed.** The signs are `amit ir nem tudok`, so *amit ír, nem tudok semmit írni*. Normalized text, translations and the spelling list corrected; *irnem tudok* removed from the list. Jolánka's letter raised the subject.
3. **Row 10: fixed.** `z10.png` shows three bars; the ledger now has E (`szerencseje`). Normalization unchanged.
4. **Row 27: fixed.** `z27b.png` shows two ticked signs of the same crossed form; the ledger now has I' I' (`viszakildíís`). The "extra o dropped" remark is gone.
5. **S6: fixed.** Now `{f}` in the ledger, listed as uncertainty 13.
6. **p call: fixed.** Row 23 now has `{p}`, the ledger header explains it, uncertainty 12 lists it.
7. **Row 25: fixed.** *meg lesz örökítve*, "it will be immortalized", in all versions. The *meg szerettél volt* alternative for row 4 is noted.
8. **Count: fixed.** "721" is now called approximate here and in the decoder output; items 5–7 of the uncertainties describe the signs as the reviewer saw them.
9. **Date: fixed.** See the Date section.

Reproduction re-run after the fixes: all four SHA-256 checks pass and the output matches the rows above.

## Revision 2026-11-02

Second attempt by Claude Opus 5.5, ordered by the human. New crops from `work/hires/*_adr.jpg` with green-channel contrast at 3 to 7x are in `work/rev2/`. Unread at the start: the clause in rows 2–4, row 12 `alokutja`, row 24 `eden`. No letter value of the key changed.

**Resolved: row 12.** The earlier reading failed on word division. `nem alok utja{b}a legyan` is *nem állok útjába, legyen boldog*, "I will not stand in your way; may you be happy", the single l being the writer's usual habit (*halgata, akor*). The sign after the faded a was read `{d}` with the normalization *de*. On `work/rev2/r12w.png` and `r12z.png` it is a tall stroke falling from the upper right to a low bowl, faded in a water stain and cut by the stain's edge. This is compatible with the six and not with a stroke pair. The closed loop of the six is only partly visible, so the b is a call by shape together with word sense, disclosed in the ledger as `{b}`. The two bars after it are clear. No *de* now stands in the text.

**Still unread: row 24 `eden`, an isolated word.** `work/rev2/r24z.png`: three bars; short then long stroke (d); three bars; a stroke pair, the left a little longer; a mark like a comma. The stroke difference in the pair is well below that of a real h (row 3), so n stays. I tested a reversed p (*éppen*), but the first pair is plainly short then long, so that attractive reading is not on the pixels and is rejected. Also rejected: *ezen* (no z), *édes* (no s), *eddig*. The sentence reads without this word.

**Still unread: rows 2–4, a whole clause.** What the pixels show:

- Row 2 blot (`work/rev2/bl.png`): wet ink wiped with a finger, leaving a diagonal mass with a small tail. Two bars and a clear joined gy follow. No stroke pair can be separated, so n, h and m all stay open; *nagy* is context only.
- Row 3 second sign: the loop form of o (compare row 4 *amikor*), not the crossed i. One dot lies above it, so ö or ó: *kör* or *kór*, also *kor*.
- Row 3 end (`h1g.png`): h (ratio of strokes clear), then a short wave fused with the postmark arc, three bars with the lowest faint, then an arch running into y. The arch may belong to the wave l or be the entry stroke of y, whose form elsewhere starts with an arch (row 2). So the word is `h ? e [l] y` or `h ? e y`. The writer never otherwise spells ly as l + y (he writes j: *mejen, ojan*), which counts against *hely*.

Tried as divisions or spellings, none giving a sentence: *nagy kár/kór/kor*, *nagykorú*, Nagykörű (place), *magy. kir.*, *hely kár*, *helykor*, *hegy*, *hölgy*, *hüvely*, *hülye kor*, *lelkére*, *hallgatá h[ogy]*, *ahelyett*, and the same with p for h. Sister cards have no matching formula: the nearest is HCP1204 *nem hallgatok az itteni pletykákra*, a different correspondent and wording. Each of these either needs signs that are not there or leaves the clause senseless, so none is adopted.

**Result.** The card stays partial, because a whole clause is unread. No DONE2, no register entry. The existing markers are kept. Normalized text, the three translations, the ledger (`{d}` to `{b}`), `report/report.md` and the PDF are updated.
