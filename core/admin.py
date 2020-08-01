from django.contrib import admin
from .models import Comments
# Register your models here.

class CommentsAdmin(admin.ModelAdmin):
    read_only_fields = ('created', 'updated')
    list_display = ('email', 'value', 'feedback')

admin.site.register(Comments, CommentsAdmin)
