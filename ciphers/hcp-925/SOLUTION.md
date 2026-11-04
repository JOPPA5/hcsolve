# hcp-925 - Solution (round 1)

Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. No earlier work on this number; no published solution found
(portal status Not solved, no attached transcription or solution; a short web search found nothing for this card).
The portal has no transcription: the transcription in `work/transcription.txt` is my own, read from the
un-converted original `work/hires/cpc_1903-05-03_DE_Wollstein_DE_Volsheim__pic.jpg` at 2.5-3x enlargement.

## Card
Embossed greeting card "Der Ferne ein Gruss" (printed). Address side: Herrn Heinrich Lechtahler, Wohlgeboren,
Volxheim in Rh(einhessen); German 5 Pf Germania stamp, postmark W...STEIN, 3 (May 1903 per the portal file name);
the postmark place is most likely Wöllstein (Rheinhessen), the neighbouring village of Volxheim, not Wollstein in Posen
(portal file name says "Wollstein"; this is my inference from geography and the address, not read in full).
The whole message is on the picture side, written as dotted groups of numbers.

## Cipher type and key
Simple monoalphabetic number substitution (register label: MASC), letter = its position in the 25-letter German
alphabet without J:

    A1 B2 C3 D4 E5 F6 G7 H8 I9 K10 L11 M12 N13 O14 P15 Q16 R17 S18 T19 U20 V21 W22 X23 Y24 Z25

No word dividers; Umlaut letters written without dots (U for Ü, A for Ä). Numbers used: 1-14, 17-20, 22, 25.
The key was found from the groups 11.9.5.2.11.9.13.7 = LIEBLING, 4.5.9.13 = DEIN, 18.5.13.4.5.19 = SENDET
and then holds for every group on the card.

## Command (run from repo root; checks source SHA-256 hashes, then decodes the whole transcription)

    python3 -I ciphers/hcp-925/work/decode.py

Output (decoded lines): ZUMGEBUTSTAGE / ALSICHHEUTEFRUHERUHERWAC + (circled) HTE / UNDANMEINENLIEBLINGDACHTE /
FIELMIRDERGEDANKEEIN / HEUTMUSSEINGEBUTSTAGSEIN / SENDET / DEIN / LIEBLING / KATCHENHOTTUM

## Plaintext (German, as written, word-divided)
Zum Gebu(t)tstage! Als ich heute früh(er) [uher] erwachte und an meinen Liebling dachte, fiel mir der Gedanke ein:
heut muss ein Gebu(t)tstag sein. Sendet dein Liebling Kätchen Hottum.

Normalised German:
Zum Geburtstage! Als ich heute früh erwachte und an meinen Liebling dachte, fiel mir der Gedanke ein:
Heut muss ein Geburtstag sein. [Es] sendet [dies] dein Liebling Kätchen Hottum.

English: For your birthday! When I woke up early this morning and thought of my darling, it occurred to me:
today must be a birthday. Sent by your darling Kätchen Hottum.

Slovak: K narodeninám! Keď som sa dnes ráno zobudila a myslela na svojho miláčika, prišlo mi na um:
dnes musia byť narodeniny. Posiela tvoj miláčik Kätchen Hottum.

## Uncertainties (all disclosed)
1. "Geburtstag" is enciphered both times as 7.5.2.20.**19**.18.19.1.7(.5) = GEBUTSTAG(E): the sign after U is
   clearly 19 (T), not 17 (R), in both places (compared at 3x with the writer's 17 = "1" + crossed 7 and 19 = "1" +
   looped 9). This is the writer's own consistent slip (or skipped R); I read the word as Geburtstag on word sense.
2. Line 1 reads 6.17.20.8.5.17.20.8.5.17.22.1|3 + circled 8.19.5 = FRUHERUHERWAC + HTE. The segment "UHER" is
   written twice (dittography); the sense is "früh erwachte" (or "früher erwachte" with stray "UH"). All digits
   are clear; only the word division/emendation rests on word sense. The meaning is the same either way.
