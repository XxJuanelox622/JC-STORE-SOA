from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# =========================
# DATOS DE PRUEBA
# =========================

users = [
    {"username": "admin", "password": "1234"},
    {"username": "juan", "password": "1234"}
]

products = [
    {
        "id": 1,
        "name": "Laptop Gamer ASUS",
        "price": 25000,
        "image": "static/img/laptop_gamer_asus.jpg"
    },
    {
        "id": 2,
        "name": "PC Gamer RTX",
        "price": 32000,
        "image": "static/img/pc_gamer_rtx.jpg"
    },
    {
        "id": 3,
        "name": "Monitor Curvo Samsung",
        "price": 8500,
        "image": "static/img/monitor_curvo.jpg"
    },
    {
        "id": 4,
        "name": "Teclado Mecánico RGB",
        "price": 1800,
        "image": "static/img/teclado_mecanico_rgb.jpg"
    }
]

orders = []

# =========================
# RUTAS PRINCIPALES
# =========================

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products-page')
def products_page():
    return render_template('products.html', products=products)


@app.route('/login-page')
def login_page():
    return render_template('login.html')


@app.route('/orders-page')
def orders_page():
    return render_template('order.html')


# =========================
# USER SERVICE
# =========================

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


@app.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "No se enviaron datos"
        }), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({
            "message": "Faltan campos"
        }), 400

    for user in users:

        if user['username'] == username and user['password'] == password:

            return jsonify({
                "message": "Login exitoso",
                "user": username
            }), 200

    return jsonify({
        "message": "Usuario o contraseña incorrectos"
    }), 401


# =========================
# PRODUCT SERVICE
# =========================

@app.route('/products', methods=['GET'])
def get_products():

    return jsonify({
        "products": products
    }), 200


# =========================
# ORDER SERVICE
# =========================

@app.route('/orders', methods=['GET'])
def get_orders():

    return jsonify({
        "orders": orders
    }), 200


@app.route('/orders', methods=['POST'])
def create_order():

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "No se enviaron datos"
        }), 400

    orders.append(data)

    return jsonify({
        "message": "Pedido creado correctamente",
        "order": data
    }), 201


# =========================
# MAIN
# =========================

if __name__ == '__main__':
    app.run(debug=True)