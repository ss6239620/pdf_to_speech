import gtts
from PyPDF2 import PdfReader
import os

print(gtts.lang.tts_langs())
lang=str(input('Enter your language: '))

reader=PdfReader(r'C:\tutorial\project\html\sample.pdfhi')
page=reader.pages[0]
text=page.extract_text()

var1=gtts.gTTS(text,lang=lang,slow=False)

var1.save(r'C:\tutorial\project\html\test.mp3')

os.system('start C:\\tutorial\project\html\\test.mp3')