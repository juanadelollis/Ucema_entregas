from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

#1- Buscar todos los productos
"""
@app.get("/productos/")
def get_productos():
    return f"Estos son los productos {(productos)}"
"""
#2- Buscar los productos por número
"""
@app.get("/productos/<int:id>")
def get_id_productos(id):
    if id in productos: 
        producto = productos[id]
        return f"<p>Este es el producto {escape(id)}</p>"
    else:
        return f"No se encuentra el producto. Error 404"
"""
#3- Editar la información de los productos
"""
@app.route("/productos/nuevo", methods=("GET", "POST"))
def modificar_producto():
    if request.method == 'POST':
        valor_input = request.form.get("name").split(",")
        productos[valor_input[0]] = {"Producto": valor_input[1], "Stock": valor_input[2], "Precio unitario": valor_input[3]}
        print(valor_input)
        return redirect(url_for('success'))
    else:
      return render_template('nuevo_producto.html')
"""
#4- Eliminar la información de los productos
"""
@app.route("/productos", methods=("DELETE"))
def eliminar_productos(id):
    if id in productos:
        productos.del(productos(id))
"""

#APLICACION
#La información sobre los productos deben estar almacenados en un DataFrame con la siguiente estructura:
productos = {
    1: {"Producto": "shampoo solido", "Stock": "5", "Precio unitario": "300"},
    2: {"Producto": "crema de manos", "Stock": "6", "Precio unitario": "600"},
}

#En el root / de la aplicación devuelve un html con el siguiente estilo:
@app.get("/")
def home():
    return render_template("maqueta2.html")

#En la ruta para obtener la información de los productos devuelve un html con el DataFrame
@app.get("/productos/")
def get_productos():
    return render_template("productos.html")


#El la ruta para acceder a cada producto la api debe soportar la modificación del producto
@app.route("/productos/nuevo", methods=("GET", "POST"))
def modificar_producto():
    if request.method == 'POST':
        id_prod = request.form.get("id")
        nombre = request.form.get("name")
        stock = request.form.get("stock")
        precio = request.form.get("price")
        producto = [id_prod, nombre, stock, precio]
        productos[producto[0]] = {"Producto": producto[1], "Stock": producto[2], "Precio unitario": producto[3]}
        print(productos)
        return redirect(url_for('/productos'))
    else:
      return render_template('producto_nuevo.html')

