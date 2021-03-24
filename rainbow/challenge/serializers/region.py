from rest_framework import serializers

from challenge.models import Region


class RegionSerializer(serializers.ModelSerializer):
    points = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ['name', 'uuid', 'points']
        # fields = '__all__'

    def get_points(self, obj):
        return obj.points