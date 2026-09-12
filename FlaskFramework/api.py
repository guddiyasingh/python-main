### Put  and Delete
###Working with API's

from flask import Flask, jsonify, request
app = Flask(__name__)

## Initial Data in my to do list

items = [

    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome to The Sample To Do List App"

## Get: Retrieve all items

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

    
if __name__ == '__main__':
    app.run(debug=True)