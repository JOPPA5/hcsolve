from pathlib import Path
import json, textwrap, html, argparse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Preformatted, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

root=next(p for p in Path(__file__).resolve().parents if (p/'README.md').exists() and (p/'ciphers').exists())
parser=argparse.ArgumentParser(); parser.add_argument('--cipher',type=int,choices=[350,351]);args=parser.parse_args()
font=Path('/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
for name,file in [('DVS','DejaVuSans.ttf'),('DVS-Bold','DejaVuSans-Bold.ttf'),('DVM','DejaVuSansMono.ttf')]:pdfmetrics.registerFont(TTFont(name,str(font/file)))
styles=getSampleStyleSheet()
for name in ('Normal','Title','Heading2'):styles[name].fontName='DVS'
styles['Normal'].fontSize=9;styles['Normal'].leading=12.5;styles['Normal'].spaceAfter=8
styles['Title'].fontName='DVS-Bold';styles['Title'].fontSize=19;styles['Title'].leading=25;styles['Title'].spaceAfter=16
styles['Heading2'].fontName='DVS-Bold';styles['Heading2'].fontSize=11;styles['Heading2'].leading=15;styles['Heading2'].spaceBefore=12;styles['Heading2'].spaceAfter=8
mono=ParagraphStyle('mono',fontName='DVM',fontSize=7.4,leading=10.5,spaceAfter=9)
def footer(c,d):
    c.setFont('DVS',7);c.setFillColor(colors.HexColor('#586174'));c.drawString(42,26,'HC Portal | reviewed content decipherment | 11 October 2026');c.drawRightString(A4[0]-42,26,str(d.page))
for n in ([args.cipher]if args.cipher else [350,351]):
    cipher=root/f'ciphers/hcp-{n}';assert(cipher/'REVIEWED1').exists() and not(cipher/'FINAL').exists()
    w=cipher/'work/kryha-decipherment';key=json.loads((w/'key.json').read_text());raw=(w/'prepared-plaintext.txt').read_text().strip();ed=(w/'editorial-reading.txt').read_text().strip();tr=(w/'english-translation.txt').read_text().strip()
    story=[];md=[f'# HC{n}: reviewed car-purchase telegram']
    def p(s):story.append(Paragraph(html.escape(s),styles['Normal']));md.append(s)
    def h(s):story.append(Paragraph(html.escape(s),styles['Heading2']));md.append('## '+s)
    def literal(s):story.append(Preformatted('\n'.join(textwrap.wrap(s,88)),mono));md.append('```text\n'+s+'\n```')
    story.append(Paragraph(f'HC{n}: car-purchase telegram',styles['Title']))
    p('Content and working key recovered. The first group and exact historical preparation remain open. Independent review: '+('ACCEPT.'if n==350 else 'REVISE; source and documentation findings addressed without changing the key.'))
    h('Origin and recovered message')
    p(f'MZV message No. {3001 if n==350 else 3002}/1944, Cieker to the Ministry of Foreign Affairs, Bratislava; Slovak National Archive, MZV box 42. Portal status at acquisition: Not solved, tagged Unsolvable. '+('Portal date: 28 February 1944.'if n==350 else 'Portal date: 3 November 1944. The source postmark reads −2 III 44−23, apparently arrival on 2 March 1944, and the handwritten number is 816/1229. The conflict is explicit; an exact dispatch date is not proved.'))
    p('These are two copies of one underlying Slovak telegram about a car for 55,000 pesetas, a requested loan from the chairman, a cheaper possible purchase in France using francs bought in Madrid, Mikuš, and a decision within three days. No published plaintext of either target was used.')
    h('How the working key was recovered')
    p('Claude’s outside batch review supplied the decisive shifted pairing, 350[i] ↔ 351[i+1], with period 23. The solver team recovered the common output cycle using finite-field/CRT error-tolerant equations, fitted two ordered stop masks to published wheel geometry, and ranked input rings and admissible paths by generic Slovak n-grams. Neither a target plaintext nor Claude’s proposed output cycle was a search seed. A final fixed-input pass enumerated 1,084,757 paths; this was not exhaustive over all joint rings.')
    p('Relative to 350, copy 351 has an extra T at position 21 in MOZNOSTTI and lacks E in final ROZHODNUTIE. This accounts for the +1 body alignment and realignment for final DOTROCHDNI. The two model masks differ by one selected stop: hole 0 in 350 becomes 48 in 351. A wrongly set stop could explain an unreadable repeat, but that historical explanation is conjecture.')
    h('Working key and mechanically consistent interpretation')
    p('Input ring, coordinate → letter: JERGZMPADHLQTVNYFSBUICXKOW. Output ring, coordinate → letter: AKXRMDTGJWNHVIPULYESZQBFOC. JSON stores output O in the inverse direction, letter → coordinate. The working displacement sequence has period 23 with total advance 179 modulo 26.')
    arcs=[]
    for a,b in zip(key['holes'],key['holes'][1:]+key['holes'][:1]):
        total=0
        while a!=b:total+=key['adjacent_distances'][a];a=(a+1)%52
        arcs.append(total)
    p('Selected stops, zero-based and in walking order: '+', '.join(map(str,key['holes']))+'. Initial stop 47; initial displacement 0. Ordinary clockwise pressing between selected stops gives increments: '+', '.join(map(str,arcs))+'.')
    p('At each character c, decode P[(O(c)−D) mod 26], then add the next increment to D. Both ring arrays are permutations. All 23 arcs traverse the 52-hole wheel once. This is a mechanically consistent adjustable Kryha interpretation; it does not identify the original hardware or prove that these were its historical settings. The recovered rings and displacement increments are the decoding evidence.')
    h('Reproduce all 385 positions')
    literal(f'python3 ciphers/hcp-{n}/work/kryha-decipherment/decrypt.py')
    p('Run from the repository root using Python 3 standard library. The command checks original-image and manual-transcription SHA-256 values, decodes every position, and independently inverse-encodes the result. It uses a manual source reading, not OCR. It omits no prefix and performs no language cleanup. Key, source provenance, alternate readings and raw snapshots accompany this report in the cipher directory.')
    story.append(PageBreak())
    h('Literal prepared plaintext: all 385 characters')
    literal(raw)
    h('Readable Slovak reconstruction — editorial')
    p('[SOSOL: probably an unenciphered indicator, meaning unknown.] '+ed)
    h('English translation of the editorial reconstruction')
    p('[SOSOL: probably an unenciphered indicator, meaning unknown.] '+tr)
    h('Differences retained, not silently repaired')
    tabledata=[['350 position / 351 position','350 literal','351 literal'],['81 / 82','DRAAE','DRAHE'],['85 / 86','PREDAVAIUCI','PSEDAVAIUCI'],['122 / 123','POPROT','POPROS'],['315 / 316','PRISTUPIK','PRISTUPIT']]
    t=Table(tabledata,colWidths=[210,145,145],hAlign='LEFT');t.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'DVS'),('FONTSIZE',(0,0),(-1,-1),8),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#edf1f5')),('BOTTOMPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('GRID',(0,0),(-1,-1),.3,colors.HexColor('#cbd1da'))]));story.append(t);md.append('\n'.join(['| '+' | '.join(tabledata[0])+' |','| --- | --- | --- |']+['| '+' | '.join(row)+' |'for row in tabledata[1:]]))
    p('Positions identify the differing letters in the shown words, not each word’s start. These four interior differences remain in the reviewed default. Copy 351 also has the extra T and missing final E. Their source/transmission/preparation cause is not established.')
    story.append(PageBreak())
    h('Uncertainties and source readings')
    p('The same source prefix SOSOL yields USMMF under the 350 body key and UITLF under 351. Because the body displacements differ there, it is probably an indicator sent unenciphered, an inference rather than a documented rule. The count 385 includes it; the decryptor retains it. Its meaning remains unknown.')
    p('Rare input labels were explicitly selected by meaning: old G→X, old Q→G, old X→J, unused old J→Q relative to the blind six-gram candidate. The unused label is not determined by this text. Sentence J and word-internal I/J normalization are historical-procedure hypotheses. Spacing, accents and local repairs are editorial; PATDESATPAT is read as päťdesiatpäť by adding I. No archival clear-text draft was found.')
    p('After review, 351 positions 11/12 were changed RW→PM and 231 L→I. Prose-assisted source reinspection and the earlier independent blind reading agree; stamp overlap leaves alternatives. Position 86 remains R because its diagonal leg is visible, with P disclosed as the blind-reader and correct-word alternative. Position 73 remains O; blind U was marked uncertain. The earlier strong 240 U→J correction is retained. Default --variant reviewed uses these readings; --variant collated reproduces the DONE1 default. The other archived variants preserve their original glyph alternatives.')
    h('Independent review and responses')
    p('Claude Opus 5.5 wrote an independent decoder from the prose and numeric key, covering and re-encrypting 385/385 letters of both copies. Its pre-recovery blind source reader agreed with all four corrected 350 glyphs and produced the same message for 351. Claude supplied the initial pairing lead and disclosed that limit on independence; the recovered rings, stops and plaintext were the solver team’s work.')
    p('350 verdict ACCEPT: findings addressed by retaining a qualified physical interpretation, identifying SOSOL only as a probable indicator, marking the one-stop error explanation as conjecture, showing both copies’ garbles side by side, and stating content/working-key recovery clearly. Original hardware, exact preparation and rare labels remain open.')
    p('351 verdict REVISE: source positions 11/12 and 231 corrected, 86 R/P and 73 O/U explained, inserted T/dropped E alignment stated, March arrival/November portal-date conflict recorded, and model attribution clarified. The numerical key is unchanged. The reviewer expressly required no second round for these revisions. Full item-by-item responses are in each SOLUTION.md.')
    p('Additional solver-team checks after DONE1, not rerun by Claude: two fresh clean paired 385-letter controls recovered exact texts and both masks among the predeclared 6/7-gram objective winners using ciphertext-only stages. One control succeeds under 7-grams, the other under 6-grams; a universally selected automatic winner remains unvalidated. The earlier controls supplied output-ring information and are distinguished from these tests.')
    h('Sources, attribution and outcome')
    p(f'Original rendered portal record: https://crypto.hcportal.eu/dashboard/cryptograms/{n}. Original images and metadata are immutable in source/; SOURCES.md records all acquisition and research. Solved 391/392/394 and later linked Madrid 373 were disclosed context, not a source of this pair’s plaintext.')
    p('Geometry source: Callimahos, Military Cryptanalytics Part III (1977), §52, pp.184–185, https://www.governmentattic.org/41docs/NSAmilitaryCryptalyticsPt3_1977.pdf. Slovak cipher context: Antal/Grošek/Zajac, Vojenská história 24(3), 2020, pp.95–108. German SSA NR2417 does not establish SOSOL or Slovak preparation rules.')
    p('Earlier GPT-6 Astra attempts were unresolved. GPT-6.1 Sol subagents recovered the cycle, working key and language, and performed audits; main OpenAI GPT integrated the recovery and selected rare-label semantics. Claude Opus 5.5 supplied the pairing lead and independent review. Content recovered; working key recovered; exact historical procedure open. No register entry is produced for the remaining partial historical claim.')
    report=cipher/'report';report.mkdir(exist_ok=True)
    (report/'report.md').write_text('\n\n'.join(md)+'\n')
    SimpleDocTemplate(str(report/'report.pdf'),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=40,bottomMargin=43).build(story,onFirstPage=footer,onLaterPages=footer)
    print(n)
