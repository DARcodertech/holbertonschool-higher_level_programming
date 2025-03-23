from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_products(file_path):
    with open(file_path) as f:
        return json.load(f)

def read_csv_products(file_path):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products = []

    json_path = os.path.join(os.path.dirname(__file__), 'products.json')
    csv_path = os.path.join(os.path.dirname(__file__), 'products.csv')

    if source == "json":
        try:
            products = read_json_products(json_path)
        except Exception as e:
            error = f"Error reading JSON: {e}"
    elif source == "csv":
        try:
            products = read_csv_products(csv_path)
        except Exception as e:
            error = f"Error reading CSV: {e}"
    else:
        error = "Wrong source. Use 'json' or 'csv'."

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