3. At the end of line 1 the last two digits are written "13" without a visible dot between them; I read 1.3 (A, C)
   because 13 (N) gives "ERWN" and the circled continuation 8.19.5 (HTE) then completes "ERWACHTE". This call
   rests on word sense; it is marked "1|3" in the transcription.
4. The circled 8.19.5 under the end of line 1 is read as the continuation of that line (no room left on the line).
5. Writer's 19 and 14 look alike in places: in "DACHTE" (line 2) the group I first took for 14 is 19 on enlargement
   (8.19.5 = HTE). In the signature the sign after 8 is "1" + open 4 (as in the writer's 4 in 7.4.1.3) = 14 = O.
6. Signature 10.1.19.3.8.5.13 8.14.19.19.20.12 = KATCHEN HOTTUM: first name Kätchen (Käthchen); surname read
   literally as Hottum. The last 12 has a trailing flourish; read 12 (M). The O (14) is partly under the portal
   watermark but visible. The name is reported literally; I could not verify it.
7. Address side: the lower Kurrent line under "in Rh." (a single word, probably a postal/district indication) is not
   securely read; it is plain writing, not ciphertext, and does not affect the message. Recipient name and Volxheim
   are read from the address; "Lechtahler" follows the portal.
8. Steganography check: I inspected the stamp box, the picture-side edges and the printed verse; no hidden or
   reversed writing is visible. The stamp is still on the card, so whatever might be under it cannot be seen on the
   scans; I cannot exclude a hidden note there.

## Why I believe it is correct
- One fixed, natural key (alphabet order without J) decodes every one of the ~140 groups on the card; no group is
  left over and no number needs a second meaning.
- The result is fluent, period-typical German birthday wishes from a sweetheart, matching the card type
  ("Der Ferne ein Gruss", forget-me-nots, love verse) and the address to a man.
- The only irregularities are two transparent writer slips (GEBUTSTAG twice, doubled UHER) and one missing dot,
  all disclosed above.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) verdict ACCEPT, four minor findings. The decoded reading is unchanged;
`python3 -I ciphers/hcp-925/work/decode.py` was re-run on 2026-11-03 after this response: all hashes OK, output
identical to the lines above.

1. Unread address word (minor) - addressed as far as the scan allows. New hi-res crop `work/crops/addr_low_hr.png`
   (from `work/hires/..._adr.jpg`, box 1350,1700-2200,2000). Line 1 is "in Rh." (Rheinhessen). The word below is
   Kurrent with a looped descender and a final ß-shape, roughly "Rh...heß"; a tentative reading is "Rheinheß."
   (Rheinhessen again, written out), but the middle letters do not resolve securely, so it stays marked as unread.
   It is a single word of plain address writing and does not touch the message.
2. Postmark evidence (minor) - fixed. New crop `work/crops/postmark_hr.png`: the ring shows "W..." at the left,
   the date "3" with "5" (May) in the centre, and "...HESS..." (Rheinhessen) at the bottom. This supports the
   identification Wöllstein (Rheinhessen), the village next to Volxheim, rather than Wollstein in Posen; the
   town name itself is still not legible in full and the portal file name "Wollstein" is kept as given.
3. Address abbreviation (minor) - fixed in the report. New crop `work/crops/addr_top_hr.png`: before "Heinrich"
   the writer has two looped capitals, best read as "S. H." or "Sr. H.", evidently an honorific abbreviation of the
   "Herrn" kind (its expansion is not certain); I give it as written ("S. H. Heinrich Lechtahler, Wohlgeboren") and do not expand it further.
4. Cipher type and under-stamp area (minor) - agreed. Register type MASC (number substitution). No hidden or
   steganographic text was found anywhere on either scan; the area under the stamp cannot be inspected because the
   stamp is still on the card, and the report says so. (Other collections, e.g. the Jolánka cards, carry hidden
   messages under the stamp; nothing indicates that here, but it cannot be excluded, so the label is not
   "MASC + Steganography".)
