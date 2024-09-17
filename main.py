from tkinter import *
from tkinter import messagebox
#from PIL import Image, ImageTk
root=Tk()
root.title('Denomination Counter')
root.geometry('600x600')
root.config(background='Yellow')
#upload=Image.open('Hi\.jpeg')
#upload=upload.resize((300,300))
#image=ImageTk.ImagePhoto(upload)
#l1=Label(root,image=image)
#l1.place(x=180,y=20)
l2=Label(root,text=('Welcome to Denomination Counter'),fg='orange',bg='Yellow')
l2.place(relx=0.5,y=340)
def show():
    m1=messagebox.showinfo('Alert','Do you want to Count denomination')
    if m1=='ok':
        topwin()
b1=Button(root,text=('Lets get started'),command=show,bg='Red',fg='Black')
b1.place(x=260,y=360)

def topwin():
    top=Toplevel()
    top.title('Denomination Window')
    top.config(background=('Green'))
    top.geometry('500x300')
    l3=Label(top,text=('Enter total number'),bg=('Green'))
    e1=Entry(top)
    l4=Label(top,text=('Here are your total number of notes for each denomination'),bg='green')
    l5=Label(top,text='2000',bg='green')
    l6=Label(top,text='500',bg='green')
    l7=Label(top,text='100',bg='green')
    e5=(top)
    e6=(top)
    e7=(top)

    def cal():
     try:
        global amount
        amount=int(e1.get())
        note2000=amount//2000
        amount%=2000
        note500=amount//500 
        amount%=500
        note100=amount//100
        amount%=100
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e5.insert(END,str(note2000))
        e6.insert(END,str(note500))
        e7.insert(END,str(note100))
     except ValueError:
        messagebox.showerror('Error','Invalid Value')
    b2=Button(top,text='Calculate',command=cal)
    
    e1.place(x=200,y=80)
    l4.place(x=140,y=170)
    l5.place(x=180,y=200)
    l6.place(x=180,y=230)
    l7.place(x=180,y=260)
    e5.place(x=270,y=200)
    e6.place(x=270,y=230)
    e7.place(x=270,y=260)
    b2.place(x=240,y=120)
    
    top.mainloop()
        












root.mainloop()