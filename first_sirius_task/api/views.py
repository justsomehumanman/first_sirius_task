from django.db import models

from rest_framework.views import APIView
from rest_framework.views import Response

from .models import Link

from .serializers import LinkSerializer


class LinkPost(APIView):
    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        a: models.CharField = serializer.get_fields().get('token')
        return Response({"status": "created",
                         "shortenedUrl": "http://localhost:8000/"+serializer.data.get('token')})

    def get(self, request):
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response({"links": serializer.data})


class LinkGet(APIView):
    def get(self, request, get_token):
        link = Link.objects.get(token=get_token)
        link.viewCount += 1
        link.save()
        return Response({"redirectTo": link.redirectTo})


class LinkViewGet(APIView):
    def get(self, request, get_token):
        link = Link.objects.get(token=get_token)
        return Response({"viewCount": link.viewCount})