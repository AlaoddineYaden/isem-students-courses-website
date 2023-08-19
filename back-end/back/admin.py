from django.contrib import admin
from .models import Year, Sector, Subject, Course, Exam

from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

class CustomUserAdmin(UserAdmin):
    def has_change_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)
    def has_add_permission(self, request):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

    def has_view_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_view_permission(request, obj)

class CustomGroupAdmin(GroupAdmin):
    def has_change_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)
    def has_add_permission(self, request):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

    def has_view_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_view_permission(request, obj)
    
class YearSectorAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)
    def has_add_permission(self, request):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

    def has_view_permission(self, request, obj=None):
        if not request.user.groups.filter(name='me').exists() and request.user.is_superuser:
            return False
        return super().has_view_permission(request, obj)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)

admin.site.register(Year, YearSectorAdmin)
admin.site.register(Sector, YearSectorAdmin)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Exam)
