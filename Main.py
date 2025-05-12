from Database import db # importando classe Database
import customtkinter as ctk # importando biblioteca customtkinter

def limpar_entry_text_direita(descrição_direita, nome_direita): # limpa o text e o entry
    descrição_direita.delete("1.0", "end")
    nome_direita.delete(0, "end")

def atualizar_lista_tarefas(scroll_frame):  # para limpar e atualizar o scrollable
    for widget in scroll_frame.winfo_children():
        widget.destroy()

    tarefas = db.listar_tarefas()

    for id_, nome, descricao in tarefas:
        # Criando o layout de cada tarefa
        tarefa_frame = ctk.CTkFrame(scroll_frame,
                                    width=550,
                                    height=120)
        tarefa_frame.pack(pady=5, padx=10, anchor="w")
        tarefa_frame.grid_propagate(False)
        tarefa_frame.grid_columnconfigure(1, weight=1)
        tarefa_frame.grid_columnconfigure(0, weight=1)
        tarefa_frame.grid_columnconfigure(1, weight=0)

        # Nome da tarefa
        nome_label = ctk.CTkLabel(tarefa_frame,
                                  text=f" Nome: {nome}",
                                  font=("Calibri", 18, "bold"),
                                  wraplength=420,
                                  justify="left")
        nome_label.grid(row=0, column=0, sticky="w")

        # Descrição da tarefa
        descricao_label = ctk.CTkLabel(tarefa_frame,
                                       text=f" Descrição: {descricao}",
                                       font=("Calibri", 16),
                                       wraplength=550,
                                       justify="left")
        descricao_label.grid(row=1, column=0, sticky="w", pady=(5, 0), columnspan=2)

        # Adicionando um botão para marcar a tarefa como concluída
        concluir_btn = ctk.CTkButton(tarefa_frame,
                                        text="Concluir Tarefa",
                                        width=100,
                                        font=("Calibri", 16, "bold"))
        concluir_btn.grid(row=0, column=1, sticky="ne",padx=10, pady=10)

