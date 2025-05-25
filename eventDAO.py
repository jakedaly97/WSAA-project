# eventDAO.py
# Author: Jake Daly

import mysql.connector
import dbconfig as cfg

# Initialize class level variables
class EventDAO:
    connection = ""
    cursor = ''
    host = ''
    user = ''
    password = ''
    database = ''
    
    # Load details from the dbconfig file
    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    # Create new connection and cursor to the database
    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    # close cursor and connection
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
        
        
    # Retrieve all rows from the events table
    def getAll(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM events"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    # Find a single event by id
    def findByID(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM events WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    # insert new event into the events table
    def create(self, event):
        cursor = self.getcursor()
        sql = "INSERT INTO events (name, location, date, genre, description, price) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (event.get("name"), event.get("location"), event.get("date"), event.get("genre"), event.get("description"), event.get("price"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        event["id"] = newid
        self.closeAll()
        return event

    # Updates existing event
    def update(self, id, event):
        cursor = self.getcursor()
        sql = "UPDATE events SET name=%s, location=%s, date=%s, genre=%s, description=%s, price=%s WHERE id=%s"
        values = (event.get("name"), event.get("location"), event.get("date"), event.get("genre"), event.get("description"), event.get("price"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
    
    # Delete event by id
    def delete(self, id):
        cursor = self.getcursor()
        sql = "DELETE FROM events WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    # Convert a row from the database (tuple) to a dictionary
    def convertToDictionary(self, resultLine):
        attkeys=['id', 'name', 'location', 'date', 'genre', 'description', 'price']
        event = {}
        currentkey = 0
        for attrib in resultLine:
            event[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return event

eventDAO = EventDAO()

# Resource
# Pretty much identical to Andrews code found here with some minor changes i.e event instead of book, https://github.com/andrewbeattycourseware/deploytopythonanywhere/blob/main/bookDAO.py