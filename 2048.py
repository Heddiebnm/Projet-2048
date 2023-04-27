import tkinter as tk
import random


# Créer une fenêtre
racine = tk.Tk()
racine.title("2048")

# Créer une grille
grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# Dictionnaire de couleur 
dico_coleurs={'0':"#FFF2EE", '2':"#FFE1D6", '4':"#FFCFBE", '8': "#FFC0AA", '16': "#FFA789", '32': "#FF8D65", '64':"#FF7F53", '128': "#FE6936", '256': "#FF5318", '512': "#FF4200", '1024': "#D23600", '2048': "#B42E00"}

# Créer la grille
for i in range(4):
    for j in range(4):
        label = tk.Label(racine, text=grid[i][j], width=12, height=6, font=("Arial", 20, "bold"), bg="SlateGray1")
        label.grid(row=i, column=j, padx=5, pady=5)

# fonction permettant l'ajout d'une tuile
def add_tile():
    global grid
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2 if random.random() < 0.9 else 4 # ajout d'une de valeur 2 avec 9 fois plus de chance d'apparition que la 4

 # fonction permettant le lancement de la partie en ajoutant deux tuiles au départ
def start():
    add_tile()
    add_tile()
    update_affichage()
    maj_couleurs()


def update_affichage():
    for i in range(4):
        for j in range(4):
            label = racine.grid_slaves(row=i, column=j)[0]
            label["text"] = str(grid[i][j])


# fonction permettant de se déplacer vers la droite
def déplacement_droite():
    for i in range(4):
        # Fusion des tuiles identiques.
        for j in range(3, 0, -1):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j - 1]:
                grid[i][j] *= 2
                grid[i][j - 1] = 0
        # Déplacement des tuiles.
        for j in range(3, 0, -1):
            if grid[i][j] == 0:
                for k in range(j - 1, -1, -1):
                    if grid[i][k] != 0:
                        grid[i][j], grid[i][k] = grid[i][k], grid[i][j]
                        break
    add_tile()
    update_affichage()
    maj_couleurs()

# fonction permettant de se déplacer vers la gauche
def déplacement_gauche():
    for i in range(4):
        # Fusion des tuiles identiques.
        for j in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j + 1]:
                grid[i][j] *= 2
                grid[i][j + 1] = 0

        # Déplacement des tuiles.
        for j in range(3):
            if grid[i][j] == 0:
                for k in range(j + 1, 4):
                    if grid[i][k] != 0:
                        grid[i][j], grid[i][k] = grid[i][k], grid[i][j]
                        break
    add_tile()
    update_affichage()
    maj_couleurs()

# fonction permettant de se déplacer vers le haut
def déplacement_haut():
    for j in range(4):
        # Fusion des tuiles identiques.
        for i in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i + 1][j]:
                grid[i][j] *= 2
                grid[i + 1][j] = 0

            # Déplacement des tuiles.
        for i in range(3):
            if grid[i][j] == 0:
                for k in range(i + 1, 4):
                    if grid[k][j] != 0:
                        grid[i][j], grid[k][j] = grid[k][j], grid[i][j]
                        break
    add_tile()
    update_affichage()
    maj_couleurs()

# fonction permettant de se déplacer vers le bas
def déplacement_bas():
    for j in range(4):
        # Fusion des tuiles identiques.
        for i in range(3, 0, -1):
            if grid[i][j] != 0 and grid[i][j] == grid[i - 1][j]:
                grid[i][j] *= 2
                grid[i - 1][j] = 0
        # Déplacement des tuiles.
        for i in range(3, 0, -1):
            if grid[i][j] == 0:
                for k in range(i - 1, -1, -1):
                    if grid[k][j] != 0:
                        grid[i][j], grid[k][j] = grid[k][j], grid[i][j]
                        break
    add_tile()
    update_affichage()
    maj_couleurs()

def new_game():
    reset()

def reset(): # fonction permettant de réinitialiser la grille
    global grid
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # nouvelle grille
    start() # appelle de nouveau la fonction start pour replacer deux nouvelles tuiles

