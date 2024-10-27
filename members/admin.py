from django.contrib import admin

# Register your models here.
from .models import *

class MemberAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", 'salary', "updated",)

admin.site.register(Member, MemberAdmin)