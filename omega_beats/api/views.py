# from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from omega_beats.api.models import Beat, BeatNotes
from omega_beats.api.serializers import BeatSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':        '/beat-list/',
        'Detail View': '/beat-detail/<str:pk>/',
        'Create':      '/beat-create/',
        'Update':      '/beat-update/<str:pk>',
        'Delete':      '/beat-delete/<str:pk>'
    }

    return Response(api_urls)


@api_view(['GET'])
def beatList(request):
    beats = BeatNotes.objects.all()
    serializer = BeatSerializer(beats, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def beatDetail(request, pk):
    beat = BeatNotes.objects.get(pk=pk)
    serializer = BeatSerializer(beat, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def beatCreate(request):
    serializer = BeatSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def beatUpdate(request, pk):
    beat = BeatNotes.objects.get(pk=pk)
    serializer = BeatSerializer(data=request.data, instance=beat)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def beatDelete(request, pk):
    beat = BeatNotes.objects.get(pk=pk)
    beat.delete()

    return Response("Item successfully deleted!")
