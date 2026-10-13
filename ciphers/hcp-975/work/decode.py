"""Apply Thomas's published 2016 key to a manual working transcription."""
from pathlib import Path
text=Path(__file__).with_name('transcription.txt').read_text()
key=str.maketrans('0123456789','saeioulmnr')
print(text.translate(key).replace('-',' '),end='')
