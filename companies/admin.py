from django.contrib import admin

# Register your models here.
from .models import Companies,Finance
admin.site.register(Companies)
admin.site.register(Finance)
