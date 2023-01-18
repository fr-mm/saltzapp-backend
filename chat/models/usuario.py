from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4)
