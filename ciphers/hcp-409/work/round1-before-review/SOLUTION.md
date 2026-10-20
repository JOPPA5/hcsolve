# HCP409 — recovered message with transferred Madrid Kryha key

Solver claim, OpenAI GPT, 2026-10-19. **Content recovered; independent review pending.** All295 letters of the declared manual transcription decode with the pre-existing374 numerical rings and physical23-stop mask. Only initial phase/displacement were searched. There is no five-letter prefix to remove in this reading. Local source defects and formerly unbound alphabet labels remain explicitly qualified. No FINAL or register entry is claimed.

## Origin and prior-solution boundary

HC Portal https://crypto.hcportal.eu/dashboard/cryptograms/409 , MZV80262/1944, Polyak to Madrid,1944-09-09, Slovak National Archive, MZV box42. All three rendered tabs were inspected on2026-10-19; status **Not solved**, category Unknown. The cover types Bern, struck out and amended Madrid. The description names only the subject, information about partisans and Slovakia. No attached plaintext/transcription was observed. Two bounded web queries found no relevant prior409solution; worldwide novelty is not proved.

The numerical key was recovered previously for374 using published373context. That provenance is credited; this is **key transfer**, not ciphertext-only recovery of the original rings. No409plaintext was used to select a key. A generic Slovak four-gram table ranks3 known keys ×2prefix choices ×23phases ×26displacements =3588cases. The full295-letter winner is key374, omit0, phase11, displacement12. Omitting5 gives the same suffix with the accordingly advanced phase; it is not independent corroboration. The next distinct full-text candidate is incoherent. Scores are ranking values, not probabilities.

## Reproduction

From repository root, one source-bound command:

```sh
python3 ciphers/hcp-409/work/decrypt.py
```

Standard-library Python3. It verifies every source-file hash and the manual-reading hash, then prints the exact plaintext. It does not perform OCR. `--json` reports295decoded letters, zero omitted prefix letters and exact re-encryption. The source images are immutable. The first-pass transcription, made before seeing the decode, remains in `work/transcription-first-pass.txt`. Seven later pixel-supported source corrections are listed in `work/transcription-changes.json`; these reinspections were prose-assisted, not blind.

`python3 ciphers/hcp-409/work/verify.py` independently computes absolute wheel coordinates and wrap counts; it imports neither decoder nor search. It reproduces295/295letters, verifies the inverse encoder and tests598phase/displacement mechanical control roundtrips of347letters each. Controls check implementation, not historical wording or glyph correctness. `work/transfer.py` reproduces the search against the preserved original374alphabet completion.

## Physical key

Both P and O below map alphabetical labels A–Z to coordinates0–25, with convention O(cipher)=P(plain)+D mod26. No numerical ring values have changed from374.

```text
P = 0 11 14 1 20 4 9 2 13 15 16 3 24 7 17 25 18 21 10 5 12 6 22 19 8 23
O = 0 4 1 21 8 3 19 15 13 18 25 10 22 16 2 12 5 23 7 20 11 14 17 24 9 6
Selected holes, zero-based, starting at the first observed letter:
4 5 8 11 13 17 20 21 24 26 29 31 34 37 40 42 44 45 47 48 49 51 2
Initial displacement =12 mod26.
```

The52adjacent distances are stored in `work/key.json`; their sum is179. Every emitted letter uses the current D, then one ordinary press walks the physical edges to the next selected hole. The mask is the same as374up to cyclic rotation; its initial hole here is4(zero-based), rather than34. This establishes a working mechanically consistent programmable Kryha interpretation. It does not prove unique original hardware/settings or explain historical key schedules.

## Exact prepared output,295letters

```text
NASLOVENSKUNIETVOBECCSLALEBOCESKYCHVOISKJSULENTLUPYZASKODNIKOVAZAVEDENISLOVACIKTORYMCESKIAWENTINAHOVORILIZEIDEOPOVSTANIERKOPOMSTUZAZAVRAZDENIEPREZIDENTATISUAZATMNUSIESLOVVLADYJVSETKOOBYVATELSTVOSLOVENSKAOKREMSPOMENUTYCHCESKKCHAWETOVIEZASAMOSTATNOSTOCISTENIESLOVENSKASADAKONCUIEJOZNAMSLOVAKOMVUSA
```

The J characters occur at positions41,176and278 and are interpreted as sentence boundaries. This interpretation is semantically supported but the historical symbol convention is not documented here. The inherited374label completion had G at9and W at22; the latter occurs in AWENTI/AWETOV and is **read editorially as G**. Neither label was bound by the old374body/tail. The machine output above retains W and no ring is silently relabelled. Unused labels remain canonical; there is no claim of a fully recovered historical input alphabet.

## Readable Slovak reconstruction — editorial

> Na Slovensku niet vôbec čsl. alebo českých vojsk. Sú len tlupy záškodníkov a zavedení Slováci, ktorým českí agenti nahovorili, že ide o povstanie ako pomstu za zavraždenie prezidenta Tisu a zatknutie slov. vlády. Všetko obyvateľstvo Slovenska okrem spomenutých českých agentov je za samostatnosť. Očistenie Slovenska sa dokončuje. Oznám Slovákom v USA.

Accents, spaces and punctuation are supplied. J is read as a sentence break; word-internal I may render J. These further repairs are explicit: AWENTI→AGENTI; RKO→AKO; ZATMNUSIE→ZATKNUTIE; CESKKCH→CESKYCH; AWETOV→AGENTOV(including a restored N); IE→JE; DAKONCUIE→DOKONČUJE. The reconstruction is not the literal output or a surviving archival clear-text draft.

This is the sender's political/propaganda message. Its characterizations and reported story about Tiso/government are preserved as documentary content, **not accepted as historical facts**. The message attributes the murder/arrest story to what the alleged agents told the Slovaks.

## English translation of the editorial reconstruction

> There are no Czechoslovak or Czech troops at all in Slovakia. There are only bands of saboteurs and misled Slovaks, whom Czech agents have told that this is an uprising in revenge for the murder of President Tiso and the arrest of the Slovak government. The entire population of Slovakia, except the aforementioned Czech agents, supports independence. The clearing of Slovakia is being completed. Inform the Slovaks in the USA.

## Source and unresolved points

1. The scan's prefixed count appears300, but the visible seven lines contain59five-letter groups =295letters. The decoder covers all of those groups and yields a coherent beginning/end. A missing initial indicator or count error is possible but unproved; no invented five-letter group is supplied.
2. Source76–80 qmqhh / qmqlh remains watermark-obscured: H gives KTORYM across the group boundary, L gives BTORYM. H is the default; retain L as an alternative. Source161–165 exzvo / exzyo is also ambiguous: current V yields ZATMNUSIE, earlier Y gives ZATMNUTIE. Neither branch resolves the whole word. Source letters are not changed merely to print the expected ZATKNUTIE.
3. Raw RKO, CESKKCH, AWETOV and DAKONCUIE remain as produced. Their origin could be transcription, typing/transmission or model imperfection. No error-free diplomatic plaintext is claimed. Semantic reconstruction is supported by the long continuous running message, but needs independent source collation.
4. The known374canonical G/J/Q/W/F labels constrain semantic interpretation. All output-ring labels were recovered in the earlier context; this new message supports G at22linguistically but does not prove labels at unused input positions.
5. No reviewer has accepted this new409claim. No PDF final report or register entry is created yet. This is a reproducible content/key handoff, not finalization.
