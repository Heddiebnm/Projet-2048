import tkinter as tk
import random
from en imoprt *


# Création d'un menu d'affichage

root = tk.Tk()
root.title("2048")
root.geometry('500x400')

# Crée une "entry" vide
entry = tk.Entry(root)
entry.pack()
def save():
    pass

def new_game():
    maj_couleurs()
    start()
    racine.mainloop()

saves = tk.Button(root, text="Save", command=save, font=("helvetica", "20"),
                    relief="groove")  # création d'un widget
saves.grid(column=6, row=0)  # positionnement du bouton save

new = tk.Button(root, text="new game", command=new_game, font=("helvetica", "20"),
                    relief="groove")  # création d'un widget
new.grid(column=5, row=0)  # positionnement du bouton save
root.mainloop()

root = tk.Tk()
root.title("2048")
root.geometry('500x400')

# Crée une "entry" vide
entry = tk.Entry(root)
entry.pack()

def save():
    pass

def new_game():
    maj_couleurs()
    start()
    racine.mainloop()

saves = tk.Button(root, text="Save", command=save, font=("helvetica", "20"),
                    relief="groove")  # création d'un widget
saves.grid(column=0, row=1)  # positionnement du bouton save

new = tk.Button(root, text="new game", command=new_game, font=("helvetica", "20"),
                    relief="groove")  # création d'un widget
new.grid(column=1, row=1)  # positionnement du bouton save
root.mainloop()