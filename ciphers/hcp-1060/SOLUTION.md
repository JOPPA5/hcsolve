# hcp-1060 – PARTIAL solution (no marker)

Card: HC Portal cryptogram 1060, `cpc_1911-11-23_DE_Schweidnitz_DE_Hier_fritzlehmann-15`, T. Schrödel collection.
Postmark SCHWEIDNITZ 23.11.11, Germania 5 Pf; addressed in plain Kurrent to "Herrn Fritz Lehmann, Hier (Schweidnitz)".
Picture side: printed photo card "Grüss' Dich Gott! Herzig Liebchen, du mein Leben." (publisher KVG 2054/4), no handwriting found.
Portal status: Not solved; no transcription or solution attached. Everything below is my own reading (Claude Opus 5.5, 2026-11-03)
from work/hires/. No earlier work existed in this directory. No web search hit for this card was looked for beyond what the
orchestrator recorded; nothing published is used.

## Cipher type and key

Number substitution (MASC), German – the same table as the finished Lehmann sister cards hcp-1113 and hcp-1134:
25-letter alphabet without J, A = 2 … Z = 26. Dots separate numbers, dashes separate words, double tick = umlaut (21" = Ü).

## What is read

The message (written sideways on the left half) has 5 lines of numbers followed by 6 lines of plain German Kurrent.

Number block (work/transcription.txt), decoded by `python3 -I ciphers/hcp-1060/work/decode.py` (checks source hashes):

```
LIEBER FRITZ VIELEN
DANK FÜR DEINEN KARTEN
HAA' HEUT DEN ARTZ GEFRAGU OB
ICH KANN SONNABEND RAUS
BIN ALSO BIS SON MITTAG FREN
```

Intended reading: "Lieber Fritz! Vielen Dank für deinen [deine] Karten. Hab' heut den Arzt gefragt, ob ich kann Sonnabend raus.
Bin also bis Son[nabend?] Mittag f…" – "Dear Fritz, many thanks for your cards. I asked the doctor today whether I can go out on
Saturday. So I am … until Saturday(?) noon …" / Slovak: "Milý Fritz, veľká vďaka za tvoje pohľadnice. Dnes som sa pýtala lekára,
či môžem v sobotu von. Som teda až do soboty(?) na obed …"

Writer slips / weak points in the number block (all from the pixels):
1. 9.2.2' – the third sign looks like this writer's 2 (round top), not the flat-topped 3 of LIEBER/SONNABEND/BIN; a tick follows.
   "HAB'" (9.2.3') is word sense only.
2. 2.18.20.26 = ARTZ (misspelling of Arzt, as written).
3. GEFRAGT ends in a clear 21 (U), not 20 (T): writer slip, read by word sense.
4. DEINEN: last number is a cramped 1+4 run into the word dash; 14 = N.
5. Last group of line 5 (7.18.6.14, "FREN") does not give a word; the third/fourth signs might be 10 and 14, but neither FREI
   (7.18.6.10) nor any other reading is supported by the pixels. Unresolved.

Plain Kurrent part (lines 6–11), what I can read with reasonable confidence:
- line 6: "[?] mir sehr so [?]. Tut mir leid, dass du deinen"
- line 7: "[Abend?] [verb, unread], hättest lieber hier bleiben sollen."
- line 8: "Man sehnt sich auch die [ist, inserted above] [unread word] dann zu meinem [?Freunde/n]"
- line 9: "zu meinem Glück, und sehnt sich [?nun] so heiß zu[?] … nach"
- line 10: "seinem(?) lieben [unread noun] zurück! Gelt, das ist wahr?"
- line 11: "Für heute viele Grüße deine Liese."

## Why this is partial

The cipher part is decoded with a known key, but its last word is unresolved, and the unenciphered Kurrent part has several
unread words in at least four lines (line 6 start and the adjective after "so", the verb in line 7, the word after "die" in line 8,
words in lines 9–10). By the project rule a whole unread clause makes the card partial, so no DONE marker is created.

## Steganography check

Stamp still affixed; no ink traces at its edges on the scan, so anything underneath cannot be inspected. Picture side: printed caption
only. Edges: nothing found.
