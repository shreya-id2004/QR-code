import qrcode

data = input("Enter the text or url to generate QR code: ")

qr = qrcode.QRCode(
    version = 1,  
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

print(f'QR code generated successfully and saved as qrcode.png')

# version : size of the QR code , that can hold the data
# error_correction : how much data can be lost
# box_size : size of each box in the QR code
# border : border size of the QR code
# fill_color : color of the QR code
# back_color : background color of the QR code
# make_image : generate the QR code image
# save : save the QR code image
# fit : fit the data into the QR code
# add_data : add the data to the QR code
# make : make the QR code

