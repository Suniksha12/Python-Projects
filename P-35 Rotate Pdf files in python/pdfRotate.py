import pikepdf

pdf_my = pikepdf.Pdf.open("C:/Users/sunik/OneDrive/Desktop/Python Projects/P-35 Rotate Pdf files in python/PHY1001_ENGINEERING-PHYSICS_LTP_1.0_1_PHY1001-Engineering Physics.pdf")

# print(pdf_my.pages)

for i in pdf_my.pages:
    i.Rotate = 180
    pdf_my.save("new_pdf.pdf")