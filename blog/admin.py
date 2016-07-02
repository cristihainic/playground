from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_added', 'last_updated')

admin.site.register(Page, PageAdmin)