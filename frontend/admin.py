from django.contrib import admin
from django.contrib import admin
from .models import *

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'Yozuvchi', 'kategoriya')
    search_fields = ('nomi', 'Yozuvchi')
    list_filter = ('kategoriya',)

