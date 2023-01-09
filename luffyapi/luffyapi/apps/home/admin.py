from django.contrib import admin

from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title','link','image_url','remark','is_show','orders','is_deleted')

