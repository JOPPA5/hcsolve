from pathlib import Path
import argparse,json,html,textwrap,subprocess,sys,re
from reportlab.platypus import SimpleDocTemplate,Paragraph,Preformatted,PageBreak,Table,TableStyle,Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'README.md').exists() and (p/'ciphers').exists());CIPHER=ROOT/'ciphers/hcp-374'
ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,default=Path(__file__).parent/'draft-report');ap.add_argument('--final',action='store_true');ap.add_argument('--authorized-report-edit',action='store_true',help='Explicit human-authorized report-only edit after FINAL');args=ap.parse_args()
if args.final:assert (CIPHER/'REVIEWED1').exists() and (not (CIPHER/'FINAL').exists() or args.authorized_report_edit)
args.output_dir.mkdir(parents=True,exist_ok=True)
font=Path('/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
for name,file in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf'),('DVM','DejaVuSansMono.ttf')]:pdfmetrics.registerFont(TTFont(name,str(font/file)))
styles=getSampleStyleSheet()
for name in ['Normal','Title','Heading2']:styles[name].fontName='DV'
styles['Normal'].fontSize=9;styles['Normal'].leading=13;styles['Normal'].spaceAfter=9
styles['Title'].fontName='DVB';styles['Title'].fontSize=20;styles['Title'].leading=25;styles['Title'].spaceAfter=15
styles['Heading2'].fontName='DVB';styles['Heading2'].fontSize=11;styles['Heading2'].leading=15;styles['Heading2'].spaceBefore=10;styles['Heading2'].spaceAfter=7
mono=ParagraphStyle('mono',fontName='DVM',fontSize=7.5,leading=11,spaceAfter=9)
key=json.loads((CIPHER/'work/key.json').read_text());decoded=json.loads(subprocess.check_output([sys.executable,str(CIPHER/'work/decrypt.py'),'--json']))
story=[];md=[]
def p(text):
    text=re.sub(r'(?<=[^\W\d_])(?=\d)|(?<=\d)(?=[^\W\d_])',' ',text)
    story.append(Paragraph(html.escape(text),styles['Normal']));md.append(text)
def h(text):story.append(Paragraph(html.escape(text),styles['Heading2']));md.append('## '+text)
def literal(text):story.append(Preformatted('\n'.join(textwrap.wrap(text,90)),mono));md.append('```text\n'+text+'\n```')
def footer(canvas,doc):
    canvas.setFont('DV',7);canvas.setFillColor(colors.HexColor('#566174'));canvas.drawString(42,25,'HC Portal 374 | '+('Reviewed partial historical claim' if args.final else 'Review pending - draft')+' | 12 October 2026');canvas.drawRightString(A4[0]-42,25,str(doc.page))

story.append(Paragraph('HC374: Madrid telegram',styles['Title']));md.append('# HC374: Madrid telegram')
p('The message body and a working Kryha key have been recovered. The deciphered body contains 80 letters. KIDAH is the shared indicator associated with the same starting state as telegram 373; how its letters encode that setting remains open. Historical uncertainties are stated explicitly.')
h('Origin and content')
p('MZV message 80174/1944, 20 May 1944, Šulík to the Slovak legation in Madrid. Slovak National Archive, MZV, box 42. Portal status at acquisition: Not solved. The scan prints a count of 85 and seventeen five-letter groups. The title describes a request to repeat the last 15 groups of 80172; the new 80-letter block is not claimed to be exactly the same 75-letter slice.')
p('Public Solved telegram 373 (80172/1944, 17 May 1944) supplied an archival clear-text draft and ciphertext. Its final sentence provided the known plaintext for recovering the machine key. The commercial content was already published in that source; the new work is key recovery and its transfer to 374.')
h('Literal output from the independent transcription')
literal(decoded['body_plaintext_literal'].upper())
p('Separate indicator: KIDAH, shared with 373 and its machine starting state. The reviewed default at source position 35 is N; alternative M gives PROTIBODVVKY. SPANLELSKE and PROTIBODAVKY preserve two garbled letters in this copy. Source letters are not edited to obtain correct words. XXXX is X padding, supported by sentence-ending X and terminal XX in 373.')
h('Readable Slovak reconstruction from the published draft')
p('A upozorňuje španielské protidodávky už pevne kúpené na základe pôvodných cien celulózy.')
p('English translation: And points out that the Spanish counter-deliveries have already been firmly purchased on the basis of the original cellulose prices. This is a content reconstruction supported by the published draft, not an error-free literal machine output.')
h('How the key was recovered')
p('The final 186-letter sentence of 373 contains no numerals. Sliding it through the complete ciphertext and testing periods 2-52 produces one witness in 94,656 cases: J normalized to I, no Q wrapper, offset 462, period 23. All 183 non-erased equations agree. Three independent physical control messages are recovered in full. Two distinct audits confirm one compatible 23-stop mask on the 52-hole wheel.')
p('Of all 598 phase/displacement pairs for 374, phase 3 and shift 8 are uniquely strongest: the reviewed reading matches 74 of 76 content letters; the next candidate matches 21, median 3. Independent source readings predate key recovery. The same key reads the entire 645-letter body of 373, including 459 letters outside the fitted 186-letter span. Running Slovak with spelled-out numbers and sentence-ending X strongly validates the key; literal source errors remain.')

story.append(PageBreak());h('Working physical key')
p('P and O map letters to coordinates 0-25; O(c)=P(p)+d modulo 26. P(A)=O(A)=0 is a coordinate convention. The table canonically completes unused F/G/J/Q/W labels; their historical positions were not recovered. M at 24 is supplied by held-out MADRID in 373; sentence boundaries and terminal XX support X at 19. Unused completions do not affect the body of 374.')
for start in [0,13]:
    letters=[chr(65+i) for i in range(start,start+13)]
    rows=[['Letter']+letters,['P']+key['input_positions'][start:start+13],['O']+key['output_positions'][start:start+13]]
    table=Table(rows,colWidths=[52]+[34]*13,hAlign='LEFT');table.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'DV'),('FONTSIZE',(0,0),(-1,-1),8),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#edf1f5')),('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#cad2dc')),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]));story.append(table);md.append('\n'.join('| '+' | '.join(map(str,row))+' |' for row in rows))
