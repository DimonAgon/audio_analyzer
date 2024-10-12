import re

from pyexpat.errors import messages
from rest_framework import serializers

from .models import Prompt, PromptAssociation, Audio
from .llm_client.client import openai_client
from .llm_client.constants import completion_preserved_arguments

import speech_recognition

import re


speech_recognizer = speech_recognition.Recognizer()


class AudioSerializer(serializers.ModelSerializer):
    prompt_associations = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = Audio
        fields = "__all__"


class PromptSerializer(serializers.ModelSerializer):
    association = serializers.SlugRelatedField(slug_field='name', queryset=PromptAssociation.objects.all())

    class Meta:
        model = Prompt
        fields = "__all__"


class PromptAssociationSerializer(serializers.ModelSerializer):
    prompts = serializers.SlugRelatedField(slug_field='crux', many=True, read_only=True)
    audio = serializers.SlugRelatedField(slug_field='name', queryset=Audio.objects.all())

    class Meta:
        model = PromptAssociation
        fields = "__all__"
        read_only_fields = ["name", "text"]


    def create(self, validated_data):
        audio = validated_data['audio']
        with speech_recognition.AudioFile(audio.audio.path) as audio_source:
            audio_data = speech_recognizer.record(audio_source)
            prompt_association_text = speech_recognizer.recognize_google(audio_data)
        prompt_association_name_response = openai_client.chat.completions.create(
            **completion_preserved_arguments,
            messages=[
                {
                    'role': 'user',
                    'content': f"name the text"
                               f"\n"
                               f"text:{prompt_association_text}"
                }
            ]
        )
        prompt_association_name = prompt_association_name_response.choices[0].message.content
        prompt_association_data = {'name': prompt_association_name, 'text': prompt_association_text, 'audio': audio}
        prompt_association = PromptAssociation.objects.create(**prompt_association_data)
        prompt_association.save()
        prompts_cruxes_text_response = openai_client.chat.completions.create(
            **completion_preserved_arguments,
            messages=[
                {
                    'role': 'user',
                    'content': f"create crux for each of main topics of the text"
                               f"\n"
                               f"text:{prompt_association_text}"
                               f"\n\n"
                               f"PUT CRUXES IN SINGLE QUOTES"
                }
            ]
        )
        prompts_cruxes_text = prompts_cruxes_text_response.choices[0].message.content
        prompts_cruxes = re.findall("'.+'", prompts_cruxes_text)
        for crux in prompts_cruxes:
            prompt_data = {'crux': crux, 'association': prompt_association}
            prompt = Prompt.objects.create(**prompt_data)
            prompt.save()

        return prompt_association
