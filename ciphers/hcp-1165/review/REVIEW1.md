REVISE

# Review 1 of hcp-1165

Reviewer: Claude Opus 5.5, 2026-11-02. The decipherment stands: same key, same 276 signs, same connected Hungarian. Three small readings are wrong against the pixels and the key table merges two signs. No blocker.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1165/work/decode.py`: hashes OK, 276 signs, 266 by table, 10 by sense; output matches the plaintext in SOLUTION.md.
- Limit of that command: it asserts readings after folding u/ú/ü/ű into one value and the unmarked accents together (`FOLD`), and verse/clear text is hard-coded. It therefore cannot see finding 1.
- Independent transcription and decoder: `review/work/verify.py` (own row-by-row reading from the hires scan, own key). Also 276 signs. Raw differences from the solver are only the disclosed sense readings (i/a three times, h/l in lassan, `üplemhaz`, `szolm`, `iübájtol`, `kedveked`, the g-like sign), plus finding 1.
- Crops at 3x and 5x from `work/hires/*adr.jpg`, made by me: `review/work/a0–a4, b1–b4, c0–c4, d1–d4, e1–e2, m1–m4, pm.png`. Every cipher row read sign by sign; all 10 ODD signs viewed at 5x.
- Picture side (`*pic.jpg`) carries no writing, only the portal stamp.
- Key sanity: `4.` gy, `6` j, `6.` ny, `4` f, `1,` b are not new to the family; they recur on sister cards (e.g. hcp-1144, 1153). The solver calls gy/j/ny "new" because it worked from hcp-1174 only; harmless.
- Plaintext judged real Hungarian of the period, spelling habits (semit, single consonants, missing accents) as on the sister cards. Margitka, Mariska (hcp-1178), Ángyika (hcp-1175 notes via hcp-1178), Árpád (hcp-1174) all fit.
- No published solution used as far as I can see; portal has none. The article was not checked, and that is disclosed.
- Clear text checked: Más: the writer's a looks like `oi` throughout (vonva, áradt/árad, szárnyait), so `Mois` is simply `Más` with the accent lost in the blot. That is firmer than the solver says, and also explains his "Hois/Mois" and `ujság`.

## Findings

1. **`.1` is not `:1`; Lübi should be Lubi (major).** The card has two distinct left-dot signs. One clear dot: fiú, utolért and the name (`m2.png` fiu, utolert; `m1.png` Lubi). Two clear dots: értünk, üzlet, bűbájtól, hű (`m2.png` ertunk, bubaj; `m1.png` uzlet; `e1.png`). Letters follow exactly: single = u/ú, double = ü/ű. This is the established `.1` = u of hcp-1137, 1140, 1144, 1152, 1153, 1160, 1161. SOLUTION.md merges them as "`:1` ü, u, ű" and hard-codes `:1` in `fiú`, `utolért`, `Lübi`, with `FOLD` hiding the difference. The name is therefore `5, .1 1, 1` = Lubi (or Lúbi), not Lübi; the solver's "one dot plus the flag of the 5" is right about the pixels, and the flag is a separate stroke at upper left (`m1.png`). Fix: add `.1` = u, ú to the table and KEY, change the three tokens, read Lubi in all three languages, rewrite the Lübi uncertainty, and stop folding u into ü.

2. **`áradt` should be `árad` (minor).** The word has one tall stem only (`m3.png` arad): `oi` á, r, `oc` a, then `o` + stem, which is the d of `kezed` and `lábad` (`m3.png`). No second stem exists for a t, and the crossbar t of `nedvtül` and `ott` is absent. `árad` rhymes exactly with `lábad`, is present tense like `terem`, and the solver cites this rhyme itself. Fix in plaintext, decode.py and the uncertainty note. The translation is unaffected.

3. **Address `Önsg.` should be `Őnsg.` (minor).** Two long slanted strokes stand above the O (`b3.png`, lower right), and hcp-1135, 1136, 1145, 1149, 1162, 1164, 1174 all give Őnsg.

4. **Two "comma not seen" statements are too pessimistic (minor).** `szólt`: a heavy stroke starts at the lower right of the 8 exactly where the comma falls, and the low letter u below has no such stem (`m1.png` szolt). It is very probably the comma, merged into the clear line, so `8,` by table. `kedvesed`: a thick stroke crosses the ruled line at the lower right of the 7 (`m2.png` kedvesed), probably the comma. Say so; the ODD count may drop from 10 to 8. Keep them flagged as touching other ink. Neither changes the reading.

5. **Wording in "Why I believe it is correct" and the Slovak (minor).** "Mezőkövesd to Szomolya walkers" has no basis on this card, which does not say how he travelled. Replace it. `Szalókiovie chlapec` is not good Slovak; use `chlapec Szalókiovcov` or similar. The translations use `ángyika` while the plaintext has `angyikát` with no accent visible: note that the normal form is supplied, and that a name Angyika is not excluded. The card's `[kezedet],` comma is the comma of the sign `8,`; no separate punctuation comma is visible.

## Checked and upheld

- Article `a` as a plain `1`, three times: the dot is truly absent (`a1.png`, `b2.png`), while `az` has `1.`. Disclosed, read by sense; no better reading.
- `lassan`: plain flagged 5, no comma (`m1.png`). Disclosed. `hassan` is no word.
- `üzletház`: plain 9 with no comma, and an 8 with a hook below (`m1.png`). Disclosed, and the missing ending is not supplied. Fine. Nothing is hidden beyond the last `9,` before the postmark ring.
- `bűbájtól`: the stroke at lower right of the first 1 (`m2.png` bubaj). Its offset is larger than usual but of the same kind as other commas, and ű below is written with dots alone, so the stroke is free to be the comma. The reading is supported and the poem needs a b here.
- `szerelem`: fourth vowel has two marks (`d4.png`), `1:`.
- `igaz`: the sign is a written g, not `4,` (`m3.png`). Disclosed. One lapse sign in a word that is otherwise clean.
- `Héba` read as a hiába variant: sense only, and disclosed. The separated pixels read `Hé` + tall letter + `a`. Hiába/héjába variants make this reasonable, but it is the softest word in the verse.
- Stray pencil `)` line 4, line-end dashes: agreed.
- Completeness: no unread clause anywhere, enciphered or clear. Once findings are fixed, the card counts as complete, with Lubi as an unidentified name.

## Could not verify

- Postmark date: even rotated and enlarged (`pm.png`) the date band is too heavy and overlaid to read; only part of the place name shows. The year rests on the portal file name.
- Source of the verses: not found by either of us; no search made.
- Who Lubi is and whether szalóki is a surname or place adjective.
- The HistoCrypt article.
