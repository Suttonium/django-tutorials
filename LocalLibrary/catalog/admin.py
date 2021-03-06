from django.contrib import admin
from .models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'borrower', 'display_genre')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('title', 'author',)
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
