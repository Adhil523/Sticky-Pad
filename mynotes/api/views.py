from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    return JsonResponse("Our API",safe=False) #safe used to ensure more than python dictioanry can be provided as data

@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all().order_by('-updated') #without minus sign, it will ordered in the opposite order
    serializer=NoteSerializer(notes, many=True) #many used to tell if we want to serialize single or all datas. Her it returns a queryset of all data
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request,pk):
    notes=Note.objects.get(id=pk)
    serializer=NoteSerializer(notes, many=False) 
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,pk):
    data=request.data  #JSON file
    note= Note.objects.get(id=pk)
    serializer=NoteSerializer(instance=note,data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted")

@api_view(['POST'])
def createNote(request):
    data=request.data
    print(data)
    note=Note.objects.create(
        body=data['body']
    )
    serializer=NoteSerializer(note,many=False)
    print(serializer.data)
    return Response(serializer.data)