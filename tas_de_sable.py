import tkinter as tk
import random as rd 
HEIGHT = 500
WIDTH = 500
l1=[]
l2=[]
l3=[]
def configuration():
    global l1,l2,l3
    l1=[rd.randint(0,9),rd.randint(0,9),rd.randint(0,9)]
    l2=[rd.randint(0,9),rd.randint(0,9),rd.randint(0,9)]
    l3=[rd.randint(0,9),rd.randint(0,9),rd.randint(0,9)] 
    print(l1)
    print(l2)
    print(l3)
    return 
#utiliser le random pour créer 3 listes aleatoires
racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
canvas.grid()
Bouton=tk.Button(racine, text="configuration aléatoire " , command=configuration , font=("Calibri","17"))
Bouton.grid()
racine.mainloop() # Lancement de la boucle principale
