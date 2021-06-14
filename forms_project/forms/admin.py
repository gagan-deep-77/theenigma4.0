from django.contrib import admin

from .models import User, Room, Questions, Options,Voters


admin.site.register(Questions)
admin.site.register(Options)
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Voters)