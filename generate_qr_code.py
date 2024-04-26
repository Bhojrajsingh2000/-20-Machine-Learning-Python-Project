import qrcode 
from PIL import Image # using formatting

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=5,border=1,)
qr.add_data("https://github.com/Bhojrajsingh2000/Python-Project")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("Python-Project-github-repository.png")