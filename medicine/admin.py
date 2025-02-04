from django.contrib import admin
from .models import Category, Subcategory, Medicine, CartItem, Address, Checkout, DietCategory, DietPlan

# Register Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

# Register Subcategory model
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

admin.site.register(Subcategory, SubcategoryAdmin)

# Register Medicine model
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_category', 'price', 'stock', 'description')
    search_fields = ('name', 'sub_category__name')
    list_filter = ('sub_category',)
    list_editable = ('price', 'stock')

admin.site.register(Medicine, MedicineAdmin)

# Register CartItem model
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'quantity', 'added_at')
    search_fields = ('medicine__name',)
    list_filter = ('added_at',)

admin.site.register(CartItem, CartItemAdmin)

# Register Address model
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_type', 'city', 'state', 'zipcode')
    search_fields = ('user__username', 'city', 'state')
    list_filter = ('address_type',)

admin.site.register(Address, AddressAdmin)

# Register Checkout model
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'delivery_address', 'billing_address', 'payment_method', 'total', 'order_summary')
    search_fields = ('user__username',)
    list_filter = ('payment_method',)

admin.site.register(Checkout, CheckoutAdmin)

# Register DietCategory model
class DietCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name',)

admin.site.register(DietCategory, DietCategoryAdmin)

# Register DietPlan model
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ('diet_category', 'file_or_image')
    search_fields = ('diet_category__name',)
    list_filter = ('diet_category',)

admin.site.register(DietPlan, DietPlanAdmin)
