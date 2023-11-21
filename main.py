import tkinter as tk
from tkinter import messagebox
import random

class Demineur:
    def __init__(self, master, width, height, mines):
        self.master = master
        self.width = width
        self.height = height
        self.mines = mines
        self.buttons = []

        self.create_game_board()
        self.place_mines()

    def create_game_board(self):
        for row in range(self.height):
            button_row = []
            for col in range(self.width):
                button = tk.Button(self.master, width=2, height=1, command=lambda r=row, c=col: self.click(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def place_mines(self):
        mine_locations = random.sample(range(self.width * self.height), self.mines)
        for mine_location in mine_locations:
            row = mine_location // self.width
            col = mine_location % self.width
            self.buttons[row][col].mine = True

    def click(self, row, col):
        button = self.buttons[row][col]

        if button.mine:
            button.configure(text='X', state=tk.DISABLED)
            self.game_over()
        else:
            mines_nearby = sum(1 for r in range(max(0, row - 1), min(row + 2, self.height))
                              for c in range(max(0, col - 1), min(col + 2, self.width))
                              if self.buttons[r][c].mine)

            button.configure(text=str(mines_nearby), state=tk.DISABLED)

            if mines_nearby == 0:
                for r in range(max(0, row - 1), min(row + 2, self.height)):
                    for c in range(max(0, col - 1), min(col + 2, self.width)):
                        if self.buttons[r][c]['state'] == tk.NORMAL:
                            self.click(r, c)

    def game_over(self):
        for row in range(self.height):
            for col in range(self.width):
                self.buttons[row][col].configure(state=tk.DISABLED)
        messagebox.showinfo("Game Over", "Vous avez touché une mine !")

class InterfaceGraphique:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu")

        self.label_bienvenue = tk.Label(master, text="Bienvenue dans le jeu !", font=("Helvetica", 16))
        self.label_bienvenue.pack(pady=20)

        self.bouton_jouer = tk.Button(master, text="Jouer", command=self.commencer_jeu)
        self.bouton_jouer.pack(pady=10)

        self.bouton_parametres = tk.Button(master, text="Paramètres", command=self.ouvrir_parametres)
        self.bouton_parametres.pack(pady=10)

        self.bouton_quitter = tk.Button(master, text="Quitter", command=self.quitter)
        self.bouton_quitter.pack(pady=10)

    def commencer_jeu(self):
        self.master.destroy()
        jeu_root = tk.Tk()
        jeu_demineur = Demineur(jeu_root, rows, cols, mines)
        jeu_root.mainloop()

    def ouvrir_parametres(self):
        messagebox.showinfo("Paramètres", "Ouverture des paramètres...")

    def quitter(self):
        self.master.destroy()

# Demander à l'utilisateur la taille du tableau et le nombre de mines
rows = int(input("Entrez le nombre de lignes: "))
cols = int(input("Entrez le nombre de colonnes: "))
mines = int(input("Entrez le nombre de mines: "))

# Créer la fenêtre principale
root = tk.Tk()
interface = InterfaceGraphique(root)

# Lancer la boucle principale
root.mainloop()
