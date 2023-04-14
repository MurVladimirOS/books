from django.contrib import admin
from .models import AllBooks


@admin.register(AllBooks)
class BookAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'descriptions', 'author']

# admin.site.register(AllBooks, BookAdmin)
