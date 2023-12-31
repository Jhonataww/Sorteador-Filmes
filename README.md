# Sorteador-Filmes

Sorteador de Filmes com uma interface gráfica simples usando Tkinter, uma biblioteca GUI para Python. O programa permite que o usuário adicione filmes a uma lista e sorteie um filme aleatório dessa lista.

**Resumo:**

- **Tecnologias:**
  - **Linguagem de Programação:** Python
  - **Biblioteca GUI:** Tkinter
  - **Empacotamento (opcional):** PyInstaller

- **Funcionalidades:**
  - Interface gráfica usando Tkinter.
  - Adição de filmes à lista.
  - Sorteio aleatório de filmes da lista.
  - Mensagens de feedback usando `messagebox` do Tkinter.

- **Componentes Principais:**
  - `tk.Tk()`: Janela principal.
  - `tk.Label`, `tk.Entry`, `tk.Button`: Componentes de interface gráfica.
  - Listagem e manipulação de filmes em uma lista Python.
  - Uso de funções para adicionar filmes, sortear filmes e lidar com interações do usuário.

- **Empacotamento (Opcional):**
  - Utilizamos o PyInstaller para criar um executável standalone do programa para Windows.

Esse projeto serviu como uma introdução prática à criação de interfaces gráficas simples em Python usando a biblioteca Tkinter, além de abordar conceitos como manipulação de listas e interações do usuário. O PyInstaller foi opcionalmente utilizado para empacotar o programa como um executável único para facilitar a distribuição.


**Para buildar e criar um .exe do projeto.**


Para criar um executável de um programa Tkinter para Windows, você pode usar uma ferramenta de empacotamento como o PyInstaller ou o cx_Freeze. Vou fornecer instruções básicas para o PyInstaller, que é amplamente utilizado.

1. **Instalar o PyInstaller:**
   Abra um terminal e execute o seguinte comando para instalar o PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. **Criar o Executável:**
   No mesmo terminal, navegue até o diretório onde o seu script Python está localizado e execute o seguinte comando para criar o executável:

   ```bash
   pyinstaller --onefile Filme.py
   ```

3. **Executar o Executável:**
   Vá para o diretório `dist` e execute o executável recém-criado para testar se o programa funciona corretamente.


Certifique-se de incluir todas as bibliotecas e recursos adicionais que seu programa possa precisar no diretório do script principal para garantir que o PyInstaller possa encontrá-los e incluí-los no executável.