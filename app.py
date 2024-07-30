from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registroMedico')
def registroMedico():
    return render_template('registroMedico.html')

@app.route('/registroPaciente')
def registroPaciente():
    return render_template('registroPaciente.html')

@app.route('/directorioM')
def directorioM():
    return render_template('directorioM.html')

@app.route('/perfilMed')
def perfilMed():
    return render_template('perfilMed.html')

@app.route('/registrOp')
def registrOp():
    return render_template('registrOp.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/respuestas')
def respuestas():
    return render_template('respuestas.html')

if __name__ == '__main__':
    app.run(debug=True)
