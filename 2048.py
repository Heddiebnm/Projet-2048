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