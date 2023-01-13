import tkinter as tk
import tkinter.messagebox as messagebox

fenetre = tk.Tk()
fenetre.resizable(False,False)
fenetre.title("Puissance 4")


couleur = "red"

def joueurClique(bouton):
    global couleur
    if bouton["bg"] == 'white':
         # mettre à jour la grille de jeu et le bouton et changer le signe
        if couleur == 'red':
            bouton.config(bg='red')
            verification()
            couleur = 'yellow'
        else:
            bouton.config(bg='yellow')
            verification()
            couleur = 'red'
    else:
        messagebox.showinfo("Case vide" , "La case n'est pas vide.")
    

def verification():
    #ligne
    for i in range(6):
        c = 0
        adjacent = 1
        couleur_precedente = ""
        for j in range(7):
            bouton = fenetre.grid_slaves(row=i,column=j)
            couleur_actuelle = bouton[0].cget("bg")
            if couleur_actuelle == couleur:
                c = c + 1
                if couleur_actuelle == couleur_precedente:
                    adjacent += 1
                else:
                    adjacent = 1
            if adjacent >= 4:
                messagebox.showinfo("Gagné", "Le joueur avec la couleur " + couleur + " a gagné!")
                exit()
            couleur_precedente = couleur_actuelle
    #colonne
    for i in range(7):
        c = 0
        adjacent = 1
        couleur_precedente = ""
        for j in range(6):
            bouton = fenetre.grid_slaves(row=j,column=i)
            couleur_actuelle = bouton[0].cget("bg")
            if couleur_actuelle == couleur:
                c = c + 1
                if couleur_actuelle == couleur_precedente:
                    adjacent += 1
                else:
                    adjacent = 1
            if adjacent >= 4:
                messagebox.showinfo("Gagné", "Le joueur avec la couleur " + couleur + " a gagné!")
                exit()
            couleur_precedente = couleur_actuelle
      #diagonale
 
            
def egalite():
    pass

for i in range(6):
    for j in range(7):
        bouton = tk.Button(fenetre,bg='white' ,font = ('Arial', 20), width=5, height=3)
        bouton.grid(row = i , column = j)
        bouton.config(command=lambda bouton=bouton: joueurClique(bouton))
        
        
fenetre.mainloop()   