from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase


class ImageInline(SortableStackedInline):
    def get_preview(self, obj):
        return format_html(f'<img src="{obj.image.url}" height=200px>')

    model = Image
    readonly_fields = ('get_preview', )
    fields = ('image', 'get_preview', 'position')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = (ImageInline, )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
