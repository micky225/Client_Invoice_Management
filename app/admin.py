from django.contrib import admin
from .models import Invoice
# Register your models here.

admin.site.site_title = 'app Admin'
admin.site.site_header = 'app Admin'

admin.site.register(Invoice)