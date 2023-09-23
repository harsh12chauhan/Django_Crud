from django.contrib import admin
from .models import details
# Register your models here.

# admin.site.register(details)

@admin.register(details)
class details_user(admin.ModelAdmin):
    list_display = ('id','surname','contact','salary','address','date_Time')
