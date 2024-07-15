import qrcode

features = qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data('linkedin.com/in/subhra-chandan-7b54aa137')
features.make(fit=True)
myqr = features.make_image(fill_color="blue",back_color="white")
myqr.save("Subhra2.png")