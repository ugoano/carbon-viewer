from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from .models import Building
from .serializers import BuildingSerializer
from ..views import csv_upload


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingUploadView(APIView):
    parser_class = (FileUploadParser,)

    @csrf_exempt
    def post(self, request, format=None):
        if "file" not in request.data:
            raise ParseError("Empty content")
        csv_upload(request.data["file"], Building)
        return Response({"success": True})
