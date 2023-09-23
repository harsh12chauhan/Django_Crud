from django.contrib import admin
from .models import userDetails
# Register your models here.

# admin.site.register(userDetails)


@admin.register(userDetails)
class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','password','date_Time')