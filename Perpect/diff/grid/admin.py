from django.contrib import admin
from .models import KeyModel, MasterModel, DetailModel

# Register your models here.

class KeyAdmin(admin.ModelAdmin):
    list_display = ['title', 'username']

class MasterAdmin(admin.ModelAdmin):
    list_display = ['key', 'master']

class DetailAdmin(admin.ModelAdmin):
    list_display = ['master', 'detail']

admin.site.register(KeyModel, KeyAdmin)
admin.site.register(MasterModel, MasterAdmin)
admin.site.register(DetailModel, DetailAdmin)