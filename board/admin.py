from django.contrib import admin
from .models import ShopComment
# Register your models here.


class ShopCommentAdmin(admin.ModelAdmin):
    search_fields = ['content']


admin.site.register(ShopComment,ShopCommentAdmin)