from tkinter import *
root = Tk()



'''

#Brian&O&OKR&4&Feuerfinger&Freier Markt&4&1&2&3&3&1&*&XX&662&Uralte Archivsysteme&Martial Arts&7&wortgewandt, vorsichtig, zufrieden&O Komm
O Laser
X Metallschlüssel
B InvinciPille

'''



maxclone=6

def death():
    global maxclone
    i=designationE.get().split("-")
    damageE.delete(0,END)
    treasonE.delete(0,END)
    i[3]=str(int(i[3])+1)
    designationE.delete(0,END)
    designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if int(i[3]) > maxclone:
        root.destroy()

def plone():
    i=int(xpE.get())
    xpE.delete(0,END)
    xpE.insert(0,i+1)

def plten():
    i=int(xpE.get())
    xpE.delete(0,END)
    xpE.insert(0,i+10)

def plhun():
    i=int(xpE.get())
    xpE.delete(0,END)
    xpE.insert(0,i+100)

def mione():
    i=int(xpE.get())
    xpE.delete(0,END)
    xpE.insert(0,i-1)

def miten():
    i=int(xpE.get())
    xpE.delete(0,END)
    xpE.insert(0,i-10)

def mihun():
    i=int(xpE.get())
    xpE.delete(0,END)
    xpE.insert(0,i-100)

def promote():
    i=designationE.get().split("-")
    if i[1]=="V":
        colorF["bg"]="white"
        i[1]="U"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="B":
        colorF["bg"]="purple"
        i[1]="V"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="G":
        colorF["bg"]="blue"
        i[1]="B"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="Y":
        colorF["bg"]="green"
        i[1]="G"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="O":
        colorF["bg"]="yellow"
        i[1]="Y"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="R":
        colorF["bg"]="dark orange"
        i[1]="O"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="I":
        colorF["bg"]="red"
        i[1]="R"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])

def demote():
    i=designationE.get().split("-")
    if i[1]=="R":
        colorF["bg"]="black"
        i[1]="I"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="O":
        colorF["bg"]="red"
        i[1]="R"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="Y":
        colorF["bg"]="dark orange"
        i[1]="O"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="G":
        colorF["bg"]="yellow"
        i[1]="Y"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="B":
        colorF["bg"]="green"
        i[1]="G"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="V":
        colorF["bg"]="blue"
        i[1]="B"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    if i[1]=="U":
        colorF["bg"]="purple"
        i[1]="V"
        designationE.delete(0,END)
        designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])

def heal():
    damageE.delete(0,1)

def hurt():
    damageE.insert(0,"X")
    if damageE.get()=="XXXX":
        death()

def addclone():
    global maxclone
    maxclone +=1

def star():
    treasonE.insert(0,"*")

def random():
    i=1

def load():
    global maxclone
    i=invT.get(1.0,END).split("&")
    designationE.delete(0,END)
    designationE.insert(0,i[0]+"-"+i[1]+"-"+i[2]+"-"+i[3])
    mutationE.delete(0,END)
    mutationE.insert(0,i[4])
    secsocE.delete(0,END)
    secsocE.insert(0,i[5])
    maE.delete(0,END)
    maE.insert(0,i[6])
    viE.delete(0,END)
    viE.insert(0,i[7])
    stE.delete(0,END)
    stE.insert(0,i[8])
    haE.delete(0,END)
    haE.insert(0,i[9])
    soE.delete(0,END)
    soE.insert(0,i[10])
    weE.delete(0,END)
    weE.insert(0,i[11])
    demote()
    promote()


    treasonE.delete(0,END)
    treasonE.insert(0,i[12])

    damageE.delete(0,END)
    damageE.insert(0,i[13])

    xpE.delete(0,END)
    xpE.insert(0,i[14])

    secE.delete(0,END)
    secE.insert(0,i[15])

    illE.delete(0,END)
    illE.insert(0,i[16])
    maxclone=int(i[17])

    adjE.delete(0,END)
    adjE.insert(0,i[18])

    invT.delete(1.0,END)
    invT.insert(1.0,i[19])

def save():
    global maxclone
    i=designationE.get().split("-")[0]+"&"+designationE.get().split("-")[1]+"&"+designationE.get().split("-")[2]+"&"+designationE.get().split("-")[3]+"&"+mutationE.get()+"&"+secsocE.get()+"&"+maE.get()+"&"+viE.get()+"&"+stE.get()+"&"+haE.get()+"&"+soE.get()+"&"+weE.get()+"&"+treasonE.get()+"&"+damageE.get()+"&"+xpE.get()+"&"+secE.get()+"&"+illE.get()+"&"+str(maxclone)+"&"+adjE.get()+"&"+invT.get(1.0,END)
    designationE.delete(0,END)
    mutationE.delete(0,END)
    secsocE.delete(0,END)
    maE.delete(0,END)
    viE.delete(0,END)
    stE.delete(0,END)
    haE.delete(0,END)
    soE.delete(0,END)
    weE.delete(0,END)
    treasonE.delete(0,END)
    damageE.delete(0,END)
    xpE.delete(0,END)
    secE.delete(0,END)
    illE.delete(0,END)
    adjE.delete(0,END)
    invT.delete(1.0,END)
    maxclone=6
    invT.delete(1.0,END)
    invT.insert(1.0,i)



