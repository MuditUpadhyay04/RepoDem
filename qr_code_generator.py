import qrcode

UserValue = input('Enter the text or URL: ')
Name = input('What should be the name of your QR code? ')
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(UserValue)
img = qr.make_image(fill_color="black", back_color="white")
img.save(Name + '.jpg')