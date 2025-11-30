#pip install qrcode


import qrcode

data = input('Enter A url :').strip()
filename = input('Enter file Name :').strip()

qr = qrcode.QRCode(box_size=10, border=2)
qr.add_data(data)

image = qr.make_image(fill_color = 'black' , back_color = 'white')

image.save(filename)

print('Successfully and QR code generated!')

image.show(filename)

'''
from IPython.display import display
print(f'\t{filename}\n')
display(image)

'''