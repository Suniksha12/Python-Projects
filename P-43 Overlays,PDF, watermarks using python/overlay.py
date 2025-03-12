from pikepdf import Pdf, Page , Rectangle

old_pdf1 = Pdf.open(r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-43 Overlays,PDF, watermarks using python\PHY1001_ENGINEERING-PHYSICS_LTP_1.0_1_PHY1001-Engineering Physics.pdf")
old_pdf2 = Pdf.open(r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-43 Overlays,PDF, watermarks using python\Sowing_guide_EN.pdf")

des_page = Page(old_pdf1.pages[0])
sur_page = Page(old_pdf2.pages[0])

des_page.add_overlay(sur_page, Rectangle(0,0,500,500))

old_pdf1.save("new_pdf.pdf")