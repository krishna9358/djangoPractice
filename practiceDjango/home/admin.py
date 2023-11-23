from django.contrib import admin
from . import models
# Register your models here.

    class notesAdmin(admin.notesAdmin):
        pass

admin.site.register(models.notes)
admin.site.register(models.notes2)
