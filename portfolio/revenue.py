import matplotlib.pyplot as plt
import numpy as np
import math

class  Revenue():

    #def __init__(self):
     #   pass


    #后续可以使用*args ，或者通过init函数初始化好后传入
    def calculate(self,exe_price1,cost_price1,is_call1,is_long1,exe_price2,cost_price2,is_call2,is_long2):
        #print(exe_price1,cost_price1,is_call1,is_long1,exe_price2,cost_price2,is_call2,is_long2)
        if exe_price1>exe_price2:
            high_price=exe_price1
            low_price =exe_price2
        else:
            high_price = exe_price2
            low_price = exe_price1
        #cur_price_list=list( np.arange(0,(high_price+low_price)*1.2,high_price/20))
        #cur_price_list=list( np.arange(low_price*0.8,high_price*1.2,0.5))
        cur_price_list=list(np.linspace(math.floor(low_price*0.8),math.ceil(high_price*1.2),21))
        print(cur_price_list)

        #使用 列表推导式 计算当前价与两个行权价之间的差
        delta_price1 = list( x-exe_price1 for x in cur_price_list  )
        delta_price2 = list( y-exe_price2 for y in cur_price_list  )

     #第一个合约
        #根据合约的 call:认购  long： 买入
        if is_long1==1 and is_call1==1:
            adjust_delta_price1=[]
            for x in delta_price1:
                if x<=0:
                    adjust_delta_price1.append(0)
                else:
                    adjust_delta_price1.append(x)

            adjust_delta_price1=list( x-cost_price1 for  x in adjust_delta_price1 )
            #print(cur_price_list)
            #print(adjust_delta_price1)
        elif is_long1==1 and is_call1==0:
            adjust_delta_price1=[]
            for x in delta_price1:
                if x>=0 :
                    adjust_delta_price1.append(0)
                else:
                    adjust_delta_price1.append(-x)
            adjust_delta_price1 = list(x - cost_price1 for x in adjust_delta_price1)
        elif is_long1==0 and is_call1==1:
            adjust_delta_price1 = []
            for x in delta_price1:
                if x <= 0:
                    adjust_delta_price1.append(0)
                else:
                    adjust_delta_price1.append(-x)
            adjust_delta_price1 = list(x + cost_price1 for x in adjust_delta_price1)
        elif is_long1==0 and is_call1==0:
            adjust_delta_price1 = []
            for x in delta_price1:
                if x >= 0:
                    adjust_delta_price1.append(0)
                else:
                    adjust_delta_price1.append(-x)
            adjust_delta_price1 = list(x + cost_price1 for x in adjust_delta_price1)

    #第二个合约
        #根据合约的 call:认购  long： 买入
        if is_long2==1 and is_call2==1:
            adjust_delta_price2=[]
            for x in delta_price2:
                if x<=0:
                    adjust_delta_price2.append(0)
                else:
                    adjust_delta_price2.append(x)

            adjust_delta_price2=list( x-cost_price1 for  x in adjust_delta_price1 )
            #print(cur_price_list)
            #print(adjust_delta_price2)
        elif is_long2==1 and is_call2==0:
            adjust_delta_price2=[]
            for x in delta_price2:
                if x>=0 :
                    adjust_delta_price2.append(0)
                else:
                    adjust_delta_price2.append(-x)
            adjust_delta_price2 = list(x - cost_price2 for x in adjust_delta_price2)
        elif is_long2==0 and is_call2==1:
            adjust_delta_price2 = []
            for x in delta_price2:
                if x <= 0:
                    adjust_delta_price2.append(0)
                else:
                    adjust_delta_price2.append(-x)
            adjust_delta_price2 = list(x + cost_price2 for x in adjust_delta_price2)
        elif is_long2==0 and is_call2==0:
            adjust_delta_price2 = []
            for x in delta_price2:
                if x >= 0:
                    adjust_delta_price2.append(0)
                else:
                    adjust_delta_price2.append(x)
            adjust_delta_price2 = list(x + cost_price2 for x in adjust_delta_price2)

        print(adjust_delta_price1)
        print(adjust_delta_price2)

        #两个队列合并，计算总收益
        func=lambda x,y:x+y
        rev_list=list(map(func,adjust_delta_price1,adjust_delta_price2))
        print(rev_list)

        # 画图
        x=np.linspace(low_price*0.9,high_price*1.1,10)
        plt.figure()
        plt.xticks(cur_price_list)
        plt.plot(cur_price_list,rev_list)
        plt.show()



if __name__ =='__main__':
    r=Revenue()
    r.calculate(2.7,9.6,1,1,    2.7,9.5,0,1)
    x=np.linspace(0,100)
