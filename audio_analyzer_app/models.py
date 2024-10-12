
from django.db import models


class Audio(models.Model):
    name = models.CharField(max_length=300)
    audio = models.FileField(upload_to='audios/')


class PromptAssociation(models.Model):
    name = models.CharField(max_length=300)
    text = models.TextField()
    audio = models.ForeignKey(Audio, related_name='prompt_associations', on_delete=models.PROTECT, blank=True, null=True)


class Prompt(models.Model):
    crux = models.CharField(max_length=5000)
    association = models.ForeignKey(PromptAssociation, related_name='prompts', on_delete=models.PROTECT, blank=True, null=True)