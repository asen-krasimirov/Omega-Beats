from rest_framework import serializers
from omega_beats.api.models import Beat, BeatNotes


class BeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeatNotes
        fields = '__all__'
