from flask import Flask, render_template 
app = Flask(__name__)
# rutas
@app.route('/')
def raiz():
    titulo = "pagina inicio"
    return '<h5 class="card-title">Bienvenido a nosotros</h5>'

# bloque de prueba
if __name__ == "__main__":
    app.run(debug=True)