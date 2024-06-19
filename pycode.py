import qrcode as qr
img =qr.make("https://www.google.co.in/")
img.save("goggle_page.png")