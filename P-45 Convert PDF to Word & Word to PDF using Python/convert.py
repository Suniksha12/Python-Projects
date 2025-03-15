from pdf2docx import Converter

old_pdf = r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-45 Convert PDF to Word & Word to PDF using Python\PHY1001_ENGINEERING-PHYSICS_LTP_1.0_1_PHY1001-Engineering Physics.pdf"

new_doc = "new.docx"

obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()