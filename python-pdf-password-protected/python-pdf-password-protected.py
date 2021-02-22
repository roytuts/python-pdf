import PyPDF2

pdf_in_file = open("simple.pdf",'rb')

inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
pages_no = inputpdf.numPages

for i in range(pages_no):
	inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
	
	output = PyPDF2.PdfFileWriter()
    
	output.addPage(inputpdf.getPage(i))
	output.encrypt('password')

	with open("simple_password_protected.pdf", "wb") as outputStream:
		output.write(outputStream)

pdf_in_file.close()