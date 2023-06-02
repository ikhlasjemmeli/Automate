from tkinter import *
#import aut

def save_grammaire():
    grammaire_info=grammaire.get()
    etat_info=etat_finaeux.get()
    print(grammaire_info)
    print(etat_info)

    test_1=True
    test_2=True
    for g in grammaire_info :
        if not ("A"<=g<="Z" or g in ["a","b","-",">"," "]):
            test_1=False
            break

    for g in etat_info:
        if not ("A"<=g<="Z" or g==" "):
            test_2=False
            break
    if test_1 and test_2:
        file=open('grammaire.txt','w')
        L=grammaire_info.split(" ")
        for i in range(len(L)):
            file.write(L[i])
            file.write("\n")
        file.write(etat_info)
        #print("grammaire: ",grammaire_info," et les etats fineaux: ",etat_info," est dans le file ")
        file.close()
        print("grammaire: ",grammaire_info," et les etats fineaux: ",etat_info," est dans le file ")
        #return "grammaire: ",grammaire_info," et les etats fineaux: ",etat_info," est dans le file "
    else :
        rmq=Label(text="error")
        rmq.place(x=50,y=300)
        heading.pack()

def gram():
    import aut



screen= Tk()
screen.geometry("400x400")
screen.title("automate")
heading=Label(text="automate",bg="grey",fg="black",width="500",height="3")
heading.pack()




gram=Label(text="la grammaire est:")
gram.place(x=10,y=60)
heading.pack()

etat=Label(text="les etats finale sont :")
etat.place(x=10,y=120)
heading.pack()


rmq=Label(text="utliliser a et b comme vocabulaire")
rmq.place(x=10,y=350)
heading.pack()



grammaire=StringVar()
etat_finaeux=StringVar()


grammaire_entry=Entry(textvariable=grammaire ,width="60")
grammaire_entry.place(x=10,y=80)
etat_finaeux_entry=Entry(textvariable=etat_finaeux,width="60")
etat_finaeux_entry.place(x=10,y=160)




button = Button(screen,text = 'envoyer',width="30",command=save_grammaire,bg="grey")
button.place(x=50,y=200)


button = Button(screen,text = 'next',width="30",command=gram,bg="grey")
button.place(x=50,y=300)

heading.mainloop()
