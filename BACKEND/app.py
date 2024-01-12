from flask import Flask, render_template 
app = Flask(__name__)
# rutas
@app.route('/')
def raiz():
    titulo = "pagina inicio"
    return '<h5 class="card-title">Bienvenido a nosotros</h5>'

# ruta para nosotros
@app.route('/nosotros')
def nosotros():
    titulo = "nosotros"
    return render_template('nosotros.html', titulo=titulo)

# bloque de prueba
if __name__ == "__main__":
    app.run(debug=True)