import customtkinter as ctk # importando a biblioteca CustomTkinter

janela = ctk.CTk() # cria a janela
janela.title("Lista de Tarefas: To-Do-List") # dando título
janela.geometry("1000x600") # tamanho da janela
janela.maxsize(width=1000, height=600) # tamanho max da janela
janela.minsize(width=1000, height=600) # tamanho min da janela
janela._set_appearance_mode("Dark") # tema da aplicação

###################################

titulo_da_aplicação = ctk.CTkLabel(janela, text="Sistema de Lista de Tarefas: To-Do-List", font=("Calibri", 60, "bold"))
titulo_da_aplicação.grid(row = 0, column = 0, padx = 10, columnspan = 3) # cria o texto inicial

frame_direita = ctk.CTkFrame(janela, width=350, height=510)
frame_direita.grid(row = 1, column = 1, padx = 10) # criar espaço na direita

frame_baixo = ctk.CTkFrame(janela, width=600, height=510)
frame_baixo.grid(row = 1, column = 0, padx = 10) # cria espaço em baixo

###################################



###################################

janela.mainloop() # roda o app
