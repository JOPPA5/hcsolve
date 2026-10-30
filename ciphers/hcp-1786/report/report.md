# HCP 1786 (pc_hcp_467): a Czech postcard from Kutná Hora to Maruška Pařezová

Human solver: Tomáš Pavuk

**Status: the enciphered message on the address side is read in full; a faint pencil note on the picture side is not read. Independent review 1 verdict REVISE; two word divisions were corrected and the key description extended.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1786 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1786), portal name pc_hcp_467, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date Unknown, language Czech, location Europe, sender Unknown, recipient Maruška Pařezová, with no transcription or solution attached.

The picture side is a coloured view titled "Kutná Hora. Chrám sv. P. Barbory a sv. Jakuba." (the churches of St Barbara and St James). The address side carries ten rows of cipher on the left and a plain address on the right:

> Spanilomyslné(?) Slečně / Marušce Pařezové, / (u p. Pařeza Pekařská ul. 12.) / Brno. / Morava.

("To the noble-minded(?) Miss Maruška Pařezová, at Mr Pařez's, Pekařská street 12, Brno, Moravia.") The first word is doubtful in the middle, where the postmark crosses it. The printed imprint gives 1907, which is a printing date only; the postmark cannot be read well enough to date the card.

The sister card HCP 1787 goes to the same surname in the same style ("Spanilé Slečně") and uses the same sign system. It was examined read-only.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side (source/address-large.jpg)](../source/address-large.jpg)

## Method

The repository held no key for this cipher. The transcription is manual, read sign by sign from enlargements of the original 1785-pixel scan, as the portal supplies none. No published solution was found.

The key was built by hand from this card and HCP 1787. Short groups gave the first values: on 1787 the groups for "jsem" and "jest" gave j, s, t, m and the dash for e, and the plain "½ 7 hod" beside "neděle" gave n, d/t and l. From there "nebyl", "přijedete" and "bude" gave b/p, ř and u. The stroke-through rule for o came from "jsou" and "přírody". An early idea that 0 was a vowel and x was v failed on "ale" and "zlaté" and was dropped.

The final decoder is mechanical: only written signs give letters, nothing is inserted to make a word fit. It decodes the 53 words, and 48 match the reading once the distinctions that the cipher does not make are folded (b/p, d/t, h/ch, i/y, accents). The other five are listed under uncertainties. Command, from the repository root: `python3 -I ciphers/hcp-1786/work/decode.py`.

## Key

A home-made Czech substitution, close to an abugida. Each consonant has one sign, and vowels are marks on or after that sign. Word spaces and punctuation are kept.

| Sign | Value | Sign | Value |
|---|---|---|---|
| 0 | l (bare 0 = o once, at word start) | 8 | ch, h |
| 1 | d, t (ď, ť) | 9 | k |
| 2 | n | x | z, ž |
| 3 | m | ζ-shaped sign | j |
| 4 | r, ř | e-shaped sign | c, č |
| 5 | s, š | v | v |
| 6 | b, p | a | a (word-initial only) |

| Mark | Value |
|---|---|
| dash after the sign | e, é |
| caron over the dash | ě |
| one dot | i, í, y, ý |
| two dots | u, ú, ů |
| stroke through the sign | adds o |
| heavy pen stroke on the sign | adds a, á |
| small caron or ring over the sign | ř, š, ž, č, ť |

The heavy stroke writes 12 of the 15 a's in the text. Two more are the sign a, and "až" has none. Pen weight is not a clean signal, since crossings look thick and there are real blots, so these calls were made by eye together with a stroke-width map.

![Stroke-width map from the review: red marks the thickest ink; line 2 starts with heavy x (za) and heavy 5 (psaníčko), line 6 has heavy x of Zaseto (review/work/heavy_map.png)](../review/work/heavy_map.png)

## Plaintext and translation

Literal mechanical output, row by row:

```text
přijměde prozadim dimdo diki
za psaničko nesmiš se zladčko
zlopidi vždiď jsem di psal že
jsou do klepi
dines jsem v kudne hoř pro ře
pové semeno zasedo již mame ješdě
kousek řepi a pude hodovo
děšim se ž přijedede dřive domu
jsou zde hladna ale zlade sluničko
přece ldevira rihle krasu prirodi
```

