from rest_framework import status
from rest_framework.decorators import api_view
from api.models import item_data3

from api.serializers import item_serializers
from rest_framework.response import Response

@api_view(['GET','POST'])
def items_data3(request):
    if request.method == 'GET':
        char_id = request.GET.get('char_id',None)
        items = item_data3.objects.all()
    
        if char_id:
            items = items.filter(char_id__iexact=char_id)
            items = sorted(items, key = lambda item : item.item_cnt, reverse=True)

        serializers = item_serializers(items, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':

        items = request.data.get('champ_items', None)


        for item in items:
            char_id = item.get('char_id',None)
            item_id = item.get('item_id',None)
            item_cnt =item.get('item_cnt',None)
            item_data3(char_id=char_id, item_id=item_id, item_cnt=item_cnt).save()

        return Response(status=status.HTTP_200_OK)