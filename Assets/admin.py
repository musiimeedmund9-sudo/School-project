from django.contrib import admin

from .models import (
    Employee, Store, Asset, Stock,
    StockItem, Requisition, RequisitionItem,
)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_fname", "employee_lname", "gender", "phone", "position", "department")


class StoreAdmin(admin.ModelAdmin):
    list_display = ("store_name", "store_location", "employee")


class AssetAdmin(admin.ModelAdmin):
    list_display = ("asset_name", "category", "brand", "stock_quantity", "re_order_level", "store")


class StockAdmin(admin.ModelAdmin):
    list_display = ("stock_date", "supplier", "total_amount", "received_by")


class StockItemAdmin(admin.ModelAdmin):
    list_display = ("stock", "asset", "quantity", "unit_price")


class RequisitionAdmin(admin.ModelAdmin):
    list_display = ("requisition_date", "employee", "requisition_state", "total_amount")


class RequisitionItemAdmin(admin.ModelAdmin):
    list_display = ("requisition", "asset", "quantity", "status")


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(StockItem, StockItemAdmin)
admin.site.register(Requisition, RequisitionAdmin)
admin.site.register(RequisitionItem, RequisitionItemAdmin)
# Register your models here.
