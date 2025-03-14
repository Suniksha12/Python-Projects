from pdf2image import convert_from_path


#in the poppler_path added the path traverse and open the bin path
old_pdf = convert_from_path(r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-44 Convert Pdf to image using python\PHY1001_ENGINEERING-PHYSICS_LTP_1.0_1_PHY1001-Engineering Physics.pdf",
                            poppler_path=r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-44 Convert Pdf to image using python\poppler-24.08.0\Library\bin")

#couting the pages
for i in range(len(old_pdf)):
    old_pdf[i].save("new" + str(i)+".jpg","JPEG")