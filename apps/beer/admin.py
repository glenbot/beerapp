from django.contrib import admin
from models import Beer

class BeerAdmin(admin.ModelAdmin):
    list_display = ['name','type','style','description']
    
admin.site.register(Beer,BeerAdmin)