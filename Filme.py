import tkinter as tk
from tkinter import messagebox
import random


class SorteadorFilme:
    def __init__(self, root):

        self.filmes = []

        self.root = root
        self.root.title("Sorteador de Filmes")
        self.root.geometry("600x700")
        self.root.configure(bg="#3c3f41")

        self.label = tk.Label(root, text="Digite um filme", bg="#3c3f41", font=("Helvetica", 24, "bold"), fg="white")
        self.label.pack(ipady=50)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", lambda event=None: self.adicionar_string())

        self.adicionar_button = tk.Button(root, text="Adicionar filme", command=self.adicionar_string, width=20, height=2, bg="lightgreen")
        self.adicionar_button.pack(pady=20)

        self.sortear_button = tk.Button(root, text="Sortear", command=self.sortear_string, width=20, height=2, bg="#FFD700")
        self.sortear_button.pack()

        self.labelLista = tk.Label(root, text="Lista de Filmes", bg="#3c3f41", font=("Helvetica", 12, "bold"), fg="white")
        self.labelLista.pack(pady=(60, 0), ipady=0)

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.listbox.pack(pady=20)
        self.listbox.bind('<Enter>', self.iniciar_temporizador)
        self.listbox.bind('<Leave>', self.parar_temporizador)
        self.temporizador_id = None

        self.limpar = tk.Button(root, text="Limpar", command=self.limpar, width=20, height=2, bg="#FFFFFF")
        self.limpar.pack()

        self.selected_index = None
        self.listbox.bind('<Double-Button-1>', self.obter_selecionado)
        root.bind('<Double-Button-1>', self.remover_item)

    def obter_selecionado(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.selected_index = selected_index[0]
        else:
            self.selected_index = None

    def remover_item(self, event):
        index = self.listbox.curselection()
        if index:
            self.selected_index = index[0]
        else:
            self.selected_index = None

        if self.selected_index is not None:
            self.listbox.delete(self.selected_index)
            self.filmes.pop(self.selected_index)
            self.selected_index = None

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
        self.filmes = []

    def iniciar_temporizador(self, event):
        self.temporizador_id = self.root.after(1000, self.mostrar_caixa_dialogo)

    def parar_temporizador(self, event):
        if self.temporizador_id:
            self.root.after_cancel(self.temporizador_id)
            self.temporizador_id = None

    def mostrar_caixa_dialogo(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_item = self.listbox.get(selected_index)
            messagebox.showinfo("Filme Selecionado", f"Click duplo remove o filme: {selected_item}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SorteadorFilme(root)
    root.mainloop()
