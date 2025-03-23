from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    with open(json_path) as f:
        data = json.load(f)
        item_list = data.get("items", [])
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)