from django.contrib import admin
from .models import District, Branch, MaterialOption,Form

# Register your models here.
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(MaterialOption)
admin.site.register(Form)

