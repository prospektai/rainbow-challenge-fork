from django.contrib import admin
from django.utils.translation import gettext as _
from fcm_django.models import FCMDevice

# Register your models here.
from import_export.admin import ExportMixin
from firebase_admin.messaging import Message as PushNotification, Notification

from results.models import Medal, Streak
from results.models.prize import Prize, ClaimedPrize
from results.models.region import Region


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.action(description=_('Send push notifications'))
def send_push_notification(modeladmin, request, queryset):
    for prize in queryset:
        message_text = _(
            "New prize added: "
        ) + prize.name
        message_title = "New prize added"
        devices = FCMDevice.objects.all()
        notification = PushNotification(
            data={"category": "new_prize"},
            notification=Notification(title=message_title, body=message_text)
        )
        devices.send_message(notification)

@admin.action(description=_('Push notifications to admins only'))
def send_push_notification_admins(modeladmin, request, queryset):
    for prize in queryset:
        message_text = _(
            "New prize added: "
        ) + prize.name
        message_title = "New prize added"
        devices = FCMDevice.objects.filter(user__is_admin=True)
        notification = PushNotification(
            data={"category": "new_prize"},
            notification=Notification(title=message_title, body=message_text)
        )
        devices.send_message(notification)



class PrizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', )
    actions = [send_push_notification, send_push_notification_admins]

class ClaimedPrizeAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('prize', 'user', 'amount', 'issued')
    list_filter = ('prize', 'user', 'issued')
    readonly_fields = ('date_claimed', )

class MedalAdmin(admin.ModelAdmin):
    list_display = ('user', 'level')

class StreakAdmin(admin.ModelAdmin):
    list_display = ('user', 'week', 'streaks', 'change')
    list_filter = ('week', 'streaks', 'change')


admin.site.register(Region, RegionAdmin)
admin.site.register(Prize, PrizeAdmin)
admin.site.register(ClaimedPrize, ClaimedPrizeAdmin)
admin.site.register(Medal, MedalAdmin)
admin.site.register(Streak, StreakAdmin)
