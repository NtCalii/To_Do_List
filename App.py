import customtkinter as ctk # importando a biblioteca CustomTkinter
from Main import * # importando a classe Main.py
from Database import * # importando a classe Database.py

################################### janela criada

janela = ctk.CTk() # cria a janela
janela.title("Lista de Tarefas: To-Do-List") # dando título
janela.geometry("1000x600") # tamanho da janela
janela.maxsize(width=1000, height=600) # tamanho max da janela
janela.minsize(width=1000, height=600) # tamanho min da janela
janela._set_appearance_mode("Dark") # tema da aplicação

################################### janela inicial

titulo_da_aplicação = ctk.CTkLabel(janela, text="Sistema de Lista de Tarefas: To-Do-List", font=("Calibri", 60, "bold"))
titulo_da_aplicação.grid(row=0, column=0, padx=10, columnspan=3) # cria o texto inicial

frame_direita = ctk.CTkFrame(janela, width=350, height=510)
frame_direita.grid(row=1, column=1, padx=10, pady=10, sticky="nsew") # criar espaço na direita
frame_direita.grid_propagate(False)  # Isso evita que o frame mude de tamanho

frame_baixo = ctk.CTkFrame(janela, width=600, height=510)
frame_baixo.grid(row=1, column=0, padx=10, pady=10, sticky="nsew") # cria espaço em baixo
frame_baixo.grid_propagate(False)  # Isso evita que o frame mude de tamanho

################################### grid da direita

titulo_direita = ctk.CTkButton(
    frame_direita,
    text="Aperte Aqui!",
    font=("Calibri", 14, "bold"),
    command= criar_banco_dados)
titulo_direita.grid(row=0, column=0, pady=(10, 0)) # cria titulo da direita

titulo_entry_nome = ctk.CTkLabel(
    frame_direita,
    text="Nome da tarefa",
    font=("Calibri", 28, "bold"))
titulo_entry_nome.grid(row=1, column=0) # cria titulo da entry nome

entry_nome = ctk.CTkEntry(
    frame_direita,
    placeholder_text="Digite o nome da tarefa: ",
    width=200,
    height=35)
entry_nome.grid(row=2, column=0, pady=(5, 10), padx=90) # cria o nome da lista

titulo_text_descrição = ctk.CTkLabel(
    frame_direita,
    text="Descrição da sua tarefa",
    font=("Calibri", 28, "bold"))
titulo_text_descrição.grid(row=3, column=0) # cria titulo do text descrição

text_descrição = ctk.CTkTextbox(
    frame_direita,
    wrap="word")
text_descrição.grid(row =4, column=0, pady=(10, 10), padx=90) # cria a descrição da lista

btn_adicionar_tarefa = ctk.CTkButton(
    frame_direita,
    text="ADICIONAR NOVA TAREFA",
    width=200,
    height=50,
    font=("Calibri", 16, "bold"),
    command=lambda: limpar_entry_text_direita(text_descrição, entry_nome))
btn_adicionar_tarefa.grid(row =5, column=0, pady=35, padx=90) # botão de adicionar tarefa

################################### grid de baixo



################################### executar app

janela.mainloop() # roda o app
if conexão:
    cursor.close()
    conexão.close()
