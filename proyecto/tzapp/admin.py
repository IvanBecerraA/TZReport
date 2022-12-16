from django.contrib import admin
from tzapp.models import parametrosRepo001


# Register your models here.

""" class p(admin.ModelAdmin):

    list_editable = ["temperatura_leche_guia"] """

admin.site.register(parametrosRepo001)
    