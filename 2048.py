import tkinter as tk

gamebox=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

HEIGHT = 320
WIDTH = 320


racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="gray34", height=HEIGHT, width=WIDTH)
canvas.grid()

def dessiner_lignes():
    #lignes horizontales
    canvas.create_line(1, 3, 320, 3,fill='black', width=10)
    canvas.create_line(1, 80, 320, 80,fill='black', width=3)
    canvas.create_line(1, 160, 320, 160,fill='black', width=3)
    canvas.create_line(1, 240, 320, 240,fill='black', width=3)
    canvas.create_line(1, 320, 320, 320, fill='black', width=10)
 
    #lignes verticales
    canvas.create_line(3, 1, 3, 320,fill='black', width=10)
    canvas.create_line(80, 1, 80, 320,fill='black', width=3)
    canvas.create_line(160, 1, 160, 320,fill='black', width=3)
    canvas.create_line(240, 1, 240, 320,fill='black', width=3)
    canvas.create_line(320, 1, 320, 325, fill='black', width=10)

def dessiner_chiffres(tab):
    k=0
    l=0
    for i in range(0,4):
        if i==0:
            k+=40
        else:
            k+=80
        l=0
        for j in range(0,4):
            if j==0:
                l+=40
            else:
                l+=80
            if tab[i][j]!=0:
                canvas.create_text(l, k, text=str(tab[i][j]), font=("arial",30,"bold"))

def actualiser_fenetre(tab):
    canvas.delete(ALL)
    dessiner_lignes()
    dessiner_chiffres(tab)
 
console_affiche(gamebox)
 
actualiser_fenetre(gamebox) # check
 
canvas.focus_set()
canvas.bind('<Key>', gestion_clavier)
canvas.pack(padx=5, pady=5)
        
racine.title("2048")
racine.mainloop() # Lancement de la boucle principale