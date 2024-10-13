
from rest_framework import serializers

from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from audio_analyzer_app.models import Prompt, PromptAssociation, Audio


class TokenSerializerNative(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ['key']
        read_only_fields = ['key']

    def create(self, validated_data):
        user = self.context['request'].user
        token_query = Token.objects.filter(user=user)
        if token_query.exists():
            return token_query.first()
        token = Token.objects.create(user=user)
        token.save()
        return token



class UserSerializer(serializers.ModelSerializer):
    prompts = serializers.SlugRelatedField(slug_field="crux", queryset=Prompt.objects.all(), many=True)
    prompt_associations = serializers.SlugRelatedField(slug_field="name", queryset=PromptAssociation.objects.all(), many=True)
    audios = serializers.SlugRelatedField(slug_field="name", queryset=Audio.objects.all(), many=True)

    class Meta:
        model = User
        fields = "__all__"
