from rest_framework import status
from rest_framework.decorators import api_view
from api.models import champion
from api.serializers import champion_serializers
from rest_framework.response import Response


@api_view(['GET'])
def champions(request):

    if request.method == 'GET':

        name = request.GET.get('name', None)
        key = request.GET.get('key', None)
        champions = champion.objects.all()
        
        if name:
            champions = champions.filter(name__iexact=name)
        if key:
            champions = champions.filter(key__iexact=key) 

        serializer = champion_serializers(champions, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
