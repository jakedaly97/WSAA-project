from flask import Flask, request, jsonify, abort
from eventDAO import eventDAO  # only change from bookDAO

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

# GET all
@app.route('/events', methods=['GET'])
def getAll():
    return jsonify(eventDAO.getAll())

# GET by ID
@app.route('/events/<int:id>', methods=['GET'])
def findById(id):
    return jsonify(eventDAO.findByID(id))

# CREATE
@app.route('/events', methods=['POST'])
def create():
    jsonstring = request.json
    event = {}

    if "name" not in jsonstring:
        abort(403)
    event["name"] = jsonstring["name"]

    if "location" not in jsonstring:
        abort(403)
    event["location"] = jsonstring["location"]

    if "date" not in jsonstring:
        abort(403)
    event["date"] = jsonstring["date"]

    if "genre" not in jsonstring:
        abort(403)
    event["genre"] = jsonstring["genre"]

    if "description" not in jsonstring:
        abort(403)
    event["description"] = jsonstring["description"]

    if "price" not in jsonstring:
        abort(403)
    event["price"] = jsonstring["price"]

    return jsonify(eventDAO.create(event))

# UPDATE
@app.route('/events/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    event = {}

    if "name" in jsonstring:
        event["name"] = jsonstring["name"]

    if "location" in jsonstring:
        event["location"] = jsonstring["location"]

    if "date" in jsonstring:
        event["date"] = jsonstring["date"]

    if "genre" in jsonstring:
        event["genre"] = jsonstring["genre"]

    if "description" in jsonstring:
        event["description"] = jsonstring["description"]

    if "price" in jsonstring:
        event["price"] = jsonstring["price"]

    return jsonify(eventDAO.update(id, event))

# DELETE
@app.route('/events/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(eventDAO.delete(id))

if __name__ == '__main__':
    app.run(debug=True)