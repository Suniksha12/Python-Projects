import pikepdf

old_pdf = pikepdf.Pdf.open(r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-36 Password Protected PDF Using Python\PHY1001_ENGINEERING-PHYSICS_LTP_1.0_1_PHY1001-Engineering Physics.pdf")

no_ext = pikepdf.Permissions(extract=False)

old_pdf.save("pro_new.pdf",
             encryption= pikepdf.Encryption(user="123asd",
                                            owner="whooshtech",
                                            allow=no_ext))  # Corrected variable name
