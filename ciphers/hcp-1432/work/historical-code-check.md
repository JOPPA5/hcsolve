# Historical-code check, 2026-10-26

Purpose: test whether the observed `.-.-` at home-1/4 is an established C in a historically relevant Morse alphabet. This is a bounded reference check, not a claim about every private/historical code.

1. Alfred Vail, *The American Electro Magnetic Telegraph* (Philadelphia, 1845), printed p.27, ALPHABET. Primary author and contemporary code table, digitized by Project Gutenberg:
   https://www.gutenberg.org/files/61533/old/61533-h/61533-h.htm
   The table explicitly prints American C as two dots, an internal space, one dot (`.. .`); J is `-.-.`; R is `. ..`; O is `. .`; Y is `.. ..`. It does **not** supply C=`.-.-`. The English postcard's repeated `---`=O, `.-.`=R and `-.--`=Y align instead with the International/Continental table. This excludes a wholesale switch to this American table as an explanation for the anomaly. HTML table directly inspected on 2026-10-26; not a downloaded scan and no claim of exhaustive variant research.

2. CCITT, Geneva 1972, Volume II-B, Recommendation F.1, Division B, paragraph B2 /1.1.1 (official table):
   https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/4.256.43.en.1003.pdf
   C=`-.-.`, O=`---`, R=`.-.`, Y=`-.--`. The ordinary alphabet agrees with the frozen decoder. This later official table documents the mapping, not provenance of the postcard's writer's actual reference.

A search extract from a modern compilation initially appeared to list 1844 American C=`.-.-`; direct comparison with Vail's 1845 primary table did not confirm it. It is excluded from the decoding key. Search excerpts/OCR are insufficient grounds for adding a private C variant.

Consequence: retain `REA{.-.-}HEDHOME` in literal output. `REACHED HOME` remains a contextual conjecture, plausibly a local writer error, rather than a demonstrated historical variant. `audit-anomaly.py` also checks reversal/inversion of every group's elements. Reversal or inversion alone makes this one group C but changes many already coherent words; no global repair is supported. Added missing separators yield RT, AA, AET, EK, ENT, ETA or ETET, never C. This does not prove the writer made a mistake, and it does not resolve the ambiguous ordinary A.1.-like mark.
