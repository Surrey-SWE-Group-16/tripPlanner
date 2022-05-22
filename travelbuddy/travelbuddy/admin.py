from django.contrib import admin
from .models import MapModel, ChecklistModel, JournalModel

# Register your models here.
admin.site.register(MapModel)
admin.site.register(ChecklistModel)
admin.site.register(JournalModel)

