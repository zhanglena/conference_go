from django.contrib import admin

from .models import Attendee, Badge, AccountVO


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    pass

@admin.register(AccountVO)
class AccountVOadmin(admin.ModelAdmin):
    pass
