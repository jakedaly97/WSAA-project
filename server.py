from flask import Flask, jsonify, request, abort
from eventDAO import eventDAO  # Changed from bookDAO to eventDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/events')
def getAll():
    results = eventDAO.getAll()
    return jsonify(results)

@app.route('/events/<int:id>')
def findById(id):
    foundEvent = eventDAO.findByID(id)
    return jsonify(foundEvent)

@app.route('/events', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    event = {
        "name": request.json['name'],
        "location": request.json['location'],
        "date": request.json['date'],
        "genre": request.json['genre'],
        "description": request.json['description'],
        "price": request.json['price'],
    }
    addedEvent = eventDAO.create(event)
    return jsonify(addedEvent)

@app.route('/events/<int:id>', methods=['PUT'])
def update(id):
    foundEvent = eventDAO.findByID(id)
    if not foundEvent:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'name' in reqJson:
        foundEvent['name'] = reqJson['name']
    if 'location' in reqJson:
        foundEvent['location'] = reqJson['location']
    if 'date' in reqJson:
        foundEvent['date'] = reqJson['date']
    if 'genre' in reqJson:
        foundEvent['genre'] = reqJson['genre']
    if 'description' in reqJson:
        foundEvent['description'] = reqJson['description']
    if 'price' in reqJson:
        foundEvent['price'] = reqJson['price']
    
    eventDAO.update(id, foundEvent)
    return jsonify(foundEvent)

@app.route('/events/<int:id>', methods=['DELETE'])
def delete(id):
    eventDAO.delete(id)
    return jsonify({"done": True})

if __name__ == '__main__':
    app.run(debug=True)