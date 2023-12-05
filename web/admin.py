from django.contrib import admin

from web.models import KindOfSport

class KindOfSportAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

admin.site.register(KindOfSport, KindOfSportAdmin)