**Czech:** Přijměte prozatím tímto díky za psaníčko, nesmíš se, zlatíčko, zlobiti, vždyť jsem ti psal, že jsou to klepy. Dnes jsem v Kutné Hoře, pro řepové semeno. Zaseto již máme, ještě kousek řepy a bude hotovo. Těším se, až přijedete dříve domů. Jsou zde chladna, ale zlaté sluníčko přece otevírá rychle krásu přírody.

**English:** Accept for now, with this, my thanks for the little letter. You must not be cross, little darling; after all I wrote to you that it is gossip. Today I am in Kutná Hora, for beet seed. We have it sown already, one more bit of beet and it will be finished. I look forward to your coming home sooner. There are cold spells here, but the golden sunshine is nevertheless quickly opening up the beauty of nature.

**Slovak:** Prijmite zatiaľ touto cestou vďaku za listček. Nesmieš sa, zlatíčko, hnevať, veď som ti písal, že sú to klebety. Dnes som v Kutnej Hore, kvôli repnému semenu. Zasiate už máme, ešte kúsok repy a bude hotovo. Teším sa, až prídete skôr domov. Sú tu chladná, ale zlaté slniečko predsa rýchlo otvára krásu prírody.

## Uncertainties

- **Picture-side pencil note, not read.** About five faint lines over the sky and the church, partly under the portal watermark. The strokes run in joined lines on a baseline, unlike the separate cipher signs, so it looks like ordinary handwriting, but this is not proved. One word looks like "Tebe". The lower-right block has a large open O and tall stems, which resembles the signature "Otta" on HCP 1787; this is a hypothesis only. The sender of this card is therefore not established.
- **Five words differ from the literal output:** zlat(í)čko has no í; "dnes" has a stray dot (literal "dines"); Hoř(e) has no e; (a)ž has no heavy stroke; "otevírá" begins with a bare 0.
- **Word-sense calls:** x and crossed 1 are near-homographs, both X shapes of similar height, so "za", "Zaseto", "to", "tímto", "domů" and "hotovo" rest partly on sense. The last sign of "hotovo" is read as crossed v, and the first sign of "vždyť" lies between 0 and v.
- **Marks read through:** a blot on the dot in "přijměte", a blot and stroke on the 6 of "přijedete", a stroke on the 5 of the second "se".
- **"krásu"** stands above the line with a curled insertion mark.
- **Mixed address:** "přijměte" and "přijedete" are plural or polite, "nesmíš" and "ti" singular. The readings are firm and the translations keep the mix. The writer may be addressing a household.
- **The first r of "přírody"** has no caron.
- **Date:** no date of writing is established. Spring is inferred from the sowing only.

## Review and what changed

A separate Claude Opus 5.5 agent reviewed the first version, with its own transcription and decoder, and gave the verdict REVISE. It upheld the sign values, the stroke-for-o rule, the vowel marks, the hyphen in ře=pové and the unread status of the pencil note. Each finding was then checked on the scan and accepted:

- "zapsaníčko", an unknown word in the first version, is **za psaníčko**: there is a real word gap, and both signs are heavy.
- "To seto" is one word, **Zaseto**: the first sign is the thickest stroke on the card and no word gap divides the group.
- The key said that a is implicit. It is in fact written with a heavy stroke, a rule also found on HCP 1787.
- The transcription now records the dot in "dnes", the strokes on 5 and 6, the accent on "pové", the insertion "krásu" and the carons on "nesmíš" and "že", which the first version had wrongly listed as omitted.
- The address is now given in full. The solver reads "ul. 12." where the reviewer tentatively had a further "č.".
- The mix of "vy" and "ty" is disclosed.
- The checker, which allowed an optional a everywhere and so let both errors pass, was replaced by a mechanical decoder. Restoring an old reading now makes it fail.

Not verified by anyone: the pencil note, the postmark, whether the writer is the Otta of HCP 1787, and the absence of a published solution beyond the portal capture and the register check of 2026-10-30.

Decipherment and report: Claude Opus 5.5.
