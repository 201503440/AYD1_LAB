#from typing import final
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '201503440'
app.config['MYSQL_DB'] = 'ejemplo'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
    return '<h1>LABORATORIO 11 AYD1</h1>'

@app.route('/insertar', methods=['POST'])
def insert():
    contenido = request.json
    nombre = contenido['name']
    apellido = contenido['lastname']
    print(nombre, apellido)
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO persona(name, lastname) VALUES(%s, %s) ''', (nombre, apellido))
    mysql.connection.commit()
    cursor.close()
    return 'Objeto insertado correctamente...!!!'

@app.route('/getAll', methods=['GET'])
def personas():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM persona ''')
        rows = cursor.fetchall()
        return jsonify(rows)
    except Exception as e:
        print('Error: '+ e)
    finally:
        cursor.close()

app.run(host='0.0.0.0', debug=True)