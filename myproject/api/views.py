from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
  items = Item.objects.all()
  serializer = ItemSerializer(items, many=True)
  return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
  serializer = ItemSerializer(data=request.data) # request.data is the data which was submitted on the fronted
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)