##############################################################################################################
##############################################################################################################
##############################################################################################################



colorF=Frame(root, padx = 15, pady = 15)
colorF.pack()

allF=Frame(colorF)
allF.pack()

designationE=Entry(allF, font="Helvetica")
designationE.pack()

adjE=Entry(allF, width="37")
adjE.pack()

lowerF=Frame(allF)
lowerF.pack()

leftF=Frame(lowerF)
leftF.pack(side=LEFT)

invT=Text(lowerF, width=20, height=22)
invT.pack(side=RIGHT)

mutationE=Entry(leftF,width="19")
mutationE.pack()

secsocE=Entry(leftF,width="19")
secsocE.pack()

attributeF=Frame(leftF)
attributeF.pack()

attvalueF=Frame(attributeF)
attvalueF.pack(side=LEFT)

attnameL=Label(attributeF, text="Management\nViolence\nStealth\n\nHardware\nSoftware\nWetware",justify=LEFT)
attnameL.pack(side=LEFT)

maE=Entry(attvalueF, width="1")
maE.pack()
viE=Entry(attvalueF, width="1")
viE.pack()
stE=Entry(attvalueF, width="1")
stE.pack()
haE=Entry(attvalueF, width="1")
haE.pack()
soE=Entry(attvalueF, width="1")
soE.pack()
weE=Entry(attvalueF, width="1")
weE.pack()

pointsF=Frame(attributeF)
pointsF.pack(side=LEFT)

treasonL=Label(pointsF,text="Verrat")
treasonL.pack()
treasonE=Entry(pointsF, width="6")
treasonE.pack()

damageL=Label(pointsF,text="Schaden")
damageL.pack()
damageE=Entry(pointsF, width="6")
damageE.pack()

xpL=Label(pointsF,text="xpPunkte")
xpL.pack()
xpE=Entry(pointsF, width="6")
xpE.pack()

secE=Entry(leftF,width="19")
secE.pack()

illE=Entry(leftF,width="19")
illE.pack()

butt1F = Frame(leftF)
butt1F.pack()
ploneB = Button(butt1F, width = "1", height="1", text = "+", command=plone)
ploneB.pack(side=LEFT)
pltenB = Button(butt1F, width = "1", height="1", text = "++", command=plten)
pltenB.pack(side=LEFT)
plhunB = Button(butt1F, width = "1", height="1", text = "+++", command=plhun)
plhunB.pack(side=LEFT)
promoteB = Button(butt1F, width = "1", height="1", text = "^", command=promote)
promoteB.pack(side=LEFT)

####container for second row of buttons, horizontally
butt2F = Frame(leftF)
butt2F.pack()
mioneB = Button(butt2F, width = "1", height="1", text = "-", command=mione)
mioneB.pack(side=LEFT)
mitenB = Button(butt2F, width = "1", height="1", text = "- -", command=miten)
mitenB.pack(side=LEFT)
mihunB = Button(butt2F, width = "1", height="1", text = "- - -", command=mihun)
mihunB.pack(side=LEFT)
demoteB = Button(butt2F, width = "1", height="1", text = "v", command=demote)
demoteB.pack(side=LEFT)

####container for third row of buttons, horizontally
butt3F = Frame(leftF)
butt3F.pack()
healB = Button(butt3F, width = "1", height="1", text = ":-)", command=heal)
healB.pack(side=LEFT)
addcloneB = Button(butt3F, width = "1", height="1", text = ":) :)", command=addclone)
addcloneB.pack(side=LEFT)
randB = Button(butt3F, width = "1", height="1",text = "?", command=random)
randB.pack(side=LEFT)
loadB=Button(butt3F, width = "1", height="1", text= "load", command=load)
loadB.pack(side=LEFT)

####container for fourth row of buttons, horizontally
butt4F = Frame(leftF)
butt4F.pack()
hurtB = Button(butt4F, width = "1", height="1",text = ":-(", command=hurt)
hurtB.pack(side=LEFT)
starB = Button(butt4F, width = "1", height="1", text = "*", command=star)
starB.pack(side=LEFT)
deathB = Button(butt4F, width = "1", height="1", text = "!", command=death)
deathB.pack(side=LEFT)
saveB=Button(butt4F, width = "1", height="1",text="save", command=save)
saveB.pack(side=LEFT)

root.mainloop()













