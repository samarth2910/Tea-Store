from django.contrib import admin
from .models import Chai,Chai_Certificate,Chai_Review,Store
# Register your models here.

class Chai_ReviewInline(admin.TabularInline):
    model=Chai_Review
    extra=1

class ChaiAdmin(admin.ModelAdmin):
    list_display=("name","type","date_added","price")
    inlines = [Chai_ReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display=("name","location")
    filter_horizontal = ("chai",)
    
class Chai_CertificateAdmin(admin.ModelAdmin):
    list_display=("chai","certificate_number","issued_date","expiry_date")


admin.site.register(Chai, ChaiAdmin)
admin.site.register(Chai_Certificate, Chai_CertificateAdmin)
admin.site.register(Store, StoreAdmin)