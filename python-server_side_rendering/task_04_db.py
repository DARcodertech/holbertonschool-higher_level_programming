from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def read_json_products(path):
    with open(path) as f:
        return json.load(f)

def read_csv_products(path):
    products = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

def read_sql_products(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products = []

    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, 'products.json')
    csv_path = os.path.join(base_dir, 'products.csv')
    db_path = os.path.join(base_dir, 'products.db')

    try:
        if source == 'json':
            products = read_json_products(json_path)
        elif source == 'csv':
            products = read_csv_products(csv_path)
        elif source == 'sql':
            products = read_sql_products(db_path)
        else:
            error = "Wrong source. Use 'json', 'csv', or 'sql'."
            products = []
    except Exception as e:
        error = f"Error reading data: {str(e)}"
        products = []

    if not error and product_id is not None:
        filtered = [p for p in products if p["id"] == product_id]
        if not filtered:
            error = "Product not found."
            products = []
        else:
            products = filtered

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)