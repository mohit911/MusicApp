from music_app.models import Music, Genere
from rest_framework import serializers


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'genere', 'rating')


class GenereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genere
        fields = ('genere',)
