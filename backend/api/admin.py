from django.contrib import admin
# Register your models here.
from .api.models import File


@admin.register(File)
class AdminPanelFile(admin.ModelAdmin):
	pass