from django.contrib import admin

# Register your models here.
from .models import Companies,Finances
admin.site.register(Companies)
admin.site.register(Finances)
