
from rest_framework import viewsets, permissions
from rest_framework.response import Response


from .models import Prompt, PromptAssociation, Audio
from .serializers import PromptSerializer, PromptAssociationSerializer, AudioSerializer
from .permissions import  general_permission_classes


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = general_permission_classes

    def list(self, request):
        user = request.user
        queryset = Audio.objects.filter(user=user)
        serializer = AudioSerializer(queryset, many=True)
        return Response(serializer.data)

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = general_permission_classes

    def list(self, request):
        user = request.user
        queryset = Prompt.objects.filter(user=user)
        serializer = PromptSerializer(queryset, many=True)
        return Response(serializer.data)


class PromptAssociationViewSet(viewsets.ModelViewSet):
    queryset = PromptAssociation.objects.all()
    serializer_class = PromptAssociationSerializer
    permission_classes = general_permission_classes

    def list(self, request):
        user = request.user
        queryset = PromptAssociation.objects.filter(user=user)
        serializer = PromptAssociationSerializer(queryset, many=True)
        return Response(serializer.data)