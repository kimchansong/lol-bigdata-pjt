from rest_framework import status
from rest_framework.decorators import api_view
from api.models import itempick

from api.serializers import itempick_serializers
from rest_framework.response import Response

@api_view(['GET','POST'])
def itempick1(request):
    if request.method == 'GET':
        items = itempick.objects.all()
        serializers = itempick_serializers(items, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':

        items = request.data.get('itempick', None)
        # print(items)

        for item in items:
            item_id = item.get('item_id',None)
            item_cnt =item.get('item_cnt',None)
            itempick(item_id=item_id, item_cnt=item_cnt).save()

        return Response(status=status.HTTP_200_OK)