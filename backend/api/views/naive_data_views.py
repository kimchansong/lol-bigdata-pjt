from rest_framework import status
from rest_framework.decorators import api_view
from api.models import naivedata

from api.serializers import naive_data_serializers
from rest_framework.response import Response

@api_view(['GET','POST'])
def naive_data(request):
    if request.method == 'GET':
        naivedatas = naivedata.objects.all()
        serializers = naive_data_serializers(naivedatas, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        items = request.data.get("naviedata", None)
        for item in items:
            # Bot1,Bot2,Bot3,Bot4,Bot5,fBlood,fT,fD,fB,TK,DK,BK,Win,all
            Bot1 = item.split(',')[0]
            Bot2 = item.split(',')[1]
            Bot3 = item.split(',')[2]
            Bot4 = item.split(',')[3]
            Bot5 = item.split(',')[4]
            fBlood = item.split(',')[5]
            fT= item.split(',')[6]
            fD= item.split(',')[7]
            fB= item.split(',')[8]
            TK= item.split(',')[9]
            DK= item.split(',')[10]
            BK= item.split(',')[11]
            Win= item.split(',')[12]    
            all= item

            naivedata(Bot1=Bot1,Bot2=Bot2,Bot3=Bot3,Bot4=Bot4,Bot5=Bot5,fBlood=fBlood,fT=fT,fD=fD,fB=fB,TK=TK,DK=DK,BK=BK,Win=Win,all=all).save()

        return Response(status=status.HTTP_200_OK)
