import qrcode
generate_qr = input("Enter the text/link to generate qr coe : ")
img = qrcode.make(generate_qr)
qr_code = img.save("QRCode.jpg")