from django.contrib import admin
from .models import Client, Artist, Work

admin.site.register(Client)
admin.site.register(Artist)
admin.site.register(Work)
