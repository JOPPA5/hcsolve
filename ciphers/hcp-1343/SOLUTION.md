# HCP1343 / pc_hcp_24 – Reg ("Reggie boy") to Gertrude Forrest ("Brownie"), Bristol (complete reading)

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1343 (status Not solved, no transcription or solution attached, see `SOURCES.md`). No published solution of this card was found or used. The transcription is my own, made from `work/hires/pc_hcp_24_adr.JPG`.

**Credit:** source capture, key application, transcription and reading by Claude Opus 5.5, 2026-10-30. The cipher and key were first established on the sister card HCP1469 (same correspondents, also Claude Opus 5.5, 2026-10-30; capture and triage of that card by an OpenAI GPT solver). This card uses that key; no earlier work on this number existed.

## Source and context

Picture side: printed "Canterbury Cathedral N.", Noakes & Co., no cipher. Address side: Miss Gertrude Forrest, West Bank, Eastfield Road, Westbury-on-Trym, Bristol, in plain writing, with a halfpenny Edward VII stamp (1902–1910). The machine postmark is fragmentary: town unreadable, a date line reading "… 5 07" whose month strokes are unresolved (portal date Unknown), so I date the card to 1907 only. Faint marks over the printed POST CARD (a B-like shape, a bow right of A, a dashed vertical, a mark right of D) match the broken print of the postmark and not the pen signs; I take them as its town line, not as cipher. The cipher fills the top margin, the left panel and one vertical line along the divider.

## Cipher type and key

English, **monoalphabetic substitution with invented signs**, identical to HCP1469 (found by comparing the recipient and alphabet, then confirmed because the key gives English at once on this card). Words are spaced.

| a | b | c | d | e | f | g | h | i | j | k | l | m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| circle | 3-shape | arch ∩ | right bowl ) | one dot | gamma Γ | 2 dots falling | 2 dots rising | 2 dots vertical | hook ⅃ | angle < | box □ | vertical bar \| |

| n | o | p | q | r | s | t | u | v | w | y |
|---|---|---|---|---|---|---|---|---|---|---|
| caret ∧ | circle with bar θ | bracket with top bar | circle with centre dot | 7-shape | 2-shape | inverted T | T on its side ⊢ | angle > | caret ∧ | caret with stem ↑ |

x and z do not occur. A short raised stroke marks the apostrophe in *won't, haven't, didn't, shouldn't, couldn't* (not in *cant*). **New on this card:** m is the plain vertical bar (`my`, `come`, `more`, `same`, `time`), and q, j, k and p are attested with better resolution than on HCP1469.

## Plaintext (line labels as in `work/transcription.txt`)

```text
B01 my dearest daRling brownie it is now
B02 quarter to twelve and i am in dining
B03 room have come downstairs after
B04 changing into blue suit and packing
B05 my bag have seen ethel and harold
B06 (the latter was awake in bed) they
B07 haven't worried about us will
B08 tell you all the news in letter
B09 reg has to thank brownie dRedful
B10 much for such a happy weekend
B11 he has had a dRedful nice time
B12 reg will forget about last night
B13 if brownie promises too as well and
B14 not to worry about it she has
B15 no need to f[ea]r? reg thinks just
B16 the same as ever
T1  he did of brownie i do hope your movey won't worry you
T2  because we sat in the dark you cant tell her that we didn't
T3  want to and shouldn't have if blinds had been in place
T4  goodbye dearie reg does love you dRedful lot and he couldn't
T5  think more highly of
T6  brownie than he does now and he is always brownies own
T7  reggie boy
S1  best wishes for a decent week at school
```

Capital R = a sign that is not the normal r (uncertainty 1). `f[ea]r?` = an overwritten word read from context (uncertainty 4). Reading order: the body ends at the foot of the panel in mid-sentence ("as ever") and continues in the top margin ("he did of Brownie"), the same layout as HCP1469; the divider line stands apart as a postscript.

**English (punctuated):** My dearest darling Brownie, it is now quarter to twelve and I am in [the] dining room. [I] have come downstairs after changing into [my] blue suit and packing my bag. Have seen Ethel and Harold (the latter was awake in bed); they haven't worried about us. Will tell you all the news in [a] letter. Reg has to thank Brownie dreadful much for such a happy weekend; he has had a dreadful nice time. Reg will forget about last night if Brownie promises too, as well, and not to worry about it. She has no need to fear(?). Reg thinks just the same as ever he did of Brownie. I do hope your "Movey" won't worry you because we sat in the dark. You can't tell her that we didn't want to, and shouldn't have if [the] blinds had been in place. Goodbye dearie. Reg does love you dreadful lot, and he couldn't think more highly of Brownie than he does now, and he is always Brownie's own Reggie boy. Best wishes for a decent week at school.

**Slovensky:** Moja najdrahšia, milovaná Brownie, je tri štvrte na dvanásť a som v jedálni. Zišiel som dolu, keď som sa prezliekol do modrého obleku a zbalil si tašku. Videl som Ethel a Harolda (ten bol hore v posteli); nerobili si o nás starosti. Všetky novinky ti napíšem v liste. Reg musí Brownie strašne ďakovať za taký šťastný víkend; strávil strašne pekné chvíle. Reg zabudne na včerajší večer, ak to Brownie sľúbi tiež a nebude sa tým trápiť. Nemá sa čoho báť(?). Reg si o Brownie myslí presne to isté ako vždy. Veľmi dúfam, že ťa tvoja „Movey“ nebude trápiť pre to, že sme sedeli potme. Nemôžeš jej povedať, že sme to nechceli a že by sme to neboli urobili, keby boli žalúzie na svojom mieste. Zbohom, drahá. Reg ťa strašne veľmi ľúbi a nemohol by si o Brownie myslieť viac než teraz, a je navždy Brownin vlastný chlapec Reggie. Všetko najlepšie do slušného týždňa v škole.

