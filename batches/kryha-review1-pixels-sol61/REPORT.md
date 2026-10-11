# Post-review pixel inspection: HCP351

Independent inspection of the immutable `ciphers/hcp-351/source/cryptogram.jpg`, after disclosure of both root and reviewer readings. This is **not blind** and supplies no new cryptanalytic evidence or key fit. Original source hash and exact crop coordinates are in manifest.json. Native crops and 6× nearest-neighbour views preserve the pixels without enhancement or retouch.

| Position1 | Preferred reading | Pixel evidence and uncertainty |
|---:|:---:|---|
|11|P|The dark typed stem and upper bowl are visible. The apparent lower diagonal overlaps the broad blue stamp rather than forming a clearly separate dark typed R leg. P is preferred; watermark interference prevents calling R impossible.|
|12|M|Two upright outer stems and the inward central join favour M. The blue diagonal overprint distorts the silhouette and can suggest W. M is preferred with moderate confidence. Together the preferred group is PMQKK.|
|73|O|The third glyph of XUOMC has a rounded dark contour with an upper curved segment, unlike the adjacent U's open top and straight uprights. O is preferred; the stamp crosses the top and middle, so U is not declared definitively excluded.|
|86|R|The first glyph of RFPFN has a lower-right dark diagonal extending from the bowl/stem junction, distinguishable from the larger blue diagonal background. This supports retaining R rather than P. The overprint still weakens certainty; P remains a documented alternative.|
|231|I|The first glyph of IVBMF is a narrow upright. No clear rightward dark L foot is independently visible. The lower end is covered by a blue stroke, so an obscured L foot remains possible. I is preferred with moderate/low confidence, not an unambiguous source proof.|

These judgements agree with root's current preferred PM / O / R / I readings, but differ from the reviewer's P86 and U73. Disagreement should remain disclosed. Selecting I231 need not imply that all model-assisted variants or lexical interpretations are uniquely supported by the scan. No canonical transcription, key, source or cipher file was edited.

Reproduce crops from repository root using the bundled Python with Pillow:

```
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 batches/kryha-review1-pixels-sol61/crop.py
```
