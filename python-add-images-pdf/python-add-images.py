import os
from fpdf import FPDF
#from PIL import Image

#pdf = FPDF(orientation = 'L')
pdf = FPDF()
pdf.add_page() #add a page first

#i = Image.open('flower.png')
#i_name = os.path.basename('flower.png')
#w, h = i.size
pdf.image('flower.png')
pdf.output("image.pdf", "F")

dirs = os.listdir('.')

pdf1 = FPDF()
#pdf1.add_page()
for img in dirs:
    if os.path.isfile(img) and os.path.splitext(img)[1].lower() in ('.jpg', '.jpeg', '.png'):
        #print(img)
        pdf1.add_page()
        pdf1.image(img)

pdf1.output("images.pdf", "F")