from tkinter import *

def save_grammaire():
    etat_primaire_info=etat_primaire.get()
    etat_finale_info=etat_finaeux.get()
    list_etats_info=list_des_etats.get()
    print(etat_primaire_info)
    print(etat_finale_info)
    print(list_etats_info)

    test_1=True
    test_2=True
    test_3=True
    for g in etat_primaire_info :
        if not ("A"<=g<="Z"):
            test_1=False
            break

    for g in etat_finale_info:
        if not ("A"<=g<="Z"or g==" "):
            test_2=False
            break

    for g in list_etats_info:
        if not("A"<=g<="Z" or g in ["-",">"]):
            test_3=False
            break

    if test_1 and test_2 and test_3:
        file=open('grammaire.txt','w')
        file.write(etat_primaire_info)
        file.write("\n")
        L=etat_finale_info.split(" ")
        for i in range(len(L)):
            file.write(L[i])
            file.write("\n")
        file.write(list_etats_info)
        file.close()
        return "grammaire: ",etat_primaire_info," et les etats fineaux: ",etat_finale_info," est dans le file "
    else :
        rmq=Label(text="error")
        rmq.place(x=50,y=300)
        heading.pack()





screen= Tk()
screen.geometry("400x400")
screen.title("automate")
heading=Label(text="automate",bg="grey",fg="black",width="500",height="3")
heading.pack()




primaire=Label(text="l'etats primaire est ")
primaire.place(x=10,y=60)
heading.pack()

final=Label(text="les etats finale sont :")
final.place(x=10,y=120)
heading.pack()


#rmq=Label(text="utliliser a et b comme vocabulaire")
#rmq.place(x=10,y=350)
#heading.pack()

list_etats=Label(text="list des etats")
list_etats.place(x=10,y=200)
heading.pack()

etat_primaire=StringVar()
etat_finaeux=StringVar()
list_des_etats=StringVar()


etat_primaire_entry=Entry(textvariable=etat_primaire ,width="60")
etat_primaire_entry.place(x=10,y=80)

etat_finaeux_entry=Entry(textvariable=etat_finaeux,width="60")
etat_finaeux_entry.place(x=10,y=160)

list_etats_entry=Entry(textvariable=list_des_etats,width="60")
list_etats_entry.place(x=10,y=250)


button = Button(screen,text = 'envoyer',width="30",command=save_grammaire,bg="grey")
button.place(x=50,y=350)



heading.mainloop()