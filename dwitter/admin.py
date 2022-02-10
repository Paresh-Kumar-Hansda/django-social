from django.contrib import admin

# Register your models here.
from .models import Profile, Dweet
from django.contrib.auth.models import Group, User
#user and profile one place creation
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(Dweet)
