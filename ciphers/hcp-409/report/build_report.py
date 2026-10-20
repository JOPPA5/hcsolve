from pathlib import Path
import json,html,textwrap,subprocess,sys
from reportlab.platypus import SimpleDocTemplate,Paragraph,Preformatted,PageBreak,Table,TableStyle,Image,Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
c=Path(__file__).resolve().parents[1];out=Path(__file__).resolve().parent
assert(c/'REVIEWED1').exists()and not(c/'FINAL').exists()
font=Path('/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
for name,file in[('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf'),('DVM','DejaVuSansMono.ttf')]:pdfmetrics.registerFont(TTFont(name,str(font/file)))
styles=getSampleStyleSheet()
for name in['Normal','Title','Heading2']:styles[name].fontName='DV'
styles['Normal'].fontSize=9;styles['Normal'].leading=13;styles['Normal'].spaceAfter=9
styles['Title'].fontName='DVB';styles['Title'].fontSize=20;styles['Title'].leading=25
styles['Heading2'].fontName='DVB';styles['Heading2'].fontSize=11;styles['Heading2'].leading=15;styles['Heading2'].spaceBefore=8;styles['Heading2'].spaceAfter=6
mono=ParagraphStyle('Mono',fontName='DVM',fontSize=7.5,leading=10,spaceAfter=8)
key=json.loads((c/'work/key.json').read_text());raw=json.loads(subprocess.check_output([sys.executable,str(c/'work/decrypt.py'),'--json']))['plaintext'].upper();sk=(c/'work/editorial-reading-sk.txt').read_text().strip();en=(c/'work/translation-en.txt').read_text().strip();story=[]
def p(t):story.append(Paragraph(html.escape(t),styles['Normal']))
def h(t):story.append(Paragraph(html.escape(t),styles['Heading2']))
def pre(t):story.append(Preformatted('\n'.join(textwrap.wrap(t,90)),mono))
def footer(canvas,doc):canvas.setFont('DV',7);canvas.setFillColor(colors.HexColor('#536174'));canvas.drawString(44,25,'HCP409 | Reviewed decipherment | 19 October 2026');canvas.drawRightString(A4[0]-44,25,str(doc.page))
story.append(Paragraph('HCP409: Madrid telegram',styles['Title']))
p('MZV 80262/1944, 9 September 1944. Polyak to the Slovak legation in Madrid. Slovak National Archive, MZV, box 42. The handwritten cover changes Bern to Madrid. Portal status at acquisition: Not solved.')
p('All 295 observed letters decode with the previously reviewed HCP374 Madrid Kryha key, using a new starting phase and displacement. Claude Opus 5.5 independently confirmed the message and key. Its REVISE verdict required four transcription corrections; they are adopted, with no second round required. No numerical key field changed.')
h('Exact reviewed prepared output')
pre(raw)
p('The output retains the inherited canonical W at coordinate 22 and J at 15. W is interpreted as G in A?ENT- contexts; J marks three sentence boundaries, and word-internal I may represent J. These readings are well supported, but unused historical input labels remain unrecovered.')
h('Readable Slovak reconstruction')
p(sk)
p('This paragraph supplies accents, spacing and punctuation. It applies the disclosed letter conventions, restores the absent N in AWETOV, and reads literal DAKONCUIE as dokončuje. It is not the exact machine output or a surviving archival draft.')
h('English translation')
p(en)
p('The historical message is propaganda. Its characterizations and reported story about Tiso and the government are preserved as documentary assertions, not accepted as historical facts.')
story.append(PageBreak());h('Method and working physical key')
p('The 374 key was recovered earlier with attributed public HCP373 context. This is key transfer, not ciphertext-only ring recovery. Generic Slovak four-gram scoring tested 3 fixed keys, 2 prefix choices, 23 phases and 26 displacements (3,588 cases). The unique coherent full setting is 374, omit zero, phase 11 in its saved ordering, displacement 12. No 409 plaintext was supplied to the search.')
p('P and O below map alphabetical A-Z labels to coordinates 0-25; O(cipher)=P(plain)+D modulo 26. The numerical rings and selected-hole set are unchanged from 374.')
for start in[0,13]:
 rows=[['Letter']+[chr(65+i)for i in range(start,start+13)],['P']+key['input_positions'][start:start+13],['O']+key['output_positions'][start:start+13]]
 t=Table(rows,colWidths=[40]+[34]*13);t.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'DV'),('FONTSIZE',(0,0),(-1,-1),8),('GRID',(0,0),(-1,-1),.3,colors.HexColor('#cbd4df')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#edf2f7')),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]));story.append(t);story.append(Spacer(1,5))
p('Selected holes, zero-based, starting at the first observed ciphertext letter:')
pre(' '.join(map(str,key['holes_zero_based'])))
p('Initial displacement: 12 modulo 26. Decode at D, then walk the saved adjacent wheel edges to the next stop after each letter. A full revolution sums to 179. The 52 adjacent distances are:')
pre(' '.join(map(str,key['adjacent_distances'])))
h('Reproduction and verification')
pre('python3 ciphers/hcp-409/work/decrypt.py')
p('Run from the repository root with Python 3. It checks immutable source and manual-reading hashes; it does not perform OCR. --json reports 295 decoded letters and exact re-encryption. A separate coordinate decoder agrees. The reviewer independently reads the 374 key and reproduces the entire text; its own 598-setting search singles out the same setting.')
h('Limits and sources')
p('The handwritten count appears 300, while 59 visible groups contain 295 letters. A clerk count is plausible; it does not establish a missing group. The plaintext begins and ends coherently. The precise cause of AWETOV and DAKONCUIE remains uncertain. Unique hardware settings, the daily-key procedure and unused alphabet labels are not established.')
p('Sources: crypto.hcportal.eu/dashboard/cryptograms/409 (all three rendered tabs, 19 October 2026); original source images on the following pages. Key provenance: ciphers/hcp-374/work/key.json and its attributed public HCP373 context. Two bounded prior-solution web queries found no relevant 409 solution; worldwide novelty is not proved.')
story.append(PageBreak());h('Independent review and corrections')
p('Reviewer: Claude Opus 5.5, 19 October 2026. Verdict: REVISE, explicitly confirming the decipherment and requiring no further round after the four source-reading changes below. The original review and marker are preserved.')
rows=[['Position','Earlier','Reviewed','Effect'],['121','LHGUL','HHGUL','RKO -> AKO'],['161','EXZVO','AXZYO','ZATM... -> ZATK...'],['164','V','Y','...NUSIE -> ...NUTIE'],['224','IIAEY','IIAAY','CESKKCH -> CESKYCH']]
rows=[[Paragraph(html.escape(x),styles['Normal'])for x in row]for row in rows]
t=Table(rows,colWidths=[55,95,100,235]);t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.3,colors.HexColor('#cbd4df')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#edf2f7')),('VALIGN',(0,0),(-1,-1),'TOP')]));story.append(t);story.append(Spacer(1,10))
p('All positions here and in the solver manifests are one-based. The review table used zero-based positions, so add one when comparing. The old Y-to-V change at 164 was wrong and has been reversed. QMQHH stays unchanged and yields KTORYM. The earlier literal garbles RKO, ZATMNUSIE and CESKKCH were transcription errors, not errors of the encipherer.')
p('The corrections are supported by reviewer crops and reinspection of the original pixels. This work was assisted by the plaintext and review, not blind. Source files remain unchanged. The full DONE1 documentary state and the first-pass transcription are archived separately; all hashes and changes are recorded.')
p('The two remaining substantive irregularities are AWETOV (one N absent in the intended word agentov) and DAKONCUIE (A where the intended word has O). Their readable restoration is editorial. The omission is compatible with a preparation or encryption-time slip, but its exact cause is not independently established.')
p('W/G and J-boundary readings receive stronger support from this message. The numerical key remains frozen, and unused positions stay canonical. The handwritten count is described as such; no absent indicator group is invented. The bounded novelty search remains expressly limited.')
h('Authorship and local register record')
p('Solver: OpenAI GPT (GPT-6; exact variant not exposed in this session). Independent review: Claude Opus 5.5. The local register entry uses solver TODO because no human name was supplied. The content/key result is finalized after the documented corrections. No online register submission, commit or push is claimed.')
h('Protected evidence')
p('The original source-image SHA-256 values are checked before every decode. The reviewed transcript and key are in work/. No review-owned file was changed. The report includes both original images on the next pages.')
story.append(PageBreak());h('Original ciphertext scan')
p('Immutable source/cryptogram.jpg. The watermark and handwritten count are part of the preserved source.')
img=Image(str(c/'source/cryptogram.jpg'));img._restrictSize(480,650);story.append(img)
story.append(PageBreak());h('Original cover and destination correction')
p('Immutable source/context.jpg. Bern is crossed out and Madrid added; the subject identifies information about partisans and Slovakia.')
img=Image(str(c/'source/context.jpg'));img._restrictSize(480,650);story.append(img)
SimpleDocTemplate(str(out/'report.pdf'),pagesize=A4,leftMargin=44,rightMargin=44,topMargin=40,bottomMargin=40,title='HCP409 - reviewed Kryha decipherment',author='OpenAI GPT; independent review Claude Opus5.5').build(story,onFirstPage=footer,onLaterPages=footer)
(out/'report.md').write_text((c/'SOLUTION.md').read_text())
print(out/'report.pdf')
