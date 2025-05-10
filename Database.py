import sqlite3 # importando banco de dados

conexão = None # criando variável de conexão
cursor = None # criando variável de cursor

def criar_banco_dados(nome_banco = "lista_tarefas.db"): # função para criar o banco
    global conexão
    global cursor
    try:
        conexão = sqlite3.connect(nome_banco) # conecta e atribui o objeto de conexão
        cursor = conexão.cursor()           # cria o cursor usando o objeto de conexão
        print(f"Banco '{nome_banco}' criado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")

