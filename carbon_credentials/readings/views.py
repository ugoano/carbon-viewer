from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from .models import Reading
from .serializers import ReadingSerializer
from ..views import csv_upload


class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

    def get_queryset(self):
        if 'meter_id' in self.request.query_params:
            return self.queryset.filter(meter_id=self.request.query_params['meter_id'])
        return self.queryset


class ReadingUploadView(APIView):
    parser_class = (FileUploadParser,)

    @csrf_exempt
    def post(self, request, format=None):
        if "file" not in request.data:
            raise ParseError("Empty content")
        csv_upload(request.data["file"], Reading)
        return Response({"success": True})
