import tkinter as tk
import random as rd

gamebox=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
tuiles= [2,2,2,2,2,2,2,2,2,4]


HEIGHT = 320
WIDTH = 320
score = 0

def choisir_tuiles_au_hasard():
    tuiles_au_hasard=[]
    for i in range (1):
        tuiles= [2,2,2,2,2,2,2,2,2,4]
        AP_tuiles = rd.randint(0,len(tuiles)-1)
        tuiles_au_hasard=tuiles_au_hasard+tuiles[AP_tuiles]
    return tuiles_au_hasard

a = choisir_tuiles_au_hasard()



def déplacement_droite():

def déplacement_gauche():

def déplacement_haut():

def déplacement_bas():



def sauvergarder_score():
    mon_fichier = open("fichier.txt", "w")
    mon_fichier.write("user01 :", score)
    mon_fichier.close()
   
def play():
    
    

racine = tk.Tk() # Création de la fenêtre racinejjjjjjjj
canvas = tk.Canvas(racine, bg="PaleGreen1", height=HEIGHT, width=WIDTH)
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