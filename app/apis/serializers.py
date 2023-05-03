from rest_framework import serializers
from .models import Client, Artist, Work
from django.contrib.auth.models import User


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filter by work type
        request = getattr(self.context, 'request', None)
        if request:
            work_type = request.query_params.get('work_type')
            if work_type:
                self.queryset = Work.objects.filter(work_type=work_type)

            # Search by artist name
            artist = request.query_params.get('artist')
            if artist:
                self.queryset = Work.objects.filter(artist__icontains=artist)


class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'works']




class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ('username', 'password')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name',)
