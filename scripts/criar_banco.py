import sqlite3
import os

# Caminho para salvar o banco na pasta database/
CAMINHO_BANCO = os.path.join("database", "biblia.db")

def criar_estruturas():
    # Garante que a pasta database/ existe
    os.makedirs("database", exist_ok=True)

    # Conecta ou cria o arquivo do banco
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    print("🛠️ Criando tabelas no banco de dados...")

    # 1. Tabela de Livros
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ordem INTEGER NOT NULL,
        nome TEXT NOT NULL,
        abrev TEXT NOT NULL,
        testamento TEXT NOT NULL CHECK(testamento IN ('AT', 'NT'))
    );
    """)

    # 2. Tabela de Versículos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS versiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER NOT NULL,
        capitulo INTEGER NOT NULL,
        versiculo INTEGER NOT NULL,
        texto TEXT NOT NULL,
        FOREIGN KEY (livro_id) REFERENCES livros (id)
    );
    """)

    # 3. Tabela do Dicionário Strong
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dicionario_strong (
        codigo TEXT PRIMARY KEY, -- Ex: 'H7257' ou 'G26'
        idioma TEXT NOT NULL CHECK(idioma IN ('hebraico', 'aramaico', 'grego')),
        palavra_original TEXT NOT NULL,
        transliteracao TEXT NOT NULL,
        definicao TEXT NOT NULL
    );
    """)

    # 4. Tabela de Análise Palavra por Palavra (Originais + Morfologia)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS palavras_originais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        versiculo_id INTEGER NOT NULL,
        posicao INTEGER NOT NULL,
        palavra TEXT NOT NULL, -- Palavra no original
        strong_codigo TEXT,
        morfologia TEXT,
        FOREIGN KEY (versiculo_id) REFERENCES versiculos (id),
        FOREIGN KEY (strong_codigo) REFERENCES dicionario_strong (codigo)
    );
    """)

    conn.commit()
    conn.close()
    print(f"✨ Banco de dados criado com sucesso em: {CAMINHO_BANCO}")

if __name__ == "__main__":
    criar_estruturas()
    