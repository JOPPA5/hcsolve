# HCP 1282 (cpc_-04-11_HU__HU_Jasz Arokszalas_jolanka-94): Feri to Jolánka Tóth, news of Ilona and Irma and a word of honour

Human solver: Tomáš Pavuk

**Status: deciphered sign by sign, with two isolated words not understood. Independent review 1 verdict REVISE; all findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1282 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1282), portal name cpc_-04-11_HU__HU_Jasz Arokszalas_jolanka-94, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution was found or used.

The cipher text fills the message side of the card in 21 rows of red ink. The address reads Tóth Jolanka, Jászárokszállás. The postmark is Jászárokszállás, apparently 11 April (the portal file name has "-04-11"); the year cannot be read. The picture side has only a printed verse. In the stamp box a short closing stands in plain Hungarian.

The card belongs to a family of Hungarian cipher postcards to Jolánka Tóth in the same hand and the same cipher, signed Feri, several of which are deciphered in this repository (for example HCP 1216, 1243, 1259, 1301). They are love letters in the formal *Ön* address. This card was read with a **known, transferred key**; it is not a new key recovery. The identity of Ilona and Irma, the two women in the news, is not known.

![Message side with the 21 cipher rows (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, printed verse only (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual. The solver read every row on enlarged crops of the un-converted original scan and recorded one token per sign in `work/ledger.txt`. The first row gave *kedves egyetlen reményem* with the family key, which placed the card. The ledger was made with knowledge of the key and the emerging sense, so it is not a blind transcription. `python3 -I ciphers/hcp-1282/work/decode.py`, run from the repository root, checks the hashes of the images, decodes the ledger and prints the plaintext.

In review, a second agent made its own crops and wrote its own shape transcription and decoder. It agreed on most rows and disagreed in eight, which led to the corrections summarized below.

## Key

Monoalphabetic substitution with invented signs; the family key from HCP 1216 is unchanged. The labels describe the handwritten shapes.

| Plain | Sign | Plain | Sign | Plain | Sign |
|---|---|---|---|---|---|
| a | two bars | i | dotted crossed curve | r | F-like sign |
| b | six | j | inverted T | s | right bowl |
| c | left bowl | k | section mark, like a cursive S | t | gamma |
| d | long + short stroke | l | wave | u | x-cross |
| e | three bars | m | three strokes | v | chevron |
| f | cross | n | two strokes | y | low descender |
| g | open loop with descender | o | cursive loop | z | crossed diagonal |
| h, p | tall stroke + companion | gy | joined sign | | |

Dots and ticks on o and u give ö, ü, ő. On this card a plain cross stands twice where the sense needs j (*újság*, *gondoljön*). The capital of *Ilona* and *Irma* is either a clear cursive I or the family y sign used as a capital. Three short free strokes and one blob stand at sentence breaks and carry no letter; they are shown as `|` and `·` below.

## Plaintext

Literal decipherment, row by row. `[t]` and `[e]` are restored under an ink blot.

```text
01 kedvesegyetlenremenyem        12 lökeajövőtitka·a
02 kivanomhogyalegjobb           13 miminketiletmaskülöm
03 kedvebentalaljaso             14 benegessegekvagyunk|en
04 raimhogytelikideje            15 dezintulboldognaker
05 miujsagönnökfelemi            16 zemmagammertbizel
06 köztünknagyvaltozas           17 metbiromonnekedesem
07 törtent|Ilonaholnap           18 becsületszavamadomiras
08 megyvarnielőszörvar           19 banishogynemrbennemis[t][e]n
09 iegyelokelövarroda            20 veleedesemgondoljön
10 ba|Irmapedigmasamod           21 neharamakiönreepedőszivvelgondol
11 leszhogymileszbelő
```

### Hungarian (normalized)

Kedves egyetlen reményem! Kívánom, hogy a legjobb kedvében találja soraim. Hogy telik ideje? Mi újság önnök felé? Mi köztünk nagy változás történt. Ilona holnap megy varrni, először vári {?} egy előkelő varrodába. Irma pedig masamód lesz. Hogy mi lesz belőlök, [ez] a jövő titka. Ami minket illet, máskülömben egészségek vagyunk. Én de [e]zintúl boldognak érzem magam, me[r]t bizelmét bírom Önnek, édesem. Becsületszavam adom írásban is, hogy nem {r} bennem. Is[te]n vele! Édesem, gondoljön néha rám, aki Önre epedő szívvel gondol.

In clear in the stamp box: csókolom számtalanszor hű [word uncertain] Feri.

### English

My dear only hope! I wish that my lines find you in the best of spirits. How is your time passing? What news on your side? Among us a great change has happened. Tomorrow Ilona goes to sew; first [*vári*: not understood] to a distinguished dressmaking workshop. And Irma will be a milliner. What will become of them is the secret of the future. As for us, otherwise we are healthy. But from now on I feel happy, because I have your trust, my sweet. I give my word of honour in writing too, that not [one word missing or not understood; a guess: that you will not be disappointed] in me. God be with you! My sweet, think sometimes of me, who thinks of you with a yearning heart.

Stamp box: I kiss you countless times. Your faithful [word uncertain], Feri.

### Slovak

Moja milá jediná nádej! Želám si, aby Vás moje riadky našli v najlepšej nálade. Ako Vám plynie čas? Čo je nové u Vás? U nás sa stala veľká zmena. Ilona ide zajtra šiť; najprv [*vári*: nerozumieme] do významnej krajčírskej dielne. A Irma bude modistkou. Čo z nich bude, to je tajomstvo budúcnosti. Čo sa nás týka, inak sme zdraví. Ale odteraz sa cítim šťastný, lebo mám Vašu dôveru, drahá. Dávam čestné slovo aj písomne, že nie [jedno slovo chýba alebo mu nerozumieme; odhad: že sa nesklamete] vo mne. S Bohom! Drahá, myslite občas na mňa, ktorý na Vás myslí s túžiacim srdcom.

V rámčeku na známku: Bozkávam Vás nespočetnekrát. Váš verný [slovo neisté], Feri.

## What remains uncertain

- **`hogy nem r bennem` (row 19).** The F-like sign and *bennem* are clear, but the clause has no verb and the sign makes no word. The bracketed sense is a guess from context.
- **`vári` (rows 8–9).** The signs are secure, the word is not understood. It may be a slip for *varni* (the writer's spelling of *varrni* in the same row) or the adjective "of the Vár".
- **`Is[te]n vele` (rows 19–20).** The restoration lies under a pink blot and is probable, not proven. What shows is i, the first part of s, a stem slanting like a t, two bars of an e, and n. *Isten vele* is the usual close of this correspondence. The rejected alternative *is van vele* gives no sense.
- **`varrodába` (rows 9–10).** The d rests on sign class and sense, since d, h and p are near-homographs.
- **`[e]zintúl` (row 15).** The z is a heavy forked stroke and the word needs two emendations; *szintúl* ("likewise") is possible.
- **j from a plain cross** (rows 5 and 20) rests on word sense, as do the h/p and d/n calls in *holnap, pedig, epedő*, the *h* of *néha* and the a of *aki*.
- **Stamp box.** After *hű* the lines are not secure; a word such as *kedvese* or a form of *szerelmes* can be neither confirmed nor excluded.
- Year of the postmark; identity of Ilona and Irma; whether the free strokes are meant as punctuation.

## Review and what changed

An independent reviewer ran the reproduction command, decoded the card from its own transcription and checked contested signs at up to 6× enlargement. Its verdict was REVISE: the key and most of the reading stood, ten findings were raised (four major, six minor), and all were accepted.

- *varrone be* became *varroda|ba*. The review read d and a at the end of row 9. The solver then also corrected the row 10 sign from e to a, because it shows two bars; the review's decoder had kept e there.
- A phantom k in row 14 was removed: *vagyunk. Én*, without the invented "[S] én". The free strokes and the row 12 blob were recorded.
- *is van vele* became the restoration *Is[te]n vele*, so the sentence *hogy nem {r} bennem* now ends before it and the unread part shrank from a clause to one word.
- *vári* lost its invented gloss "she sews" and is now marked not understood.
- The ö/ő marks of *először* were entered; the claim of an unenciphered capital I was softened; *szintúl* was disclosed; the subject of the English close was corrected to the writer; and the stamp box reading was reduced to what is secure.

The key did not change, and the content of the letter is the same.
