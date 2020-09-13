from django.contrib import admin
from .models import userProfile,cart,wishlist,orderDetails,reviewDetails
# Register your models here.
#admin.site.register(userProfile)


admin.site.site_header="Farmers E Market"

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group


class ProfileInline(admin.StackedInline):
    model = userProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(cart)
admin.site.register(wishlist)
admin.site.register(orderDetails)
admin.site.register(reviewDetails)