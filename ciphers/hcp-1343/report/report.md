# HCP 1343 (pc_hcp_24): a cipher postcard from "Reggie boy" to Gertrude Forrest ("Brownie")

Human solver: Tomáš Pavuk

**Status: deciphered in full, with one uncertain word. Independent review 1 verdict REVISE; all findings addressed, one word changed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1343 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1343), portal name pc_hcp_24, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date and language Unknown, location Europe, sender Unknown, recipient Gertrude Forrest, with no transcription or solution attached. No published solution of this card was found or used.

The picture side is a printed view, "Canterbury Cathedral N." (Noakes & Co.), with no cipher. The address side reads in plain writing: **Miss Gertrude Forrest, West Bank, Eastfield Road, Westbury-on-Trym, Bristol.** It carries a halfpenny Edward VII stamp (1902–1910). The machine postmark is fragmentary: the town cannot be read and the date line reads "… 5 07", with the month unresolved. The card can therefore be dated to 1907 only.

The cipher fills the top margin, the left panel and one vertical line along the divider. Faint marks over the printed POST CARD match the broken print of the postmark, not the pen signs, and are taken as its town line, not as cipher.

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the same correspondence as HCP 1469 (London to Bristol, 11 November 1907), which has the same recipient, hand, signature and layout, and which first established the key.

## Method

The recipient's name led to HCP 1469, and its key gave English at once. This is therefore a **transferred key**, not a new key recovery.

The transcription is manual. Every line was read sign by sign on 3–5× enlarged, deslanted crops of the un-converted original scan (1785 × 1175 px); there is no OCR. Dots needed the most care, because e, g, h and i are written as dots only and differ by count and slant.

The body comes first and ends at the foot of the left panel in mid-sentence ("as ever"). The sentence continues in the top margin ("he did of Brownie"), the same layout as HCP 1469. The divider line stands apart as a postscript.

The reproduction command checks the hashes of the scans and decodes the transcription with the key (`python3 -I ciphers/hcp-1343/work/decode.py`). Result: 24 lines, 174 words, 698 sign tokens, every sign with a key value.

## Key

English, monoalphabetic substitution with invented signs. Words are spaced.

| a | b | c | d | e | f | g | h | i | j | k | l | m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| circle | 3-shape | arch ∩ | right bowl ) | one dot | gamma Γ | 2 dots falling | 2 dots rising | 2 dots vertical | hook | angle < | box □ | vertical bar |

| n | o | p | q | r | s | t | u | v | w | y |
|---|---|---|---|---|---|---|---|---|---|---|
| caret ∧ | circle with bar θ | bracket with top bar | circle with centre dot | 7-shape | 2-shape | inverted T | T on its side | angle > | caret ∧ | caret with stem |

The letters n and w share the caret. A hooked form tends to n and a plain one to w, but not reliably, so w is decided from context (28 places); each such word has only one sensible reading. x and z do not occur. A short raised stroke marks the apostrophe. The key is that of HCP 1469, with the plain bar as the form of m.

## Plaintext

Capital R marks a sign that is not the normal r. `f[ea]r?` marks the uncertain word.

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

## Translation

**English (punctuated):** My dearest darling Brownie, it is now quarter to twelve and I am in [the] dining room. [I] have come downstairs after changing into [my] blue suit and packing my bag. Have seen Ethel and Harold (the latter was awake in bed); they haven't worried about us. Will tell you all the news in [a] letter. Reg has to thank Brownie dreadful much for such a happy weekend; he has had a dreadful nice time. Reg will forget about last night if Brownie promises too, as well, and not to worry about it. She has no need to fear(?). Reg thinks just the same as ever he did of Brownie. I do hope your "Movey" won't worry you because we sat in the dark. You can't tell her that we didn't want to, and shouldn't have if [the] blinds had been in place. Goodbye dearie. Reg does love you dreadful lot, and he couldn't think more highly of Brownie than he does now, and he is always Brownie's own Reggie boy. Best wishes for a decent week at school.

