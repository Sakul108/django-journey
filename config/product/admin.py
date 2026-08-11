from django.contrib import admin

from .models import ProductItem, Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ProductItem)