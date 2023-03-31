from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import status

from webapi.models import Observacion
from webapi.serializers import ObservacionSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def observacion_list(request):
    if request.method == 'GET':
        observacion = Observacion.objects.all()
        observacion_serializer = ObservacionSerializer(observacion, many=True)
        return JsonResponse(observacion_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        observacion_data = JSONParser().parse(request)
        observacion_serializer = ObservacionSerializer(data=observacion_data)
        if Observacion_serializer.is_valid():
            Observacion_serializer.save()
            return JsonResponse(Observacion_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Observacion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)