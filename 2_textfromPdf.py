# extracting_text.py
# extract text from pdf

from PyPDF2 import PdfFileReader
data = " "

def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        # get the #th page
        page = pdf.getPage(6)
        print(page)
        print('page type: {}'.format(str(type(page))))

        text = page.extractText()
        print(text)
        

if __name__ == '__main__':
    path = 'cp.pdf'
    text_extractor(path)
