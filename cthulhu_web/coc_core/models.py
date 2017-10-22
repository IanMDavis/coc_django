from django.db import models

from django.db import models

class Character(models.Model):
    player_name = models.CharField(max_length=128)
    character_name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'
