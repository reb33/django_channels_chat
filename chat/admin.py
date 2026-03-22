from django.contrib import admin

from chat.models import Message, Event, Group

admin.site.register(Message)
admin.site.register(Event)
admin.site.register(Group)
