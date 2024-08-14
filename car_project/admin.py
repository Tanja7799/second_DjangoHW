from django.contrib import admin
from .models import Car



class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'slug', 'model', 'country', "pover", 'fuel_type', 'is_available')
    list_editable = ('is_available',)
    list_filter = ('make', 'model', 'fuel_type')
    search_fields = ('make',)
    prepopulated_fields = {'slug': ('make', 'model')}


admin.site.register(Car, CarAdmin)
