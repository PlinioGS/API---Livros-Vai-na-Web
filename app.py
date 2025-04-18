# source venv/Scripts/activate: para ativar o ambiente virtual
# pip install flask: pra instalar o Flask
# deactivate: desativar o ambiente virtual

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
import sqlite3


def init_db():
    # sqlite3 crie o arquivo darabase.db e se conecte com a váriavel conn (connection).
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
                CREATE TABLE IF NOT EXISTS LIVROS(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     titulo TEXT NOT NULL,
                     categoria TEXT NOT NULL,
                     autor TEXT NOT NULL,
                     imagem_url TEXT NOT NULL,
                     UNIQUE(titulo, autor, imagem_url)
                     )
        """)

init_db()

@app.route("/")
def home():
    return "<h1>Olá Vai na Web!! Bem-vindos a nossa API!</h1>"

@app.route("/doar", methods =["POST"])
def doar():

    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados.get("imagem_url")

    if not titulo or not categoria or not autor or not imagem_url:
        return jsonify({"erro":"Todos os campos são obrigatórios"}), 400

    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
        INSERT INTO LIVROS (titulo,categoria,autor,imagem_url)
        VALUES ("{titulo}", "{categoria}", "{autor}", "{imagem_url}")
""")
        
    conn.commit()
    return jsonify({"mensagem":"Livro cadastrado com sucesso"}), 201

@app.route("/livros", methods=["GET"])
def listar_livros():

    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        livros_formatados = []

        for item in livros:
            dicionario_livros={
                "id":item[0],
                "titulo":item[1],
                "categoria":item[2],
                "autor":item[3],
                "imagem_url":item[4]
        }
            livros_formatados.append(dicionario_livros)

    return jsonify(livros_formatados), 200


if __name__ == "__main__":
    app.run(debug=True)