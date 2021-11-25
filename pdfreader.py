import typing
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction
import paths
pdf_array =[]
x = 1

# getting pdfs to pdf array
while(x<11):
    d: typing.Optional[Document] = None
    l: SimpleTextExtraction = SimpleTextExtraction()
    file_name = "{}/invoice-{}.pdf".format(paths.pdfPath,x)
    with open(file_name, "rb") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle, [l])
    assert d is not None
    myPDF = l.get_text_for_page(0)
    pdf_array.append(myPDF)
    x += 1

