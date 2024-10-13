
from django.db import models

from django.contrib.auth.models import User


class Audio(models.Model):
    name = models.CharField(max_length=300)
    audio = models.FileField(upload_to='audios/')
    user = models.ForeignKey(User, related_name='audios', on_delete=models.PROTECT, blank=True, null=True)


class PromptAssociation(models.Model):
    name = models.CharField(max_length=300)
    text = models.TextField()
    related_name = 'prompt_associations'
    audio = models.ForeignKey(Audio, related_name=related_name, on_delete=models.PROTECT, blank=True, null=True)
    user = models.ForeignKey(User, related_name=related_name, on_delete=models.PROTECT, blank=True, null=True)


class Prompt(models.Model):
    crux = models.CharField(max_length=5000)
    related_name = 'prompts'
    association = models.ForeignKey(PromptAssociation, related_name=related_name, on_delete=models.PROTECT, blank=True, null=True)
    user = models.ForeignKey(User, related_name=related_name, on_delete=models.PROTECT, blank=True, null=True)