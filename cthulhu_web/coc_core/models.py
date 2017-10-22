from django.db import models

from django.db import models

class Character(models.Model):
    player_name = models.CharField(null=True, max_length=128)
    character_name = models.CharField(null=True, max_length=128)
    occupation = models.CharField(null=True, max_length=128)
    age = models.IntegerField(null=True)
    sex = models.CharField(null=True, max_length=128)
    residence = models.CharField(null=True, max_length=128)
    birthplace = models.CharField(null=True, max_length=128)

    strength = models.IntegerField(null=True)
    dexterity = models.IntegerField(null=True)
    intelligence = models.IntegerField(null=True)
    constitution = models.IntegerField(null=True)
    appearance = models.IntegerField(null=True)
    power = models.IntegerField(null=True)
    size = models.IntegerField(null=True)
    education = models.IntegerField(null=True)
    current_hp = models.IntegerField(null=True)
    max_hp = models.IntegerField(null=True)
    current_mp = models.IntegerField(null=True)
    max_mp = models.IntegerField(null=True)
    current_sanity = models.IntegerField(null=True)
    max_sanity = models.IntegerField(null=True)
        

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'