**Slovensky:** Moja najdrahšia, milovaná Brownie, je tri štvrte na dvanásť a som v jedálni. Zišiel som dolu, keď som sa prezliekol do modrého obleku a zbalil si tašku. Videl som Ethel a Harolda (ten bol hore v posteli); nerobili si o nás starosti. Všetky novinky ti napíšem v liste. Reg musí Brownie strašne ďakovať za taký šťastný víkend; strávil strašne pekné chvíle. Reg zabudne na včerajší večer, ak to Brownie sľúbi tiež a nebude sa tým trápiť. Nemá sa čoho báť(?). Reg si o Brownie myslí presne to isté ako vždy. Veľmi dúfam, že ťa tvoja „Movey“ nebude trápiť pre to, že sme sedeli potme. Nemôžeš jej povedať, že sme to nechceli a že by sme to neboli urobili, keby boli žalúzie na svojom mieste. Zbohom, drahá. Reg ťa strašne veľmi ľúbi a nemohol by si o Brownie myslieť viac než teraz, a je navždy Brownin vlastný chlapec Reggie. Všetko najlepšie do slušného týždňa v škole.

## Uncertainties

1. **"fear" (B15) is the weakest word.** The word has three signs: a clear gamma (f); a round sign with a heavy right stroke, which is neither the barred o nor an e dot; and a seven-shape with a small circle inside it, so an r written over or corrected from a circle. The letters e and a are not literally legible. "Fear" is a contextual reading.

![Line B15: "no need to" and, as the last group on the right, the overwritten word (work/b15-word.png)](../work/b15-word.png)

2. **Four r-places use another sign.** *dredful* (three times) has a caret where r is expected. The same spelling occurs on HCP 1469, so it is a habit. As the caret is also w, a baby-talk "dwedful" is a possible explanation; this is a hypothesis and the sense is the same. *darling* has an arch and literally reads "dacling"; it is read from context as a single slip.
3. **"movey" (T1)** is clear in the pixels as m-o-v-e-y, and its meaning is unknown. As "her" follows, it may be a nickname of a woman who might object, such as a mother or a housemate.
4. **"no" (B15)** is blotted, with a caret and a blotted circle visible and a smear below.
5. **Persons.** The identity of Ethel, Harold and "her" is unknown. "She" in B14 is taken as Brownie in the third person, matching "Reg" for himself, but this is not proven.
6. **Postmark.** Town and month are unresolved.
7. **Omissions** are the writer's own. Bracketed words in the translation are not on the card. His underlining is not reproduced.

## Review and what changed

An independent Claude Opus 5.5 reviewer ran the command, decoded with its own script and key table (identical output), and read every line of the original scan sign by sign. The cipher, key and reading stood, except for one word. Verdict: REVISE.

1. **Major: "fool" (B15) was forced.** The solver had given four signs, F-o-o-l, with a box at the end. The third sign is a seven-shape with a circle inside, not a box, and the word has three signs. Fixed: the transcription now records what is seen, and the word is printed `f[ea]r?`. The sentence changed from "She has no need to fool Reg; [he] thinks…" to "She has no need to fear. Reg thinks…", which removes an inserted word.
2. **Minor: "without any adjustment" was overstated.** The claim now names the plain bar for m and the contextual places; the decoder's "unknown=0" became "unmapped=0".
3. **Minor: the "dwedful" alternative was undisclosed.** It is now stated as a hypothesis.
4. **Minor: postmark and printed area.** The marks over POST CARD are recorded and the date is limited to 1907.

The reviewer could not verify the meaning of *movey*, the identity of the people, the postmark month and town, or that "fear" is the intended word.

## Credit

Source capture, transcription and reading of this card by Claude Opus 5.5 (2026-10-30). Key from HCP 1469 (Claude Opus 5.5; capture and triage of that card by an OpenAI GPT solver). Review by a separate Claude Opus 5.5 agent.
