
from tkinter import *
from array import *

#lire apartir d'un fichier
f =open("grammaire.txt","r")
chaine= f.readlines()
f.close()
for i in chaine :
   if(i=="\n"):
        print("erreur")
   else :
        print(i)


#automate
Window = Tk()
Window.geometry("1350x300")
c=Canvas(Window,width=1350,height=300,bg="white")

ch1=[]
ch2=[]
ch3=[]
for ch in chaine :
  for i in range(len(ch)) :
       if (ch[i].isupper()) :
         if ch[i] not in ch1:
           ch1.append(ch[i])
  
  for i in range(len(ch)) :
    if (ch[i].islower()) :
      if(ch[0] != ch[4]):
        ch2.append(ch[i])
      else:
        ch3.append(ch[0])
        #for c in range(len(ch3)):
        for j in range(len(ch1)):
           if(ch1[j] == ch3[0] ):
            c.create_line(70+(200*j),98,70+(200*j),140,fill="black",width=5)
            c.create_line(40+(200*j),98,40+(200*j),140,fill="black",width=5,arrow="first")
            c.create_line(40+(200*j),140,70+(200*j),140,fill="black",width=5)
            c.create_text(55+(200*j),150,text=ch[3])

  

  x0=10
  y0=10
  x1=100
  y1=100 

  

  c.create_oval(x0,y0,x1,y1)
  for i in range(len(ch1)-1):
      
    c.create_oval(x0+290+(200*i),y0,x1+100+(200*i),y1)
    c.create_line(100+(200*i),50,200+(200*i),50,fill="black",arrow="last",width=5)

    for i in range(len(ch1)):
      c.create_text(50+(200*i),50,text=ch1[i])
      
    for i in range(len(ch2)):  
      c.create_text(150+(200*i),40,text=ch2[i])
    
 

# double cercle
for i in range(len(ch1)):
  if(ch1[i] == chaine[len(chaine)-1]) :
      c.create_oval(10+(200*i),20,90+(200*i),90)# double cercle



c.pack(pady=20)
Window.mainloop()