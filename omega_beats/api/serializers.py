from rest_framework import serializers
from omega_beats.api.models import Beat


class BeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beat
        fields = '__all__'
