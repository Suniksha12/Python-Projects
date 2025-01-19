"""This is a file which generates QR code but we can modfy its properties"""

import qrcode 

from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,border=10)

#add you url
qr.add_data("https://www.youtube.com/@Wonder_women-l8l/videos")

#change anything inside it
qr.make(fit=True)

#chnaged the color
img = qr.make_image(fill_color="pink",back_color="white")

#save the image
img.save("whoosh_tech_youtube.png")