p('Selected holes in walking order from the first body letter, ZERO-BASED indices 0-51 (add 1 for human hole labels 1-52):')
literal(' '.join(map(str,key['holes_zero_based'])))
p('Initial displacement 1 modulo 26, equivalent to 27. After each letter, walk adjacent edges to the next selected hole. The 52 adjacent distances are:')
literal(' '.join(map(str,key['adjacent_distances'])))
p('One revolution sums to 179. Decode by subtracting the current displacement from O and locating the resulting coordinate in P. The historical dial setting, indicator coding and unused alphabet labels are not established. Mask uniqueness applies only to this geometry and the frozen recovered schedule.')
h('Reproduction and independent verification')
literal('python3 ciphers/hcp-374/work/decrypt.py')
p('Run from the repository root. Python checks the original JPEG and manual-transcription hashes; it does not perform OCR. It returns all 80 body letters and the indicator separately. --alternate-35-m selects the other reading. A separate verify.py uses absolute coordinates and wrap counts. An internal GPT-6.1 Sol audit used its own continuous physical algorithm without importing these functions: both complete 80-letter readings re-encode exactly to their source transcriptions.')
h('Independent review and remaining limits')
review=CIPHER/'review/REVIEW1.md'
if args.final:
    verdict=review.read_text().splitlines()[0];p('Claude Opus 5.5: '+verdict+', no second round required. His independent decoder verified the complete body, all 598 settings and the body of 373. Changes after review: default N at 35 with M retained, the 459-letter held-out test, observed X preparation and two garbles in this copy. Extending the requested 15 groups to a word boundary and repadding yields 16; this is an explanatory inference. Full responses are in SOLUTION.md.')
else:p('External review is pending. This working draft is not the final report or confirmation of a complete historical solution.')
p('Readers prefer G/Q/V at source positions 9/25/60. At 35, the reviewed default is the older independent N; the newer M reading remains an alternative. Source 21 S and 32 L are not changed to W/A: they are garbles in this copy, with their cause unresolved. The updated review confirms shared KIDAH and the same starting state (first selected stop, displacement 1). The sentence begins after 567 body emissions in 373, but from the start in 374: zero of 76 ciphertext letters agree, versus 74 plaintext letters. It was re-enciphered, not copied; indicator coding remains open. No register entry is written without separate human authorization because the content was already public.')
p('Sources: crypto.hcportal.eu/dashboard/cryptograms/374 and /373; all three rendered tabs and attachments recorded in SOURCES.md. Antal/Zajac/Grošek, Diplomatic Ciphers Used by Slovak Attaché During the WW2, HistoCrypt 2020; wheel geometry from Callimahos, Military Cryptanalytics Part III, §52. Main solver: OpenAI GPT; mathematical recovery and internal audits: GPT-6.1 Sol; external reviewer identified in REVIEW1.md.')

story.append(PageBreak());h('Original document 374')
p('Unmodified archival image from the recorded portal attachment. The manual transcription and its alternatives are kept separate from the image.')
image=Image(str(CIPHER/'source/cryptogram.jpg'));image.drawWidth=505;image.drawHeight=505*image.imageHeight/image.imageWidth;story.append(image)
md.append(f'![Original scan]({CIPHER}/source/cryptogram.jpg)')
(args.output_dir/'report.md').write_text('\n\n'.join(md)+'\n')
SimpleDocTemplate(str(args.output_dir/'report.pdf'),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=38,bottomMargin=42,title='HCP374: reviewed Madrid telegram',author='OpenAI GPT solver; GPT-6.1 Sol solver team; Claude Opus5.5 review').build(story,onFirstPage=footer,onLaterPages=footer)
print(args.output_dir/'report.pdf')
