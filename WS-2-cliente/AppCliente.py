from flask import Flask, request, json
from flask import render_template


__author__ = 'Carlos Perez', 'Diana Camacho', 'Hillary Brenes'

app = Flask(__name__)

# ------------------------------------------------ MOSTRAR FORMULARIO --------------------------------------------------#
@app.route('/formulario')
def formulario():
    print("Si")
    return render_template('registro.html')

# ---------------------------------------------- MOSTRAR FORMULARIO LOGIN ----------------------------------------------#
@app.route('/login')
def login():
    print("Si")
    return render_template('login.html')

# ------------------------------------------ MOSTRAR HTML PARA CONSULTAS -----------------------------------------------#
@app.route('/consultas')
def consultas():
    return render_template('consultas.html')

# ---------------------------------------- MOSTRAR HTML PARA RESERVACIONES ---------------------------------------------#
@app.route('/reservar')
def reservar():
    return render_template('reservacion.html')

# ----------------------------------------------------- EJECUCIÓN ------------------------------------------------------#
if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
