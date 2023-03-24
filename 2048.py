import tkinter as tk

HEIGHT = 500
WIDTH = 500
largeur_case = WIDTH // 4
hauteur_case = HEIGHT // 4

racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)
canvas.grid()
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            color = "bisque2"
        else:
            color = "Peachpuff3"
        canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)

racine.title("2048")
racine.mainloop() # Lancement de la boucle principale

#boutons à finaliser

racine = tk.Tk
racine.title("2048")
texte = tk.Label(text= "Commencer à jouer")
text.grid(column= , row = )
b1 = tk.Button(text = "Play", command = #mettre 2 tuiles de manière aléatoire (2 ou 4) dans la grilles)
b1.grid( column =  , row = )
racine.mainloop()

import tkinter as tk
racine = tk.Tk
racine.title("2048")
texte = tk.Label(text= "Terminer la partie et voir le score")
text.grid(column= , row = )
b1 = tk.Button(text = "Exit", command = #finir la partie et afficher le score)
b1.grid( column =  , row = )
racine.mainloop() 

import tkinter as tk
racine = tk.Tk
racine.title("2048")
texte = tk.Label(text= "Sauvergarder la partie")
text.grid(column= , row = )
b1 = tk.Button(text = "Save", command = #sauvergarder une partie en cours dans un fichier)
b1.grid( column =  , row = )

import tkinter as tk
racine = tk.Tk
racine.title("2048")
texte = tk.Label(text= "Reprendre une partie")
text.grid(column= , row = )
b1 = tk.Button(text = "Resume the game", command = #reprendre une partie enregistrée)
b1.grid( column =  , row = )
