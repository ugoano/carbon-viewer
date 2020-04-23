from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from .models import Meter
from .serializers import MeterSerializer
from ..views import csv_upload


class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer


class MeterUploadView(APIView):
    parser_class = (FileUploadParser,)

    @csrf_exempt
    def post(self, request, format=None):
        if "file" not in request.data:
            raise ParseError("Empty content")
        csv_upload(request.data["file"], Meter)
        return Response({"success": True})
