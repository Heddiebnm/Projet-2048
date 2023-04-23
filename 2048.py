import tkinter as tk
import random as rd


def choisir_tuiles_au_hasard():
    tuiles_au_hasard=[]
    for i in range (1):
        tuiles= [2,2,2,2,2,2,2,2,2,4]
        AP_tuiles = rd.randint(0,len(tuiles)-1)
        tuiles_au_hasard=tuiles_au_hasard+tuiles[AP_tuiles]
    return tuiles_au_hasard


  # Fonction pour déplacer les tuiles vers la droite.
def déplacement_droite():
    for i in range(4):
        for j in range(3, 0, -1):
            if grid[i][j] == 0:
                for k in range(j-1, -1, -1):
                    if grid[i][k] != 0:
                        grid[i][j], grid[i][k] = grid[i][k], grid[i][j]
                        break

        # Fusion des tuiles identiques.
        for j in range(3, 0, -1):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j-1]:
                grid[i][j] *= 2
                grid[i][j-1] = 0


# Fonction pour déplacer les tuiles vers la gauche.
def déplacement_gauche():
    for i in range(4):
                for j in range(3):
            if grid[i][j] == 0:
                for k in range(j+1, 4):
                    if grid[i][k] != 0:
                        grid[i][j], grid[i][k] = grid[i][k], grid[i][j]
                        break

        # Fusion des tuiles identiques.
        for j in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i][j+1] = 0



# Fonction pour déplacer les tuiles vers le haut.
def déplacement_haut():
    for j in range(4):
        for i in range(3):
            if grid[i][j] == 0:
                for k in range(i+1, 4):
                    if grid[k][j] != 0:
                        grid[i][j], grid[k][j] = grid[k][j], grid[i][j]
                        break

        # Fusion des tuiles identiques.
        for i in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i+1][j]:
                grid[i][j] *= 2
                grid[i+1][j] = 0


# Fonction pour déplacer les tuiles vers le bas.
def déplacement_bas():
    for j in range(4):
        for i in range(3, 0, -1):
            if grid[i][j] == 0:
                for k in range(i-1, -1, -1):
                    if grid[k][j] != 0:
                        grid[i][j], grid[k][j] = grid[k][j], grid[i][j]
                        break

        # Fusion des tuiles identiques.
        for i in range(3, 0, -1):
            if grid[i][j] != 0 and grid[i][j] == grid[i-1][j]:
                grid[i][j] *= 2
                grid[i-1][j] = 0
       



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

