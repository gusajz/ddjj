from django.contrib import admin

from .models import Document, AffidavitTemplate, Person

admin.site.register(Document)
admin.site.register(AffidavitTemplate)
admin.site.register(Person)
