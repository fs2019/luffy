from django.contrib import admin

from .models import Banner,Nav

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title','link','image_url','remark','is_show','orders','is_deleted')

@admin.register(Nav)
class NavAdmin(admin.ModelAdmin):
    list_display = ('title','link','is_show','is_site','position')
