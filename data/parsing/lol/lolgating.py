from functools import reduce

import pandas as pd
import pprint

# import request

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
        if yes>no:
            print('good')
        else:
            print('bad')

if __name__ == "__main__":
    c = Classifier(filename="new_dataset.csv", class_attr="Play" )
    c.calculate_priori
    #봇1 , 봇2 입력받고 출력
    c.hypothesis = {"Bot1":'84', "Bot2":"236"}

    c.calculate_conditional_probabilities(c.hypothesis)
    c.classify()
