from django.shortcuts import render
from.seriallizer import *
from.models import *
from rest_framework.decorators import api_view
from rest_framework.response import response
# reate your views here.
#read
@api_view(['GET'])
def booklist(request):
  booksobj=booksmodel.objects.all()#queryset
  serializer=bookserializer(booksobj,many=True)
  return Response(serializer.data)
#create
@api_view(['Post'])
def post_bookt(request):
  booksobj=booksmodel.objects.all()#queryset
  serializer=bookserializer(data=request.data)
  if serializer.is_valid():
  serializer.save()
  return Response(serializer.data)
#update
  @api_view(['Post'])
def update_bookt(request,id):
  booksobj=booksModel.objects.get(id=id)#queryset
  serializer=bookserializer(instance=booksobj,data=request.data)
  if serializer.is_valid():
  serializer.save()
  return Response(serializer.data)
  #delete
  @api_view(['DELETE'])
def delete_bookt(request,id):
  booksobj=booksModel.objects.get(id=id)#queryset
  booksobj.delete
  return Response("book is deleted")
