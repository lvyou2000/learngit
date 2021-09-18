#选项框
# from tkinter import *
# root=Tk()
# v=[]
# Girls=["貂蝉","西施","杨玉环","王昭君"]
# for girl in Girls:
#     v.append(IntVar())
#     c=Checkbutton(root,text=girl,variable=v[-1])
#     c.pack(anchor=W)
# l=Label(root,textvariable=v)
# l.pack()
#
# group=LabelFrame(root,text="世界上最好的语言是？",padx=10,pady=10)
# group.pack(padx=10,pady=10)
# Langs=[("python",1),("c++",2),("java",3),("php",4),("javascrip",5)]
# m=IntVar()
# m.set(1)
# for lang,num in Langs:
#     b=Radiobutton(group,text=lang,variable=m,value=num)
#     b.pack(anchor=W)
# mainloop()

#-----------------------------------------------------------------------------------
#账号和密码
from tkinter import *
root=Tk()
Label(root,text="账号：",).grid(row=0,column=0)
Label(root,text="密码：",).grid(row=1,column=0)
v1=StringVar()
v2=StringVar()
e1=Entry(root,textvariable=v1)
e2=Entry(root,textvariable=v2,show="*")
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)

def show():
    print("账号：%s"% e1.get())
    print("密码：%s"% e2.get())
Button(root,text="点击进入查看成绩",width=20,command=show)\
    .grid(row=3,column=0,sticky=W,padx=10,pady=5)
Button(root,text="退出",width=10,command=root.quit)\
    .grid(row=3,column=1,sticky=E,padx=10,pady=5)
mainloop()