from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CompanyDetails)
admin.site.register(Manufacturers)
admin.site.register(Products)
admin.site.register(Stock)
admin.site.register(Party)
admin.site.register(Invoice)
admin.site.register(Entry)
admin.site.register(SaveEntries)
admin.site.register(RateEntry)
admin.site.register(SaveRateEntries)
admin.site.register(SavedInvoice)

