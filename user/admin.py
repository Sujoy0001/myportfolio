from django.contrib import admin
from .models import UserProfile, FAQ


admin.site.register(UserProfile)
admin.site.register(FAQ)