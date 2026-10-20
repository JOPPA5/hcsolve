from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Image,Table,TableStyle,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
B=Path(__file__).resolve().parent;ROOT=B.parent
pdfmetrics.registerFont(TTFont('Arial','/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='ArialBold',italic='Arial',boldItalic='ArialBold')
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='Body',fontName='Arial',fontSize=10.2,leading=14.4,spaceAfter=9,textColor=colors.HexColor('#243440')));styles.add(ParagraphStyle(name='SmallBody',parent=styles['Body'],fontSize=8.5,leading=11.8));styles.add(ParagraphStyle(name='TitleA',fontName='ArialBold',fontSize=25,leading=29,textColor=colors.HexColor('#124f5c'),spaceAfter=12));styles.add(ParagraphStyle(name='SubA',parent=styles['Body'],fontSize=10,textColor=colors.HexColor('#56727a'),spaceAfter=18));styles.add(ParagraphStyle(name='HeadA',fontName='ArialBold',fontSize=13,leading=17,textColor=colors.HexColor('#124f5c'),spaceBefore=8,spaceAfter=8))
flow=[]
def p(s,style='Body'):flow.append(Paragraph(s,styles[style]))
def h(s):p(s,'HeadA')
def textparas(path):
 for line in path.read_text().strip().split('\n\n'):p(escape(line))
def footer(c,d):
 c.setStrokeColor(colors.HexColor('#c3d2d5'));c.line(48,42,547,42);c.setFont('Arial',8);c.setFillColor(colors.HexColor('#56727a'));c.drawString(48,28,'HC Portal 1098 | Reviewed decipherment | 19 October 2026');c.drawRightString(547,28,str(d.page))
p('A numerical postcard<br/>from 1909','TitleA');p('HC Portal 1098 - Complete reading, independently reviewed','SubA')
p('<b>Result.</b> The 312 numerical symbols use the ordinary alphabet order, A=1 through Z=26. The full message is readable English personal correspondence. Claude Opus 5.5 accepted the solution after checking every numerical group against the original scan.')
h('Origin and evidence')
p('The card is addressed to Mr. Homer Wright in Bernardston, Massachusetts. Its Brattleboro, Vermont cancellation is dated 25 March 1909. The sender is unnamed. HC Portal identifies the source as Tobias Schrödel\'s postcard collection and displayed Not solved when the solver inspected all three tabs on 19 October 2026.')
p('The picture side carries the numerical message and several words in ordinary script. The address side is ordinary addressing. Both original scans are preserved unchanged. No supplied target transcription or plaintext attachment was encountered.')
h('Method')
p('Each number n is replaced by the nth letter of the English alphabet. Dots separate numbers and dashes usually separate words. For example, 18.5.3.5.9.22.5.4 reads RECEIVED. Six words continue across source line breaks; rejoining them changes no letters. Cleartext spans are kept unchanged.')
h('Complete English text')
p('The following preserves the decoded words; sentence punctuation and capitalization are editorial. Original THEN, DONT, NETTIES, TO NIGHT and TO MORROW are retained.','SmallBody')
textparas(ROOT/'work/readable-en.txt')
flow.append(PageBreak());p('Translation and validation','TitleA')
h('Slovak translation')
textparas(ROOT/'work/translation-sk.txt')
h('Reproduce the complete reading')
p('From the repository root, with Python 3:', 'SmallBody')
p('<font name="Courier" size="8.7">python3 ciphers/hcp-1098/work/decrypt.py</font>')
p('The command verifies the original source hashes and decodes the explicit manual transcription. It does not perform OCR or pretend to decode image pixels. The --json option lists each source group, each decoded group, and all 22 physical source lines. A separate audit decodes and re-encodes every one of the 312 numerical positions and checks that the readable English has the same complete letter sequence.')
h('Independent review and response')
p('Claude Opus 5.5 returned ACCEPT in REVIEW1 on 19 October 2026. The reviewer used an independent decoder and enlarged crops covering the complete numerical message. No digit reading that changes a letter was found. All unenciphered spans were also checked.')
p('Minor comments: THEN may be read as period spelling for THAN; the literal form is retained. The writer is unnamed and no name, relationship or gender is inferred. This report supplies the previously pending final documentation. The Thursday postmark is consistent with writing on Wednesday evening, but that writing date is an inference rather than an explicit date on the message.')
h('Limits and attribution')
p('Netties is literally NETTIES, without an apostrophe. Nettie\'s identity is unknown. The last P.M. is preserved; afternoon is the natural contextual reading, while initials cannot be excluded solely from the letters. Unused alphabet entries are supplied by the standard A1Z26 convention, not separately attested in this message.')
p('The linked Schrödel 2021 paper is a collection overview. Its text and illustrated final page were checked; no plaintext of this particular card was encountered. This is not a claim of first-ever or first-private decipherment.')
p('Source page: https://crypto.hcportal.eu/dashboard/cryptograms/1098<br/>Collection paper: Tobias Schrödel, Cryptographic postcards, HistoCrypt 2021, DOI 10.3384/ecp183166.<br/>Solver: OpenAI GPT-6 (Codex). Independent reviewer: Claude Opus 5.5.','SmallBody')
flow.append(PageBreak());p('Original source scans','TitleA');p('Unmodified source images, reproduced for traceability. The original files accompany the executable reading.','SmallBody')
for filename,title in [('picture.jpg','Picture side: numerical message'),('address.jpg','Address side: recipient and cancellation')]:
 if filename=='address.jpg':flow.append(PageBreak())
 h(title);im=Image(str(ROOT/'source'/filename));w=490;im.drawHeight=im.imageHeight*w/im.imageWidth;im.drawWidth=w;flow.append(im);flow.append(Spacer(1,9))
doc=SimpleDocTemplate(str(B/'report.pdf'),pagesize=(595.276,841.89),leftMargin=48,rightMargin=48,topMargin=45,bottomMargin=55,title='HC Portal 1098 - Reviewed A1Z26 postcard',author='OpenAI GPT-6 (Codex); independent review Claude Opus 5.5');doc.build(flow,onFirstPage=footer,onLaterPages=footer)
