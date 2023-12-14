from django.contrib import admin

from pyskill.models import Dispatch


# Register your models here.


@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    list_display = ("mail_to_send",)
