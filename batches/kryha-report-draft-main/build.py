from pathlib import Path
import json,textwrap,re,html,argparse
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Preformatted,PageBreak,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
root=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent);args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True)
font=Path('/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
pdfmetrics.registerFont(TTFont('DVS',str(font/'DejaVuSans.ttf')));pdfmetrics.registerFont(TTFont('DVS-Bold',str(font/'DejaVuSans-Bold.ttf')));pdfmetrics.registerFont(TTFont('DVM',str(font/'DejaVuSansMono.ttf')))
styles=getSampleStyleSheet()
for k in ('Normal','BodyText','Title','Heading1','Heading2'):styles[k].fontName='DVS'
styles['Normal'].fontSize=9;styles['Normal'].leading=12;styles['Normal'].spaceAfter=7
styles['Title'].fontSize=19;styles['Title'].leading=25;styles['Title'].spaceAfter=15
styles['Heading2'].fontName='DVS-Bold';styles['Heading2'].fontSize=11;styles['Heading2'].leading=15;styles['Heading2'].spaceBefore=12;styles['Heading2'].spaceAfter=7
mono=ParagraphStyle('Mono',fontName='DVM',fontSize=7.4,leading=10,spaceAfter=10)

def readable(text):
 fixes={'WORKING DRAFT':'WORKING DRAFT','Firstfive':'First five','sourcecharacters':'source characters','allrenderedtabs':'all rendered tabs','immutableimages':'immutable images','published350/351plaintext':'published 350/351 plaintext','were separately':'were separately','391/392/394were':'391/392/394 were','unknownprefix':'unknown prefix','Unknownprefix':'Unknown prefix','sourceprefixes':'source prefixes','doubledT':'doubled T','missingfinalE':'missing final E','Sentence-boundary':'Sentence boundary','spaces,accents':'spaces, accents','transmission,preparation':'transmission, preparation','PartIII':'Part III','Antal/Zajac/Grošek,Diplomatic':'Antal/Zajac/Grošek, Diplomatic','DuringWW2,HistoCrypt':'During WW2, HistoCrypt','German procedures':'German procedures','NR2417German':'NR2417 German','unchangedphysical':'unchanged physical','defaultcollated':'default collated','strong351':'strong 351','uncertain351':'uncertain 351','glyph reading':'glyph reading','sha256':'SHA-256','Natural-word':'Natural word','oldG':'old G','oldQ':'old Q','oldX':'old X','unusedoldJ':'unused old J','rank1':'rank 1','335':'335'}
 for a,b in fixes.items():text=text.replace(a,b)
 text=text.replace('Defaultcollated','Default collated').replace('for350','for 350').replace('stops (zero-based,','stops (zero-based, ').replace('spaces,accents','spaces, accents').replace('text,source','text, source').replace('copy,','copy, ')
 parts=re.split(r'(https://\S+)',text)
 for i in range(0,len(parts),2):
  parts[i]=re.sub(r'(?<=[a-z])(?=\d)|(?<=\d)(?=[A-Za-z])',' ',parts[i])
  parts[i]=re.sub(r',(?=[A-Za-z])|;(?=[A-Za-z0-9])',lambda m:m.group()+' ',parts[i])
  parts[i]=parts[i].replace('cipherletter','cipher letter').replace('addingI','adding I').replace('copy,  ','copy, ').replace('text.350','text. 350').replace('T,PSED','T, PSED')
 return ''.join(parts)
def para(story,text):story.append(Paragraph(html.escape(readable(text)),styles['Normal']))
def heading(story,text):story.append(Paragraph(html.escape(text),styles['Heading2']))
def literal(story,text):story.append(Preformatted('\n'.join(textwrap.wrap(text,88)),mono))
def footer(canvas,doc):
 canvas.setFont('DVS',7);canvas.setFillColor(colors.HexColor('#667080'));canvas.drawString(42,26,'HC Portal | solver draft | external review pending');canvas.drawRightString(A4[0]-42,26,str(doc.page))
for n in (350,351):
 d=root/f'ciphers/hcp-{n}';w=d/'work/kryha-decipherment';key=json.loads((w/'key.json').read_text());raw=(w/'prepared-plaintext.txt').read_text().strip();ed=(w/'editorial-reading.txt').read_text().strip();tr=(w/'english-translation.txt').read_text().strip();story=[]
 story.append(Paragraph(f'HC{n}: car-purchase telegram',styles['Title']))
 para(story,'WORKING DRAFT - not yet reviewed by Claude. Proposed content decipherment, incomplete historical preparation. No register entry. 11 October 2026.')
 heading(story,'Origin and claim')
 para(story,f'MZV message No.{3001 if n==350 else 3002}/1944, Cieker to MZV Bratislava, Slovak National Archive, MZV box42. Portal status Not solved; its Unsolvable label is not treated as a mathematical result. '+('Portal date28February1944.' if n==350 else 'Portal date3November1944 is disputed by arrival stamp2.III.44-23; exact dispatch date is not established.'))
 para(story,'We recover a coherent car-purchase/loan message and a full physical23-stop adjustable Kryha key. Every385character position of the declared manual source transcription decodes and re-encrypts exactly. The first5source letters SOSOL remain unexplained. Exact historical I/J preparation and rare input-letter labels are not established. This report keeps literal output separate from an editorial reconstruction.')
 heading(story,'Method and validation')
 para(story,'The human-supplied Claude batch review identified the decisive350[i] to351[i+1] relationship of period23. The solver team then independently recovered the common output cycle by finite-field/CRT error-tolerant analysis, solved ordered two-mask wheel constraints, and ranked input-ring/physical-mask candidates by generic Slovak n-grams. The reviewer cycle and a target plaintext were not seeded into recovery.')
 para(story,'The final fixed-input-ring pass exhausts1,084,757 physically admissible paths; input neighbors are then tested. Fresh385-letter TEST controls recover both full texts conditional on supplied output ring O and displacement-difference ΔK. These are language/physical-stage controls, not end-to-end ciphertext-only complete-key recovery. Independent adjacent-hole decoding and a separate encoder audit reproduce every source position for both target keys. Exact re-encryption establishes consistency, not every glyph or historical rule.')
 heading(story,'Physical key')
 para(story,'Input letters at coordinates0-25: JERGZMPADHLQTVNYFSBUICXKOW. Output letters at coordinates0-25: AKXRMDTGJWNHVIPULYESZQBFOC. Initial stop47, displacement0. One ordinary press per character, clockwise adjacent-hole walk.')
 para(story,'Selected stops (zero-based,23of52): '+', '.join(map(str,key['holes']))+'. All23arcs traverse the52holes once and sum179 units.')
 para(story,'Adjacent physical distances, indices0-51: '+', '.join(map(str,key['adjacent_distances']))+'.')
 para(story,'For cipherletter c at displacement D, output P[(O(c)-D)mod26]; then advance D by the next selected-stop arc. Key JSON stores P as coordinate-to-letter indices and O as letter-to-coordinate indices, the inverse of the printed output ring. The two messages differ by selected hole0 in350 replaced with48 in351.')
 para(story,'The printed input ring explicitly applies semantic relabeling oldG→X,oldQ→G,oldX→J,unusedoldJ→Q to the blind6-gram key. EXISTUIE and TELEGRAFUI support this interpretation; the frozen model does not uniquely settle the rare labels. It is not proof of historical sentence J or I/J merging. We do not import German commercial J/extra-press rules.')
 reproduce_start=len(story)
 heading(story,'Reproduce')
 literal(story,f'python3 ciphers/hcp-{n}/work/kryha-decipherment/decrypt.py')
 para(story,'Run from repository root with Python3 standard library. Original source-image SHA256 values and manual transcription hashes are checked before decoding. No supplied source transcription exists: this is source-bound manual reading, not OCR. Defaultcollated contains strong351240U→J correction; --variant strong preserves the older snapshot. --variant collated-moderate adds uncertain351231L→I. Older --variant moderate preserves disputed stamp alternatives and is not the preferred glyph reading. For350 variants are identical. No language cleanup is performed.')
 story[reproduce_start:]=[KeepTogether(story[reproduce_start:])]
 literal_start=len(story)
 heading(story,'Literal prepared plaintext: all 385 characters')
 literal(story,raw)
 story[literal_start:]=[KeepTogether(story[literal_start:])]
 heading(story,'Readable Slovak reconstruction: editorial')
 para(story,'[Firstfive sourcecharacters unexplained.] '+ed)
 heading(story,'English translation of the reconstruction')
 para(story,'[Firstfive sourcecharacters unexplained.] '+tr)
 heading(story,'Remaining uncertainty')
 para(story,'Unknownprefix raw '+key['plaintext'][:5].upper()+'. Both sourceprefixes are clear SOSOL; alternative pressing/reset hypotheses do not select a unique plaintext. Sentence-boundary J and internal I/J interpretation are lexical hypotheses. PATDESATPAT is edited to päťdesiatpäť by addingI; spaces,accents and local error repairs are not exact machine output.350 DRAAE/POPROT/PRISTUPIK remain literal errors;351 has damaged MNOHZJH,doubledT,PSEDAVAIUCI,missingfinalE and an ambiguous231glyph. The source-supported240J correction fixes LACNEISIA without refitting the key. No printed letter is changed only to force prose.')
 para(story,'The default aligned interior still has five discrepancies between copies; the separate231I alternative leaves four. Differences may reflect source,transmission,preparation or genuine textual changes; their causes are not proved. The old20-letter prefix/10-letter suffix framing conjecture is withdrawn: most of the opening and DOTROCHDNI ending are plaintext. Input-alphabet uniqueness is not claimed.')
 heading(story,'Sources and review')
 para(story,f'Portal https://crypto.hcportal.eu/dashboard/cryptograms/{n}; allrenderedtabs and immutableimages are attributed in the cipher SOURCES.md. No published350/351plaintext was used. Solved391/392/394were separately read as attributed context for other telegrams. The car text is recovered here, not imported from those records.')
 para(story,'Machine geometry: Callimahos,Military Cryptanalytics PartIII(1977),§52,pp184-185, public primarycopy https://www.governmentattic.org/41docs/NSAmilitaryCryptalyticsPt3_1977.pdf. Slovak contextual evidence: Antal/Zajac/Grošek,Diplomatic Ciphers Used by Slovak Attaché DuringWW2,HistoCrypt2020,pp25-26. SSA NR2417German procedures do not establish this traffic’s SOSOL or I/J preparation.')
 para(story,'Solver: main OpenAI GPT with GPT-6.1 Sol subagents; earlier GPT-6 Astra attempts retained as provenance. Independent provider reviewer Claude is pending after DONE1; this draft does not claim its acceptance. Final report must include the actual verdict and each response before FINAL. No register entry for this partial claim.')
 # Editable source accompanies draft; never writes to frozen cipher directories.
 md=f'# HC{n} car-purchase telegram - unreviewed draft\n\n'
 def source_text(x):
  if hasattr(x,'_content'):return '\n\n'.join(source_text(y) for y in x._content)
  if hasattr(x,'getPlainText'):return x.getPlainText()
  return '\n'.join(getattr(x,'lines',[]))
 md+='\n\n'.join(source_text(x) for x in story)
 (args.out/f'hcp-{n}-report.md').write_text(md+'\n');SimpleDocTemplate(str(args.out/f'hcp-{n}-report.pdf'),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=40,bottomMargin=43).build(story,onFirstPage=footer,onLaterPages=footer)
 print(n)
