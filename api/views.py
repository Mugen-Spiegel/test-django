import json

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SnippetSerializer
from django.core import serializers
from .models import Snippet 

@api_view(['GET'])
def snippet_list(request):
    """
    List all code snippets
    """
    snippet_object= Snippet.objects.all().values('title','description', 'language', 'active', 'code_block')
    print(snippet_object)
    return Response(snippet_object)

@api_view(['POST'])
def create_snippet(request):
    """
    create a new snippet.
    """
    data = json.loads(request.body.decode('utf-8'))
    snippet = Snippet(
        title=data["title"], 
        description=data["description"], 
        language=data["language"], 
        active=data["active"], 
        code_block=data["code_block"], 
    )
    snippet.save()
    return Response({"message": "Success!!"})