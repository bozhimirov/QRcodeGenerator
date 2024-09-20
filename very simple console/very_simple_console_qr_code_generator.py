import qrcode

# the data you want to encode in the QR code
data = input('Enter anything to generate QR code: ')
name = input('Enter name for the image: ')

# generate the QR code
qr = qrcode.QRCode(version=2, box_size=10, border=1)
qr.add_data(data)
qr.make(fit=True)

# create an image from the QR code
image = qr.make_image(fill='black', back_color='white')

# save the image
if name:
    image.save(f'{name}.png')
else:
    image.save('qr_code.png')
