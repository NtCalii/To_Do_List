def limpar_entry_text_direita(descrição_direita, nome_direita):
    descrição_direita.delete("1.0", "end")
    nome_direita.delete(0, "end") # limpa o text e o entry


