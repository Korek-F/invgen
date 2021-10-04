from django.contrib import admin
from .models import Invitation, CustomTemplate
# Register your models here.
admin.site.register(Invitation)
admin.site.register(CustomTemplate)