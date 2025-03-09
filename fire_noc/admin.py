from django.contrib import admin
from .models import FireNOCSubmission

class FireNOCSubmissionAdmin(admin.ModelAdmin):
    list_display=["name","email","phone","date","org_name","org_address"]

admin.site.register(FireNOCSubmission,FireNOCSubmissionAdmin)

