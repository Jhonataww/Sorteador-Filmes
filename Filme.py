import tkinter as tk
from tkinter import messagebox
import random


class SorteadorFilme:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorteador de Filmes")
        self.root.geometry("600x400")
        self.root.configure(bg="#3c3f41")
        self.filmes = []
        self.label = tk.Label(root, text="Digite um filme", bg="#3c3f41", font=("Arial", 12, "bold"), fg="white")
        self.label.pack(ipady=50)
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", lambda event=None: self.adicionar_string())
        self.adicionar_button = tk.Button(root, text="Adicionar filme", command=self.adicionar_string, width=20, height=2, bg="lightgreen")
        self.adicionar_button.pack(pady=20)
        self.sortear_button = tk.Button(root, text="Sortear", command=self.sortear_string, width=20, height=2, bg="#FFD700")
        self.sortear_button.pack()

    def adicionar_string(self):
        nova_string = self.entry.get()
        if nova_string:
            self.filmes.append(nova_string)
            messagebox.showinfo("Sucesso", "Filme adicionado com sucesso!")
            self.entry.delete(0, tk.END)

    def sortear_string(self):
        if not self.filmes:
            messagebox.showwarning("Aviso", "Não há Filmes para sortear.")
        else:
            string_sorteada = random.choice(self.filmes)
            messagebox.showinfo("Filme Sorteado", f"O filme sorteado é: {string_sorteada}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SorteadorFilme(root)
    root.mainloop()
