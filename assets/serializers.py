
from django.db.models import Model


class PrivateSerializerFieldQuerySetGetter:
    model: Model

    def get_queryset(self):
        user = self.context['request'].user
        return self.model.objects.filter(user=user)