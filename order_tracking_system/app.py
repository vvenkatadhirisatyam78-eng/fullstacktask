from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vishnusai@456",
    database="order_tracking_system"
)

cursor = db.cursor()

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Insert Order
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        customer = request.form['customer']
        product = request.form['product']
        status = request.form['status']
        amount = request.form['amount']

        query = "INSERT INTO orders (customer_name, product_name, status, amount) VALUES (%s,%s,%s,%s)"
        values = (customer, product, status, amount)
        cursor.execute(query, values)
        db.commit()

        return redirect('/')

    return render_template('insert.html')

# Update Order
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        order_id = request.form['order_id']
        status = request.form['status']

        query = "UPDATE orders SET status=%s WHERE order_id=%s"
        values = (status, order_id)
        cursor.execute(query, values)
        db.commit()

        return redirect('/')

    return render_template('update.html')

# Report Page
@app.route('/report')
def report():
    cursor.execute("SELECT * FROM daily_order_report")
    report_data = cursor.fetchall()

    cursor.execute("SELECT * FROM order_log")
    logs_data = cursor.fetchall()

    return render_template('report.html', report=report_data, logs=logs_data)

if __name__ == '__main__':
    app.run(debug=True)