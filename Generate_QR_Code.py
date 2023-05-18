import qrcode

toqr = input("Enter string to QR-ify: ")
print(toqr)

img = qrcode.make(toqr)

outputname = input("Save output QR code as: ")
type(img) #qrcode.image.pil.PilImage

img.save(f'{outputname}.png')