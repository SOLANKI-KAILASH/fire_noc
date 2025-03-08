from django.shortcuts import render,redirect
from .models import FireNOCSubmission
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
# Create your views here.
def index(request):
    return render(request,"index.html")

def generate_fire_noc_pdf(request):
    if request.method == "POST":
        # Get form data
        site_address = request.POST["site_address"]
        fire_extinguisher = request.FILES["fire_extinguisher"]
        fire_exit = request.FILES["fire_exit"]
        fire_safety_sign = request.FILES["fire_safety_sign"]
        water_infrastructure = request.FILES["water_infrastructure"]

        # Save data in database
        noc = FireNOCSubmission.objects.create(
            site_address=site_address,
            fire_extinguisher=fire_extinguisher,
            fire_exit=fire_exit,
            fire_safety_sign=fire_safety_sign,
            water_infrastructure=water_infrastructure,
        )
    # Get user input (assuming data is coming via POST request)
        site_address = request.POST.get("site_address", "Unknown Address")
        
        # Create a response object for a PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="fire_noc.pdf"'

        # Create a PDF object
        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        # Title
        p.setFont("Helvetica-Bold", 18)
        p.drawString(200, height - 50, "FIRE NOC CERTIFICATE")
        
        # Address Section
        p.setFont("Helvetica", 12)
        p.drawString(50, height - 100, f"Site Address: {site_address}")
        
        # Approval Statement
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, height - 150, "This is to certify that the Fire NOC has been issued")
        p.drawString(50, height - 170, "as per the required safety guidelines.")

        # Signature
        p.setFont("Helvetica-Oblique", 12)
        p.drawString(50, height - 250, "________________________")
        p.drawString(50, height - 270, "Authorized Signatory")

        # Save the PDF
        p.showPage()
        p.save()

    return response