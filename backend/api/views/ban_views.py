from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Pickban
from api.serializers import Pickban_serializers
from rest_framework.response import Response

@api_view(['GET','POST'])
def pickbans(request):
    if request.method == 'GET':
        re = Pickban.objects.all()
        serializer = Pickban_serializers(re, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        pickban = request.data.get('pickban', None)
        for i in range(len(pickban)):
            print(pickban[i]['id'])
            id = pickban[i]['id']
            name = pickban[i]['name']
            pickcount = pickban[i]['pickcount']
            bancount = pickban[i]['bancount']
            Pickban(id=id, name = name , pickcount=pickcount, bancount=bancount).save()
        return Response(status=status.HTTP_200_OK)