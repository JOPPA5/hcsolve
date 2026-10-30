# HCP 1787 (pc_hcp_468): a Czech soldier's card from Čáslav to Mařenka Pařezová

Human solver: Tomáš Pavuk

**Status: key established and message read except for three words; two further words are read sign by sign but not identified. Independent review 1 verdict REVISE; all findings addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1787 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1787), portal name pc_hcp_468, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, category Substitution, date Unknown, language Czech, location Europe, sender Unknown, recipient Maruška Pařezová, with no transcription or solution attached.

It is a picture postcard printed by Ferd. Bucek in Čáslav, showing "Zámek Filipovský" (Filipov castle), Čáslav. Cipher text fills the left half of the address side and continues at the top and bottom of the picture side. The address is in clear: **Známé slečně / sl. Mařence Pařezové / Dobřeň / p.p. Suhdol** (the writer's spelling of Suchdol). Dobřeň is a part of Suchdol in the Kutná Hora district, close to Čáslav. Two postmarks are present: ČÁSLAV, partly under the 5-heller stamp, and SUKDOL with the year **06**. Day and month of both are unread, so the card dates from 1906, and "May" comes from the text alone.

The sender signs **Otta** in clear. He is a soldier stationed at Čáslav; his identity is not established. Sister card HCP 1786, to the same recipient, uses a closely similar system. That the two have one sender is a hypothesis.

![Picture side, with cipher text above and below the view (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side, with the main cipher text at the left (source/address-large.jpg)](../source/address-large.jpg)

## Method

The whole work was done by Claude Opus 5.5; there was no earlier work on this number and no sister key to transfer. The transcription is manual, from enlarged crops of the un-converted originals. There was no OCR.

The key was cracked by hand. The opening groups gave jsem, sem and jest; a later group gave "se těším". From these came dash = e, dot = i/y, slash = o, two dots = u, and the merging of t/d, p/b and h/ch. Then a heavy pen stroke turned out to mean a, and the ring sign solved "Maďar". The key was fixed by those independent words and then predicted the rest.

The script `work/decode.py` checks the hashes of the scans, decodes the transcription into a mechanical literal, and tests each reading strictly: a reading may add only an unwritten a/á. Words that fail are pinned as disclosed exceptions. It does not read the images.

Reproduce from the repository root:

```sh
python3 -I ciphers/hcp-1787/work/decode.py
```

## Key

A home-made Czech substitution, close to an abugida: each consonant has one sign, and a vowel is shown by marking that sign. Spaces are real word gaps.

| Sign | Value | Sign | Value |
|---|---|---|---|
| 0 | l | 8 | h, ch |
| 1 | t, d (caron ť, ď; ring ď) | 9 | k |
| 2 | n | v | v |
| 3 | m | x | z (caron ž) |
| 4 | r (caron ř) | ζ | j |
| 5 | s (caron š) | c | c, č |
| 6 | p, b | crossed S (once) | s |

Vowels: dash = e; dash with caron = ě; mid dot = i, í, y, ý; two dots = u, ů; slash through the sign = o; heavy stroke on the sign = a, á. Initial vowels have their own signs: a, σ (o), U (u). The heavy stroke and the carons are often omitted. The signature Otta, "½ 7 hod" and so the digit 7 are in clear.

## Plaintext

Reading order: address side, then the top of the picture side, then its bottom. Punctuation and capitals are editorial, apart from the written question marks. [?] marks unread signs, and square brackets around a word mark a guess.

**Jest neděle ½ 7 hod ráno, odešel jsem z kasáren do parku „Vodranty". Jak krása zde za tak krásného májového jitra. Vzpomínám si na vás, milovaná Mařenko, a na drahý domov. Jak rád bych se byl podíval domů, ale náš hejtman, prokletý Maďar, nedovolil ani jednoho, že jsme sem přišli na tři neděle, a když nám dá jednou až za týden, to toho máme dosti. Tak se těším, zdali bychom se mohli vidět? Nechodíte na Pon[á]vlink? Vrozděři jste také nebyla ještě letos? Sedím na lavce a píšu: přijeďte sem ve středu k tetice? Jak šťasten bych byl, kdybych vás viděl po boku svým. U tohoto zámku je celý [?]k, děláme každý den velké marše, že každý si naříká, že ho bolejí nohy, [?]ebe, až bude [?čtvrtá] neděle. Srdečně vás zdraví, pac a pusu posílá váš Otta.**

English translation: **It is Sunday, half past six in the morning; I left the barracks for the "Vodranty" park. What beauty here on so lovely a May morning. I think of you, beloved Mařenka, and of my dear home. How gladly I would have gone home for a visit, but our captain, a damned Magyar, did not allow a single one, since we came here for three weeks, and when he gives us [leave?] just once in a week, we have enough of that. So I am looking forward to whether we could see each other? Do you not go to Pon[á]vlink? Have you not been at Vrozděř this year either? I sit on a bench and write: come here on Wednesday to your aunt's? How happy I would be if I saw you by my side. By this castle there is a whole [?]; every day we do long marches, so that everyone complains his feet hurt, [?], when it is [?the fourth] week. Warm greetings to you; a handshake and a kiss from your Otta.**

Slovak translation: **Je nedeľa, pol siedmej ráno, odišiel som z kasární do parku „Vodranty". Aká krása je tu za takého krásneho májového rána. Spomínam si na vás, milovaná Marienka, a na drahý domov. Ako rád by som sa bol pozrel domov, ale náš kapitán, prekliaty Maďar, nedovolil ani jednému, lebo sme sem prišli na tri týždne, a keď nám dá raz až za týždeň, toho máme dosť. Tak sa teším, či by sme sa mohli vidieť? Nechodíte na Pon[á]vlink? Vo Vrozděři ste tento rok ešte tiež neboli? Sedím na lavičke a píšem: príďte sem v stredu k tete? Aký šťastný by som bol, keby som vás videl po svojom boku. Pri tomto zámku je celý [?], každý deň robíme veľké pochody, takže každý sa sťažuje, že ho bolia nohy, [?], až bude [?štvrtý] týždeň. Srdečne vás pozdravuje, podáva ruku a bozk posiela váš Otta.**

Notes on the reading: **hejtman** is the army rank of captain. **neděle** means both Sunday and, colloquially, week; the card uses both. **Vodranty** is a forest park in Čáslav, and the name decodes mechanically. "U tohoto zámku" points at the castle printed on the card. **Bolejí** is a colloquial form of bolí.

## Uncertainties

- **Three unread words.** `?9` ("celý [?]k") has an overwritten blot as first sign. `?-6-` ("[?]ebe") has a first sign under print specks: possibly 2 ("nebe", no sense), while "lépe" would suit the sense but needs a 0 the pixels do not show. `?1_0v41_` before "neděle" has a scribbled first sign; "čtvrtá" is a sense guess, modestly supported by "na tři neděle", and the signs do not fit it cleanly.
- **Two unidentified words.** "Pon[á]vlink" (literally ponvlynk, the á is guessed) and "Vrozděři" (perhaps a locative, or "v Rozděři") look like place names; neither is verified.
- **"nedovolil".** The crossed 8 gives literal "nedoholil"; the reading rests on sense.
- **Heavy stroke not fully clean.** In jsme, děláme and vidět it is not a. Heavy or plain was judged by eye.
- **Other writer's departures.** "mohli" is written with u-dots; "hejtman" has no e; "středu" has no r; "že" in "že ho" has no dash; "to" has a dash that is probably a line-end mark, and the sign is crossed by the watermark. Carons are often omitted.
- **"k tetice"** is written as one word; the split is mine. "[leave?]" is an inference: what the captain gives is not stated.
- **Merged values.** t/d, p/b and h/ch are not distinguished, so those letters rest on word sense, as do unmarked a/á. "posílá" is read from faint signs.
- **Date.** Day and month of the postmarks are unread. Identity of Otta is unknown. No published solution was seen, and the portal attaches none.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. It retranscribed all words from its own crops of the originals and decoded them with its own stricter script. It confirmed the key and the overall reading, and the 56 heavy marks against 67 a/á. What changed because of the review:

- **Vodrant became Vodranty.** A thin slash through the v and a final dot had been missed, so the literal is now exactly the place name and one disclosed exception went away.
- **"na dráhy domov" became "na drahý domov"** ("my dear home" instead of "roads home").
- **"a až bude" became "až bude".** The second a was never written; the old check had let it through.
- **Vrozděř became Vrozděři**, with a final dot.
- **Smaller corrections.** A question mark after "vidět"; the hook of "středu" is on the dash; the i of "přijeďte" is present; ring means ď alone; "přišli" reads with a dot, so it is no longer an exception.
- **Address and year added** from the clear address and the SUKDOL postmark.
- **Check tightened** in decode.py so only an unwritten a may be added; nine exceptions are pinned and disclosed.
- **Status wording** changed from "whole message read", and "[?regiment]" removed from the translation as unsupported.

One small difference remains: the reviewer wrote of a caron on the 4 in "přijeďte"; the solver sees none there or in "přišli", only the single mark after it. The reading is unaffected. The reviewer judged no second round necessary for these corrections, and the three unread words did not change.

## Sources

- HC Portal record 1787, all three tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1787 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/5421/pc_hcp_468_pic.JPG; address side: https://api.hcportal.eu/media/5422/pc_hcp_468_adr.JPG.
- Vodranty, Čáslav: https://en.wikipedia.org/wiki/Stadion_pod_Hr%C3%A1dkem and https://dspace.cuni.cz/bitstream/20.500.11956/35983/1/DPTX_2010_2__0_296114_0_107453.pdf
- Dobřeň, Suchdol: https://en.wikipedia.org/wiki/Suchdol_(Kutn%C3%A1_Hora_District)
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30 by the orchestrator: no record.
