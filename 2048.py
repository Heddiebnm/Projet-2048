import tkinter as tk
import random 

# Créer une fenêtre
racine = tk.Tk()
racine.title("2048")

# Créer une grille
grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(4):
    for j in range(4):
        label = tk.Label(racine, text=grid[i][j], width=12, height=6, font=("Arial", 20, "bold"), bg="gray80")
        label.grid(row=i, column=j, padx=5, pady=5)


def add_tile():
    global grid
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2 if random.random() < 0.9 else 4




def start():
    add_tile()
    add_tile()
    for i in range(4):
        for j in range(4):
            label = racine.grid_slaves(row=i, column=j)[0]
            label["text"] =str(grid[i][j])
    

def déplacement_droite():
    for i in range(4):
        # Fusion des tuiles identiques.
        for j in range(3, 0, -1):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j-1]:
                grid[i][j] *= 2
                grid[i][j-1] = 0
        # Déplacement des tuiles.
        for j in range(3, 0, -1):
            if grid[i][j] == 0:
                for k in range(j-1, -1, -1):
                    if grid[i][k] != 0:
                        grid[i][j], grid[i][k] = grid[i][k], grid[i][j]
                        break
        
        

def déplacement_gauche():
    for i in range(4):
        # Fusion des tuiles identiques.
        for j in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i][j+1] = 0

        # Déplacement des tuiles.
        for j in range(3):
            if grid[i][j] == 0:
                for k in range(j+1, 4):
                    if grid[i][k] != 0:
                        grid[i][j], grid[i][k] = grid[i][k], grid[i][j]
                        break

def déplacement_haut():
    for j in range(4):
        # Fusion des tuiles identiques.
        for i in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i+1][j]:
                grid[i][j] *= 2
                grid[i+1][j] = 0
                
            # Déplacement des tuiles.
        for i in range(3):
            if grid[i][j] == 0:
                for k in range(i+1, 4):
                    if grid[k][j] != 0:
                        grid[i][j], grid[k][j] = grid[k][j], grid[i][j]
                        break




def déplacement_bas():
    for j in range(4):
        # Fusion des tuiles identiques.
        for i in range(3, 0, -1):
            if grid[i][j] != 0 and grid[i][j] == grid[i-1][j]:
                grid[i][j] *= 2
                grid[i-1][j] = 0
    # Déplacement des tuiles.
    for i in range(3, 0, -1):
            if grid[i][j] == 0:
                for k in range(i-1, -1, -1):
                    if grid[k][j] != 0:
                        grid[i][j], grid[k][j] = grid[k][j], grid[i][j]
                        break


def reset():
    pass

def save():
    pass

def end():
    pass

start()

Button1 = tk.Button(racine, text="Droite", command= déplacement_droite , font=("helvetica", "20"), relief="groove")
Button1.grid(column=6, row=2) # positionnement du bouton de déplacement vers la droite

Button2 = tk.Button(racine, text="Gauche", command= déplacement_gauche , font=("helvetica", "20"), relief="groove")
Button2.grid(column=4, row=2) # positionnement du bouton de déplacement vers la gauche

Button3 = tk.Button(racine, text="Haut", command= déplacement_haut , font=("helvetica", "20"), relief="groove")
Button3.grid(column=5, row=1) # positionnement du bouton de déplacement vers le haut 

Button4 = tk.Button(racine, text="Bas", command = déplacement_bas , font = ("helvetica", "20"), relief = "groove") # création d'un widget
Button4.grid(column=5, row=3) # positionnement du bouton dedéplacement vers le bas 

Button5 = tk.Button(racine, text="Reset", command = reset , font = ("helvetica", "20"), relief = "groove") # création d'un widget
Button5.grid(column=4, row=0) # positionnement du bouton reset

Button6 = tk.Button(racine, text="Save", command = save , font = ("helvetica", "20"), relief = "groove") # création d'un widget
Button6.grid(column=6, row=0) # positionnement du bouton save

button7 = tk.Button(racine, text="Start", command = start , font = ("helvetica", "20"), relief = "groove") # création d'un widget
button7.grid(column=4, row=4) # positionnement du bouton start

Button8 = tk.Button(racine, text="End", command = end , font = ("helvetica", "20"), relief = "groove") # création d'un widget
Button8.grid(column=6, row=4) # positionnement du bouton end


racine.mainloop() # permet d'afficher la fenêtre 
