
from django.db.models import Model

class PrivateModelViewSetQuerySetGetter:
    model: Model

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)