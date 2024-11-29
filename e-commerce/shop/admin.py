from django.contrib import admin

from .views import Product
from .models import *

admin.site.register(Catagory)
admin.site.register(Product)
