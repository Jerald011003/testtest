from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import *

User = get_user_model()
admin.site.register(Customer)
admin.site.register(ProductForCustomer)
admin.site.register(Order)
admin.site.register(Tag)