def save(): # fonction permettant de sauvegarder une partie
    partie_sauvegardé = open("partie_sauvegardé.txt", "w")
    partie_sauvegardé.write(str(grid)) #Fonctionne avec seulement un imput dans la fonction write, elle peut pas en detecter deux 
    partie_sauvegardé.close()

def load(): #Probleme avec le réaffichage de la grille, le chargement fonctionne corretement toutefois
    global grid
    chargement_partie = open('partie_sauvegardé.txt', 'r') #r = read, permet de lire le contenu du fichier
    li = chargement_partie.readline()
    grid = li

    update_affichage()
    maj_couleurs()    
    chargement_partie.close()

def partie_gagné():
    if i or j == 2048:
        message= "Tu as gagné"
        label_win = tk.Label(racine, text=message, font=("Arial", 18))
        label_win.pack()


def fin_de_la_partie():
    score = sum(sum(tile) for tile in grid) # Calculer le score en faisant la somme des valeurs dans la grille
    message = "Fin de la partie!\nScore : " + str(score)
    label_score = tk.Label(racine, text=message, font=("Arial", 18))
    label_score.pack()

def maj_couleurs(): # fonction pour les couleurs de chaque tuile
    for i in range(4):
        for j in range(4):
                label = racine.grid_slaves(row=i, column=j)[0]
                for q, r in dico_coleurs.items() :
                    if label["text"] == q:
                        label["bg"] = r
                
maj_couleurs()
start()



Button1 = tk.Button(racine, text="Droite", command=déplacement_droite, font=("helvetica", "20"), relief="groove")
Button1.grid(column=6, row=2)  # positionnement du bouton de déplacement vers la droite

Button2 = tk.Button(racine, text="Gauche", command=déplacement_gauche, font=("helvetica", "20"), relief="groove")
Button2.grid(column=4, row=2)  # positionnement du bouton de déplacement vers la gauche

Button3 = tk.Button(racine, text="Haut", command=déplacement_haut, font=("helvetica", "20"), relief="groove")
Button3.grid(column=5, row=1)  # positionnement du bouton de déplacement vers le haut

Button4 = tk.Button(racine, text="Bas", command=déplacement_bas, font=("helvetica", "20"),
                    relief="groove")  # création d'un widget
Button4.grid(column=5, row=3)  # positionnement du bouton dedéplacement vers le bas

Button5 = tk.Button(racine, text="Reset", command=reset, font=("helvetica", "20"),
                    relief="groove")  # création d'un widget
Button5.grid(column=4, row=0)  # positionnement du bouton reset

Button6 = tk.Button(racine, text="Save", command=save, font=("helvetica", "20"),
                    relief="groove")  # création d'un widget
Button6.grid(column=6, row=0)  # positionnement du bouton save

Button7 = tk.Button(racine, text="Exit", command=fin_de_la_partie, font=("helvetica", "20"),
                    relief="groove")  # création d'un widget
Button7.grid(column=5, row=4)  # positionnement du bouton exit



root=tk.Tk()

#HEIGHT = 320
#WIDTH = 320

#racine = tk.Tk() # Création de la fenêtre racine
#canvas = tk.Canvas(racine, bg="gray34", height=HEIGHT, width=WIDTH)
#canvas.grid()


# personnaliser l'interface graphique
root.title("Interface graphique 2048")
root.geometry("350x400") 
root.config(background='#808080')

button8 = tk.Button(root, text="Commencer une nouvelle partie", command=new_game, font=("helvetica", "20"),
                    relief="groove")  # création d'un widget
button8.grid(column=1, row=0)  # positionnement du bouton save

button9 = tk.Button(root, text="Charger une partie", command=load, font=("helvetica", "20"),
                    relief="groove")  # création d'un widget
button9.grid(column=1, row=1)  # positionnement du bouton save

button10 = tk.Button(root, text="Quitter la partie", command=exit, font=("helvetica", "20"),
                    relief="groove")  # création d'un widget
button10.grid(column=1, row=2)  # positionnement du bouton save


root.mainloop()
racine.mainloop()
