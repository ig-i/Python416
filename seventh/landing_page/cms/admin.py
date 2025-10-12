from django.contrib import admin
from .models import CmsSlider
from django.utils.safestring import mark_safe


class CmcAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')  # поля которые будут отображаться в админке
    readonly_fields = ('get_img',)                                       # вывод нередактируемого поля

    def get_img(self, obj):
        return mark_safe(f"<img src='{obj.cms_img.url}' width='80'>")

    get_img.short_description = 'Миниатюра'


admin.site.register(CmsSlider, CmcAdmin)

