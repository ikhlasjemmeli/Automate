from operator import truediv
from tkinter import *
from array import *

#lire apartir d'un fichier
f =open("mot.txt","r")
chaine= f.readlines()
f.close()
for i in chaine :
   if(i=="\n"):
        print("erreur")
   else :
        print(i)


#mot -> automate
Window = Tk()
Window.geometry("1350x300")
c=Canvas(Window,width=1350,height=300,bg="white")


def etoile(ch):
     L=[]
     C=[]
     R=[]
     n=0
     k=0
     for i in range(len(ch)):
          if ch[i]!="*":
               L.append(ch[i])
          else:
               C.append(i)

     for i in range(len(ch)):
          if C[len(C)-1]>=i:
               for j in C:
                    if j!=i and j>i:
                         R.append(chr(65+n))
                         n=n+1
                         k=k+1
                         break
                    else:
                         if j==i:
                              R.append(R[k-1])
                              k=k+1
                              break
          else:
               R.append(chr(65+n))
               n=n+1
     return R


#def plus(ch)
#def parenthese(ch)



ch=chaine[0]
V=[]
test=True
n=len(ch)

for i in range(len(ch)):
     if ch[i] =="*":
          L=etoile(ch)
          test=False
          break

#print(L)

if test==True:
     L=[]
     for i in range(n+1):
          L.append(chr(65+i))




for i in range(len(ch)):
     if ch[i] not in ["*","+","(",")"]:
          V.append(ch[i])
     else:
          V.append(ch[i-1])


R=[]


print(V)

if test==True:
     for i in range(min(len(V),n)):
          R.append(V[i]+L[i+1])
else:
     for i in range(min(len(V),len(L))):
          R.append(V[i]+L[i])

print(R)

if test==True:
     for i in range(len(R)):
          c.create_text(50,50+(50*i),text=L[i])
          c.create_line(60,50+(50*i),130,50+(50*i),fill="black",arrow="last",width=5)
          c.create_text(140,50+(50*i),text=R[i])
else:
     for i in range(len(R)):
          c.create_text(50,50+(50*i),text=L[i])
          c.create_line(60,50+(50*i),130,50+(50*i),fill="black",arrow="last",width=5)
          c.create_text(140,50+(50*i),text=R[i])



if test==True:
     c.create_text(50,50+(50*(1+i)),text=L[i+1])
     c.create_line(60,50+(50*(i+1)),130,50+(50*(1+i)),fill="black",arrow="last",width=5)
     c.create_text(140,50+(50*(1+i)),text="£")
else:
     c.create_text(50,50+(50*(1+i)),text=L[i])
     c.create_line(60,50+(50*(i+1)),130,50+(50*(1+i)),fill="black",arrow="last",width=5)
     c.create_text(140,50+(50*(1+i)),text="£")




c.pack(pady=20)
Window.mainloop()