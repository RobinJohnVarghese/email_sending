from django.contrib import admin
from .models import Email
# Register your models here.



class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient', 'subject', 'message','send_at')
    list_display_links = ('id', 'recipient')

admin.site.register(Email, EmailAdmin)