from flask import Flask, jsonify, request, abort, send_from_directory
import os
app = Flask(__name__)

# Import the eventDAO for database operations
from eventDAO import eventDAO

@app.route('/')
def index():
    return send_from_directory('.', 'eventviewer.html')

#curl "http://127.0.0.1:5000/events"
@app.route('/events')
def getAll():
    # Retrieve all events from the database
    results = eventDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/events/2"
@app.route('/events/<int:id>')
def findById(id):
    # Retrieve a specific event by ID
    foundEvent = eventDAO.findByID(id)
    return jsonify(foundEvent)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"Concert\",\"location\":\"Stadium\",\"date\":\"2025-05-15\",\"genre\":\"Music\",\"description\":\"A great concert!\",\"price\":50}" http://127.0.0.1:5000/events
@app.route('/events', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    # Retrieve data from the request
    event = {
        "name": request.json['name'],
        "location": request.json['location'],
        "date": request.json['date'],
        "genre": request.json['genre'],
        "description": request.json['description'],
        "price": request.json['price'],
    }

    # Add the event to the database
    addedEvent = eventDAO.create(event)
    
    return jsonify(addedEvent)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"Updated Concert\",\"location\":\"Arena\",\"date\":\"2025-06-01\",\"genre\":\"Pop\",\"description\":\"Updated description\",\"price\":60}" http://127.0.0.1:5000/events/1
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

    # Update the event with the new values
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