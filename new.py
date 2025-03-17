import qrcode

# URL of the PDF
url = "https://res.cloudinary.com/dsnmvwbvj/image/upload/v1742231258/fire_noc_Rudra_Prajapati_.pdf"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill="black", back_color="white")
img.save("fire_noc_qr.png")

print("QR code saved as fire_noc_qr.png")
