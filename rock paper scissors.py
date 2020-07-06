import random
from tkinter import*

me=Tk()
me.geometry("354x460")
me.title("ROCK PAPER SCISSORS")
melabel = Label(me,text="PLAY AND HAVE FUN",bg='PINK',font=("ARIAL",25))
melabel.pack(side=TOP)
me.config(background='BROWN')
s=('rock','paper','scissors')
textin=StringVar()

def but_r():
    r=random.choice(s)
    if r=='paper' :
        textin.set('you loose')
    elif r=='scissors' :
        textin.set('you won')
    else :
        textin.set('tie')
        
def but_p():
    r=random.choice(s)
    if r=='rock' :
        textin.set('you won')
    elif r=='scissors' :
        textin.set('you loose')
    else :
        textin.set('tie')
        
def but_s():
    r=random.choice(s)
    if r=='paper' :
        textin.set('you won')
    elif r=='rock' :
        textin.set('you loose')
    else :
        textin.set('tie')
metext=Entry(me,font=("Courier New",16,'bold'),textvar=textin,width=25,bd=10,bg='WHITE')
metext.place(x=5,y=80)
    
but1=Button(me,padx=14,pady=14,bd=4,bg='RED',command=lambda:but_r(),text="rock",font=("Courier New",16,'bold'))
but1.place(x=10,y=150)

but4=Button(me,padx=14,pady=14,bd=4,bg='YELLOW',command=lambda:but_p(),text="paper",font=("Courier New",16,'bold'))
but4.place(x=230,y=150)


butpl=Button(me,padx=14,pady=14,bd=4,bg='ORANGE',text="sicissors",command=lambda:but_s(),font=("Courier New",16,'bold'))
butpl.place(x=80,y=280)

me.mainloop()