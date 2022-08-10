from django.contrib import admin
from .models import Order

# Register your models here.

# admin.site.register(Order)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # create fields for displaying at the admin
    list_display = ['size', 'order_status', 'quantity', 'created_at']

    # create fields for filtering
    list_filter = ['size', 'order_status', 'quantity', 'created_at', ]
