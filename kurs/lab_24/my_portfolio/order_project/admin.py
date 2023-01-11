from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):

    list_display = ("name_customer", "phone_customer", "email_customer", "type_website", "created_on")
    list_filter = ("type_website", "email_customer")
    fieldsets = (
        ("Customer info", {
            "fields": (("name_customer",), ("phone_customer", "email_customer"))
        }),
        ("Website Info", {
            "fields": (("title", "type_website"), ("body",))
        }),
    )


admin.site.register(Order, OrderAdmin)

