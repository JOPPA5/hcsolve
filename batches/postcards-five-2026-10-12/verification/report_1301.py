from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
import re
R=Path(__file__).resolve().parents[3]; p=R/'ciphers/hcp-1301'; out=p/'report';out.mkdir(exist_ok=True)
if (p/'FINAL').exists():raise SystemExit('Already final; refuse regeneration')
font='/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/poppler/fonts/DejaVuSans.ttf'
pdfmetrics.registerFont(TTFont('DejaVu',font))
styles=getSampleStyleSheet()
for st in styles.byName.values():st.fontName='DejaVu'
styles['BodyText'].fontSize=9; styles['BodyText'].leading=13
styles['Heading1'].fontSize=17;styles['Heading1'].leading=23
styles['Heading2'].fontSize=12;styles['Heading2'].leading=17;styles['Heading2'].keepWithNext=True;styles['Heading1'].keepWithNext=True
styles.add(ParagraphStyle('code',fontName='DejaVu',fontSize=7,leading=10,spaceAfter=7,wordWrap='CJK'))
s=(p/'SOLUTION.md').read_text(); (out/'report.md').write_text(s+'\n## Archived source provenance\n\n'+(p/'SOURCES.md').read_text())
flow=[]
def para(t,style='BodyText'):
 t=re.sub(r'\*\*(.*?)\*\*',r'\1',t);t=t.replace('`','')
 flow.append(Paragraph(escape(t),styles[style]))
 if not style.startswith('Heading'):flow.append(Spacer(1,6))
lines=s.splitlines();i=0;code=False
while i<len(lines):
 l=lines[i]
 if l.startswith('```'):code=not code;i+=1;continue
 if l.startswith('|'):
  rows=[]
  while i<len(lines) and lines[i].startswith('|'):
   cells=[c.strip() for c in lines[i].strip('|').split('|')]
   if not all(set(c)<=set('-: ') for c in cells):rows.append([Paragraph(escape(c),styles['BodyText']) for c in cells])
   i+=1
  table=Table(rows,colWidths=[45,195,45,195],repeatRows=1)
  table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e5edf3')),('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,0),(-1,-1),.3,colors.lightgrey)]));flow += [table,Spacer(1,10)];continue
 if l.strip():para(l[2:] if l.startswith('# ') else l[3:] if l.startswith('## ') else l.lstrip('> '),'Heading1' if l.startswith('# ') else 'Heading2' if l.startswith('## ') else 'code' if code else 'BodyText')
 i+=1
flow.append(PageBreak());para('Original address-side evidence','Heading1')
flow.append(Image(str(p/'source/address.jpg'),width=480,height=480*__import__('PIL').Image.open(p/'source/address.jpg').height/1024))
para('Source: HC Portal 1301, Tobias Schrödel collection. Original scan retained unchanged.','BodyText')
para('https://crypto.hcportal.eu/dashboard/cryptograms/1301','code')
para('Archived source provenance','Heading2')
for line in (p/'SOURCES.md').read_text().splitlines():
 if line.strip():para(line,'code')
def footer(c,d):
 c.setFont('DejaVu',8);c.setFillColor(colors.grey);c.drawString(48,26,'HCP1301 • reviewed reading, corrected documentary edition');c.drawRightString(547,26,str(d.page))
SimpleDocTemplate(str(out/'report.pdf'),pagesize=(595,842),rightMargin=48,leftMargin=48,topMargin=42,bottomMargin=45).build(flow,onFirstPage=footer,onLaterPages=footer)
print(out/'report.pdf')
