from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *

User = get_user_model()
admin.site.register(Customer)
admin.site.register(ProductForCustomer)
admin.site.register(Order)
admin.site.register(Tag)

class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Departmet', {'fields': ('department',)}),
    )
