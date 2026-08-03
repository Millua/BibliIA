import sqlite3
import os

CAMINHO_BANCO = os.path.join("database", "biblia.db")

def povoar_strong():
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    print("📖 Populando a tabela dicionario_strong...")

    # Limpa a tabela antes de inserir para evitar duplicados
    cursor.execute("DELETE FROM dicionario_strong;")

    # Lista com termos de exemplo do Dicionário Strong (Hebraico e Grego)
    dados_strong = [
        ("H7257", "hebraico", "רָבַץ", "rabats", "Deitar-se, reclinar-se, repousar"),
        ("H430", "hebraico", "אֱלֹהִים", "Elohim", "Deus, Juízes, Seres celestiais"),
        ("H7225", "hebraico", "רֵאשִׁית", "reshiyth", "Princípio, começo, primícias"),
        ("H1254", "hebraico", "בָּרָא", "bara", "Criar, fazer do nada"),
        ("G746", "grego", "ἀρχή", "arche", "Princípio, origem, soberania"),
        ("G3056", "grego", "λόγος", "logos", "Palavra, verbo, discurso, expressão divina"),
        ("G2316", "grego", "θεός", "theos", "Deus, divindade"),
        ("G26", "grego", "ἀγάπη", "agape", "Amor incondicional, benevolência")
    ]

    cursor.executemany("""
    INSERT INTO dicionario_strong (codigo, idioma, palavra_original, transliteracao, definicao)
    VALUES (?, ?, ?, ?, ?);
    """, dados_strong)

    conn.commit()
    conn.close()
    print("✨ Dicionário Strong populado com sucesso no banco 'biblia.db'!")

if __name__ == "__main__":
    povoar_strong()