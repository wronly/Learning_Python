from tkinter import *
import numpy as np
from revenue import Revenue
import tkinter

def run():
    if(CheckVar1.get()==0 and CheckVar2.get()==0 and CheckVar3.get()==0 and CheckVar4.get()==0):
        s_1 = '您还没选择任何组合策略'
    else:
        s1 = "认购" if CheckVar1.get() == 1 else ""
        s2 = "认沽" if CheckVar2.get() == 1 else ""
        s3 = "买入" if CheckVar3.get() == 1 else ""
        s4 = "卖出" if CheckVar4.get() == 1 else ""
        s_1  = "第一个合约：%s %s %s %s 合约" % (s1,s2,s3,s4)
    lb2.config(text=s_1) 

    exe_price1 =float(inp1.get())
    cost_price1=float(inp2.get())


    if(CheckVar5.get()==0 and CheckVar6.get()==0 and CheckVar7.get()==0 and CheckVar8.get()==0):
        s_2 = '您还没选择任何组合策略'
    else:
        s5 = "认购" if CheckVar5.get() == 1 else ""
        s6 = "认沽" if CheckVar6.get() == 1 else ""
        s7 = "买入" if CheckVar7.get() == 1 else ""
        s8 = "卖出" if CheckVar8.get() == 1 else ""
        s_2  = "第二个合约：%s %s %s %s 合约" % (s5,s6,s7,s8)
    lb3.config(text=s_2) 

    exe_price2 =float(inp3.get())
    cost_price2=float(inp4.get())

    #运行画图函数
    is_call1= CheckVar1.get() if CheckVar1.get() == 1 else 0
    is_long1= CheckVar3.get() if CheckVar3.get() == 1 else 0

    is_call2= CheckVar5.get() if CheckVar5.get() == 1 else 0
    is_long2= CheckVar7.get() if CheckVar7.get() == 1 else 0
    rev=Revenue()
    print(exe_price1,cost_price1,is_call1,is_long1,exe_price2,cost_price2,is_call2,is_long2)
    rev.calculate(exe_price1,cost_price1,is_call1,is_long1,exe_price2,cost_price2,is_call2,is_long2)


root = tkinter.Tk()
root.geometry('800x600')
root.title('股票期权组合策略')
lb1=Label(root,text='请选择您的组合')

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()

#第一个合约
ch1 = Checkbutton(root,text='认购',variable = CheckVar1,onvalue=1,offvalue=0)
ch2 = Checkbutton(root,text='认沽',variable = CheckVar2,onvalue=1,offvalue=0)
ch3 = Checkbutton(root,text='买入',variable = CheckVar3,onvalue=1,offvalue=0)
ch4 = Checkbutton(root,text='卖出',variable = CheckVar4,onvalue=1,offvalue=0)

ch1.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)
ch2.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
ch3.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.1)
ch4.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

#获取价格
inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.1)
inp2 = Entry(root)
inp2.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.1)

#第二个合约
ch5 = Checkbutton(root,text='认购',variable = CheckVar5,onvalue=1,offvalue=0)
ch6 = Checkbutton(root,text='认沽',variable = CheckVar6,onvalue=1,offvalue=0)
ch7 = Checkbutton(root,text='买入',variable = CheckVar7,onvalue=1,offvalue=0)
ch8 = Checkbutton(root,text='卖出',variable = CheckVar8,onvalue=1,offvalue=0)

ch5.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.1)
ch6.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)
ch7.place(relx=0.6, rely=0.3, relwidth=0.3, relheight=0.1)
ch8.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)

#获取价格
inp3 = Entry(root)
inp3.place(relx=0.6, rely=0.6, relwidth=0.3, relheight=0.1)
inp4 = Entry(root)
inp4.place(relx=0.6, rely=0.7, relwidth=0.3, relheight=0.1)

btn = Button(root,text="提交",command=run)
btn.pack()

lb2 = Label(root,text='')
lb2.place(relx=0.1, rely=0.5,relwidth=0.3, relheight=0.1)
lb3 = Label(root,text='')
lb3.place(relx=0.6, rely=0.5,relwidth=0.3, relheight=0.1)
root.mainloop()