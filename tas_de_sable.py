import tkinter as tk
import random as rd 
HEIGHT = 500
LENGTH = 500
l=[[0,0,0],[0,0,0],[0,0,0]]
liste=[]
x=0
y=0
x1=150
y1=150
v=0
couleur = {0:"white", 1:"grey", 2:"purple", 3:"blue", 4:"green", 5:"yellow", 6:"orange", 7:"red"}
#créer une fonction aleatoire pour avoir une grille 

def configuration_aléatoire():
    global l , liste , x, y, x1, y1 , v
    for i in range(len(l)):
        for j in range (len(l)):
            l[i][j]=rd.randint(0,7)
            couleurs()
    liste.append(l)


def couleurs():
    """
    Affiche la couleur de toutes les cases
    """
    carre1 = canvas.create_rectangle(0,0,LENGTH/3,HEIGHT/3, width=5, fill=couleur[l[0][0]])
    carre2 = canvas.create_rectangle(LENGTH/3,0,LENGTH/3*2,HEIGHT/3, width=5, fill=couleur[l[0][1]])
    carre3 = canvas.create_rectangle(LENGTH/3*2,0,LENGTH,HEIGHT/3, width=5, fill=couleur[l[0][2]])
    carre4 = canvas.create_rectangle(0,HEIGHT/3,LENGTH/3,HEIGHT/3*2, width=5, fill=couleur[l[1][0]])
    carre5 = canvas.create_rectangle(LENGTH/3,HEIGHT/3,LENGTH/3*2,HEIGHT/3*2, width=5, fill=couleur[l[1][1]])
    carre6 = canvas.create_rectangle(LENGTH/3*2,HEIGHT/3,LENGTH,HEIGHT/3*2, width=5, fill=couleur[l[1][2]])
    carre7 = canvas.create_rectangle(0,HEIGHT/3*2,LENGTH/3,HEIGHT, width=5, fill=couleur[l[2][0]])
    carre8 = canvas.create_rectangle(LENGTH/3,HEIGHT/3*2,LENGTH/3*2,HEIGHT, width=5, fill=couleur[l[2][1]])
    carre9 = canvas.create_rectangle(LENGTH/3*2,HEIGHT/3*2,LENGTH,HEIGHT, width=5, fill=couleur[l[2][2]])
    return carre1,carre2,carre3,carre4,carre5,carre6,carre7,carre8,

def initialisation():
  global l , liste 
  l=[[0,0,0],[0,0,0],[0,0,0]]
  couleurs()
  liste.append(l)

#utiliser le random pour créer une grille aleatoires
###################################
racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=LENGTH)
canvas.grid()
Bouton1=tk.Button(racine, text="configuration aléatoire" , command= configuration_aléatoire , font=("Calibri","17"))
Bouton2=tk.Button(racine, text="initialisation" , command=initialisation , font=("calibir","17"))
Bouton1.grid()
Bouton2.grid()
racine.mainloop() # Lancement de la boucle principale
