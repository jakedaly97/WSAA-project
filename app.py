# flask server that links to a DAO
# author: Jake Daly

from flask import Flask, request, jsonify, abort
from dao.event_dao import EventDAO  # Import the EventDAO class

app = Flask(__name__)

# Instantiate the EventDAO class
eventDAO = EventDAO()

@app.route('/')
def index():
    return "Hello, Event World!"

# Get all events
# curl http://127.0.0.1:5000/events
@app.route('/events', methods=['GET'])
def getall():
    return jsonify(eventDAO.getAll())

# Get event by ID
# curl http://127.0.0.1:5000/events/1
@app.route('/events/<int:id>', methods=['GET'])
def findbyid(id):
    return jsonify(eventDAO.findByID(id))

# Create a new event
# curl -X POST -d "{\"title\":\"Event Title\", \"date\":\"2025-06-01\", \"location\":\"City Park\", \"description\":\"A fun event!\"}" http://127.0.0.1:5000/events
@app.route('/events', methods=['POST'])
def create():
    # Read json from the body
    jsonstring = request.json
    event = {}

    if "title" not in jsonstring:
        abort(403)
    event["title"] = jsonstring["title"]
    
    if "date" not in jsonstring:
        abort(403)
    event["date"] = jsonstring["date"]
    
    if "location" not in jsonstring:
        abort(403)
    event["location"] = jsonstring["location"]
    
    if "description" not in jsonstring:
        abort(403)
    event["description"] = jsonstring["description"]
    
    return jsonify(eventDAO.create(event))

# Update an existing event
# curl -X PUT -d "{\"title\":\"Updated Event\", \"date\":\"2025-06-15\", \"location\":\"New Location\", \"description\":\"Updated details\"}" http://127.0.0.1:5000/events/1
@app.route('/events/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    event = {}

    if "title" in jsonstring:
        event["title"] = jsonstring["title"]
    if "date" in jsonstring:
        event["date"] = jsonstring["date"]
    if "location" in jsonstring:
        event["location"] = jsonstring["location"]
    if "description" in jsonstring:
        event["description"] = jsonstring["description"]
    
    return jsonify(eventDAO.update(id, event))

# Delete an event
# curl -X DELETE  http://127.0.0.1:5000/events/1
@app.route('/events/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(eventDAO.delete(id))

if __name__ == "__main__":
    app.run(debug=True)