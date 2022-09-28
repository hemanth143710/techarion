from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import *
from .serializers import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class ProductsList(APIView):
    """
    List all Products, or create a new User object.
    """
   
  
    def get(self, request, format=None):
        task = Products.objects.all()
        page = request.query_params.get("page")
        limit = request.query_params.get("limit")
        if limit == None:
            limit = 5
        paginator = Paginator(task, limit)
        try:
            task = paginator.page(page)
        except PageNotAnInteger:
            task = paginator.page(1) 
        serializer = ProductsSerializer(task, many=True)
        return Response(serializer.data)
     

class ProductDetail(APIView):
    """
    Retrieve, update or delete a Products instance.
    """
    def get_object(self, id):
        try:
            return Products.objects.get(id=id)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        task = self.get_object(id)
        serializer = ProductsSerializer(task)
        return Response(serializer.data)