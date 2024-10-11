
from rest_framework import viewsets, permissions

from .models import Prompt, PromptAssociation
from .serializers import PromptSerializer, PromptAssociationSerializer
from .permissions import  general_permission_classes

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = general_permission_classes


class PromptAssociationViewSet(viewsets.ModelViewSet):
    queryset = PromptAssociation.objects.all()
    serializer_class = PromptAssociationSerializer
    permission_classes = general_permission_classes