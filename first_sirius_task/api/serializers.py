from rest_framework import serializers

from .models import Link

import secrets


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('redirectTo', 'urlToShorten', 'token')

    def create(self, validated_data):
        link = Link()
        link.redirectTo = validated_data['urlToShorten']
        link.token = self.generate_token(set([x.token for x in Link.objects.all()]))
        link.save()
        return link

    @staticmethod
    def generate_token(self, tokens=set()):
        while True:
            token = secrets.token_urlsafe(6)
            if token not in tokens:
                return str(token)
