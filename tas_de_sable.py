import tkinter as tk
import random as rd 
HEIGHT = 500
WIDTH = 500
l=[[0,0,0],[0,0,0],[0,0,0]]
liste=[]
couleur = {0:"white", 1:"grey", 2:"purple", 3:"blue", 4:"green", 5:"yellow", 6:"orange", 7:"red"}
#créer une fonction aleatoire pour avoir une grille 

def configuration_aléatoire():
    global l , liste
    for i in range(len(l)):
        for j in range (len(l)):
            l[i][j]=rd.randint(0,9)
    liste.append(l)
    print(liste)


def initialisation():
  l=[[0,0,0],[0,0,0],[0,0,0]]
  liste.append(l)
  print(liste)     
#utiliser le random pour créer une grille aleatoires
###################################
racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
canvas.grid()
Bouton1=tk.Button(racine, text="configuration aléatoire" , command= configuration_aléatoire , font=("Calibri","17"))
Bouton2=tk.Button(racine, text="initialisation" , command=initialisation , font=("calibir","17"))
Bouton1.grid()
Bouton2.grid()
racine.mainloop() # Lancement de la boucle principale
