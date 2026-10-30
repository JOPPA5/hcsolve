import re
s=open('SOLUTION.md',encoding='utf-8').read()
def sec(h):
    m=re.search(r'^## '+h+r'\n(.*?)(?=^## )',s,re.M|re.S); return m.group(1).strip()
key=sec('Cipher type and key'); key=key[key.index('| sign'):]
lit=re.search(r'```\n01 .*?```',s,re.S).group(0).replace('```\n','```text\n',1)
unc=sec('Uncertainties')
head='''# HCP 1289 (cpc_--22_HU__HU_Jasz Arokszalas_jolanka-87): Feri to Jolánka Tóth, money or love

Human solver: Tomáš Pavuk

**Status: deciphered in full (824 signs, 29 rows and 8 rows under the stamp), with five restored signs and a few doubtful ones listed below; independent review 1 verdict REVISE, findings addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1289 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1289), portal name cpc_--22_HU__HU_Jasz Arokszalas_jolanka-87, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt proceedings, https://ecp.ep.liu.se/index.php/histocrypt). When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date, language and sender unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a tinted photograph of a man in evening dress at a table, leaning towards a woman, with the printed Hungarian verse *Sokszor úgy szeretnék sírni* ("Often I would so like to cry"). It carries no cipher text. The message is on the address side, written in reddish ink in invented signs: 25 rows in the left block, 4 long rows across the whole card under the address, and 8 short rows in the box under the stamp. The address is in clear: *Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás*. The postmark shows Árokszállás and "22"; the month and year are not legible, so the card is undated. The sender signs only "Feri".

The card belongs to a family of postcards in invented signs addressed to Jolánka Tóth, several of them deciphered in this repository (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). The key was transferred from those cards; it is not a new key recovery. A Feri signs HCP 1216 and a Sándor appears on HCP 1216 and 1217, but no identification of the persons is claimed. No earlier reading of this card was used. The portal attaches none, the orchestrator's check of the AI Decipherment Register on 2026-10-30 found no record, and no search of the wider literature was made.

![Address side: cipher rows, address in clear, stamp box (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, printed verse only, shown as scanned (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

No earlier work exists on this number. Claude Opus 5.5 identified the family from the address and the sign shapes, took the sign classes from HCP 1216 and transcribed the card by hand from enlarged crops of the un-converted scan. This is not OCR, and the transcription was made with the emerging sense in view. The ledger of 824 signs and a short decoder check the source hashes and print the literal text:

```sh
python3 -I ciphers/hcp-1289/work/decode_opus.py
```

The first reading corrected several signs from context checks (chevron v, not j; crossed diagonal z, not x), and the review corrected more (see below). The key was never changed to fit the text.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs and no word division. On this card *gy* is written as two signs (g + y) and *sz* as right bowl + z. Accents are written only irregularly, and the labels below are conventional names for handwritten shapes.

'''
mid=f'''

## Literal decipherment

`[x]` restored, hidden sign; `(x)` struck out by the writer; `x?` doubtful sign; h stands for the h/p sign.

{lit}

## Plaintext (normalized Hungarian)

Word division, punctuation, accents and spelling are editorial. Square brackets mark endings the writer omitted.

{sec('Hungarian \\(normalized\\)')}

## English translation

{sec('English')}

## Slovak translation

{sec('Slovak')}

## Uncertainties

{unc}

## Review and what changed

An independent Claude Opus 5.5 agent ran the decoder, decoded with its own key table, read all 37 rows from its own crops and compared them with the ledger. Its verdict was REVISE: the key and the overall reading stand, but five signs were misread and one was missing.

- Row 28 was corrected from *ráér és … fog[lal]kozni* to *ráérek … foglalkozni*, with a k and a wave sign restored to the ledger (823 to 824 signs). This changed the subject of the clause. The solver then took *meg* as *még* and supplied *Sándor[ral]*, giving "I can still deal with Sándor later"; that sense is inferred.
- *ades* became *edes* (row 10) and *vale* became *vele* (row 29); both are plain three-bar e. This removed the parallels cited for a slip in row 4, where a detached stroke is now reported and the sign is marked doubtful.
- Dots that had been missed were added: *köztün* (row 18), *köszö|nök* (row 2), *elöbb* (row 27, firm on the second, possible on the first).
- The I-beam sign in row 8, the r of *szeretetel* and the g of *légy* are now flagged as doubtful or sense-based.

The review's open points stay open: the exact meaning of the Sándor clause, the misspellings *hogadja* and *ottobi*, *merr* in row 17, the date and the identity of the sender. The corrected reading was not put through a second review, as the changes affect one clause of the translation and transcription details, not the cipher or the key.
'''
open('report/report.md','w',encoding='utf-8').write(head+key+mid)
