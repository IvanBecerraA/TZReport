from django.contrib import admin
from tzapp.models import parametrosRepo001
from django.contrib.auth.models import Permission

# Register your models here.

""" class p(admin.ModelAdmin):

    list_editable = ["temperatura_leche_guia"] """

admin.site.register(parametrosRepo001)
admin.site.register(Permission)