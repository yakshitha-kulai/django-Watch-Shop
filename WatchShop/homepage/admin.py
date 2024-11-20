from django.contrib import admin
from .models import Watches, WatchesUploads, Wishlist, Cart, WatchReview
# Register your models here.

admin.site.register(Watches)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(WatchReview)

class WatchesUploadsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'description', 'price', 'image')
    list_filter= ('name', 'price')
    search_fields = ['name', 'description']

admin.site.register(WatchesUploads, WatchesUploadsAdmin)
