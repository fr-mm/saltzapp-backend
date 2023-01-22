from django.contrib import admin
from chat import models

admin.site.register(models.Bot)
admin.site.register(models.Cliente)
admin.site.register(models.Mensagem)
admin.site.register(models.Usuario)
admin.site.register(models.UltimaMensagem)
admin.site.register(models.ClienteEmCriacao)
