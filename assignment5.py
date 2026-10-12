import qrcode

name = input("Enter your name or a short message: ")

img = qrcode.make(name)
img.save("personal_qrcode.png")

print("QR code generated and saved as 'personal_qrcode.png'. You can scan it to see your message!")

website = input("Enter a website URL to generate a QR code: ")

img2 = qrcode.make(website)
img2.save("website_qrcode.png")

print("QR code for the website generated and saved as 'website_qrcode.png'. You can scan it to visit the website!")
