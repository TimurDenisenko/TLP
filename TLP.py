from tkinter import *
from tkinter import ttk
from random import *
import io as io
from os import *
from re import *

def loe(file):
    tem=[]
    with io.open(file,"r",encoding="utf-8-sig") as f:
        for i in f:
            tem.append(i.strip())
    return tem

def salv(tem,file):
    for i in range(len(tem)):
        tem[i]+="\n"
    with io.open(file,"w",encoding="utf-8-sig") as f:
        f.writelines(tem)

fon="White"
tekst="Black"
kaust="Light"

def D(func,win):
    global fon,tekst,kaust
    fon="Black"
    tekst="White"
    kaust="Dark"
    func(win)

def L(func,win):
    global fon,tekst,kaust
    fon="White"
    tekst="Black"
    kaust="Light"
    func(win)

def kodu(win=None):
    global fon,tekst
    if win:
       win.destroy()
    win=Tk()
    win.geometry("600x600")
    win.resizable(width=False,height=False)
    win.title("Kodu")
    win.iconbitmap("brain.ico")
    win.configure(bg=fon)
    lbl=Label(win,text="Võllapuud",font="Arial 40",bg=fon,fg=tekst)
    imgpet=PhotoImage(file="petl.png")
    imgpet=imgpet.subsample(6,6)
    lblpet=Label(win,image=imgpet,bg=fon)

    btnrez=Button(win,text="Režiimid",bg="Green",font="Arial 20",fg="White", width=19, relief=GROOVE,activeforeground="Green",command=lambda: rez(win))
    imgrez=PhotoImage(file="rez.png")
    imgrez=imgrez.subsample(5,5)
    lblrez=Label(win,image=imgrez,bg=fon)

    btnst=Button(win,text="Stuudio",bg="Orange",fg="White",font="Arial 20",width=19,relief=GROOVE,activeforeground="Orange", command=lambda: stuudio(win))
    imgmk=PhotoImage(file="molklu.png")
    imgmk=imgmk.subsample(11,11)
    lblmk=Label(win,image=imgmk,bg=fon)

    btnlp=Button(win,text="Lõpeta mäng",bg="Red",fg="White",font="Arial 20",width=19,relief=GROOVE,activeforeground="Red",command=lambda: lop(win))
    imglp=PhotoImage(file="lop.png")
    imglp=imglp.subsample(5,5)
    lbllp=Label(win,image=imglp,bg=fon)

    btnD=Button(win,text="Tume",font="Arial 20",bg="Blue",fg="White",command=lambda:D(kodu,win))
    btnL=Button(win,text="Valgus",font="Arial 20",bg="Orange",fg="White",command=lambda:L(kodu,win))
    btnL.place(x=490,y=540)
    btnD.place(x=390,y=540)

    lbl.place(x=165,y=50)
    lblpet.place(x=395,y=30)
    btnrez.place(x=0,y=200)
    lblrez.place(x=320,y=178)
    btnst.place(x=0,y=300)
    lblmk.place(x=330,y=288)
    btnlp.place(x=0,y=400)
    lbllp.place(x=335,y=395)

    win.mainloop()

def lop(win):
    win.destroy()

