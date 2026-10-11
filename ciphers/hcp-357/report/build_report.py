from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Preformatted,PageBreak
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
P=Path(__file__).resolve().parent
font=Path('/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/poppler/fonts/DejaVuSans.ttf')
pdfmetrics.registerFont(TTFont('DV',str(font)))
styles=getSampleStyleSheet()
for name in ['Normal','Title','Heading1','Heading2']:
 styles[name].fontName='DV'
styles['Normal'].fontSize=9.5;styles['Normal'].leading=14;styles['Normal'].spaceAfter=8
styles['Title'].fontSize=25;styles['Title'].leading=31;styles['Title'].textColor=colors.HexColor('#172B4D');styles['Title'].alignment=TA_LEFT
styles['Heading2'].fontSize=12;styles['Heading2'].leading=17;styles['Heading2'].spaceBefore=10;styles['Heading2'].textColor=colors.HexColor('#174A68')
styles['Code'].fontName='Courier';styles['Code'].fontSize=8.5;styles['Code'].leading=12;styles['Code'].spaceAfter=10
sections=[
('title','HC Portal 357'),
('subtitle','UNRESOLVED | Reviewed attempt | 11 October 2026'),
('body','No cipher key or supported plaintext was recovered. This report closes a reviewed attempt, not a decipherment. There is no register entry, original-language plaintext, or plaintext translation.'),
('heading','Origin and evidence'),
('body','The portal identifies this as MZV message 80132/1944, dated 15 March 1944, from Belnay to the Slovak legation in Sofia. Archive: Slovak National Archive in Bratislava, MZV, box 42. The title concerns instructions for handing over decorations; it is contextual metadata, not a decrypted message. The scan includes two 15. III. 1944 stamps and a handwritten receipt time of 17.45.'),
('body','The source is the portal-displayed 1024-pixel-wide large image conversion. An original-resolution upload was not obtained. No transcription or solution attachment was shown. The image bytes remain unchanged. OpenAI GPT-6 Astra manually transcribed the body; Claude Opus 5.5 independently agreed with all 85 letters. Possible n/m ambiguities remain in groups 5 and 10.'),
('code','amaon yoato qcbzu mtrds ddnmn tooip\nyzlro vpatv pnyly hndei raaza oznrc\ncyiao ysoce rescm nnaaa vzvvk'),
('heading','Method and result'),
('body','The header 685 has a suffix matching the 85-letter body. The meaning of the leading 6 remains unresolved. The index of coincidence is 0.05742; removing group 3 yields 0.06234. These statistics are compatible with transposition, but do not identify a cipher.'),
('body','The historical R/XQ system is a candidate: three columnar transpositions with daily key permutations and a five-letter indicator. Neither its use here nor an indicator position is established. Searches covered simple routes, Caesar/reversal controls, and stochastic single-columnar variants of widths 2-30. Inputs included the full body, removal of group 3, and, after review, removal of group 6. None produced coherent plaintext.'),
('body','Two- and three-stage searches failed known-answer controls. Their target failures therefore have no evidential weight against multiple transposition or solvability. Single-columnar controls succeeded at width 11; that demonstrates limited capability, not exhaustive coverage of every width and transcription.'),
('page',''),
('heading','Independent review and corrections'),
('body','Claude Opus 5.5 returned REVISE in review/REVIEW1.md. The reviewer confirmed the transcription, checksums and byte-identical reproduction of eight output files. The reviewer explicitly required the outcome to remain unresolved and allowed an unresolved report after the corrections; no second round was required unless a plaintext emerged.'),
('body','1. The report and working notes now clearly separate limited single-columnar evidence from failed multi-stage optimization. Reviewer controls recovered 3/3 single-columnar examples, but 0/3 double and 0/3 triple examples.'),
('body','2. The suffix/length pattern is recorded. The requested group-6-removal search was completed in both directions. Best scores were 136.605 and 125.829; candidates remain incoherent. These scores are heuristic rankings, not decipherment confidence.'),
('body','3. Group 3 is no longer supported by the presence of Q: documented preparation permits Q as a plaintext separator. The unique B/U observation is weak and establishes no indicator.'),
('body','4. Equal stage widths were an unsupported simplification. Figure 5 of the historical paper uses widths 21, 19 and 20. Its example has alignment n=7, indicator position ip=5, and header 360. Consequently a universal rule equating the header prefix with alignment or indicator position is not supported. A different local convention remains possible.'),
('body','5. The large-conversion source limitation is explicit, both n/m uncertainties and receipt annotations are recorded in a working supplement, and the displayed source hash was corrected without changing source bytes. The full item-by-item response is in SOLUTION.md, section Response to review 1.'),
('heading','Reproduction and remaining uncertainty'),
('code','sh ciphers/hcp-357/work/reproduce.sh'),
('body','Run from the repository root. This regenerates diagnostic candidates from the manual transcription; it does not decrypt the source into a full plaintext. The exact cipher, daily key, indicator position, original-resolution readings, plaintext and translation are still unknown. Useful progress needs better source/key evidence or an attack validated on comparable multi-stage controls. No mathematical impossibility or unsolvability is claimed.'),
('heading','Sources and provenance'),
('body','Portal record: https://crypto.hcportal.eu/dashboard/cryptograms/357\nHistorical method: Antal, Zajac and Grošek, Diplomatic Ciphers Used by Slovak Attaché During the WW2, HistoCrypt 2020, pp. 22-23 and Figure 5. https://ep.liu.se/ecp/171/004/ecp2020_171_004.pdf'),
('body','Language scoring used fourgram log counts from Universal Dependencies Slovak SNK training text, documented in SOURCES.md. No published solution of this target was used. Local evidence: source/cryptogram.jpg, NOTES.md, SOLUTION.md, review/REVIEW1.md and work/.')]
md=[];story=[]
for kind,text in sections:
 if kind=='page':story.append(PageBreak());md.append('\n---\n');continue
 if kind=='code':story.append(Preformatted(text,styles['Code']));md.append('```\n'+text+'\n```');continue
 sty='Title' if kind=='title' else 'Heading2' if kind=='heading' else 'Normal'
 story.append(Paragraph(escape(text).replace('\n','<br/>'),styles[sty]));md.append(('# ' if kind=='title' else '## ' if kind=='heading' else '')+text)
(P/'report.md').write_text('\n\n'.join(md)+'\n')
def footer(c,doc):
 c.setStrokeColor(colors.HexColor('#CED8E0'));c.line(42,39,553,39)
 c.setFont('DV',7);c.setFillColor(colors.HexColor('#526274'));c.drawString(42,27,'HC Portal 357 | Unresolved attempt | Independent review: Claude Opus 5.5');c.drawRightString(553,27,str(doc.page))
doc=SimpleDocTemplate(str(P/'report.pdf'),pagesize=(595.28,841.89),rightMargin=42,leftMargin=42,topMargin=40,bottomMargin=50,title='HC Portal 357 - Unresolved reviewed attempt',author='OpenAI GPT-6 Astra; independent review by Claude Opus 5.5')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
