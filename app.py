from flask import Flask, render_template, request, redirect, jsonify, url_for, session
from datetime import timedelta

app = Flask(__name__)

# Secret key and session settings
app.secret_key = 'bdc556f280795c3fbeeceec6c1371403e130cfef785cbd02ba648f3a10ff3c75'
app.permanent_session_lifetime = timedelta(seconds=3)

# Sample product data
products = [
    {"id": 1, "name": "Medicine A", "price": 10.00, "image": 'https://static.oxinis.com/healthmug/image/product/102338-2-1000.webp'},
    {"id": 2, "name": "Medicine B", "price": 15.00, "image": 'https://www.jeevandip.com/wp-content/uploads/2022/07/librium10-tab.png'},
    {"id": 3, "name": "Medicine C", "price": 20.00, "image": 'https://meds.myupchar.com/126487/18f7ef0ffd194851bcaf003816e63909.jpg'},
    {"id": 4, "name": "Medicine D", "price": 10.00, "image": 'https://static.oxinis.com/healthmug/image/product/102338-2-1000.webp'},
    {"id": 5, "name": "Medicine E", "price": 15.00, "image": 'https://www.jeevandip.com/wp-content/uploads/2022/07/librium10-tab.png'},
    {"id": 6, "name": "Medicine F", "price": 20.00, "image": 'https://meds.myupchar.com/126487/18f7ef0ffd194851bcaf003816e63909.jpg'},
    {"id": 7, "name": "Medicine G", "price": 10.00, "image": 'https://static.oxinis.com/healthmug/image/product/102338-2-1000.webp'},
    {"id": 8, "name": "Medicine H", "price": 15.00, "image": 'https://www.jeevandip.com/wp-content/uploads/2022/07/librium10-tab.png'},
    {"id": 9, "name": "Medicine I", "price": 20.00, "image": 'https://meds.myupchar.com/126487/18f7ef0ffd194851bcaf003816e63909.jpg'}
]

cart = []

# Redirect root to login
@app.route('/')
def index():
    return redirect(url_for('login'))

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg2 = ''
    if request.method == 'POST':
        email = request.form.get('login-email')
        password = request.form.get('login-password')
        if email == "abc@mail.com" and password == "abc123":
            session.permanent = True
            session['email'] = email
            return redirect(url_for('home'))
        else:
            msg2 = 'Invalid credentials'
    return render_template('login.html', msg2=msg2)

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phonenumber = request.form.get('phonenumber')
        address = request.form.get('address')
        password = request.form.get('password')
        # Normally you would insert these into a database here
        msg = 'Registration Successful!'
        return render_template('login.html', msg=msg)
    return render_template('Registration.html')

# Home Page
@app.route('/home')
def home():
    return render_template('home.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Forget Password Page
@app.route('/forget')
def forget():
    return render_template('forget_password.html')

# Chatbot Page
@app.route('/chat')
def chat():
    return render_template('chatbot.html')

# Pharmacy Product Page
@app.route('/pharm')
def pharmacy():
    return render_template('pharmacy.html', products=products)

# Add to Cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = int(request.form['product_id'])
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return jsonify({'message': 'Item added to cart'})

# View Cart
@app.route('/cart')
def view_cart():
    total_price = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)

# Remove from Cart
@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = int(request.form['product_id'])
    product = next((p for p in cart if p['id'] == product_id), None)
    if product:
        cart.remove(product)
    return jsonify({'message': 'Item removed from cart'})

# Run App
if __name__ == '__main__':
    app.run(debug=True)
