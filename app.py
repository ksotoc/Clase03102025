from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ventas'

conexion = MySQL(app) # Inicializar la conexion

# mysql -u root
# create database ventas
# exit
# mysql -u root ventas < copia_db_ventas.sql

@app.route("/")
def home():
    return "Hola mundo desde flask"

@app.route("/about")
def about():
    return "Ruta de informacion"

@app.route("/contacto")
def contacto():
    return "Ruta de contacto"

@app.route("/usuario/<nombre>")
def usuario(nombre):
    return f"Hola {nombre}, bienvenido"

@app.route("/suma/<int:a>/<int:b>")  #/suma/4/5
def suma(a, b):
    return f"La suma de {a} + {b} es {a+b}"

@app.route("/precio/<float:a>")
def precio(a):
    return f"Precio de {a}"

@app.route("/api/info")
def info():
    return {
        "app": "Flask",
        "version": "x.x",
        "autor": "Kevin"
    }
    
@app.route("/lista-clientes")
def lista_clientes():
    cursor = conexion.connection.cursor()  # c[0]
    sql = "SELECT id_cliente, nombre, email FROM clientes ORDER BY 1 asc"
    cursor.execute(sql) # Ejecutar consulta -> sql
    datos = cursor.fetchall()
    cursor.close()
    
    print("Lista Clientes", datos)
    
    return render_template("clientes.html", clientes=datos, title="Clientes Array")

@app.route("/clientes-lista")
def clientes_lista():
    cursor = conexion.connection.cursor(MySQLdb.cursors.DictCursor)  # c.columna
    sql = "SELECT id_cliente, nombre, email FROM clientes ORDER BY 1 asc"
    cursor.execute(sql) # Ejecutar consulta -> sql
    datos = cursor.fetchall()
    cursor.close()
    
    print("Lista Clientes (Diccionario)", datos)
    
    return render_template("clientes-json.html", clientes=datos, total=len(datos), title="Clientes json")

if __name__ == "__main__":
    app.run(debug=True)