def rez(win):
    win.destroy()
    win=Tk()
    win.geometry("600x600")
    win.resizable(width=False,height=False)
    win.iconbitmap("rez.ico")
    win.title("Režiimid")
    win.configure(bg=fon)

    lbl=Label(win,text="Režiimid",font="Arial 40",bg=fon,fg=tekst)
    imgrez=PhotoImage(file="rez.png")
    imgrez=imgrez.subsample(5,5)
    lblrez=Label(win,image=imgrez,bg=fon)

    var=IntVar()

    rbsolo=Radiobutton(win,text="Üksikmängija mäng",font="Arial 20",fg="Blue",bg=fon,variable=var,value=1)
    imgsolo=PhotoImage(file=kaust+"\\stick.png")
    imgsolo=imgsolo.subsample(9,9)
    lblsolo=Label(win,image=imgsolo,bg=fon)

    rbbot=Radiobutton(win,text="Robotimäng",font="Arial 20",bg=fon,fg="Red",variable=var, value=2)
    imgrob=PhotoImage(file=kaust+"\\robot.png")
    imgrob=imgrob.subsample(23,23)
    lblrob=Label(win,image=imgrob,bg=fon)

    rbmulti=Radiobutton(win,text="Mängib sõbraga",bg=fon,font="Arial 20",fg="Purple",variable=var,value=3)
    imgmulti=PhotoImage(file=kaust+"\\2stick.png")
    imgmulti=imgmulti.subsample(9,9)
    lblmulti=Label(win,image=imgmulti,bg=fon)

    btnmang=Button(win,text="Mängi",font="Arial 20",width=19,bg="Green",fg="White",activeforeground="Green",command=lambda: rezvar(var,win))

    img=PhotoImage(file=kaust+"\\kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,bg=fon,command=lambda: kodu(win))
    btn.place(x=0,y=0)

    btnD=Button(win,text="Tume",font="Arial 20",bg="Blue",fg="White",command=lambda:D(rez,win))
    btnL=Button(win,text="Valgus",font="Arial 20",bg="Orange",fg="White",command=lambda:L(rez,win))
    btnL.place(x=490,y=540)
    btnD.place(x=390,y=540)

    lbl.place(x=190,y=50)
    lblrez.place(x=395,y=30)
    rbsolo.place(x=165,y=200)
    lblsolo.place(x=430,y=190)
    rbbot.place(x=165,y=280)
    lblrob.place(x=350,y=265)
    rbmulti.place(x=165,y=360)
    lblmulti.place(x=390,y=350)
    btnmang.place(x=150,y=450)

    win.mainloop()

def rezvar(var,win):
    global nimi,img1,n,x1,y1,ico1
    v=var.get()
    if v==1:
        nimi="Üksikmängija mäng";img1="stick.png";n=9;x1=465;y1=50;ico1="stick.ico"
        solomang(win,solomang3)
    if v==2:
        nimi="Robotimäng";img1="robot.png";n=15;x1=350;y1=20;ico1="robot.ico"
        solomang(win,robomang)

def solomangg(win):
    win.destroy()

def solomang(win,func):
    global nimi,img1,n,x1,y1,ico1
    if win:
        win.destroy()
    win=Tk()
    win.resizable(width=False,height=False)
    win.geometry("600x600")
    win.title(nimi)
    win.iconbitmap(ico1)
    win.configure(bg=fon)

    lbl=Label(win,text=nimi,font="Arial 30",bg=fon,fg=tekst)
    imgsolo=PhotoImage(file=kaust+"\\"+img1)
    imgsolo=imgsolo.subsample(n,n)
    lblsolo=Label(win,image=imgsolo,bg=fon)

    lblnimi=Label(win,text="Kirjuta sinu nimi:",bg=fon,fg=tekst,font="Arial 20")
    entnimi=Entry(win,font="Arial 20",fg="Blue",width=13)

    var1=IntVar()

    rbr=Radiobutton(win,text="Vali teema juhuslikult",font="Arial 20",fg="Purple",bg=fon,variable=var1,value=1)
    rbi=Radiobutton(win,text="Vali oma teema",font="Arial 20",fg="Purple",bg=fon,variable=var1,value=2)

    btnv=Button(win,text="Valmis",font="Arial 20",width=19,fg="White",bg="Green",activeforeground="Green",command=lambda: solomang2(entnimi,var1,rbr,rbi,win,func))

    img=PhotoImage(file=kaust+"\\kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,bg=fon,command=lambda: kodu(win))
    btn.place(x=0,y=0)

    btnD=Button(win,text="Tume",font="Arial 20",bg="Blue",fg="White",command=lambda:D(solomang,win))
    btnL=Button(win,text="Valgus",font="Arial 20",bg="Orange",fg="White",command=lambda:L(solomang,win))
    btnL.place(x=490,y=540)
    btnD.place(x=390,y=540)

    lbl.place(x=120,y=50)
    lblsolo.place(x=x1,y=y1)
    lblnimi.place(x=50,y=200)
    entnimi.place(x=50,y=250)
    rbr.place(x=300,y=200)
    rbi.place(x=300,y=250)
    btnv.place(x=120,y=330)

    win.mainloop()

def solomang2(entnimi,var,rbr,rbi,win,func):
    nimi=entnimi.get()
    global sona1
    if len(nimi)!=0:
        entnimi.configure(bg="White")
        v=var.get()
        if v in [1,2]:
            rbr.configure(fg="Purple")
            rbi.configure(fg="Purple")
            teemad=otsifiletxt()
            if v==1:
                teema=choice(teemad)
                teema+=".txt"
                sona=choice(filetolist(teema))
            else:
                valiteema(win,entnimi,func)
            sona1=sona
            func(win)
        else:
            rbr.configure(fg="Red")
            rbi.configure(fg="Red")
    else:
        entnimi.configure(bg="Red")

def otsifiletxt():
    teemad=[]
    files=listdir(getcwd())
    for i in files:
        if i.endswith(".txt"):
            i=sub(".txt","",i)
            teemad.append(i)
    return teemad

def valiteema(win,entnimi,func):
    win.destroy()
    win=Tk()
    win.title("Vali teema")
    win.geometry("300x400")
    win.resizable(width=False,height=True)

    teemad=otsifiletxt()

    lbl=Label(win,text="Vali teema",font="Arial 20")
    cb=ttk.Combobox(win,values=teemad)
    btn=Button(win,text="Vali",font="Arial 20",width=10,bg="Green",fg="White",activeforeground="Green",command=lambda: retvar(cb,win,btn,entnimi,func))

    lbl.pack()
    cb.pack()
    btn.pack(side=BOTTOM)

    win.mainloop()

def retvar(cb,win,btn,entnimi,func):
    global v1
    v1=cb.get()
    teemad=otsifiletxt()
    if v1 not in teemad:
        btn.configure(bg="Red")
    else:
        btn.configure(bg="White")
        v1+=".txt"
        sona=choice(filetolist(v1))
        global sona1
        sona1=sona
        func(win)

lst=None
vimg="v0.png"

def mang(win,ent,lblsona,lblvis,lblk,p1=None,p2=None):
    a=ent.get()
    global sona1, lst, vimg
    sonalst=list(sona1.lower())
    a=a.lower()
    if len(a)==1 and a.isalpha() or a==" ":
        ent.configure(bg="white")
        if a in sonalst:
            lblk.configure(text=":)",bg=fon,fg=tekst,font="Arial 100")
            ind=sonalst.index(a)
            if ind==0:
                a=a.upper()
            print(a)
            lst[ind]=a
            sonalst=lst
            sona1=sona1.replace(a,"*",1)
            if a.lower() in sona1:
                mang(win,ent,lblsona,lblvis,lblk)
            sona=" ".join(sonalst)
            lblsona.configure(text=sona)
            if "_" not in sonalst:
                win.destroy()
                win=Tk()
                win.geometry("300x300")
                win.title("Võit")
                win.iconbitmap("win.ico")
                win.resizable(width=False,height=False)

                lbl=Label(win,text="Võit!",font="Arial 30",fg=tekst,bg=fon)
                imgk=PhotoImage(file="win.png")
                imgk=imgk.subsample(2,2)
                lblk=Label(win,image=imgk,bg=fon)

                img=PhotoImage(file="kodu.png")
                img=img.subsample(9,9)
                btn=Button(win,image=img,bg=fon,command=lambda: kodu(win))
                btn.place(x=0,y=0)

                lbl.place(x=100,y=5)
                lblk.place(x=20,y=50)

                win.mainloop()
        else:
            lblk.configure(text=":(",bg=fon,fg=tekst,font="Arial 100")
            vimg=list(vimg)
            vimg[1]=str(int(vimg[1])+1)
            vimg="".join(vimg)
            if vimg=="v10.png":
                win.destroy()
                win=Tk()
                win.geometry("300x300")
                win.title("Kaotamas")
                win.iconbitmap("lose.ico")
                win.resizable(width=False,height=False)

                lbl=Label(win,text="Kaotamas!",font="Arial 30",fg=tekst,bg=fon)
                imgk=PhotoImage(file=kaust+"\\lose.png")
                imgk=imgk.subsample(2,2)
                lblk=Label(win,image=imgk,bg=fon)

                img=PhotoImage(file=kaust+"\\kodu.png")
                img=img.subsample(9,9)
                btn=Button(win,image=img,bg=fon,command=lambda: kodu(win))
                btn.place(x=0,y=0)

                lbl.place(x=70,y=5)
                lblk.place(x=20,y=50)

                win.mainloop()
            vimg1=vimg
            vimg1=PhotoImage(file=kaust+"\\"+vimg1)
            vimg1.photo=vimg1
            lblvis.destroy()
            lblvis=Label(win,image=vimg1)
            lblvis.place(x=50,y=100)
    else:
        ent.configure(bg="Red")

def robomang(win):
    win.destroy()
    global sona1,lst,vimg
    sona=lst=sona1
    for i in sona:
        sona=sona.replace(i,"_ ")
    lst=list(lst)
    for i in range(len(lst)):
        lst[i]="_"
    win=Tk()
    win.configure(bg=fon)
    win.geometry("1280x800")
    win.title("Robotimäng")
    win.resizable(width=False,height=False)
    win.iconbitmap("robot.ico")
    win.configure(bg=fon)

    lbl=Label(win,text="Robotimäng",font="Arial 30",bg=fon,fg=tekst)
    imgsolo=PhotoImage(file=kaust+"\\robot.png")
    imgsolo=imgsolo.subsample(16,16)
    lblsolo=Label(win,image=imgsolo,bg=fon)

    vimg1=PhotoImage(file=kaust+"\\v0.png")
    lblvis=Label(win,image=vimg1,bg=fon)

    lblk=Label(win,bg=fon,fg=tekst)

    lblsona=Label(win,text=sona,font="Arial 25",bg=fon,fg=tekst)
    ent=Entry(win,font="Arial 20",width=3)
    print(sona1)
    btnvod=Button(win,text="Proovida",font="Arial 20",bg="Purple",fg="White",activeforeground="Purple",command=lambda: mang(win,ent,lblsona,lblvis,lblk))

    img=PhotoImage(file=kaust+"\\kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,bg=fon,command=lambda: kodu(win))
    btn.place(x=0,y=0)    

    lbl.place(x=120,y=20)
    lblsolo.place(x=350,y=10)
    lblsona.place(x=50,y=520)
    ent.place(x=50,y=620)
    btnvod.place(x=150,y=620)
    lblvis.place(x=200,y=100)
    lblk.place(x=1000,y=200)

    win.mainloop()



def solomang3(win):
    win.destroy()
    global sona1,lst,vimg
    sona=lst=sona1
    for i in sona:
        sona=sona.replace(i,"_ ")
    lst=list(lst)
    for i in range(len(lst)):
        lst[i]="_"
    win=Tk()
    win.configure(bg=fon)
    win.geometry("1280x800")
    win.title("Üksikmängija mäng")
    win.resizable(width=False,height=False)
    win.iconbitmap("stick.ico")
    win.configure(bg=fon)

    lbl=Label(win,text="Üksikmängija mäng",font="Arial 30",bg=fon,fg=tekst)
    imgsolo=PhotoImage(file=kaust+"\\stick.png")
    imgsolo=imgsolo.subsample(9,9)
    lblsolo=Label(win,image=imgsolo,bg=fon)

    vimg1=PhotoImage(file=kaust+"\\v0.png")
    lblvis=Label(win,image=vimg1,bg=fon)

    lblk=Label(win,bg=fon,fg=tekst)

    lblsona=Label(win,text=sona,font="Arial 25",bg=fon,fg=tekst)
    ent=Entry(win,font="Arial 20",width=3)
    print(sona1)
    btnvod=Button(win,text="Proovida",font="Arial 20",bg="Purple",fg="White",activeforeground="Purple",command=lambda: mang(win,ent,lblsona,lblvis,lblk))

    img=PhotoImage(file=kaust+"\\kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,bg=fon,command=lambda: kodu(win))
    btn.place(x=0,y=0)    

    lbl.place(x=120,y=40)
    lblsolo.place(x=465,y=40)
    lblsona.place(x=50,y=520)
    ent.place(x=50,y=620)
    btnvod.place(x=150,y=620)
    lblvis.place(x=50,y=100)
    lblk.place(x=1000,y=200)

    win.mainloop()

def stuudio(win):
    win.destroy()
    win=Tk()
    win.title("Stuudio")
    win.geometry("600x600")
    win.resizable(width=False,height=False)
    win.iconbitmap("molklu.ico")
    win.configure(bg=fon)

    lbl=Label(win,text="Stuudio",fg=tekst,bg=fon,font="Arial 40")
    imgmk=PhotoImage(file="molklu.png")
    imgmk=imgmk.subsample(11,11)
    lblmk=Label(win,image=imgmk,bg=fon)

    var=IntVar()

    rblt=Radiobutton(win,text="Lisa teema",font="Arial 20",bg=fon,fg="#ffc900",variable=var,value=1)
    imgram=PhotoImage(file="raamat.png")
    imgram=imgram.subsample(9,9)
    lbllt=Label(win,image=imgram,bg=fon)

    rbls=Radiobutton(win,text="Lisa sõna",font="Arial 20",bg=fon,fg="#ffba00",variable=var,value=2)
    imgleht=PhotoImage(file=kaust+"\\leht.png")
    imgleht=imgleht.subsample(10,10)
    lblleht=Label(win,image=imgleht,bg=fon)

    rbms=Radiobutton(win,text="Muuda sõna",font="Arial 20",bg=fon,fg="#e6ae19",variable=var,value=3)
    imgpl=PhotoImage(file=kaust+"\\pliiats.png")
    imgpl=imgpl.subsample(11,11)
    lblpl=Label(win,image=imgpl,bg=fon)

    btnhak=Button(win,text="Alusta",font="Arial 20",width=19,bg="Green",fg="White",activeforeground="Green",command=lambda: stuvar(var,win))

    img=PhotoImage(file=kaust+"\\kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,bg=fon,command=lambda: kodu(win))
    btn.place(x=0,y=0)

    btnD=Button(win,text="Tume",font="Arial 20",bg="Blue",fg="White",command=lambda:D(stuudio,win))
    btnL=Button(win,text="Valgus",font="Arial 20",bg="Orange",fg="White",command=lambda:L(stuudio,win))
    btnL.place(x=490,y=540)
    btnD.place(x=390,y=540)

    lbl.place(x=190,y=50)
    lblmk.place(x=380,y=40)
    rblt.place(x=190,y=200)
    lbllt.place(x=390,y=195)
    rbls.place(x=190,y=260)
    lblleht.place(x=350,y=260)
    rbms.place(x=190,y=320)
    lblpl.place(x=380,y=320)
    btnhak.place(x=150,y=450)

    win.mainloop()

def stuvar(var,win):
    v=var.get()
    if v==1:
        lisateema(win)
    elif v==2:
        lisasona(win)
    elif v==3:
        muudasona(win)

def lisateema(win):
    win.destroy()
    win=Tk()
    win.geometry("600x600")
    win.title("Lisa teema")
    win.resizable(width=False,height=False)
    win.iconbitmap("raamat.ico")
    win.configure(bg=fon)

    lbl=Label(win,text="Lisa teema",font="Arial 40",fg=tekst,bg=fon)
    imgram=PhotoImage(file="raamat.png")
    imgram=imgram.subsample(9,9)
    lbllt=Label(win,image=imgram,bg=fon)

    lblsona=Label(win,text="Lisa uus sõna",font="Arial 20",fg=tekst,bg=fon)
    entso=Entry(win,font="Arial 15",width=16,fg="#00008b")
    btnso=Button(win,text="Lisa",font="Arial 18",width=12,bg="Red",fg="White",state="disabled",activeforeground="Red")

    lblteema=Label(win,text="Kirjuta uus teema",font="Arial 20",fg=tekst,bg=fon)
    entte=Entry(win,font="Arial 15",width=19,fg="#00008b")
    btnte=Button(win,text="Lisa",font="Arial 18",width=14,bg="Green",fg="White",activeforeground="Green",command=lambda: lisateemacom(btnte,entte,btnso,entso))

    img=PhotoImage(file=kaust+"\\kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,bg=fon,command=lambda: kodu(win))
    btn.place(x=0,y=0)

    btnD=Button(win,text="Tume",font="Arial 20",bg="Blue",fg="White",command=lambda:D(lisateema,win))
    btnL=Button(win,text="Valgus",font="Arial 20",bg="Orange",fg="White",command=lambda:L(lisateema,win))
    btnL.place(x=490,y=540)
    btnD.place(x=390,y=540)

    lbl.place(x=155,y=40)
    lbllt.place(x=420,y=45)
    lblteema.place(x=50,y=200)
    entte.place(x=50,y=250)
    btnte.place(x=52,y=300)
    lblsona.place(x=380,y=200)
    entso.place(x=380,y=250)
    btnso.place(x=382,y=300)

    win.mainloop()

def error():
        er=Tk()
        er.geometry("400x100")
        er.title("Viga")
        er.resizable(width=False,height=False)
        er.iconbitmap("error.ico")
        lbl=Label(er,text="Kontrolli, kas sisestatud väärtust pole olemas\n ja kas see pole tühi",font="Arial 13",justify=LEFT)
        lbl.pack(side=LEFT)
        er.mainloop()

def lisateemacom(btnte,entte,btnso,entso):
    nimi=entte.get()
    if len(nimi)==0:
        error()
    else:
        try:
            with io.open(f"{nimi}.txt","x",encoding="utf-8-sig") as f:
                btnte.configure(bg="Red",activeforeground="Red",state="disabled")
                entte.configure(state="disabled")
                btnso.configure(bg="Green",activeforeground="Green",state="normal",command=lambda: lisasonacom(nimi,entso,btnso))
        except:
            error()

def filetolist(file):
    lst=[]
    with io.open(file,"r",encoding="utf-8-sig") as f:
        for i in f:
            lst.append(i.strip())
    return lst

def listtofile(lst,file):
    lst1=[]
    for i in lst:
        lst1.append(i+"\n")
    with io.open(file,"w",encoding="utf-8-sig") as f:
        f.writelines(lst1)

def lisasonacom(nimi,entso,btnso,x=None):
    sona=entso.get()
    nimi+=".txt"
    lst=filetolist(nimi)
    if sona not in lst and len(sona)!=0:
        lst.append(sona)
        btnso.configure(bg="Green")
        entso.delete(0,END)
        listtofile(lst,nimi)
    else:
        btnso.configure(bg="Red")
        error()

def kontrollteema(entte,btnso,btnte,entso,func,entmuso=None):
    nimi=entte.get()
    nimi1=nimi
    nimi1+=".txt"
    if path.isfile(nimi1):
        entte.configure(state="disabled")
        btnte.configure(state="disabled")
        btnso.configure(bg="Green",activeforeground="Green",state="normal",command=lambda: func(nimi,entso,btnso,entmuso))
    else:
        entte.configure(bg="Red")

def lisasona(win):
    win.destroy()
    win=Tk()
    win.geometry("600x600")
    win.title("Lisa sõna")
    win.resizable(width=False,height=False)
    win.iconbitmap("leht.ico")
    win.configure(bg=fon)

    lbl=Label(win,text="Lisa sõna",font="Arial 40",bg=fon,fg=tekst)
    imgram=PhotoImage(file=kaust+"\\leht.png")
    imgram=imgram.subsample(9,9)
    lbllt=Label(win,image=imgram,bg=fon)

    lblsona=Label(win,text="Kirjuta uus sõna",font="Arial 20",bg=fon,fg=tekst)
    entso=Entry(win,font="Arial 15",width=16,fg="#00008b")
    btnso=Button(win,text="Lisa",font="Arial 18",width=12,bg="Red",fg="White",state="disabled",activeforeground="Red")

    lblteema=Label(win,text="Kirjuta olemasolev teema ",font="Arial 20",bg=fon,fg=tekst)
    entte=Entry(win,font="Arial 15",width=23,fg="#00008b")
    btnte=Button(win,text="Kontrollima",font="Arial 18",width=17,bg="Green",fg="White",activeforeground="Green",command=lambda: kontrollteema(entte,btnso,btnte,entso,lisasonacom))

    img=PhotoImage(file=kaust+"\\kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,bg=fon,command=lambda: kodu(win))
    btn.place(x=0,y=0)

    btnD=Button(win,text="Tume",font="Arial 20",bg="Blue",fg="White",command=lambda:D(lisasona,win))
    btnL=Button(win,text="Valgus",font="Arial 20",bg="Orange",fg="White",command=lambda:L(lisasona,win))
    btnL.place(x=490,y=540)
    btnD.place(x=390,y=540)

    lbl.place(x=155,y=40)
    lbllt.place(x=390,y=45)
    lblteema.place(x=30,y=200)
    entte.place(x=50,y=250)
    btnte.place(x=55,y=300)
    lblsona.place(x=380,y=200)
    entso.place(x=380,y=250)
    btnso.place(x=382,y=300)

    win.mainloop()

def muudasonacom(nimi,entso,btnso,entmuso):
    nimi+=".txt"
    lst=filetolist(nimi)
    valesona=entmuso.get()
    uussona=entso.get()
    if valesona in lst:
        entmuso.configure(bg="White")
        if uussona not in lst:
            entso.configure(bg="White")
            i=lst.index(valesona)
            lst[i]=uussona
            entmuso.delete(0,END)
            entso.delete(0,END)
            listtofile(lst,nimi)
        else:
            entso.configure(bg="Red")
    else:
        entmuso.configure(bg="Red")

def muudasona(win):
    win.destroy()
    win=Tk()
    win.geometry("600x600")
    win.resizable(width=False,height=False)
    win.title("Muuda sõna")
    win.iconbitmap("pliiats.ico")
    win.configure(bg=fon)

    lbl=Label(win,text="Muuda sõna",font="Arial 40",bg=fon,fg=tekst)
    imgpl=PhotoImage(file=kaust+"\\pliiats.png")
    imgpl=imgpl.subsample(11,11)
    lblpl=Label(win,image=imgpl,bg=fon)

    lblmusona=Label(win,text="Kirjuta vale sõna",font="Arial 20",bg=fon,fg=tekst)
    entmuso=Entry(win,font="Arial 15",width=16,fg="#00008b")

    lblsona=Label(win,text="Kirjuta uus sõna",font="Arial 20",bg=fon,fg=tekst)
    entso=Entry(win,font="Arial 15",width=16,fg="#00008b")

    btnmuuda=Button(win,text="Muuda",font="Arial 18",width=20,state="disabled",bg="Red",fg="White",activeforeground="Red",)

    lblteema=Label(win,text="Kirjuta olemasolev teema ",font="Arial 20",bg=fon,fg=tekst)
    entte=Entry(win,font="Arial 15",width=25,fg="#00008b")
    btnte=Button(win,text="Kontrollima",font="Arial 18",width=20,bg="Green",fg="White",activeforeground="Green",command=lambda: kontrollteema(entte,btnmuuda,btnte,entso,muudasonacom,entmuso))

    img=PhotoImage(file=kaust+"\\kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,bg=fon,command=lambda: kodu(win))
    btn.place(x=0,y=0)

    btnD=Button(win,text="Tume",font="Arial 20",bg="Blue",fg="White",command=lambda:D(muudasona,win))
    btnL=Button(win,text="Valgus",font="Arial 20",bg="Orange",fg="White",command=lambda:L(muudasona,win))
    btnL.place(x=490,y=540)
    btnD.place(x=390,y=540)

    lbl.place(x=155,y=40)
    lblpl.place(x=450,y=40)
    lblteema.place(x=155,y=150)
    entte.place(x=170,y=200)
    btnte.place(x=165,y=250)
    lblmusona.place(x=50,y=320)
    entmuso.place(x=60,y=370)
    lblsona.place(x=350,y=320)
    entso.place(x=360,y=370)
    btnmuuda.place(x=165,y=430)

    win.mainloop()

kodu()
