import pikepdf

old_pdf = pikepdf.Pdf.open(r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-38 Split a Pdf into single page pdfs using python\PHY1001_ENGINEERING-PHYSICS_LTP_1.0_1_PHY1001-Engineering Physics.pdf")

for n,page_can in enumerate(old_pdf.pages):
    new_pdf = pikepdf.new()
    new_pdf.pages.append(page_can)
    name = "test" + str(n) + ".pdf"
    new_pdf.save(name)