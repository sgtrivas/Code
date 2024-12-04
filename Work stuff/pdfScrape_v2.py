# simple pdf Scaper using PDFquery
import pdfquery as p
from bs4 import BeautifulSoup

pdf = p.PDFQuery(r"Annex A - Telework_Dos_and_Donts.pdf")
pdf.load()

pdf.tree.write('testPdf.xml', pretty_print = True)

# Load the XML file
with open("testPdf.xml", "r", encoding="utf-8") as file:
    content = file.read()

# Parse with BeautifulSoup
soup = BeautifulSoup(content, "xml")

# Find all LTTextLineHorizontal elements
lt_text_lines = soup.find_all("LTTextLineHorizontal")

# Display or process the text lines
for line in lt_text_lines:
    print(line.get_text()) 