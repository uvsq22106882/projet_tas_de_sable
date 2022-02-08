from tkinter import *


sandpile_w= Tk()

sandpile_w.title("Tas de sable")

sandpile_w.geometry("600x600")


monCanvas = Canvas(sandpile_w, width=500, height=500, bg='ivory')
monCanvas.pack()
monCanvas.place(x=50,y=50)

def fun():  
    messagebox.showinfo("Hello", "Red Button clicked")  


b1 = Button(sandpile_w,text = "Red",command = fun,activeforeground = "red",activebackground = "pink",pady=10)  

b1.pack(side = LEFT)  
bouton = sandpile_w.Button (text = "zone de texte")

sandpile_w.mainloop()

