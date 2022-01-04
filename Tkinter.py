from tkinter import*
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
def klikker_minus(event):
    global klik
    klik-=1
    lgl.configure(text=klik)
def txt_to_lbl(event):
    #pass
    text=txt.get()#From Entry to text
    lbl.configure(text=text_to_lbl)
    txt.delete(0,END)
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.delete(0,valik_)
    txt.insert(0,valik_)
aken=Tk() #teeme aken
aken.title("akna nimetus") #sisestame akna nimi
aken.geometry("400x300") #akna suurus
nupp=Button(aken,text="Mina olen nupp\nVajuta mind!",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE) #esemesena kirjutakse see kuhu kasutstakse nuppu, teksat- kirjutame ningi tekst,font-шрифт,fg-värv, bg-фон, height-pikkus, width-laius, relief-GROOVE,RAISED,SUNKEN
nupp.bind("<Button-1>",klikker)#LKM
nupp.bind("<Button-3>",klikker_minus)#PMK
lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="green",bg="lightblue")
txt=Entry(aken,width=20,font="Arial 20",fg="blue",bg="lightblue",justify=CENTER)
txt.bind("<Return>",txt_to_lbl) #Enter

i1=PhotoImage(file="1.png")
i2=PhotoImage(file="2.png")
i3=PhotoImage(file="3.png")
var=StringVar()
var.set("üks")
r1=Radiobutton(aken,image=i1,variable=var,value="üks",command=valik)
r2=Radiobutton(aken,image=i2,variable=var,value="kaks",command=valik)
r3=Radiobutton(aken,image=i3,variable=var,value="kolm",command=valik)

lbl.pack()
nupp.pack()#side=LEFT,TOP,RIGHT 
txt.pack()
r1.pack()
r2.pack()
r3.pack()
aken.mainloop()
