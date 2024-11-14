from django.contrib import admin
from .models import Watches, WatchesUploads

# Register your models here.
admin.site.register(Watches)
class WatchesUploadAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','image')

    list_filter = ('name','price')

    list_search = ('name','description')

admin.site.register(WatchesUploads,WatchesUploadAdmin)
