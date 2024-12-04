# simple pdf Scaper using PDFquery
import pdfquery as p

pdf = p.PDFQuery(r"C:\Users\ssgnr\Downloads\You're going to Orlando on 08_04 (2JQF89)!.pdf")
pdf.load()

pdf.tree.write('customers2.xml', pretty_print = True)
#pdf



text_elements = pdf.pq('LTTextLineHorizontal:in_bbox("8, 599.161, 227.874, 606.661")').text()
#text_elements = pdf.pq('')


print(text_elements)