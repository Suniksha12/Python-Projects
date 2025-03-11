import pikepdf

old_pdf = pikepdf.Pdf.open(r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-41 Free PDF editor using python\PHY1001_ENGINEERING-PHYSICS_LTP_1.0_1_PHY1001-Engineering Physics.pdf")

#reversing the old pdf
old_pdf.pages.reverse()
old_pdf.save("rev_new.pdf")