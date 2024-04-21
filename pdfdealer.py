from PyPDF4 import PdfFileReader, PdfFileWriter
from PyPDF4.pdf import PageObject
def add_watermark(input_pdf, output_pdf, watermark_file, coords):
file_name = input("Enter notes pdf: \n")
watermark_file = input("Enter watermark file name: \n")
coords = (220, 220, 400, 400)


watermark = PdfFileReader(watermark_file)
watermark_page = watermark.getPage(0)

pdf_reader = PdfFileReader(input_pdf)
pdf_writer = PdfFileWriter()

for page_num in range(pdf_reader.getNumPages()):
page = pdf_reader.getPage(page_num)
page.merge_page(watermark_page)
pdf_writer.addPage(page)

with open(output_pdf, 'wb') as out:
pdf_writer.write(out)

name = input("Enter file name you want to save as: ").strip(".pdf") + ".pdf"
add_watermark(file_name, name, watermark_file, coords)

pdf_reader = PdfFileReader(name)
pdf_writer = PdfFileWriter()

for page_num in range(pdf_reader.getNumPages()):
page = pdf_reader.getPage(page_num)
page.compressContentStreams()
pdf_writer.addPage(page)

with open("out.pdf", "wb") as f:
pdf_writer.wri