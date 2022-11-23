from django.contrib import admin

from .models import Contact , Breakfast , Lunch , Dinner

# Registered models
admin.site.register(Contact)
admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Dinner)
