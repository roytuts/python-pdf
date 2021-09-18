import PyPDF2

#pdf_in_file = open("simple.pdf",'rb')
pdf_in_file = open("gre_research_validity_data.pdf",'rb')

inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
pages_no = inputpdf.numPages
output = PyPDF2.PdfFileWriter()

for i in range(pages_no):
    inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
    
    output.addPage(inputpdf.getPage(i))
    output.encrypt('password')

    #with open("simple_password_protected.pdf", "wb") as outputStream:
    with open("gre_research_validity_data_password_protected.pdf", "wb") as outputStream:
        output.write(outputStream)

pdf_in_file.close()