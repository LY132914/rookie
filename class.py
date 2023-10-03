class Goods:
    __num = 0
    __name = 'none'
    __sum = 0
    __price = 0
    __remain = 0
    def __init__(self,num,name,price,sum,remain):
        self.__num=num
        self.__name=name
        self.__price=price
        self.__sum=sum
        self.__remain=remain
    def display(self):
        print('num=%d'%self.__num)
        print('name=%s'%self.__name)
        print('price=%d'%self.__price)
        print('sum=%d'%self.__sum)
        print('remain=%d'%self.__remain)
    def income(self):
        p =self.__price*(self.__sum-self.__remain)
        return p
    def setdata(self,num,name,price,sum,remain):
        if(num!=0):
            self.__num=num
        if(name!=' '):
            self.__name=name
        if(price!=0):
            self.__price=price
        if(sum!=0):
            self.__sum=sum
        if(remain!=0):
            self.__remain=remain
