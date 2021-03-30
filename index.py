import PyPDF2 as p2

book_data = {}

file = p2.PdfFileReader("cp.pdf")

book_data["description"] = file.documentInfo
book_data["total Pages"] = file.getNumPages()

# print(book_data)

str = " "
for i in range(1, 5):
    str += file.getPage(i).extractText()

with open("text.txt", "w", encoding='utf-8') as f:
    f.write(str)
