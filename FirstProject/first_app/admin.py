from django.contrib import admin
from .models import AccessRecord, Topic, Webpage, User

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User, YourModelAdmin)