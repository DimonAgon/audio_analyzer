
from rest_framework import serializers

from rest_framework.authtoken.models import Token


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

    def retrieve(self, *args, **kwargs):
        user = self.context['request'].user
        token = Token.objects.get_or_404(user=user)
        return token