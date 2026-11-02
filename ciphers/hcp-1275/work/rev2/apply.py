import re
def sub(path, pairs):
    t=open(path,encoding='utf-8').read()
    for a,b in pairs:
        assert a in t,(path,a)
        t=t.replace(a,b)
    open(path,'w',encoding='utf-8').write(t)
common=[
 ("Nem a lokutja(?), de legyen boldog","Nem állok útjába, legyen boldog"),
 ("Not the [lokutja?], but may you be happy","I will not stand in your way; may you be happy"),
 ("Nie [lokutja?], ale buďte šťastná","Nebudem Vám stáť v ceste, buďte šťastná"),
]
sub('work/normalized-opus.txt',common[:1])
sub('work/ledger-opus.txt',[
 ("12 N E M A L O K U T J A {d} A L E G Y A N","12 N E M A L O K U T J A {b} A L E G Y A N"),
 ("{d} blotted tall sign;","{b} faded tall sign in a water stain, value by shape and word sense (revision 2026-11-02);"),
])
sub('SOLUTION.md',common+[
 ("**Status: PARTIAL. All of the card's roughly 721 signs are transcribed and decoded, but one whole clause (rows 2–4) is not understood, and two further isolated words are not understood. Review 1 verdict REVISE; findings addressed. No register entry is made for this card.** Written 2026-11-01 by Claude Opus 5.5.",
  "**Status: PARTIAL (revised 2026-11-02). All of the card's roughly 721 signs are transcribed and decoded, but one whole clause (rows 2–4) is not understood, and one further isolated word (row 24 `eden`) is not understood. Row 12 is now read. Review 1 verdict REVISE; findings addressed. No register entry is made for this card.** Written 2026-11-01 by Claude Opus 5.5."),
 ("12 nemalokutja{d}alegyan","12 nemalokutja{b}alegyan"),
 ("**Not understood: one whole clause and two further isolated words.","**Not understood: one whole clause and one further isolated word (the second earlier gap, row 12, is resolved; see Revision 2026-11-02)."),
 ("2. **Row 12 `alokutja`** after *nem*: all signs clear (a l o k u t j a). Word not identified.","2. **Row 12**: resolved, *nem állok útjába* (see Revision 2026-11-02)."),
 ("3. **Row 24 `eden`** after *kezböl*: e d e n and a comma, all clear. Could be a noun of address; not established. It does not affect the surrounding sentence.",
  "3. **Row 24 `eden`** after *kezböl*: e d e n and a comma, all clear. Could be a noun of address; not established. It does not affect the surrounding sentence. The last sign's left stroke is a little longer than its right; I keep n, h/p would give no word either."),
 ("4. Row 12 `{d}`: a blotted tall sign, then two bars: `{d}a`, normalized *de* (\"but\"). The bars may be three (one lost in the blot). h is not excluded (*ha*, \"if\").",
  "4. Row 12 `{b}`: a faded tall sign in a water stain, then two bars. Revised from `{d}`: the shape is compatible with the six, but it rests partly on word sense (*útjába*)."),
])
t=open('SOLUTION.md',encoding='utf-8').read()
t+='''
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
'''
open('SOLUTION.md','w',encoding='utf-8').write(t)
n=open('NOTES.md',encoding='utf-8').read()
n+='''
2026-11-02 (Claude Opus 5.5, solver, second attempt ordered by the human): new crops in work/rev2/. Row 12 solved by re-division: nem allok utjaba, legyen boldog; the blotted {d} is a faded six-like sign {b}, partly word sense. Row 24 eden: tested eppen (first pair is short+long, so no), ezen, edes; left open as an isolated word. Rows 2-4: tried nagy kar/kor/kor, Nagykoru, m. kir., hely/hegy/holgy/huvely/hulye, lelkere, ahelyett, h. for hogy; nothing reads. Note: writer spells ly as j elsewhere, against hely. Card stays partial, no marker, no register entry.
'''
open('NOTES.md','w',encoding='utf-8').write(n)
sub('report/report.md',common+[
 ("**Status: PARTIAL. All of the card's roughly 721 cipher signs are transcribed and decoded and nearly all of the letter reads, but one whole clause (rows 2–4) and two further words are not understood.","**Status: PARTIAL (revised 2026-11-02). All of the card's roughly 721 cipher signs are transcribed and decoded and nearly all of the letter reads, but one whole clause (rows 2–4) and one further word (row 24) are not understood."),
 ("12 nemalokutja{d}alegyan","12 nemalokutja{b}alegyan"),
 ("- **Row 12 `alokutja`:** all signs are clear, but the word is not identified.\n","- **Row 12:** resolved on 2026-11-02 by re-division, nem állok útjába (\"I will not stand in your way\").\n"),
 ("  - Row 12 `{d}` is a blotted sign before two bars (*de*; h is not excluded).","  - Row 12 `{b}` is a faded tall sign in a water stain before two bars; its shape fits the six, and the call rests partly on word sense."),
])
t=open('report/report.md',encoding='utf-8').read()
t=re.sub(r'(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)',r'"\1"',t)
t+='''
## Revision of 2026-11-02

A second attempt on new high-contrast crops resolved row 12 (nem állok útjába, legyen boldog; the former "de" is gone). Row 24 "eden" and the clause in rows 2–4 stay unread after testing other divisions, spellings and sister cards. The tempting "éppen" for row 24 was rejected because the sign order does not allow it. The card stays partial and has no register entry.
'''
open('report/report.md','w',encoding='utf-8').write(t)
