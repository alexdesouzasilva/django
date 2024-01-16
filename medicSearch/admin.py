from django.contrib import admin
from .models import *

#criando classe e add atributo de filtro por data de criação
class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)