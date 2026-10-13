# HCP1216 — Waiting for a letter and hoping to meet again

**Status: partial.** This card has not had an independent full-text review. Work date: 2026-10-12.

## Source and method

[HC Portal record](https://crypto.hcportal.eu/dashboard/cryptograms/1216) was visibly **Not solved**. General, Description and Attachments were read. Both postcard sides are preserved in `source/`; the portal supplied no transcription or solution. See `SOURCES.md` for attachment URLs and hashes.

The text is Hungarian written with a graphic monoalphabetic substitution. The working alphabet was transferred from this workspace’s HCP1301/HCP1243 readings and tested manually against this separate card. Repeated greetings and unrelated coherent passages support the transfer; they do not resolve every handwritten symbol. Accents can modify the same base symbol; joined `gy` and `cs` require care.

The following is an editorial reading with spaces and punctuation, not an exact symbol-by-symbol transcript. Square brackets mark alternatives, supplied letters or gaps. No external plaintext was used for these passages. The AI Register search for `jolanka` returned “No matching contributions” among 37 contributions on the work date; that limited check does not prove that no historical solution exists elsewhere.

## Hungarian reading

Szeretett édes Jolánkám! Nem tudom mire vélni, hogy nem ír. Már [a] szerdai posta is elment […] sora[it?] […] Édesem, úgy várom, mint a zsidók a Messiást. Édes egyetlen reményem, hogy van, egésséges? Alig várom, hogy viszontlássam.

Múlt héten beszéltem Sándorral, mondta, hogy jól néz ki, mer[t] bizony régen nem láttam. A múltkor, hogy erre mentem, [olyan nehezemre esett?] […] Vámosgyörk mellett elmenni, [de?] leküzdöttem fájdalmam, mert biztatott az a tudat, hogy nem soká fel [fog?] jönni, és akkor viszontláthatom. Isten vele, a viszontlátásra.

Under the stamp: Csókolom számtalanszor. Sírig hű kedvese, Feri.

## English translation

My beloved, sweet Jolánka! I do not know what to make of your not writing. The Wednesday post has already gone […] your lines […] My darling, I wait as the Jews await the Messiah. My sweet, only hope, how are you; are you well? I can hardly wait to see you again.

Last week I spoke with Sándor; he said that you look well, for indeed I have not seen you for a long time. The last time I came this way, [it was so hard for me?] […] to pass Vámosgyörk, [but?] I overcame my sorrow, because I was encouraged by the thought that you [would?] soon come up and that I could then see you again. Farewell, until we meet again.

Under the stamp: I kiss you countless times. Your sweetheart, faithful until death, Feri.

## Uncertainty and remaining work

Fourth pass: a full spatial ledger now covers all 22 main rows, the right-edge continuation, and six stamp rows. The apparent leftover nemos before Györk is the beginning of Vámosgyörk: the first overwritten sign is a chevron, followed by the two-bar a, m, o and s. The right-edge continuation reads latasra. Main rows 4-5 remain unresolved: the shape output resembles nekuz{?}om / kel sorait ne{?}ig{?}gyjael. The proposed normalization nélkülöznöm kell sorait is linguistically plausible but is not sufficiently supported to promote into an exact reading. No completion marker is created.

## Working key

At this scan resolution h/p are near-homographs and sometimes require linguistic context; d/n can also differ only by stroke length. The shape names below describe tendencies, not a guaranteed visual classifier. This qualification follows the independent HCP1301 review that arrived during this batch.

| Named graphic class | Letter |
|---|---|
| two-bars | a |
| six | b |
| left-bowl | c |
| joined-two-strokes | d |
| three-bars | e |
| cross | f |
| open-loop-descender | g |
| two-tall-strokes | h |
| dotted-crossed-curve | i |
| inverted-T | j |
| section-mark | k |
| wave | l |
| three-short-strokes | m |
| two-short-strokes | n |
| cursive-loop | o |
| tall-short-stroke | p |
| F | r |
| right-bowl | s |
| gamma | t |
| x | u |
| chevron | v |
| low-descender | y |
| crossed-diagonal | z |
| two-bars:acute | á |
| three-bars:acute | é |
| dotted-crossed-curve:acute | í |
| cursive-loop:acute | ó |
| cursive-loop:diaeresis | ö |
| cursive-loop:double-acute | ő |
| x:acute | ú |
| x:diaeresis | ü |
| x:double-acute | ű |

## Reproduction boundary

Run from the repository root:

```sh
python3 batches/jolanka-next-five-2026-10-12/check_readings.py 1216
```

This verifies the archived files against the recorded hashes and prints the saved manual reading. It **does not decipher pixels** or independently validate the proposed text. `work/reading.json` records the claim; `work/top.png`, `bottom.png` and `stamp.png` are enlarged source crops for visual comparison. Full automated reproduction is not yet available, which is another reason not to create a completion marker.


## Fourth-pass coverage and reproduction

Fourth pass: a full spatial ledger now covers all 22 main rows, the right-edge continuation, and six stamp rows. The apparent leftover nemos before Györk is the beginning of Vámosgyörk: the first overwritten sign is a chevron, followed by the two-bar a, m, o and s. The right-edge continuation reads latasra. Main rows 4-5 remain unresolved: the shape output resembles nekuz{?}om / kel sorait ne{?}ig{?}gyjael. The proposed normalization nélkülöznöm kell sorait is linguistically plausible but is not sufficiently supported to promote into an exact reading. No completion marker is created.

Run `python3 batches/jolanka-next-five-2026-10-12/visual-ledgers/decode.py 1216` to check the scan hash and decode the current ledger. The provenance manifest states its coverage. Full spatial transcription is not the same as successful decipherment of uncertain words. The earlier partial editions remain archived.
