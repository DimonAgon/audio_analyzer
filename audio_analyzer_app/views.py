
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from assets.viewsets import PrivateModelViewSetQuerySetGetter
from .models import Prompt, PromptAssociation, Audio
from .serializers import PromptSerializer, PromptAssociationSerializer, AudioSerializer
from .permissions import  general_permission_classes


class AudioViewSet(PrivateModelViewSetQuerySetGetter, viewsets.ModelViewSet):
    model = Audio
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = general_permission_classes


class PromptViewSet(PrivateModelViewSetQuerySetGetter, viewsets.ModelViewSet):
    model = Prompt
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = general_permission_classes


class PromptAssociationViewSet(PrivateModelViewSetQuerySetGetter, viewsets.ModelViewSet):
    model = PromptAssociation
    queryset = PromptAssociation.objects.all()
    serializer_class = PromptAssociationSerializer
    permission_classes = general_permission_classes