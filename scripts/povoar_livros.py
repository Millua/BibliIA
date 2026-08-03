import sqlite3
import os

CAMINHO_BANCO = os.path.join("database", "biblia.db")

LIVROS = [
    # Antigo Testamento
    (1, "Gênesis", "Gn", "AT"), (2, "Êxodo", "Êx", "AT"), (3, "Levítico", "Lv", "AT"),
    (4, "Números", "Nm", "AT"), (5, "Deuteronômio", "Dt", "AT"), (6, "Josué", "Js", "AT"),
    (7, "Juízes", "Jz", "AT"), (8, "Rute", "Rt", "AT"), (9, "1 Samuel", "1Sm", "AT"),
    (10, "2 Samuel", "2Sm", "AT"), (11, "1 Reis", "1Rs", "AT"), (12, "2 Reis", "2Rs", "AT"),
    (13, "1 Crônicas", "1Cr", "AT"), (14, "2 Crônicas", "2Cr", "AT"), (15, "Esdras", "Esd", "AT"),
    (16, "Neemias", "Ne", "AT"), (17, "Ester", "Et", "AT"), (18, "Jó", "Jó", "AT"),
    (19, "Salmos", "Sl", "AT"), (20, "Provérbios", "Pv", "AT"), (21, "Eclesiastes", "Ec", "AT"),
    (22, "Cânticos", "Ct", "AT"), (23, "Isaías", "Is", "AT"), (24, "Jeremias", "Jr", "AT"),
    (25, "Lamentações", "Lm", "AT"), (26, "Ezequiel", "Ez", "AT"), (27, "Daniel", "Dn", "AT"),
    (28, "Oséias", "Os", "AT"), (29, "Joel", "Jl", "AT"), (30, "Amós", "Am", "AT"),
    (31, "Obadias", "Ob", "AT"), (32, "Jonas", "Jn", "AT"), (33, "Miquéias", "Mq", "AT"),
    (34, "Naum", "Na", "AT"), (35, "Habacuque", "Hc", "AT"), (36, "Sofonias", "Sf", "AT"),
    (37, "Ageu", "Ag", "AT"), (38, "Zacarias", "Zc", "AT"), (39, "Malaquias", "Ml", "AT"),
    # Novo Testamento
    (40, "Mateus", "Mt", "NT"), (41, "Marcos", "Mc", "NT"), (42, "Lucas", "Lc", "NT"),
    (43, "João", "Jo", "NT"), (44, "Atos", "At", "NT"), (45, "Romanos", "Rm", "NT"),
    (46, "1 Coríntios", "1Co", "NT"), (47, "2 Coríntios", "2Co", "NT"), (48, "Gálatas", "Gl", "NT"),
    (49, "Efésios", "Ef", "NT"), (50, "Filipenses", "Fp", "NT"), (51, "Colossenses", "Cl", "NT"),
    (52, "1 Tessalonicenses", "1Ts", "NT"), (53, "2 Tessalonicenses", "2Ts", "NT"),
    (54, "1 Timóteo", "1Tm", "NT"), (55, "2 Timóteo", "2Tm", "NT"), (56, "Tito", "Tt", "NT"),
    (57, "Filemom", "Fm", "NT"), (58, "Hebreus", "Hb", "NT"), (59, "Tiago", "Tg", "NT"),
    (60, "1 Pedro", "1Pe", "NT"), (61, "2 Pedro", "2Pe", "NT"), (62, "1 João", "1Jo", "NT"),
    (63, "2 João", "2Jo", "NT"), (64, "3 João", "3Jo", "NT"), (65, "Judas", "Jd", "NT"),
    (66, "Apocalipse", "Ap", "NT")
]

def povoar():
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    print("📚 Inserindo os 66 livros da Bíblia...")
    
    # Limpa a tabela antes de inserir para evitar duplicados se rodar de novo
    cursor.execute("DELETE FROM livros;")
    
    cursor.executemany("""
    INSERT INTO livros (ordem, nome, abrev, testamento)
    VALUES (?, ?, ?, ?);
    """, LIVROS)

    conn.commit()
    conn.close()
    print("✨ Todos os 66 livros foram cadastrados com sucesso!")

if __name__ == "__main__":
    povoar()