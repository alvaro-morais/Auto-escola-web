from django.contrib import admin
from django.contrib.auth.models import Group
from django.http import request
from .models import Agenda, Pessoa

class agendaAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'hour')
    list_filter = ('name',)
    list_per_page = 5

admin.site.index_title = "Auto Escola Líder"
#admin.site.index_template = "admin.html" 
admin.site.unregister(Group)
admin.site.register(Agenda, agendaAdmin)
admin.site.register(Pessoa)
