from django.contrib import admin
from .models import Receipe


class ReceipeHistoryAdmin(admin.ModelAdmin):
    list_display = ('receipe_name', 'user', 'created_at')
    history_list_display = ['receipe_description']
    search_fields = ('receipe_name', 'user__username')
    history_list_per_page = 100
admin.site.register(Receipe,ReceipeHistoryAdmin)