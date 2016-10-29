"""Django Admin View configuration."""
from django.contrib import admin
# from .models import UserProfile, UserProfileInfo
from .models import UserProfileInfo


class UserProfileInfoAdmin(admin.ModelAdmin):
    """Customising admin view of UserProfileInfo class."""

    '''Displaying all the fields in admin in order.'''
    # fields = ['user', 'gender', 'full_name']

    '''Displaying all the fields in admin in different sections.'''
    # readonly_fields = ['joining_date']
    fieldsets = [
        ('User Information header', {'fields': ['user', 'first_name', 'last_name', 'gender', 'profile_picture']}),
        ('Date information', {'fields': ['joining_date'], 'classes': ['collapse']}),
    ]

    list_display = ['first_name', 'gender', 'profile_picture']
    list_filter = ['joining_date']
    search_fields = ['first_name', 'last_name', 'gender']
    readonly_fields = ['user', 'joining_date']

    class Meta:
        """Information of this class."""

        model = UserProfileInfo

# admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserProfileInfo, UserProfileInfoAdmin)
