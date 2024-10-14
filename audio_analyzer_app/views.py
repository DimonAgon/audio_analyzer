
from rest_framework import viewsets, permissions
from rest_framework.response import Response


from .models import Prompt, PromptAssociation, Audio
from .serializers import PromptSerializer, PromptAssociationSerializer, AudioSerializer
from .permissions import  general_permission_classes


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = general_permission_classes

    def get_queryset(self):
        user = self.request.user
        queryset = Audio.objects.filter(user=user)
        return queryset

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = general_permission_classes

    def get_queryset(self):
        user = self.request.user
        queryset = Prompt.objects.filter(user=user)
        return queryset


class PromptAssociationViewSet(viewsets.ModelViewSet):
    queryset = PromptAssociation.objects.all()
    serializer_class = PromptAssociationSerializer
    permission_classes = general_permission_classes

    def get_queryset(self):
        user = self.request.user
        queryset = PromptAssociation.objects.filter(user=user)
        return queryset