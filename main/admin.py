from django.contrib import admin
from main.db_models.app_users import AppUser
from main.db_models.busineses import Supplier, Customer, SupplierTranslation, CustomerTranslation

from datetime import datetime, timezone

@admin.register(AppUser)
class AppUsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'tg_id', 'tg_username', 'username', 'reg_date_formatted', 'business_id', 'business_role']
    def reg_date_formatted(self, obj):
        if obj.reg_date:            
            dt = datetime.fromtimestamp(obj.reg_date, tz=timezone.utc)
            return dt.strftime("%Y-%m-%d - %H:%M:%S (UTC)")
        return ""
    reg_date_formatted.short_description = "Reg Date (formatted)"


@admin.register(Supplier)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner_tg_id', 'name', 'reg_date_formatted', 'staff', 'tariff', 'end_tariff_date_formatted']
    def reg_date_formatted(self, obj):
        if obj.reg_date:            
            dt = datetime.fromtimestamp(obj.reg_date, tz=timezone.utc)
            return dt.strftime("%Y-%m-%d - %H:%M:%S (UTC)")
        return ""
    def end_tariff_date_formatted(self, obj):
        if obj.end_tariff_date:
            dt = datetime.fromtimestamp(obj.end_tariff_date, tz=timezone.utc)
            return dt.strftime("%Y-%m-%d - %H:%M:%S (UTC)")
        return ""
    reg_date_formatted.short_description = "Reg Date:"
    end_tariff_date_formatted.short_description = "Tariff End:"


@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner_tg_id', 'name', 'reg_date_formatted', 'staff', 'tariff', 'end_tariff_date_formatted']
    def reg_date_formatted(self, obj):
        if obj.reg_date:            
            dt = datetime.fromtimestamp(obj.reg_date, tz=timezone.utc)
            return dt.strftime("%Y-%m-%d - %H:%M:%S (UTC)")
        return ""
    def end_tariff_date_formatted(self, obj):
        if obj.end_tariff_date:
            dt = datetime.fromtimestamp(obj.end_tariff_date, tz=timezone.utc)
            return dt.strftime("%Y-%m-%d - %H:%M:%S (UTC)")
        return ""
    reg_date_formatted.short_description = "Reg Date:"
    end_tariff_date_formatted.short_description = "Tariff End:"


@admin.register(SupplierTranslation)
class SupplierTranslationAdmin(admin.ModelAdmin):
    list_display = ['id', 'language', 'supplier_id', 'name']

@admin.register(CustomerTranslation)
class CustomerTranslationAdmin(admin.ModelAdmin):
    list_display = ['id', 'language', 'customer_id', 'name']