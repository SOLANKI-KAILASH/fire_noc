from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

# Define file path where the PDF will be saved
save_path = os.path.join("D:\Downloads", "fire_noc.pdf")  # Change the path as needed

# Create a PDF object
p = canvas.Canvas(save_path, pagesize=A4)
width, height = A4


print(f"PDF saved successfully at {save_path}")
