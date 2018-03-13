from django.contrib import admin

# Register your models here.
from django.contrib import admin

from demo.models import Code, Item

admin.site.register(Code)

admin.site.register(Item)
