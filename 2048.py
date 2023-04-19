import tkinter as tk
import random as rd


def choisir_tuiles_au_hasard():
    tuiles_au_hasard=[]
    for i in range (1):
        tuiles= [2,2,2,2,2,2,2,2,2,4]
        AP_tuiles = rd.randint(0,len(tuiles)-1)
        tuiles_au_hasard=tuiles_au_hasard+tuiles[AP_tuiles]
    return tuiles_au_hasard



def déplacement_droite():
    pass


def déplacement_gauche():
    pass


def déplacement_haut():
    pass


def déplacement_bas():
    pass


def sauvergarder_score():
    mon_fichier = open("fichier.txt", "w")
    mon_fichier.write("user01 :", score)
    mon_fichier.close()
   
def play():
    pass
    
    

racine = tk.Tk()
racine.title("2048")

# Créer une grille
grid = []
for i in range(4):
    row = []
    for j in range(4):
        label = tk.Label(racine, text="", width=4, height=2, font=("Arial", 20, "bold"), bg="gray80")
        label.grid(row=i, column=j, padx=5, pady=5)
        row.append(label)
    grid.append(row)
        

texte = tk.Label(text= "Commencer à jouer")
texte.grid(column= 0, row = 1)
b1 = tk.Button(text = "Play", command = play , font = ("helvetica", "26")) #mettre 2 tuiles de manière aléatoire (2 ou 4) dans la grilles
b1.grid( column =  0, row = 1)


texte = tk.Label(text= "Terminer la partie et voir le score")
texte.grid(column= 1, row = 1)
b1 = tk.Button(text = "Exit", command = "" , font = ("helvetica", "26") ) #finir la partie et afficher le score)
b1.grid( column =  1, row = 1)


texte = tk.Label(text= "Sauvergarder la partie")
texte.grid(column= 0, row = 1)
b1 = tk.Button(text = "Save", command = sauvergarder_score, font = ("helvetica", "26"))#sauvergarder une partie en cours dans un fichier)
b1.grid( column =  0, row = 1)
               

texte = tk.Label(text= "Reprendre une partie")
texte.grid(column= 1, row = 2)
b1 = tk.Button(text = "Resume the game", command = "c", font = ("helvetica", "26"))#reprendre une partie enregistrée)
b1.grid( column =  1, row = 2)

texte = tk.Label(text= "se déplacer à droite")
texte.grid(column= 0, row = 1)
b1 = tk.Button(text = "Droite", command = déplacement_droite , font = ("helvetica", "26")) #boutton permettant le déplacement à droite
b1.grid( column =  0, row = 1)

texte = tk.Label(text= "se déplacer à gauche")
texte.grid(column= 0, row = 1)
b1 = tk.Button(text = "Gauche", command = déplacement_gauche , font = ("helvetica", "26")) #boutton permettant le déplacement à gauche
b1.grid( column =  0, row = 1)

texte = tk.Label(text= "se déplacer en haut")
texte.grid(column= 0, row = 1)
b1 = tk.Button(text = "Haut", command = déplacement_haut , font = ("helvetica", "26")) #boutton permettant le déplacement en haut
b1.grid( column =  0, row = 1)

texte = tk.Label(text= "se déplacer en bas")
texte.grid(column= 0, row = 1)
b1 = tk.Button(text = "Bas", command = déplacement_bas , font = ("helvetica", "26")) #boutton permettant le déplacement en bas 
b1.grid( column =  0, row = 1)

racine.mainloop()

