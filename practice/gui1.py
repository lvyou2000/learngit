import tkinter as tk

class App():
    def __init__(self,master):
        frame=tk.Frame(master)
        frame.pack(ipadx=100,padx=10,pady=10)
        self.hi_there=tk.Button(frame,text="进入秘境",fg="black",command=self.say_hi)
        self.hi_there.pack()
    def say_hi(self):
        print("我就知道你是个LSP，你想看的都没有！")
root=tk.Tk()#根窗口
root.geometry("300x150+300+0")
app=App(root)
root.title("demo")
var=tk.StringVar()
var.set("FBI Waring!\n 您所观看的内容含有未成年人限制内容，\n请年满18周岁以上再点击观看")
the_label=tk.Label(root,textvariable=var)
the_label.pack()
photo=tk.PhotoImage("E:\python\\aaa\cat.jpg")
image_label=tk.Label(root,image=photo,justify=tk.LEFT,compound=tk.CENTER,fg="white")
image_label.pack()
root.mainloop()#主事件循环，tkinter代码的最后一句
