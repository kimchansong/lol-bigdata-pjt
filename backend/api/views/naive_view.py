from rest_framework import status
from rest_framework.decorators import api_view
from api.models import duodata,naivedata
from api.serializers import duodata_serializers,naive_data_serializers
from rest_framework.response import Response

from functools import reduce

import pandas as pd
import pprint
import time

class Classifier():
    data = None
    class_attr = None
    priori = {}
    cp = {}
    hypothesis = None



    #self = 간단히 말하면 이 메소드를 부르는 객체가 해당 클래스의 인스턴스인지
    #확인해주는 장치 하지만 self를 이용해서 객체내의 정보를 저장하거나 불러올 수 있음
    def __init__(self,filename=None, class_attr=None ):
        self.data = pd.read_csv(filename, sep=',', header =(0))
        self.class_attr = class_attr

    '''
        probability(class) =    How many  times it appears in cloumn
                             __________________________________________
                                  count of all class attribute
    '''
    #여기서 불러온데이터로 표 만듦
    def calculate_priori(self):
        class_values = list(set(self.data[self.class_attr]))
        class_data =  list(self.data[self.class_attr])
        for i in class_values:
            self.priori[i]  = class_data.count(i)/float(len(class_data))
        print ("Priori Values: ", self.priori)

    '''
        Here we calculate the individual probabilites
        P(outcome|evidence) =   P(Likelihood of Evidence) x Prior prob of outcome
                               ___________________________________________
                                                    P(Evidence)
    '''
    def get_cp(self, attr, attr_type, class_value):
        data_attr = list(self.data[attr])
        class_data = list(self.data[self.class_attr])
        total =1
        for i in range(0, len(data_attr)):
            if class_data[i] == class_value and data_attr[i] == attr_type:
                total+=1
        return total/float(class_data.count(class_value))

    '''
        Here we calculate Likelihood of Evidence and multiple all individual probabilities with priori
        (Outcome|Multiple Evidence) = P(Evidence1|Outcome) x P(Evidence2|outcome) x ... x P(EvidenceN|outcome) x P(Outcome)
        scaled by P(Multiple Evidence)
    '''
    def calculate_conditional_probabilities(self, hypothesis):
        for i in self.priori:
            self.cp[i] = {}
            for j in hypothesis:
                self.cp[i].update({ hypothesis[j]: self.get_cp(j, hypothesis[j], i)})
        print ("\nCalculated Conditional Probabilities: \n")
        pprint.pprint(self.cp)

    def classify(self):
        print ("Result: ")
        print(self.cp['yes'])
        # for i in self.cp:
        print ('good', " ==> ", reduce(lambda x, y: x*y, self.cp['yes'].values())*self.priori['yes'])
        print ('bad', " ==> ", reduce(lambda x, y: x*y, self.cp['no'].values())*self.priori['no'])
        yes = reduce(lambda x, y: x*y, self.cp['yes'].values())*self.priori['yes']
        no = reduce(lambda x, y: x*y, self.cp['no'].values())*self.priori['no']
        # i = reduce(lambda x, y: x*y, self.cp[i].values())*self.priori[i]
        result = ""
        if yes>no:
            print('good')
            result = 'good'
        else:
            print('bad')
            result = 'bad'
        return result

@api_view(['GET','POST'])
def champion_data(request):
    if request.method == 'GET':
        result = ""
        avg = 0
        avgfBlood = 0
        avgfT = 0
        avgfD = 0
        avgfB = 0
        avgTK = 0
        avgDK = 0
        avgBK = 0
        avgwin = 0
        bot1 = request.GET.get('bot1', None)
        bot2 = request.GET.get('bot2', None)
        print(bot1,bot2)

        file = open("./new_dataset.csv",'w',encoding='UTF8')
        #DB에서 인덱스 꺼내와서 파일로 만든후 나이브 ㄱㄱ
        bigdata = naivedata.objects.all();
        file.writelines("Bot1,Bot2,Win")
        file.write('\n')
        # i =0
        for gamedata in bigdata:
            avg = avg+1
            num1 = gamedata.Bot1
            num2 = gamedata.Bot2
            num3 = gamedata.Bot3
            num4 = gamedata.Bot4
            num5 = gamedata.Bot5
            fBlood = gamedata.fBlood
            fT = gamedata.fT
            fD = gamedata.fD
            fB = gamedata.fB
            TK = gamedata.TK
            DK = gamedata.DK
            BK = gamedata.BK
            win = gamedata.Win




            members = [num1,num2,num3,num4,num5]
            check1 = 0
            check2 = 0

            for member in members:
                if bot1==member:
                    check1 = 1
                elif bot2 == member:
                    check2 = 1
            if check1==1 & check2==1:
                # file.writelines(','.join([str(bot1),str(bot2),str(fBlood),str(fT),str(fD),str(fB),str(TK),str(DK),str(BK),str(win)]))
                avgfBlood = avgfBlood + int(fBlood)
                avgfT = avgfT + int(fT)
                avgfD = avgfD + int(fD)
                avgfB = avgfB + int(fB)
                avgTK = avgTK + int(TK)
                avgDK = avgDK + int(DK)
                avgBK = avgBK + int(BK)
                if win =="yes":
                    avgwin = avgwin+1

                file.writelines(','.join([str(bot1),str(bot2),str(win)]))
                file.write('\n')


        file.close()
        avgfBlood = avgfBlood/avg *100
        avgfT = avgfT/avg *100
        avgfD = avgfD/avg *100
        avgfB = avgfB/avg *100
        avgTK = avgTK/avg *100
        avgDK = avgDK/avg *100
        avgBK = avgBK/avg *100
        avgwin = avgwin/avg *100
        # serializers = naive_data_serializers(naivedatas, many=True)
        # return Response(data=serializers.data, status=status.HTTP_200_OK)
        c = Classifier(filename="new_dataset.csv", class_attr="Win" )
        c.calculate_priori()
        #봇1 , 봇2 입력받고 출력
        c.hypothesis = {"Bot1":int(bot1), "Bot2":int(bot2)}
        c.calculate_conditional_probabilities(c.hypothesis)
        result = c.classify();
        print(result)
        print(avgfBlood,avgfT,avgfD,avgfB,avgTK,avgDK,avgBK,avgwin)
        resultdata = [result,avgfBlood,avgfT,avgfD,avgfB,avgTK,avgDK,avgBK,avgwin]
        avg = 0
        avgfBlood = 0
        avgfT = 0
        avgfD = 0
        avgfB = 0
        avgTK = 0
        avgDK = 0
        avgBK = 0
        avgwin = 0
        return Response(data=resultdata, status=status.HTTP_200_OK)
