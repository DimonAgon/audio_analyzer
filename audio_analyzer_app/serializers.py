
from rest_framework import serializers

from .models import Prompt, PromptAssociation


class PromptSerializer(serializers.ModelSerializer):
    association = serializers.SlugRelatedField(slug_field='name', queryset=PromptAssociation.objects.all())

    class Meta:
        model = Prompt
        fields = "__all__"


class PromptAssociationSerializer(serializers.ModelSerializer):
    prompts = serializers.SlugRelatedField(slug_field='crux', many=True, read_only=True)

    class Meta:
        model = PromptAssociation
        fields = "__all__"