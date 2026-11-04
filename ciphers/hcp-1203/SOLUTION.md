# HCP1203 — Jolánka to Feri (Holecz Ferenc): PARTIAL reading

**Status: PARTIAL. No marker created, no register entry.** Claude Opus 5.5, 2026-11-02. No earlier work on this number. Portal: Not solved, no solution attached; no published solution met.

Cipher: Hungarian monoalphabetic substitution with invented signs, the Jolánka family key (hcp-1216 table and sign classes), written here by Jolánka herself, so with hand variants; see NOTES.md. The transcription is mine (no portal transcription). Layout: block A upright (26 rows), block B with the card turned 180 degrees (8 cipher rows plus one plain row), block C in the stamp frame (7 rows).

**Type note (2026-11-03, Claude Opus 5.5):** cipher type is now **MASC + Steganography**: block C was written in the stamp box and hidden under the stamp, which has since been lifted (see "Stamp-box message (2026-11-03)" below). This card has no register entry (status PARTIAL); none is created.

Command: `python3 -I ciphers/hcp-1203/work/decode.py` (hash check, ledger, working normalization).

Working text, Hungarian: see `work/normalized.txt` (printed by the command).

English gist: Dear Feri, my sweet hope! I got your card, thanks. Your mother was here this week with Ko[p/n]csik and his wife; we heard she was not satisfied with her reception. I received her kindly enough; what displeased her I can guess, I will tell you in person. They will probably write to you first. In a week I will tell all anyway. I am going to Pest on the 28th of this month, and will be at Rákos on Saturday after 7 pm. Do not wait at the Pest station at all, since my siblings will be there and I do not want them to know I told you. State your occupation as it is, railway brakeman. If you watch at Rákos and see me we will go on to Pest together; if free, appear in civilian clothes if you can. [Unread stretch.] Clothes are dear now. / I wrote this card on Friday, had no time to send it; on Sunday I waited all day, in the evening I was at the harvest ball; [someone] from Kaposvár was here, the chaperone was Bözsi's mother. I am going to a wedding, so I will not write this week. My new address: Petőfi utca 16 [...]. / God be with you, darling, till our happy meeting. Greets you your faithful sweetheart Jolánka.

Slovak gist: Milý Feri, moja sladká nádej! Lístok som dostala, ďakujem. Tento týždeň tu bola Vaša matka s Ko[p/n]csikom a jeho ženou; počuli sme, že nebola spokojná s prijatím. Prijala som ju dosť srdečne; čo sa jej nepáčilo, tuším, poviem Vám osobne. Do týždňa Vám všetko poviem. 28. tohto mesiaca idem do Pešti, v sobotu po 7. večer budem na Rákosi. Na peštianskej stanici vôbec nečakajte, lebo tam budú súrodenci a nechcem, aby vedeli, že som Vám to oznámila. Svoje zamestnanie uvádzajte, ako je, železničný brzdár. Ak ma na Rákosi uvidíte, pôjdeme do Pešti spolu; ak môžete, príďte v civilných šatách. [Neprečítaný úsek.] Šaty sú dnes drahé. / Tento lístok som napísala v piatok, nemala som čas poslať ho; v nedeľu som čakala celý deň, večer som bola na vinobraneckom bále; garde robila Bözsina matka. Idem na svadbu, tento týždeň nepíšem. Moja nová adresa: Petőfi utca 16 [...]. / S Bohom, drahý, do šťastného zvidenia. Pozdravuje Vaša verná milá Jolánka.

Unresolved (why partial): A24 "K mibe a G me"; B02 opening; A22 "lesz{gv}ak"; A26 "Hel"; B05 "gub"; B06/07 "jola", "n{y}iszi-ek"; plain row after "16 szám" ("házmerten/ház emeleten?", "ere?kene", "?lozsek", perhaps Olaszék); A16 "He n[?]em" has a blot. Sense-based calls: h/p/d in "de", "ha", "este"; "garnedem" = gardedám; "viszintl atasra", "lapit", "gondolin" with i for o; "teljesiri" = teljesíti; "28" plain digits. Year unknown; the Saturday 28th with a harvest ball would fit Sept 1912 or Oct 1911, not established.

## Stamp-box message (2026-11-03)

Audit by Claude Opus 5.5 on enlarged crops (2x-4x) of `work/hires/cpc_--23_HU__HU_Rakos-Palota-Ujfalu_jolanka-88_adr.jpg`, saved in `work/stamp-2026-11-03/` (box_2x.png, rows0-2_3x.png, row3_4x.png, row4_5_4x.png).

State: the stamp has been **lifted**. Torn green stamp paper and glue stains remain at the lower left, lower edge and right edge of the dashed stamp frame (upper right of the address side). Inside the frame are 7 rows of **cipher signs** in the card's key, no plain Hungarian. This is block C of the ledger (rows C01-C07), which the 2026-11-02 reading already covered; `work/decode.py` already prints these rows, so neither the ledger nor the script was changed.

Literal (ledger C01-C07): `isten vele / edesem a bol / dog viszintl / a tasra / üdvözli Hű / Kdvese / jolanka`

Normalized Hungarian: Isten vele, édesem, a boldog viszontlátásra. Üdvözli hű kedvese Jolánka.

English: God be with you, my darling, until our happy meeting. Greetings from your faithful sweetheart Jolánka.

Slovak: S Bohom, drahý môj, do šťastného zvidenia. Pozdravuje Vás Vaša verná milá Jolánka.

Rechecked on the pixels today: rows 1, 2, 6 and 7 match the ledger sign by sign (row 2 opens with a three-bar e at the frame edge; row 6 opens with the barred ke-sign). What stays uncertain:
- Row 3: the opening "dog" is two or three crowded signs (a long slanted stroke with tick, then a loop with a dot below); they are not cleanly separable, and "dog" rests on the formula "boldog viszontlátásra" carried over from "bol" at the end of row 2. "viszintl" has the writer's undotted loop where sense wants o (viszont-); the final l is not seen as a separate sign after the t, so "viszontl-" is partly a sense reading.
- Row 4: one sign after "át" is covered by an ink blot; "á" is the one letter that makes the word (átásra), so it is a disclosed restoration.
- Row 5: the ü of "üdvözli" sits at the smudged left edge of the frame next to the stamp remnant and is not clearly visible; the rest (d v ö z l i, then h ű) is read.
Nothing else in the box is unread; no clause is missing.

Stamp-box conclusion: hidden message present, in cipher; type MASC + Steganography.
