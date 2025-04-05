from django.contrib import admin
from .models import FibreSheetJali
from django.contrib.auth.models import Group, User

class ItemAdmin(admin.ModelAdmin):
    list_display = ('color', 'size', 'length', 'weight', 'category','type' , 'availability', 'date_added', 'date_updated')  # ✅ Display all fields in the admin panel
    search_fields = ('color', 'size', 'length', 'weight', 'category')  # ✅ Add search functionality for easy access
    list_editable = ('category', 'availability', 'type')  # ✅ Make category editable directly in admin panel
    list_filter = ('color', 'availability', 'category', 'type')  # ✅ Add filters for easy selection
    ordering = ('size','availability')  # ✅ Sort by size and availability
    @admin.display(description="Total Weight (kg)")
    def total_weight_display(self, obj):
        return obj.total_weight()

    def total_weight_per_category(self):
        category_totals = FibreSheetJali.objects.values("category").annotate(total_weight=Sum("weight"))
        result = {entry["category"]: entry["total_weight"] for entry in category_totals}
        return result

    admin.site.site_header = "Inventory Management"
    admin.site.site_title = "Inventory Admin"
    admin.site.index_title = "Manage Inventory"
    admin.site.site_url = None  # Remove the default Django admin URL
    verbose_name = "Inventory"


admin.site.register(FibreSheetJali, ItemAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)