import sqlite3

# Caminho do banco (pode ser alterado se necessário)
NOME_BANCO = "lista_tarefas.db"

# Criar conexão e cursor de forma controlada
class Database:
    def __init__(self, nome_banco=NOME_BANCO):
        self.nome_banco = nome_banco
        self.conexão = None
        self.cursor = None
        self.conectar()

    def conectar(self):
        try:
            self.conexão = sqlite3.connect(self.nome_banco)
            self.cursor = self.conexão.cursor()
            print(f"[✓] Banco '{self.nome_banco}' conectado com sucesso.")
        except sqlite3.Error as e:
            print(f"[X] Erro ao conectar ao banco de dados: {e}")

    def criar_tabela(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_tarefa_db TEXT NOT NULL,
                    descrição_tarefa_db TEXT
                )
            ''')
            self.conexão.commit()
            print("[✓] Tabela 'tarefas' criada ou já existente.")
        except sqlite3.Error as e:
            print(f"[X] Erro ao criar tabela: {e}")

    def adicionar_tarefa(self, nome, descrição):
        try:
            self.cursor.execute(
                "INSERT INTO tarefas (nome_tarefa_db, descrição_tarefa_db) VALUES (?, ?)",
                (nome, descrição)
            )
            self.conexão.commit()
            print(f"[✓] Tarefa '{nome}' adicionada com sucesso.")
        except sqlite3.Error as e:
            print(f"[X] Erro ao adicionar tarefa: {e}")

    def fechar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexão:
            self.conexão.close()
            print("[✓] Conexão com o banco fechada.")

    def listar_tarefas(self):
        try:
            self.cursor.execute("SELECT * FROM tarefas")
            tarefas = self.cursor.fetchall()
            return tarefas
        except sqlite3.Error:
            return []


# Instância global (pode ser importada no restante do app)
db = Database()
