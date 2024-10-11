
from django.db import models


class PromptAssociation(models.Model):
    name = models.CharField(max_length=300)
    text = models.TextField()


class Prompt(models.Model):
    crux = models.CharField(max_length=5000)
    association = models.ForeignKey(PromptAssociation, related_name='prompts', on_delete=models.PROTECT, blank=True, null=True)