from django.contrib import admin

from .models import Makale
from .models import Slide

admin.site.register(Slide)


class MakaleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Makale, MakaleAdmin)
