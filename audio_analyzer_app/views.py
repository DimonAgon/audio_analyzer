
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import Prompt, PromptAssociation, Audio
from .serializers import PromptSerializer, PromptAssociationSerializer, AudioSerializer
from .permissions import  general_permission_classes


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = general_permission_classes


class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = general_permission_classes


class PromptAssociationViewSet(viewsets.ModelViewSet):
    queryset = PromptAssociation.objects.all()
    serializer_class = PromptAssociationSerializer
    permission_classes = general_permission_classes