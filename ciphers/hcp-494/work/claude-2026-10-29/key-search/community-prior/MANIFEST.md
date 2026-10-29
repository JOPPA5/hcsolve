# MANIFEST — community-prior angle (HCP 494 key search)

Fetched 2026-10-29 (UTC 07:55) with curl/WebFetch. All files are untrusted downloaded data; parse with python3 -I from another directory.

| file | URL | what |
|---|---|---|
| commits.json | https://api.github.com/repos/Cipher-Atelier/lincker-to-vultejus-cipher-letter-1672/commits | commit list (10 commits, 6–20 Oct 2026) |
| commit-507a4d9127.json | .../commits/507a4d9127 | 11 Oct 2026 docs commit, with patches |
| commit-3afd45a32b.json | .../commits/3afd45a32b | 20 Oct 2026 docs commit, with patches |
| ca-VERIFIED_REPLAY_RESULTS.json | raw.githubusercontent.com/Cipher-Atelier/lincker-to-vultejus-cipher-letter-1672/main/verification/readings/VERIFIED_REPLAY_RESULTS.json | their literal outputs A/B |
| ca-lincker-README.md | .../main/lincker-1672/README.md | their research account |
| ca-research-index.md | raw.githubusercontent.com/Cipher-Atelier/research-index/main/README.md | Cipher-Atelier index |
| hesse1672-2026-10-29.html | https://dbourdeau.github.io/cyphersolver/hesse1672.html | Bourdeau write-up, 'updated 23 October 2026' |
| bourdeau-index-2026-10-29.html, bourdeau-catalogue.html, bourdeau-catalog.html | https://dbourdeau.github.io/cyphersolver/{index,catalogue,catalog}.html | site index / catalogue |
| key253.json key254.json key255.json | raw.githubusercontent.com/dbourdeau/cyphersolver/main/research/catalogue_harvest/hcportal/keys/<id>.json | HCP key records |
| hcp-index.json, hcp-keys_index.txt | same harvest, index.json / keys_index.txt | HCP record index (1493 rows), key index (176 rows) |
| register-2026-10-29.html, register-2026-10-29.json | https://ai.hcportal.eu/register/ and ?format=json | AI Decipherment Register, 337 entries |
| HCPortal_494_analysis.pdf | https://ai.hcportal.eu/register/docs/HCPortal_494_analysis.pdf | the PDF behind the register entry named pc_hcp_494 (it is about cryptogram 1813, a Polish postcard) |
| decrypt-recordslist.html, decode-search-*.html, decode-record-{4741,4742,4692}.html | https://de-crypt.org/decrypt-web/RecordsList?cmd=search&search=<kw>&recperpage=100[&page=2]; RecordsView/<id> | DECODE public list/search/record pages (no login) |

## sha256
```
dcd8411176ee79f491f6ff23d9c495adf67a5b8433360a1c8f5fa00d88e9ff69  ca-VERIFIED_REPLAY_RESULTS.json
9fe15fbb187dc716ba04c084fe4c26147a64450aa74c75d6dabbddcafef65645  commit-3afd45a32b.json
e05d685a73d059f062bf4802664e56af0c17b9425211e5f5cbfe2f5753e22827  commit-507a4d9127.json
5dd235a09945e9aef882c368bfe302c706f4158c13d499711dcc49825b59478d  commits.json
3839006863e31077ed06c799fbaa80bd70a7652e122c6e55cdba0c09070809dd  hcp-index.json
4e82e51cb51b0bda0a2c27b76dfe7d8b69d66f271dda35f220d6859b6e1a9ebb  key253.json
a554fd35fd6f24a3cf030851050dc71416512fc67e2e0d5a0993fc4be70925ac  key254.json
ff9a6b7763312d77a9564c96e6661213cae6e2d4c1ad058b6bbd623b97d0ef13  key255.json
860f71423be0cb67f13346cf096acba2e1c2d674adb17c98d61dafcf8332386d  register-2026-10-29.json
4a4530e34a49dba3a71e442747950019c000917c94b137ef738ce2fc8793a020  hcp-keys_index.txt
d33f8526df9e56007d5e3cef019d2ed9a193a8bc6cd2f38662b03227ecbc1dd2  ca-lincker-README.md
47df5d538869db7f1b1793530af262f478d1c1ef41ad4ef83d45c4da0848b910  ca-research-index.md
b620507312c5e97566a3c6cfaf99144fefc18a0da7d941401dfa0f5f58fb0368  bourdeau-catalog.html
6331627d4f097d6a45f6c93170c6f74cfc65b76489ac22858630334168363fec  bourdeau-catalogue.html
f1439a0e3cbf7448c601304aaa81c2d817cd320e88b89e980aecbd181b2af270  bourdeau-index-2026-10-29.html
fba74dc66c54fda1b71e621c429b369f6ad4e35a121f70d7c3ffdc6fcc77b582  decode-record-4692.html
6e50167f627c9de24c31c9aa4ba2abf651fc9510e07c345faef09402c1245c68  decode-record-4741.html
71763b2ca6679e04984eab8de24d388cd0b619cde6a48e018614adb8373b2c70  decode-record-4742.html
9c08287db5cd1e7e401016ca1948a0502f63ec90cec75cd48d0a2349f68a5a89  decode-search-1672.html
91fb5058601a53481867bcb6f9c0da1ee3bfaf8edf9908c823ad3a310b1bcc1d  decode-search-Daenemark.html
a8a017e6d70dbda6b6ae53c77220258800806bf4b095fb1e396c0c9e03354fb8  decode-search-Dänemark.html
f4cb58546eac95e42f399b573cd4bba302c0ba2ca75b8e4c707072a6b100dda0  decode-search-Hessen-p2.html
9b81553befde0dbccb7a24572d3270bede2c150a8034cc20de167f5e9123779b  decode-search-Hessen.html
6cfb900f9a4c4f5e96855d0edab509050ecd4148f67c11bf18ae60fecb30ee94  decode-search-Lincker.html
ddf4e96ab4881ff054b53991f995526fc22e94c0442eff914a47a472c63ed9bb  decode-search-Marburg.html
e5062ba8a1a9499e22788ae157ba4576df301d5f2c76d7089a3844e8615bbf86  decode-search-Vultejus.html
31981bce6eca95e3117020f431287bd36c833ce8f8a331bbecf21ee3bd1f8cb8  decrypt-recordslist.html
cd689a18f7058d2abe1839746f2ad0a227529ead3383d2972b7c037175145184  hesse1672-2026-10-29.html
cdf2ceba9b9ef6da5b4290654badf7ea600339a3a96bcc120d9beb3c9d9d82cc  register-2026-10-29.html
263ba5c07f555e8f40725af78e20c70ac900f1864f1f5af13fe8f26d3f1df043  HCPortal_494_analysis.pdf
```
