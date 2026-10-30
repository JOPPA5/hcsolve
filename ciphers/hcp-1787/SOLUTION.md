# hcp-1787 (pc_hcp_468) - solution, round 1, corrected after review 1

Solver: Claude Opus 5.5, 2026-10-30. No earlier work on this number. No published solution was seen; the portal attaches none. Own transcription from `work/hires/` (the portal has no transcription). Status: key established; message read except for three words (`?9`, `?-6-`, `?1_0v41_`), and two more words read sign by sign but not identified (Ponvlink, Vrozděři). See Uncertainties.

## Cipher and key

Home-made Czech substitution, close to an abugida: each consonant has one sign, and a vowel is shown by marking that sign. Spaces are real word gaps. Reading order: address side, top of the picture side, bottom of the picture side. The signature "Otta", "½ 7 hod" (and so the digit 7) are in clear.

| Sign | Value | Sign | Value |
|---|---|---|---|
| 0 | l | 8 | h, ch |
| 1 | t, d (1 with caron: ť, ď; 1 with ring: ď) | 9 | k |
| 2 | n | v | v |
| 3 | m | x | z (with caron: ž) |
| 4 | r (with caron: ř) | ζ | j |
| 5 | s (with caron: š) | c | c, č |
| 6 | p, b | crossed S (once) | s |

Vowels: dash = e; dash with caron = ě; mid dot = i, í, y, ý; two dots = u, ů; slash through the sign = o; heavy pen stroke on the sign = a, á. Initial vowels have own signs: a, σ (o), U (u). A ring on 1 gives ď (Maďar, přijeďte). The heavy stroke is often missing, so a/á may be unmarked; in Maďar the second a is simply unmarked.

## Reproduce

From the repo root: `python3 -I ciphers/hcp-1787/work/decode.py`

It checks the SHA-256 of both source scans and both hi-res originals and decodes `work/transcription.txt` sign by sign. The primary output is the mechanical literal. It then prints the reading, which is the typed column of the transcription and not decoder output, and checks each word strictly: a reading may add only an unwritten a/á to the literal (carons folded; t/d, p/b, h/ch, i/y merged). Nine words that fail this are pinned as disclosed exceptions (see Uncertainties); anything else fails with exit 1. The script does not read the images: the transcription is manual.

## Address and date

