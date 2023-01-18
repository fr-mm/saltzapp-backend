from django.contrib import admin
from chat import models


admin.site.register(models.Bot)
admin.site.register(models.Cliente)
admin.site.register(models.Funcionario)
admin.site.register(models.Mensagem)
