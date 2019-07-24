from django.contrib import admin
from .models import udata
# Register your models here.

class lview(admin.ModelAdmin):
    list_display=('name','status','gender','marital_status','interest_in','email','username','password','address','profile_picture')

admin.site.register(udata,lview)

 