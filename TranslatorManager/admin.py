from django.contrib import admin
from TranslatorManager.models import Client,JobType,ClientJob
# Register your models here.


admin.site.register(Client)
admin.site.register(JobType)
admin.site.register(ClientJob)