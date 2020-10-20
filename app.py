from flask import Flask
from Usuario import Usuario

misUsuario = []
misUsuario.append(Usuario(1,"usuario1","123"))
misUsuario.append(Usuario(2,"usuario2","123"))


app = Flask(__name__)

@app.route("/login/:user", methods=["POST"])



@app.route("/")
def index():
    nombre = misUsuario[0].usuario
    return "<h1>" + nombre + "</h1>"


if __name__ == "__main__":
    app.run(threaded=True, port=5000,debug=True)