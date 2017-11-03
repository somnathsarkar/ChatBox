from django.contrib import admin
from .models import User, Message, Friendship, Group, UserGroup
# Register your models here.

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Friendship)
admin.site.register(Group)
admin.site.register(UserGroup)