## Reproduce (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1343/work/decode.py
```

It checks the SHA-256 of the two `source/` scans and the two `work/hires/` originals, then decodes `work/transcription.txt` with the key (saved output: `work/decoded.txt`). `STATS: 24 lines, 174 words, 698 sign tokens, unmapped=0`, plus a count of the contextual signs. `unmapped=0` only means every sign has a key value; it does not mean every reading is certain. The pixel-to-sign step is manual; there is no OCR.

## Uncertainties and editorial decisions

1. **Three r-places use another sign.** *dredful* (B09, B11, T4) is written d-caret-e-d-f-u-l, exactly the spelling already seen twice on HCP1469, so it is a habit, not a misreading here; printed with `R`. The caret is also the sign for w, so "dwedful", a baby-talk r→w in keeping with the third-person "Reg" and "Brownie's own Reggie boy", is a possible explanation (hypothesis only; the sense is the same). *darling* (B01) has an arch where r is expected (`d a ∩ l i n g`): literally "dacling". I read it as *darling* by context; this is a single-occurrence slip, and it is an interpretation. The two signs are not a shown r homophone: seven-shape r is used everywhere else.
2. **n / w share the caret.** A hooked form tends to n and a plain one to w, but not reliably (the n of *nice* is plain), so as on HCP1469 w is contextual (`V=w`, 28 times). Each such word has only one sensible reading.
3. **"movey" (T1)** is read sign by sign as m-o-v-e-y, with clear pixels. I do not know what it means. As *her* follows, I take it as a nickname of a woman who might object (a mother or a housemate). A reading such as "mother" is excluded by the signs. Left literal.
4. **"fear" (B15, printed `f[ea]r?`) is the weakest word on the card.** It has three signs (crop: `work/b15-word.png`): a clear gamma (f); a round sign with a heavy stroke at its right side, which is not the barred o and shows no e dot; and a seven-shape (top stroke overshooting left, stem below the line) with a small circle inside it, so an r written over or corrected from a circle. No box, hence no l. The letters e and a are not literally legible: *fear* is a contextual reading that needs an e lost or absent and the second sign taken as a corrected a. It fits the reassuring passage and needs no inserted subject before *thinks*. The first reading, "fool", was withdrawn in review 1.
5. **"no" (B15).** The first word is heavily blotted with a smear underneath; a caret and a blotted circle are visible. *not* above it (B14) also has a blotted circle. Read from the visible shapes.
6. **Dots.** e, g, h, i are dots only; every group was checked on 3–5x crops for count and slant. *dining* in B02 ends in the two dots of g, the second one elongated; it is not a hyphen. *Ethel* starts with a dark diamond dot (e).
7. **Omissions** are the writer's own; bracketed words in the translation are not on the card ("I", "the", "a", "my"). The underlining of *do, has, just, couldn't*, the *dredful*s and others is his emphasis and is not reproduced in the plaintext.
8. **"they haven't worried about us" (B07)** and the persons "Ethel and Harold", "her" and "she": their identity is not known. *she* in B14 I take as Brownie in the third person, matching "Reg" for himself. Date and place of writing are not stated.

## Why I believe it is correct

- The key of HCP1469, a card to the same recipient, plus the plain bar for m, gives 174 words of continuous, grammatical, period-plausible English. Every sign has a key value, but four r-places (uncertainty 1) and the word in uncertainty 4 are contextual.
- Internal repeat evidence: *brownie* occurs 5 times, *reg* 4, *dredful* 3, same spellings; *dredful*, and *reg* writing of himself in the third person, also match HCP1469, as do the signature and the layout (body then top margin).
- The text fits the card: a young man leaving at near midnight after a weekend with Brownie, sent to Bristol.

## Response to review 1

Verdict REVISE. All four findings are addressed; no other word changed. `python3 -I ciphers/hcp-1343/work/decode.py` was re-run: hash check passes, output saved to `work/decoded.txt`, 698 sign tokens (699 before, as the word has three signs, not four).

1. **"fool" – accepted and fixed.** On my own look at the enlargement of the original (`work/b15-word.png`) the third sign has the overshooting top stroke and the descending stem of the seven-shape, with a small circle inside; it is not a box. The transcription now gives `F @=[ea] 7@=r?`, the plaintext prints `f[ea]r?`, and the English and Slovak were changed, removing the inserted "[he]". `decode.py` counts both signs as contextual. Uncertainty 4 is rewritten.
2. **"without any adjustment" – accepted and fixed.** The claim now reads "the key of HCP1469 plus the plain bar for m" and names the contextual places. `decode.py` prints `unmapped=0` instead of `unknown=0`, with a note on what that means.
3. **Caret in *dredful* – accepted.** The "dwedful" baby-talk hypothesis is added to uncertainty 1 as a hypothesis. The plaintext stays `dRedful`, as the sense does not change. *dacling* stays a one-off.
4. **Postmark and printed area – accepted and fixed.** The faint marks over POST CARD are recorded under Source and context; the date is given as "1907" only and the month as unresolved. I agree with the reviewer that the weekday reasoning gives no safe month.
