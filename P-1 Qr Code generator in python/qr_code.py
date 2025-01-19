"""This is a file which generates normal QR code"""

import qrcode as qr

#i want the qr in image format so inside the make method you can give url 
# or text message whatever you want.

"""Copy any url you want to create the QR code of and past it in the make method."""

img = qr.make("https://github.com/Suniksha12")

#save the file and add your extension .jpg or .png
img.save("suni_git.png")

#before running this write the command in your command prompt 
"""pip install pillow 
   pip show pillow"""

#now run the file traverse to your directory of your code you will see that the qr file is saved.