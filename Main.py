from Database import db

def limpar_entry_text_direita(descrição_direita, nome_direita): # limpa o text e o entry
    descrição_direita.delete("1.0", "end")
    nome_direita.delete(0, "end")

