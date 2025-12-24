import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS inscritos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    equipe TEXT NOT NULL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin_sessions (
    token TEXT PRIMARY KEY
)
""")


con.commit()
con.close()

print("Banco criado com sucesso!")
