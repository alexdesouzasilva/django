from django.contrib import admin
from .models import *

#criando classe e add atributo de filtro por data de criação
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)
    readonly_fields = ('user',)
    exclude = ('favorites', 'created_at', 'update_at',)
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'birth', 'specialtiesList', 'addressesList',)
    list_display_links = ('user', 'role',)
    empty_value_display = '----'
    list_filter = ('user__is_active', 'role')


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)