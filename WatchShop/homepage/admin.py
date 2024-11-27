from django.contrib import admin
from .models import Watches, WatchesUploads, Wishlist, Cart, WatchReview,CartItem
# Register your models here.

admin.site.register(Watches)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(WatchReview)
admin.site.register(CartItem)
class WatchesUploadsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'description', 'price', 'image','count')
    list_filter= ('name', 'price')
    search_fields = ['name', 'description']

admin.site.register(WatchesUploads, WatchesUploadsAdmin)
