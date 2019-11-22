from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Bancount3
from api.serializers import bancount_serializers
from rest_framework.response import Response
@api_view(['GET','POST'])
def bancounting1(request):
    if request.method == 'GET':
        char_id = request.GET.get("char_id",None)
        name = request.GET.get("name",None)
        bancounts = Bancount3.objects.all()
       
        if char_id:
            bancounts = bancounts.filter(char_id__iexact=char_id)
            bancounts = sorted(bancounts, key = lambda cnt : cnt.cnt, reverse=True)

        if name:
            bancounts = bancounts.filter(name__iexact=name)
            bancounts = sorted(bancounts, key = lambda cnt : cnt.cnt, reverse=True)

        serializers = bancount_serializers(bancounts, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        bancounts = request.data.get('bancount', None)
        for bancount in bancounts:
            id = bancount.get('id',None)
            name = bancount.get('name',None)
            char_id =bancount.get('char_id',None)
            ban_char_id =bancount.get('ban_char_id',None)
            cnt =bancount.get('cnt',None)
            Bancount3(id=id, name=name, char_id=char_id, ban_char_id=ban_char_id, cnt=cnt).save()
        return Response(status=status.HTTP_200_OK)