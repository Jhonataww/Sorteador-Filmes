import tkinter as tk
from tkinter import messagebox
import random


class SorteadorFilme:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorteador de Filmes")
        self.root.geometry("600x700")
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

        self.labelLista = tk.Label(root, text="Lista de Filmes", bg="#3c3f41", font=("Arial", 8, "bold"), fg="white")
        self.labelLista.pack(pady=(60, 0), ipady=0)

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.listbox.pack(pady=20)

        self.limpar = tk.Button(root, text="Limpar", command=self.limpar, width=20, height=2, bg="#FFD700")
        self.limpar.pack()

        # Associa o evento de seleção e a tecla Delete ao Listbox
        self.listbox.bind('<<ListboxSelect>>', self.obter_selecionado)
        root.bind('<Delete>', self.remover_item)

    def obter_selecionado(self, event):
        # Obtém o índice do item selecionado
        selected_index = self.listbox.curselection()
        if selected_index:
            self.selected_index = selected_index[0]
        else:
            self.selected_index = None

    def remover_item(self, event):
        # Certifica-se de que um item foi realmente selecionado
        if self.selected_index is not None:
            # Remove o item selecionado pelo índice
            self.listbox.delete(self.selected_index)

    def adicionar_string(self):
        nova_string = self.entry.get()
        if nova_string:
            self.filmes.append(nova_string)
            messagebox.showinfo("Sucesso", "Filme adicionado com sucesso!")
            self.listbox.insert(tk.END, nova_string)
            self.entry.delete(0, tk.END)

    def sortear_string(self):
        if not self.filmes:
            messagebox.showwarning("Aviso", "Não há Filmes para sortear.")
        else:
            string_sorteada = random.choice(self.filmes)
            messagebox.showinfo("Filme Sorteado", f"O filme sorteado é: {string_sorteada}")

    def limpar(self):
        self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SorteadorFilme(root)
    root.mainloop()
