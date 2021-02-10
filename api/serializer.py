from rest_framework import serializers 
  
# import model from models.py 
from .models import Snippet 
  
# Create a model serializer  
class SnippetSerializer(serializers.ModelSerializer): 
    # specify model and fields 
    class Meta: 
        model = Snippet 
        fields = ('title', 'description', 'language', 'code_block', 'active') 