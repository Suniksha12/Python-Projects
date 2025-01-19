"""This is a file which generates QR code but we can modfy its properties"""

import qrcode 

from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)

#add you url
qr.add_data("https://www.youtube.com/@Wonder_women-l8l/videos")

#change anything inside it
qr.make(fit=True)

#chnaged the color
img = qr.make_image(fill_color="red",back_color="blue")

#save the image
img.save("whoosh_tech_U2be.png")