Address in clear: "Známé slečně / sl. Mařence Pařezové / Dobřeň / p.p. Suhdol" (the writer's spelling of Suchdol). Postmarks: ČÁSLAV (partly under the stamp) and SUKDOL with year 06, clear at 3x; day and month of both are not read. So the card is from 1906; "May" comes from the text only. Dobřeň is a municipal part of Suchdol in the Kutná Hora district (https://en.wikipedia.org/wiki/Suchdol_(Kutn%C3%A1_Hora_District), checked 2026-10-30), not the Dobřeň in the Mělník district. That is close to Čáslav and fits "podíval domů".

## Plaintext (punctuation and capitals added)

Jest neděle ½ 7 hod ráno, odešel jsem z kasáren do parku „Vodranty". Jak krása zde za tak krásného májového jitra. Vzpomínám si na vás, milovaná Mařenko, a na drahý domov. Jak rád bych se byl podíval domů, ale náš hejtman, prokletý Maďar, nedovolil ani jednoho, že jsme sem přišli na tři neděle, a když nám dá jednou až za týden, to toho máme dosti. Tak se těším, zdali bychom se mohli vidět? Nechodíte na Pon[á]vlink? Vrozděři jste také nebyla ještě letos? Sedím na lavce a píšu: přijeďte sem ve středu k tetice? Jak šťasten bych byl, kdybych vás viděl po boku svým. U tohoto zámku je celý [?]k, děláme každý den velké marše, že každý si naříká, že ho bolejí nohy, [?]ebe, až bude [?čtvrtá] neděle. Srdečně vás zdraví, pac a pusu posílá váš Otta.

## English

It is Sunday, half past six in the morning; I left the barracks for the "Vodranty" park. What beauty here on so lovely a May morning. I think of you, beloved Mařenka, and of my dear home. How gladly I would have gone home for a visit, but our captain, a damned Magyar, did not allow a single one, since we came here for three weeks, and when he gives us [leave?] just once in a week, we have enough of that. So I am looking forward to whether we could see each other? Do you not go to Pon[á]vlink? Have you not been at Vrozděř this year either? I sit on a bench and write: come here on Wednesday to your aunt's? How happy I would be if I saw you by my side. By this castle there is a whole [?]; every day we do long marches, so that everyone complains his feet hurt, [?], when it is [?the fourth] week. Warm greetings to you; a handshake and a kiss from your Otta.

## Slovensky

Je nedeľa, pol siedmej ráno, odišiel som z kasární do parku „Vodranty". Aká krása je tu za takého krásneho májového rána. Spomínam si na vás, milovaná Marienka, a na drahý domov. Ako rád by som sa bol pozrel domov, ale náš kapitán, prekliaty Maďar, nedovolil ani jednému, lebo sme sem prišli na tri týždne, a keď nám dá raz až za týždeň, toho máme dosť. Tak sa teším, či by sme sa mohli vidieť? Nechodíte na Pon[á]vlink? Vo Vrozděři ste tento rok ešte tiež neboli? Sedím na lavičke a píšem: príďte sem v stredu k tete? Aký šťastný by som bol, keby som vás videl po svojom boku. Pri tomto zámku je celý [?], každý deň robíme veľké pochody, takže každý sa sťažuje, že ho bolia nohy, [?], až bude [?štvrtý] týždeň. Srdečne vás pozdravuje, podáva ruku a bozk posiela váš Otta.

## Uncertainties

Unread (no reading is offered as fact):
1. `?9` in "celý [?]k": first sign is an H-shaped overwritten blot. "pluk" has no support from the pixels and is dropped from the translations.
2. `?-6-` ("[?]ebe"): first sign is under print specks. Its base may be a 2 ("nebe"), which gives no sense; "lépe, až bude…" (better when…) would suit the sense but needs 0, which the pixels do not show. Unsolved.
3. `?1_0v41_` before "neděle": a scribbled sign, heavy 1, a tall oval partly under the watermark (0 or c), v, 4, heavy 1. "čtvrtá" is a sense guess, supported modestly by "na tři neděle" earlier; the order of signs does not fit it cleanly.

Read but not identified:
4. "Pon[á]vlink" (`6/2v0.29`, literal "ponvlynk"): the á has no heavy stroke and is my guess. "Vrozděři" (`v4/x1-^4^.`) looks like a locative; a split "v Rozděři" is a hypothesis, and no such place is verified.
5. "k tetice" is written as one word `91-1.c-` then "?"; "k tetice" is my reading.
6. "dá" and what is given (leave?) are not stated; "[leave?]" is an inference.

Disclosed exceptions in decode.py (literal does not fit under the strict test):
7. "nedovolil": 8/ gives "ho", so literal "nedoholil". The crossed 8 is really there; the reading rests on sense, and 8 elsewhere is always h/ch.
8. "jsme" (heavy ζ), "děláme", "vidět" (heavy or blotted 1): the heavy stroke here is not a. Pen pressure is not a perfectly clean signal, and heavy or plain was judged by eye.
9. "mohli": written with two dots, the sign that otherwise means u.
10. "to": written `1/-` at line end; the dash is probably a line-end mark, and the watermark crosses this sign, so the sign is less sure than the others.
11. "hejtman" has no e (`8z13_2`); "středu" has no r (`51-^1:`, literally stědu); "že" in "že ho" has no dash.

Other points:
12. Carons and accents are often omitted: no caron is visible on 4 or 5 in "přišli", on 4 in "přijeďte", on 5 in "marše" and "váš". The dot after "jednoho" is treated as punctuation. "posílá" is read from faint signs (`6/5.0_`), with slash and dot barely visible.
13. Sign values t/d, p/b and h/ch are merged, so those letters rest on word sense. Sense also supplies unmarked a/á.
14. Day and month of the postmarks are unread.

## Why I believe it

Nearly every word decodes to ordinary Czech under one small key, and the words join into a coherent soldier's letter. "Mařenko" matches the address (Mařence Pařezové), "kasáren", "hejtman" and "marše" fit a soldier, and "u tohoto zámku" matches the printed Filipov castle view from Čáslav. The Vodranty park is a local name that was not assumed in advance, and it decodes mechanically (`v/14_21.`). The key was fixed by independent words (jsem, jest, ještě, že, těším) and then predicted the rest. It is a small-corpus reading; independent review 1 retranscribed all words and confirmed the key and reading, with the corrections below.

Sister card hcp-1786 (same recipient) now has its own SOLUTION.md with a closely similar system: the same consonant digits, slash = o, dash = e, dot = i, two dots = u. There a is left unwritten rather than shown by a heavy stroke. Same sender is a hypothesis; I compared only that file's key.

Credit: Claude Opus 5.5 only.

## Response to review 1

Verdict REVISE. I rechecked the contested places on the reviewer's crops and on my own 4-9x crops of `work/hires/`. All findings are accepted, with one difference in finding 7. `python3 -I ciphers/hcp-1787/work/decode.py` was re-run after the changes: exit 0, 136 tokens, 9 disclosed exceptions, 0 misfits.

1. Vodranty: fixed. The slash through v, heavy 4, plain 1 and final dot are visible; transcription now `v/14_21.`; all three language versions changed; exception removed.
2. drahý domov: fixed in all three languages; the plural note is gone.
3. "a až": fixed. The token is now one word `ax^`, "až bude". No second a is written.
4. Vrozděři: fixed, dot added; the split is offered as a hypothesis only. "Pon[á]vlink" now marks the á as a guess.
5. "vidět?": fixed, question mark added. The same mark is now also recorded after Pon[á]vlink, letos and k tetice.
6. "středu": fixed to `51-^1:`, literally stědu; the key entry is deleted.
7. "přijeďte": partly different. The i is there, and the mark on 1 is the ring, so "ring = ď + a" is deleted. But I see no caron on the 4, only the single mark after it, and likewise in "přišli" (also no caron on 5). So both are now `64.`, without the caron the reviewer's wording implies. This does not change the reading.
8. Address and date: added in a new section, with the year 1906 from the SUKDOL postmark and Dobřeň in the Kutná Hora district. Day and month stay unread.
9. decode.py: fixed. The check now allows only an unwritten a/á, exceptions are pinned as literal-reading pairs, the literal prints first, and the reading is labelled as typed. Under the stricter test "hejtman", "to", "že" and "středu" appear as exceptions too. All are listed.
10. Smaller points: the file and SOLUTION now agree on `91-1.c-` plus "?"; the "two dots" note is gone. "přišli" now reads with dot (`0.`), so it is no longer an exception. The dot after jednoho is recorded as punctuation. "marše" with no caron is listed; I checked the 5 at 4x and the bar over it belongs to the sign. "to" is reworded.
11. Status wording: fixed here and carried to the report.

Unread words: no change. "[?regiment]" and "[?pluk]" are removed. The reading of those three words did not change, and the other changes are corrections of single words, so per the reviewer's disposition no second round is needed.
