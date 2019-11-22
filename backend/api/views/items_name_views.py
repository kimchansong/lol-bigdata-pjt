from rest_framework import status
from rest_framework.decorators import api_view
from api.models import name_data
from api.serializers import item_name_serializers
from rest_framework.response import Response

@api_view(['GET','POST'])
def Name_data1(request):
    if request.method == 'GET':
        key = request.GET.get('key',None)
        items = name_data.objects.all()
    
        if key:
            items = items.filter(key__iexact=key)

        serializers = item_name_serializers(items, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':

        items = request.data.get('champ_items_name', None)
        print(items)
        for item in items:
        
            name =item.get('name',None)
            key = item.get('key',None)
            print(name)
            # model은 3개 파라메터를 받아야하는데 여기는 두개만 받아서 오류남 ㅜㅜ
            
            name_data(name=name, key=key, ).save()
            print(name_data)
            

        return Response(status=status.HTTP_200_OK)