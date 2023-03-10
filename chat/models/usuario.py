from __future__ import annotations

from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from djongo import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Usuario(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4)

    @classmethod
    def criar(cls, nome: str, senha: str) -> Usuario:
        return Usuario.objects.create_user(
            username=nome,
            password=senha
        )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
