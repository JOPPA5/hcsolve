# 373/374 common prefix: source evidence and limits

Independent **source reinspection**, not blind transcription: the assigned task already named KIDAH. Both original images visibly print lower-case **kidah** as their first five-letter group. Its placement is inside the grouped cipher, immediately after the numerical length header, in the same typeface and baseline as the remaining groups. Neither image labels its purpose. Source coordinates for this group are approximately 373 `(349,314,421,344)` and 374 `(307,411,379,439)` in their original 1024×1365 images.

373 has header650 and130groups; 374 has header85 and17groups. Both show Madrid and Legación Eslovaquia. Published portal metadata dates are respectively **17 May1944** (Országh, message80172) and **20 May1944** (Šulík, message80174), consistent with visible date stamps. Provenance: `batches/solved-context-main/373/SOURCES.md` and `ciphers/hcp-374/SOURCES.md`; public records [373](https://crypto.hcportal.eu/dashboard/cryptograms/373) and [374](https://crypto.hcportal.eu/dashboard/cryptograms/374). Source hashes are recorded in `manifest.json`. The previously acquired sources were only read offline.

My preferred source reading of374 is:

`KIDAH CRTCS BVBPT ILOIQ SPQHO NZYHI QLXUM AIPOT KBCEY HVUIU QOQPM TLIJV ABAVE KZAXI MLEMP QXMJC JSLWF`

The watermark leaves the declared branches **CRTCS/CRTCG**, **SPQHO/SPQHQ**, **TLIJV/TLIJY**. These alternatives are not selected using a proposed plaintext. No glyph substitutions beyond these declared alternatives were tried. All eight combinations were compared independently with the complete650-character preferred transcription of373. None occurs as a complete85-character substring, none has its remaining80characters as a substring, and none equals373's last15groups. The **only identical complete group anywhere between the two texts is the initial KIDAH**, atgroup1in both. This conclusion also survives the separately recorded373 glyph alternatives, because those groups cannot become any374 group under those alternatives.

373's last15groups116–130 are:

`OJGEC NCJHP NFIRI ZGAHM XAJYY ALRWG SKYSK BTRQK RTJUJ KQQKS HJSYQ XUROU ZBLTW YDJUQ FNPBV`

374's Description says its original document title requests repetition of the last15groups of80172. That is contextual metadata, **not evidence that374 itself contains the repeated cipher tail**. The literal comparison shows it does not. No plaintext for374 is inferred solely from that title.

A shared named-key/control identifier, a conventional dummy prefix, or a fixed plaintext preamble enciphered at a common starting state are all compatible with this local repetition. The evidence does not choose between them. The analogous SOSOL repetition in350/351 suggests that a stable five-character component deserves a procedural hypothesis, but it does not establish shared rings, key names, dummy content, initialization, or an unencrypted indicator. A useful discriminating test would independently recover/transfer the full Madrid body key and inspect the first five characters under that **same** body procedure: a coherent fixed preamble versus arbitrary decoded symbols would inform the hypotheses, without proving an indicator merely because a prefix repeats.

This is attributed published context for373, not a new decipherment. No keys were forced, no source/cipher/marker files changed. Reproduce the comparisons with:

`python3 batches/kryha-prefix-context-sol61/compare.py`
