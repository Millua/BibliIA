import sqlite3
import os

CAMINHO_BANCO = os.path.join("database", "biblia.db")

VERSICULOS = [
    # (livro_id, capitulo, versiculo, texto, versao)
    (1, 1, 1, "No princípio criou Deus os céus e a terra.", "NVI"),
    (1, 1, 2, "A terra era sem forma e vazia; havia trevas sobre a face do abismo, e o Espírito de Deus se movia sobre as águas.", "NVI"),
    (27, 5, 5, "De repente apareceram dedos de mão humana que escreviam no reboco da parede do palácio real, em frente do castiçal; e o rei viu a parte da mão que escrevia.", "NVI"),
    (43, 1, 1, "No princípio era aquele que é a Palavra. Ele estava com Deus, e ele era Deus.", "NVI"),
    (43, 1, 14, "A Palavra se fez carne e habitou entre nós. Vimos a sua glória, glória como do Filho único do Pai, cheio de graça e de verdade.", "NVI")
]

def povoar_versiculos():
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    print("📜 Populando a tabela de versículos de teste...")

    cursor.execute("DELETE FROM versiculos;")

    # Descobre o nome real das colunas na tabela
    cursor.execute("PRAGMA table_info(versiculos);")
    colunas_banco = [coluna[1] for coluna in cursor.fetchall() if coluna[1] != 'id']

    # Mapeia os dados de acordo com o que existe no banco
    dados_para_inserir = []
    for item in VERSICULOS:
        # Se o banco tem 4 colunas (sem versao) ou 5 colunas (com versao)
        if len(colunas_banco) == 4:
            dados_para_inserir.append((item[0], item[1], item[2], item[3]))
        else:
            dados_para_inserir.append(item)

    colunas_str = ", ".join(colunas_banco)
    placeholders = ", ".join(["?"] * len(colunas_banco))

    query = f"INSERT INTO versiculos ({colunas_str}) VALUES ({placeholders});"
    cursor.executemany(query, dados_para_inserir)

    conn.commit()
    conn.close()
    print("✨ Versículos inseridos com sucesso!")

if __name__ == "__main__":
    povoar_versiculos()